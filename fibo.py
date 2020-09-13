# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:38:44 2020

@author: user
"""


def fibo(a):
    if a<=0:
        return print("Wrong Input!!")
    fb  =[0,1]
    if a==1:
        return fb[0]
    if a==2:
        return fb
    for i in range(2,a):
        fb.append(fb[i-1]+fb[i-2])
    return fb
def fibono(a):
    if a<=0:
        return print("Wrong Input!!")
    fb =[0,1]
    if a> 2:
        for i in range(2,a):
            fb.append(fb[i-1]+fb[i-2])
    return fb[a-1]
