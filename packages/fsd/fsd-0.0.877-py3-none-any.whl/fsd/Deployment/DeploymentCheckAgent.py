import os
import aiohttp
import asyncio
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from util.portkey import AIGateway
from json_repair import repair_json
from log.logger_config import get_logger
from fsd.util.utils import read_file_content
logger = get_logger(__name__)

class DeploymentCheckAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_deployment_check_plan(self):
        """
        Get a development plan for all txt files from Azure OpenAI based on the user prompt.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            all_file_contents (str): The concatenated contents of all files.

        Returns:
            dict: Development plan or error reason.
        """
        messages = [
            {
                "role": "system",
                "content": (
                    "Check if the current project is eligible for deployment as a static HTML/CSS website. "
                    "The project is eligible if you can see there's an index.html file in the project folder. "
                    f"The root path: {self.repo.get_repo_path()}. "
                    "Here's the project structure:\n"
                    f"{self.repo.print_tree()}\n\n"
                    "Example of an eligible project structure:\n"
                    "project_root/\n"
                    "├── index.html\n"
                    "├── css/\n"
                    "│   └── styles.css\n"
                    "├── js/\n"
                    "│   └── script.js\n"
                    "└── images/\n"
                    "    └── logo.png\n\n"
                    "Respond in this exact JSON format:\n"
                    "{\n"
                    '    "result": "0" or "1",\n'
                    '    "full_project_path": "full/path/to/project_folder_containing_index.html" or null\n'
                    "}\n"
                    "Where 'result' is '1' if eligible (index.html found in root), '0' if not. "
                    "'full_project_path' must be the full path including the project folder name that contains index.html at the root level, or null if not found."
                )
            },
            {
                "role": "user",
                "content": "Check if this project is eligible for deployment and return full path for deploy folder."
            }
        ]

        try:
            logger.debug("\n #### The `DeploymentCheckAgent` is initiating a request to the AI Gateway")
            response = await self.ai.prompt(messages, self.max_tokens, 0, 0)
            res = json.loads(response.choices[0].message.content)
            logger.debug("\n #### The `DeploymentCheckAgent` has successfully parsed the AI response")
            return res
        except json.JSONDecodeError:
            logger.debug("\n #### The `DeploymentCheckAgent` encountered a JSON decoding error and is attempting to repair it")
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            logger.debug("\n #### The `DeploymentCheckAgent` has successfully repaired and parsed the JSON")
            return plan_json
        except Exception as e:
            logger.error(f" #### The `DeploymentCheckAgent` encountered an error during the process: `{e}`")
            return {
                "reason": str(e)
            }

    async def get_deployment_check_plans(self):
        """
        Get development plans for a list of txt files from Azure OpenAI based on the user prompt.

        Args:
            files (list): List of file paths.

        Returns:
            dict: Development plan or error reason.
        """
        logger.debug("\n #### The `DeploymentCheckAgent` is beginning to retrieve deployment check plans")
        plan = await self.get_deployment_check_plan()
        logger.debug("\n #### The `DeploymentCheckAgent` has successfully retrieved deployment check plans")
        return plan
