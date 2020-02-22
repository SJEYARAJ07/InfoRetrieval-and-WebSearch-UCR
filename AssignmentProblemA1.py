# calculateBM25
import numpy as numpy

N, n1, n2, n3 = 1000, 100, 200, 150
f1, f2, f3 = 1,4, 1
k1, k2 = 1.2, 100
b = 0.75
#Assumptions
#no info on relevace
r, R = 0, 0
#document length is same as average document length
documenLen = 0.9
# query has two terms
qf = 1

def K(k1, b, documenLen):
    return k1*((1-b)+b*documenLen)

def calculateBM25(k1,k2,ri,ni,fi,R,qf,K):
    return numpy.log(((ri+0.5)/(R-ri+0.5))/((ni-ri+0.5)/(N-ni-R+ri+0.5)))* \
        (((k1+1)*fi)/(K+fi))*(((k2+1)*qf)/(k2+qf))

K = K(k1,b,documenLen)

university = calculateBM25(k1, k2, r, n2, f2, R, qf, K)
riverside = calculateBM25(k1, k2, r, n1, f1, R, qf, K)
diverse = calculateBM25(k1, k2, r, n3, f3, R, qf, K)

#Q1 university Riverside
print('BM25 score for Q1:',university+riverside)
#Q2diverse univeristy
print('BM25 score for Q2:',diverse+university)
