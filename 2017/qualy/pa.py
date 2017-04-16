import sys, StringIO

DEBUG = 0

def solution(s, n):
    c = 0
    l = len(s)-1
    if DEBUG: print "".join(s), n
    for i in range(l/2+1):
        #is it from left an '-'?
        if i+n<=l+1 and s[i]=='-':
            c+=1
            for j in range(n):
                s[i+j]= s[i+j]=='-' and '+' or '-'
            if DEBUG: print "".join(s)
        #is it from right an '-'?
        if i+n<=l+1 and s[l-i]=='-':
            c+=1
            for j in range(n):
                s[l-i-j]= s[l-i-j]=='-' and '+' or '-'
            if DEBUG: print "".join(s)
    return s.count('-')>0 and 'IMPOSSIBLE' or c

if __name__ == '__main__':
    if len(sys.argv)>1:
        input = file(sys.argv[1])
    else:
        input = StringIO.StringIO("""3
---+-++- 3
+++++ 4
-+-+- 4""")
    cases = int(input.readline())
    for case in range(cases):
        s, n = input.readline().split()
        print("Case #%d: %s" % (case+1, solution(list(s), int(n))))
