from pathlib import Path
import re

txt_path = Path("myFather.txt")
out_path = Path("myFather_out.txt")

with open(txt_path, "rb") as f:
    with open(out_path, "w") as out_f:
        while True:
            #
            line = f.readline().decode("gb2312", errors="ignore").encode("utf-8").decode("utf-8")
            if not line:
                break
            # 正则表达式模式
            pattern = r'(?:^|^\s+)第\d+章\s+.*$'
            match = re.match(pattern, line)
            if match:
                # 标题
                print(match.group())
                out_f.write(match.group())
            # elif line in ["\n", "\r\n"]:
            #     print("空行")
            #     out_f.write("<br>\r\n")
            else:
                line = line.replace("\n", "<br>")
                out_f.write(line)
