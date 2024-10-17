import os
import json
import markdown

def markdown_to_html(md_content):
    return markdown.markdown(md_content)

def generate_problem_json(directory):
    # 构建problem.json的路径
    problem_json_path = os.path.join(directory, 'problem.json')

    # 读取content.md文件
    content_md_path = os.path.join(directory, 'content.md')
    with open(content_md_path, 'r', encoding='utf-8') as f:
        content_md = f.read()

    # 解析content.md文件
    sections = content_md.split('### ')
    description = markdown_to_html(sections[1].split('【题目描述】')[1].strip())
    input_description = markdown_to_html(sections[2].split('【输入】')[1].strip())
    output_description = markdown_to_html(sections[3].split('【输出】')[1].strip())
    hint = markdown_to_html(sections[4].split('【提示】')[1].strip())

    # 获取子目录的数字
    dir_number = os.path.basename(directory)

    # 构建display_id和title
    display_id = f"SSOI-{dir_number}"
    title = f"SSOI-{dir_number}"

    # 获取data目录下的所有.in和.out文件
    data_dir = os.path.join(directory, 'data')
    in_files = sorted([f for f in os.listdir(data_dir) if f.endswith('.in')])
    out_files = sorted([f for f in os.listdir(data_dir) if f.endswith('.out')])

    # 计算每组测试样例的分数
    num_test_cases = len(in_files)
    score_per_case = 100 // num_test_cases

    # 构建test_case_score
    test_case_score = []
    for i in range(num_test_cases):
        test_case_score.append({
            "score": score_per_case,
            "input_name": in_files[i],
            "output_name": out_files[i]
        })

    # 构建problem.json的内容
    problem_json = {
        "display_id": display_id,
        "title": title,
        "description": {
            "format": "html",
            "value": description
        },
        "tags": [
            "\u4e00\u672c\u901a"
        ],
        "input_description": {
            "format": "html",
            "value": input_description
        },
        "output_description": {
            "format": "html",
            "value": output_description
        },
        "test_case_score": test_case_score,
        "hint": {
            "format": "html",
            "value": hint
        },
        "time_limit": 1000,
        "memory_limit": 256,
        "samples": [
            {
                "input": "",
                "output": ""
            }
        ],
        "template": {},
        "spj": None,
        "rule_type": "OI",
        "source": "SDNU \u673a\u5668\u4eba\u5b9e\u9a8c\u5ba4\u5728\u7ebf\u8bc4\u6d4b\u7cfb\u7edf http://127.0.0.1",
        "answers": []
    }

    # 写入problem.json文件
    with open(problem_json_path, 'w', encoding='utf-8') as f:
        json.dump(problem_json, f, ensure_ascii=False, indent=4)

def main():
    collections_dir = 'C:\\User\\excnies\\Collections'
    for subdir in os.listdir(collections_dir):
        subdir_path = os.path.join(collections_dir, subdir)
        if os.path.isdir(subdir_path):
            generate_problem_json(subdir_path)

if __name__ == "__main__":
    main()