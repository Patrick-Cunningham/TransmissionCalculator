import math
import matplotlib.pyplot as plt

class transmission:
    def __init__(self, code: str, description: str, gear1: float, gear2: float, gear3: float, gear4: float, gear5: float, gear6: float, diffRatio: float):
        self.code = code
        self.gear = []
        self.gear.append(0)
        self.gear.append(gear1)
        self.gear.append(gear2)
        self.gear.append(gear3)
        self.gear.append(gear4)
        self.gear.append(gear5)
        self.gear.append(gear6)
        self.diffRatio = diffRatio
        self.description = description

class tire:
    def __init__(self, width: float, aspectRatio: float, wheelSize: float):
        if aspectRatio > 0 and aspectRatio <= 100:
            self.aspectRatio = aspectRatio
        else:
            raise Exception("aspectRatio must be between 1 and 100")
        self.width = width
        self.wheelSize = wheelSize
    
    def diameter(self): #In MM
        sidewallHeight = self.width * (self.aspectRatio/100.0)
        wheelSizeMM = self.wheelSize * 25.4
        return wheelSizeMM + sidewallHeight + sidewallHeight
    
    def circumference(self):
        return math.pi * self.diameter()
    

def rpmToMPH(trans: transmission, tire: tire, rpm: float, gear: int):
    if trans.gear[gear] is not None:
        return ((((rpm*60) / trans.gear[gear]) / trans.diffRatio) * tire.circumference()) / 1609344.0 #Miles per Hour
    else:
        raise Exception("Gear not available in selected transmission")
   
def sweepAll(trans: str, tlist, tire: tire, rpmMin: float, rpmMax: float, color: str):
    for t in tlist:
        if t.code == trans:
            speed = []
            rpm = []
            for i in range(1, 6):
                if t.gear[i] is not None:
                    if i == 1:
                        for x in range(rpmMin, rpmMax, 10):
                            speed.append(rpmToMPH(t, tire, x, i))
                            rpm.append(x)
                    else:
                        for x in range(rpmMin, rpmMax, 10):
                            a = rpmToMPH(t, tire, x, i)
                            if a >= (speed[len(speed)-1] - 0):
                                speed.append(a)
                                rpm.append(x)
                            
            plt.plot(speed, rpm, color=color, label=t.code+" | "+t.description)
    
    del speed
    del rpm

trnsList = []
trnsList.append(transmission(code="EBD", description="1.8T Mk4 Golf (AGU Engine)", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="ENJ", description="1.8T (2000) Mk4 Golf", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.684))
trnsList.append(transmission(code="EHA", description="1.8T AWP 180hp", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.824))
trnsList.append(transmission(code="CZM", description="2.0L Beetle '98", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="DQY", description="1998-2001 TDI Beetle", gear1=3.778, gear2=2.118, gear3=1.360, gear4=0.971, gear5=0.756, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="EGD", description="1.8T Beetle '99", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.938))
trnsList.append(transmission(code="DZQ", description="2.0L Beetle / Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EBP", description="2.0L Beetle / Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EGT", description="2.0L Beetle / Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EKG", description="2.0L Beetle / Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EKH", description="2.0L Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EMS", description="2.0L Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EZK", description="2.0L Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="FBV", description="2.0L Golf / Jetta IV", gear1=3.778, gear2=2.118, gear3=1.360, gear4=1.029, gear5=0.837, gear6=None, diffRatio=4.235))
trnsList.append(transmission(code="EBJ", description="TDI Beetle, Golf/Jetta IV 4cyl", gear1=3.778, gear2=2.118, gear3=1.360, gear4=0.971, gear5=0.756, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="EGR", description="TDI Beetle, Golf/Jetta IV 4cyl", gear1=3.778, gear2=2.118, gear3=1.360, gear4=0.971, gear5=0.756, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="EBQ", description="1.8T Beetle,Golf/Jetta IV", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.938))
trnsList.append(transmission(code="EMT", description="1.8T Beetle,Golf/Jetta IV", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.938))
trnsList.append(transmission(code="EGQ", description="2000-up 1.8T Golf/Jetta IV", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.938))
trnsList.append(transmission(code="FBW", description="2000-up 1.8T Golf/Jetta IV", gear1=3.300, gear2=1.944, gear3=1.308, gear4=1.029, gear5=0.837, gear6=None, diffRatio=3.938))
trnsList.append(transmission(code="DZC", description="VR6 Golf / Jetta IV", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="EHC", description="VR6 Golf / Jetta IV", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="EGF", description="VR6 Golf / Jetta IV", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="EWW", description="VR6 Golf / Jetta IV", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="FBY", description="VR6 Golf / Jetta IV", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=3.389))
trnsList.append(transmission(code="FCF", description="VR6 Golf / Jetta IV", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=3.389))

trnsList.append(transmission(code="CUSTOM", description="VR6 Golf / Jetta IV gears, 2.0L Diff", gear1=3.625, gear2=2.071, gear3=1.474, gear4=1.038, gear5=0.844, gear6=None, diffRatio=4.235))

#trnsList.append(transmission(code="", gear1=, gear2=, gear3=, gear4=, gear5=, gear6=None, diffRatio=)) # 

t = tire(width=205, aspectRatio=55, wheelSize=15)

rpmMin = 1000
rpmMax = 7000

plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(14,6))
plt.get_current_fig_manager().set_window_title("Transmission Calculator")


sweepAll("CUSTOM", trnsList, t, rpmMin, rpmMax, "green")
sweepAll("EHA", trnsList, t, rpmMin, rpmMax, "red")
sweepAll("CZM", trnsList, t, rpmMin, rpmMax, "blue")


plt.xlabel("Speed (MPH)")
plt.ylabel("RPM")
plt.xlim(0, 160)
plt.ylim(rpmMin, rpmMax+500)
plt.legend()
plt.title("Speed (MPH) vs RPM")
plt.show()