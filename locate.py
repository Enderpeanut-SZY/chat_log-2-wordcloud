
line_order = []
locations = []
target_string = input("请输入消息对象名称(备注): ")

with open("input.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if line.startswith("=") and len(line.strip())==64 and set(line.strip())=={"="}:
            line_order.append(line_number)
for i in range(len(line_order)-2):
    if line_order[i+1]-line_order[i]==2 and line_order[i+2]-line_order[i+1]==2:
        locations.append(line_order[i]+3)
locations.append(4)

with open("input.txt", "r", encoding="utf-8") as file:
    pos = 0
    found = False
    for current_line_number, line in enumerate(file, start=1):
        if current_line_number==locations[pos]:
            pos += 1
            if line.strip() == f"消息对象:{target_string}":
                print(f"\n消息对象: {target_string} 的消息行数范围为\n{locations[pos-1]+2}\n至\n{locations[pos]-4}")
                found = True
if not found: print(f"未找到消息对象: {target_string}")





