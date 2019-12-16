'''
author: kyang
task: 简单工厂模式实现四则运算计算器
'''

class Operation(object):
    def __init__(self):
        self.numA = None
        self.numB = None

    @set
    def numA(self):
        

    def cal(self):
        NotImplemented()


class AddOpertion(Operation):
    def cal(self):
        return self.numA + self.numB

class Opertion(Operation):
    def cal(self):
        return self.numA + self.numB

class AddOpertion(Operation):
    def cal(self):
        return self.numA + self.numB

class AddOpertion(Operation):
    def cal(self):
        return self.numA + self.numB