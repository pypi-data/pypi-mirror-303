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
dagent = LLM("ollama")

# Function to generate mock data for testing
def generate_mock_data(num_samples=5):
    """
    生成用于测试的假数据。
    """
    message_list = []
    for i in range(num_samples):
        message = f"讲个笑话 ，随机数：{i}"
        message_list.append(message)
    role_list = ["human"] * num_samples
    return message_list, role_list

if __name__ == "__main__":
    # 生成假数据
    num_samples = 50 # 假设生成10个测试样本
    message_list, role_list = generate_mock_data(num_samples)
    # 定义并发进程数
    num_processes = 10

  
    # -----------------------------
    # 测试多进程 choose_multi_process 的执行时间
    # -----------------------------
    start_time_multi = time.time()
    print("start")

    result_list_multi = dagent.chat_multi_process(
        message_list=message_list,
        role_list=role_list,
        num_processes=num_processes
    )
    print(result_list_multi)
    end_time_multi = time.time()
    multi_process_duration = end_time_multi - start_time_multi


    # -----------------------------
    # 测试单进程 chat 的执行时间
    # -----------------------------
    start_time_single = time.time()
    for i in range(num_samples):
        # message = message_list[i]+f"\n随机数: {i}"
        result = dagent.chat(message_list[i], role_list[i], add_to_history=False)
        print(result)
    end_time_single = time.time()
    single_process_duration = end_time_single - start_time_single
    console.print(f"单进程 chat 方法执行时间：{single_process_duration:.2f} 秒")
    console.print(f"多进程 chat 方法执行时间：{multi_process_duration:.2f} 秒")
