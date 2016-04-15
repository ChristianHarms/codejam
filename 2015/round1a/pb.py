import sys, StringIO


#Works for cycles with m=[0,0,0,0...]
#problem with large m = [1,2,3,4,5,6....] - where is the cycle?
def solution(b, n, m):
  t = [0] * len(m)
  n=n-1
  start = n

  while n:
    #print "n:%d - t: %s, m: %s" % (n, t, m)
    #find next free barber and and working time
    nextM = t.index(0)
    t[nextM] = m[nextM]

    #wait for next free barber
    wait = min(t)
    t = [x-wait for x in t]

    n-=1

    #Check if we have an cycle
    if max(t) == 0:
      #print "cycle %d, n:%d -> %s" % ((start-n), n, n % (start-n))
      n = n % (start-n)
  return t.index(0)+1

if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""3
2 4
10 5
3 12
7 7 7
3 8
4 2 1""")
  cases = int(input.readline())
  for case in range(cases):
    b, n = [int(x) for x in input.readline().split()]
    m = [int(x) for x in input.readline().split()]
    print("Case #%d: %d" % (case+1, solution(b, n, m)))
