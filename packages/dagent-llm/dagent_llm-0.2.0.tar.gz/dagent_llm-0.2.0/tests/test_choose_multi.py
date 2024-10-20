import os
import csv
import subprocess
import pandas as pd
from tqdm import tqdm
from datetime import datetime
import argparse
import time

from rich.console import Console
from rich.table import Table
console = Console()

# Importing relevant classes
from dspeech import STT
from dagent_llm import LLM
from dguard import DguardModel as dm

# Initialize LLM
dagent = LLM("deepseek")

# Function to generate mock data for testing
def generate_mock_data(num_samples=5):
    """
    生成用于测试的假数据。
    """
    options_list = [["option1", "option2", "option3"] for _ in range(num_samples)]
    prompt_list = [f"Prompt {i}" for i in range(num_samples)]
    option_type_list = ["single" for _ in range(num_samples)]  # 假设都为单选
    need_reason_list = [False for _ in range(num_samples)]
    multiple_list = [False for _ in range(num_samples)]
    add_to_history_list = [False for _ in range(num_samples)]
    max_try_list = [3 for _ in range(num_samples)]  # 假设最多尝试3次
    examples_list = [["example1", "example2"] for _ in range(num_samples)]
    notes_list = [f"Note {i}" for i in range(num_samples)]

    return options_list, prompt_list, option_type_list, need_reason_list, multiple_list, add_to_history_list, max_try_list, examples_list, notes_list

if __name__ == "__main__":
    # 生成假数据
    num_samples = 10  # 假设生成10个测试样本
    options_list, prompt_list, option_type_list, need_reason_list, multiple_list, add_to_history_list, max_try_list, examples_list, notes_list = generate_mock_data(num_samples)

    # 定义并发进程数
    num_processes = 10

    # 打印表格展示输入数据
    table = Table(title="Test Data for choose_multi_process")
    table.add_column("Options", justify="center", style="cyan")
    table.add_column("Prompt", justify="center", style="magenta")
    table.add_column("Option Type", justify="center", style="green")
    table.add_column("Need Reason", justify="center", style="yellow")
    table.add_column("Multiple", justify="center", style="blue")
    table.add_column("Add to History", justify="center", style="red")
    table.add_column("Max Try", justify="center", style="purple")
    table.add_column("Examples", justify="center", style="cyan")
    table.add_column("Notes", justify="center", style="magenta")

    for i in range(num_samples):
        table.add_row(
            str(options_list[i]),
            prompt_list[i],
            option_type_list[i],
            str(need_reason_list[i]),
            str(multiple_list[i]),
            str(add_to_history_list[i]),
            str(max_try_list[i]),
            str(examples_list[i]),
            notes_list[i]
        )

    console.print(table)

    # -----------------------------
    # 测试多进程 choose_multi_process 的执行时间
    # -----------------------------
    start_time_multi = time.time()

    result_list_multi = dagent.choose_multi_process(
        options_list=options_list,
        prompt_list=prompt_list,
        option_type_list=option_type_list,
        need_reason_list=need_reason_list,
        multiple_list=multiple_list,
        add_to_history_list=add_to_history_list,
        max_try_list=max_try_list,
        examples_list=examples_list,
        notes_list=notes_list,
        num_processes=num_processes
    )
    print(result_list_multi)
    end_time_multi = time.time()
    multi_process_duration = end_time_multi - start_time_multi


    # -----------------------------
    # 测试单进程 choose 的执行时间
    # -----------------------------
    start_time_single = time.time()

    result_list_single = []
    for i in range(num_samples):
        result = dagent.choose(
            options_list[i],
            prompt_list[i],
            option_type_list[i],
            need_reason_list[i],
            multiple_list[i],
            add_to_history_list[i],
            max_try_list[i],
            examples_list[i],
            notes_list[i]
        )
        result_list_single.append(result)

    end_time_single = time.time()
    single_process_duration = end_time_single - start_time_single

    # 打印结果
    table_result = Table(title="Results of choose_multi_process")
    table_result.add_column("Prompt", justify="center", style="cyan")
    table_result.add_column("Chosen Option (Multi)", justify="center", style="magenta")
    table_result.add_column("Chosen Option (Single)", justify="center", style="green")

    for i in range(num_samples):
        table_result.add_row(
            prompt_list[i],
            str(result_list_multi[i]),
            str(result_list_single[i])
        )

    console.print(table_result)

    # 打印时间对比
    console.print(f"\n[bold]Multi-process Execution Time:[/bold] {multi_process_duration:.2f} seconds")
    console.print(f"[bold]Single-process Execution Time:[/bold] {single_process_duration:.2f} seconds")
