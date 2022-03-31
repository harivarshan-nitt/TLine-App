import math

def short_line(form_input):
    output={}
    return output

def medium_line(form_input):
    return form_input

def long_line(form_input):
    return form_input



def inductance(mgmd,sgmd):
    return (2*(10**(-7))*math.log(mgmd/sgmd))/1000

def capacitance(mgmd,sgmd):
    return ((10**(-9))/18*math.log(mgmd/sgmd))/1000

def inductance_reactance(i,l,f):
    return i*l*f*2*math.pi

def capacitance_reactance(c,l,f):
    return l/c*f*2*math.pi

def mgmd(a,b,c):
    return (a*b*c*a*b*c)**(1/6)

def sgmd(n,r,l):
    if n==1:
        return 0.7788*r
    return
        

def radius(dia,n):
    if (n==1):
        return dia/2
    elif (n==7):
        return 3*dia/2
    elif (n==19):
        return 5*dia/2
    elif (n==37):
        return 7*dia/2
    else:
        return 9*dia/2

def shortline_cc():
    return "0 A"

def shortline_ABCD(L,R):
    return 1,complex(R,L),0,1

def Ir(Pr,pf,Vr):
    return Pr/(((3)**0.5)*Vr*pf)

def sending_end(A,B,C,D,Vr,Ir):
    Vs = A * Vr + B * Ir
    Is = C * Vr + D * Ir
    return Vs,Is

if __name__=="__main__":
    print('TLine Models')
