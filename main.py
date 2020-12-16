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
    Miguel Rodrigues up201906042
    ---
"""

import matplotlib.pyplot as plt
import math
from Methods.RootFinding import bissection as bissec
from Methods.RootFinding import falsePosition as falsePos
from Methods.RootFinding import newton
from Methods.RootFinding import picardPeano as picPeano

#Ka = TEMOS DE CALCULAR COM A EQUAÇÃO DO PROF #(constante cinética de absorção) 
Ket = 0.17325 #/h constante cinética de eliminação total
Vap = 3150 # em ml Volume aparente de plasma
tmax = 4 #h
DurTrat = 5 #dia
DosDia = 100 #mg Dose Diária

def f(Ka):
    return Ka*math.exp(-Ka*tmax) - Ket*math.exp(-Ket*tmax)
def derf(Ka):
    return Ket**2*tmax*math.exp(-Ket*tmax) - Ka**2*tmax*math.exp(-Ka*tmax)

def g(Ka):
    return (Ket*math.exp(-Ket*tmax))/(math.exp(-Ka*tmax))
def derg(Ka):
    return 0.346551001817167*math.exp(4*Ka)
    
print("###### Bissection ######")
Ka1 = bissec.bissection_abs_stop(0.10, 0.25, f)
Ka2 = bissec.bissection_abs_stop(0.25, 0.40, f)
Ka = (Ka1 + Ka2)/2
print("Ka1: ", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka)


print("###### False Position ######")
Ka1 = falsePos.false_position_abs_stop(0.10, 0.25, f)
#Ka2 = falsePos.false_position_null_at_root(0.20, 0.60, f)
Ka = ( Ka1 + Ka2 )/2
print("Ka1: ", Ka1, "\nKa2: NOT WORKING", Ka2, "\nKa: ", Ka)

print("###### Newton ######")
#Ka1 = newton.newton_one_var(0.13, 20,f, derf)
Ka2 = newton.newton_one_var(0.4, 30,f, derf)
Ka = ( Ka1 + Ka2 )/2
print("Ka1: NOT WORKING", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka)

print("###### PicardPeano ######")
#Ka1 = picPeano.picard_peano(0.25, 20, f, derf)
#Ka2 = picPeano.picard_peano(0.4, 30,f, derf)
#Ka = ( Ka1 + Ka2 )/2
print("Ka1: ", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka)


def D(t):
    return (-t % (24*60))*(100/(24*60))

x = [x for x in range(0, 24*60*5)]
y = [D(x) for x in x]

plt.plot(x, y)
plt.show()

#CONFIRMAÇÃO GRÁFICA
# =============================================================================
# x = [x/100 for x in range(10,50)]
# y = [f(x) for x in x]
# plt.plot(x,y)
# plt.show()
# =============================================================================

from Methods.Differentials import *

# Modelo Monocompartimental
def dCp(t, Cp):
    return (D(t)-Ket*Cp)/Vap

# Modelo Bicompartimental
def dMi(t, Mi, Mp):
    return D(t) - (Ka/60)*Mi
def dMp(t, Mi, Mp):
    return (Ka/60)*Mi - (Ket/60)*Mp

# print("###### EULER ######")
# euler_system(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1, True)
# print(euler_qc(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1))
# print(euler_system_error(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1))

print("###### RK2 ######")
rk2_system(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1, True)
print(rk2_qc(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1))
print(rk2_system_error(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1))

# print("###### RK4 ######")
# rk4_system(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1, True)
# print(rk4_qc(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1))
# print(rk4_system_error(dMi, dMp, 0, 100, 0, 24 * 60 * DurTrat, 1))
