import sys, StringIO, collections

DEBUG = 0

def solution(n, k):
    d = [n]
    if DEBUG: print ("\t%s , k:%d" % (d, k))
    while k:
        s = d.pop()
        if s>2:
          r1 = (s-(s+1)%2)/2
          r2 = s/2
          d.extend([r1, r2])
        if s==2:
          r1 = 0
          r2 = 1
          d.append(r2)
        if s==1:
          r1 = 0
          r2 = 0
        k-=1
        d.sort()
        if DEBUG: print ("\t%s , k:%d" % (d, k))
    return r2, r1

def solution2(n, k):
    d = collections.defaultdict(int)
    d[n]= 1
    if DEBUG: print ("\t%s , k:%d" % (d, k))
    while k:
        s = max(d.keys())
        i = 1
        if k>=d[s]:
            i = d[s]
        d[s]-=i
        if not d[s]:
            d.pop(s)

        if s>2:
            r1 = (s-(s+1)%2)/2
            r2 = s/2
            d[r1]+=i
            d[r2]+=i
        if s==2:
            r1 = 0
            r2 = 1
            d[r2]+=i
        if s==1:
            r1 = 0
            r2 = 0
        k-=i
        if DEBUG: print ("\t%s , k:%d" % (d, k))
    return r2, r1

if __name__ == '__main__':
    if len(sys.argv)>1:
        input = file(sys.argv[1])
    else:
        input = StringIO.StringIO("""5
4 2
10 5
6 2
1000000 1000000
1000 1""")
    cases = int(input.readline())
    for case in range(cases):
        n, k = input.readline().split()
        r1 , r2 = solution2(int(n), int(k))
        print("Case #%d: %d %d" % (case+1, r1, r2))
