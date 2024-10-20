import os
import sys
import asyncio
import re
import aiohttp
import json
from datetime import datetime

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from json_repair import repair_json
from fsd.log.logger_config import get_logger
from fsd.system.FileContentManager import FileContentManager
from fsd.util.utils import read_file_content
logger = get_logger(__name__)

class SelfHealingAgent:

    def __init__(self, repo):
        self.repo = repo
        self.conversation_history = []
        self.code_manager = FileContentManager()  # Initialize CodeManager in the constructor
        self.ai = AIGateway()

    def get_current_time_formatted(self):
        """Get the current time formatted as mm/dd/yy."""
        current_time = datetime.now()
        formatted_time = current_time.strftime("%m/%d/%y")
        return formatted_time

    def clear_conversation_history(self):
        """Clear the conversation history."""
        self.conversation_history = []

    def initial_setup(self, role):
        """
        Initialize the conversation with a system prompt and user context.
        """
        prompt = f"""You are a senior {role} working as a bug fixing agent. You will receive detailed instructions to work on. Follow these guidelines strictly:
                1. For ALL code changes, additions, or deletions, you MUST ALWAYS use the following *SEARCH/REPLACE block* format:

                   <<<<<<< SEARCH
                   [Existing code to be replaced, if any]
                   =======
                   [New or modified code]
                   >>>>>>> REPLACE

                2. For new code additions, use an empty SEARCH section:

                   <<<<<<< SEARCH
                   =======
                   [New code to be added]
                   >>>>>>> REPLACE

                3. Ensure that the SEARCH section exactly matches the existing code, including whitespace and comments.

                4. For large files, focus on the relevant sections. Use comments to indicate skipped portions:
                   // ... existing code ...

                5. For complex changes or large files, break them into multiple SEARCH/REPLACE blocks.

                6. CRITICAL: NEVER provide code snippets, suggestions, or examples outside of the SEARCH/REPLACE block format. ALL code must be within these blocks.

                7. Do not provide explanations, ask questions, or engage in discussions. Only return SEARCH/REPLACE blocks.

                8. If a user's request cannot be addressed solely through SEARCH/REPLACE blocks, do not respond.

                Remember, your responses should ONLY contain SEARCH/REPLACE blocks for code changes. Nothing else is allowed.
        """

        self.conversation_history.append({"role": "system", "content": prompt})

    def read_all_file_content(self, all_path):
        """
        Read the content of all specified files.

        Args:
            all_path (list): List of file paths.

        Returns:
            str: Concatenated content of all files.
        """
        all_context = ""

        for path in all_path:
            file_context = read_file_content(path)
            all_context += f"\n\nFile: {path}\n{file_context}"

        return all_context

    async def get_fixing_request(self, instruction, file_content, all_file_content, tech_stack):
        """
        Get fixing response for the given instruction and context from Azure OpenAI.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            instruction (str): The fixing instructions.
            file_content (str): The content of the file to be fixed.
            all_file_content (str): The content of all related files.

        Returns:
            dict: Fixing response or error reason.
        """

        prompt = ""

        if all_file_content != "":
            prompt = (
                f"Current damaged file:\n{file_content}\n\n"
                f"Related files context:\n{all_file_content}\n\n"
                f"Follow this instructions:\n{instruction}\n\n"
                f"Please strictly follow the exact syntax and formatting for {tech_stack}\n\n"
                f"Always keep the file default description for {tech_stack}.\n"
                f"Tree:\n{self.repo.print_tree()}\n\n"
                "For any mockup or placeholder data you create, label it clearly as mock information so readers can identify it.\n"
                "Remember, your responses should ONLY contain SEARCH/REPLACE blocks for code changes. Nothing else is allowed."
            )
        else:
            prompt = (
                f"Current damaged file:\n{file_content}\n\n"
                f"Follow this instructions:\n{instruction}\n\n"
                f"Please strictly follow the exact syntax and formatting for {tech_stack}\n\n"
                f"Always keep the file default description for {tech_stack}.\n"
                f"Tree:\n{self.repo.print_tree()}\n\n"
                 "For any mockup or placeholder data you create, label it clearly as mock information so readers can identify it.\n"
                "Remember, your responses should ONLY contain SEARCH/REPLACE blocks for code changes. Nothing else is allowed."
            )

        self.conversation_history.append({"role": "user", "content": prompt})

        try:
            response = await self.ai.coding_prompt(self.conversation_history, 4096, 0, 0)
            self.conversation_history.pop()
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f" #### The `SelfHealingAgent` encountered an error during the fixing request: {e}")
            return {
                "reason": str(e)
            }

    async def get_fixing_requests(self, instructions):
        """
        Get fixing responses for a list of instructions from Azure OpenAI based on user prompt.

        Args:
            instructions (list): List of instructions for fixing bugs.

        Returns:
            dict: Fixing response or error reason.
        """
        for instruction in instructions:
            file_name = instruction['file_name']
            tech_stack = instruction['tech_stack']
            list_related_file_name = instruction['list_related_file_name']
            all_comprehensive_solutions_for_each_bugs = instruction['all_comprehensive_solutions_for_each_bug']
            if file_name in list_related_file_name:
                list_related_file_name.remove(file_name)

            if len(list_related_file_name) == 0:
                main_path = file_name
                file_content = read_file_content(main_path)
                logger.info(f"\n #### The `Self-Healing Agent` is initiating work on: `{instruction['Solution_detail_title']}`")
                result = await self.get_fixing_request(all_comprehensive_solutions_for_each_bugs, file_content, "", tech_stack)
                await self.replace_all_code_in_file(main_path, result)
                logger.info(f"\n #### The `Self-Healing Agent` has completed tasks for: `{instruction['Solution_detail_title']}`.")
            else:
                main_path = file_name
                all_path = list_related_file_name
                file_content = read_file_content(main_path)
                all_file_content = self.read_all_file_content(all_path)
                logger.info(f"\n #### The `Self-Healing Agent` is beginning work on: `{instruction['Solution_detail_title']}`.")
                result = await self.get_fixing_request(all_comprehensive_solutions_for_each_bugs, file_content, all_file_content, tech_stack)
                await self.replace_all_code_in_file(main_path, result)
                logger.info(f"\n #### The `Self-Healing Agent` has successfully completed tasks for: `{instruction['Solution_detail_title']}`.")

    async def replace_all_code_in_file(self, file_path, result):
        """
        Replace the entire content of a file with the new code snippet.

        Args:
            file_path (str): Path to the file.
            new_code_snippet (str): New code to replace the current content.
        """
        if file_path:
            await self.code_manager.handle_coding_agent_response(file_path, result)
        else:
            logger.debug(f" #### The `SelfHealingAgent` could not locate the file: `{file_path}`")
