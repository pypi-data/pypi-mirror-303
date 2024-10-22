import os
import re
import json
from openai import OpenAI
from .utils import gen_func_description, repair_spec, repair_spec_impl

SYSTEM_PROMPT = "你是一位经验丰富的openEuler RPM软件包构建人员，你的任务是根据提供的spec脚本和报错日志修复spec脚本，以解决构建过程中出现的问题。"

PROMPT_TEMPLATE = """
spec脚本：
{spec}

报错日志：
{log}
"""


class SpecBot:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY", None)
        base_url = os.getenv("OPENAI_BASE_URL", None)
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = "gpt-4-0613"

    def repair(self, spec_file, log_file, repair_file):
        spec = self._preprocess_spec(spec_file)
        log = self._preprocess_log(log_file)
        tools = self._prepare_tools()
        messages = self._prepare_messages(spec, log)
        
        is_repaired = False
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice={"type": "function", "function": {"name": "repair_spec"}},
            )
            tool_calls = response.choices[0].message.tool_calls
            arguments = tool_calls[0].function.arguments
            arguments = json.loads(arguments)
            suggestion = arguments.get("suggestion", None)
            fault_segment = arguments.get("fault_segment", None)
            repaired_segment = arguments.get("repaired_segment", None)
            
            if suggestion and fault_segment and repaired_segment:
                is_repaired = repair_spec_impl(
                    spec_file, fault_segment, repaired_segment, repair_file
                )
        except Exception as e:
            suggestion = str(e)
        return suggestion, is_repaired

    def _prepare_messages(self, spec, log):
        # 准备消息
        messages = []
        if SYSTEM_PROMPT:
            messages.append({"role": "system", "content": SYSTEM_PROMPT})
        messages.append(
            {"role": "user", "content": PROMPT_TEMPLATE.format(spec=spec, log=log)}
        )
        return messages

    def _prepare_tools(self):
        # 准备工具
        return [gen_func_description(repair_spec)]

    def _preprocess_spec(self, spec_file):
        # 预处理spec
        with open(spec_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        start_index = 0
        for i in range(len(lines)):
            if "License" in lines[i]:
                start_index = i + 1
                break
            if "BuildRequires" in lines[i]:
                start_index = i
                break
        spec = "".join(lines[start_index:])
        return spec

    def _preprocess_log(self, log_file):
        # 预处理log
        with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        start_index = 0
        end_index = len(lines)

        for i in range(len(lines) - 1, -1, -1):
            if "RPM build errors:" in lines[i]:
                end_index = i

            pattern = re.compile(r"^Executing\(%\w+\):")
            if pattern.match(lines[i]):
                start_index = i
                break

        log = "".join(lines[start_index:end_index])

        return log
