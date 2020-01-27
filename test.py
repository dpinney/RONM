# run each of the (.dss, .json) input pairs through ONM and other tools

import os
os.system('tar xvf other_test_data.tar')
sec_circ = open('secret_test_data/test98_circuit_secretCoop.dss').read()
print(sec_circ)