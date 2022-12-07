import json
import importlib.resources as pkg_resources
import uebung_6_helpers
import math

ac = json.load(pkg_resources.open_binary(uebung_6_helpers, 'ac_data.json'))

mu = 2 * ac['m'] / (ac['rho'] * ac['S'] * ac['l_mu'])

#-----------------------    Variation SP-Lage   -------------------------------#
##----------------------    Anstellwinkelschwingung     -----------------------#
###---------------------    Dämpfung    ---------------------------------------#
A_sigma_alpha = -(ac["V"]/(2 * mu * ac["l_mu"]))*(ac["C_A_alpha"] +
                                                  pow((ac["l_mu"]/ac["i_y"]), 2) * ac['C_AHalphaH'] *
                                                  ac['S_h_durch_S'] *
                                                  pow(ac['r_h_stern_durch_l_mu'], 2) *
                                                  (math.sqrt(ac["q_h_durch_q"]) + ac["q_h_durch_q"] * ac['dalpha_w_nach_dalpha']))

B_sigma_alpha = (ac['V']/(2 * mu * ac['l_mu'])) * \
    ac['C_AHalphaH'] * \
    pow((ac['l_mu']/ac['i_y']), 2) * \
    ac['S_h_durch_S'] * \
    ac['r_h_stern_durch_l_mu'] * \
    (2 * math.sqrt(ac['q_h_durch_q']) +
     ac['q_h_durch_q'] * ac['dalpha_w_nach_dalpha'])

D_sigma_alpha = -(ac['V']/(2 * mu * ac['l_mu'])) * \
    pow((ac['l_mu']/ac['i_y']), 2) * \
    ac['C_AHalphaH'] * \
    math.sqrt(ac['q_h_durch_q']) * \
    ac['S_h_durch_S']

###---------------------    Eigenfrequenz   -----------------------------------#
A_omega_alpha = -pow(ac['V']/ac['i_y'], 2) * ac['C_A_alpha']/mu * \
    ac['C_AHalphaH'] * ac['S_h_durch_S'] * ac['r_h_stern_durch_l_mu'] * (
        1/mu * math.sqrt(ac['q_h_durch_q']) * ac['r_h_stern_durch_l_mu'] -
        1/ac['C_A_alpha'] * (1 - ac['dalpha_w_nach_dalpha']) *
        ac['q_h_durch_q']
)

B_omega_alpha = -pow(ac['V']/ac['i_y'], 2) * ac['C_A_alpha']/mu * (
    1 + 2 * (ac['C_AHalphaH'] / mu) *
    ac['q_h_durch_q'] * ac['S_h_durch_S'] *
    ac['r_h_stern_durch_l_mu']
)

D_omega_alpha = pow(ac['V']/ac['i_y'], 2) * ac['C_A_alpha'] * ac['C_AHalphaH'] * \
    math.sqrt(ac['q_h_durch_q']) * ac['S_h_durch_S'] / (mu*mu)

##----------------------    Phygoide     --------------------------------------#
