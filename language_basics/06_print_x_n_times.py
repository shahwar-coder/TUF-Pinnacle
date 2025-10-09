'''
Print X N numbers of times
'''

class Solution:
    def printX(self, X, N):
        if N==1:
            print(X)
        else:
            print((str(X)+' ') *N) 
