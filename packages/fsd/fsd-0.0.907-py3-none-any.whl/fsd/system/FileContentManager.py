import re
import aiofiles
import os
import mimetypes
from typing import List, Tuple, Optional, Dict
from fsd.log.logger_config import get_logger
import PyPDF2
import docx
import chardet
import openpyxl
import io
import difflib
from pathlib import Path
import math
from fsd.util.utils import send_error_to_api

logger = get_logger(__name__)

class FileContentManager:
    # Delimiters for SEARCH/REPLACE blocks
    HEAD = "<<<<<<< SEARCH"
    DIVIDER = "======="
    UPDATED = ">>>>>>> REPLACE"
    DEFAULT_FENCE = ("```", "```")  # Not used currently, but kept for potential future enhancements
    SIMILARITY_THRESHOLD = 0.6  # Configurable threshold for fuzzy matching

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
            error_message = f"Failed to read file {file_path}: {e}"
            logger.exception(error_message)
            send_error_to_api(error_message, str(e))
            return ""

    @staticmethod
    async def write_file(file_path: str, content: str):
        """Write content to the file asynchronously."""
        try:
            directory = os.path.dirname(file_path)
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                logger.debug(f" #### The `file manager agent` has created a new directory: `{directory}` for the file: `{file_path}`")
            
            async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
                await file.write(content)
            
            logger.debug(f" #### The `file manager agent` has successfully written to the file: `{file_path}`")
        except Exception as e:
            error_message = f" #### The `file manager agent` encountered an error while writing to file `{file_path}`. Error details: `{e}`"
            logger.error(error_message)
            send_error_to_api(error_message, str(e))

    @staticmethod
    def parse_search_replace_blocks(response: str) -> List[Tuple[str, str]]:
        """
        Parses a response string for single or multiple SEARCH/REPLACE blocks,
        returning search and replace content as tuples.

        Args:
            response (str): The string containing SEARCH/REPLACE blocks.

        Returns:
            List[Tuple[str, str]]: A list of tuples where each tuple contains (search, replace).

        Raises:
            ValueError: If no valid SEARCH/REPLACE blocks are found.
        """
        # Regular expression pattern to capture multiple SEARCH/REPLACE blocks
        pattern = rf'^{re.escape(FileContentManager.HEAD)}\s*\n(.*?)\n^{re.escape(FileContentManager.DIVIDER)}\s*\n(.*?)\n^{re.escape(FileContentManager.UPDATED)}\s*$'

        # Find all matches in the response with MULTILINE and DOTALL flags
        matches = re.findall(pattern, response, re.MULTILINE | re.DOTALL)

        # Raise an error if no blocks are found
        if not matches:
            error_message = "No valid SEARCH/REPLACE blocks found in the input."
            logger.debug("No matches found with the current regex pattern.")
            logger.debug(f"Response Content:\n{response}")
            send_error_to_api(error_message, response)
            raise ValueError(error_message)

        blocks = []
        for search, replace in matches:
            # Strip any extra spaces or newlines for cleanliness
            search = search.strip()
            replace = replace.strip()

            # Append the search and replace blocks as a tuple
            blocks.append((search, replace))

        return blocks

    @classmethod
    def parse_search_replace_blocks_line_by_line(cls, response: str) -> List[Tuple[str, str]]:
        """
        Parses the response for SEARCH/REPLACE blocks using a line-by-line approach,
        allowing for more flexibility in block formatting.

        Args:
            response (str): The string containing SEARCH/REPLACE blocks.

        Returns:
            List[Tuple[str, str]]: A list of tuples where each tuple contains (search, replace).

        Raises:
            ValueError: If no valid SEARCH/REPLACE blocks are found.
        """
        blocks = []
        lines = response.splitlines()
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith(cls.HEAD):
                search_content = []
                replace_content = []
                i += 1
                # Collect search content
                while i < len(lines) and not lines[i].strip().startswith(cls.DIVIDER):
                    search_content.append(lines[i])
                    i += 1
                if i >= len(lines):
                    error_message = "Incomplete SEARCH/REPLACE block: Missing DIVIDER."
                    logger.error("SEARCH block not properly closed with DIVIDER.")
                    send_error_to_api(error_message, response)
                    raise ValueError(error_message)
                i += 1  # Skip the DIVIDER line
                # Collect replace content
                while i < len(lines) and not lines[i].strip().startswith(cls.UPDATED):
                    replace_content.append(lines[i])
                    i += 1
                if i >= len(lines):
                    error_message = "Incomplete SEARCH/REPLACE block: Missing UPDATED."
                    logger.error("REPLACE block not properly closed with UPDATED.")
                    send_error_to_api(error_message, response)
                    raise ValueError(error_message)
                i += 1  # Skip the UPDATED line
                # Append the block
                blocks.append((
                    "\n".join(search_content).strip(),
                    "\n".join(replace_content).strip()
                ))
            else:
                i += 1
        if not blocks:
            error_message = "No valid SEARCH/REPLACE blocks found in the input."
            logger.debug("No valid SEARCH/REPLACE blocks found using line-by-line parser.")
            logger.debug(f"Response Content:\n{response}")
            send_error_to_api(error_message, response)
            raise ValueError(error_message)
        return blocks

    @staticmethod
    def create_pattern_from_search(search: str) -> str:
        """
        Create a regex pattern from the search string where any whitespace sequences are replaced with \s+.

        Args:
            search (str): The search string.

        Returns:
            str: The regex pattern.
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
                    error_message = f" #### The `file manager agent` couldn't find a match for search block in file: `{file_path}`"
                    logger.error(error_message)
                    similar_lines = cls.find_similar_lines(search, content)
                    if similar_lines:
                        logger.debug(f"Did you mean to match these lines in `{file_path}`?\n{similar_lines}")
                    send_error_to_api(error_message, f"Search: {search}\nContent: {content}")
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
        Attempts exact match first, then handles whitespace discrepancies, and finally uses fuzzy matching.

        Args:
            content (str): The original content of the file.
            search (str): The search string.
            replace (str): The replace string.

        Returns:
            Optional[str]: The modified content if replacement is successful, else None.
        """
        # Attempt exact match
        if search in content:
            return content.replace(search, replace)
        
        # Attempt perfect replacement
        new_content = FileContentManager.perfect_replace(content, search, replace)
        if new_content:
            return new_content

        # Attempt whitespace-flexible replacement
        new_content = FileContentManager.replace_part_with_missing_leading_whitespace(content, search, replace)
        if new_content:
            return new_content

        # Attempt fuzzy matching
        new_content = FileContentManager.fuzzy_replace(content, search, replace)
        if new_content:
            return new_content

        # If all methods fail, return None
        error_message = "Failed to replace content"
        send_error_to_api(error_message, f"Search: {search}\nReplace: {replace}\nContent: {content}")
        return None

    @staticmethod
    def perfect_replace(whole: str, part: str, replace: str) -> Optional[str]:
        """
        Attempt to replace the exact match of part with replace in whole.

        Args:
            whole (str): The original content.
            part (str): The exact search string.
            replace (str): The replace string.

        Returns:
            Optional[str]: The modified content if replacement is successful, else None.
        """
        part_lines = part.splitlines(keepends=True)
        replace_lines = replace.splitlines(keepends=True)
        whole_lines = whole.splitlines(keepends=True)

        part_tup = tuple(part_lines)
        part_len = len(part_lines)

        for i in range(len(whole_lines) - part_len + 1):
            whole_tup = tuple(whole_lines[i : i + part_len])
            if part_tup == whole_tup:
                return "".join(whole_lines[:i] + replace_lines + whole_lines[i + part_len :])

        return None

    @staticmethod
    def replace_part_with_missing_leading_whitespace(whole: str, part: str, replace: str) -> Optional[str]:
        """
        Handle replacement when there are leading whitespace discrepancies between part and whole.

        Args:
            whole (str): The original content.
            part (str): The search string.
            replace (str): The replace string.

        Returns:
            Optional[str]: The modified content if replacement is successful, else None.
        """
        whole_lines = whole.splitlines(keepends=True)
        part_lines = part.splitlines(keepends=True)
        replace_lines = replace.splitlines(keepends=True)

        # Calculate the minimum leading whitespace to remove
        leading = [len(p) - len(p.lstrip()) for p in part_lines if p.strip()] + [
            len(r) - len(r.lstrip()) for r in replace_lines if r.strip()
        ]

        if leading:
            num_leading = min(leading)
            part_lines = [p[num_leading:] if p.strip() else p for p in part_lines]
            replace_lines = [r[num_leading:] if r.strip() else r for r in replace_lines]

        # Attempt to find and replace with adjusted whitespace
        part_tup = tuple(part_lines)
        part_len = len(part_lines)

        for i in range(len(whole_lines) - part_len + 1):
            whole_tup = tuple(whole_lines[i : i + part_len])
            if part_tup == whole_tup:
                # Determine the leading whitespace from the original content
                leading_whitespace_match = re.match(r'\s*', whole_lines[i])
                leading_whitespace = leading_whitespace_match.group() if leading_whitespace_match else ''
                adjusted_replace = [f"{leading_whitespace}{r.lstrip()}" if r.strip() else r for r in replace_lines]
                return "".join(whole_lines[:i] + adjusted_replace + whole_lines[i + part_len :])

        return None

    @staticmethod
    def fuzzy_replace(content: str, search: str, replace: str, threshold: float = 0.6) -> Optional[str]:
        """
        Attempt to replace the search block in content with replace block using fuzzy matching.

        Args:
            content (str): The original content.
            search (str): The search string.
            replace (str): The replace string.
            threshold (float): The similarity threshold for replacement.

        Returns:
            Optional[str]: The modified content if replacement is successful, else None.
        """
        content_lines = content.splitlines(keepends=True)
        search_lines = search.splitlines(keepends=True)
        replace_lines = replace.splitlines(keepends=True)

        best_ratio = 0
        best_match_start = -1
        best_match_end = -1

        part_len = len(search_lines)
        scale = 0.1
        min_len = max(1, math.floor(part_len * (1 - scale)))
        max_len = math.ceil(part_len * (1 + scale))

        for length in range(min_len, max_len + 1):
            for i in range(len(content_lines) - length + 1):
                chunk = content_lines[i : i + length]
                chunk_text = "".join(chunk)
                search_text = "".join(search_lines)

                similarity = difflib.SequenceMatcher(None, chunk_text, search_text).ratio()

                if similarity > best_ratio:
                    best_ratio = similarity
                    best_match_start = i
                    best_match_end = i + length

        if best_ratio >= threshold:
            new_content = (
                "".join(content_lines[:best_match_start]) +
                "".join(replace_lines) +
                "".join(content_lines[best_match_end:])
            )
            return new_content

        return None

    @classmethod
    def find_similar_lines(cls, search: str, content: str, num_lines: int = 5) -> str:
        """
        Find lines in content that are similar to the search block.

        Args:
            search (str): The search string.
            content (str): The original content.
            num_lines (int): Number of lines to include before and after the match for context.

        Returns:
            str: A string containing similar lines with context, or an empty string if no similar lines are found.
        """
        search_lines = search.splitlines()
        content_lines = content.splitlines()

        best_ratio = 0
        best_match = []
        best_match_index = -1

        for i in range(len(content_lines) - len(search_lines) + 1):
            chunk = content_lines[i : i + len(search_lines)]
            ratio = difflib.SequenceMatcher(None, search_lines, chunk).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = chunk
                best_match_index = i

        if best_ratio < cls.SIMILARITY_THRESHOLD:
            error_message = "No similar lines found"
            send_error_to_api(error_message, f"Search: {search}\nContent: {content}")
            return ""

        # Check if the matched chunk exactly matches the search lines
        if best_match and best_match[0] == search_lines[0] and best_match[-1] == search_lines[-1]:
            return "\n".join(best_match)

        # Provide context around the best match
        N = num_lines
        best_match_end = min(len(content_lines), best_match_index + len(search_lines) + N)
        best_match_start = max(0, best_match_index - N)

        best = content_lines[best_match_start:best_match_end]
        return "\n".join(best)

    @classmethod
    async def process_coding_agent_response(cls, file_path: str, coding_agent_response: str):
        """Process the coding agent response and automatically apply changes to the file."""
        try:
            # First, try regex-based parsing
            blocks = cls.parse_search_replace_blocks(coding_agent_response)
        except ValueError:
            logger.debug("Regex-based parsing failed. Attempting line-by-line parsing.")
            try:
                # Fallback to line-by-line parsing
                blocks = cls.parse_search_replace_blocks_line_by_line(coding_agent_response)
            except ValueError as e:
                error_message = f" #### The `file manager agent` found no valid SEARCH/REPLACE blocks in the coding agent response for file: `{file_path}`"
                logger.error(error_message)
                logger.debug(f"Error details: {e}")
                send_error_to_api(error_message, coding_agent_response)
                return

        new_content = await cls.apply_changes(file_path, blocks)
        await cls.write_file(file_path, new_content)
        logger.debug(f" #### The `file manager agent` has automatically applied changes to file: `{file_path}`")

    @classmethod
    async def handle_coding_agent_response(cls, file_path: str, coding_agent_response: str):
        """Main method to handle coding agent responses and automatically manage code changes for a single file."""
        logger.debug("Received coding agent response:")
        logger.debug(coding_agent_response)
        try:
            await cls.process_coding_agent_response(file_path, coding_agent_response)
            logger.debug(f" #### The `file manager agent` has successfully processed the coding agent response for file: `{file_path}`")
        except Exception as e:
            error_message = f" #### The `file manager agent` encountered an error while processing the coding agent response for file `{file_path}`. Error details: `{e}`"
            logger.error(error_message)
            send_error_to_api(error_message, coding_agent_response)
