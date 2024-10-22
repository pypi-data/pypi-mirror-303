# SpecRepair

## Install

```shell
pip install specrepair
```

## How to use?

Step 1: Setup openai api key and base url

```shell
export OPENAI_API_KEY=your_openai_api_key
export OPENAI_BASE_URL=your_openai_base_url
```

Step 2: Create a bot instance

```python
from specrepair import SpecBot

spec = SpecBot()
```

Step 3: Repair spec with the "repair" method

```python
spec_file = "path/to/your/spec/file.spec" # 待修改spec脚本文件
log_file = "path/to/your/log/file.log"    # 报错日志文件
repair_file = "path/to/save/your/repaired/file.spec" # 修改后的spec脚本保存地址
suggestion, flag = bot.repair(spec_file, log_file, repair_file)
```

> flag: 如果为 True，表示修复成功，修复后的 spec 脚本存储在 repair_file 路径下；否则修复失败，不生成修复脚本
> suggestion: spec 脚本的修改建议，无论 flag 为 True 还是 False，都输出修改建议
