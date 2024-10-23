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

class CompileProjectAnalysAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.conversation_history = []
        self.ai = AIGateway()

    def clear_conversation_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
        logger.debug("Conversation history cleared by CompileProjectAnalysAgent")

    def remove_latest_conversation(self):
        """Remove the latest conversation from the history."""
        if self.conversation_history:
            self.conversation_history.pop()
            logger.debug("Latest conversation entry removed by CompileProjectAnalysAgent")

    def initial_setup(self, dependency_files, OS_architecture):
        """
        Initialize the conversation with a system prompt and user context.
        """
        logger.debug("CompileProjectAnalysAgent initializing conversation setup")

        tree_contents = self.repo.print_tree()

        dependency_files_path = dependency_files

        all_file_contents = ""
        if dependency_files_path:
            for file_path in dependency_files_path:
                file_content = read_file_content(file_path)
                if file_content:
                    all_file_contents += f"\n\nFile: {file_path}:\n{file_content}"
        else:
            all_file_contents = "No dependency files found."

        system_prompt = (
            f"You are a senior DevOps engineer. Analyze the project structure and develop a concise plan for setting up and compiling the project for local development using CLI commands. Follow these guidelines:\n\n"
            f"Working directory: {self.repo.get_repo_path()}\n"
            "1. Provide a SHORT TITLE for the setup process.\n"
            "2. ANALYZE the project structure.\n"
            "3. For empty/incomplete projects:\n"
               "   a. Create necessary directories/files.\n"
               "   b. Provide CLI commands for file creation.\n"
            "4. For existing projects:\n"
               "   a. Analyze the structure for config files, build scripts, etc.\n"
               "   b. Don't assume existence of files not shown.\n"
            "5. Focus on local development setup only.\n"
            f"6. Always navigate to the right path in {self.repo.get_repo_path()} and the right relative path from the provided instruction.\n"
            "7. Explain steps concisely, referencing specific file names/paths.\n"
            "8. Provide CLI commands for setup, file creation, dependency installation, and compilation.\n"
            "9. For new files, provide exact CLI commands to create and populate.\n"
            "10. Navigate back to working directory before major operations.\n"
            "11. Provide each task as a separate, logical step.\n"
            "12. Follow best practices for dependency management (e.g., venv for Python, npm for Node.js).\n"
            "13. Create dependency config files if missing.\n"
            "14. Check project structure before suggesting file operations.\n"
            "15. Include compilation steps for compiled languages.\n"
            "16. Provide steps for multiple scenarios if project type is unclear.\n"
            "17. Don't specify dependency versions unless requested.\n"
            "18. If no dependency files are found or provided, initialize appropriate ones based on the project type.\n"
            "19. Ignore tasks like creating minimal index.html files or touching any coding files. Focus only on dependency setup.\n"
            "20. Use nice format in bash markdown for all bash commands.\n"
            "21. Include a profile example for bash commands to show execution time.\n\n"

            "Response structure:\n"
            "- Title: [Short setup process title]\n"
            "- Explanation: [Brief process overview]\n"
            "- Steps: [Numbered list of concise steps with CLI commands]\n\n"

            f"CRITICAL: Limit to local development setup. Start with 'cd {self.repo.get_repo_path()}' and end with final compilation/run command. Use exact file names/paths. Provide each CLI command as a separate step. If no dependency files exist, create appropriate ones. Focus solely on dependency setup and ignore tasks related to creating or modifying code files. Ensure all bash commands are formatted in nice bash markdown. Include a profile example for bash commands to show execution time."
        )

        self.conversation_history.append({"role": "system", "content": system_prompt})
        self.conversation_history.append({"role": "user", "content":  f"Here are the current dependency files: {all_file_contents}\n\nProject structure: {tree_contents}\n\nOS Architecture: {OS_architecture}"})
        self.conversation_history.append({"role": "assistant", "content": "Got it! Give me user prompt so i can support them."})
        logger.debug("CompileProjectAnalysAgent completed initial conversation setup")

    async def get_idea_plan(self, user_prompt, original_prompt_language, file_attachments, focused_files, assets_link):
        """
        Get development plan for all txt files from Azure OpenAI based on user prompt.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Development plan or error reason.
        """
        logger.debug("CompileProjectAnalysAgent generating idea plan based on user prompt")
        prompt = (
             f"Follow the user prompt strictly and provide a well-organized response with clear format and good spacing:\n{user_prompt}\n\n"
             f"Respond using the language: {original_prompt_language}\n\n"
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
            response = await self.ai.arch_stream_prompt(self.conversation_history, self.max_tokens, 0.2, 0.1)
            return response
        except Exception as e:
            logger.error(f"AIGateway encountered an error while generating idea plan: {e}")
            return {
                "reason": str(e)
            }


    async def get_idea_plans(self, user_prompt, original_prompt_language, file_attachments, focused_files, assets_link):
        """
        Get development plans for a list of txt files from Azure OpenAI based on user prompt.

        Args:
            files (list): List of file paths.
            user_prompt (str): The user's prompt.

        Returns:
            dict: Development plan or error reason.
        """
        plan = await self.get_idea_plan(user_prompt, original_prompt_language, file_attachments, focused_files, assets_link)
        return plan
