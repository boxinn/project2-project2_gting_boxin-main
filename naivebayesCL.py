#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY

def naivebayesCL(x, y):
# =============================================================================
#function [w,b]=naivebayesCL(x,y);
#
#Implementation of a Naive Bayes classifier
#Input:
#x : n input vectors of d dimensions (dxn)
#y : n labels (-1 or +1)
#
#Output:
#w : weight vector
#b : bias (scalar)
# =============================================================================
    d1,n1=np.shape(x)
    po,ne=naivebayesPXY(x,y)
    pos,neg=naivebayesPY(x,y)
    w=np.log(po)-np.log(ne)
    b=np.log(pos)-np.log(neg)

    
    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    
    # Pre-configuring the size of matrix X
    d,n = X.shape
    
# =============================================================================
# fill in code here
    
    return w,b
# =============================================================================
