import uuid
from typing import Union, Dict, List, Generator, Literal

from ..types._message import Message
from ..types.usage import Usage
_MODELS_TYPE = Literal[ 'meta-llama/Meta-Llama-3.1-70B-Instruct',
    'CohereForAI/c4ai-command-r-plus-08-2024',
    'Qwen/Qwen2.5-72B-Instruct',
    'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF',
    'meta-llama/Llama-3.2-11B-Vision-Instruct',
    'NousResearch/Hermes-3-Llama-3.1-8B',
    'mistralai/Mistral-Nemo-Instruct-2407',
    'microsoft/Phi-3.5-mini-instruct']

class Messages:
    def __init__(self, llm):
        self.llm = llm
        self.system_prompt = ""



    def create(
            self,
            max_tokens:int|None = None,
            model: Union[_MODELS_TYPE, None] = None,
            prompt: str | None = None,
            messages: List[Dict[str, Union[str, int, float]]] | None = None,
            stream: bool = False,
            conversation: bool = False,
            **kwargs
    ) -> Message | Generator:
        if stream:
            return self.stream(model=model, messages=prompt or messages, conversation=conversation,
                               max_tokens=max_tokens,**kwargs)
        else:
            return self.invoke(model=model, messages= messages or prompt, conversation=conversation,
                               max_tokens=max_tokens, **kwargs)

    def _prepare_prompt(self, messages: List[Dict[str, Union[str, int, float]]]) -> str:
        prompt = ""
        for message in messages:
            role = message.get("role", "")
            content = message.get("content", "")
            prompt += f"{role.capitalize()}: {content}\n"
        return prompt.strip()

    def _stream_response(self, response: Generator[str, None, None]) -> Generator[str, None, None]:
        for chunk in response:
            yield chunk

    def _get_sys_and_user_prompt(self, messages: Union[List[Dict], str]):
        if isinstance(messages, str):
            return "", messages
        sp, up = "", ""
        for m in messages:
            if m['role'] == "system":
                sp = m['content']
            elif m['role'] == "user":
                up = m['content']
        return sp, up

    def invoke(self, messages: Union[List, str], model: str = None,
               max_tokens:int|None = None,
               conversation: Union[bool, None] = None,
               **kwargs):
        response:str = ""
        for _ in self.stream(
            model=model,
            messages=messages,
            conversation=conversation,
            max_tokens=max_tokens,
            **kwargs
        ):
            response+=_.content[0].text
        usage = Usage(input_tokens=10, output_tokens=10)
        return Message(
            id = str(uuid.uuid4()),
            role="assistant",
            content=[{ "type": "text", "text": response}],
            type='message',
            model=model if model else 'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF',
            conversation=conversation,
            usage = usage,
            **kwargs
        )

    def stream(
            self,
            messages: Union[List, str],
            model: str = None,
            max_tokens: int|None = None,
            conversation: Union[bool, None] = None,
            **kwargs):
        """new chat """
        user_prompt = self._update_dependencies(model_name=model,
                                                messages=messages,
                                                conversation=conversation)
        res = self.llm.chat(user_prompt, stream=True, **kwargs)
        for token in self._stream_with_chat(res,max_tokens):
            if token == '<MAX_TOKEN_REACHED>':
                break
            usage = Usage(input_tokens=10, output_tokens=10)
            yield Message(
                id = str(uuid.uuid4()),
                role="assistant",
                content=[{ "type": "text", "text": token}],
                type='message',
                model=model if model else 'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF',
                conversation=conversation,
                usage = usage,
                **kwargs
                    )


    def pstream(self, messages: Union[List[Dict], str], model: str = None,
                conversation=None,
                **kwargs):
        for _ in self.stream(messages, model_name=model,
                             conversation=conversation,
                             **kwargs):
            print(_, end="", flush=True)

    def _update_dependencies(self, model_name, messages, conversation):
        # Setting Defaults
        conversation = False if conversation is None else conversation
        curr_sys_prompt, user_prompt = self._get_sys_and_user_prompt(messages)

        if not conversation:  # Default conversation is False
            if curr_sys_prompt and (curr_sys_prompt != self.system_prompt):
                self.system_prompt = curr_sys_prompt
            self.llm.new_conversation(modelIndex=self.llm.MODELS.index(model_name) if model_name else 0,
                                      system_prompt=self.system_prompt,
                                      switch_to=True)
        return user_prompt

    def _stream_with_chat(self, res,max_tokens):
        token_count = 0
        for x in res:
            if x and isinstance(x, dict):
                res = x.get('token', "")
                if max_tokens and token_count>=max_tokens:
                    yield "<MAX_TOKEN_REACHED>"
                token_count+=1
                yield res
            else:
                yield "<MAX_TOKEN_REACHED>"
