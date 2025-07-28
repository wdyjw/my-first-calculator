last_result = None # 全局变量存储上次结果

def get_user_num(prompt: str):
    while True:
        try:
            n = float(input(prompt))
            if n is None:
                return
            return float(n)
        except ValueError:
            print("\n----无效输入，请重新输入数字。----")

def calculate():
    global last_result
    print("\n=====简易计算机=====")

    # 获取用户输入的两个值

    n1 = get_user_num("请输入第 1 个数字（可直接使用上次计算结果）：")
    n1 = float(n1) if n1 else last_result

    if n1 is None:
        print("无历史记录，请完整输入两个数字")
        return
    
    n2 = get_user_num("请输入第 2 个数字：")

    op = input("请输入运算符号（+、-、*、/、**、%）:")

    result = None

    if op == '+':
        result = float(n1) + float(n2)
    elif op == '-':
        result = float(n1) - float(n2)
    elif op == '*':
        result = float(n1) * float(n2)
    elif op == '/':
        if n2 != 0:
            result = float(n1) / float(n2)
        else:
            print("\n----除数不能为 0。----")
            return
    elif op == '**':
        result = float(n1) ** float(n2)
    elif op == '%':
        result = float(n1) % float(n2)
    else:
        print("\n----请输入正确的运算符号。----")

    # 存储上一次结果，用于下一次运算
    last_result = result
    print("\n=====运算结果=====")
    print("结果是：" + str(result))

if __name__ == '__main__':
    while True:

        calculate()

        print("\n再来一次吗？(y/n)")

        n = input(":")

        if n != 'y':
            break


