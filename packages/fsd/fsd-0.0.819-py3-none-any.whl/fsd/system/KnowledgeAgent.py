import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.util.portkey import AIGateway
from fsd.log.logger_config import get_logger
from .FileContentManager import FileContentManager
from fsd.util.utils import read_file_content
logger = get_logger(__name__)

class KnowledgeAgent:
    def __init__(self, repo):
        self.repo = repo
        self.max_tokens = 4096
        self.knowledge_manager = FileContentManager()
        self.ai = AIGateway()

    async def get_knowledge_summary(self, user_prompt):
        """
        Get a concise summary of key points from the user prompt and learn user behavior.

        Args:
            user_prompt (str): The user's prompt.

        Returns:
            str: Markdown formatted summary of key points.
        """
        logger.debug("\n #### The `KnowledgeAgent` is generating a summary and learning user behavior")
        knowledge_file_path = os.path.join(self.repo.get_repo_path(), '.knowledge.md')
        current_summary = ""

        file_content = read_file_content(knowledge_file_path)
        if file_content:
            current_summary += f"\n\nFile: {knowledge_file_path}: {file_content}"

        system_prompt = """You are an ELITE engineering specialist working as a knowledge agent. You will receive detailed instructions to work on. Follow these guidelines strictly:
                1. For ALL knowledge changes, additions, or deletions, you MUST ALWAYS use the following *SEARCH/REPLACE block* format:

                   <<<<<<< SEARCH
                   [Existing knowledge to be replaced, if any]
                   =======
                   [New or modified knowledge]
                   >>>>>>> REPLACE

                2. For new knowledge additions, use an empty SEARCH section:

                   <<<<<<< SEARCH
                   =======
                   [New knowledge to be added]
                   >>>>>>> REPLACE

                3. Ensure that the SEARCH section exactly matches the existing knowledge, including whitespace and comments.

                4. For large files, focus on the relevant sections. Use comments to indicate skipped portions:
                   // ... existing knowledge ...

                5. For complex changes or large files, break them into multiple SEARCH/REPLACE blocks.

                6. CRITICAL: NEVER provide knowledge snippets, suggestions, or examples outside of the SEARCH/REPLACE block format. ALL knowledge must be within these blocks.

                7. Do not provide explanations, ask questions, or engage in discussions. Only return SEARCH/REPLACE blocks.

                8. If a user's request cannot be addressed solely through SEARCH/REPLACE blocks, do not respond.

                Remember, your responses should ONLY contain SEARCH/REPLACE blocks for knowledge changes. Nothing else is allowed."""
        messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"""Current knowledge context: {current_summary}

                ONLY extract key information from the context AND update knowledge. Do not add assumptions or extra details.
                Update only the content within the existing 13 sections. Do not modify section headings.
                Analyze context:
                {user_prompt}

                NOTICE: Your response should ONLY contain SEARCH/REPLACE blocks for KEY changes. Nothing else is allowed.
                """
            }
        ]

        logger.info(messages)

        try:
            response = await self.ai.prompt(messages, self.max_tokens, 0.7, 0.1)
            summary = response.choices[0].message.content
            
            # Simple user behavior learning (example)
            keywords = ['code', 'bug', 'caution', 'error']
            for keyword in keywords:
                if keyword in user_prompt.lower():
                    self.user_behavior[keyword] = self.user_behavior.get(keyword, 0) + 1
            
            logger.debug("\n #### The `KnowledgeAgent` has generated the summary and updated user behavior")
            return summary
        except Exception as e:
            logger.error(f" #### The `KnowledgeAgent` encountered an error: {e}")
            return f"Error: {str(e)}"

    async def get_knowledge_summary_plan(self, user_prompt):
        knowledge_file_path = os.path.join(self.repo.get_repo_path(), '.knowledge.md')
        if not os.path.exists(knowledge_file_path):
            with open(knowledge_file_path, 'w') as f:
                # Create a new file with template sections
                template = """# Knowledge Summary

1. User Preferences

2. Project-Specific Settings

3. User Workflow

4. Code Snippets/Best Practices

5. Documentation & Commenting

6. Optimization & Performance Preferences

7. User Interaction Preferences

8. Collaboration & Communication

9. Learning & Feedback

10. Data Handling & Storage

11. Frequent Bugs

12. Cautious Areas

"""
        f.write(template)

        logger.info("\n #### The `KnowledgeAgent` is processing the knowledge summary and user behavior")
        summary = await self.get_knowledge_summary(user_prompt)
        logger.info("\n #### The `KnowledgeAgent` has completed the knowledge summary and user behavior analysis")
        logger.info(f"Summary: {summary}")


        # Write the new summary to knowledge1.txt
        knowledge1_file_path = os.path.join(self.repo.get_repo_path(), 'knowledge1.txt')
        with open(knowledge1_file_path, 'w') as f:
            f.write(summary)
        
        # Handle the coding agent response without deleting existing content
        await self.knowledge_manager.handle_coding_agent_response(knowledge_file_path, summary)
