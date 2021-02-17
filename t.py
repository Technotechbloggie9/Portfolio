def solution(xs):
    # handy spare lists
    rx = []
    nx = []
    fx = []
    zx = []
    mx = 1
    #counting negatives
    cnegs = 0
    for n in range(len(xs)):
        if not isinstance(xs[n], int) and not isinstance(xs[n], float):
            zx.append(0)
        elif xs[n] < 0:
            cnegs = cnegs + 1
            nx.append(xs[n])
        elif xs[n] > 1:
            rx.append(xs[n])
        elif xs[n] > 0 and xs[n] < 1:
            fx.append(xs[n])
        else:
            zx.append(xs[n])
    if (cnegs % 2) > 0 and len(nx) > 1:
        #literally, not even
        nx.sort()
        nx.pop()
    else:
        pass
    if len(rx)>1 or len(nx)==1 and len(fx) == 0 or len(nx)>1:
        jx = rx + nx
        jx.sort()
        for m in range(len(jx)):
            mx = mx * jx[m]
    elif (len(rx)==0 and len(nx)==0 and len(zx) !=0) or (len(fx) != 0 and len(rx)==0 and len(nx)==0) or len(rx)<=1 and len(nx) <2:
        gx = -3
        jx = fx + zx + rx
        for m in range(len(jx)):
            if jx[m] > gx:
                gx = jx[m]
        mx = gx
    else:
        print("here")
        mx = 0
    smx = str(mx)
    return smx
def main():
    print(solution([.2, .9, -.2, -9]))
    print(solution([0,0,-5,.2,0]))
    print(solution([2,-3,1,0,-5]))
    print(solution([-.2,-.1,8,-5]))
    print(solution([0,0,0,0,0]))
    print(solution(['dog']))
    print(solution([1000**25, 1000**25]))
    print(solution([-1]))
if __name__=="__main__":
    main()
'''
cd = [2, 0, 2, 2, 0]
count_negatives = 0
bc =[]
nbc = []
for n in range(len(cd)):
    if cd[n] < 0:
        count_negatives = count_negatives + 1
        nbc.append(cd[n])
    elif cd[n] > 0:
        bc.append(cd[n])
    else:
        pass
if (count_negatives % 2) > 0:
    nbc.sort()
    nbc.pop()
jbc = bc + nbc
jbc.sort()
print(jbc)

mx = 1
for l in range(len(jbc)):
   mx = mx * jbc[l]
   
print(str(mx))
'''
'''
a_cap = ord('A')
z_cap = ord('Z')
zl = ord('z')
al = ord('a')
i = 0
string1 = ''
dictionary = {}
for n in range(ord('a'), (ord('z')+1)):
    #dictionary[chr(a_cap+i)] = chr(z_cap-i)
    dictionary[chr(al+i)] = chr(zl-i)
    i = i + 1
x = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
for m in range(len(x)):
    if x[m] in dictionary:
        string1 = string1 + dictionary[x[m]]
    else:
        string1 = string1 + x[m]

print(string1)
'''   

