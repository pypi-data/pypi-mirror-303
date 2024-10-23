import inspect
import sys

功能 = [
    '''
    页码导航
    1.关于基本的
    2.关于用法的
    3.关于数据类型的
    ''',
    '''
    ##########关于基本的
    print = 输出
    input = 输入
    help = 帮助
    type = 属性
    ''',
    '''
    ##########关于用法的
    values = "值"
    sep = "分隔符"
    end = "结束"
    file = "文件"
    flush = "刷新"
    ''',
    '''
    ##########关于数据类型的
    整数 = int
    小数 = float
    字符串 = str
    布尔 = bool
    列表 = list
    元组 = tuple
    字典 = dict
    集合 = set
    自定义类 = "class"
    没有类型 = "NoneType"
    '''
]

def 帮助(页码=None):
    if 页码 == None:
        print('''
        更新于2023年11月6日
        作者：hshmeng
        功能：将python原本的英文关键字替换成中文，英文字符还是要用的
        用法：我也不知道，慢慢研究吧（输入：帮助(页码)）第0面是目录
        邮箱：hshmeng@foxmail.com   代码有问题记得发邮箱哦~
        特别：有小彩蛋哦~    
        ''')
    if 页码 != None:
        try:
            try:
                int(页码)
            except Exception:
                print("在使用帮助模块的时候，请输入整数哦")
            print(功能[页码])
        except Exception:
            print("页码超出范围，请重新输入")




def 属性(数据):
    数据类型 = {
        int: "类型：整数",
        float: "类型：小数",
        str: "类型：字符串",
        bool: "类型：布尔",
        list: "类型：列表",
        tuple: "类型：元组",
        dict: "类型：字典",
        set: "类型：集合",
        "meng": "类型：猛"
    }
    当前数据类型 = type(数据)
    if 当前数据类型 in 数据类型:
        return 数据类型[当前数据类型]
    if inspect.isclass(数据):
        return "类型：自定义类"
    if 数据 is None:
        return "类型：没有类型"
    return "未知类型"

整数 = int
小数 = float
字符串 = str
布尔 = bool
列表 = list
元组 = tuple
字典 = dict
集合 = set
自定义类 = "class"
没有类型 = "NoneType"

values = "值"
sep = "分隔符"
end = "结束"
file = "文件"
flush = "刷新"

def 输出(值, 分隔符=None, 结束=None, 文件=None, 刷新=None):
    if 分隔符 is not None:
        # 如果分隔符不为空，则使用指定的分隔符
        separator = 分隔符
    else:
        # 如果分隔符为空，则使用空字符串作为分隔符
        separator = ''
    if 结束 is not None:
        # 如果结束符不为空，则使用指定的结束符
        ending = 结束
    else:
        # 如果结束符为空，则使用默认的结束符
        ending = '\n'
    if 文件 is not None:
        # 如果文件不为空，则将输出写入指定的文件
        output_file = 文件
    else:
        # 如果文件为空，则使用标准输出作为文件
        output_file = sys.stdout
    if 刷新 is not None:
        # 如果刷新不为空，则将输出刷新到文件
        do_flush = 刷新
    else:
        # 如果刷新为空，则不进行刷新
        do_flush = False
    # 使用列表推导式将值转换为字符串，并用分隔符连接
    output = separator.join(str(value) for value in 值) + ending
    # 将输出写入文件
    output_file.write(output)
    if do_flush:
        # 如果进行刷新，则刷新文件
        output_file.flush()
    pass


def 输入(prompt=None):
    if prompt is not None:
        print(prompt,end="")
    return input()
    pass

def 导入(模块名):
    try:
        模块 = __import__(模块名)
    except ImportError:
        print(f"无法导入模块 {模块名}")
        return None
    return 模块

def 导(模块名):
    return __import__(模块名)
