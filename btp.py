import sys

# Define constants
THICKNESS = 13

# Define a record type
class Record:
    def __init__(self):
        self.pen = 0
        self.dil = 0
        self.rhi = 0
        self.w1 = 0
        self.v1 = 0
        self.s1 = 0
        self.n1 = 0
        self.a1 = 0
        self.g1 = 0
        self.wp1 = 0
        self.wh1 = 0
        self.ht1 = 0
        self.wt1 = 0
        self.i = 0
        self.apen = 0

# Define variables
wpx2 = 0
height = 0
width = 0
thn = 0
w = 0
v = 0
n = 0
s = 0
g = 0
a = 0
wp = 0
wh = 0
ph = 0
p = 0
rh = 0
mind = 0
maxpen = 0
minpen = 0
maxdil = 0
mindil = 0
maxh = 0
minh = 0
maxrhi = 0
minrhi = 0
rhi2 = 0
i2 = 0
ap = 0
ap1 = 0
ap2 = 0
maxap = 0
minap = 0
pval = [Record() for _ in range(11)]
size = 0
j = 0
rnum = 0
scpen = 0
user_ch = 0
ctr = 0
counter = 0
hcount = 0
wcount = 0
totalvals = 0
phcount = 0
lkey = ''

# Define procedures/functions
def ok_val(inp_var, lo, hi, xc, yc):
    vent = False
    iv1 = ''
    xcl = xc
    ycl = yc

    while not vent:
        iv1 = input(f'Enter value between {lo} and {hi}: ')
        try:
            inp_var = int(iv1)
            if lo <= inp_var <= hi:
                vent = True
        except ValueError:
            pass

def ok_val2(inp_var, lo, hi, xc, yc):
    global lkey
    vent = False
    iv1 = ''
    xcl = xc
    ycl = yc

    while not vent:
        iv1 = input(f'Enter value between {lo} and {hi}: ')
        if iv1 == chr(27):
            lkey = iv1
            return
        try:
            inp_var = float(iv1)
            if lo <= inp_var <= hi:
                vent = True
        except ValueError:
            pass

def init():
    global pval
    pval = [Record() for _ in range(10)]


def optimized():
    global pval,ap,ap1,maxap,minap,size,j,rnum,scpen,user_ch,ctr,counter,hcount,wcount,totalvals,phcount,lkey, size, totalvals, counter, hcount, wcount, phcount, maxh, minh, maxpen, minpen, maxdil, mindil, maxrhi, minrhi, maxap, minap, scpen, mind, rhi2

    # Your sorting functions and other parts of the function remain unchanged

    def sortarr1():
        global size, pval
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii].rhi > pval[jj].rhi:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr2():
        global size, pval
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii].rhi == pval[jj].rhi and pval[ii].pen < pval[jj].pen:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr3():
        global size, pval
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if (pval[ii].rhi == pval[jj].rhi and pval[ii].pen == pval[jj].pen
                        and pval[ii].wp1 > pval[jj].wp1):
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr4():
        global size, pval
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if (pval[ii].rhi == pval[jj].rhi and pval[ii].pen == pval[jj].pen
                        and pval[ii].wp1 == pval[jj].wp1 and pval[ii].wh1 < pval[jj].wh1):
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr5():
        global size, pval
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if (pval[ii].rhi == pval[jj].rhi and pval[ii].pen == pval[jj].pen
                        and pval[ii].wp1 == pval[jj].wp1 and pval[ii].wh1 == pval[jj].wh1
                        and (pval[ii].pen / pval[ii].ht1) < (pval[jj].pen / pval[jj].ht1)):
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr6():
        global size, pval
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if (pval[ii].rhi == pval[jj].rhi and pval[ii].pen == pval[jj].pen
                        and pval[ii].wp1 == pval[jj].wp1 and pval[ii].wh1 == pval[jj].wh1
                        and (pval[ii].pen / pval[ii].ht1) == (pval[jj].pen / pval[jj].ht1)
                        and pval[ii].dil > pval[jj].dil):
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def insertrec():
        global size, pval, scpen
        if size < 10:
            size += 1
            pval[size].pen = p
            pval[size].w1 = w
            pval[size].v1 = v
            pval[size].n1 = n
            pval[size].s1 = s
            pval[size].g1 = g
            pval[size].a1 = a
            pval[size].wp1 = wp
            pval[size].wh1 = wh
            pval[size].ht1 = height
            pval[size].wt1 = width
            pval[size].dil = mind
            pval[size].apen = ap
            pval[size].rhi = rhi2
        else:
            size = 10
            if pval[size].rhi > rhi2:
                pval[size].pen = p
                pval[size].w1 = w
                pval[size].v1 = v
                pval[size].n1 = n
                pval[size].s1 = s
                pval[size].g1 = g
                pval[size].a1 = a
                pval[size].wp1 = wp
                pval[size].wh1 = wh
                pval[size].ht1 = height
                pval[size].wt1 = width
                pval[size].dil = mind
                pval[size].apen = ap
                pval[size].rhi = rhi2
        if size > 1:
            sortarr1()

    totalvals = 0
    counter = 0
    hcount = 0
    wcount = 0
    phcount = 0
    maxh = 0
    minh = 10
    maxpen = 0
    minpen = 5
    maxdil = 51.81
    mindil = 60
    maxrhi = 0
    minrhi = 300
    maxap = 0
    minap = 50
    scpen = 0
    init()
    size = 0
    thn = (33 / 100) * THICKNESS
    w = -1.5
    while w < 1:
        w += 0.5
        v = -1.5
        while v < 1:
            v += 0.5
            n = -1.5
            while n < 1:
                n += 0.5
                s = -1.5
                while s < 1:
                    s += 0.5
                    a = -1.5
                    while a < 1:
                        a += 0.5
                        g = -1.5
                        while g < 1:
                            g += 0.5
                            totalvals += 1
                            height = 3.75 - 0.32 * v + 0.45 * w + 0.09 * n - 0.44 * s + 0.12 * a - 0.09 * g + 0.11 * w * a + 0.09 * w * n

                            if height <= thn:
                                hcount += 1
                                p = 4.02 - 0.05 * v + 1.25 * w + 0.2 * n - 0.53 * s - 0.2 * g + 0.35 * w * n - 0.23 * w * s
                                ph = p / height

                                if ph >= 1.3:
                                    phcount += 1
                                    width = 13.27 + 0.24 * v + 1.43 * w - 0.37 * n - 1.22 * s - 0.35 * w * v + 0.22 * w * n + 0.22 * s * a + 0.24 * n * s
                                    wh = width / height

                                    if 4 <= wh <= 5:
                                        wcount += 1
                                        wp = width / p

                                        if 2.5 <= wp <= 3.5:
                                            if p >= 5.58:
                                                mind = 43.47 + 6.94 * w + 1.40 * w * v
                                                i2 = 257.18 + 17.81 * w + 5.31 * v - 4.0 * n - 4.0 * a + 2.8 * s + 2.18 * w * v - 2.18 * w * a - 2.81 * n * a + 2.81 * a * s
                                                rhi2 = ((v * 2.5) + 26.5) * i2 * 6.0 / ((s * 7.5) + 32.5)
                                                ap = 31.18 + 14.1 * w - 7.12 * s - 3.5 * w * s + 3.1 * w * n

                                                if scpen == 0:
                                                    minpen = p
                                                    minrhi = rhi2
                                                    minap = ap
                                                    mindil = mind
                                                    minh = height
                                                    maxpen = p
                                                    maxrhi = rhi2
                                                    maxap = ap
                                                    maxdil = mind
                                                    maxh = height

                                                scpen += 1
                                                insertrec()

                                            if p > maxpen:
                                                maxpen = p
                                            if p < minpen:
                                                minpen = p
                                            if mind < mindil:
                                                mindil = mind
                                            if mind > maxdil:
                                                maxdil = mind
                                            if height > maxh:
                                                maxh = height
                                            if height < minh:
                                                minh = height
                                            if rhi2 > maxrhi:
                                                maxrhi = rhi2
                                            if rhi2 < minrhi:
                                                minrhi = rhi2
                                            if ap > maxap:
                                                maxap = ap
                                            if ap < minap:
                                                minap = ap
                                            counter += 1

    sortarr1()
    sortarr2()
    sortarr3()
    sortarr4()
    sortarr5()
    sortarr6()

    print('total values         = ', totalvals)
    print('h pass               = ', hcount, '       w/h pass             = ', wcount)
    print('p/h pass             = ', phcount, '       w/p pass             = ', counter)
    print()
    print('maximum penetration  = ', maxpen, '       minimum penetration  = ', minpen)
    print('maximum dilution     = ', maxdil, '       minimum dilution     = ', mindil)
    print('maximum height       = ', maxh, '       minimum height       = ', minh)
    print('maximum RHI          = ', maxrhi, '       minimum RHI          = ', minrhi)
    print('max. area of pen.    = ', maxap, '       min. area of pen.    = ', minap)
    print('Number of procedures to choose an optimum from = ', scpen)
    print()

    for j in range(1, scpen + 1):
        vnat = pval[j].v1 * 2.5 + 26.5
        wnat = pval[j].w1 * 0.75 + 6.85
        snat = pval[j].s1 * 7.5 + 32.5
        nnat = pval[j].n1 * 2.5 + 17.5
        anat = pval[j].a1 * 10 + 90
        gnat = pval[j].g1 * 7.5 + 25.5

        print(' OPTIMUM PROCEDURE ')
        print('BG&SR responses                       Direct process parameters')
        print('penetration          = ', pval[j].pen, ' mm ', '    wire feed rate  = ', wnat, ' m/min')
        print('height               = ', pval[j].ht1, ' mm ', '    arc voltage     = ', vnat, ' volts')
        print('width                = ', pval[j].wt1, ' mm ', '    contact tube to = ', nnat, ' mm')
        print('w/h                  = ', pval[j].wh1, '        plate distance')
        print('w/p                  = ', pval[j].wp1, '        angle           = ', anat, ' degrees')
        print('area of penetration  = ', pval[j].apen, ' mm² ', '   welding speed   = ', snat, ' cm/min ')
        print('dilution             = ', pval[j].dil, ' %  ', '    gas flow rate   = ', gnat, ' l/min')
        print('RHI                  = ', pval[j].rhi, ' j/mm.  ')
        print('Press ENTER to continue or ESC to return')
        xx = input()
        if xx == chr(27):
            return



def check_range(value, min_val, max_val):
    return min_val <= value <= max_val

def usr_opt():
    usr_w, usr_v, usr_n, usr_th, usr_s, usr_g = None, None, None, None, None, None

    print("Press ESC to Exit")

    while True:
        usr_w = float(input("Enter Wire Feed Rate (W) (6.1 to 7.6 m/min): "))
        if check_range(usr_w, 6.1, 7.6):
            break
        else:
            print("Value out of range. Please enter a value between 6.1 and 7.6.")

    if input() == chr(27):
        sys.exit()

    while True:
        usr_v = float(input("Enter Arc Voltage (V) (24.0 to 29.0 Volts): "))
        if check_range(usr_v, 24.0, 29.0):
            break
        else:
            print("Value out of range. Please enter a value between 24.0 and 29.0.")

    if input() == chr(27):
        sys.exit()

    while True:
        usr_n = float(input("Enter Nozzle to Plate Distance (N) (15.0 to 20.0 mm): "))
        if check_range(usr_n, 15.0, 20.0):
            break
        else:
            print("Value out of range. Please enter a value between 15.0 and 20.0.")

    if input() == chr(27):
        sys.exit()

    while True:
        usr_th = float(input("Enter Electrode Inclination (A) (80.0 to 100.0 degrees): "))
        if check_range(usr_th, 80.0, 100.0):
            break
        else:
            print("Value out of range. Please enter a value between 80.0 and 100.0.")

    if input() == chr(27):
        sys.exit()

    while True:
        usr_s = float(input("Enter Welding Speed (S) (25.0 to 40.0 cm/min): "))
        if check_range(usr_s, 25.0, 40.0):
            break
        else:
            print("Value out of range. Please enter a value between 25.0 and 40.0.")

    if input() == chr(27):
        sys.exit()

    while True:
        usr_g = float(input("Enter Gas Flow Rate (G) (18.0 to 33.0 Litres/min): "))
        if check_range(usr_g, 18.0, 33.0):
            break
        else:
            print("Value out of range. Please enter a value between 18.0 and 33.0.")

    if input() == chr(27):
        sys.exit()

    w = (usr_w - ((6.1 + 7.6) / 2)) / (7.6 - (6.1 + 7.6) / 2)
    v = (usr_v - ((24.0 + 29.0) / 2)) / (29.0 - (24.0 + 29.0) / 2)
    n = (usr_n - ((15.0 + 20.0) / 2)) / (20.0 - (15.0 + 20.0) / 2)
    a = (usr_th - ((80.0 + 100.0) / 2)) / (100.0 - (80.0 + 100.0) / 2)
    s = (usr_s - ((25.0 + 40.0) / 2)) / (40.0 - (25.0 + 40.0) / 2)
    g = (usr_g - ((18.0 + 33.0) / 2)) / (33.0 - (18.0 + 33.0) / 2)

    height = 3.75 - 0.32 * v + 0.45 * w + 0.09 * n - 0.44 * s + 0.12 * a - 0.09 * g + 0.11 * w * a + 0.09 * w * n
    p = 4.02 - 0.05 * v + 1.25 * w + 0.2 * n - 0.53 * s - 0.2 * g + 0.35 * w * n - 0.23 * w * s
    width = 13.27 + 0.24 * v + 1.43 * w - 0.37 * n - 1.22 * s - 0.35 * w * v + 0.22 * w * n + 0.22 * s * a + 0.24 * n * s
    wh = width / height
    wp = width / p

    mind = 43.47 + 6.94 * w + 1.40 * w * v
    i2 = 257.18 + 17.81 * w + 5.31 * v - 4.0 * n - 4.0 * a + 2.8 * s + 2.18 * w * v - 2.18 * w * a - 2.81 * n * a + 2.81 * a * s
    rhi2 = ((v * 2.5) + 26.5) * i2 * 6.0 / ((s * 7.5) + 32.5)
    ap = 31.18 + 14.1 * w - 7.12 * s - 3.5 * w * s + 3.1 * w * n

    print("\nPROCEDURE")
    print("────────────────────────────────────────────────────")
    print("BG&SR responses                       Direct process parameters")
    print(f"penetration          = {p:7.2f} mm      wire feed rate  = {usr_w:7.2f} m/min")
    print(f"height               = {height:7.2f} mm      arc voltage     = {usr_v:7.2f} volts")
    print(f"width                = {width:7.2f} mm      contact tube to = {usr_n:7.2f} mm")
    print(f"w/h                  = {wh:7.2f}         plate distance")
    print(f"w/p                  = {wp:7.2f}         angle           = {usr_th:7.2f} degrees")
    print(f"area of penetration  = {ap:7.2f} mm²    welding speed   = {usr_s:7.2f} cm/min ")
    print(f"dilution             = {mind:7.2f} %     gas flow rate   = {usr_g:7.2f} l/min")
    print(f"RHI                  = {rhi2:7.2f} j/mm.")
    print("────────────────────────────────────────────────────")
    input("Press Enter to return")
    







#third and last remains
def resp_opt():
    global THICKNESS
    global pval,ap,ap1,maxap,minap,size,j,rnum,scpen,user_ch,ctr,counter,hcount,wcount,totalvals,phcount,lkey, size, totalvals, counter, hcount, wcount, phcount, maxh, minh, maxpen, minpen, maxdil, mindil, maxrhi, minrhi, maxap, minap, scpen, mind, rhi2

    # Initialize variables
    wnat = 0.0
    vnat = 0.0
    snat = 0.0
    nnat = 0.0
    anat = 0.0
    gnat = 0.0
    usr_p = 0.0
    p_lo = 0.0
    p_hi = 0.0
    pmax = 0.0
    var_int = 0
    xx = ''
    size=0
    # Define a dictionary to hold pval values
    # Initialize pval as an empty list
    pval = []

    def init():
        global pval
        # Initialize pval with empty dictionaries
        pval = [{} for _ in range(11)]
        for i in range(1, 11):  
            pval[i-1] = {
                'pen': 0.0,
                'dil': 0.0,
                'rhi': 0.0,
                'w1': 0.0,
                'v1': 0.0,
                's1': 0.0,
                'n1': 0.0,
                'a1': 0.0,
                'g1': 0.0,
                'wp1': 0.0,
                'wh1': 0.0,
                'ht1': 0.0,
                'wt1': 0.0,
                'i': 0,  # This is a Python keyword, so using a different name
                'apen': 0.0
            }


    # Call init function to initialize pval
    init()
    def sortarr1():
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii]['rhi'] > pval[jj]['rhi']:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr2():
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii]['rhi'] == pval[jj]['rhi'] and pval[ii]['pen'] < pval[jj]['pen']:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr3():
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii]['rhi'] == pval[jj]['rhi'] and pval[ii]['pen'] == pval[jj]['pen'] \
                        and pval[ii]['wp1'] > pval[jj]['wp1']:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr4():
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii]['rhi'] == pval[jj]['rhi'] and pval[ii]['pen'] == pval[jj]['pen'] \
                        and pval[ii]['wp1'] == pval[jj]['wp1'] and pval[ii]['wh1'] < pval[jj]['wh1']:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr5():
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii]['rhi'] == pval[jj]['rhi'] and pval[ii]['pen'] == pval[jj]['pen'] \
                        and pval[ii]['wp1'] == pval[jj]['wp1'] and pval[ii]['wh1'] == pval[jj]['wh1'] \
                        and (pval[ii]['pen'] / pval[ii]['ht1']) < (pval[jj]['pen'] / pval[jj]['ht1']):
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp

    def sortarr6():
        for ii in range(1, size):
            for jj in range(ii + 1, size + 1):
                if pval[ii]['rhi'] == pval[jj]['rhi'] and pval[ii]['pen'] == pval[jj]['pen'] \
                        and pval[ii]['wp1'] == pval[jj]['wp1'] and pval[ii]['wh1'] == pval[jj]['wh1'] \
                        and (pval[ii]['pen'] / pval[ii]['ht1']) == (pval[jj]['pen'] / pval[jj]['ht1']) \
                        and pval[ii]['dil'] > pval[jj]['dil']:
                    tmp = pval[ii]
                    pval[ii] = pval[jj]
                    pval[jj] = tmp
                    
    def insertrec():
            global size
            if size < 10:
                size += 1
                pval[size] = {
                    'pen': p, 'w1': w, 'v1': v, 'n1': n, 's1': s, 'g1': g, 'a1': a, 'wp1': wp,
                    'wh1': wh, 'ht1': height, 'wt1': width, 'dil': mind, 'apen': ap, 'rhi': rhi2
                }
            else:
                size = 10
                if pval[size]['rhi'] > rhi2:
                    pval[size] = {
                        'pen': p, 'w1': w, 'v1': v, 'n1': n, 's1': s, 'g1': g, 'a1': a, 'wp1': wp,
                        'wh1': wh, 'ht1': height, 'wt1': width, 'dil': mind, 'apen': ap, 'rhi': rhi2
                    }
            if size > 1:
                sortarr1()

    # resp_opt part
    lkey = 'x'
    
    while True:
        usr_p = float(input("Enter penetration range(3.98 mm - 5.82mm) "))
        if check_range(usr_p,3.98 , 5.82):
            break
        else:
            print("Value out of range. Please enter a value between 3.98 and 5.82 .")

    if input() == chr(27):
        sys.exit()

    while True:
        var_int = float(input("Enter Acceptable Variation(1-10%) "))
        if check_range(var_int, 1.0, 10.0):
            break
        else:
            print("Value out of range. Please enter a value between 1.0 and 10.0.")
            
   

    p_lo = usr_p - (var_int / 100) * usr_p
    p_hi = usr_p + (var_int / 100) * usr_p

    if p_lo < 3.99 or p_lo == 3.99:
        p_lo = 4.0
    if p_hi > 5.81 or p_hi == 5.81:
        p_hi = 5.82

    totalvals = 0
    counter = 0
    hcount = 0
    scpen = 0
    wcount = 0
    phcount = 0
    init()
    size = 0
    thn = (33 / 100) * THICKNESS

    w = -1.5
    while w < 1:
        w += 0.5
        v = -1.5
        while v < 1:
            v += 0.5
            n = -1.5
            while n < 1:
                n += 0.5
                s = -1.5
                while s < 1:
                    s += 0.5
                    a = -1.5
                    while a < 1:
                        a += 0.5
                        g = -1.5
                        while g < 1:
                            g += 0.5
                            totalvals += 1
                            height = 3.75 - 0.32 * v + 0.45 * w + 0.09 * n - 0.44 * s + 0.12 * a - 0.09 * g + 0.11 * w * a + 0.09 * w * n

                            if height <= thn:
                                hcount += 1
                                p = 4.02 - 0.05 * v + 1.25 * w + 0.2 * n - 0.53 * s - 0.2 * g + 0.35 * w * n - 0.23 * w * s
                                ph = p / height

                                if ph >= 1.3:
                                    phcount += 1
                                    width = 13.27 + 0.24 * v + 1.43 * w - 0.37 * n - 1.22 * s - 0.35 * w * v + 0.22 * w * n + 0.22 * s * a + 0.24 * n * s
                                    wh = width / height

                                    if 5 >= wh >= 4:
                                        wcount += 1
                                        wp = width / p

                                        if 3.5 >= wp >= 2.5:
                                            counter += 1

                                            if p_lo <= p <= p_hi:
                                                mind = 43.47 + 6.94 * w + 1.40 * w * v
                                                i2 = 257.18 + 17.81 * w + 5.31 * v - 4.0 * n - 4.0 * a + 2.8 * s + 2.18 * w * v - 2.18 * w * a - 2.81 * n * a + 2.81 * a * s
                                                rhi2 = ((v * 2.5) + 26.5) * i2 * 6.0 / ((s * 7.5) + 32.5)
                                                ap = 31.18 + 14.1 * w - 7.12 * s - 3.5 * w * s + 3.1 * w * n

                                                scpen += 1
                                                insertrec()

    sortarr1()
    sortarr2()
    sortarr3()
    sortarr4()
    sortarr5()
    sortarr6()


    print('Value entered by user  : {:.2f} mm'.format(usr_p))
    print()
    print('Values between {:.2f} mm and {:.2f} mm'.format(p_lo, p_hi))
    print('total values =', totalvals)
    print('h pass       =', hcount)
    print('p/h pass     =', phcount)
    print('w/h pass     =', wcount)
    print('w/p pass     =', counter)
    print('scpen        =',scpen)
    print()

    scpen_print = scpen if scpen <= 10 else 10
    print('scpen_print        =',scpen_print)
    print()
    for j in range(1, scpen_print + 1):
        pval_j = pval[j]

        vnat = pval_j['v1'] * 2.5 + 26.5
        wnat = pval_j['w1'] * 0.75 + 6.85
        snat = pval_j['s1'] * 7.5 + 32.5
        nnat = pval_j['n1'] * 2.5 + 17.5
        anat = pval_j['a1'] * 10 + 90
        gnat = pval_j['g1'] * 7.5 + 25.5

        print('   PROCEDURE ')
        print('BG&SR responses                       Direct process parameters')
        print('penetration          = {:.2f} mm    wire feed rate  = {:.2f} m/min'.format(pval_j['pen'], wnat))
        print('height               = {:.2f} mm    arc voltage     = {:.2f} volts'.format(pval_j['ht1'], vnat))
        print('width                = {:.2f} mm    contact tube to = {:.2f} mm'.format(pval_j['wt1'], nnat))
        print('w/h                  = {:.2f}        plate distance'.format(pval_j['wh1']))
        print('w/p                  = {:.2f}        angle           = {:.2f} degrees'.format(pval_j['wp1'], anat))
        print('area of penetration  = {:.2f} mm²    welding speed   = {:.2f} cm/min'.format(pval_j['apen'], snat))
        print('dilution             = {:.2f} %     gas flow rate   = {:.2f} l/min'.format(pval_j['dil'], gnat))
        print('RHI                  = {:.2f} j/mm.'.format(pval_j['rhi']))

        print('Press ENTER to continue or ESC to return')
        xx = input()
        if xx == chr(27):
            break






# Main function
def main():
    global user_ch, lkey

    while user_ch != 4:
        print('OPTIMIZATION ALGORITHM FOR WELDING PROCEDURE')
        print('GMAW of Aluminium Alloy 5083, 13mm thick plate')
        print('Default Parameter Ranges')
        print('Wire Feed Rate           (W) :  6.1 to   7.6 m/min')
        print('Arc Voltage              (V) : 24.0 to  29.0 Volts')
        print('Nozzle to Plate Distance (N) : 15.0 to  20.0 mm')
        print('Electrode Inclination    (A) : 80.0 to 100.0 degrees')
        print('Welding Speed            (S) : 25.0 to  40.0 cm/min')
        print('Gas Flow Rate            (G) : 18.0 to  33.0 l/min')
        print('OPTIONS')
        print('1. Optimum Procedure for Default Parameter Ranges')
        print('2. Optimum Procedure for Parameters specified by User')
        print('3. Optimum Procedure for specified Response, Penetration')
        print('4. Quit')

        user_ch = int(input('Please Enter your Option 1-4: '))

        if user_ch == 1:
            optimized()
        elif user_ch == 2:
            usr_opt()
        elif user_ch == 3:
            resp_opt()

    print('Exiting program...')

if __name__ == "__main__":
    main()
