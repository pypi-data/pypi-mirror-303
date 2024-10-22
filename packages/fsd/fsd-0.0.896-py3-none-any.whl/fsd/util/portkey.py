from portkey_ai import Portkey
from typing import Dict, List, Optional
import random
import asyncio
import time

from fsd.log.logger_config import get_logger
from fsd.util.utils import read_file_content, call_error_api

logger = get_logger(__name__)

class BaseModel:
    def __init__(self, api_key: str, virtual_key: str, config_id: str):
        try:
            self.portkey = Portkey(api_key=api_key, virtual_key=virtual_key, config=config_id)
        except Exception as e:
            error_message = f"Error initializing Portkey: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))

    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        raise NotImplementedError

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        raise NotImplementedError

class AzureModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using AzureModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 4096
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in AzureModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using AzureModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in AzureModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class BedrockModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using BedrockModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 4096,
            "model": "anthropic.claude-3-5-sonnet-20240620-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in BedrockModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using BedrockModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True,
            "model": "anthropic.claude-3-5-sonnet-20240620-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in BedrockModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise
    
    def generate_image(self, prompt: str, size: str = "1024x1024", model: str = "stability.stable-diffusion-xl-v1"):
        logger.debug(f"Using {model} for image generation")
        try:
            return self.portkey.images.generate(
                prompt=prompt,
                model=model
            )
        except Exception as e:
            error_message = f"Error in BedrockModel generate_image: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class BedrockOpusModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using BedrockOpusModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 4096,
            "model": "anthropic.claude-3-opus-20240229-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in BedrockOpusModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using BedrockOpusModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True,
            "model": "anthropic.claude-3-opus-20240229-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in BedrockOpusModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class GeminiModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using GeminiModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 4096,
            "model": "gemini-1.5-pro"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in GeminiModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using GeminiModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True,
            "model": "gemini-1.5-pro"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in GeminiModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class GeminiFlashModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using GeminiFlashModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 4096,
            "model": "gemini-1.5-flash"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in GeminiFlashModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using GeminiFlashModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True,
            "model": "gemini-1.5-flash"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in GeminiFlashModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class DalleModel(BaseModel):
    def generate_image(self, prompt: str, size: str = "1024x1024"):
        logger.debug("Using DALL-E 3 for image generation")
        try:
            return self.portkey.images.generate(prompt=prompt, size=size)
        except Exception as e:
            error_message = f"Error in DalleModel generate_image: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class LlamaModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using LlamaModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 2048,
            "model": "meta.llama3-1-70b-instruct-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in LlamaModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using LlamaModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 2048,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True,
            "model": "meta.llama3-1-70b-instruct-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in LlamaModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class CodingLlamaModel(BaseModel):
    async def prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float) -> Dict:
        logger.debug("Using CodingLlamaModel for prompt")
        common_params = {
            "messages": messages,
            "temperature": 0.2,
            "top_p": 0.1,
            "max_tokens": 2048,
            "model": "meta.llama3-1-405b-instruct-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in CodingLlamaModel prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

    async def stream_prompt(self, messages: List[Dict[str, str]], max_tokens: int, temperature: float, top_p: float):
        logger.debug("Using CodingLlamaModel for stream_prompt")
        common_params = {
            "messages": messages,
            "max_tokens": 2048,
            "temperature": 0.2,
            "top_p": 0.1,
            "stream": True,
            "model": "meta.llama3-1-405b-instruct-v1:0"
        }
        try:
            return await asyncio.to_thread(self.portkey.chat.completions.create, **common_params)
        except Exception as e:
            error_message = f"Error in CodingLlamaModel stream_prompt: {str(e)}"
            logger.error(error_message)
            call_error_api(error_message, str(e))
            raise

class AIGateway:
    _instance = None

    API_KEY = "Tf7rBh3ok+wNy+hzHum7dmizdBFh"
    CONFIG_ID = "pc-zinley-74e593"
    
    VIRTUAL_KEYS: Dict[str, str] = {
        "azure": "azure-7e4746",
        "bedrock": "bedrock-bfa916",
        "gemini": "gemini-b5d385",
        "dalle3": "dalle3-ea9815"
    }

    MODEL_WEIGHTS = {
        "azure": 0.9,
        "bedrock": 0.1,
    }

    STREAM_MODEL_WEIGHTS = {
        "azure": 0.9,
        "bedrock": 0.1,
    }

    STREAM_EXPLAINER_MODEL_WEIGHTS = {
        "azure": 1
    }

    STREAM_Architect_MODEL_WEIGHTS = {
        "bedrock": 1,
    }

    Architect_MODEL_WEIGHTS = {
        "bedrock": 1,
    }

    CODING_MODEL_WEIGHTS = {
        "bedrock": 1
    }

    IMAGE_MODEL_WEIGHTS = {
        "sdxl": 0.5,
        "dalle3": 0.5
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AIGateway, cls).__new__(cls)
            try:
                cls._instance.azure_model = AzureModel(cls.API_KEY, cls.VIRTUAL_KEYS["azure"], cls.CONFIG_ID)
                cls._instance.bedrock_model = BedrockModel(cls.API_KEY, cls.VIRTUAL_KEYS["bedrock"], cls.CONFIG_ID)
                cls._instance.bedrock_opus_model = BedrockOpusModel(cls.API_KEY, cls.VIRTUAL_KEYS["bedrock"], cls.CONFIG_ID)
                cls._instance.gemini_model = GeminiModel(cls.API_KEY, cls.VIRTUAL_KEYS["gemini"], cls.CONFIG_ID)
                cls._instance.gemini_flash_model = GeminiFlashModel(cls.API_KEY, cls.VIRTUAL_KEYS["gemini"], cls.CONFIG_ID)
                cls._instance.dalle3_model = DalleModel(cls.API_KEY, cls.VIRTUAL_KEYS["dalle3"], cls.CONFIG_ID)
                cls._instance.llama_model = LlamaModel(cls.API_KEY, cls.VIRTUAL_KEYS["bedrock"], cls.CONFIG_ID)
                cls._instance.coding_llama_model = CodingLlamaModel(cls.API_KEY, cls.VIRTUAL_KEYS["bedrock"], cls.CONFIG_ID)
                logger.debug("AIGateway initialized with all models")
            except Exception as e:
                error_message = f"Error initializing AIGateway: {str(e)}"
                logger.error(error_message)
                call_error_api(error_message, str(e))
        return cls._instance

    def _select_model(self, weights, exclude=None):
        available_models = {k: v for k, v in weights.items() if k != exclude}
        if not available_models:
            error_message = "No available models to choose from"
            logger.error(error_message)
            call_error_api(error_message, "")
            raise ValueError(error_message)
        selected_model = random.choices(list(available_models.keys()), 
                              weights=list(available_models.values()), 
                              k=1)[0]
        logger.debug(f"Selected model: {selected_model}")
        return selected_model

    async def prompt(self, 
                     messages: List[Dict[str, str]], 
                     max_tokens: int = 4096, 
                     temperature: float = 0.2, 
                     top_p: float = 0) -> Dict:
        logger.debug("Starting prompt method")
        tried_models = set()
        while len(tried_models) < len(self.MODEL_WEIGHTS):
            model_type = self._select_model(self.MODEL_WEIGHTS, exclude=tried_models)
            tried_models.add(model_type)
            try:
                logger.debug(f"Attempting to use {model_type} model")
                model = getattr(self, f"{model_type}_model")
                completion = await model.prompt(messages, max_tokens, temperature, top_p)
                logger.debug(f"Successfully received response from {model_type} model")
                return completion
            except Exception as e:
                logger.debug(f"Error in prompting {model_type} model: {str(e)}")
        
        error_message = "All models failed to respond"
        logger.debug(error_message)
        call_error_api(error_message, "")
        raise Exception(error_message)
    
    async def arch_prompt(self, 
                     messages: List[Dict[str, str]], 
                     max_tokens: int = 4096, 
                     temperature: float = 0.2, 
                     top_p: float = 0) -> Dict:
        logger.debug("Starting arch_prompt method")
        model_type = "bedrock"
        model = getattr(self, f"{model_type}_model")
        for attempt in range(3):
            try:
                logger.debug(f"Attempt {attempt + 1}: Using {model_type} model for architecture")
                completion = await model.prompt(messages, max_tokens, temperature, top_p)
                logger.debug(f"Successfully received response from {model_type} model for architecture")
                return completion
            except Exception as e:
                logger.debug(f"Error in prompting {model_type} model for architecture: {str(e)}")
                if attempt < 2:
                    logger.debug(f"Retrying in 1-3 seconds...")
                    await asyncio.sleep(random.uniform(1, 3))
                else:
                    error_message = "All attempts failed for arch_prompt"
                    logger.debug(error_message)
                    call_error_api(error_message, str(e))
                    raise Exception(error_message)
    
    async def coding_prompt(self, 
                     messages: List[Dict[str, str]], 
                     max_tokens: int = 4096, 
                     temperature: float = 0.2, 
                     top_p: float = 0) -> Dict:
        logger.debug("Starting coding_prompt method")
        model_type = "bedrock"
        model = getattr(self, f"{model_type}_model")
        for attempt in range(3):
            try:
                logger.debug(f"Attempt {attempt + 1}: Using {model_type} model for coding")
                completion = await model.prompt(messages, max_tokens, temperature, top_p)
                logger.debug(f"Successfully received response from {model_type} model for coding")
                return completion
            except Exception as e:
                logger.debug(f"Error in prompting {model_type} model for coding: {str(e)}")
                if attempt < 2:
                    logger.debug(f"Retrying in 2-3 seconds...")
                    await asyncio.sleep(random.uniform(2, 3))
                else:
                    error_message = "All attempts failed for coding prompt"
                    logger.debug(error_message)
                    call_error_api(error_message, str(e))
                    raise Exception(error_message)

    async def stream_prompt(self, 
                     messages: List[Dict[str, str]], 
                     max_tokens: int = 4096, 
                     temperature: float = 0.2, 
                     top_p: float = 0):
        logger.debug("Starting stream_prompt method")
        tried_models = set()
        while len(tried_models) < len(self.STREAM_MODEL_WEIGHTS):
            model_type = self._select_model(self.STREAM_MODEL_WEIGHTS, exclude=tried_models)
            tried_models.add(model_type)
            try:
                logger.debug(f"Attempting to use {model_type} model for streaming")
                model = getattr(self, f"{model_type}_model")
                chat_completion_stream = await model.stream_prompt(messages, max_tokens, temperature, top_p)
                logger.debug(f"Successfully received streaming response from {model_type} model")
                final_response = ""
                for chunk in chat_completion_stream:
                    if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        print(content, end='', flush=True)
                        final_response += content
                print()
                return final_response
            except Exception as e:
                logger.debug(f"Error in streaming from {model_type} model: {str(e)}")
        
        error_message = "All models failed to respond for stream prompt"
        logger.debug(error_message)
        call_error_api(error_message, "")
        raise Exception(error_message)
    
    async def explainer_stream_prompt(self, 
                     messages: List[Dict[str, str]], 
                     max_tokens: int = 4096, 
                     temperature: float = 0.2, 
                     top_p: float = 0):
        logger.debug("Starting explainer_stream_prompt method")
        tried_models = set()
        while len(tried_models) < len(self.STREAM_EXPLAINER_MODEL_WEIGHTS):
            model_type = self._select_model(self.STREAM_EXPLAINER_MODEL_WEIGHTS, exclude=tried_models)
            tried_models.add(model_type)
            try:
                logger.debug(f"Attempting to use {model_type} model for streaming")
                model = getattr(self, f"{model_type}_model")
                chat_completion_stream = await model.stream_prompt(messages, max_tokens, temperature, top_p)
                logger.debug(f"Successfully received streaming response from {model_type} model")
                final_response = ""
                for chunk in chat_completion_stream:
                    if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        print(content, end='', flush=True)
                        final_response += content
                print()
                return final_response
            except Exception as e:
                logger.debug(f"Error in streaming from {model_type} model: {str(e)}")
        
        error_message = "All models failed to respond for explainer stream prompt"
        logger.debug(error_message)
        call_error_api(error_message, "")
        raise Exception(error_message)
    
    async def arch_stream_prompt(self, 
                     messages: List[Dict[str, str]], 
                     max_tokens: int = 4096, 
                     temperature: float = 0.2, 
                     top_p: float = 0):
        logger.debug("Starting arch_stream_prompt method")
        model_type = "bedrock"
        max_retries = 3
        for attempt in range(max_retries):
            try:
                logger.debug(f"Attempt {attempt + 1}: Using {model_type} model for streaming")
                model = getattr(self, f"{model_type}_model")
                chat_completion_stream = await model.stream_prompt(messages, max_tokens, temperature, top_p)
                logger.debug(f"Successfully received streaming response from {model_type} model")
                final_response = ""
                for chunk in chat_completion_stream:
                    if chunk.choices and len(chunk.choices) > 0 and chunk.choices[0].delta.content is not None:
                        content = chunk.choices[0].delta.content
                        print(content, end='', flush=True)
                        final_response += content
                print()
                return final_response
            except Exception as e:
                logger.debug(f"Error in streaming from {model_type} model: {str(e)}")
                if attempt < max_retries - 1:
                    logger.debug(f"Retrying in 2-3 seconds...")
                    await asyncio.sleep(random.uniform(2, 3))
                else:
                    error_message = "All attempts failed for arch stream prompt"
                    logger.debug(error_message)
                    call_error_api(error_message, str(e))
                    raise Exception(error_message)

    def generate_image(self, prompt: str, size: str = "1024x1024"):
        logger.debug("Starting image generation")
        tried_models = set()
        while len(tried_models) < len(self.IMAGE_MODEL_WEIGHTS):
            model_type = self._select_model(self.IMAGE_MODEL_WEIGHTS, exclude=tried_models)
            tried_models.add(model_type)
            logger.debug(f"Attempting to use {model_type} model for image generation")
            try:
                if model_type == "dalle3":
                    image = self.dalle3_model.generate_image(prompt, size)
                else:
                    model_id = {
                        "sdxl": "stability.stable-diffusion-xl-v1",
                        "stable_image_core": "stability.stable-image-core-v1:0",
                        "sd3_large": "stability.sd3-large-v1:0",
                        "stable_image_ultra": "stability.stable-image-ultra-v1:0"
                    }[model_type]
                    logger.debug(f"Calling to use {model_id} model for image generation")
                    image = self.bedrock_model.generate_image(prompt, size, model_id)
                logger.debug(f"Successfully generated image with {model_type} model")
                
                return image
            except Exception as e:
                logger.debug(f"Error in generating image with {model_type}: {str(e)}")
                if len(tried_models) == len(self.IMAGE_MODEL_WEIGHTS):
                    error_message = "All image generation models failed"
                    call_error_api(error_message, str(e))
                    raise Exception(error_message)
