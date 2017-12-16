# -*- coding: utf-8 -*-

"""
普通方法通过self参数隐式传递当前类对象的实例
class方法(带@classmethod修饰器)通过cls参数传递当前类的对象
静态方法(带@staticmethod修饰器)直接传递参数
"""


class MethodClass(object):

    # 普通方法
    def common_method(self, x):
        print("commonMethod was called successful, x = %s. self = %s" % (x, self))

    # class方法
    @classmethod
    def class_method(cls, x):
        print("classMethod was called successful, x = %s. cls = %s" % (x, cls))

    # 静态方法，是把函数嵌入到类中的一种方式，函数就属于类，同时表明函数不需要访问这个类。
    # 通过子类的继承覆盖，能更好的组织代码。
    @staticmethod
    def static_method(x):
        print("staticMethod was called successful, x = %s" % x)


class MethodClassChild(MethodClass):
    pass

classInstance = MethodClass()
childClass = MethodClassChild()

# 调用方式
print("=====classInstance call=====")
classInstance.common_method(1)  # 正确
classInstance.class_method(1)   # 正确
classInstance.static_method(1)  # 正确

print()
print("=====classObject call=====")
# MethodClass.common_method(1)      # 错误
MethodClass.class_method(1)       # 正确
MethodClass.static_method(1)      # 正确

print()
print("=====childClass call=====")
childClass.common_method(1)
childClass.class_method(1)
childClass.static_method(1)
