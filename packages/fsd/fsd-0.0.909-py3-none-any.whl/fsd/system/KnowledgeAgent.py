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
        knowledge_file_path = os.path.join(self.repo.get_repo_path(), '.zl-knowledge.txt')
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

                Extract only critically important information, focusing primarily on user preferences and dependencies. Update existing knowledge when significant changes occur. Focus on:
                - User preferences related to style, architecture, and language
                - Critical dependencies
                - Essential updates to existing information

                Keep points extremely concise. Limit to a maximum of 5 key points.
                Format: 
                # section name
                **Key:** Brief factual value

                Context to extract from:
                {user_prompt}

                Do not include any File Structure tree information or general information.
                NOTICE: ONLY use SEARCH/REPLACE blocks for KEY changes. Nothing else allowed.
                """
            }
        ]

        try:
            response = await self.ai.coding_prompt(messages, self.max_tokens, 0.7, 0.1)
            summary = response.choices[0].message.content
            logger.debug("\n #### The `KnowledgeAgent` has generated the summary and updated user behavior")
            return summary
        except Exception as e:
            logger.error(f" #### The `KnowledgeAgent` encountered an error: {e}")
            return f"Error: {str(e)}"

    async def get_knowledge_summary_plan(self, user_prompt):
        knowledge_file_path = os.path.join(self.repo.get_repo_path(), '.zl-knowledge.txt')
        if not os.path.exists(knowledge_file_path):
            try:
                open(knowledge_file_path, 'a').close()
            except IOError as e:
                logger.error(f"Error creating knowledge file: {e}")
                return

        logger.debug("\n #### The `KnowledgeAgent` is processing the knowledge summary and user behavior")
        summary = await self.get_knowledge_summary(user_prompt)
        logger.debug("\n #### The `KnowledgeAgent` has completed the knowledge summary and user behavior analysis")

        # Write the new summary to knowledge1.txt
        knowledge1_file_path = os.path.join(self.repo.get_repo_path(), 'knowledge1.txt')
        try:
            with open(knowledge1_file_path, 'w') as f:
                f.write(summary)
        except IOError as e:
            logger.error(f"Error writing to knowledge1.txt: {e}")
        
        # Handle the coding agent response without deleting existing content
        try:
            await self.knowledge_manager.handle_coding_agent_response(knowledge_file_path, summary)
        except Exception as e:
            logger.error(f"Error handling coding agent response: {e}")
