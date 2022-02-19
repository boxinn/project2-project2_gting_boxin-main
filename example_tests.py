#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nigel
"""
import numpy as np
import random
import sys
from genTrainFeatures import genTrainFeatures
from naivebayesPY import naivebayesPY
from naivebayesPXY import naivebayesPXY
# for test import something dont belong to this file originally
from naivebayesCL import naivebayesCL
from classifyLinear import classifyLinear


def example_tests():
# =============================================================================
# function [r, ok, s]=example_tests()
#
# Tests the functions from homework assignment 0
# Please make sure that the error statements are instructive.
#
# Output:
# r= The number of tests that failed
# ok= The number of tests that passed
# s= statement describing the failed test (s={} if all succeed)
# =============================================================================

    # Put in any seed below
    random.seed(31415926535)
    # initial outputs
    r=0
    ok=0
    s=[] #used to be matlab cell array

    # load in name data
    xTr,yTr = genTrainFeatures()
    print('Starting Test 1')
    try:
        # Test 1: check if probabilities sum to 1
        pos,neg = naivebayesPY(xTr,yTr)
        failtest = (np.linalg.norm(pos+neg-1) > 1e-8)
        addon=''
    except:
        failtest = True
        addon = traceback.format_exc()

    if failtest:
        r = r+1
        s.append('Failed Test 1 naivebayesPY: Probabilities of P(Y) do not sum to 1.\n' + addon + '\n')
    else:
        ok=ok+1

    print('Completed Test 1')

    y=np.matrix([-1, 1])
    x=np.matrix([[0, 1], [1, 0]])

    failtest = False
    print('Starting Test 2')
    try:
        # Test 2: Test the Naive Bayes function on a simple matrix
        pos,neg = naivebayesPY(x,y)
        pos0 = 0.5
        neg0 = 0.5
        if (pos != pos0) or (neg != neg0):
            failtest = True
            addon = ''
    except:
        failtest = True
        addon = traceback.format_exc()

    if failtest:
        r = r + 1
        s.append('Failed Test 2 naivebayesPXY: The calculation of P(Y) seems incorrect.\n' + addon + '\n')
    else:
        ok=ok+1
    print('Completed Test 2')


    failtest = False
    print('Starting Test 3')
    pospossi0 = np.matrix([[0.66667], [0.33333]])
    negpossi0 = np.matrix([[0.33333], [0.66667]])
    try:
        # Test 3 calculate conditional probabilities
        pospossi,negpossi = naivebayesPXY(x,y)
        addon = ''
        if (np.linalg.norm(pospossi - pospossi0) > 1e-3) or (np.linalg.norm(negpossi - negpossi0) > 1e-3):
            failtest = True
    except:
        failtest = True
        addon = traceback.format_exc()

    if failtest:
        r = r+1
        s.append('Failed Test 3: The calculation of P(X|Y) seems incorrect.\n' + addon + '\n')
    else:
        ok=ok+1
    print('Finished Test 3')

#    Tests 4~8 are testing about the naivebayesPXY function.
#    Some are sanity tests that the function is returning reasonable answers.
#    Some are making sure they are correct on small cases

#    Tests 9 is on naivebayes

#    Tests 10 is on naivebayesCL


    percentage=ok/(r+ok)*100;
    return r,ok,s

if __name__ == '__main__':
    failed,ok,msgs = example_tests()
    print("Number of failed example tests: "+str(failed))
    print("Number of passed example tests: "+str(ok))
    if len(msgs):
        failMsg = 'Unfortunately, you failed %d test(s) on this evaluation: \n\n' % len(msgs)
        for j in range(0,len(msgs)):
            print(msgs[j])
    print("\nNote: we only implemented 3 out of 12 tests for you. Check the inline documentation for what the other tests do and implement them yourself!")

#for test error

x,y=genTrainFeatures()
w,b=naivebayesCL(x,y)
preds=classifyLinear(x,w,b)
preds=preds.reshape(-1,1)
y=y.reshape(-1,1)
d,n=np.shape(x)
aa=0

for i in range (0,n):
    if y[i]==preds[i]: aa=aa+1
trainingerror=np.sum(aa)/(n)
print(trainingerror)
