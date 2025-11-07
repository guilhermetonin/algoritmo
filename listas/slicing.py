# --- slicing ---
valores = [0, 1, 2, 3, 4, 5, 6]


# --- [início : fim] ---
# da 1 (inclusa) até a 4 (exclusa)
v1 = valores[1:4] 
print(v1) # [1, 2, 3]


# --- [início :] ---
# da posição 3 (inclusa) até o final
v2 = valores[3:] 
print(v2) # [3, 4, 5, 6]


# --- [: fim] ---
# do início até a posição 4 (exclusa)
v3 = valores[:4] 
print(v3) # [0, 1, 2, 3]


# --- [início : fim : intervalo] ---
# extrai da posição 1 até a 7 (exclusa), pulando de 3 em 3
v4 = valores[1:7:3] 
print(v4) # [1, 4]