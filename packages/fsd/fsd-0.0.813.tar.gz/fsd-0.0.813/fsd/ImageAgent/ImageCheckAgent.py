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

class ImageCheckAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_image_check_plan(self, user_prompt):
        """
        Get a plan for image generation based on the user prompt.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            all_file_contents (str): The concatenated contents of all files.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Image generation plan or error reason.
        """

        messages = [
            {
                "role": "system",
                "content": (
                    "Carefully analyze the user's request to determine if it involves generating, creating, or producing any NEW png, jpg, jpeg, PNG, JPG, JPEG, or .ico images. ONLY for NEW image generation demand. Ignore any mentions of modifying existing images, moving images, or any other image-related tasks that don't involve creating new images. Return '1' if any new images of these types are required to be generated, even if the need is implied rather than directly stated. Return '0' only if you are absolutely certain that no new images of these types need to be generated. Respond in this exact JSON format:\n"
                    "{\n"
                    '    "result": ""\n'
                    "}"
                )
            },
            {
                "role": "user",
                "content": f"Check if ANY NEW PNG, png, JPG, jpg, JPEG, jpeg, or .ico images, No other types of images are allowed. {user_prompt}"
            }
        ]

        try:
            logger.debug("\n #### The `ImageCheckAgent` is initiating a request to the AI Gateway")
            response = await self.ai.prompt(messages, self.max_tokens, 0, 0)
            res = json.loads(response.choices[0].message.content)
            logger.debug("\n #### The `ImageCheckAgent` has successfully parsed the AI response")
            return res
        except json.JSONDecodeError:
            logger.debug("\n #### The `ImageCheckAgent` encountered a JSON decoding error and is attempting to repair it")
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            logger.debug("\n #### The `ImageCheckAgent` has successfully repaired and parsed the JSON")
            return plan_json
        except Exception as e:
            logger.error(f" #### The `ImageCheckAgent` encountered an error during the process: `{e}`")
            return {
                "reason": str(e)
            }

    async def get_image_check_plans(self, user_prompt):
        """
        Get image generation plans based on the user prompt.

        Args:
            files (list): List of file paths.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Image generation plan or error reason.
        """
        logger.debug("\n #### The `ImageCheckAgent` is beginning to retrieve image check plans")
        plan = await self.get_image_check_plan(user_prompt)
        logger.debug("\n #### The `ImageCheckAgent` has successfully retrieved image check plans")
        return plan
