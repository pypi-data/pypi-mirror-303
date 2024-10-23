import subprocess
import os
import sys
import requests
import json
import threading
import time
import re
import signal
from log.logger_config import get_logger
from .FileContentManager import FileContentManager
from .OSEnvironmentDetector import OSEnvironmentDetector
from .ConfigAgent import ConfigAgent
from .TaskErrorPlanner import TaskErrorPlanner
from .ErrorDetection import ErrorDetection

logger = get_logger(__name__)

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.coding_agent.BugExplainer import BugExplainer
from fsd.coding_agent.SelfHealingAgent import SelfHealingAgent
from fsd.MainOperation.ProjectManager import ProjectManager
from fsd.coding_agent.FileManagerAgent import FileManagerAgent
from fsd.util.utils import parse_payload

class CompileCommandRunner:
    def __init__(self, repo):
        """
        Initializes the CommandRunner.
        """
        self.repo = repo
        self.config = ConfigAgent(repo)
        self.errorDetection = ErrorDetection(repo)
        self.errorPlanner = TaskErrorPlanner(repo)
        self.self_healing = SelfHealingAgent(repo)
        self.bugExplainer = BugExplainer(repo)
        self.project = ProjectManager(repo)
        self.fileManager = FileManagerAgent(repo)
        self.config_manager = FileContentManager()  # Initialize CodeManager in the constructor
        self.detector = OSEnvironmentDetector()
        self.directory_path = repo.get_repo_path()
        self.max_retry_attempts = 3  # Set a maximum number of retry attempts

    async def get_config_requests(self, instructions, file_name):
        """Generate coding requests based on instructions and context."""

        main_path = file_name
        logger.info(f"\n #### `ConfigAgent` is processing file: {file_name} in {main_path}")
        logger.info(f"\n #### Task: {instructions}")
        result = await self.config.get_config_requests(instructions, main_path)
        if main_path:
            await self.config_manager.handle_coding_agent_response(main_path, result)
            logger.info(f"\n #### `ConfigAgent` has completed its work on {file_name}")
        else:
            logger.debug(f" #### `ConfigAgent` was unable to locate the file: {file_name}")

    async def get_error_planner_requests(self, error, config_context, os_architecture, compile_files, original_prompt_language):
        """Generate coding requests based on instructions and context."""
        result = await self.errorPlanner.get_task_plans(error, config_context, os_architecture, compile_files, original_prompt_language)
        return result

    def run_command(self, command, method='bash'):
        """
        Runs a given command using the specified method.
        Shows real-time output during execution.
        Returns a tuple of (return_code, all_output).
        """
        try:
            # Use bash for all commands
            shell = True
            executable = '/bin/bash'

            # Check if the first part of the command is 'cd'
            if command.startswith('cd '):
                # Change the working directory
                new_dir = command[3:].strip()
                os.chdir(new_dir)
                logger.info(
                    f"#### Directory Change\n"
                    f"```bash\n"
                    f"cd {new_dir}\n"
                    f"```\n"
                    f"Changed directory to: {new_dir}\n"
                    f"----------------------------------------"
                )
                return 0, [f"Changed directory to: {new_dir}"]

            # Log the current working directory and the command to be executed
            current_path = os.getcwd()
            logger.info(
                f"#### Executing Command\n"
                f"```bash\n"
                f"cd {current_path}\n"
                f"{command}\n"
                f"```\n"
                f"----------------------------------------"
            )

            # Start the process and capture output
            process = subprocess.Popen(
                command,
                shell=shell,
                executable=executable,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True,
                cwd=current_path  # Explicitly set the working directory
            )

            # Initialize output list
            output = []

            # Start streaming output
            logger.info("#### Command Output")
            logger.info("```bash")

            while True:
                # Read output from stdout and stderr
                stdout_line = process.stdout.readline()
                stderr_line = process.stderr.readline()

                if stdout_line:
                    logger.info(stdout_line.strip())
                    output.append(stdout_line.strip())
                if stderr_line:
                    logger.info(stderr_line.strip())
                    output.append(stderr_line.strip())

                # Check if the process has finished
                if process.poll() is not None:
                    # Read any remaining output
                    for line in process.stdout:
                        logger.info(line.strip())
                        output.append(line.strip())
                    for line in process.stderr:
                        logger.info(line.strip())
                        output.append(line.strip())
                    break

            # Close the bash code block
            logger.info("```")

            return_code = process.returncode
            logger.info(
                f"#### Command Finished with Return Code: `{return_code}`\n"
                f"----------------------------------------"
            )
            logger.info("The CommandRunner has completed the current step and is proceeding to the next one.")
            return return_code, output

        except Exception as e:
            logger.error(
                f"#### Error Executing Command\n"
                f"```bash\n"
                f"{command}\n"
                f"```\n"
                f"Error: {str(e)}\n"
                f"----------------------------------------"
            )
            return -1, [f"Command execution failed: {str(e)}"]

    def run_localhost_command(self, command, current_path):
        """
        Runs a localhost command in a separate session.
        If no error occurs, waits for 20 seconds after command completion before returning.
        Collects all output and errors before returning.
        """
        logger.info(
            f"#### Running Localhost Command\n"
            f"```bash\n"
            f"# Command:\n"
            f"{command}\n\n"
            f"# In Directory:\n"
            f"cd {current_path}\n"
            f"```\n"
            f"----------------------------------------"
        )
        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=current_path,
            start_new_session=True
        )

        output = []
        error_output = []
        has_error = False
        port_already_in_use_line = None

        logger.info("#### Command Output")
        logger.info("```bash")
        while True:
            return_code = process.poll()
            if return_code is not None:
                # Process has finished
                stdout, stderr = process.communicate()
                for line in stdout.splitlines():
                    logger.info(line)
                    output.append(line)
                    if "already running on port" in line.lower():
                        port_already_in_use_line = line
                for line in stderr.splitlines():
                    logger.info(line)
                    error_output.append(line)
                break

            # Check for any output
            stdout = process.stdout.readline()
            if stdout:
                line = stdout.strip()
                logger.info(line)
                output.append(line)
                if "already running on port" in line.lower():
                    port_already_in_use_line = line
                elif "error" in line.lower():
                    has_error = True
            stderr = process.stderr.readline()
            if stderr:
                line = stderr.strip()
                logger.info(line)
                error_output.append(line)
                has_error = True

            time.sleep(0.1)
        logger.info("```")

        if port_already_in_use_line:
            logger.info(
                f"#### Port Already in Use\n"
                f"```bash\n{port_already_in_use_line}\n```\n"
                f"Press Tab to process the fix, or Enter to skip\n"
                f"----------------------------------------"
            )
            user_input = input()
            if user_input == '\t':
                return -1, [port_already_in_use_line]
            else:
                return 0, [port_already_in_use_line]
        elif has_error or return_code != 0:
            logger.info(
                f"#### Command Failed\n"
                f"```bash\nReturn Code: {return_code}\n```\n"
                f"----------------------------------------"
            )
            return -1, output + error_output
        else:
            logger.info(
                f"#### Command Completed Successfully\n"
                f"```bash\n"
                f"Return Code: {return_code}\n"
                f"Waiting for 10 seconds before completion\n"
                f"```\n"
                f"----------------------------------------"
            )
            # Wait for 10 seconds after successful completion
            time.sleep(10)
            return 0, output + error_output

    def update_file(self, file_name, content):
        """
        Updates the content of a file.
        """
        try:
            with open(file_name, 'a') as file:
                file.write(content + '\n')
            logger.info(f"\n #### `FileUpdater` has successfully updated {file_name}")
            return f"Successfully updated {file_name}"
        except Exception as e:
            logger.error(f" #### `FileUpdater` failed to update {file_name}: {str(e)}")
            return f"Failed to update {file_name}: {str(e)}"

    async def print_code_error(self, error_message, code_files, role="Elite software engineer", max_retries=50):
        """
        Prints the code syntax error details.
        """
        totalfile = set()
        fixing_related_files = set()

        retries = 0

        while retries < max_retries:
            self.self_healing.clear_conversation_history()
            self.bugExplainer.clear_conversation_history()

            self.bugExplainer.initial_setup(role)
            self.self_healing.initial_setup(role)

            try:
                logger.info(" #### `ErrorHandler` has detected an issue and will commence work on the fix immediately")
                overview = ""

                overview = self.repo.print_tree()

                # Ensure basename list is updated without duplicates
                fixing_related_files.update(list(code_files))
                fixing_related_files.update(list(totalfile))

                logger.info(" #### `BugExplainer` is initiating the examination of bugs and creation of a fixing plan")
                fix_plans = await self.bugExplainer.get_bugFixed_suggest_requests(
                    error_message, list(fixing_related_files), overview)
                print(f"fix_plans: {fix_plans}")
                logger.info(" #### `BugExplainer` has completed the examination of bugs and creation of a fixing plan")

                logger.info(" #### `FileProcessor` is beginning work on file processing")
                file_result = await self.get_file_planning(fix_plans)
                await self.process_creation(file_result)
                add = file_result.get('Adding_new_files', [])
                move = file_result.get('Moving_files', [])
                if add or move:
                    commits = file_result.get('commits', "")
                    if commits:
                        self.repo.add_all_files(f"Zinley - {commits}")
                logger.info(" #### `FileProcessor` has completed processing files")

                logger.info(f"\n #### `FixingAgent` is attempting to fix for the {retries + 1} time")
                steps = fix_plans.get('steps', [])

                for step in steps:
                    file_name = step['file_name']
                    totalfile.add(file_name)

                await self.self_healing.get_fixing_requests(steps)

                # If we reach this point without exceptions, we assume the fix was successful
                logger.info(" #### `FixingAgent` has successfully applied the fix")
                return list(totalfile)

            except requests.exceptions.HTTPError as http_error:
                if http_error.response.status_code == 429:
                    wait_time = 2 ** retries
                    logger.info(f"\n #### `RateLimitHandler` has detected that the rate limit has been exceeded, retrying in {wait_time} seconds...")
                    time.sleep(wait_time)  # Exponential backoff
                else:
                    logger.error(f" #### `HTTPErrorHandler` encountered an HTTP error: {http_error}")
                    raise
            except Exception as e:
                logger.error(f" #### `ErrorHandler` encountered an error during the fixing process: {str(e)}")

            retries += 1

        self.self_healing.clear_conversation_history()
        self.bugExplainer.clear_conversation_history()
        logger.info(" #### `BuildManager` reports that the build has failed after maximum retries")

    async def execute_steps(self, steps_json, compile_files, code_files, original_prompt_language):
        """
        Executes a series of steps provided in JSON format.
        Asks for user permission before executing each step.
        Waits for each command to complete before moving to the next step.
        """
        self.errorDetection.initial_setup()
        steps = steps_json['steps']

        for step in steps:
            if step['method'] == 'bash':
                logger.info(f"\n #### `Compile Command Runner`: {step['prompt']}")
                logger.info(f"```bash\n{step['command']}\n```")
            elif step['method'] == 'update':
                logger.info(f"\n #### `Compile Command Runner`:")
                logger.info(f"```yaml\n{step['prompt']}\n```")

            logger.info("")
            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
            user_permission = input()

            user_prompt, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_permission)
            user_prompt = user_prompt.lower()

            if user_prompt == 'exit':
                logger.info(" #### The user has chosen to exit. The `CommandRunner` is halting execution.")
                return "Execution stopped by user"
            elif user_prompt == 's':
                logger.info(" #### The user has chosen to skip this step.")
                continue

            logger.info(f"\n #### `StepExecutor`: Executing step: {step['prompt']}")

            retry_count = 0
            while retry_count < self.max_retry_attempts:
                if step['method'] == 'bash':
                    # Run the command and get the return code and output
                    return_code, command_output = self.run_command(step['command'])

                    # Check for errors based on the return code
                    if return_code != 0:
                        error_message = ','.join(command_output)
                        logger.error(f" #### `CommandExecutor` failed with return code {return_code}: {error_message}")

                        # Check if the error suggests an alternative command
                        if "Did you mean" in error_message:
                            suggested_command = error_message.split("Did you mean")[1].strip().strip('"?')
                            logger.info(f"\n #### `SystemSuggestionHandler` has found an alternative command: {suggested_command}")
                            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
                            user_choice = input()

                            user_select, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_choice)
                            user_select = user_select.lower()
                            
                            if user_select == 'a':
                                logger.info(f"\n #### `UserInteractionHandler`: Executing suggested command: {suggested_command}")
                                return_code, command_output = self.run_command(suggested_command)
                                if return_code == 0:
                                    break  # Command executed successfully
                                else:
                                    # Update error_message with new command output
                                    error_message = ','.join(command_output)
                                    logger.error(
                                        f"\n #### `CommandExecutor`: Suggested command also failed with return code {return_code}: {error_message}")
                            elif user_select == 'exit':
                                logger.info(" #### `UserInteractionHandler`: User has chosen to exit. Stopping execution.")
                                return "Execution stopped by user"
                            else:
                                logger.info(" #### `UserInteractionHandler`: User chose not to run the suggested command.")

                        error_check = await self.errorDetection.get_task_plan(error_message)
                        error_type = error_check.get('error_type', 1)
                        AI_error_message = error_check.get('error_message', "")

                        if error_type == 1:
                            await self.print_code_error(AI_error_message, code_files)
                            retry_count += 1
                            continue  # Re-run the command after fixing the code error
                        
                        # Proceed to handle the error
                        fixing_steps = await self.get_error_planner_requests(
                            error_message, step['prompt'], self.detector, compile_files, original_prompt_language)
                        fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, code_files, original_prompt_language)
                        if fixing_result == "Execution stopped by user":
                            logger.info(" #### `UserInteractionHandler`: User chose to exit during fixing steps. Skipping current step.")
                            break
                        retry_count += 1
                    else:
                        break  # Command executed successfully without errors
                elif step['method'] == 'update':
                    file_name = step.get('file_name', '')
                    if file_name != 'N/A':
                        await self.get_config_requests(step['prompt'], file_name)
                        logger.info(f"\n #### `FileUpdater` has successfully updated {file_name}")
                    else:
                        logger.debug("\n #### `FileUpdater`: Update method specified but no file name provided.")
                    break
                else:
                    logger.error(f" #### `StepExecutor` encountered an unknown method: {step['method']}")
                    break

            if retry_count == self.max_retry_attempts:
                logger.error(f" #### `StepExecutor`: Step failed after {self.max_retry_attempts} attempts: {step['prompt']}")
                error_message = f"Step failed after {self.max_retry_attempts} attempts: {step['prompt']}"
                fixing_steps = await self.get_error_planner_requests(
                    error_message, step['prompt'], self.detector, compile_files, original_prompt_language)
                fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, code_files)
                if fixing_result == "Execution stopped by user":
                    logger.info(" #### `UserInteractionHandler`: User chose to exit during fixing steps. Skipping current step.")
                    continue
                return f"Step failed after {self.max_retry_attempts} attempts: {step['prompt']}"

            logger.info(" #### `StepExecutor`: Step completed. Proceeding to the next step.")

        logger.info(" #### `StepExecutor`: All steps have been completed successfully")
        return "All steps completed successfully"

    async def execute_fixing_steps(self, steps_json, compile_files, code_files, original_prompt_language):
        """
        Executes a series of steps provided in JSON format to fix dependency issues.
        Asks for user permission before executing each step.
        Waits for each command to complete before moving to the next step.
        """
        steps = steps_json['steps']

        for step in steps:

            if step['method'] == 'bash':
                logger.info(f"\n #### `Compile Command Runner`: {step['error_resolution']}")
                logger.info(f"```bash\n{step['command']}\n```")
            elif step['method'] == 'update':
                logger.info(f"\n #### `Compile Command Runner`:")
                logger.info(f"```yaml\n{step['error_resolution']}\n```")

            logger.info("")
            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
            user_permission = input()

            user_prompt, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_permission)
            user_prompt = user_prompt.lower()

            if user_prompt == 'exit':
                logger.info(" #### The user has chosen to exit. The `CommandRunner` is halting execution.")
                return "Execution stopped by user"
            elif user_prompt == 's':
                logger.info(" #### The user has chosen to skip this step.")
                continue

            logger.info(f"\n #### `FixingStepExecutor`: Executing step: {step['error_resolution']}")

            retry_count = 0
            while retry_count < self.max_retry_attempts:
                if step['method'] == 'bash':
                    # Run the command and get the return code and output
                    return_code, command_output = self.run_command(step['command'])

                    # Check for errors based on the return code
                    if return_code != 0:
                        error_message = ','.join(command_output)
                        logger.error(f" #### `CommandExecutor` failed with return code {return_code}: {error_message}")

                        ## Check if the error suggests an alternative command
                        if "Did you mean" in error_message:
                            suggested_command = error_message.split("Did you mean")[1].strip().strip('"?')
                            logger.info(f"\n #### `SystemSuggestionHandler` has found an alternative command: {suggested_command}")
                            logger.info(" ### Press 'a' or 'Approve' to execute this step, or press Enter to skip, or type 'exit' to exit the entire process: ")
                            user_choice = input()

                            user_select, _, _, _, _ = parse_payload(self.repo.get_repo_path(), user_choice)
                            user_select = user_select.lower()
                            
                            if user_select == 'a':
                                logger.info(f"\n #### `UserInteractionHandler`: Executing suggested command: {suggested_command}")
                                return_code, command_output = self.run_command(suggested_command)
                                if return_code == 0:
                                    break  # Command executed successfully
                                else:
                                    # Update error_message with new command output
                                    error_message = ','.join(command_output)
                                    logger.error(
                                        f"\n #### `CommandExecutor`: Suggested command also failed with return code {return_code}: {error_message}")
                            elif user_select == 'exit':
                                logger.info(" #### `UserInteractionHandler`: User has chosen to exit. Stopping execution.")
                                return "Execution stopped by user"
                            else:
                                logger.info(" #### `UserInteractionHandler`: User chose not to run the suggested command.")

                        error_check = await self.errorDetection.get_task_plan(error_message)
                        error_type = error_check.get('error_type', 1)
                        AI_error_message = error_check.get('error_message', "")

                        if error_type == 1:
                            await self.print_code_error(AI_error_message, code_files)
                            retry_count += 1
                            continue  # Re-run the command after fixing the code error

                        # Proceed to handle the error
                        fixing_steps = await self.get_error_planner_requests(
                            error_message, step['error_resolution'], self.detector, compile_files, original_prompt_language)
                        fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, code_files, original_prompt_language)
                        if fixing_result == "Execution stopped by user":
                            return "Execution stopped by user"
                        retry_count += 1
                    else:
                        break  # Command executed successfully without errors
                elif step['method'] == 'update':
                    file_name = step.get('file_name', '')
                    if file_name != 'N/A':
                        await self.get_config_requests(step['error_resolution'], file_name)
                        logger.info(f"\n #### `FileUpdater` has successfully updated {file_name}")
                    else:
                        logger.debug("\n #### `FileUpdater`: Update method specified but no file name provided.")
                    break
                else:
                    logger.error(f" #### `FixingStepExecutor` encountered an unknown method: {step['method']}")
                    break

            if retry_count == self.max_retry_attempts:
                logger.error(f" #### `FixingStepExecutor`: Step failed after {self.max_retry_attempts} attempts: {step['error_resolution']}")
                error_message = f"Step failed after {self.max_retry_attempts} attempts: {step['error_resolution']}"
                fixing_steps = await self.get_error_planner_requests(
                    error_message, step['error_resolution'], self.detector, compile_files, original_prompt_language)
                fixing_result = await self.execute_fixing_steps(fixing_steps, compile_files, code_files)
                if fixing_result == "Execution stopped by user":
                    return "Execution stopped by user"
                return f"Step failed after {self.max_retry_attempts} attempts: {step['error_resolution']}"

            logger.info(" #### `FixingStepExecutor`: Step completed. Proceeding to the next step.")

        logger.info(" #### `FixingStepExecutor`: All fixing steps have been completed successfully")
        return "All fixing steps completed successfully"

    async def get_file_planning(self, idea_plan):
        """Generate idea plans based on user prompt and available files."""
        return await self.fileManager.get_file_plannings(idea_plan)

    async def process_creation(self, data):
        moving_processes = data.get('Moving_files', [])
        
        if data.get('Is_creating'):
            new_files = data.get('Adding_new_files', [])
            await self.project.execute_files_creation(new_files)
            
        if moving_processes:
            await self.project.execute_files_creation(moving_processes)
        
        if not data.get('Is_creating') and not moving_processes:
            logger.info(" #### `FileCreationManager`: No new files need to be added or moved at this time.")
