class CLanguage:
    # 类成员
    desc = "计算机语言"

    # 类构造方法，也属于实例方法
    def __init__(self):
        self.name = "C"
        self.add = "github.com"

    # 类方法
    @classmethod
    def info(cls):
        print("正在调用类方法", cls)

    @staticmethod
    def static_show_name(name):
        '''不需要传入cls'''
        print("正在调用类静态方法", name)

    # 实例方法
    def show_name(self):
        print(self.name)


print(CLanguage.desc)
CLanguage.info()

cls = CLanguage()

print(cls.add)

cls.show_name()
