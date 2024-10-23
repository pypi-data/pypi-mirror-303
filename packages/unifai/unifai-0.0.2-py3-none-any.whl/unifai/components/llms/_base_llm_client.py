from typing import Type, Optional, Sequence, Any, Union, Literal, TypeVar, Callable, Iterator, Iterable, Generator

from ..base_adapters._base_adapter import UnifAIAdapter
from .._base_component import convert_exceptions, convert_exceptions_generator

from unifai.types import Message, MessageChunk, Tool, ToolCall, Image, ResponseInfo, Embeddings, Usage
from unifai.exceptions import UnifAIError, ProviderUnsupportedFeatureError

T = TypeVar("T")

class LLMClient(UnifAIAdapter):
    provider = "base_ai"
    default_model = "mistral:7b-instruct"


    # List Models
    def list_models(self) -> list[str]:
        raise NotImplementedError("This method must be implemented by the subclass")    
    

    # Chat
    def _get_chat_response(
            self,
            stream: bool,
            messages: list[Any],
            model: str = default_model,
            system_prompt: Optional[str] = None,                    
            tools: Optional[list[dict]] = None,
            tool_choice: Optional[Union[Literal["auto", "required", "none"], dict]] = None,
            response_format: Optional[str] = None,            
            max_tokens: Optional[int] = None,
            frequency_penalty: Optional[float] = None,
            presence_penalty: Optional[float] = None,
            seed: Optional[int] = None,
            stop_sequences: Optional[list[str]] = None, 
            temperature: Optional[float] = None,
            top_k: Optional[int] = None,
            top_p: Optional[float] = None, 
            **kwargs
            ) -> Any:
        raise ProviderUnsupportedFeatureError(f"{self.provider} does not support chat")


    def chat(
            self,
            messages: list[T],     
            model: str = default_model,
            system_prompt: Optional[str] = None,                    
            tools: Optional[list[dict]] = None,
            tool_choice: Optional[Union[Literal["auto", "required", "none"], dict]] = None,
            response_format: Optional[str] = None,            
            max_tokens: Optional[int] = None,
            frequency_penalty: Optional[float] = None,
            presence_penalty: Optional[float] = None,
            seed: Optional[int] = None,
            stop_sequences: Optional[list[str]] = None, 
            temperature: Optional[float] = None,
            top_k: Optional[int] = None,
            top_p: Optional[float] = None, 
            **kwargs
            ) -> tuple[Message, T]:
        
        # kwargs["stream"] = False
        # kwargs["messages"] = messages
        # kwargs["model"] = model
        # kwargs["system_prompt"] = system_prompt
        # kwargs["tools"] = tools
        # kwargs["tool_choice"] = tool_choice
        # kwargs["response_format"] = response_format
        # kwargs["max_tokens"] = max_tokens
        # kwargs["frequency_penalty"] = frequency_penalty
        # kwargs["presence_penalty"] = presence_penalty
        # kwargs["seed"] = seed
        # kwargs["stop_sequences"] = stop_sequences
        # kwargs["temperature"] = temperature
        # kwargs["top_k"] = top_k
        # kwargs["top_p"] = top_p

        kwargs.update({k:v for k,v in locals().items() if k != "self" and k != "kwargs"})
        kwargs["stream"] = False        
        
        response = self.run_func_convert_exceptions(
            func=self._get_chat_response, 
            **kwargs
        )
        std_message, client_message = self.parse_message(response, **kwargs)
        return std_message, client_message
    

    def chat_stream(
            self,
            messages: list[T],     
            model: str = default_model,
            system_prompt: Optional[str] = None,                    
            tools: Optional[list[dict]] = None,
            tool_choice: Optional[Union[Literal["auto", "required", "none"], dict]] = None,
            response_format: Optional[str] = None,            
            max_tokens: Optional[int] = None,
            frequency_penalty: Optional[float] = None,
            presence_penalty: Optional[float] = None,
            seed: Optional[int] = None,
            stop_sequences: Optional[list[str]] = None, 
            temperature: Optional[float] = None,
            top_k: Optional[int] = None,
            top_p: Optional[float] = None, 
            **kwargs
            ) -> Generator[MessageChunk, None, tuple[Message, T]]:
        
        # kwargs["stream"] = True
        # kwargs["messages"] = messages
        # kwargs["model"] = model
        # kwargs["system_prompt"] = system_prompt
        # kwargs["tools"] = tools
        # kwargs["tool_choice"] = tool_choice
        # kwargs["response_format"] = response_format
        # kwargs["max_tokens"] = max_tokens
        # kwargs["frequency_penalty"] = frequency_penalty
        # kwargs["presence_penalty"] = presence_penalty
        # kwargs["seed"] = seed
        # kwargs["stop_sequences"] = stop_sequences
        # kwargs["temperature"] = temperature
        # kwargs["top_k"] = top_k
        # kwargs["top_p"] = top_p
        kwargs.update({k:v for k,v in locals().items() if k != "self" and k != "kwargs"})
        kwargs["stream"] = True

        response = self.run_func_convert_exceptions(
            func=self._get_chat_response, 
            **kwargs
        )
        std_message, client_message = yield from self.run_func_convert_exceptions_generator(
            func=self.parse_stream,
            response=response,
            **kwargs
        )        
        return std_message, client_message


    # Convert Objects from UnifAI to AI Provider format        
        # Messages
    def format_message(self, message: Message) -> Any:
        if message.role == "user":
            return self.format_user_message(message)
        elif message.role == "assistant":
            return self.format_assistant_message(message)
        elif message.role == "tool":
            return self.format_tool_message(message)
        elif message.role == "system":
            return self.format_system_message(message)        
        else:
            raise ValueError(f"Invalid message role: {message.role}")
    

    def format_user_message(self, message: Message) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")


    def format_assistant_message(self, message: Message) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")    
        

    def format_tool_message(self, message: Message) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")
    

    def split_tool_message(self, message: Message) -> Iterator[Message]:     
        yield message


    def format_system_message(self, message: Message) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")
    

    def format_messages_and_system_prompt(self, 
                                              messages: list[Message], 
                                              system_prompt_arg: Optional[str] = None
                                              ) -> tuple[list, Optional[str]]:
        raise NotImplementedError("This method must be implemented by the subclass")


        # Images
    def format_image(self, image: Image) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")    
    

        # Tools
    def format_tool_call(self, tool_call: ToolCall) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")
        

    def format_tool(self, tool: Tool) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")
        

    def format_tool_choice(self, tool_choice: str) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")    


        # Response Format
    def format_response_format(self, response_format: Union[str, dict]) -> Any:
        raise NotImplementedError("This method must be implemented by the subclass")



    # Convert Objects from AI Provider to UnifAI format    
        # Images
    def parse_image(self, response_image: Any, **kwargs) -> Image:
        raise NotImplementedError("This method must be implemented by the subclass")


        # Tool Calls
    def parse_tool_call(self, response_tool_call: Any, **kwargs) -> ToolCall:
        raise NotImplementedError("This method must be implemented by the subclass")
    

        # Response Info (Model, Usage, Done Reason, etc.)    
    def parse_done_reason(self, response_obj: Any, **kwargs) -> str|None:
        raise NotImplementedError("This method must be implemented by the subclass")
    

    def parse_usage(self, response_obj: Any, **kwargs) -> Usage|None:
        raise NotImplementedError("This method must be implemented by the subclass")
    

    def parse_response_info(self, response: Any, **kwargs) -> ResponseInfo:
        raise NotImplementedError("This method must be implemented by the subclass")
    

        # Assistant Messages (Content, Images, Tool Calls, Response Info)
    def parse_message(self, response: Any, **kwargs) -> tuple[Message, Any]:
        raise NotImplementedError("This method must be implemented by the subclass")     
    

    def parse_stream(self, response: Any, **kwargs) -> Generator[MessageChunk, None, tuple[Message, Any]]:
        raise NotImplementedError("This method must be implemented by the subclass")



