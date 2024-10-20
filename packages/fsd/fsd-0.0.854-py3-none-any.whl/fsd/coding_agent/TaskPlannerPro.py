import os
import aiohttp
import json
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from json_repair import repair_json
from fsd.log.logger_config import get_logger

logger = get_logger(__name__)

class TaskPlannerPro:
    """
    A class to plan and manage tasks using AI-powered assistance.
    """

    def __init__(self, repo):
        """
        Initialize the TaskPlanner with necessary configurations.

        Args:
            directory_path (str): Path to the project directory.
            api_key (str): API key for authentication.
            endpoint (str): API endpoint URL.
            deployment_id (str): Deployment ID for the AI model.
            max_tokens (int): Maximum number of tokens for AI responses.
        """
        self.max_tokens = 4096
        self.repo = repo
        self.ai = AIGateway()

    async def get_task_plan(self, instruction, file_list, original_prompt_language):
        """
        Get a development plan based on the user's instruction using AI.

        Args:
            instruction (str): The user's instruction for task planning.
            file_list (list): List of available files.
            original_prompt_language (str): The language of the original prompt.

        Returns:
            dict: Development plan or error reason.
        """
        logger.debug("\n #### The `TaskPlanner` is initiating the process to generate a task plan")
        messages = [
            {
                "role": "system",
                "content": (
                    "You are a principal engineer specializing in Pyramid architecture. Generate an ordered list of task groups for implementing a system based on the user's instruction and provided file list.\n\n"
                    "Guidelines:\n"
                    "1. MUST Only include files from the provided 'file_list' for all task, no exception.\n"
                    "2. Prioritize grouping tasks by work type and system layers:\n"
                    "   a. Foundation layers (e.g., database setup, core utilities)\n"
                    "   b. Application layout and structure\n"
                    "   c. API integration and calls\n"
                    "   d. Feature implementation\n"
                    "   e. UI/UX enhancements\n"
                    "3. If grouping by work type is not feasible, group by tech stack.\n"
                    "4. Maximize concurrent execution within each group while adhering to dependencies.\n"
                    "5. Each group should contain tasks that can be worked on concurrently without violating dependencies or architectural principles.\n"
                    "6. Strictly enforce separation of concerns. Files that need context from others (e.g., main files, style files, script files) must be in appropriate groups.\n"
                    "7. Order groups following Pyramid architecture principles, ensuring each group provides necessary context for subsequent groups.\n"
                    "8. Provide `file_name` (full path) and `techStack` for each task.\n"
                    "9. Omit configuration, dependencies, and non-essential files.\n"
                    "10. Exclude all image files except `.svg` and all audio asset files.\n"
                    "11. For each tech stack or file type, create a separate group for a 'lead' file. The lead file must always be in its own group and implemented first. It defines the structure, patterns, and conventions for all other files in the same tech stack.\n"
                    "12. All other files in the same tech stack should strictly follow the lead file's structure and conventions. Group these follower files together when possible to maximize concurrent execution.\n"
                    "13. Apply the 'lead file' principle to all tech stacks, including SVG icons.\n"
                    "14. All SVG files must be strictly grouped together in the last group, without exception.\n"
                    "15. Critically analyze dependencies between files. If file A depends on file B, ensure B is implemented before A, but group independent files together when possible.\n"
                    "16. The order of groups is crucial. Always prioritize providing necessary context for subsequent tasks while maximizing concurrent execution within groups.\n"
                    "17. Each file should appear only once in the entire plan. Ensure correct ordering to avoid repetition.\n"
                    "18. Generate a commit message for the changes/updates, for specific work. The commit message must use the imperative tense and be structured as follows: <type>: <description>. Use these for <type>: bugfix, feature, optimize, update, config, document, format, restructure, enhance, verify. The commit message should be a single line.\n"
                    "Response Format:\n"
                    '{\n'
                    '    "groups": [\n'
                    '        {\n'
                    '            "group_name": "",\n'
                    '            "tasks": [\n'
                    '                {\n'
                    '                    "file_name": "/full/path/to/file.py",\n'
                    '                    "techStack": "python"\n'
                    '                }\n'
                    '            ]\n'
                    '        },\n'
                    '        {\n'
                    '            "group_name": "",\n'
                    '            "tasks": [\n'
                    '                {\n'
                    '                    "file_name": "/full/path/to/file.html",\n'
                    '                    "techStack": "html"\n'
                    '                }\n'
                    '            ]\n'
                    '        }\n'
                    '    ],\n'
                    '    "commits": ""\n'
                    '}'
                    f"Current working project is {self.repo.get_repo_path()}\n\n"
                    "Return only valid JSON without additional text or formatting."
                )
            },
            {
                "role": "user",
                "content": f"Create a grouped task list following Pyramid architecture using only files from:\n{file_list} - MUST Only include files from the provided 'file_list' for all task, no exception\n\nPrioritize grouping by work type and system layers (foundation, layout, API calls, etc.). If not feasible, group by tech stack. Maximize concurrent execution within groups. Place each lead file in its own group to be completed first, with other files in the same tech stack grouped together when possible. Order groups to provide context, adhering to Pyramid principles. Analyze dependencies: if A depends on B, B precedes A, but group independent files together. Each file appears once. Original instruction: {instruction}\n\n"
            }
        ]

        try:
            response = await self.ai.arch_prompt(messages, self.max_tokens, 0.2, 0.1)
            res = json.loads(response.choices[0].message.content)
            logger.debug("\n #### The `TaskPlanner` has successfully generated the task plan")
            return res
        except json.JSONDecodeError:
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            logger.debug("\n #### The `TaskPlanner` has repaired and processed the JSON response")
            return plan_json
        except Exception as e:
            logger.error(f" #### The `TaskPlanner` encountered an error while generating the task plan: {e}")
            return {"reason": str(e)}

    async def get_task_plans(self, instruction, file_lists, original_prompt_language):
        """
        Get development plans based on the user's instruction.

        Args:
            instruction (str): The user's instruction for task planning.

        Returns:
            dict: Development plan or error reason.
        """
        logger.debug("\n #### The `TaskPlanner` is generating task plans")
        plan = await self.get_task_plan(instruction, file_lists, original_prompt_language)
        logger.debug("\n #### The `TaskPlanner` has completed generating the task plans")
        return plan