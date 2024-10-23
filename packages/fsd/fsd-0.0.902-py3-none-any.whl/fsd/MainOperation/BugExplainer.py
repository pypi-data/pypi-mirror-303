import os
import sys
import asyncio
import re
from json_repair import repair_json
import aiohttp
import json

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from fsd.log.logger_config import get_logger
from fsd.util.utils import read_file_content
logger = get_logger(__name__)

class XcodeBugExplainer:
    def __init__(self, repo):
        self.repo = repo
        self.conversation_history = []
        self.ai = AIGateway()

    def clear_conversation_history(self):
        """Clear the conversation history."""
        self.conversation_history = []

    def initial_setup(self, role):
        """Set up the initial prompt for the Xcode bug-fixing agent."""
        prompt = (
            f"You are a senior {role} Xcode bug-fixing agent. Analyze the Xcode project context and errors, identify root causes, and provide structured steps to fix each bug. Focus on the root cause, not applying fixes to all affected files. Rules:\n"
            "1. Each step involves one file only.\n"
            "2. 'file_name' must include full file path within the Xcode project structure.\n"
            "3. 'list_related_file_name' includes full paths of potentially impacted files in the Xcode project; empty list if none.\n"
            "4. 'is_new' is 'True' for new files, 'False' otherwise.\n"
            "5. 'new_file_location' specifies relative path for new files within the Xcode project structure.\n"
            "Respond with valid JSON only without additional text or symbols or MARKDOWN, following this format:\n"
            "{\n"
            "        {\n"
            "            \"Step\": 1,\n"
            "            \"file_name\": \"Full/Path/To/File.swift\",\n"
            "            \"tech_stack\": \"Swift\",\n"
            "            \"is_new\": \"True/False\",\n"
            "            \"new_file_location\": \"Relative/Path/In/Xcode/Project\",\n"
            "            \"list_related_file_name\": [\"Full/Path/To/Related1.swift\", \"Full/Path/To/Related2.swift\"],\n"
            "            \"Solution_detail_title\": \"Brief Xcode issue description\",\n"
            "            \"all_comprehensive_solutions_for_each_bug\": \"Detailed Xcode-specific fix instructions\"\n"
            "        }\n"
            "}\n"
            "No additional content or formatting."
        )

        self.conversation_history.append({"role": "system", "content": prompt})

    async def get_bugFixed_suggest_request(self, bug_logs, all_file_contents, overview, file_attachments, focused_files):
        """
        Get development plan for all Xcode project files based on user prompt.

        Args:
            bug_logs (str): Xcode-specific bug logs.
            all_file_contents (str): The concatenated contents of all Xcode project files.
            overview (str): Xcode project overview description.
            file_attachments (list): List of attached file paths.
            focused_files (list): List of focused file paths in the Xcode project.

        Returns:
            dict: Xcode-specific development plan or error reason.
        """

        error_prompt = (
            f"Current Xcode project files:\n{all_file_contents}\n\n"
            f"Xcode project structure:\n{self.repo.print_tree()}\n\n"
            f"Xcode project overview:\n{overview}\n\n"
            f"Xcode bug logs:\n{bug_logs}\n\n"
            "Return only a valid JSON format Xcode bug fix response without additional text or Markdown symbols or invalid escapes.\n\n"
        )

        file_attachments = [f for f in file_attachments if not f.lower().endswith(('.webp', '.jpg', '.jpeg', '.png'))]

        all_attachment_file_contents = ""
        all_focused_files_contents = ""

        if file_attachments:
            for file_path in file_attachments:
                file_content = read_file_content(file_path)
                if file_content:
                    all_attachment_file_contents += f"\n\nFile: {os.path.relpath(file_path)}:\n{file_content}"

        if focused_files:
            for file_path in focused_files:
                file_content = read_file_content(file_path)
                if file_content:
                    all_focused_files_contents += f"\n\nFile: {os.path.relpath(file_path)}:\n{file_content}"

        if all_attachment_file_contents:
            error_prompt += f"\nUser has attached these Xcode project files for you, use them appropriately: {all_attachment_file_contents}"

        if all_focused_files_contents:
            error_prompt += f"\nUser has focused on these files in the current Xcode project, pay special attention to them if needed: {all_focused_files_contents}"

        self.conversation_history.append({"role": "user", "content": error_prompt})

        try:
            response = await self.ai.coding_prompt(self.conversation_history, 4096, 0.6, 0.7)
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.error(f" #### `XcodeBugExplainer`: Failed to get Xcode bug fix suggestion: {e}")
            return {
                "reason": e
            }

    async def get_bugFixed_suggest_requests(self, bug_logs):
        """
        Get development plans for a list of Xcode project files based on user prompt.

        Args:
            bug_logs (str): Xcode-specific bug logs.
            files (list): List of Xcode project file paths.
            overview (str): Xcode project overview description.
            file_attachments (list): List of attached file paths.
            focused_files (list): List of focused file paths in the Xcode project.

        Returns:
            dict: Xcode-specific development plan or error reason.
        """
        # Get the Xcode-specific bug-fixed suggestion request
        plan = await self.get_bugFixed_suggest_request(bug_logs)
        return plan