import os
import sys
import random
import string
from .DeploymentCheckAgent import DeploymentCheckAgent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from fsd.log.logger_config import get_logger

logger = get_logger(__name__)

HOME_DIRECTORY = os.path.expanduser('~')
HIDDEN_ZINLEY_FOLDER = '.zinley'

class DeploymentControllerAgent:
    def __init__(self, repo):
        self.repo = repo
        self.deploymentCheckAgent = DeploymentCheckAgent(repo)

    async def get_started_deploy_pipeline(self):
        logger.info("\n #### `Deploy Agent` is checking if the current project is eligible for deployment")
        check_result = await self.deploymentCheckAgent.get_deployment_check_plans()
        result = check_result.get('result')
        
        if result in ["0", 0]:
            logger.info("\n #### `Deploy Agent` has determined that this project is not supported for deployment at this time!")
        elif result in ["1", 1]:
            path = check_result.get('full_project_path')
            if path != "null":
                logger.info("\n #### This project is eligible for deployment. `Deploy Agent` is proceeding with deployment now.")
                name_subdomain = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 15)))
                logger.info(f"\n #### Your website is live here: https://{name_subdomain}.zinley.xyz")
                self.repo.deploy_to_server(path, name_subdomain)
            else:
                logger.info("\n #### Unable to deploy. Please try again!")