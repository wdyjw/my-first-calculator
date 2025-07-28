def calculate():
    print("\n=====简易计算机=====")

    # 获取用户输入的两个值

    n1 = input("请输入第 1 个数字：")

    n2 = input("请输入第 2 个数字：")

    op = input("请输入运算符号（+、-、*、/）:")

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
    else:
        print("\n----请输入正确的运算符号。----")

    print("\n=====运算结果=====")
    print("结果是：" + str(result))

if __name__ == '__main__':
    calculate()


