# coding=utf-8
# @Time    : 2024-10-12 09:05:22
# @Author  : zhaosheng@nuaa.edu.cn
# @Describe: LLM.py

from langchain_openai import ChatOpenAI
from dsqlenv.core import SQL
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from pydantic import BaseModel, Field
import logging
from rich.table import Table
from rich.console import Console
console = Console()


# Get the logger for 'httpx'
httpx_logger = logging.getLogger("httpx")
# Set the logging level to WARNING to ignore INFO and DEBUG logs
httpx_logger.setLevel(logging.CRITICAL)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# print(__name__)
logger.setLevel(logging.CRITICAL)

class LLM:
    def __init__(self, llm_server="ollama", max_retries=2, temperature=0, api_key=None, base_url=None, model_name=None, history=[], sql_setup=None):
        if sql_setup:
            self.sql = SQL(sql_setup)
        else:
            try:
                self.sql = SQL()
            except Exception as e:
                logger.error(f"Failed to initialize SQL: {str(e)}")
                console.print(f"[red][bold]Failed to initialize SQL: {str(e)}")
                console.print(f"[green]Please provide sql_setup when initializing dagent_llm.LLM()")
                console.print(f"[green]Example: sql_setup = {{'DB_HOST': 'localhost', 'DB_PORT': 5432, ...}}")
                console.print(f"[green]Please refer to the documentation of the dsqlenv package for more information.")
                console.print(f"[green]https://pypi.org/project/dsqlenv/[/green]")
                console.print("[yellow]Or you can specify the <api_key>, <base_url>, <model_name>, <temperature>, <max_retries> directly.")
                console.print("[yellow][bold]Example: [/bold][green]LLM(api_key='your_api_key', base_url='your_base_url', model_name='your_model_name', temperature=0.5, max_retries=2)")
                # raise ValueError(f"Failed to initialize SQL: {str(e)}")
        self.llm_server = llm_server
        self.base_url = self._get_or_raise(f"{self.llm_server}_base_url", base_url)
        self.api_key = self._get_or_raise(f"{self.llm_server}_api_key", api_key)
        self.model_name = self._get_or_raise(f"{self.llm_server}_model_name", model_name)
        self.temperature = self._get_or_raise(f"{self.llm_server}_temperature", temperature)
        self.max_retries = self._get_or_raise(f"{self.llm_server}_max_retries", max_retries)
        self.model = ChatOpenAI(
            model=self.model_name,
            temperature=float(self.temperature),
            max_retries=int(self.max_retries),
            api_key=self.api_key,
            base_url=self.base_url
        )
        self.history = []
        self.load_history(history)
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def load_history(self, history):
        for message in history:
            if isinstance(message, (HumanMessage, SystemMessage, AIMessage)):
                self.history.append(message)
            else:
                logger.error(f"Invalid message type: {type(message)}")
                logger.error(f"Message content: {message}")
                logger.error("Only langchain_core.messages.HumanMessage, \
                    SystemMessage, and AIMessage are allowed.")
                raise ValueError(f"Invalid message type: {type(message)}")

    def chat(self, message, role="human"):
        if role == "human":
            self.history.append(HumanMessage(content=message))
        elif role == "ai":
            self.history.append(AIMessage(content=message))
        elif role == "system":
            self.history.append(SystemMessage(content=message))
        else:
            raise ValueError(f"Invalid role: {role}")
        response = self.model.invoke(self.history)
        self._update_token_usage(response.usage_metadata)
        self.history.append(response)
        return response
    
    def choose(self, options, prompt, option_type=None, need_reason=False, multiple=False, add_to_history=True, max_try=3, examples=[], notes=[]):
        """
        This method allows users to provide options, a prompt, and other settings to choose an option.
        It supports few-shot learning through `examples` and allows `notes` to be added for customized behavior.
        
        Args:
        - options: List of options to choose from.
        - prompt: The question or task prompt.
        - option_type: String describing the type of options.
        - need_reason: Whether the model should provide reasons.
        - multiple: Whether multiple options can be selected.
        - add_to_history: Whether to log the conversation to history.
        - max_try: Maximum retries for invalid responses.
        - examples: Few-shot examples for better model context.
        - notes: A list of instructions or notes that the model should consider.
        
        Returns:
        - The selected option(s) and reasons (if applicable).
        """

        table = Table(title="Options")
        table.add_column("Index", justify="center", style="cyan")
        table.add_column("Option", justify="center", style="magenta")
        for i, option in enumerate(options):
            table.add_row(str(i), option)
        console.print(table)
        with console.status("[bold green] LLM is choosing..."):
            # if option_type is not provided， we will use the LLM to automatically generate it
            if not option_type:
                try:
                    logger.info("Option type not provided. Using LLM to generate it.")
                    # generate message
                    tmp_msg = "Now we want use LLM to choose the option from the following options: "
                    for i, option in enumerate(options):
                        tmp_msg += f"{i+1}. {option}, "
                    tmp_msg = tmp_msg[:-2] + "."
                    tmp_msg += "\n\nWhat is the option name?"
                    tmp_msg += "\nFor example, when the chooses is 'apple', 'banana', 'orange', the option type is 'fruit'."
                    tmp_msg += "\nPlease provide the option type.(just one or two word)"
                    option_type = self.model.invoke(tmp_msg).content
                except Exception as e:
                    logger.error(f"Failed to generate option type: {str(e)}")
                    option_type = "option"
            if need_reason:
                class Choice(BaseModel):
                    choice: str = Field(description=f"The chosen {option_type}, separate multiple choices by commas if allowed.")
                    reason: str = Field(description="The reason for the choice.")
            else:
                class Choice(BaseModel):
                    choice: str = Field(description=f"The chosen {option_type}, separate multiple choices by commas if allowed.")
            structured_llm = self.model.with_structured_output(Choice)
            # Build the prompt with options and notes
            new_prompt = f"{prompt}\n\nOptions: {options}"
            new_prompt += f"\n\nPlease choose the {option_type}."
            if multiple:
                new_prompt += " (Multiple selections are allowed)"
            if need_reason:
                new_prompt += " and provide a reason."
            # Incorporate examples into the prompt if provided
            if examples:
                example_text = "\n\nHere are some examples for reference:\n"
                for example in examples:
                    example_text += f"- {example}\n"
                new_prompt += example_text
            # Add any additional notes to the prompt
            if notes:
                note_text = "\n\nConsider the following points:\n"
                for note in notes:
                    note_text += f"- {note}\n"
                new_prompt += note_text
            new_prompt += "\n\nMake sure all choices are from the provided options."
            # Chat interaction loop with retry
            result = []
            for attempt in range(max_try):
                if add_to_history:
                    self.history.append(HumanMessage(content=new_prompt))
                response = structured_llm.invoke(new_prompt)
                if add_to_history:
                    self.history.append(response)
                choices = [c.strip() for c in response.choice.split(",") if c.strip() in options]
                if choices:
                    result = choices
                    break
                else:
                    logger.error(f"Invalid choices: {response.choice}. Attempt {attempt + 1}/{max_try}.")
            if not result:
                raise ValueError("Max retries reached. No valid options chosen.")

            return result if multiple else result[0]

    def choose_with_args(self, options, prompt, option_type, need_reason=False, multiple=False, add_to_history=True, examples=[], notes=[]):
        """
        Presents options and prompts the user to choose one or more options.
        Arguments:
        - options: A list of choices to display.
        - prompt: The prompt for the choice.
        - option_type: The type of option being selected (e.g., function).
        - need_reason: If True, asks for a reason along with the choice.
        - multiple: If True, allows selecting multiple options.
        - add_to_history: If True, adds prompt and response to conversation history.
        - examples: Few-shot examples of inputs to guide the user.
        - note: Additional note to guide the user.
        """
        
        if need_reason:
            class Choice(BaseModel):
                choice: str = Field(description="name: The chosen option" + ("(s), please separate multiple options with commas" if multiple else ""))
                reason: str = Field(description="The reason for the choice")
                args: str = Field(description="The arguments for the chosen option in the format <arg1_name>:<arg1_value>,<arg2_name>:<arg2_value>..." + ("(s), separate multiple arguments with commas" if multiple else ""))
        else:
            class Choice(BaseModel):
                choice: str = Field(description="name: The chosen option" + ("(s), please separate multiple options with commas" if multiple else ""))
                args: str = Field(description="The arguments for the chosen option in the format <arg1_name>:<arg1_value>,<arg2_name>:<arg2_value>..." + ("(s), separate multiple arguments with commas" if multiple else ""))

        # Initialize LLM with structured output handling
        structured_llm = self.model.with_structured_output(Choice)
        new_prompt = prompt + "\n\n" + f"Options: {options}"
        
        # Add prompt details
        new_prompt += f"\nPlease choose the {option_type}"
        if need_reason:
            new_prompt += " and provide a reason"
        if multiple:
            new_prompt += " (multiple options allowed)"
        
        # Adding notes or few-shot examples for user guidance
        if notes:
            note_text = "\n\nConsider the following points:\n"
            for note in notes:
                note_text += f"- {note}\n"
            new_prompt += note_text
        if examples:
            few_shot_text = "\nExamples:\n" + "\n".join(examples)
            new_prompt += few_shot_text
        
        new_prompt += "\n\nPlease note that the arguments should be in the format <arg1_name>:<arg1_value>,<arg2_name>:<arg2_value>..."
        
        if add_to_history:
            self.history.append(HumanMessage(content=new_prompt))
        
        response = structured_llm.invoke(new_prompt)
        
        if add_to_history:
            self.history.append(response)
        
        return response.choice, response.args

    def function_choose(self, functions_info, prompt, need_reason=False, multiple=False, add_to_history=True, max_try=3, examples=[], notes=[]):
        """
        Chooses a function from a list of available functions and collects its input arguments.
        Arguments:
        - functions_info: List of dictionaries with details about each function.
        - prompt: The prompt to display to the user for function selection.
        - need_reason: If True, asks the user to provide a reason for the choice.
        - multiple: If True, allows choosing multiple functions.
        - add_to_history: If True, adds the conversation to history.
        - max_try: Maximum attempts for input validation.
        - examples: Few-shot examples to guide the user.
        - notes: Additional note to help the user.
        """

        # Generate information about available functions
        choose_info = []
        for i, data in enumerate(functions_info, 1):
            _ = f"name: {data['name']}"
            if "description" in data:
                _ += f", description: {data['description']}"
            if "input" in data:
                _ += f", input: {', '.join(data['input'])}"
            if "input_type" in data:
                _ += f", input type: {data['input_type']}"
            if "example_input" in data:
                _ += f", example input: {data['example_input']}"
            if "output_type" in data:
                _ += f", output type: {data['output_type']}"
            if "example_output" in data:
                _ += f", example output: {data['example_output']}"
            choose_info.append(_)

        while max_try > 0:
            max_try -= 1
            console.print("[yellow]Available functions:")
            table = Table(title="Functions")
            table.add_column("Index", justify="center", style="cyan")
            table.add_column("Function", justify="center", style="magenta")
            for i, info in enumerate(choose_info):
                table.add_row(str(i), info)
            console.print(table)

            function_name, args = self.choose_with_args(
                choose_info,
                prompt,
                "function name and provide input for the function",
                need_reason=need_reason,
                multiple=multiple,
                add_to_history=add_to_history,
                examples=examples,
                notes=notes
            )

            # logger.info(f"Function name: {function_name}")
            # logger.info(f"Arguments: {args}")
            console.print(f"[green]Function name: {function_name}")
            console.print(f"[green]Arguments: {args}")
            if need_reason and add_to_history:
                reason = self.history[-1].reason
                console.print(f"[red]Reasons: {reason}")

            # Parse arguments
            args_list = args.split(",")
            parsed_args = {}
            for arg in args_list:
                if ":" in arg:
                    key, value = arg.split(":")
                    parsed_args[key.strip()] = value.strip()

            # Verify if all needed arguments are provided
            needed_args = []
            for data in functions_info:
                if data["name"] == function_name:
                    needed_args = data["input"]

            if set(needed_args) == set(parsed_args.keys()):
                return {"function_name": function_name, "args": parsed_args}
            else:
                logger.error(f"Missing or incorrect arguments for function '{function_name}'. Needed: {set(needed_args)}, Provided: {set(parsed_args.keys())}")

            if max_try == 0:
                raise ValueError("Maximum attempts reached. Function selection or argument matching failed.")

    def _update_token_usage(self, usage_metadata):
        self.input_tokens += usage_metadata.get("input_tokens", 0)
        self.output_tokens += usage_metadata.get("output_tokens", 0)
        self.total_tokens += usage_metadata.get("total_tokens", 0)

    def _get_or_raise(self, key, default=None):
        if default:
            logger.warning(f"Using default value: {default}")
            return default
        value = self.sql.get_data_by_id(key)
        if value is None:
            logger.warning(f"{key} is not set in the database")
            raise ValueError(f"{key} is not set in the database\
                and no default value provided")
        return value
