from reft import re

def uncomIndent(s: str, blank_tab_num: int = 4) -> str:
    # 将输入字符串按行分割
    lines = s.splitlines()

    # 忽略空行
    non_blank_lines = [line for line in lines if re.strip(line)]

    if not non_blank_lines:
        return ""

    # 找到所有非空行的最小缩进
    indents:list[tuple[int, int, list]] = []
    for line in non_blank_lines:
        i, _len, _cnt, _spans = 0, len(line), 0, []
        while i < _len:
            if line[i] == '\t':
                _cnt += 1
                _spans.append((i, i+1))
                i += 1
            elif line[i:i+blank_tab_num] == ' ' * blank_tab_num:
                _cnt += 1
                _spans.append((i, i+blank_tab_num))
                i += blank_tab_num
            elif line[i] == ' ':
                raise ValueError("Invalid indent: " f"Can not match {blank_tab_num} spaces and a tab at pos:{i}.")
            else:
                break
        indents.append((_cnt, i, _spans))


    # 移除每一行的缩进
    min_indent, result = min(indents, key=lambda x: x[0])[0], []
    for line, (cnt, start, spans) in zip(lines, indents):
        if cnt == min_indent:
            result.append(line)
        else:
            _tarspan = spans[min_indent]



# 测试函数
input_str = """
    en_code1 = ""
    if en:
        en_code1 = "else if (cnt <= cmp) cnt <= cnt + 1;"
"""

print(uncomIndent(input_str))