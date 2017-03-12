
import sys, StringIO

# 2,2,2 -> 1,2,2
# 2,2,1 -> 1,1,1
# 3,2,1 -> 2,2,1 -> 1,1,1
# 2,1,1 -> 1,1,1 -> 0,1,1
def evacuate(c, senators):
    result = []
    senators.sort(lambda a,b: b[1]-a[1])
    while senators[0][1]>0:
        round=""
        #print "\t%s" % senators
        if senators[0][1]>senators[1][1]:
            round+=senators[0][0]
            senators[0][1]-=1
        if senators[0][1]==senators[1][1]:
            if len(senators)>2 and senators[1][1]==senators[2][1]:
                round+=senators[0][0]
                senators[0][1]-=1
            else:
                if round:
                    result.append(round)
                round = senators[0][0]+senators[1][0]
                senators[0][1]-=1
                senators[1][1]-=1
        result.append(round)
        senators.sort(lambda a,b: b[1]-a[1])

    return " ".join(result)

if __name__ == "__main__":
    if len(sys.argv)>1:
        fp = file(sys.argv[1])
    else:
        fp = StringIO.StringIO("""4
2
2 2
3
3 2 2
3
1 1 2
3
2 3 1
""")
    for case in range(int(fp.readline())):
        count = int(fp.readline())
        n = [[chr(65+int(x)), int(n)] for x,n in enumerate(fp.readline().split())]
        print "Case #%d: %s" % (case+1, evacuate(count, n))