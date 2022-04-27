import cmath
import math
from cmath import phase

def resize(r,r_x,r_y,s_x,s_y):
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
    plot = resize(r,a1,b1,a2,b2)
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
   