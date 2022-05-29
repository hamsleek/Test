# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 比较两个数字的大小
def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


# 比较两个字符串的大小
def compare_str(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


# 创建一个学生对象
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_info(self):
        print(f'{self.name} is {self.age} years old and has score {self.score}')

    # 提取一个列表中的偶数，并返回一个新列表


def extract_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
