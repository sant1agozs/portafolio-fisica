# Caso numérico Tema 9: Voyager 2 en Júpiter. Separa |Δv| (cambio del vector) de Δ|v| (cambio de rapidez).
# Datos: NASA/JPL Horizons, estados en 1979-07-09 22:30 TDB, eclíptica J2000 (ver README.md).
import numpy as np
mu=1.26686534e8
r=np.array([4.388609102395209E+05,5.659771102205508E+05,-8.633416661730577E+04])
v=np.array([-1.600160538287928E+01,1.237446188235658E+01,-2.409809392411857E-01])
VJ=np.array([-8.971602603017415E+00,-9.055345595432266E+00,2.381804089732373E-01])
R=np.linalg.norm(r);V=np.linalg.norm(v)
E=V**2/2-mu/R; vinf=np.sqrt(2*E)
h=np.cross(r,v); evec=np.cross(v,h)/mu - r/R; e=np.linalg.norm(evec)
rp=np.linalg.norm(h)**2/mu/(1+e)
print("R",R,"V",V,"vinf",vinf,"e",e,"rp",rp)
# asymptote directions: angle of true anomaly limit nu_inf = arccos(-1/e)
nu=np.arccos(-1/e)
p_hat=evec/e; hhat=h/np.linalg.norm(h); q_hat=np.cross(hhat,p_hat)
# velocity at true anomaly nu: v = sqrt(mu/p)*(-sin nu p + (e+cos nu) q)
def vel(n): 
    p=np.linalg.norm(h)**2/mu
    return np.sqrt(mu/p)*(-np.sin(n)*p_hat+(e+np.cos(n))*q_hat)
vin=vel(-nu+1e-12); vout=vel(nu-1e-12)
print("|vin|,|vout|",np.linalg.norm(vin),np.linalg.norm(vout))
d=vout-vin; delta=np.degrees(np.arccos(np.dot(vin,vout)/vinf**2))
print("delta",delta,"|dv|",np.linalg.norm(d), 2*vinf*np.sin(np.radians(delta/2)))
hin=VJ+vin; hout=VJ+vout
print("|VJ|",np.linalg.norm(VJ),"helio in",np.linalg.norm(hin),"out",np.linalg.norm(hout),"Δ|v|",np.linalg.norm(hout)-np.linalg.norm(hin))
print("angle VJ vs dv",np.degrees(np.arccos(np.dot(VJ,d)/np.linalg.norm(VJ)/np.linalg.norm(d))))
print("check (|out|^2-|in|^2)/2",(np.linalg.norm(hout)**2-np.linalg.norm(hin)**2)/2,"VJ.dv",np.dot(VJ,d))
# angle between vin helio and vout helio
print("turn of helio velocity", np.degrees(np.arccos(np.dot(hin,hout)/np.linalg.norm(hin)/np.linalg.norm(hout))))
print("angles VJ-vin",np.degrees(np.arccos(np.dot(VJ,vin)/np.linalg.norm(VJ)/vinf)),"VJ-vout",np.degrees(np.arccos(np.dot(VJ,vout)/np.linalg.norm(VJ)/vinf)))
