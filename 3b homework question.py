#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:14:03 2020

@author: amyshah
"""
import sympy as sp



# Create a matrix each [...]  is a row in the matrix
# Matrix is a sympy function that returns a Matrix
# in this case we store that in A.

data1= sp.Matrix([4,6,8,10,12,14,16,18])
index = sp.Matrix([[0,1,2,3,4,5,6,7]])
ycol= sp.Matrix([1.54, 2.01, 2.4, 2.9, 3.2, 3.5, 3.7, 4.38])
data2= data1.applyfunc(lambda x: pow(x,2))

data3= data1.applyfunc(lambda x: pow(x,3))

x = data1.col_insert(2, data2)
x = x.col_insert(3,data3)

xt = x.transpose()
xtx= xt*x
xty = xt*ycol

#xtx_inverse = xtx.inv()

#answer = xtx_inverse*xty

augmented = xtx.col_insert(4,xty)




#sp.pprint(answer.echelon_form())
sp.pprint(augmented.rref())