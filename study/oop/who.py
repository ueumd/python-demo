
class WhoSay:
    def say(self, who):
        who.say()

class CLanguage:
    def say(self):
        print("调用的是 Clanguage 类的say方法")

class CPython(CLanguage):
    def say(self):
        print("调用的是 CPython 类的say方法")

class CLinux(CLanguage):
    def say(self):
        print("调用的是 CLinux 类的say方法")

a = WhoSay()
#调用 CLanguage 类的 say() 方法
a.say(CLanguage())
#调用 CPython 类的 say() 方法
a.say(CPython())
#调用 CLinux 类的 say() 方法
a.say(CLinux())