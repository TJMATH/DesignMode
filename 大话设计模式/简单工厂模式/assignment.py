'''
author: kyang
task: 简单工厂模式实现四则运算计算器
'''

class Operation(object):
    def __init__(self):
        self._numA = None
        self._numB = None

    @property
    def numA(self):
        return self._numA

    @numA.setter
    def numA(self, num):
        assert isinstance(num, float) or isinstance(num, int), '必须输入数字'
        self._numA = num

    @property
    def numB(self):
        return self._numB

    @numB.setter
    def numB(self, num):
        assert isinstance(num, float) or isinstance(num, int), '必须输入数字'
        self._numB = num

    def cal(self):
        NotImplemented()


class AddOpertion(Operation):
    def cal(self):
        return self.numA + self.numB

class SubtrOpertion(Operation):
    def cal(self):
        return self.numA - self.numB

class MultiOpertion(Operation):
    def cal(self):
        return self.numA * self.numB

class DivOpertion(Operation):
    def cal(self):
        assert self.numB != 0, '除0错误'
        return self.numA / self.numB

class OperationFactory(object):
    def __init__(self):
        self.opertions = {
            '+': AddOpertion,
            '-': SubtrOpertion,
            '*': MultiOpertion,
            '/': DivOpertion
        }

    def get_operation(self, operation):
        return self.opertions[operation]()


def test(num1, num2):
    operFactory = OperationFactory()
    print('============================================')
    for op in ['+', '-', '*', '/']:
        oper = operFactory.get_operation(op)
        oper.numA = num1
        oper.numB = num2
        print('{} {} {} = {}'.format(num1, op, num2, oper.cal()))

if __name__ == '__main__':
    test(1, 2)
    test(3.2, 0)