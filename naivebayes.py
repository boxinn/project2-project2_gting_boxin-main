#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayes(x, y, x1):
# =============================================================================
#function logratio = naivebayes(x,y,x1);
#

#Computation of log P(Y|X=x1) using Bayes Rule
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#x1: input vector of d dimensions (dx1)
#
#Output:
#logratio: log (P(Y = 1|X=x1)/P(Y=-1|X=x1))
# =============================================================================


    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    X1= np.matrix(x1)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
# =============================================================================
# fill in code here

    p_py,n_ny=naivebayesPY(x,y)
    p_pxy,n_nxy=naivebayesPXY(x,y)
    logratio=np.log(p_py/n_ny)+np.dot(X1.T,np.log(p_pxy))-np.dot(X1.T,np.log(n_nxy))
    return logratio




'''
    logg=np.zeros(d).reshape(-1,1)
    for i in range(0,d):
        sum=sum_p=sum_n=0

        for j in range(0,n):
            if X1[i]==X[i,j]:
                sum=sum+1
                if y[j]==1: sum_p=sum_p+1
                else : sum_n=sum_n+1
        logg[i]=np.log((sum_p/(sum+1)+1)/((sum_n/sum+1)+1))
    logratio=logg.reshape(1,-1)
    return logratio



    sum = sum_p = sum_n = 0
    for i in range(0, n):
        if X[:, i].reshape(-1,1) == X1:
            sum = sum + 1
            if y[i] == 1:
              sum_p = sum_p + 1
            else:
              sum_n = sum_n + 1

    p1 = sum_p / sum + 1
    p2 = sum_n / sum + 1

    logratio = np.log(p1 / p2)

    return logratio

    logg=np.zeros(d).reshape(-1,1)
    for i in range(0,d):
        sum=sum_p=sum_n=0

        for j in range(0,n):
            if X1[i]==X[i,j]:
                sum=sum+1
                if y[j]==1: sum_p=sum_p+1
                else : sum_n=sum_n+1
        logg[i]=np.log((sum_p/(sum+1)+1)/((sum_n/sum+1)+1))
    logratio=logg.reshape(1,-1)
    return logratio

'''







