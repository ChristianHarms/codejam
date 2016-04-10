import cPickle, sys, StringIO
from bitarray import bitarray

def bin2x(num, base):
  s = 0
  for d in list(bin(num)[2:]):
    s = s*base + int(d)
  #print "%s ^ %d -> %s" % (bin(num), base, s)
  return s

def iterPrims(n):
    a = bitarray(n)
    a.setall(1)

    p = 2
    while True:
        #search for next not-null
        while p<n-1 and a[p]==0:
            p += 1
        #return it as prim
        yield p
        #end of sieve
        if p == n-1:
            raise StopIteration
        #fill all multiple  a[p]
        step = p
        i = step*2
        while i<n-1:
            #print "a[%d] = 0 " % i
            a[i] = 0
            i += step
        p += 1
#iterPrims


def solve(n, count):
  c = 2**(n-1)+1
  maxP = 1000
  try:
    prims = cPickle.load(open('prims-%d'%maxP))
  except:
    prims = list(iterPrims(maxP))
    cPickle.dump(prims, open('prims-%d'%maxP,'wb'))
  primSet = set(prims)
  print "Case #1:"
  while count:
    div = []
    base = [ bin2x(c, i) for i in range(2, 11) ]

    found = True
    i = 1
    while found and i<10:
      i+=1
      d = base[i-2]
      if d not in primSet:
        found = False
        j = 0
        while not found and j<len(prims) and prims[j] < d/2:
          if d % prims[j]==0:
            found = prims[j]
          j+=1
        div.append(found)
    if found and len(div)==9:
      count-=1
      #print base
      print "%s %s" % (bin(c)[2:], " ".join([str(x) for x in div]))
    c+=2


if __name__=="__main__":
  if len(sys.argv)>1:
    input = file(sys.argv[1])
  else:
    input = StringIO.StringIO("""1
32 50""")
  cases = int(input.readline())
  for case in range(cases):
    n, c = [int(x) for x in input.readline().split()]
    solve(n, c)
