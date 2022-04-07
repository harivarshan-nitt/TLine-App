import cmath
import math
from cmath import phase

def inductance(mgmd,sgmd):
    return (2*(10**(-7))*math.log(mgmd/sgmd))*1000

def capacitance(mgmd,sgmd):
    return ((10**(-9))/(18*math.log(mgmd/sgmd)))*1000

def inductance_reactance(i,l,f):
    return i*l*f*2*math.pi

def capacitance_reactance(c,l,f):
    return 1/(c*f*2*math.pi*l)

def mgmd(a,b,c):
    return (a*b*c)**(1/3)

def sgmd(n,r,l):
    if n==1:
        return 0.7788*r
    elif n==2:
        return (r*0.7788*(l**(n-1)))**(1/n)
    elif n==3:
        return (0.7788*r*(l**(n-1)))**(1/n)
    elif n==4:
        return ((2**0.5)*0.7788*r*(l**(n-1)))**(1/n)
    elif n==5:
        return ((1.618**2)*0.7788*r*(l**(n-1)))**(1/n)
    elif n==6:
        return (3*2*0.7788*r*(l**(n-1)))**(1/n)
    elif n==7:
        return (16.39*0.7788*r*(l**(n-1)))**(1/n)
    else:
        return (9.2426*2.1631*0.7788*r*(l**(n-1)))**(1/n)

def sgmd_c(n,r,l):
    if n==1:
        return r
    elif n==2:
        return (r*(l**(n-1)))**(1/n)
    elif n==3:
        return (r*(l**(n-1)))**(1/n)
    elif n==4:
        return ((2**0.5)*r*(l**(n-1)))**(1/n)
    elif n==5:
        return ((1.618**2)*r*(l**(n-1)))**(1/n)
    elif n==6:
        return (3*2*r*(l**(n-1)))**(1/n)
    elif n==7:
        return (16.39*r*(l**(n-1)))**(1/n)
    else:
        return (9.2426*2.1631*r*(l**(n-1)))**(1/n)
    
def Z(R,L):
    return complex(R,L)

def Y (C):
    return complex(0,1/C)

def Zc(C):
    return complex(0,C)
    
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

def cc(Is,Ir):
    return Is-Ir

def shortline_ABCD(L,R):
    return complex(1,0),complex(R,L),complex(0,0),complex(1,0)

def mediumline_ABCD(Z,Y):
    return Z*Y/2 +1,Z,Y*(Z*Y/4 +1),Z*Y/2 +1

def longline_ABCD(Z,Y):
    return cmath.cosh((Z*Y)**0.5),((Z/Y)**0.5)*cmath.sinh((Z*Y)**0.5),((Y/Z)**0.5)*cmath.sinh((Z*Y)**0.5) ,cmath.cosh((Z*Y)**0.5)

def IR(Pr,pf,Vr):
    return complex(Pr/(((3)**0.5)*Vr*pf)*pf,Pr/(((3)**0.5)*Vr*pf)*math.sin(math.acos(pf)))

def sending_end(A,B,C,D,Vr,Ir):
    Vs = A*Vr + B*Ir
    Is = C*Vr + D*Ir
    return Vs,Is

def VR(vs,vr):
    return (abs(vs) - abs(vr))*100/abs(vs)*100

def pf(V,I):
    return math.cos(cmath.phase(V/I))

def powerLoss_eff(vr,vs,Ir,Is):
    return (abs(vs)*abs(Is)*pf(vs,Is) - abs(vr)*abs(Ir)*pf(vr,Ir))*(3**0.5),( abs(vr)*abs(Ir)*pf(vr,Ir))*100/(abs(vs)*abs(Is)*pf(vs,Is) )

def shuntcomp(Vs,Is):
    return abs(Vs)*abs(Is)*math.sin(phase(Vs/Is))/1000000

def resize(Vs,Vr,A,B,D):
    r = abs(Vs)*abs(Vr)/(abs(B)*1000000)
    r_x =(-1)*abs(A)*(abs(Vr)**2)*math.cos(phase(B)-phase(A))/(abs(B)*1000000)
    r_y = (-1)*abs(A)*(abs(Vr)**2)*math.sin(phase(B)-phase(A))/1000000
    s_x = abs(D)*(abs(Vs)**2)*math.cos(phase(B)-phase(D))/(abs(B)*1000000)
    s_y = abs(D)*(abs(Vs)**2)*math.sin(phase(B)-phase(D))/(abs(B)*1000000)
    #max_p = max(r,r_x,r_y,s_x,s_y)
    max_p = 2*max(r+((s_x**2+s_y**2)**0.5),r+((r_x**2+r_y**2)**0.5))
    if max_p > 380:
        Ra,R_x,R_y,S_x,S_y = r*(1/int(1+ max_p/380 )),r_x*(1/int(1+ max_p/380 )),r_y*(1/int(1+ max_p/380 )),s_x*(1/int(1+ max_p/380 )),s_y*(1/int(1+ max_p/380 ))
        scale = int(1+ max_p/380 )
    else:
        Ra,R_x,R_y,S_x,S_y = r,r_x,r_y,s_x,s_y
        scale = 1
    plot = {}
    plot["radius"] =Ra
    plot["r_x"] =R_x
    plot["r_y"] =R_y
    plot["s_x"] =S_x
    plot["s_y"] =S_y
    plot["Scale"] = f" x,y: 1 unit = {scale} units"
    plot["Radius"] =r
    plot["Receiving end X"] =r_x
    plot["Receiving end Y"] =r_y
    plot["Sending end X"] =s_x
    plot["Sending end Y"] =s_y

    return plot

def res(r,r_x,r_y,s_x,s_y):
    max_p = 2*max(r+((s_x**2+s_y**2)**0.5),r+((r_x**2+r_y**2)**0.5))
    if max_p > 380:
        Ra,R_x,R_y,S_x,S_y = r*(1/int(1+ max_p/380 )),r_x*(1/int(1+ max_p/380 )),r_y*(1/int(1+ max_p/380 )),s_x*(1/int(1+ max_p/380 )),s_y*(1/int(1+ max_p/380 ))
        scale = int(1+ max_p/380 )
    else:
        Ra,R_x,R_y,S_x,S_y = r,r_x,r_y,s_x,s_y
        scale = 1
    plot = {}
    plot["radius"] =Ra
    plot["r_x"] =R_x
    plot["r_y"] =R_y
    plot["s_x"] =S_x
    plot["s_y"] =S_y
    plot["Scale"] = f" x,y: 1 unit = {scale} units"
    plot["Radius"] =r
    plot["Receiving end X"] =r_x
    plot["Receiving end Y"] =r_y
    plot["Sending end X"] =s_x
    plot["Sending end Y"] =s_y

    return plot

def short_line(form_input):
    m = 0
    if form_input["sym"]=="Symmentrical":
        m = mgmd(float(form_input["space"]),float(form_input["space"]),float(form_input["space"]))
    else:
        m = mgmd(float(form_input["space_12"]),float(form_input["space_23"]),float(form_input["space_31"]))
    s = sgmd(int(form_input["n_sub_con"]),float(radius(float(form_input["strand_dm"]),int(form_input["n_strand"]))),float(form_input["sub_space"]))
    s_c = sgmd_c(int(form_input["n_sub_con"]),float(radius(float(form_input["strand_dm"]),int(form_input["n_strand"]))),float(form_input["sub_space"]))
    ind_km = inductance(m,s)
    cap_km = capacitance(m,s_c)
    ind_rea = inductance_reactance(ind_km,float(form_input["len"]),float(form_input["f"]))
    cap_rea = capacitance_reactance(cap_km,float(form_input["len"]),float(form_input["f"]))
    A,B,C,D= shortline_ABCD(ind_rea,float(form_input["R"])*float(form_input["len"]))
    Vr = complex(float(form_input["V"])*1000,0)/(3**0.5)
    Ir = IR(float(form_input["L"])*1000000,float(form_input["pf"]),float(form_input["V"])*1000)
    Vs,Is = sending_end(A,B,C,D,Vr,Ir)
    CC = cc(Is,Ir)
    ploss,eff=powerLoss_eff(Vr,Vs,Ir,Is)
    sc = shuntcomp(Vr,Ir)
    Vs_3 = Vs*(3**0.5)
    output = {}
    output["Inductance / km"]=f"{round(ind_km*1000,8)} mH / km"
    output["Capacitance / km"]=f"{round(cap_km*1000000000000,8)} pF / km"
    output["Inductive reactance"]=f"{round(ind_rea,8)} ohm"
    output["Capacitive reactance"]=f"{round(cap_rea,8)} ohm"
    output["Charging current"]= f"{round(abs(CC),8)} ∠ {round(phase(CC),8)} A"
    output["A"] = f"{round(abs(A),8)} ∠ {round(phase(A),8)}"
    output["B"]=f"{round(abs(B),8)} ∠ {round(phase(B),8)} ohm"
    output["C"]=f"{round(abs(C),8)} ∠ {round(phase(C),8)} S"
    output["D"]=f"{round(abs(D),8)} ∠ {round(phase(D),8)}"
    output["Sending end Voltage"]=f"{round(abs(Vs_3/1000),8)} ∠ {round(phase(Vs_3/1000),8)} kV"
    output["Sending end Current"]=f"{round(abs(Is),8)} ∠ {round(phase(Is),8)} A"
    output["Voltage regulation"]=f"{round(VR(Vs,Vr),8)} %"
    output["Power loss"] = f"{round(ploss/1000000,8)} MW"
    output["Efficiency"]=f"{round(eff,8)} %"
    if sc >=0 :
        output["Shunt Compensation Type"]="Inductive"
    else :
        output["Shunt Compensation Type"]="Capacitive"
        sc = sc*(-1)
    output["Shunt Compensation"]=f"{round(sc,8)} MVAR"
    plot_p = resize(Vs,Vr,A,B,D)
    return output,plot_p

def medium_line(form_input):
    m = 0
    if form_input["sym"]=="Symmentrical":
        m = mgmd(float(form_input["space"]),float(form_input["space"]),float(form_input["space"]))
    else:
        m = mgmd(float(form_input["space_12"]),float(form_input["space_23"]),float(form_input["space_31"]))
    s = sgmd(int(form_input["n_sub_con"]),float(radius(float(form_input["strand_dm"]),int(form_input["n_strand"]))),float(form_input["sub_space"]))
    s_c = sgmd_c(int(form_input["n_sub_con"]),float(radius(float(form_input["strand_dm"]),int(form_input["n_strand"]))),float(form_input["sub_space"]))
    ind_km = inductance(m,s)
    cap_km = capacitance(m,s_c)
    ind_rea = inductance_reactance(ind_km,float(form_input["len"]),float(form_input["f"]))
    cap_rea = capacitance_reactance(cap_km,float(form_input["len"]),float(form_input["f"]))
    A,B,C,D= mediumline_ABCD(Z(float(form_input["R"])*float(form_input["len"]),ind_rea),Y(cap_rea))
    Vr =complex(float(form_input["V"])*1000,0)/(3**0.5)
    Ir = IR(float(form_input["L"])*1000000,float(form_input["pf"]),float(form_input["V"])*1000)
    Vs,Is = sending_end(A,B,C,D,Vr,Ir)
    CC = cc(Is,Ir)
    ploss,eff=powerLoss_eff(Vr,Vs,Ir,Is)
    Vs_3 = Vs*(3**0.5)
    output = {}
    output["Inductance / km"]=f"{round(ind_km*1000,8)} mH / km"
    output["Capacitance / km"]=f"{round(cap_km*1000000,8)} uF / km"
    output["Inductive reactance"]=f"{round(ind_rea,8)} ohm"
    output["Capacitive reactance"]=f"{round(cap_rea,8)} ohm"
    output["Charging current"]= f"{round(abs(CC),8)} ∠ {round(phase(CC),8)} A"
    output["A"] = f"{round(abs(A),8)} ∠ {round(phase(A),8)}"
    output["B"]=f"{round(abs(B),8)} ∠ {round(phase(B),8)} ohm"
    output["C"]=f"{round(abs(C),8)} ∠ {round(phase(C),8)} S"
    output["D"]=f"{round(abs(D),8)} ∠ {round(phase(D),8)}"
    output["Sending end Voltage"]=f"{round(abs(Vs_3/1000),8)} ∠ {round(phase(Vs_3/1000),8)} kV"
    output["Sending end Current"]=f"{round(abs(Is),8)} ∠ {round(phase(Is),8)} A"
    output["Voltage regulation"]=f"{round(VR(Vs,Vr),8)} %"
    output["Power loss"] = f"{round(ploss/1000000,8)} MW"
    output["Efficiency"]=f"{round(eff,8)} %"
    plot_p = resize(Vs,Vr,A,B,D)
    return output,plot_p

def long_line(form_input):
    m = 0
    if form_input["sym"]=="Symmentrical":
        m = mgmd(float(form_input["space"]),float(form_input["space"]),float(form_input["space"]))
    else:
        m = mgmd(float(form_input["space_12"]),float(form_input["space_23"]),float(form_input["space_31"]))
    s = sgmd(int(form_input["n_sub_con"]),float(radius(float(form_input["strand_dm"]),int(form_input["n_strand"]))),float(form_input["sub_space"]))
    s_c = sgmd_c(int(form_input["n_sub_con"]),float(radius(float(form_input["strand_dm"]),int(form_input["n_strand"]))),float(form_input["sub_space"]))
    ind_km = inductance(m,s)
    cap_km = capacitance(m,s_c)
    ind_rea = inductance_reactance(ind_km,float(form_input["len"]),float(form_input["f"]))
    cap_rea = capacitance_reactance(cap_km,float(form_input["len"]),float(form_input["f"]))
    A,B,C,D= longline_ABCD(Z(float(form_input["R"])*float(form_input["len"]),ind_rea),Y(cap_rea))
    Vr =complex(float(form_input["V"])*1000,0)/(3**0.5)
    Ir = IR(float(form_input["L"])*1000000,float(form_input["pf"]),float(form_input["V"])*1000)
    Vs,Is = sending_end(A,B,C,D,Vr,Ir)
    CC = cc(Is,Ir)
    ploss,eff=powerLoss_eff(Vr,Vs,Ir,Is)
    Vs_3 = Vs*(3**0.5)
    output = {}
    output["Inductance / km"]=f"{round(ind_km*1000,8)} mH / km"
    output["Capacitance / km"]=f"{round(cap_km*1000000,8)} uF / km"
    output["Inductive reactance"]=f"{round(ind_rea,8)} ohm"
    output["Capacitive reactance"]=f"{round(cap_rea,8)} ohm"
    output["Charging current"]= f"{round(abs(CC),8)} ∠ {round(phase(CC),8)} A"
    output["A"] = f"{round(abs(A),8)} ∠ {round(phase(A),8)}"
    output["B"]=f"{round(abs(B),8)} ∠ {round(phase(B),8)} ohm"
    output["C"]=f"{round(abs(C),8)} ∠ {round(phase(C),8)} S"
    output["D"]=f"{round(abs(D),8)} ∠ {round(phase(D),8)}"
    output["Sending end Voltage"]=f"{round(abs(Vs_3/1000),8)} ∠ {round(phase(Vs_3/1000),8)} kV"
    output["Sending end Current"]=f"{round(abs(Is),8)} ∠ {round(phase(Is),8)} A"
    output["Voltage regulation"]=f"{round(VR(Vs,Vr),8)} %"
    output["Power loss"] = f"{round(ploss/1000000,8)} MW"
    output["Efficiency"]=f"{round(eff,8)} %"
    plot_p = resize(Vs,Vr,A,B,D)
    return output,plot_p

def compute(i):
    if i["sym"]=="Symmentrical":
        a=float(i["space"])
        b=a
        c=a
    else:
        a=float(i["space_12"])
        b=float(i["space_23"])
        c=float(i["space_31"])
    subcon=int(i["n_sub_con"])
    subspa = float(i["sub_space"])
    d=subspa*10
    nos =int(i["n_strand"])
    line =float(i["len"])
    type = i["model"]
    r =float(i["R"])
    f = float(i["f"])
    dia= float(i["strand_dm"])
    V = float(i["V"])*1000
    Pr = float(i["L"])*1000000
    pf=float(i["pf"])
    l=(3+((12*nos)-3)**(1/2))/6
    rad=dia*(2*l-1)/2
    h=0.7788*rad
    if subcon==1:
        SGMl=h
        SGMc=rad
    elif subcon==2:
        SGMl=(h*d)**(1/2)
        SGMc=(rad*d)**(1/2)
    elif subcon==3:
        SGMl=(h*d*d)**(1/3)
        SGMc=(rad*d*d)**(1/3)
    elif subcon==4:
        SGMl=(h*1.414*d*d*d)**(1/4)
        SGMc=(rad*1.414*d*d*d)**(1/4)
    elif subcon==5:
        SGMl=(3.23606*d*d*d*d*h)**(1/5)
        SGMc=(3.23606*d*d*d*d*rad)**(1/5)
    else:
        SGMl=(6*h*d*d*d*d*d)**(1/6)
        SGMc=(6*rad*d*d*d*d*d)**(1/6)
    
    GMD=(a*b*c)**(1/3)
    L=2*0.0001*math.log(GMD*1000/SGMl)
    Ca=(2*(10**-9)*8.854*3.14)/(math.log(GMD*1000/SGMc))
    R=r*line
    X=line*L*2*3.14*f
    Z=R+(X)*1j
    Y=(2*3.14*Ca*line)*1j
    if type=="short":
        A=1
        C=0
        D=A
        B=Z
    elif type=="medium":
        A=1+(Z*Y*0.5)
        B=Z
        C=Y*(1+(0.25*Y*Z))
        D=A
    elif type=="long":
        Zc=((Z/line)/(Y/line))**(1/2)
        Yc=((Z/line)*(Y/line))**(1/2)
        A=(2.71828**(Yc*line)+2.71828**(Yc*line*-1))*0.5
        B=(2.71828**(Yc*line)-2.71828**(Yc*line*-1))*0.5*Zc
        C=(2.71828**(Yc*line)-2.71828**(Yc*line*-1))*0.5*(1/Zc)
        D=A
    I=Pr/(pf*V*(3**(0.5)))
    Vr=V/(3**0.5)
    Ir=I*pf-(I*((1-(pf**2))**(0.5))*1j)
    Vs=A*Vr+B*Ir
    Is=C*Vr+D*Ir

    Vore=(abs(Vs)-abs(Vr))/abs(Vs)

    los=(abs(Vs)*abs(Is)*math.cos(cmath.phase(Vs/Is)))-(abs(Vr)*abs(Ir)*math.cos(cmath.phase(Vr/Ir)))
    loss=los*(3**0.5)
    eff=(abs(Vr)*abs(Ir)*math.cos(cmath.phase(Vr/Ir)))/(abs(Vs)*abs(Is)*math.cos(cmath.phase(Vs/Is)))
    output={}
    output["Inductance / km"]=f"{round(L*1000,8)} mH / km"
    output["Capacitance / km"]=f"{round(Ca*1000000,8)} uF / km"
    output["Inductive reactance"]=f"{round(X,8)} ohm"
    output["Capacitive reactance"]=f"{round(abs(1/Y),8)} ohm"
    output["Charging current"]= f"{round(abs(Is-Ir),8)} ∠ {round(phase(Is-Ir),8)} A"
    output["A"] = f"{round(abs(A),8)} ∠ {round(phase(A),8)}"
    output["B"]=f"{round(abs(B),8)} ∠ {round(phase(B),8)} ohm"
    output["C"]=f"{round(abs(C),8)} ∠ {round(phase(C),8)} S"
    output["D"]=f"{round(abs(D),8)} ∠ {round(phase(D),8)}"
    output["Sending end Voltage"]=f"{round(abs((Vs*(3**0.5))/1000),8)} ∠ {round(phase((Vs*(3**0.5))/1000),8)} kV"
    output["Sending end Current"]=f"{round(abs(Is),8)} ∠ {round(phase(Is),8)} A"
    output["Voltage regulation"]=f"{round(Vore*100,8)} %"
    output["Power loss"] = f"{round(loss/1000,8)} kW"
    output["Efficiency"]=f"{round(eff*100,8)} %"
    a1=(abs(A)*abs(Vr)*abs(Vr)/abs(B))*math.cos(cmath.phase(B/A))*-1/1000000
    b1=(abs(A)*abs(Vr)*abs(Vr)/abs(B))*math.sin(cmath.phase(B/A))*-1/1000000
    a2=(abs(A)*abs(Vs)*abs(Vs)/abs(B))*math.cos(cmath.phase(B/A))/1000000
    b2=(abs(A)*abs(Vs)*abs(Vs)/abs(B))*math.sin(cmath.phase(B/A))/1000000
    r=abs(Vs)*abs(Vr)/abs(B)/1000000
    plot = res(r,a1,b1,a2,b2)
    if type=="short":
        P=Pr/3000000
        Ql=((1-(pf**2))**(0.5))*P/pf
        Qr=(((r**2)-((P-a1)**2))**(0.5))+b1
        Qc = Qr - Ql
        if Qc < 0:
            output["Shunt Compensation Type"]="Capacitive"
            output["Shunt Compensation"]=f"{(-1)*3*(Qr-Ql)} MVAR"
        elif Qc > 0:
            output["Shunt Compensation Type"]="Inductive"
            output["Shunt Compensation"]=f"{3*(Qr-Ql),8} MVAR"
    
    return  output , plot


if __name__=="__main__":
    print('TLine Models')
    input ={'sym': 'Symmentrical', 'space': '3', 'space_12': '5', 'space_23': '5', 'space_31': '4', 'n_sub_con': '1', 'sub_space': '2.5', 'n_strand': '7', 'strand_dm':'5', 'len': '11', 'R': '0.3', 'f': '50', 'V': '230000', 'L': '40', 'pf': '0.8', 'bool': 'false','model':'short'}
    o , p = compute(input)
    #print(o)
    