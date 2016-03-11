import sys, StringIO

def solution(c, s):
  friends = 0
  sum = 0
  for i, x in enumerate(s):
    if sum<i:
      friends+=i-sum
      sum+=i-sum
    sum += int(x)

  return friends

if __name__ == '__main__':
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""4
4 11111
1 09
5 110011
0 1""")
  cases = int(input.readline())
  for case in range(cases):
    c, s = input.readline().split()
    print("Case #%d: %d" % (case+1, solution(c,s)))
