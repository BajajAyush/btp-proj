from flask import Flask,render_template,request
app = Flask(__name__)

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
pval = [Record() for _ in range(10)]
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

    # No print statements here


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'GET':
        optimized()
        results = []  # Store optimization results
        for j in range(1, scpen + 1):
            vnat = pval[j].v1 * 2.5 + 26.5
            wnat = pval[j].w1 * 0.75 + 6.85
            snat = pval[j].s1 * 7.5 + 32.5
            nnat = pval[j].n1 * 2.5 + 17.5
            anat = pval[j].a1 * 10 + 90
            gnat = pval[j].g1 * 7.5 + 25.5

            result = {
                'penetration': pval[j].pen,
                'wire_feed_rate': wnat,
                'arc_voltage': vnat,
                'contact_tube_to': nnat,
                'plate_distance': pval[j].wh1,
                'angle': anat,
                'welding_speed': snat,
                'gas_flow_rate': gnat,
                'rhi': pval[j].rhi,
                'area_of_penetration': pval[j].apen
            }
            results.append(result)

        return render_template('results.html', results=results)
    else:
        return render_template('index.html')


        def check_range(value, min_val, max_val):
          return min_val <= value <= max_val

def usr_opt(usr_w, usr_v, usr_n, usr_th, usr_s, usr_g):
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
    
    return {
        'height': height,
        'p': p,
        'width': width,
        'wh': wh,
        'wp': wp,
        'mind': mind,
        'rhi2': rhi2,
        'ap': ap
    }

@app.route('/secondf', methods=['POST'])
def secondf():
    if request.method == 'POST':
        # Retrieve form data
        usr_w = float(request.form['wire_feed_rate'])
        usr_v = float(request.form['arc_voltage'])
        usr_n = float(request.form['nozzle_distance'])
        usr_th = float(request.form['electrode_inclination'])
        usr_s = float(request.form['welding_speed'])
        usr_g = float(request.form['gas_flow_rate'])

        # Call usr_opt() to process the form data
        result = usr_opt(usr_w, usr_v, usr_n, usr_th, usr_s, usr_g)

        return render_template('second.html', result=result)

@app.route('/parameters', methods=['GET', 'POST'])
def parameters():
    if request.method == 'POST':
        # Retrieve form data
        usr_w = float(request.form['wire_feed_rate'])
        usr_v = float(request.form['arc_voltage'])
        usr_n = float(request.form['nozzle_distance'])
        usr_th = float(request.form['electrode_inclination'])
        usr_s = float(request.form['welding_speed'])
        usr_g = float(request.form['gas_flow_rate'])

        # Call usr_opt() to process the form data
        result = usr_opt(usr_w, usr_v, usr_n, usr_th, usr_s, usr_g)

        # Render the parameters template with the calculated values
        return render_template('secondf.html', result=result)
    else:
        return render_template('secondf.html')     


def resp_opt(user_p, vaer_int):
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
        for i in range(1, 11):  # Pascal uses one-based indexing
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
 
    usr_p = user_p
    var_int = vaer_int
       

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


@app.route('/thirdparameters', methods=['GET', 'POST'])
def third_parameters():
    if request.method == 'POST':
        usr_p = float(request.form['usr_p'])
        var_int = float(request.form['var_int'])

        # Call the resp_opt function with user input
        #print(usr_p,var_int)
        resp_opt(usr_p, var_int)

        # In resp_opt function after calculation
       # print(scpen)
        scpen_print = scpen if scpen <= 10 else 10

        results = []  # Initialize results list

        for j in range(1, scpen_print + 1):
            pval_j = pval[j]

            vnat = pval_j['v1'] * 2.5 + 26.5
            wnat = pval_j['w1'] * 0.75 + 6.85
            snat = pval_j['s1'] * 7.5 + 32.5
            nnat = pval_j['n1'] * 2.5 + 17.5
            anat = pval_j['a1'] * 10 + 90
            gnat = pval_j['g1'] * 7.5 + 25.5

            # Append the results as a dictionary to the results list
            results.append({
                'penetration': round(pval_j['pen'], 2),
                'wire_feed_rate': round(wnat, 2),
                'arc_voltage': round(vnat, 2),
                'contact_tube_distance': round(nnat, 2),
                'width_height_ratio': round(pval_j['wh1'], 2),
                'width_penetration_ratio': round(pval_j['wp1'], 2),
                'area_of_penetration': round(pval_j['apen'], 2),
                'dilution': round(pval_j['dil'], 2),
                'RHI': round(pval_j['rhi'], 2)
            })
            #print(results)

        # Render a new HTML page to display the results
        return render_template('thirdresult.html', results=results)
    else:
        return render_template('thirdparameters.html')






if __name__ == "__main__":
    app.run(debug=True)