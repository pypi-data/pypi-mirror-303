import os
import sys


from .CompilePrePromptAgent import CompilePrePromptAgent
from .CompileProjectAnalysAgent import CompileProjectAnalysAgent
from .CompileFileFinderAgent import CompileFileFinderAgent
from .CompileGuiderAgent import CompileGuiderAgent
from .CompileTaskPlanner import CompileTaskPlanner


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.system.CompileCommandRunner import CompileCommandRunner
from fsd.system.OSEnvironmentDetector import OSEnvironmentDetector
from fsd.util.utils import parse_payload
from fsd.log.logger_config import get_logger
from fsd.PromptImageUrlAgent.PromptImageUrlAgent import PromptImageUrlAgent
logger = get_logger(__name__)

class CompileControllerAgent:
    def __init__(self, repo):
        self.repo = repo
        self.analysAgent = CompileProjectAnalysAgent(repo)
        self.preprompt = CompilePrePromptAgent(repo)
        self.fileFinder = CompileFileFinderAgent(repo)
        self.guider = CompileGuiderAgent(repo)
        self.taskPlanner = CompileTaskPlanner(repo)
        self.command = CompileCommandRunner(repo)
        self.imageAgent = PromptImageUrlAgent(repo)
        self.detector = OSEnvironmentDetector()

    async def get_prePrompt(self, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        return await self.preprompt.get_prePrompt_plans(user_prompt)

    async def start_CLI_compile_process(self, instruction, code_files, original_prompt_language, file_attachments, focused_files):
        logger.info("-------------------------------------------------")
    
        os_architecture = self.detector

        file_result = await self.fileFinder.get_compile_file_plannings(instruction)

        compile_files = file_result.get('crucial_files', [])

        logger.debug(f" #### The `Compiler Agent` has identified the following compile-related files: {compile_files}")

        self.analysAgent.initial_setup(compile_files, os_architecture)

        logger.info(" #### The `Compiler Analyst Agent` is creating plan for clarification")

        image_result = await self.imageAgent.process_image_links(instruction)
        assets_link = image_result.get('assets_link', []) if isinstance(image_result, dict) else []

        idea_plan = await self.analysAgent.get_idea_plans(instruction, original_prompt_language, file_attachments, focused_files, assets_link)

        while True:
            logger.info(" #### The `Compile Analysis Agent` is requesting feedback. Click `Approve` if you feel satisfied, click `Skip` to end this process, or type your feedback below.")

            logger.info(" ### Press a or Approve to execute this step, or Enter to skip: ")

            user_prompt_json = input()
            user_prompt,tier, file_attachments, focused_files, _ = parse_payload(self.repo.get_repo_path(), user_prompt_json)
            user_prompt = user_prompt.lower()

            if user_prompt == 's':
                logger.info(" #### The `Compiler Agent` has detected that the run/compile process has been skipped.")
                return

            if user_prompt == "a":
                break
            else:
                logger.info(" #### The `Compiler Analysis Agent` is updating based on user feedback.")
                instruction = instruction + "." + user_prompt
                self.analysAgent.remove_latest_conversation()
                image_result = await self.imageAgent.process_image_links(instruction)
                assets_link = image_result.get('assets_link', []) if isinstance(image_result, dict) else []
                idea_plan = await self.analysAgent.get_idea_plans(instruction, original_prompt_language, file_attachments, focused_files, assets_link)

        self.analysAgent.clear_conversation_history()
        logger.info(" #### The `Compiler Task Agent` is now organizing and preparing the task for execution.")
        task = await self.taskPlanner.get_task_plan(idea_plan, os_architecture, original_prompt_language)
        await self.command.execute_steps(task, compile_files, code_files, original_prompt_language)
        logger.info(" #### The `Compiler Agent` has successfully completed the compilation process.")
        logger.info("-------------------------------------------------")


    async def get_started(self, user_prompt, original_prompt_language, file_attachments, focused_files):
        """Start the processing of the user prompt."""
        logger.info("-------------------------------------------------")
        logger.info(" #### The `Compiler Agent` is initiating the compilation request process.")

        prePrompt = await self.get_prePrompt(user_prompt)
        finalPrompt = prePrompt['compile_plan']
        pipeline = prePrompt['pipeline']

        if pipeline == "0" or pipeline == 0:
            logger.info(" #### The `Compiler Agent` has determined that no compilation is needed.")
        elif pipeline == "1" or pipeline == 1:
            await self.start_CLI_compile_process(finalPrompt, [], original_prompt_language, file_attachments, focused_files)

        logger.info(f"\n #### The `Compiler Agent` has completed processing the user prompt: {user_prompt}.")
        logger.info("-------------------------------------------------")
