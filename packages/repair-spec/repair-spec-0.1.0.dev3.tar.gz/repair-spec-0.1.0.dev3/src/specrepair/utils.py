import inspect
from typing import Dict, Annotated, get_origin, get_args

TYPE_MAPPING = {
    "str": "string",
    "int": "integer",
    "float": "number",
    "bool": "boolean",
    "list": "array",
    "dict": "object",
    # 添加其他类型的映射，如果需要的话
}


def gen_func_description(func) -> Dict:
    # 生成函数描述
    func_name = func.__name__
    func_desc = func.__doc__.strip() if func.__doc__ else ""

    # 获取函数参数的注解信息和默认值
    sig = inspect.signature(func)
    annotations = func.__annotations__

    parameters = {}
    required_params = []

    for name, param in sig.parameters.items():
        hint = annotations.get(name, None)
        origin = get_origin(hint)
        args = get_args(hint)

        if origin is Annotated:
            # 处理 Annotated 类型
            param_type = args[0].__name__.lower()
            param_desc = args[1]
        else:
            # 处理非 Annotated 类型
            param_type = (
                hint.__name__.lower() if hasattr(hint, "__name__") else str(hint)
            )
            param_desc = ""

        # 使用类型映射进行转换
        param_type = TYPE_MAPPING.get(param_type, "string")

        parameters[name] = {"description": param_desc, "type": param_type}

        # 检查参数默认值
        if param.default is param.empty:
            required_params.append(name)

    # 将生成的参数信息结构化
    param_schema = {
        "type": "object",
        "properties": parameters,
        "required": required_params,
    }

    # 返回最终的结构化函数描述
    return {
        "type": "function",
        "function": {
            "name": func_name,
            "description": func_desc,
            "parameters": param_schema,
        },
    }


def repair_spec(
    suggestion: Annotated[str, "spec脚本修改建议"],
    fault_segment: Annotated[str, "spec脚本中导致错误的代码片段,用于定位错误位置"] = "",
    repaired_segment: Annotated[
        str, "修复后的spec脚本代码段,用于替换原有的错误片段"
    ] = "",
) -> str:
    """根据报错信息修复spec脚本"""

    return "spec 脚本修复"


def repair_spec_impl(
    original_spec_file: str,
    fault_segment: str,
    repaired_segment: str,
    repaired_spec_file: str,
) -> bool:
    with open(original_spec_file, "r", encoding="utf-8", errors="ignore") as f:
        spec_lines = f.readlines()
    fault_lines = fault_segment.split("\n")
    fault_lines = [line + "\n" for line in fault_lines]
    repaired_lines = repaired_segment.split("\n")
    repaired_lines = [line + "\n" for line in repaired_lines]

    indices = [index for index, line in enumerate(spec_lines) if line == fault_lines[0]]

    if len(indices) == 0:
        return False

    success_list = [True] * len(indices)
    fault_length = len(fault_lines)
    for i in range(len(indices)):
        index = indices[i]
        fault_segment_extract = spec_lines[index : index + fault_length]
        for j in range(fault_length):
            if fault_segment_extract[j] != fault_lines[j]:
                success_list[i] = False
                break

    if any(success_list):
        # 找到第一个匹配的索引
        index = indices[success_list.index(True)]
        del spec_lines[index : index + fault_length]
        spec_lines[index:index] = repaired_segment
    else:
        return False

    with open(repaired_spec_file, "w") as f:
        f.write("".join(spec_lines))
    return True
