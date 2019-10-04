#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:02:53 2019

@author: ajfinn
"""

a = int(input("Loan Amount: "))
n = int(input("Number of Periodic Payments: "))
i = (int(input("Annual Interest Rate: ")))/n
d = (((1+i)^n)-1)/(i(1+i)^n)

p = a/d
print (p)

