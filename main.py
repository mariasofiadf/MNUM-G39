"""
Diclofenac

mi = (massa de fármaco presente no compartimento central, o índice i diferencia as vias de administração)
mp = (massa de fármaco no compartimento plasmático)
Ka = (constante cinética de absorção)
Ket  = (constante cinética de eliminação total)
Vap = (Volume aparente de plasma)
tmax = (instante onde ocorre concentração plasmática máxima)
DurTrat = (Duração padrão do tratamento)
Ddia = (Dose diária)

Da autoria de:
    Pedro Figueiredo up201904675
    Miguel Rodrigues up201906042
    ---
"""

import matplotlib.pyplot as plt
import math

# Ka = TEMOS DE CALCULAR COM A EQUAÇÃO DO PROF  #(constante cinética de absorção)

Ket_hr = 0.17325  # constante cinética de eliminação total por hora
Ket_min = Ket_hr / 60  # constante cinética de eliminação total por minuto

Vap = 3150  # Volume aparente de plasma em ml

tmax_hr = 4  # tempo máximo em horas
tmax_min = tmax_hr * 60  # tempo máximo em minutos

DurTrat = 6  # Duração do Tratamento em dias
DosDia = 100  # Dose diária do fármaco em mg


def f(Ka):
    return Ka * math.exp(-Ka * tmax_min) - Ket_min * math.exp(-Ket_min * tmax_min)


# Derivada Calculada no Maxima
def diff_f(Ka):
	return math.exp(-10.395 * Ka) - 10.395 * Ka * math.exp(-10.395 * Ka)


# Funções para o método iterativo de Picard Peano
def g1(Ka):
	return Ket_min * math.exp(-Ket_min * tmax_min) / math.exp(-Ka * tmax_min)
def g2(Ka):
	return -(math.log((Ket_min * math.exp(-Ket_min * tmax_min)) / Ka) / tmax_min)


# Derivadas Calculadas no Maxima
def g1_diff(Ka):
	return Ket_min * tmax_min * math.exp(Ka * tmax_min - Ket_min * tmax_min)
def g2_diff(Ka):
	return 1 / (Ka * tmax_min)


# Plot da equação do Ka
ka_axis = [x / (100 * 60) for x in range(0, 50)]
ke_axis = [f(x) for x in ka_axis]

plt.xlabel("$K_a$")
plt.title("$K_a e^{-K_a t_{max} }-K_e e^{-K_e t_{max} }$")
plt.grid()

plt.plot(ka_axis, ke_axis)
plt.show()

from Methods.RootFinding import *

print("###### Bissection ######")
Ka1 = bissection_abs_stop(0.002, 0.003, f)
Ka2 = bissection_abs_stop(0.005, 0.006, f)
Ka_avg = ((Ka1 + Ka2) / 2) * 60
print("Ka1: ", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka_avg)


# Não Conseguimos Calcular os Zeros
# print("###### False Position ######")
# Ka1 = false_position_abs_stop(0.002, 0.003, f)
# Ka2 = false_position_abs_stop(0.005, 0.006, f)
# Ka_avg = ((Ka1 + Ka2) / 2) * 60
# print("Ka1: ", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka_avg)

# Não conseguimos calcular Zeros visto que a derivada troca de sinal entre os zeros
# print("###### Newton ######")
# Ka1 = newton_one_var(0.002, 18, f, diff_f)
# Ka2 = newton_one_var(0.008, 18, f, diff_f)
# Ka_avg = ((Ka1 + Ka2) / 2) * 60
# print("Ka1:", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka_avg)


# print("###### PicardPeano ######")
# Ka1 = picard_peano(0.002, 25, g1, g1_diff)
# Ka2 = picard_peano(0.005, 25, g2, g2_diff)
# Ka_avg = ((Ka1 + Ka2) / 2) * 60
# print("Ka1: ", Ka1, "\nKa2: ", Ka2, "\nKa: ", Ka_avg)


# Função Administração
def D(tempo):
	return 100 if not tempo % 24 else 0

def D(tempo):
    if((tempo > 120)):
        return 0
    if((tempo % 24 >= 0) and (tempo % 24 <= 4)):
        return (tempo%24)*100/(12*4)
    elif((tempo % 24 > 4)):
        m = -10/24
        b = 10
        return (tempo%24)*(m)+b
    return 0

t = [x for x in range(0, 24 * DurTrat)]
y = [D(tempo) for tempo in t]

plt.xlabel("t")
plt.ylabel("D(t)")
plt.title("Função Administração $D(t)$")
plt.grid()

plt.plot(t, y)
plt.show()

from Methods.Differentials import *


# Modelo Monocompartimental


def dCp(tempo, Cp):
	return (D(tempo) - Ket_hr * Cp * Vap) / Vap


print("###### EULER ######")
step_euler = 0.125
res_euler_mono = euler(dCp, 0, 0, 24 * DurTrat, step_euler)
print("QC Euler: ", euler_quotient(dCp, 0, 0, 24 * DurTrat, step_euler))
print("Erro Euler: ", euler_error(dCp, 0, 0, 24 * DurTrat, step_euler))

t = [elem[0] for elem in res_euler_mono]
cp = [elem[1] / step_euler for elem in res_euler_mono]

plt.xlabel("t")
plt.suptitle("Balanço Mássico")
plt.title("Modelo Monocompartimental - Euler")
plt.grid()

plt.plot(t, cp, label=r"$cp(t)$")
plt.legend(loc=1)
plt.show()

print("###### RK2 ######")
step_rk2 = 0.125
res_rk2_mono = rk2(dCp, 0, 0, 24 * DurTrat, step_rk2)
print("QC RK2: ", rk2_quotient(dCp, 0, 0, 24 * DurTrat, step_rk2))
print("Erro RK2: ", rk2_error(dCp, 0, 0, 24 * DurTrat, step_rk2))

t = [elem[0] for elem in res_rk2_mono]
cp = [elem[1] / step_rk2 for elem in res_rk2_mono]

plt.xlabel("t")
plt.suptitle("Balanço Mássico")
plt.title("Modelo Monocompartimental - RK2")
plt.grid()

plt.plot(t, cp, label=r"$cp(t)$")
plt.legend(loc=1)
plt.show()

print("###### RK4 ######")
step_rk4 = 0.125
res_rk4_mono = rk4(dCp, 0, 0, 24 * DurTrat, step_rk4)
print("QC RK4: ", rk4_quotient(dCp, 0, 0, 24 * DurTrat, step_rk4))
print("Erro RK4: ", rk4_error(dCp, 0, 0, 24 * DurTrat, step_rk4))

t = [elem[0] for elem in res_rk4_mono]
cp = [elem[1] / step_rk4 for elem in res_rk4_mono]

plt.xlabel("t")
plt.suptitle("Balanço Mássico")
plt.title("Modelo Monocompartimental - RK4")
plt.grid()

plt.plot(t, cp, label=r"$cp(t)$")
plt.legend(loc=1)
plt.show()


# Modelo Bicompartimental


def dMi(tempo, Mi, Mp):
	return D(tempo) - Ka_avg * Mi


def dMp(tempo, Mi, Mp):
	return Ka_avg * Mi - Ket_hr * Mp


print("###### EULER ######")
step_euler = 0.125
res_euler = euler_system(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_euler, False)
print("QC Euler: ", euler_qc(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_euler))
print("Erro Euler: ", euler_system_error(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_euler))

t = [elem[0] for elem in res_euler]
mi = [elem[1] / step_euler for elem in res_euler]
mp = [elem[2] / step_euler for elem in res_euler]

plt.xlabel("t")
plt.suptitle("Balanço Mássico")
plt.title("Modelo Bicompartimental - Euler")
plt.grid()

plt.plot(t, mi, label=r"$mi(t)$")
plt.plot(t, mp, label=r"$mp(t)$")
plt.legend(loc=1)
plt.show()

print("###### RK2 ######")
step_rk2 = 0.125
res_rk2 = rk2_system(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_rk2, False)
print("QC RK2: ", rk2_qc(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_rk2))
print("Erro RK2: ", rk2_system_error(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_rk2))

t = [elem[0] for elem in res_euler]
mi = [elem[1] / step_rk2 for elem in res_euler]
mp = [elem[2] / step_rk2 for elem in res_euler]

plt.xlabel("t")
plt.suptitle("Balanço Mássico")
plt.title("Modelo Bicompartimental - RK2")
plt.grid()

plt.plot(t, mi, label=r"$mi(t)$")
plt.plot(t, mp, label=r"$mp(t)$")
plt.legend(loc=1)
plt.show()

print("###### RK4 ######")
step_rk4 = 0.125
res_rk4 = rk4_system(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_rk4, False)
print("QC RK4: ", rk4_qc(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_rk4))
print("Erro RK4: ", rk4_system_error(dMi, dMp, 0, 0, 0, 24 * DurTrat, step_rk4))

t = [elem[0] for elem in res_euler]
mi = [elem[1] / step_rk4 for elem in res_euler]
mp = [elem[2] / step_rk4 for elem in res_euler]

plt.xlabel("t")
plt.suptitle("Balanço Mássico")
plt.title("Modelo Bicompartimental - RK4")
plt.grid()

plt.plot(t, mi, label=r"$mi(t)$")
plt.plot(t, mp, label=r"$mp(t)$")
plt.legend(loc=1)
plt.show()
