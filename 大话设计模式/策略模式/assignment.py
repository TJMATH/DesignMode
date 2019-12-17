'''
author: kyang
task: 策略模式+简单工厂 实现现金收费
'''
import pytest

class Cash(object):
    '''
    Cash 类
    定义算法接口
    '''
    def __init__(self):
        self.price = None

    def cal_collection(self, price):
        NotImplementedError()

class CashNormal(Cash):
    def cal_collection(self, price):
        return price

class CashReturn(Cash):
    '''
    满100反20
    '''
    def __init__(self, goal=100, rt=20):
        super().__init__()
        self.goal = goal
        self.rt = rt

    def cal_collection(self, price):
        rtn = (price // self.goal) * self.rt
        return price - rtn

class CashRebate(Cash):
    '''
    打8折
    '''
    def __init__(self, account=8):
        super().__init__()
        self.account = account

    def cal_collection(self, price):
        return price * self.account / 10

class Context(object):
    def __init__(self, case='normal'):
        self.case_dict = {
            'normal': CashNormal,
            'return': CashReturn,
            'rebate': CashRebate
        }
        self.cash_method = self.case_dict[case]()

    def getResult(self, price):
        return self.cash_method.cal_collection(price)

def test_price():
    for price in range(100, 1000, 50):
        target = [price, 80*(price // 100) + price%100, price*0.8]
        for idx, case in enumerate(['normal', 'return', 'rebate']):
            cash_context = Context(case)
            assert cash_context.getResult(price) == target[idx], ( cash_context.getResult(price), target[idx])

def test_single():
    cash_context = Context('normal')
    assert cash_context.getResult(100) == 100

# if __name__ == '__main__':
#     test_price()