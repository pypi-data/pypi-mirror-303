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

class DependencyPrePromptAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_prePrompt_plan(self, user_prompt):
        """
        Get a development plan for all txt files from Azure OpenAI based on the user prompt.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            all_file_contents (str): The concatenated contents of all files.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Development plan or error reason.
        """
        all_file_contents = self.repo.print_tree()
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a DevOps expert who knows a lot about managing dependencies. Look at the project files and what the user wants, then give a detailed answer in JSON format. Follow these important rules:\n\n"
                    "install_plan: Change the user's request into clear instructions about installing dependencies. If it's not in English, translate it well. Add useful information about dependencies from the project. Your instructions should guide another AI on how to install dependencies. If pipeline is 2, tell the AI which tool to use (like CocoaPods, npm, or pip). Give examples to make it clear. Do not include any information about AI models.\n"
                    "pipeline: Choose the best action. Answer with 0, 1, or 2 based on these rules:\n"
                    "For handling dependencies:\n"
                    "0. Do nothing: Use this when the user doesn't mention installing or updating any dependencies.\n"
                    "1. Need expert help: Use this when the user specifically talks about using an IDE for installation. Explain why command-line tools can't be used.\n"
                    "2. Can be done with CLI: Use this for all other cases. Try to use command-line tools for all dependency installations, even if the user didn't mention them. This includes all package managers like CocoaPods, npm, pip, etc.\n"
                    "explainer: For pipeline 1, explain in detail why automatic installation won't work. For pipeline 2, just list the dependencies to install, their versions (use latest if not specified), and which command-line tool to use. Only include important warnings if necessary. Write this explanation in the user's language.\n"
                    "Your JSON answer should look like this:\n\n"
                    "{\n"
                    '    "install_plan": "Detailed instructions for dependency installation, ignore integration parts",\n'
                    '    "pipeline": "0, 1, or 2",\n'
                    '    "explainer": ""\n'
                    "}\n\n"
                    "Make sure your answer is a properly formatted JSON object without any extra text or comments. Focus only on installing and managing dependencies. When providing bash commands, use nice formatting in markdown, like this:\n\n"
                    "```bash\n"
                    "npm install package-name\n"
                    "```"
                )
            },
            {
                "role": "user",
                "content": (
                    f"Important project information:\n{all_file_contents}\n\n"
                    f"What the user wants:\n{user_prompt}\n"
                )
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
            logger.error(f" #### The `DependencyPrePromptAgent` encountered an error\n Error: {e}")
            return {
                "reason": str(e)
            }

    async def get_prePrompt_plans(self, user_prompt):
        """
        Get development plans for a list of txt files from Azure OpenAI based on the user prompt.

        Args:
            files (list): List of file paths.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Development plan or error reason.
        """
        plan = await self.get_prePrompt_plan(user_prompt)
        return plan
