import re

at_regex = re.compile(r'@[^\x20]+\s?')                                                                     # 正则表达式：@+昵称+可有可无空格
empty_line_regex = re.compile(r'\n\s*\n')                                                                  # 正则表达式：空行
Strings_to_remove = [line.rstrip() for line in open('paras/strings_to_remove.txt','r', encoding='utf-8')]  # 无效字符串集
Lines_to_remove = [line.rstrip() for line in open('paras/lines_to_remove.txt','r', encoding='utf-8')]      # 无效行集

def extract_msgs(input_file, out_file, begin_line, end_line):
    try:
        with open(input_file,'r',encoding='utf-8') as infile:
            lines = infile.readlines()
        if begin_line<=0 or end_line<begin_line or end_line>len(lines):
            print("行范围错误")
            return
        date_regex = re.compile(r"^\d{4}-\d{2}-\d{2} .+$")
        msgs_count = 0
        with open(out_file, 'w', encoding='utf-8') as outfile:
            for i in range(begin_line-1, end_line):
                line = lines[i].strip()
                if date_regex.match(line):
                    msgs_count+=1
                    continue
                if not line: continue
                outfile.write(line + '\n')
        print(f"  共提取 {msgs_count} 条消息")
    except FileNotFoundError:
        print(f"无法打开文件: {input_file}")
    except Exception as e:
        print(f"发生错误: {e}")

def filter_chat_log(input_file, output_file, strings_to_remove, lines_to_remove):
    # 以下删除无效行
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    new_lines = [line for line in lines if not any(re.search(re.escape(string), line) for string in lines_to_remove)]
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    # 以下删除无效字符串与空行
    with open(output_file, 'r', encoding='utf-8') as file:
        content = file.read()
    for string in strings_to_remove:
        pattern = re.compile(re.escape(string))
        content = pattern.sub('', content)
        content = empty_line_regex.sub('\n', content)
    content = content.strip()
    content = at_regex.sub('', content)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

input_File = "input.txt"
extracted_File = "outputs/extracted.txt"
filtered_File = "outputs/filtered.txt"
try:
    begin_Line = int(input("请输入聊天记录开始行数: "))
    end_Line = int(input("请输入聊天记录结束行数: "))
    print("——————————开始提取——————————")
    extract_msgs(input_File, extracted_File, begin_Line, end_Line)
    filter_chat_log(extracted_File, filtered_File, Strings_to_remove, Lines_to_remove)
    print("——————————过滤成功——————————")
except ValueError:
    print("输入错误")
