#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""

import numpy as np

def classifyLinear(x, w, b):
# =============================================================================
#function preds=classifyLinear(x,w,b);
#
#Make predictions with a linear classifier
#Input:
#x : n input vectors of d dimensions (dxn)
#w : weight vector
#b : bias
#
#Output:
#preds: predictions
# =============================================================================
    d1,n1=np.shape(x)
    preds=np.zeros(n1).reshape(-1,1)
    for i in range(0,n1):
        if np.dot(x[:,i],w.reshape(-1,1))+b>0:
            preds[i]=1
        else: preds[i]=-1



    # Convertng input matrix x and x1 into NumPy matrix
    # input x and y should be in the form: 'a b c d...; e f g h...; i j k l...'
    X = np.matrix(x)
    W = np.matrix(w)
    
# =============================================================================
# fill in code here
    
    return preds
# =============================================================================



