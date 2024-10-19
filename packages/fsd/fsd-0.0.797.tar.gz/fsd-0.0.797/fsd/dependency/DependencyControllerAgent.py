import os
import sys
import json
import subprocess
import asyncio
import re

from .DependencyPrePromptAgent import DependencyPrePromptAgent
from .DependencyProjectAnalysAgent import DependencyProjectAnalysAgent
from .DependencyFileFinderAgent import DependencyFileFinderAgent
from .DependencyGuiderAgent import DependencyGuiderAgent
from .DependencyTaskPlanner import DependencyTaskPlanner
from .DependencyCheckAgent import DependencyCheckAgent
from .DependencyCheckCLIAgent import DependencyCheckCLIAgent


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.MainOperation.ProjectManager import ProjectManager
from fsd.coding_agent.LanguageAgent import LanguageAgent
from fsd.system.CommandRunner import CommandRunner
from fsd.system.OSEnvironmentDetector import OSEnvironmentDetector
from fsd.util.utils import parse_payload
from fsd.log.logger_config import get_logger
logger = get_logger(__name__)

HOME_DIRECTORY = os.path.expanduser('~')
HIDDEN_ZINLEY_FOLDER = '.zinley'

class DependencyControllerAgent:
    def __init__(self, repo):
        self.repo = repo
        self.analysAgent = DependencyProjectAnalysAgent(repo)
        self.preprompt = DependencyPrePromptAgent(repo)
        self.project = ProjectManager(repo)
        self.fileFinder = DependencyFileFinderAgent(repo)
        self.guider = DependencyGuiderAgent(repo)
        self.lang = LanguageAgent(repo)
        self.taskPlanner = DependencyTaskPlanner(repo)
        self.command = CommandRunner(repo)
        self.detector = OSEnvironmentDetector()
        self.CLI = DependencyCheckCLIAgent(repo)
        self.checker = DependencyCheckAgent(repo)
        self.directory_path = self.repo.get_repo_path()


    async def get_prePrompt(self, user_prompt):
        """Generate idea plans based on user prompt and available files."""
        return await self.preprompt.get_prePrompt_plans(user_prompt)


    async def guider_pipeline(self, user_prompt):
        """Pipeline for regular coding tasks."""
        logger.info(" #### The `DependencyControllerAgent` is initiating the guider pipeline.")

        while True:
            user_prompt_json = input("Do you need more help with dependency?: ")
            guide = await self.guider.get_guider_plans(user_prompt_json)
            finalPrompt = guide['processed_prompt']
            pipeline = guide['pipeline']
            explainer = guide['explainer']

            if pipeline == "0":
                break
            elif pipeline == "1":
                print(explainer)
            elif pipeline == "2":
                print(guide)
                await self.start_dependency_installation_process(user_prompt)
                break


    async def start_dependency_installation_process(self, instruction, original_prompt_language, file_attachments, focused_files):
        
        logger.info(instruction)
        logger.info(" #### It looks like you need to install some dependency. Click `Approve` so I can do it for you, or `Skip if you don't want to proceed.")
        logger.info(" ### Press a or Approve to execute this step, or Enter to skip: ")
        user_permission = input()

        user_prompt, _, _, _= parse_payload(self.repo.get_repo_path(), user_permission)
        user_prompt = user_prompt.lower()
        
        if user_prompt != "a":
            logger.info(" #### The `Dependency Agent` has skipped the installation as per user request.")
            return
        else:
            os_architecture = self.detector
            file_result = await self.fileFinder.get_dependency_file_plannings()
            dependency_files = file_result.get('dependency_files', [])
            self.analysAgent.initial_setup(dependency_files, os_architecture)
            idea_plan = await self.analysAgent.get_idea_plans(instruction, original_prompt_language, file_attachments, focused_files)
            
            while True:
                logger.info(" #### The `Dependency Analysis Agent` is requesting feedback. Click `Approve` if you feel satisfied, click `Skip` to end this process, or type your feedback below.")

                logger.info(" ### Press a or Approve to execute this step, or Enter to skip: ")

                user_prompt_json = input()
                user_prompt, tier, file_attachments, focused_files = parse_payload(self.repo.get_repo_path(), user_prompt_json)
                user_prompt = user_prompt.lower()

                if user_prompt == 's':
                    logger.info(" #### The `Dependency Agent` has skipped the installation as per user request.")
                    return

                if user_prompt == "a":
                    break
                else:
                    logger.info(" #### The `Dependency Analysis Agent` is updating the plan based on feedback.")

                    CLI_prompt = await self.CLI.get_dependency_check_plan(user_prompt)

                    if "I am sorry" not in CLI_prompt:
                        eng_prompt = await self.lang.get_language_plans(user_prompt, "DevOps engineer")
                        instruction = instruction + " " + eng_prompt
                        self.analysAgent.remove_latest_conversation()
                        idea_plan = await self.analysAgent.get_idea_plans(instruction, original_prompt_language, file_attachments, focused_files)

            self.analysAgent.clear_conversation_history()
            logger.info(" #### The `Dependency Task Agent` is preparing to execute the finalized plan.")
            task = await self.taskPlanner.get_task_plan(idea_plan, os_architecture, original_prompt_language)
            await self.command.execute_steps(task, dependency_files, original_prompt_language)
            logger.info(f"\n #### The `Dependency Agent` has completed the task: {instruction}")

        logger.info("-------------------------------------------------")

    async def get_started(self, user_prompt, original_prompt_language, file_attachments, focused_files):
        """Start the processing of the user prompt."""
        logger.info(" #### The `Dependency Agent`is beginning to process the user request.")

        prePrompt = await self.get_prePrompt(user_prompt)
        pipeline = prePrompt['pipeline']

        if pipeline == "0" or pipeline == 0:
            explainer = prePrompt['explainer']
            print(explainer)
        elif pipeline == "1" or pipeline == 1:
            explainer = prePrompt['explainer']
            print(explainer)
            self.guider.initial_setup(user_prompt)
            self.guider.conversation_history.append({"role": "assistant", "content": f"{prePrompt}"})
            await self.guider_pipeline(user_prompt)
        elif pipeline == "2" or pipeline == 2:
            install_plan = prePrompt['install_plan']
            await self.start_dependency_installation_process(install_plan, original_prompt_language, file_attachments, focused_files)

        logger.info(f"\n #### The `Dependency Agent` has completed processing the request: {user_prompt}")
        logger.info("-------------------------------------------------")


    async def get_started_coding_pipeline(self, user_prompt, original_prompt_language, file_attachments, focused_files):
        logger.info("-------------------------------------------------")
        logger.debug(" #### The `Dependency Agent` is assigned.")
        """Start the processing of the user prompt."""

        check_result = await self.checker.get_dependency_check_plans(user_prompt)
        result = check_result.get('result')
        if result == "0" or result == 0:
            logger.debug(" #### The `Dependency Agent` has determined that no dependencies are needed for this task")
            return
        elif result == "1" or result == 1:
            prePrompt = await self.get_prePrompt(user_prompt)
            pipeline = prePrompt['pipeline']

            if pipeline == "0" or pipeline == 0:
                explainer = prePrompt['explainer']
                print(explainer)
            elif pipeline == "2" or pipeline == 2:
                install_plan = prePrompt['install_plan']
                await self.start_dependency_installation_process(install_plan, original_prompt_language, file_attachments, focused_files)

            logger.info(" #### The `Dependency Agent` has installed all required dependencies. ")
        logger.info("-------------------------------------------------")
