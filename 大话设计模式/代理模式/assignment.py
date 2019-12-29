# -*- coding: utf-8 -*-
'''
author: kyang
task: 代理模式...神tm追妹类
'''


class ProgressBar():
    def __init__(self, base=0, target=100):
        self.curr = base
        self.target = target
        self.len = target - base

    def is_finish(self):
        return self.curr >= self.target

    def up(self, num=1):
        self.curr += num
        print('Completion rate: ', 1 - (self.target - self.curr) / self.len)

class Girl():
    def __init__(self, name):
        self.name = name
        self.get_gifts = dict()
        self.accept_gifts = dict()
        self.candidate = dict()
        self.boy_friend = None
        for boy_name in {'a', 'b', 'c', 'd'}:
            self.candidate[boy_name] = ProgressBar()

    def _is_candidate(self, boy_name):
        return boy_name in self.candidate

    def get_gift(self, pair):
        boy_name, gift = pair
        if boy_name not in self.get_gifts:
            self.get_gifts[boy_name] = []
        self.get_gifts[boy_name].append(gift)
        if self._is_candidate(boy_name):
            self._accept_gift(boy_name)
            del self.get_gifts[boy_name]
            return 'accepted'
        del self.get_gifts[boy_name]
        return 'refused'

    def _accept_gift(self, boy_name):
        gifts = self.get_gifts.get(boy_name, [])
        if boy_name not in self.accept_gifts:
            self.accept_gifts[boy_name] = []
        self.accept_gifts[boy_name].extend(gifts)
        self.candidate[boy_name].up()
        if self.candidate[boy_name].is_finish():
            self.boy_friend = boy_name
            self.candidate = dict()

class Bitch(Girl):
    def _is_candidate(self, boy_name):
        if boy_name not in self.candidate:
            self.candidate[boy_name] = ProgressBar(- 2<<32, 2<<32)
        return True

    def _accept_gift(self, boy_name):
        gifts = self.get_gifts.get(boy_name, [])
        if boy_name not in self.accept_gifts:
            self.accept_gifts[boy_name] = []
        self.accept_gifts[boy_name].extend(gifts)
        self.candidate[boy_name].up()
        if self.candidate[boy_name].is_finish():
            if self.boy_friend is None:
                self.boy_friend = []
            self.boy_friend.append(boy_name)

class Interface():
    def giveA(self):
        NotImplementedError

    def giveB(self):
        NotImplementedError

    def giveC(self):
        NotImplementedError

class Pursuit(Interface):
    def __init__(self, name, girl):
        self.name = name
        self.girl = girl
    
    def giveA(self):
        return 'A'

    def giveB(self):
        return 'B'

    def giveC(self):
        return 'C'

    def get_return(self, rtn):
        '''
        收了就嘿嘿嘿，舔狗无疑
        '''
        if rtn == 'accepted':
            print('嘿嘿嘿')
        else:
            print('TAT')

class Proxy(Interface):
    def __init__(self, boy):
        self.boy = boy

    def give_gift(self, gift):
        pair = (self.boy.name, gift)
        girl = self.boy.girl
        rtn = girl.get_gift(pair)
        self.boy.get_return(rtn)

    def giveA(self):
        self.give_gift(self.boy.giveA())

    def giveB(self):
        self.give_gift(self.boy.giveB())

    def giveC(self):
        self.give_gift(self.boy.giveC())

if __name__ == '__main__':
    girl = Girl('lalal')
    Aftermath = Pursuit('jinmeng', girl)
    kyang = Proxy(Aftermath)
    kyang.giveA()
    kyang.giveB()
    kyang.giveC()