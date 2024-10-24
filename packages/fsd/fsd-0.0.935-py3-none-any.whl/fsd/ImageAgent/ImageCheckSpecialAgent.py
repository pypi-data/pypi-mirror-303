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

class ImageCheckSpecialAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_image_check_plan(self, user_prompt, original_prompt_language):
        """
        Get an image check plan from Azure OpenAI based on the user prompt.

        Args:
            user_prompt (str): The user's prompt.
            original_prompt_language (str): The language to use for the response.

        Returns:
            dict: Image check plan or error reason.
        """
        messages = [
            {
                "role": "system",
                "content": (
                    f"STRICTLY analyze the user's request for ONLY NEW PNG, png, JPG, jpg, JPEG, jpeg, or .ico images that need to be GENERATED. EXCLUDE ALL OTHER IMAGE FORMATS AND ANY EXISTING IMAGES OR IMAGE MODIFICATIONS. For each new image to be generated, extract and return the following details in a markdown table format:\n\n"
                    "| Aspect | Detail description |\n"
                    "|--------|-------------|\n"
                    "| Image Name | [Exact name from development plan] |\n"
                    f"| File Path | [Full path starting with {self.repo.get_repo_path()} and STRICTLY using the EXACT relative path from development plan, INCLUDING ANY PROJECT FOLDER NAMES] |\n"
                    "| Description | [Detailed description for this new image, style and purpose of using] |\n"
                    "| Format | [PNG, JPG, JPEG, or ICO] |\n"
                    "| Dimensions | [Width x Height in pixels] |\n\n"
                    "DO NOT process or include any existing images, image modifications, or other types of assets. Respond ONLY with the extracted details for NEW PNG, JPG, JPEG, and .ico images that need to be generated.\n"
                    f"- Separate each image table clearly using a line of dashes (---------------------)\n"
                    "Use appropriate spacing to ensure the text is clear and easy to read.\n"
                    "Use clear headings (maximum size #### for h4) to organize your response.\n"
                    f"Provide the response in the following language: {original_prompt_language}\n"
                    "IMPORTANT:\n"
                    f"- File Path MUST be the full path, starting with the root path: {self.repo.get_repo_path()}\n"
                    "- Use ONLY the EXACT full paths for new images as specified in the development plan, appended to the root path\n"
                    "- DO NOT modify, guess, or create new paths for images under ANY circumstances\n"
                    "- STRICTLY adhere to the relative paths provided in the development plan\n"
                    "- ALWAYS INCLUDE project folder names (e.g., project1, project2, tic-tac-toe) if present in the instruction\n"
                    "- NEVER skip or omit project folder names in the file paths\n"
                    "- Provide full and detailed descriptions for each new image as mentioned in the development plan\n"
                    "- Include the dimensions (width x height) for each new image if specified in the development plan\n"
                    "- If the user request contains any image formats other than PNG, JPG, JPEG, or .ico, or any existing image operations, completely ignore and do not mention them in the response"
                )
            },
            {
                "role": "user",
                "content": f"INCLUDES ONLY NEW PNG, png, JPG, jpg, JPEG, jpeg, or .ico images. DO NOT INCLUDE ANY OTHER types of images such as svg. Identify images that need to be generated in this development plan: {user_prompt}"
            }
        ]

        response = await self.ai.arch_stream_prompt(messages, self.max_tokens, 0, 0)
        return response

    async def get_image_check_plans(self, user_prompt, original_prompt_language):
        """
        Get image check plans based on the user prompt.

        Args:
            user_prompt (str): The user's prompt.

        Returns:
            dict: Image check plan or error reason.
        """
        logger.debug(f" #### The `ImageCheckSpecialAgent` is initiating the image check plan generation\n User prompt: {user_prompt}")
        plan = await self.get_image_check_plan(user_prompt, original_prompt_language)
        logger.debug(f" #### The `ImageCheckSpecialAgent` has completed generating the image check plan")
        return plan
