import os
import aiohttp
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from json_repair import repair_json
from fsd.log.logger_config import get_logger
from fsd.util.utils import read_file_content

logger = get_logger(__name__)

class TaskErrorPlanner:
    """
    A class to plan and manage tasks using AI-powered assistance, including error handling and suggestions.
    """

    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_task_plan(self, error, config_context, os_architecture, compile_files, original_prompt_language):
        """
        Get a dependency installation plan based on the error, config context, and OS architecture using AI.

        Args:
            error (str): The error message encountered during dependency installation.
            config_context (str): The configuration context of the project, including what is being built.
            os_architecture (str): The operating system and architecture of the target environment.
            compile_files (list): List of files to be checked for configuration issues.

        Returns:
            dict: Dependency installation plan or error reason.
        """

        all_file_contents = ""

        files_paths = compile_files

        if files_paths:
            for file_path in files_paths:
                file_content = read_file_content(file_path)
                if file_content:
                    all_file_contents += f"\n\nFile: {file_path}:\n{file_content}"
        else:
            all_file_contents = "No related files found."


        tree = self.repo.print_tree()


        messages = [
            {
                "role": "system",
                "content": (
                    "As a principal DevOps engineer, create a concise, step-by-step dependency installation/build configuration plan. Follow these guidelines:\n\n"
                    "1. Analyze the error and suggest fixes.\n"
                    "2. Organize steps logically, starting with foundational components.\n"
                    "3. Consider the OS architecture for commands.\n"
                    "4. Provide detailed, executable commands.\n"
                    "5. Check configuration files for issues.\n"
                    "6. All 'cd' commands must always be in separate steps, DO NOT combine with other commands.\n\n"
                    "For each task, include:\n"
                    f"- file_name: Full path of the config file or 'N/A' for bash commands. Use {self.repo.get_repo_path()} as the project directory.\n"
                    "- error_resolution: Specific instruction for the task.\n"
                    "- method: 'update' for file modifications or 'bash' for terminal commands.\n"
                    "- command: Exact command to execute (for 'bash' method only).\n"
                    "Respond with a valid JSON in this format without additional text or symbols or MARKDOWN:\n"
                    "{\n"
                    '    "steps": [\n'
                    '        {\n'
                    '            "file_name": "",\n'
                    '            "method": "",\n'
                    '            "command": "",\n'
                    f'            "error_resolution": ""\n'
                    '        }\n'
                    '    ]\n'
                    "}\n\n"
                    "Provide only the JSON response."
                )
            },
            {
                "role": "user",
                "content": f"Create a focused plan to resolve this error:\n\n"
                           f"0. Tree structure: {tree}\n"
                           f"1. Config Context: {config_context}\n"
                           f"2. Error: {error}\n"
                           f"3. OS Architecture: {os_architecture}\n"
                           f"4. Configuration Files:\n{all_file_contents}\n\n"
                           f"Provide specific commands. Only include dependency configuration and installation steps. "
                           f"Check all files for misconfigurations. Address the error considering the architecture and build context. "
                           f"Remember, all 'cd' commands must be in separate steps and not combined with other commands. "
                           f"Respond using the language: {original_prompt_language}"
            }
        ]

        try:
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            res = json.loads(response.choices[0].message.content)
            return res
        except json.JSONDecodeError:
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.error(f" #### The `TaskErrorPlanner` agent encountered an error:\n Failed to get task plan\n Error: {e}")
            return {"reason": str(e)}

    async def get_task_plans(self, error, config_context, os_architecture, compile_files, original_prompt_language):
        """
        Get development plans based on the error, config context, and OS architecture.

        Args:
            error (str): The error message encountered during dependency installation.
            config_context (str): The configuration context of the project.
            os_architecture (str): The operating system and architecture of the target environment.

        Returns:
            dict: Development plan or error reason.
        """
        plan = await self.get_task_plan(error, config_context, os_architecture, compile_files, original_prompt_language)
        return plan
