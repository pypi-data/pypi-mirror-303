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

class CompileFileFinderAgent:
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
            logger.debug(f" #### `CompileFileFinderAgent` encountered an error while reading dependency file:\n{file_path}\nError: {e}")
            return None


    async def get_compile_file_planning(self, userRequest, tree):
        """
        Request compile file planning from Azure OpenAI API for a given project structure.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            userRequest (str): The user's request or context.
            tree (str): The project structure.

        Returns:
            dict: JSON response with the compile file plan.
        """
        prompt = (
            "Identify MAIN files crucial for compilation, running, and build processes:\n"
            "1. INCLUDE: Main dependency, entry point, configuration, build script, and environment files\n"
            "2. EXCLUDE: Third-party libraries, generated folders, IDE-specific folders, dependency caches\n"
            "3. FOCUS ON: Main entry points, primary build scripts, core configuration files\n"
            "4. CONSIDER: Project-specific main files impacting compilation or runtime\n\n"
            "IMPORTANT: Carefully examine the provided project structure. Only include files that actually exist in the tree.\n"
            "Do not invent or hallucinate files that are not present in the given structure.\n\n"
            "CRITICAL: Never include long, unnecessary files such as package-lock.json, yarn.lock, Podfile.lock, Gemfile.lock, poetry.lock, composer.lock, cargo.lock, etc.\n"
            "This applies to all types of projects including but not limited to: Node.js, Python, Ruby, Java, Kotlin, Swift, C#, Go, Rust, PHP, and any other programming language or framework.\n\n"
            "Respond with ONLY a valid JSON object without additional text or symbols or MARKDOWN:\n"
            "{\n"
            "    \"crucial_files\": [\"full/path/to/file1.extension\", \"full/path/to/file2.extension\", ...]\n"
            "}\n"
            f"CRITICAL: Return ONLY parseable JSON with full paths. Project location: {self.repo.get_repo_path()}\n"
            "If no crucial files are found, return an empty list for 'crucial_files'."
        )

        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": f"User Request: {userRequest}\nThis is the current project structure:\n{tree}\n"
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
            logger.error(f" #### `CompileFileFinderAgent` failed to obtain dependency file planning:\nError: {e}")
            return {
                "reason": str(e)
            }


    async def get_compile_file_plannings(self, userRequest):
        """
        Request dependency file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            idea (str): The general plan idea.
            tree (list): List of file paths representing the project structure.

        Returns:
            dict: JSON response with the dependency file plan.
        """
        logger.debug("\n #### `CompileFileFinderAgent` is initiating the file processing task")
        all_dependency_file_contents = self.repo.print_tree()

        plan = await self.get_compile_file_planning(userRequest, all_dependency_file_contents)
        logger.debug("\n #### `CompileFileFinderAgent` has successfully completed the file processing task")
        return plan
