"""
@File    :   utils.py
@Time    :   2024/09/26 10:40:58
@Author  :   TankNee
@Version :   1.0
@Desc    :   Utils
"""

import re
from PIL import Image
import base64
import io
from copy import deepcopy


def markdown_table_to_json(markdown_table: str):
    """Convert a Markdown table to a list of dictionaries.

    Args:
        markdown_table (str): A Markdown table.

    Returns:
        list: A list of dictionaries.
    """
    lines = markdown_table.split("\n")
    headers = [header.strip() for header in lines[0].split("|") if header.strip()]
    data_lines = [line for line in lines[2:] if line.strip()]
    json_list = []
    template = {header: "" for header in headers}
    for line in data_lines:
        if not line.startswith("|"): line = "|" + line
        if not line.endswith("|"): line += "|"
        values = []
        for char in line[:-1]:
            if char == '|':
                values.append('')
            else:
                values[-1] += char
        values = [value.strip() for value in values]

        item = deepcopy(template)
        if len(values) != len(headers):
            return []
        for i, value in enumerate(values):
            item[headers[i]] = value
        json_list.append(item)
    return json_list


def json_to_markdown_table(json_list: list):
    """Convert a list of dictionaries to a Markdown table.

    Args:
        json_list (list): A list of dictionaries.

    Returns:
        str: A Markdown table.
    """
    if not json_list:
        return ""
    # 获取表头（第一个字典的键）
    headers = list(json_list[0].keys())
    # 创建 Markdown 表格的表头行
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    # 添加数据行
    for item in json_list:
        values = [str(item[key]) for key in headers]
        markdown_table += "| " + " | ".join(values) + " |\n"
    return markdown_table


def pil_image_to_base64(image):
    """
    将 PIL 图像转换为 base64 编码。
    """

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def base64_to_pil_image(base64_str):
    """
    将 base64 编码转换为 PIL 图像。
    """

    img_data = base64.b64decode(base64_str)
    img = Image.open(io.BytesIO(img_data)).convert("RGB")
    return img

def flatten(array: list):
    """
    将多维数组展平为一维数组。
    """

    result = []
    for item in array:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result