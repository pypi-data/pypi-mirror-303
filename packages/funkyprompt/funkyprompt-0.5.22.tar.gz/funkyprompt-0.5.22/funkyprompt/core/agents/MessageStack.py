import typing
from pydantic import BaseModel, Field, model_serializer, model_validator
from funkyprompt.core import AbstractModel, AbstractEntity
import datetime
import json
from funkyprompt.core.agents import CallingContext
from funkyprompt import LanguageModelProvider
from pydantic._internal._model_construction import ModelMetaclass

class Message(BaseModel):
    role: str
    content: str | dict
    name: typing.Optional[str] = Field(
        description="for example function names", default=None
    )


class UserMessage(Message):
    role: str = "user"

class SystemMessage(Message):
    role: str = "system"

class AssistantMessage(Message):
    role: str = "assistant"

class MessageStack(BaseModel):
    """
    Message stack abstracts our notion of changing message context and provides some basic helpers
    Experiment with;
    - type prompts
    - known entities
    - smart pruning of context
    - function patterns
    """

    model: AbstractModel | type = Field(
        description="The Model for the guidance of the agents - a model contains Config and functions and is required - it can be anything with a `get_model_description` method for this purpose"
    )

    current_date: typing.Optional[datetime.datetime] = Field(
        description="Id data is added to messages it can guide agents that are confused about the fourth dimension",
        default=None,
    )

    # could add base messages to but depending on what they are they could be typed things

    function_names: typing.Optional[typing.List[str]] = Field(
        description="Listing function names can be a useful hint", default_factory=list
    )

    question: typing.Optional[str|typing.List[str]] = Field(
        description="The users question", default=None
    )

    messages: typing.Optional[typing.List[Message]] = Field(
        description="A list of messages sent to the language mode context",
        default_factory=list,
    )

    language_model_provider: typing.Optional[LanguageModelProvider] = Field(
        description="The model provider can affect the serialization", default=None
    )

    known_entities: typing.Optional[typing.List[AbstractEntity]] = Field(
        default_factory=list,
        description="Known entities can be useful metadata if we encounter a small number of entities in the session - it costs context but if used can be powerful metadata",
    )

    @model_validator(mode="before")
    def _create(cls, values):
        """
        we basically want a prompt and a question but we can add in other stuff too
        """
        messages = values.get('messages') or []

        if not messages:
            """these are the default initial messages in the stack"""
            model = values.get("model")
            prompt = """Answer the users questions using 1. provided data, 2. any provided functions or 3. world knowledge depending on the context. 4. Call the help function before conceding.
            Use any Structured Response Type details you are given to respond in JSON format otherwise response in natural language.
            Always check that you can use functions that you have. 
            Do not use a search function facilities if another function or existing data can be used in place and do not call functions if world knowledge will suffice."""
            
            #model description is more lightweight - there may be instances when its enough
            #e.g. the entity type and functions can be determine at runtime via lookups (TODO: optimize this)
            
            if not isinstance(model, ModelMetaclass) and isinstance(model,AbstractModel) and  hasattr(model, "get_instance_model_as_prompt"): #experimentally support model instances because we can load specific agents from data
                prompt += (model.get_instance_model_as_prompt() or 'answer the users question\n')  
            elif hasattr(model, "get_model_as_prompt"):
                prompt += (model.get_model_as_prompt() or 'answer the users question\n')
            elif hasattr(model, "get_model_description"):
                prompt += (model.get_model_description() or 'answer the users question\n')
            """update messages from context, model and question"""

            messages.append(SystemMessage(content=prompt))
            date = values.get("current_date")
            if date:
                """this is added because sometimes it screws up date based queries"""
                messages.append(
                    SystemMessage(
                        content=f"I observe the current date is {date} so I should take that into account if asked questions about time"
                    )
                )

            function_names = values.get("function_names")
            if function_names:
                """this is added because sometimes it seems to need this nudge (TODO:)"""
                messages.append(
                    UserMessage(
                        content=f"""Using the following functions by default {function_names} and in some cases expect to be able to search and load others. 
                        On encountering a new function by name (e.g. in the list of Available Functions) it can be activated without asking the user, calling it where possible."""
                    )
                )
                """the alternating pattern of user and assistant as done to respect claude"""
                messages.append(
                    AssistantMessage(
                        content=f"""I acknowledge the functions that are ready for use and will activate or search for others that i need"""
                    )
                )

            """finally add the users question"""
            if values.get("question"):
                messages.append(UserMessage(content=str(values.get("question"))))

        values["messages"] = messages

        return values

    def reset(cls):
        """returns the message stack only with the model elements"""
        data = dict(vars(cls))
        data["messages"] = []
        return MessageStack(model=cls.model, current_date=cls.current_date)

    def add(cls, message: Message | dict):
        """augment the message and retain all the other stuff"""
        if isinstance(message, dict):
            message = Message(**message)
        messages = cls.messages
        messages.append(message)
        data = dict(vars(cls))
        data["messages"] = messages

        return MessageStack(**data)

    def add_system_message(cls, data: str):
        """add string or dict content as system message"""
        return cls.add(SystemMessage(content=data))

    def add_user_message(cls, data: str | dict):
        """add string or dict content as system message"""
        return cls.add(UserMessage(content=data))
    
    def add_assistant_message(cls, data: str | dict):
        """add string or dict content as system message"""
        return cls.add(AssistantMessage(content=data))

    @classmethod
    def structure_question(
        cls, question: str, model: AbstractModel, context: CallingContext = None
    ) -> typing.List[dict]:
        """Prompt building in `funkyprompt` is governed by models or types. A question is injected into a scaffold based on the type
        For language models we can construct a set of one or more messages using different roles.
        One large blob in a question can work but its often sensible to split fragments by role

        Args:
            question (str): the users question
            model (AbstractModel): the model used to generate the plan
            context (CallingContext, optional): context is used to determine the model provider and other session context. Defaults to None.
        """
        return []
    
    @classmethod
    def from_q_and_a(cls, question:str, data: typing.Any, observer_model:AbstractModel=AbstractEntity):
        """
        often we will have a question that will trigger a search
        the search result can then be 'observed' by an observer model that responds to the user
        the result of this is typically to provide a formatted response to the user
        
        the data should be serializable to json
        
        """
        messages= [
            SystemMessage(content=f'The data below were retrieved from a resource and can be used to answer the users question\n````json{json.dumps(data,default=str)}``'),
            UserMessage(content=question)
        ]
        return MessageStack(question=question,messages=messages, model=observer_model)
    
    @classmethod
    def format_function_response_data(
        cls, name: str, data: typing.Any, context: CallingContext = None
    ) -> Message:
        """format the function response for the agent - essentially just a json dump

        Args:
            name (str): the name of the function
            data (typing.Any): the function response
            context (CallingContext, optional): context such as what model we are using to format the message with

        Returns: formatted messages for agent as a dict
        """
        
        """Pydantic things """
        if hasattr(data,'model_dump'):
            data = data.model_dump()

        return Message(
            role="function",
            name=f"{str(name)}",
            content=json.dumps(
                {
                    # do we need to be this paranoid most of the time?? this is a good label to point later stages to the results
                    "about-these-data": f"You called the tool or function `{name}` and here are some data that may or may not contain the answer to your question - please review it carefully",
                    "data": data,
                },
                default=str,
            ),
        )

    @classmethod
    def format_function_response_type_error(
        cls, name: str, ex: Exception, context: CallingContext = None
    ) -> Message:
        """type errors imply the function was incorrectly called and the agent should try again

        Args:
            name (str): the name of the function
            data (typing.Any): the function response
            context (CallingContext, optional): context such as what model we are using to format the message with

        Returns: formatted error messages for agent as a dict
        """
        return Message(
            role="function",
            name=f"{str(name.replace('.','_'))}",
            content=f"""You have called the function incorrectly - try again {ex}""",
        )

    def format_function_response_error(
        name: str, ex: Exception, context: CallingContext = None
    ) -> Message:
        """general errors imply something wrong with the function call

        Args:
            name (str): the name of the function
            data (typing.Any): the function response
            context (CallingContext, optional): context such as what model we are using to format the message with

        Returns: formatted error messages for agent as a dict
        """

        return Message(
            role="function",
            name=f"{str(name.replace('.','_'))}",
            content=f"""This function failed - you should try different arguments or a different function. - {ex}. 
If no data are found you must search for another function if you can to answer the users question. 
Otherwise check the error and consider your input parameters """,
        )

    """smart pruning of messages"""

    @model_serializer()
    def custom_serializer(self):
        """
        we can be smarter about this
        """

        return [m.model_dump() for m in self.messages]
