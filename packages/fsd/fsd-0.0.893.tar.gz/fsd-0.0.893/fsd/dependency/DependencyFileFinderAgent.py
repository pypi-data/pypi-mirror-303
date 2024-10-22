import os
import aiohttp
import asyncio
import json
import sys
from json_repair import repair_json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from fsd.log.logger_config import get_logger
logger = get_logger(__name__)

class DependencyFileFinderAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.ai = AIGateway()

    async def get_dependency_file_planning(self, tree):
        """
        Request dependency file planning from Azure OpenAI API for a given idea and project structure.

        Args:
            session (aiohttp.ClientSession): The aiohttp session to use for the request.
            idea (str): The general plan idea.
            tree (str): The project structure.

        Returns:
            dict: JSON response with the dependency file plan.
        """
        logger.debug("\n #### The `DependencyFileFinderAgent` is initiating dependency file planning")

        prompt = (
            f"Identify ALL main dependency, configuration, and installation files in the project structure. Include:\n"
            "1. Dependency files (e.g., requirements.txt, package.json, Pipfile)\n"
            "2. Config files (e.g., .npmrc, pip.conf)\n"
            "3. Environment files (e.g., .env, Dockerfile)\n"
            "4. Build scripts (e.g., Makefile, gulpfile.js)\n"
            "Exclude third-party libraries and generated folders.\n"
            "Carefully examine the provided project structure. Only include files that actually exist in the tree.\n"
            "Do not hallucinate or assume the existence of files not present in the given structure.\n"
            "If a typical dependency file is not found, do not include it in the response.\n"
            "IMPORTANT: Never include long, unnecessary files such as package-lock.json, yarn.lock, Podfile.lock, Gemfile.lock, poetry.lock, composer.lock, cargo.lock, etc.\n"
            "This applies to all types of projects including but not limited to: Node.js, Python, Ruby, Java, Kotlin, Swift, C#, Go, Rust, PHP, and any other programming language or framework.\n"
            "Return ONLY a JSON object:\n"
            "{\n"
            "    \"dependency_files\": [\"/path/to/file1\", \"/path/to/file2\"]\n"
            "}\n"
            f"Use full paths from: {self.repo.get_repo_path()}"
        )

        messages = [
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": f"This is the current project structure:\n{tree}\n"
            }
        ]

        try:
            logger.debug("\n #### The `DependencyFileFinderAgent` is sending a request to the AI Gateway")
            response = await self.ai.prompt(messages, self.max_tokens, 0.2, 0.1)
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            logger.debug("\n #### The `DependencyFileFinderAgent` encountered a JSON decoding error and is attempting to repair")
            good_json_string = repair_json(response.choices[0].message.content)
            plan_json = json.loads(good_json_string)
            return plan_json
        except Exception as e:
            logger.error(f" #### The `DependencyFileFinderAgent` encountered an error during dependency file planning: {e}")
            return {
                "reason": str(e)
            }


    async def get_dependency_file_plannings(self):
        logger.debug("\n #### The `DependencyFileFinderAgent` is starting to gather dependency file plannings")
        all_dependency_file_contents = self.repo.print_tree()

        logger.debug("\n #### The `DependencyFileFinderAgent` is processing the project structure")
        plan = await self.get_dependency_file_planning(all_dependency_file_contents)
        return plan
