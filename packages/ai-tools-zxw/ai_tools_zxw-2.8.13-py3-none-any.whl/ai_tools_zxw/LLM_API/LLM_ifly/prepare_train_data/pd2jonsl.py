import json
import pandas as pd
from pathlib import Path


def pd2jsonl(pd_data: pd.DataFrame, out_path: Path) -> bool:
    """
    :param pd_data: 必须有三个columns，分别为instruction, input, output
    :param out_path: 输出路径
    :return:
    """
    with open(out_path, "w") as file_write:
        for index, row in pd_data.iterrows():
            one_line = {"instruction": row["instruction"],
                        "input": row["input"],
                        "output": row["output"]}
            file_write.write(json.dumps(one_line, ensure_ascii=False))
            file_write.write("\n")
    return True
