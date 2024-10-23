import neutralocean

def seos(S, T, Z, rn_a0 = 1.655e-1, rn_b0 = 7.655e-1,
               rn_nu = 2.4341e-3, rn_lambda1 = 5.9520e-2, rn_lambda2 = 7.4914e-4,
               rn_mu1 = 1.4970e-4, rn_mu2 = 1.1090e-5 ):

    rho_0 = 1026.
    T0 = 10.
    S0 = 35.

    dT = T - T0
    dS = S - S0

    rho  =  rho_0  \
           - rn_a0 * ( 1 + 0.5 * rn_lambda1 * dT ) * dT  \
           + rn_b0 * ( 1 - 0.5 * rn_lambda2 * dS ) * dS  \
           - rn_nu * dT * dS \
           - (rn_a0 * rn_mu1 * dT + rn_b0 * rn_mu2 * dS) * Z

    return rho

rho = seos(35.1, 0, 1000)

eos = lambda S,T,Z : seos(S,T,Z, rn_nu = 0., rn_lambda1=0., rn_lambda2=0., rn_mu1 =0., rn_mu2 = 0.)

S = 35.1
T = 11
Z = 1000

print(seos(S,T,Z))
print(eos(S,T,Z))





from neutralocean.eos.tools import make_eos

make_eos(eos)