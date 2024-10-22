import os
import aiohttp
import asyncio
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from fsd.log.logger_config import get_logger
from fsd.util.utils import read_file_content
from fsd.util.utils import process_image_files
logger = get_logger(__name__)

class DependencyProjectAnalysAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.conversation_history = []
        self.ai = AIGateway()

    def clear_conversation_history(self):
        """Clear the conversation history."""
        self.conversation_history = []

    def remove_latest_conversation(self):
        """Remove the latest conversation from the history."""
        if self.conversation_history:
            self.conversation_history.pop()

    def initial_setup(self, dependency_files, OS_architecture):
        """
        Initialize the conversation with a system prompt and user context.
        """

        all_file_contents = ""
        tree_contents = self.repo.print_tree()

        logger.debug(f" #### `DependencyProjectAnalysAgent`: Initializing analysis with repository path\n{self.repo.get_repo_path()}")

        dependency_files_path = dependency_files

        if dependency_files_path:
            for file_path in dependency_files_path:
                file_content = read_file_content(file_path)
                if file_content:
                    all_file_contents += f"\n\nFile: {file_path}:\n{file_content}"
        else:
            all_file_contents = "No dependency files found."

        system_prompt = (
            f"You are a DevOps engineer. Create a simple CLI-only dependency installation plan. Follow these rules:\n\n"
            "1. Navigate to the project directory\n"
            "2. Carefully examine the project tree to identify existing configuration files\n"
            "3. If configuration files (e.g., package.json, Podfile, requirements.txt) are missing, create them first\n"
            "4. Initialize configuration files with basic structure before proceeding with installations\n"
            "5. Identify and install dependencies using appropriate package managers (e.g., pip, npm, yarn)\n"
            "6. Set up a virtual environment if necessary (e.g., venv for Python)\n"
            "7. Provide concise CLI commands for each step, using nice formatting in bash markdown, like this:\n"
            "   ```bash\n"
            "   cd /path/to/project\n"
            "   npm install package-name\n"
            "   ```\n"
            "8. Focus only on essential dependency setup and configuration\n"
            "9. Ensure the setup allows for easy project execution later\n"
            "10. For any file modifications, specify the file path and content to be changed\n"
            "11. Prioritize simplicity and avoid potential conflicts in the installation process\n"
            "12. Configure build/run files to make project execution as simple as possible\n"
            "13. If appropriate, create a simple run script (e.g., run.sh or run.bat) with clear instructions\n"
            "14. For compiled languages, include compilation steps and create executable files if needed\n"
            "15. Update package.json to include start script and other necessary scripts\n"
            "16. For other project types, ensure similar configuration files are properly set up (e.g., Gemfile for Ruby, pom.xml for Java)\n"
            "17. Double-check all configuration files for completeness and correctness\n"
            "Do not create or modify any code files beyond basic configuration and build/run scripts. Match the OS architecture provided."
        )

        self.conversation_history.append({"role": "system", "content": system_prompt})
        self.conversation_history.append({"role": "user", "content":  f"Here are the current dependency files: {all_file_contents}\n\nProject tree: {tree_contents}\n\nOS Architecture: {OS_architecture}"})
        self.conversation_history.append({"role": "assistant", "content": "Got it! Give me user prompt so i can support them."})

    async def get_idea_plan(self, user_prompt, original_prompt_language, file_attachments, focused_files, assets_link):
        prompt = (
            f"Follow the user prompt strictly and provide a no code response:\n\n"
            f"{user_prompt}\n\n"
            "Ensure the response is well-organized with clear formatting and good spacing.\n\n"
            f"Provide the response in the following language: {original_prompt_language}"
        )

        image_files = process_image_files(file_attachments)

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
            prompt += f"\nUser has attached these files for you, use them appropriately: {all_attachment_file_contents}"

        if all_focused_files_contents:
            prompt += f"\nUser has focused on these files in the current project, pay special attention to them according if need: {all_focused_files_contents}"


        user_content = [{"type": "text", "text": prompt}]

        # Add image files to the user content
        for base64_image in image_files:
            user_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"{base64_image}"
                }
            })

        if assets_link:
            for image_url in assets_link:
                user_content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                })

        self.conversation_history.append({"role": "user", "content": user_content})

        try:
            response = await self.ai.arch_stream_prompt(self.conversation_history, self.max_tokens, 0, 0)
            return response
        except Exception as e:
            logger.error(f" #### `DependencyProjectAnalysAgent`: Error occurred while generating idea plan\n{e}")
            return {
                "reason": str(e)
            }


    async def get_idea_plans(self, user_prompt, original_prompt_language, file_attachments, focused_files, assets_link):
        plan = await self.get_idea_plan(user_prompt, original_prompt_language, file_attachments, focused_files, assets_link)
        return plan
