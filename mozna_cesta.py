
zacatecni_bod = (15, 15)
koncovy_bod = (50, 50)
# nase_usecka = n_u
n_u = (zacatecni_bod[0], zacatecni_bod[1], koncovy_bod[0], koncovy_bod[1])
# polygon_usecka
p_u = (20, 50, 45, 20)

# pod class?
def najdi_prusecik(n_u, p_u):
    x_help1 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) * n_u[0] + (n_u[2] - n_u[0]) * (p_u[2] - p_u[0]) * (p_u[1] - n_u[1]) - (p_u[3] - p_u[1]) * (n_u[2] - n_u[0]) * p_u[0]
    x_help2 = (n_u[3] - n_u[1]) * (p_u[2] - p_u[0]) - (n_u[2] - n_u[0]) * (p_u[3] - p_u[1])
    x = x_help1 / x_help2
    y_help1 = x * (n_u[3] - n_u[1]) + n_u[1] * (n_u[2] - n_u[0]) - n_u[0] * (n_u[3] - n_u[1])
    y_help2 = (n_u[2] - n_u[0])
    y = y_help1 / y_help2
    print(x, y)
    if n_u[0] <= x <= n_u[2] and p_u[0] <= x <= p_u[2] and n_u[1] <= y <= n_u[3] and p_u[1] <= y <= p_u[3]:
    return x, y
najdi_prusecik(n_u, p_u)
