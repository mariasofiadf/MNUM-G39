"""
Diclofenac

mi = (massa de fármaco presente no compartimento central, o índice i diferencia as vias de administração)
mp = (massa de fármaco no compartimento plasmático)
Ka = (constante cinética de absorção)
Ket  = (constante cinética de eliminação total)
Vap = (Volume aparente de plasma)
tmax = (instante onde ocorre concentração plasmática máxima)
DurTrat = (Dureção padrão do tratamento)
Ddia = (Dose diária)

Da autoria de:
    Pedro Figueiredo up201904675
    ---
    ---
"""

import matplotlib.pyplot as plt
import math
from Methods.RootFinding import bissection as bis

#Ka = TEMOS DE CALCULAR COM A EQUAÇÃO DO PROF #(constante cinética de absorção) 
Ket = 0.17325 #/h constante cinética de eliminação total
Vap = 3150 # em ml Volume aparente de plasma
tmax = 4 #h
DurTrat = 5 #dia
DosDia = 100 #mg Dose Diária

def f(Ka):
    return Ka*math.exp(-Ka*tmax) - Ket*math.exp(-Ket*tmax)
Ka1 = bis.bissection_abs_stop(0.10, 0.25, f)
Ka2 = bis.bissection_abs_stop(0.25, 0.40, f)
Ka = ( Ka1 + Ka2 )/2
print("Ka1: ", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka)

#CONFIRMAÇÃO GRÁFICA
# =============================================================================
# x = [x/100 for x in range(10,50)]
# y = [f(x) for x in x]
# plt.plot(x,y)
# plt.show()
# =============================================================================

"""
#Dose administrada como função do tempo
def D(t):
    return 100 if (t % 24 == 0) else 0

#t está em horas e t está em [0, 24*5] (pois o tratamento dura 5 dias)
Dt = [t for t in range(0,24*5)]
#D(t) está em mg
Dy = [D(t) for t in Dt]
#Display gráfico da função
plt.scatter(Dt,Dy) # ou usar plt.plot(Dt, Dy)
plt.ylabel('Dose administrada em função do tempo')
plt.show()

#Modelo Monocompartimental
def dCp(t, Cp):
    return (D(t)-Ke*Cp)/Vap

#Modelo Bicompartimental
def dMi(t, Mi):
    return D(t) - Ka*Mi


def dMp(t, Mp):
    return Ka*Mi - Ke*Mp
"""