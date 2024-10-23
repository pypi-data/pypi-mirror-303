import os
import asyncio
import base64
from typing import Dict, List, Tuple
from fsd.log.logger_config import get_logger
from fsd.util.portkey import AIGateway
from PIL import Image
import io
import aiohttp

logger = get_logger(__name__)

class ImageGenAgent:
    """
    An agent responsible for generating images based on provided prompts and parameters.
    """

    def __init__(self, repo):
        self.repo = repo
        self.ai = AIGateway()

    def validate_dimensions(self, dalle_dimension: str) -> str:
        """
        Validates the requested image dalle_dimension against supported sizes.
        """
        supported_sizes = ['1024x1024', '1792x1024', '1024x1792']
        if dalle_dimension in supported_sizes:
            return dalle_dimension
        else:
            logger.debug(f" #### Unsupported size '{dalle_dimension}'. Defaulting to '1024x1024'.")
            return '1024x1024'  # Default to a supported size

    def normalize_image_format(self, image_format: str) -> str:
        """
        Normalizes the image format string for compatibility with PIL.
        """
        format_upper = image_format.upper()
        return 'JPEG' if format_upper == 'JPG' else format_upper

    async def save_image_data(self, image_data: str, file_path: str, image_format: str):
        """
        Saves base64-encoded image data to a file asynchronously.
        """
        try:
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
            image_format = self.normalize_image_format(image_format)
            folder_path = os.path.dirname(file_path)
            
            # Check if the folder exists and is accessible
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
            elif not os.access(folder_path, os.W_OK):
                logger.error(f" #### Folder {folder_path} is not writable. Attempting to remove and recreate.")
                os.rmdir(folder_path)
                os.makedirs(folder_path, exist_ok=True)
            
            # Check if the folder is empty
            if not os.listdir(folder_path):
                logger.debug(f" #### Folder {folder_path} is empty. Proceeding with save.")
            
            await asyncio.to_thread(image.save, file_path, format=image_format)
            logger.debug(f"\n #### `Image Gen Agent` saved image to {os.path.basename(file_path)}.")
        except Exception as e:
            logger.error(f" #### Error saving image: {str(e)}")
            raise

    async def save_and_resize_image(self, image_data: str, file_path: str, image_format: str, target_size: Tuple[int, int]):
        """
        Saves and resizes base64-encoded image data to a file asynchronously.
        """
        try:
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))
            image = await asyncio.to_thread(self.resize_image_with_aspect_ratio, image, target_size)
            image_format = self.normalize_image_format(image_format)
            folder_path = os.path.dirname(file_path)
            
            # Check if the folder exists and is accessible
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
            elif not os.access(folder_path, os.W_OK):
                logger.error(f" #### Folder {folder_path} is not writable. Attempting to remove and recreate.")
                os.rmdir(folder_path)
                os.makedirs(folder_path, exist_ok=True)
            
            # Check if the folder is empty
            if not os.listdir(folder_path):
                logger.debug(f" #### Folder {folder_path} is empty. Proceeding with save.")
            
            await asyncio.to_thread(image.save, file_path, format=image_format)
            logger.info(f"\n #### `ImageGenAgent` saved and resized image to {target_size} at {os.path.basename(file_path)}.")
        except Exception as e:
            logger.error(f" #### Error saving and resizing image: {str(e)}")
            raise

    def resize_image_with_aspect_ratio(self, image: Image.Image, target_size: Tuple[int, int]) -> Image.Image:
        """
        Resizes an image while maintaining aspect ratio and crops it to fit the target size.
        """
        target_width, target_height = target_size
        target_aspect = target_width / target_height
        image_aspect = image.width / image.height
        if image_aspect > target_aspect:
            new_height = target_height
            new_width = int(new_height * image_aspect)
        else:
            new_width = target_width
            new_height = int(new_width / image_aspect)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2
        return image.crop((left, top, right, bottom))

    def extract_image_data(self, response):
        """
        Extracts image data from the API response, either base64-encoded or via URL.
        """
        try:
            if hasattr(response, 'error') and response.error:
                error_message = getattr(response.error, 'message', 'Unknown error')
                raise Exception(f"API error: {error_message}")
            if hasattr(response, 'data') and response.data:
                data_item = response.data[0]
            else:
                raise ValueError("No image data in response.")
            image_data_b64 = getattr(data_item, 'b64_json', None)
            if image_data_b64:
                return image_data_b64, 'base64'
            else:
                image_url = getattr(data_item, 'url', None)
                if image_url:
                    return image_url, 'url'
                else:
                    raise ValueError("No image data (base64 or URL) found.")
        except Exception as e:
            logger.error(f" #### Failed to extract image data: {str(e)}")
            logger.debug(f" #### Response content: {response}")
            raise

    async def fetch_and_save_image_from_url(self, url: str, file_path: str, image_format: str, target_size: Tuple[int, int] = None):
        """
        Fetches an image from a URL and saves (and optionally resizes) it to a file.
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        image_bytes = await resp.read()
                        image = Image.open(io.BytesIO(image_bytes))
                        if target_size:
                            image = await asyncio.to_thread(self.resize_image_with_aspect_ratio, image, target_size)
                        image_format = self.normalize_image_format(image_format)
                        folder_path = os.path.dirname(file_path)
                        
                        # Check if the folder exists and is accessible
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path, exist_ok=True)
                        elif not os.access(folder_path, os.W_OK):
                            logger.error(f" #### Folder {folder_path} is not writable. Attempting to remove and recreate.")
                            os.rmdir(folder_path)
                            os.makedirs(folder_path, exist_ok=True)
                        
                        # Check if the folder is empty
                        if not os.listdir(folder_path):
                            logger.debug(f" #### Folder {folder_path} is empty. Proceeding with save.")
                        
                        await asyncio.to_thread(image.save, file_path, format=image_format)
                        logger.debug(f" #### `ImageGenAgent` fetched and saved image to {os.path.basename(file_path)}")
                    else:
                        raise Exception(f"Failed to fetch image. HTTP status: {resp.status}")
        except Exception as e:
            logger.error(f" #### Error fetching and saving image: {str(e)}")
            raise

    async def generate_image(self, prompt: str, dalle_dimension: str, actual_dimension: str, image_format: str, file_path: str):
        """
        Generates an image using the AI model and saves it to a file.
        """
        max_retries = 3
        for attempt in range(max_retries):
            try:
                supported_size = self.validate_dimensions(dalle_dimension)
                response = await asyncio.to_thread(self.ai.generate_image, prompt=prompt, size=supported_size)
                image_data, data_type = self.extract_image_data(response)
                if data_type == 'base64':
                    if dalle_dimension != actual_dimension:
                        target_size = tuple(map(int, actual_dimension.lower().split('x')))
                        await self.save_and_resize_image(image_data, file_path, image_format, target_size)
                    else:
                        await self.save_image_data(image_data, file_path, image_format)
                elif data_type == 'url':
                    target_size = tuple(map(int, actual_dimension.lower().split('x'))) if dalle_dimension != actual_dimension else None
                    await self.fetch_and_save_image_from_url(image_data, file_path, image_format, target_size)
                else:
                    raise ValueError("Unsupported image data type.")
                logger.info(f"\n #### `Image Gen Agent` generated {os.path.basename(file_path)}.")
                break
            except Exception as e:
                logger.error(f" #### Error during attempt {attempt + 1}: {str(e)}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(2)
                else:
                    logger.error("\n #### Max retries reached. Operation aborted.")
                    logger.debug(f" #### Prompt: {prompt}")
                    raise

    async def process_image_generation_pro(self, steps: List[Dict]):
        """
        Processes image generation steps concurrently, limited to 5 at a time.
        """
        async def generate_image_task(step):
            try:
                await self.generate_image(
                    prompt=step['prompt'],
                    dalle_dimension=step['dalle_dimension'],
                    actual_dimension=step['actual_dimension'],
                    image_format=step['format'],
                    file_path=step['file_path']
                )
                filename = os.path.basename(step['file_path'])
                logger.info(f"![{filename}]({step['file_path']})")
            except Exception as e:
                logger.error(f" #### Failed to generate image {step}: {str(e)}")

        semaphore = asyncio.Semaphore(10)  # Limit to 5 concurrent tasks

        async def bounded_generate_image_task(step):
            async with semaphore:
                await generate_image_task(step)

        tasks = [bounded_generate_image_task(step) for step in steps]
        await asyncio.gather(*tasks)

    async def process_image_generation(self, steps: List[Dict]):
        """
        Processes each image generation step sequentially.
        """
        for step in steps:
            try:
                await self.generate_image(
                    prompt=step['prompt'],
                    dalle_dimension=step['dalle_dimension'],
                    actual_dimension=step['actual_dimension'],
                    image_format=step['format'],
                    file_path=step['file_path']
                )

                filename = os.path.basename(step['file_path'])
                logger.info(f"![{filename}]({step['file_path']})")

            except Exception as e:
                logger.error(f" #### Failed to generate image {step}: {str(e)}")
                continue

    async def generate_images(self, task: Dict, tier, snow_mode):
        """
        Generates images based on the given task.
        """
        steps = task.get('steps', [])

        if not steps:
            logger.debug("\n #### No steps for image generation.")
            return
        logger.info(f"\n #### `Image Gen Agent` starting generation of {len(steps)} image(s).")
        if tier == "Pro" and snow_mode:
            logger.info(" #### `Image Gen Agent` will start image generation in Snow mode.")
            await self.process_image_generation_pro(steps)
        else:
            logger.info(" #### `Image Gen Agent` starting image generation in normal mode.")
            await self.process_image_generation(steps)
       
        logger.info(" #### `Image Gen Agent` completed image generation.")
        logger.info("-------------------------------------------------")