#!/usr/bin/env python 
# -*- coding:utf-8 -*-

class Student(object):

    @property
    def birth(self):
        return  self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2019 -self._birth

s = Student()

print('请输入学生年纪：')
douming = input()
s.birth = int (douming)

print(s.age)