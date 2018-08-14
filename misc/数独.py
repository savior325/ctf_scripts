# -*- coding: utf-8 -*-
'''
Created on 2012-10-5
@author: Administrator
'''
from collections import defaultdict
import itertools
a = [
  [ 0, 7, 0, 0, 0, 0, 0, 0, 0], #0
  [ 5, 0, 3, 0, 0, 6, 0, 0, 0], #1
  [ 0, 6, 2, 0, 8, 0, 7, 0, 0], #2
  #
  [ 0, 0, 0, 3, 0, 2, 0, 5, 0], #3
  [ 0, 0, 4, 0, 1, 0, 3, 0, 0], #4
  [ 0, 2, 0, 9, 0, 5, 0, 0, 0], #5
  #
  [ 0, 0, 1, 0, 3, 0, 5, 9, 0], #6
  [ 0, 0, 0, 4, 0, 0, 6, 0, 3], #7
  [ 0, 0, 0, 0, 0, 0, 0, 2, 0], #8
#  0, 1, 2, 3,|4, 5, 6,|7, 8
  ]
#a = [
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #0
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #1
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #2
#  #
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #3
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #4
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #5
#  #
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #6
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #7
#  [0, 0, 0, 0, 0, 0, 0, 0, 0], #8
##  0, 1, 2, 3,|4, 5, 6,|7, 8
#  ]
exists_d = dict((((h_idx, y_idx), v) for h_idx, y in enumerate(a) for y_idx , v in enumerate(y) if v))
h_exist = defaultdict(dict)
v_exist = defaultdict(dict)
for k, v in exists_d.items():
 h_exist[k[ 0]][k[ 1]] = v
 v_exist[k[ 1]][k[ 0]] = v
aa = list(itertools.permutations(range(1, 10), 9))
h_d = {}
for hk, hv in h_exist.items():
 x = filter(lambda x:all((x[k] == v for k, v in hv.items())), aa)
 x = filter(lambda x:all((x[vk] != v for vk , vv in v_exist.items() for k, v in vv.items() if k != hk)), x)
# print x
 h_d[hk] = x
def test(x, y):
 return all([y[i] not in [x_[i] for x_ in x] for i in range(len(y)) ])
def test2(x):
 return len(set(x)) != 9
s = set(range(9))
sudokus = []
for l0 in h_d[0 ]:
 for l1 in h_d[ 1]:
  if not test((l0,), l1):
   continue
  for l2 in h_d[ 2]:
   if not test((l0, l1), l2):
    continue
   # 1,2,3行 进行验证
   if test2([l0[ 0], l0[ 1], l0[ 2]
      , l1[ 0], l1[ 1], l1[ 2]
      , l2[ 0], l2[ 1], l2[ 2]
      ]) : continue   
   if test2([l0[ 3], l0[ 4], l0[ 5]
      , l1[ 3], l1[ 4], l1[ 5]
      , l2[ 3], l2[ 4], l2[ 5]
      ]) : continue   
   if test2([l0[ 6], l0[ 7], l0[ 8]
      , l1[ 6], l1[ 7], l1[ 8]
      , l2[ 6], l2[ 7], l2[ 8]
      ]) : continue   
   for l3 in h_d[ 3]:
    if not test((l0, l1, l2), l3):
     continue
    for l4 in h_d[ 4]:
     if not test((l0, l1, l2, l3), l4):
      continue
     for l5 in h_d[ 5]:
      if not test((l0, l1, l2, l3, l4), l5):
       continue
      # 4，5，6行 进行验证
      if test2([l3[ 0], l3[ 1], l3[ 2]
         , l4[ 0], l4[ 1], l4[ 2]
         , l5[ 0], l5[ 1], l5[ 2]
         ]) : continue   
      if test2([l3[ 3], l3[ 4], l3[ 5]
         , l4[ 3], l4[ 4], l4[ 5]
         , l5[ 3], l5[ 4], l5[ 5]
         ]) : continue   
      if test2([l3[ 6], l3[ 7], l3[ 8]
         , l4[ 6], l4[ 7], l4[ 8]
         , l5[ 6], l5[ 7], l5[ 8]
         ]) : continue   
      for l6 in h_d[ 6]:
       if not test((l0, l1, l2, l3, l4, l5,), l6):
        continue
       for l7 in h_d[ 7]:
        if not test((l0, l1, l2, l3, l4, l5, l6), l7):
         continue
        for l8 in h_d[ 8]:
         if not test((l0, l1, l2, l3, l4, l5, l6, l7), l8):
          continue
         # 7，8，9行 进行验证
         if test2([l6[ 0], l6[ 1], l6[ 2]
            , l7[0 ], l7[1 ], l7[2 ]
            , l8[0 ], l8[1 ], l8[2 ]
            ]) : continue   
         if test2([l6[ 3], l6[ 4], l6[ 5]
            , l7[3 ], l7[4 ], l7[5 ]
            , l8[3 ], l8[4 ], l8[5 ]
            ]) : continue   
         if test2([l6[ 6], l6[ 7], l6[ 8]
            , l7[6 ], l7[7 ], l7[8 ]
            , l8[6 ], l8[7 ], l8[8 ]
            ]) : continue   
         print l0
         print l1
         print l2
         print l3
         print l4
         print l5
         print l6
         print l7
         print l8
         sudokus.append((l0, l1, l2, l3, l4, l5, l6, l7, l8))
