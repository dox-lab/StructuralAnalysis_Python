import numpy as np
import pandas as pd

# Lectura de datos
file_path = "data\ANÁLISIS DE ESTRUCTURAS _ INPUT.xlsx"

nBarras = int(pd.read_excel(file_path, sheet_name='BARRAS', usecols='V', nrows=1).values[0][0])  # Número de barras
nNudos = int(pd.read_excel(file_path, sheet_name='NUDOS', usecols='J', nrows=1).values[0][0] / 3)  # Número de nudos
nGDL = nNudos * 3  # Número de GDL

Xi = pd.read_excel(file_path, sheet_name='NUDOS', usecols='B').values.flatten()[:nNudos]  # Coordenadas X
Yi = pd.read_excel(file_path, sheet_name='NUDOS', usecols='C').values.flatten()[:nNudos]  # Coordenadas Y
GDLR = pd.read_excel(file_path, sheet_name='RESTRIC', usecols='A').values.flatten()  # GDL Restringidos
nGDLR = int(pd.read_excel(file_path, sheet_name='RESTRIC', usecols='B', nrows=2).values[0][0])  # Número restricciones
GDLx = pd.read_excel(file_path, sheet_name='NUDOS', usecols='D').values.flatten()
GDLy = pd.read_excel(file_path, sheet_name='NUDOS', usecols='E').values.flatten()
GDLm = pd.read_excel(file_path, sheet_name='NUDOS', usecols='F').values.flatten()

CargaX = pd.read_excel(file_path, sheet_name='NUDOS', usecols='G').values.flatten()[:nNudos]  # Carga X
CargaY = pd.read_excel(file_path, sheet_name='NUDOS', usecols='H').values.flatten()[:nNudos]  # Carga Y
CargaM = pd.read_excel(file_path, sheet_name='NUDOS', usecols='I').values.flatten()[:nNudos]  # Carga M
Carga = np.column_stack([CargaX, CargaY, CargaM])
W = pd.read_excel(file_path, sheet_name='BARRAS', usecols='U').values.flatten()[:nBarras]

Elem = pd.read_excel(file_path, sheet_name='BARRAS', usecols='A').values.flatten()[:nBarras]  # Elementos
A = pd.read_excel(file_path, sheet_name='BARRAS', usecols='B').values.flatten()[:nBarras]  # Área
I = pd.read_excel(file_path, sheet_name='BARRAS', usecols='C').values.flatten()[:nBarras]  # Inercia
E = pd.read_excel(file_path, sheet_name='BARRAS', usecols='D').values.flatten()[:nBarras]  # Módulo de Young
N_i = pd.read_excel(file_path, sheet_name='BARRAS', usecols='E').values.flatten()[:nBarras]  # Nudo i
N_j = pd.read_excel(file_path, sheet_name='BARRAS', usecols='F').values.flatten()[:nBarras]  # Nudo j
L = pd.read_excel(file_path, sheet_name='BARRAS', usecols='Q').values.flatten()[:nBarras]  # Longitud
ANG = pd.read_excel(file_path, sheet_name='BARRAS', usecols='R').values.flatten()[:nBarras]  # Ángulo

gdlx1 = pd.read_excel(file_path, sheet_name='BARRAS', usecols='K').values.flatten()[:nBarras]
gdly1 = pd.read_excel(file_path, sheet_name='BARRAS', usecols='L').values.flatten()[:nBarras]
gdlm1 = pd.read_excel(file_path, sheet_name='BARRAS', usecols='M').values.flatten()[:nBarras]

gdlx2 = pd.read_excel(file_path, sheet_name='BARRAS', usecols='N').values.flatten()[:nBarras]
gdly2 = pd.read_excel(file_path, sheet_name='BARRAS', usecols='O').values.flatten()[:nBarras]
gdlm2 = pd.read_excel(file_path, sheet_name='BARRAS', usecols='P').values.flatten()[:nBarras]
gdl = np.column_stack([gdlx1, gdly1, gdlm1, gdlx2, gdly2, gdlm2])

# Creación de vector de GDL
GDL = np.arange(1, nGDL + 1).reshape(-1, 1)

# Número de GDL libres
nGDLL = nGDL - nGDLR

Q = np.zeros((nGDL, 1))
R = np.zeros((nGDL, 1))
K = np.zeros((nGDL, nGDL))
KLL = np.zeros((nGDLL, nGDLL))

EA = E * A
EI = E * I
Atrans = [None] * nBarras
k = [None] * nBarras
r = [None] * nBarras

# Cálculo de propiedades de barra
for i in range(nBarras):
    A_0 = np.array([
        [np.cos(ANG[i]), np.sin(ANG[i]), 0, 0, 0, 0],
        [-np.sin(ANG[i]), np.cos(ANG[i]), 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, np.cos(ANG[i]), np.sin(ANG[i]), 0],
        [0, 0, 0, -np.sin(ANG[i]), np.cos(ANG[i]), 0],
        [0, 0, 0, 0, 0, 1]
    ])
    Atrans[i] = A_0
    k_0 = np.array([
        [EA[i] / L[i], 0, 0, -EA[i] / L[i], 0, 0],
        [0, 12 * EI[i] / (L[i] ** 3), 6 * EI[i] / (L[i] ** 2), 0, -12 * EI[i] / (L[i] ** 3), 6 * EI[i] / (L[i] ** 2)],
        [0, 6 * EI[i] / (L[i] ** 2), 4 * EI[i] / L[i], 0, -6 * EI[i] / (L[i] ** 2), 2 * EI[i] / L[i]],
        [-EA[i] / L[i], 0, 0, EA[i] / L[i], 0, 0],
        [0, -12 * EI[i] / (L[i] ** 3), -6 * EI[i] / (L[i] ** 2), 0, 12 * EI[i] / (L[i] ** 3), -6 * EI[i] / (L[i] ** 2)],
        [0, 6 * EI[i] / (L[i] ** 2), 2 * EI[i] / L[i], 0, -6 * EI[i] / (L[i] ** 2), 4 * EI[i] / L[i]]
    ])
    k[i] = k_0
    r_0 = np.array([0, W[i] * L[i] / 2, W[i] * (L[i] ** 2) / 12, 0, W[i] * L[i] / 2, -W[i] * (L[i] ** 2) / 12])
    r[i] = r_0
# Ensamblaje de la matriz K


for rr in range(nBarras):
    a_00 = Atrans[rr]
    k_00 = k[rr]
    kBarra = a_00.T @ k_00 @ a_00
    for i in range(6):
        m = int(gdl[rr, i] - 1)  # Convertimos a índice
        for j in range(6):
            n = int(gdl[rr, j] - 1)  # Convertimos a índice
            K[m, n] += kBarra[i, j]

# Ensamblaje de la matriz R
for m in range(nBarras):
    a_01 = Atrans[m]
    r_01 = r[m]
    RBarra = a_01.T @ r_01
    for j in range(6):
        n = int(gdl[m, j] - 1)  # Convertimos a índice
        R[n, 0] += RBarra[j]

# Ensamblaje de la matriz Q
Q = Carga.reshape(-1, 1)

# Cálculo de vector de GDL libres
GDLL = np.zeros((nGDLL, 1))
nn = 1
ll = 0
for i in range(nGDL):
    a = GDL[i, 0]
    for n in range(nGDLR):
        b = GDLR[n]
        if a != b:
            ll += 1
    if ll == nGDLR:
        GDLL[nn - 1, 0] = a
        nn += 1
    ll = 0

# KLL
for i in range(nGDLL):
    a = int(GDLL[i, 0])
    for ii in range(nGDLL):
        b = int(GDLL[ii, 0])
        KLL[i, ii] = K[a-1, b-1]

# Cálculo de Q libre y R libre
QL = np.zeros((nGDLL, 1))
for i in range(nGDLL):
    a = int(GDLL[i, 0])
    QL[i, 0] = Q[a-1, 0]

RL = np.zeros((nGDLL, 1))
for i in range(nGDLL):
    a = int(GDLL[i, 0])
    RL[i, 0] = R[a-1, 0]

# Desplazamiento libres
Vector_Cargas_Libres = QL - RL
DL = np.linalg.inv(KLL) @ Vector_Cargas_Libres

# Desplazamiento general
D = np.zeros((nGDL, 1))
for a in range(nGDL):
    for b in range(nGDLL):
        if GDL[a, 0] == GDLL[b, 0]:
            D[a, 0] = DL[b, 0]

# Impresión de Resultados
print('\n')
print('Vector de grados de libertad libres GDLL')
print(GDLL)

print('\n')
print('Vector de grados de libertad restringidos GDLR>')
print(GDLR)

print('\n')
print('Matriz de Rigidez General')
print(K)

print('\n')
print('Matriz de Rigidez Libre')
print(KLL)

print('\n')
print('Vector de cargas libres')
print(Vector_Cargas_Libres)

print('\n')
print('Vector de desplazamiento libre')
print(DL)

print('\n')
print('Vector de desplazamiento general')
print(D)

# Impresión de Datos de Barra

ok = False
print('\n')
print('           Visualizador de propiedades de Barra\n')
while not ok:
    n_barra = int(input('Número de barra del que desea ver Matrices = '))-1
    D_Barra = np.zeros((6, 1))
    for b in range(6):
        index = gdl[n_barra, b] 
        D_Barra[b] = D[int(index)-1]
    
    a_barra = Atrans[n_barra]
    r_barra = r[n_barra].reshape(6, 1)
    k_barra = k[n_barra]

    d_local_barra = a_barra @ D_Barra
    q_local_barra = k_barra @ d_local_barra + r_barra

    print('\n')
    print('Matriz de Transformacion')
    print(a_barra)

    print('\n')
    print('Matriz de Reacciones de la Barra')
    print(r_barra)

    print('\n')
    print('Matriz de Rigidez de la Barra')
    print(k_barra)

    print('\n')
    print('Matriz de Desplazamientos de la Barra')
    print(d_local_barra)

    print('\n')
    print('Matriz de Cargas de la Barra')
    print(q_local_barra)

    # Pregunta si se quiere repetir el proceso
    datok = input('Parar aqui?? (s/n): ')
    ok = (datok == 's')
    print('\n')

print('\n')
print('PROGRAMA FINALIZADO')
print('\n')
