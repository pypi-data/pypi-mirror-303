import os
import aiohttp
import asyncio
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from json_repair import repair_json
from fsd.log.logger_config import get_logger
logger = get_logger(__name__)

class LanguageAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_language_plan(self, user_prompt, role):
        """
        Get a development plan for the given prompt from Azure OpenAI.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            user_prompt (str): The user's prompt.

        Returns:
            str: Development plan or error reason.
        """
        logger.debug("\n #### The `LanguageAgent` is initiating the process to generate a language plan")

        messages = [
            {
                "role": "system",
                "content": f"As a senior {role}, translate non-English prompts to clear, concise English. Correct grammar and avoid confusion."
            },
            {
                "role": "user",
                "content": f"Original prompt:\n{user_prompt}"
            }
        ]

        try:
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            logger.debug("\n #### The `LanguageAgent` has successfully generated the language plan")
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f" #### The `LanguageAgent` encountered an error while generating the language plan: {e}")
            return {
                "reason": str(e)
            }

    async def get_language_plans(self, user_prompt, role):
        logger.debug("\n #### The `LanguageAgent` is processing the language plan")
        plan = await self.get_language_plan(user_prompt, role)
        logger.debug("\n #### The `LanguageAgent` has completed retrieving the language plans")
        return plan
