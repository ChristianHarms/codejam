import sys, StringIO

def solution(n):
    l1 = list(str(n))
    l2 = sorted(l1)
    while (l1!=l2):
        #find the first not tidy number
        t=-1
        for i in range(len(l1)-1):
            if l1[i]>l1[i+1]:
                t=i
        #fill up all digits after this place
        for i in range(len(l1)):
            if i>t+1:
                l1[i]='9'
        n = int(''.join(l1))
        n-=10**(len(l1)-t-2)*(int(l1[t+1])+1)
        l1 = list(str(n))
        l2 = sorted(l1)
    return n

if __name__ == '__main__':
    if len(sys.argv)>1:
        input = file(sys.argv[1])
    else:
        input = StringIO.StringIO("""4
132
1000
7
111111111111111110""")
    cases = int(input.readline())
    for case in range(cases):
        n = int(input.readline())
        print("Case #%d: %s" % (case+1, solution(int(n))))
