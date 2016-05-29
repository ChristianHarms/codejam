# -*- coding: utf-8 -*-

import sys, StringIO



def sortList(a, b):
  i = 0
  for i in range(len(a)):
    if a[i]!=b[i]:
      return a[i]-b[i]
  return a[i]-b[i]

def solution(n, l):
  l.sort(sortList)
  #print l
  a = [0 for i in range(n*n)]
  missing = -1
  t = 0
  #print a
  while t<len(l):
    p = l[t - (missing!=-1)]
    canInsert = True
    if t%2==0:
      #check row
      print "insert row"
      i = t/2
      for j in range(n):
        print "\t", a[i*n+j], p[j]
        canInsert = canInsert and (a[i*n+j] == p[j] or a[i*n+j] == 0)
      if canInsert:
        for j in range(n):
          a[i*n+j] = p[j]
      else:
        missing = t
    else:
      #check col
      j=t/2
      print "insert col"
      for i in range(n):
        print "\t", a[i*n+j], p[i]
        canInsert = canInsert and (a[i*n+j] == p[i] or a[i*n+j] == 0)
      if canInsert:
        for i in range(n):
          a[i*n+j] = p[i]
      else:
        missing = t
    print i, canInsert, p, missing
    print a
    t+=1

  #nothnig found -> last row
  if missing==-1:
    missing = t

  r = [0 for i in range(n)]
  if missing%2==0:
    #missing row
    i = missing/2
    for j in range(n):
      r[j] = a[i*n+j]
  else:
    #missing col
    j=missing/2
    for i in range(n):
      r[i] = a[i*n+j]
  return " ".join([str(x) for x in r])
#solution


if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""1
4
5 9 14 16
1 4 5 6
6 12 16 20
4 7 9 12
8 12 15 20
4 7 10 12
5 10 14 15""")
  cases = int(input.readline())
  for case in range(cases):
    n = int(input.readline().strip())
    l = []
    for i in range(n*2-1):
      l.append([int(x) for x in input.readline().split()])
    print("Case #%d: %s" % (case+1, solution(n, l)))
