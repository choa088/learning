income = int(input('请输入你的薪资:'))
salary =0
shouldpay = 0
def calculator(num):
    """计算税后薪资的函数，参数为原始收入"""
    shouldpay = num - 5000
    if shouldpay <= 0:
        tax = 0
    elif 0 < shouldpay <= 3000:
        tax = shouldpay * 0.03
    elif 3000 < shouldpay <= 12000:
        tax = shouldpay * 0.1 - 210
    elif 12000 < shouldpay <= 25000:
        tax = shouldpay * 0.2 -1410
    elif 25000 < shouldpay <= 35000:
        tax = shouldpay * 0.25 - 1410
    elif 35000 < shouldpay <= 55000:
        tax = shouldpay * 0.3 -4410
    elif 55000 < shouldpay <= 80000:
        tax = shouldpay *0.35 -7160
    else:
        tax = shouldpay *0.45 -15160

    salary = income - tax
    return '{:.2f}'.format(salary)

print('你的税后收入是：{}'.format(calculator(income)))
