import math
import os
import random
import re
import sys
if __name__ == '__main__':
  n = int(input())
  r=[]
  while n>0:
  	r.append(n%2)
  	n=n//2
  i=len(r)  
  while i>0:
   print (r[i-1])
   i -= 1