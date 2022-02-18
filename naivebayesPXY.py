#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
@author: Yichen
@author: M.Joo
"""

import numpy as np

def naivebayesPXY(x, y):
# =============================================================================
#    function [posprob,negprob] = naivebayesPXY(x,y);
#
#    Computation of P(X|Y)
#    Input:
#    x : n input vectors of d dimensions (dxn)
#    y : n labels (-1 or +1) (1xn)
#
#    Output:
#    posprob: probability vector of p(x|y=1) (dx1)
#    negprob: probability vector of p(x|y=-1) (dx1)
# =============================================================================



    # Convertng input matrix x and y into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    # TODO: do not use np.matrix!
    X = np.matrix(x)
    Y = np.matrix(y)

    d,n = X.shape

    # Pre-constructing a matrix of all-ones (dx2)
    X0 = np.ones((d,2))
    Y0 = np.array([[-1, 1]])

    # add one all-ones positive and negative example
    Xnew = np.hstack((X, X0)) #stack arrays in sequence horizontally (column-wise)
    Ynew = np.hstack((Y, Y0))

    # matrix of all-zeros -
    X1 = np.zeros((d, 2))
    # add one all-zeros positive and negative example - M.Joo
    Xnew = np.hstack((Xnew, X1))
    Ynew = np.hstack((Ynew, Y0))

    # Re-configuring the size of matrix Xnew
    d,n = Xnew.shape

# =============================================================================
# fill in code here
    # YOUR CODE HERE
    ft1=np.zeros(d).reshape(-1,1)
    ft2=ft1
    pe=ne=0
    y1=Ynew.reshape(-1,1)
    for i in range(0,n):
        if y1[i]==1:
            ft1=ft1+Xnew[:,i].reshape(-1,1)
            pe=pe+1
        else:
            ft2=ft2+Xnew[:,i].reshape(-1,1)
            ne=ne+1
    posprob=ft1/pe
    negprob=ft2/ne


    return posprob,negprob

# =============================================================================










# =============================================================================
