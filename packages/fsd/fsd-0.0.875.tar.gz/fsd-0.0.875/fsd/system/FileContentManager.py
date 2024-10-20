import re
import aiofiles
import os
import mimetypes
from typing import List, Tuple, Optional
from fsd.log.logger_config import get_logger
import PyPDF2
import docx
import chardet
import openpyxl
import io
import difflib

logger = get_logger(__name__)

class FileContentManager:
    @staticmethod
    async def read_file(file_path: str) -> str:
        """
        Read and return the content of any type of file asynchronously, including special files like PDFs,
        DOCs, XLSX, and all code file types.

        Args:
            file_path (str): Full path to the file.

        Returns:
            str: Content of the file or empty string if file doesn't exist or can't be read.
        """
        if not os.path.exists(file_path):
            logger.debug(f"File does not exist: {file_path}")
            return ""

        mime_type, _ = mimetypes.guess_type(file_path)

        try:
            # Handle PDF files
            if mime_type == 'application/pdf':
                async with aiofiles.open(file_path, 'rb') as file:
                    content = await file.read()
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(content))
                text_content = []
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text:
                        text_content.append(text)
                return '\n'.join(text_content)

            # Handle DOC and DOCX files
            elif mime_type in [
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ]:
                async with aiofiles.open(file_path, 'rb') as file:
                    content = await file.read()
                doc = docx.Document(io.BytesIO(content))
                return '\n'.join(paragraph.text for paragraph in doc.paragraphs)

            # Handle XLSX (Excel) files
            elif mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                async with aiofiles.open(file_path, 'rb') as file:
                    content = await file.read()
                workbook = openpyxl.load_workbook(io.BytesIO(content), data_only=True)
                sheet = workbook.active  # Read the first sheet
                data = []
                for row in sheet.iter_rows(values_only=True):
                    data.append('\t'.join([str(cell) if cell is not None else "" for cell in row]))
                return '\n'.join(data)

            # Handle text and code files
            else:
                # Attempt to read as UTF-8 first
                try:
                    async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
                        return await file.read()
                except UnicodeDecodeError:
                    # If UTF-8 fails, detect encoding
                    async with aiofiles.open(file_path, 'rb') as file:
                        raw_data = await file.read()
                    detected = chardet.detect(raw_data)
                    encoding = detected['encoding'] if detected['encoding'] else 'utf-8'
                    async with aiofiles.open(file_path, 'r', encoding=encoding, errors='replace') as file:
                        return await file.read()

        except Exception as e:
            logger.exception(f"Failed to read file {file_path}: {e}")
            return ""

    @staticmethod
    async def write_file(file_path: str, content: str):
        """Write content to the file asynchronously."""
        try:
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
                logger.debug(f" #### The `file manager agent` has created a new directory: `{directory}` for the file: `{file_path}`")
            
            async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
                await file.write(content)
            
            if not os.path.exists(file_path):
                logger.debug(f" #### The `file manager agent` has successfully created a new file: `{file_path}`")
            else:
                logger.debug(f" #### The `file manager agent` has successfully updated the file: `{file_path}`")
        except Exception as e:
            logger.error(f" #### The `file manager agent` encountered an error while writing to file `{file_path}`. Error details: `{e}`")

    @staticmethod
    def parse_search_replace_blocks(response: str) -> List[Tuple[str, str]]:
        """
        Parses a response string for single or multiple SEARCH/REPLACE blocks,
        returning search and replace content as tuples.
        """
        # Regular expression pattern to capture multiple SEARCH/REPLACE blocks
        pattern = r'<<<<<<< SEARCH\n(.*?)=======\n(.*?)>>>>>>> REPLACE'

        # Find all matches in the response
        matches = re.findall(pattern, response, re.DOTALL)

        # Raise an error if no blocks are found
        if not matches:
            raise ValueError("No valid SEARCH/REPLACE blocks found in the input.")

        blocks = []
        for search, replace in matches:
            # Strip any extra spaces or newlines for cleanliness
            search = search.strip()
            replace = replace.strip()

            # Append the search and replace blocks as a tuple
            blocks.append((search, replace))

        return blocks

    @staticmethod
    def create_pattern_from_search(search: str) -> str:
        """
        Create a regex pattern from the search string where any whitespace sequences are replaced with \s+.
        """
        # Split the search string into parts, separating by whitespace
        parts = re.split(r'(\s+)', search)
        # For each part, if it is whitespace, replace with \s+, else escape it
        pattern = ''.join(
            (r'\s+' if s.isspace() else re.escape(s)) for s in parts
        )
        return pattern

    @classmethod
    async def apply_changes(cls, file_path: str, blocks: List[Tuple[str, str]]) -> str:
        """Apply the changes from SEARCH/REPLACE blocks to the file content."""
        content = await cls.read_file(file_path)
        original_content = content  # Keep a copy of the original content for logging

        for search, replace in blocks:
            if search:
                new_content = cls.replace_content(content, search, replace)
                if new_content is None:
                    logger.error(f" #### The `file manager agent` couldn't find a match for search block in file: `{file_path}`")
                    similar_lines = cls.find_similar_lines(search, content)
                    if similar_lines:
                        logger.debug(f"Did you mean to match these lines in `{file_path}`?\n{similar_lines}")
                    continue
                else:
                    content = new_content
            else:
                # Append the replace content if search is empty
                content += f"{replace}"
        
        if content != original_content:
            logger.debug(f" #### The `file manager agent` has successfully applied changes to the content of file: `{file_path}`")
        else:
            logger.info(f" #### The `file manager agent` did not make any changes to the file: `{file_path}`")
        return content

    @staticmethod
    def replace_content(content: str, search: str, replace: str) -> Optional[str]:
        """
        Replace the search block with the replace block in the content.
        Attempts exact match first, then normalizes whitespace, and finally uses regex pattern matching.
        """
        # Attempt exact match
        if search in content:
            return content.replace(search, replace)
        
        # Normalize whitespace in both search and content
        def normalize(text):
            return re.sub(r'\s+', ' ', text).strip()
        
        content_normalized = normalize(content)
        search_normalized = normalize(search)

        if search_normalized in content_normalized:
            # Create a regex pattern that matches any amount of whitespace where the search has whitespace
            pattern = FileContentManager.create_pattern_from_search(search)
            try:
                new_content, count = re.subn(pattern, replace, content, flags=re.DOTALL)
                if count > 0:
                    return new_content
            except re.error as e:
                logger.error(f"Regex error: {e}")
                return None

        # Use fuzzy matching
        new_content = FileContentManager.fuzzy_replace(content, search, replace)
        return new_content

    @staticmethod
    def fuzzy_replace(content: str, search: str, replace: str, threshold: float = 0.6) -> Optional[str]:
        """
        Attempt to replace the search block in content with replace block using fuzzy matching.
        """
        content_lines = content.splitlines(keepends=True)
        search_lines = search.splitlines(keepends=True)
        content_text = ''.join(content_lines)
        search_text = ''.join(search_lines)

        sequence_matcher = difflib.SequenceMatcher(None, content_text, search_text)
        match = sequence_matcher.find_longest_match(0, len(content_text), 0, len(search_text))

        if match.size == 0:
            return None

        similarity = match.size / len(search_text)
        if similarity >= threshold:
            # Perform the replacement
            start, end = match.a, match.a + match.size
            new_content = content_text[:start] + replace + content_text[end:]
            return new_content

        return None

    @staticmethod
    def find_similar_lines(search: str, content: str, num_lines: int = 5) -> str:
        """
        Find lines in content that are similar to the search block.
        """
        search_lines = search.splitlines()
        content_lines = content.splitlines()

        matcher = difflib.SequenceMatcher(None, search_lines, content_lines)
        blocks = matcher.get_matching_blocks()

        similar_snippets = []
        for block in blocks:
            if block.size > 0:
                start = max(0, block.b - num_lines)
                end = min(len(content_lines), block.b + block.size + num_lines)
                snippet = '\n'.join(content_lines[start:end])
                similar_snippets.append(snippet)

        return '\n\n'.join(similar_snippets)

    @classmethod
    async def process_coding_agent_response(cls, file_path: str, coding_agent_response: str):
        """Process the coding agent response and automatically apply changes to the file."""
        try:
            blocks = cls.parse_search_replace_blocks(coding_agent_response)
        except ValueError as e:
            logger.error(f" #### The `file manager agent` found no valid SEARCH/REPLACE blocks in the coding agent response for file: `{file_path}`")
            return

        new_content = await cls.apply_changes(file_path, blocks)
        await cls.write_file(file_path, new_content)
        logger.debug(f" #### The `file manager agent` has automatically applied changes to file: `{file_path}`")

    @classmethod
    async def handle_coding_agent_response(cls, file_path: str, coding_agent_response: str):
        """Main method to handle coding agent responses and automatically manage code changes for a single file."""
        logger.debug(coding_agent_response)
        try:
            await cls.process_coding_agent_response(file_path, coding_agent_response)
            logger.debug(f" #### The `file manager agent` has successfully processed the coding agent response for file: `{file_path}`")
        except Exception as e:
            logger.error(f" #### The `file manager agent` encountered an error while processing the coding agent response for file `{file_path}`. Error details: `{e}`")
