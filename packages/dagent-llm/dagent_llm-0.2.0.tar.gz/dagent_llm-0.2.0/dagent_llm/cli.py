#!/usr/bin/env python3
# coding=utf-8
# @Time    : 2024-10-15
# @Author  : zhaosheng@nuaa.edu.cn
# @Describe: Command Line Interface for LLM package

import sys
import argparse
import logging
from dagent_llm import LLM

# Import necessary modules for console printing
from rich.console import Console
import dagent_llm.version
# Create a console object for rich printing
console = Console()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)

def main():
    parser = argparse.ArgumentParser(description="Command Line Interface for LLM operations.")
    
    # Define subcommands
    subparsers = parser.add_subparsers(dest='command', help="Sub-commands for various operations")
    
    # 'chat' subcommand
    chat_parser = subparsers.add_parser('chat', help='Send a message to the LLM and get a response.')
    chat_parser.add_argument('--message', required=True, help='The message to send to the LLM.')
    chat_parser.add_argument('--llm_server', default='deepseek', help="Specify the LLM server to use.")
    chat_parser.add_argument('--role', default='human', choices=['human', 'ai', 'system'], help="Specify the role of the message sender.")
    # api_key, base_url, model_name, temperature, max_retries
    chat_parser.add_argument('--api_key', help="Specify the API key for the LLM server.")
    chat_parser.add_argument('--base_url', help="Specify the base URL for the LLM server.")
    chat_parser.add_argument('--model_name', help="Specify the model name for the LLM server.")
    chat_parser.add_argument('--temperature', type=float, help="Specify the temperature for the LLM server.")
    chat_parser.add_argument('--max_retries', type=int, help="Specify the maximum number of retries for the LLM server.")

    
    # 'choose' subcommand
    choose_parser = subparsers.add_parser('choose', help='Present options to the LLM and get a choice.')
    choose_parser.add_argument('--options', nargs='+', required=True, help='List of options to choose from.')
    choose_parser.add_argument('--prompt', required=True, help='The prompt presented to the LLM for making a choice.')
    choose_parser.add_argument('--need-reason', action='store_true', help='Ask the LLM to provide reasons for the choice.')
    choose_parser.add_argument('--multiple', action='store_true', help='Allow the LLM to select multiple options.')
    choose_parser.add_argument('--notes', help='Provide notes for customized behavior, split by comma.')
    choose_parser.add_argument('--examples', help='Provide examples for few-shot learning, split by comma.')
    # api_key, base_url, model_name, temperature, max_retries
    choose_parser.add_argument('--api_key', help="Specify the API key for the LLM server.")
    choose_parser.add_argument('--base_url', help="Specify the base URL for the LLM server.")
    choose_parser.add_argument('--model_name', help="Specify the model name for the LLM server.")
    choose_parser.add_argument('--temperature', type=float, help="Specify the temperature for the LLM server.")
    choose_parser.add_argument('--max_retries', type=int, help="Specify the maximum number of retries for the LLM server.")

    # 'choose_with_args' subcommand
    choose_args_parser = subparsers.add_parser('choose_with_args', help='Choose an option and provide arguments.')
    choose_args_parser.add_argument('--options', nargs='+', required=True, help='List of options to choose from.')
    choose_args_parser.add_argument('--prompt', required=True, help='The prompt for choosing.')
    choose_args_parser.add_argument('--option-type', required=True, help='The type of options being chosen.')
    choose_args_parser.add_argument('--need-reason', action='store_true', help='Provide reasons for the choice.')
    choose_args_parser.add_argument('--multiple', action='store_true', help='Allow multiple selections.')
    choose_args_parser.add_argument('--notes', help='Provide notes for customized behavior, split by comma.')
    choose_args_parser.add_argument('--examples', help='Provide examples for few-shot learning, split by comma.')
    # api_key, base_url, model_name, temperature, max_retries
    choose_args_parser.add_argument('--api_key', help="Specify the API key for the LLM server.")
    choose_args_parser.add_argument('--base_url', help="Specify the base URL for the LLM server.")
    choose_args_parser.add_argument('--model_name', help="Specify the model name for the LLM server.")
    choose_args_parser.add_argument('--temperature', type=float, help="Specify the temperature for the LLM server.")
    choose_args_parser.add_argument('--max_retries', type=int, help="Specify the maximum number of retries for the LLM server.")


    help_parser = subparsers.add_parser('help', help='Show help information.')

    # Parse arguments
    args = parser.parse_args()

    if args.command == "help" or args.command == "-h" or args.command == "--help" or args.command == "h" or args.command == "--h" or args.command == "-help"\
        or args.command == "H" or args.command == "--H" or args.command == "-HELP":
        console.print("[green]D-Agent LLM Command Line Interface[/green]\n")
        console.print("[blue]Usage:[/blue] dagent_llm [command] [options]\n")
        console.print("[green]Available Commands:[/green]")
        console.print("[blue]  chat            [/blue] Send a message to the LLM and get a response.")
        console.print("[blue]  choose          [/blue] Present options to the LLM and get a choice.")
        console.print("[blue]  choose_with_args[/blue] Choose an option and provide arguments.\n")
        

        console.print("[green]Options for 'chat' command:[/green]")
        console.print("[blue]  --message        [/blue] The message to send to the LLM.")
        console.print("[blue]  --llm_server     [/blue] Specify the LLM server to use.")
        console.print("[blue]  --role           [/blue] Specify the role of the message sender (default: 'human').\n")

        console.print("[green]Options for 'choose' command:[/green]")
        console.print("[blue]  --options        [/blue] List of options to choose from.")
        console.print("[blue]  --prompt         [/blue] The prompt for choosing.")
        console.print("[blue]  --need-reason    [/blue] Ask the LLM to provide reasons for the choice.")
        console.print("[blue]  --multiple       [/blue] Allow the LLM to select multiple options.\n")
        # notes and examples
        console.print("[blue]  notes           [/blue] Provide notes for customized behavior, split by comma.")
        console.print("[blue]  examples        [/blue] Provide examples for few-shot learning, split by comma.\n")

        console.print("[green]Options for 'choose_with_args' command:[/green]")
        console.print("[blue]  --options        [/blue] List of options to choose from.")
        console.print("[blue]  --prompt         [/blue] The prompt for choosing.")
        console.print("[blue]  --option-type    [/blue] The type of options being chosen.")
        console.print("[blue]  --need-reason    [/blue] Provide reasons for the choice.")
        console.print("[blue]  --multiple       [/blue] Allow multiple selections.\n")
        # notes and examples
        console.print("[blue]  notes           [/blue] Provide notes for customized behavior, split by comma.")
        console.print("[blue]  examples        [/blue] Provide examples for few-shot learning, split by comma.\n")

        # console.rule()
        console.print("[green]If you are not Using DSQlenv, you can specify the following options:[/green]")
        console.print("[blue]  --api_key        [/blue] Specify the API key for the LLM server.")
        console.print("[blue]  --base_url       [/blue] Specify the base URL for the LLM server.")
        console.print("[blue]  --model_name     [/blue] Specify the model name for the LLM server.")
        console.print("[blue]  --temperature    [/blue] Specify the temperature for the LLM server.")
        console.print("[blue]  --max_retries    [/blue] Specify the maximum number of retries for the LLM server.\n")
        console.print(f"[green]For more information, please refer to the documentation of the dsqlenv package:[/green]")
        console.print(f"[blue]https://pypi.org/project/dsqlenv/[/blue]\n")

        console.print("[green]Version:[/green] " + dagent_llm.version.__version__ + " | 2024-10-18")
        console.print("[green]Copyright:[/green] © 2024 VoiceCodeAI, Singapore")

        sys.exit(0)
    else:
        # Initialize the LLM object
        llm = LLM(  api_key=args.api_key if args.api_key else None,
                    base_url=args.base_url if args.base_url else None,
                    model_name=args.model_name if args.model_name else None,
                    temperature=args.temperature if args.temperature else None,
                    max_retries=args.max_retries if args.max_retries else None)

    if args.command == 'chat':
        # Chat command
        response = llm.chat(args.message, role=args.role)
        # print(f"LLM response: {response.content}")
        console.print(f"[green]LLM response:[/green] {response.content}")

    elif args.command == 'choose':
        # Choose command
        notes=args.notes if args.notes else []
        examples=args.examples if args.examples else []
        if notes:
            notes = [note.strip() for note in notes.split(",")]
        if examples:
            examples = [example.strip() for example in examples.split(",")]
        result = llm.choose(
            options=args.options,
            prompt=args.prompt,
            need_reason=args.need_reason,
            multiple=args.multiple,
            notes=notes,
            examples=examples
        )
        # print(f"LLM choice: {result}")
        console.print(f"[green]LLM choice:[/green] {result}")
        if args.need_reason:
            # print(f"LLM reasons: {result.reasons}")
            reason = llm.history[-1].reason
            console.print(f"[red]LLM reasons:[/red] {reason}")

    elif args.command == 'choose_with_args':
        # Choose with arguments command
        notes=args.notes if args.notes else []
        examples=args.examples if args.examples else []
        if notes:
            notes = [note.strip() for note in notes.split(",")]
        if examples:
            examples = [example.strip() for example in examples.split(",")]
        choice, args = llm.choose_with_args(
            options=args.options,
            prompt=args.prompt,
            option_type=args.option_type,
            need_reason=args.need_reason,
            multiple=args.multiple,
            notes=notes,
            examples=examples
        )
        # print(f"LLM choice: {choice}")
        # print(f"LLM arguments: {args}")
        console.print(f"[green]LLM choice:[/green] {choice}")
        console.print(f"[red]LLM arguments:[/red] {args}")
        if args.need_reason:
            # print(f"LLM reasons: {choice.reasons}")
            reason = llm.history[-1].reason
            console.print(f"[blue]LLM reasons:[/blue] {reason}")

    else:
        print("Invalid command. Use --help for more details.")

if __name__ == '__main__':
    main()
