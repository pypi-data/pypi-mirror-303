import json
import csv


def to_jsonl(read_path, out_path):
    file_write = open(out_path, "w")
    file_read = open(read_path, "r")
    reader = csv.reader(file_read, delimiter="\t")
    for row in reader:
        print(row)
        one_line = {"instruction": "",  # "Extract the name of the store from the input",  # 中文意思为：从输入中提取标签
                    "input": row[1],  # "withdraw the label from input",
                    "output": row[0]}
        json.dump(one_line, file_write, ensure_ascii=False)
        file_write.write("\n")

    file_write.close()
    file_read.close()


if __name__ == '__main__':
    to_jsonl("trains/train.tsv", "trains/train.jsonl")
    to_jsonl("trains/test.tsv", "trains/test.jsonl")
