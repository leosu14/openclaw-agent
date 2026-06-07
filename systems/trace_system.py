import json
import os

# ======================================
# trace 文件路径
# ======================================

TRACE_FILE = "data/trace.json"

# ======================================
# 创建 data 目录
# ======================================

os.makedirs(
    "data",
    exist_ok=True
)

# ======================================
# log trace
# ======================================

def log_trace(step, result):

    data = {
        "step": step,
        "result": str(result)
    }

    try:

        with open(
            TRACE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            logs = json.load(f)

    except:

        logs = []

    logs.append(data)

    with open(
        TRACE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            logs,
            f,
            indent=2,
            ensure_ascii=False
        )