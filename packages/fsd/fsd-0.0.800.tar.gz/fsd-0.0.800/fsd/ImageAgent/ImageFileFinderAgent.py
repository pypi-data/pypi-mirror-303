import os
import aiohttp
import asyncio
import json
import sys
from json_repair import repair_json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from fsd.log.logger_config import get_logger
logger = get_logger(__name__)

class ImageFileFinderAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    def read_dependency_file_content(self, file_path):
        """
        Read the content of a dependency file.

        Args:
            file_path (str): Path to the dependency file to read.

        Returns:
            str: Content of the dependency file, or None if an error occurs.
        """
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            logger.debug(f" #### `ImageFileFinderAgent` encountered an issue while reading dependency file:\n{file_path}\nError: {e}")
            return None


    async def get_style_file_planning(self, tree):
        """
        Request dependency file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            idea (str): The general plan idea.
            tree (str): The project structure.

        Returns:
            dict: JSON response with the dependency file plan.
        """

        prompt = (
            f"Identify main color and style files in the project structure:\n"
            "1. Include: Main style files, key config files, UI libraries, color/theme files.\n"
            "2. Exclude: Third-party, external, generated files.\n"
            "3. Focus on root and key subdirectory files impacting main styling.\n"
            "4. If no clear style file, find potential relevant files.\n\n"
            "Return ONLY this JSON:\n"
            "{\n"
            f"    \"style_files\": [\"{self.repo.get_repo_path()}/path/file1.ext\", \"{self.repo.get_repo_path()}/path/file2.ext\"]\n"
            "}\n"
            "Ensure valid, parseable JSON with full file paths. No extra text or formatting."
        )

        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": f"This is the current project structure:\n{tree}\n"
            }
        ]

        try:
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.debug(f" #### `ImageFileFinderAgent` failed to obtain dependency file planning:\nError: {e}")
            return {
                "reason": str(e)
            }


    async def get_style_file_plannings(self):
        """
        Request dependency file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (list): List of file paths representing the project structure.

        Returns:
            dict: JSON response with the dependency file plan.
        """
        logger.debug("\n #### `ImageFileFinderAgent` is initiating the style file planning process")
        all_tree_file_contents = self.repo.print_tree()
        plan = await self.get_style_file_planning(all_tree_file_contents)
        logger.debug("\n #### `ImageFileFinderAgent` has successfully completed the style file planning")
        return plan
