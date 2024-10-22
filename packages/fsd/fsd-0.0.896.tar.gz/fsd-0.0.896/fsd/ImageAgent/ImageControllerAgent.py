import os
import sys
import json
import subprocess
import asyncio
import re

from .ImagePrePromptAgent import CompilePrePromptAgent
from .ImageTaskPlanner import ImageTaskPlanner
from .ImageFileFinderAgent import ImageFileFinderAgent
from .ImageAnalysAgent import ImageAnalysAgent
from .ImageGenAgent import ImageGenAgent
from .ImageCheckAgent import ImageCheckAgent
from .ImageCheckSpecialAgent import ImageCheckSpecialAgent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.utils import parse_payload, read_file_content, call_error_api
from fsd.log.logger_config import get_logger
from fsd.PromptImageUrlAgent.PromptImageUrlAgent import PromptImageUrlAgent
logger = get_logger(__name__)

class ImageControllerAgent:
    def __init__(self, repo):
        self.repo = repo
        self.preprompt = CompilePrePromptAgent(repo)
        self.fileFinder = ImageFileFinderAgent(repo)
        self.analysAgent = ImageAnalysAgent(repo)
        self.taskPlanner = ImageTaskPlanner(repo)
        self.imageGenAgent = ImageGenAgent(repo)
        self.imageCheckAgent = ImageCheckAgent(repo)
        self.imageCheckSpecialAgent = ImageCheckSpecialAgent(repo)
        self.imageAgent = PromptImageUrlAgent(repo)

    async def get_prePrompt(self, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        try:
            return await self.preprompt.get_prePrompt_plans(user_prompt)
        except Exception as e:
            call_error_api(f"Error in get_prePrompt: {str(e)}", "get_prePrompt")
            raise


    async def start_image_process(self, tier, instruction, original_prompt_language, snow_mode):

        logger.info(" #### Image generation needed. Click `Approve` to proceed or `Skip` to cancel.")
        logger.info(f" \n ### Press a or Approve to execute this step, or Enter to skip: ")
        user_permission = input()
        try:
            user_prompt, tier, _, _, snow_mode  = parse_payload(self.repo.get_repo_path(), user_permission)
            user_prompt = user_prompt.lower()
        except Exception as e:
            call_error_api(f"Error parsing payload: {str(e)}", "start_image_process")
            raise
        
        if user_prompt != "a":
            logger.info(" #### The `Image Generation Agent` has skipped as per user request.")
            return

        logger.info(f"\n #### `Image Task Planner` is organizing and preparing the task. ")
        try:
            task = await self.taskPlanner.get_task_plan(instruction)
            await self.imageGenAgent.generate_images(task, tier, snow_mode)
            commits = task.get('commits', "")
            self.repo.add_all_files(f"Zinley - {commits}")
        except Exception as e:
            call_error_api(f"Error in image generation process: {str(e)}", "start_image_process")
            raise
        logger.info(f"\n #### Image generation process completed.")


    async def get_started(self, tier, instruction, original_prompt_language, file_attachments, focused_files, snow_mode):
        """Start the processing of the user prompt."""
        
        logger.info(" #### `Image Analysis Agent` is finding relevant style content.")
        
        try:
            file_result = await self.fileFinder.get_style_file_plannings()
            style_files = file_result.get('style_files', [])
            self.analysAgent.initial_setup(style_files)
        except Exception as e:
            call_error_api(f"Error in file finding and analysis setup: {str(e)}", "get_started")
            raise

        logger.info(" #### `Image Analysis Agent` is preparing an initial image plan for clarification.")

        try:
            image_result = await self.imageAgent.process_image_links(instruction)
            assets_link = image_result.get('assets_link', []) if isinstance(image_result, dict) else []
            idea_plan = await self.analysAgent.get_idea_plans(instruction, original_prompt_language, file_attachments, focused_files, assets_link)
        except Exception as e:
            call_error_api(f"Error in initial image plan preparation: {str(e)}", "get_started")
            raise

        while True:

            logger.info(" #### The `Image Analysis Agent` is requesting feedback. Click `Approve` if you feel satisfied, click `Skip` to end this process, or type your feedback below.")

            logger.info(" ### Press a or Approve to execute this step, or Enter to skip: ")

            user_prompt_json = input()
            try:
                user_prompt,tier,file_attachments, focused_files, snow_mode = parse_payload(self.repo.get_repo_path(), user_prompt_json)
                user_prompt = user_prompt.lower()
            except Exception as e:
                call_error_api(f"Error parsing user input: {str(e)}", "get_started")
                raise

            if user_prompt == 's':
                logger.info(" #### The `Image Generation Agent` has skipped as per user request.")
                return

            if user_prompt == "a":
                break
            else:
                logger.info(f"\n #### `Image Analysis Agent` is updating the image plan based on user feedback.")
                instruction = instruction + "." + user_prompt
                self.analysAgent.remove_latest_conversation()
                try:
                    image_result = await self.imageAgent.process_image_links(instruction)
                    assets_link = image_result.get('assets_link', []) if isinstance(image_result, dict) else []
                    idea_plan = await self.analysAgent.get_idea_plans(instruction, original_prompt_language, file_attachments, focused_files, assets_link)
                except Exception as e:
                    call_error_api(f"Error updating image plan: {str(e)}", "get_started")
                    raise

        self.analysAgent.clear_conversation_history()

        logger.info(f"\n #### `Image Task Planner` is organizing and preparing the task. ")
        try:
            task = await self.taskPlanner.get_task_plan(idea_plan)
            await self.imageGenAgent.generate_images(task, tier, snow_mode)
            commits = task.get('commits', "")
            self.repo.add_all_files(f"Zinley - {commits}")
        except Exception as e:
            call_error_api(f"Error in final image generation process: {str(e)}", "get_started")
            raise
        logger.info(f"\n #### Image generation process completed.")


    async def get_started_image_generation(self, tier, user_prompt, original_prompt_language, snow_mode):
        """Start the processing of the user prompt."""
        
        logger.debug(" #### Image generation agent initialized and ready to process image requests")

        try:
            result = await self.imageCheckAgent.get_image_check_plans(user_prompt)
            result = result['result']
        except Exception as e:
            call_error_api(f"Error checking image plans: {str(e)}", "get_started_image_generation")
            raise

        if result == "0" or result == 0:
            logger.info(" #### `Image generation agent` has determined that no additional images need to be generated")
        elif result == "1" or result == 1:
            try:
                finalPrompt = await self.imageCheckSpecialAgent.get_image_check_plans(user_prompt, original_prompt_language)
                await self.start_image_process(tier, finalPrompt, original_prompt_language, snow_mode)
            except Exception as e:
                call_error_api(f"Error in special image check or image process: {str(e)}", "get_started_image_generation")
                raise

        logger.debug(f" #### Image generation process completed!")
