import sys, StringIO

def solution(n, m):

  diff = 0
  va = 0
  for i in range(1,len(m)):
    if i and m[i-1]>m[i]:
      va += m[i-1]-m[i]
      diff = max(diff, m[i-1]-m[i])

  vb = 0
  for i in range(1,len(m)):
    if m[i-1]<diff:
      vb += m[i-1]
    else:
      vb += diff

  return "%d %d" % (va, vb)

if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""4
4
10 5 15 5
2
100 100
8
81 81 81 81 81 81 81 0
6
23 90 40 0 100 9""")
  cases = int(input.readline())
  for case in range(cases):
    n = int(input.readline())
    m = [int(x) for x in input.readline().split()]
    print("Case #%d: %s" % (case+1, solution(n, m)))
