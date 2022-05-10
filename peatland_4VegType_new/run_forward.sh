#!/bin/sh

cd ../cali_$1

# forward runs
python3 Multi_ECH2O.py  --mode forward_runs --nEns 5 --inEns 0 --FWD_It 0 --file def_50m_forward.py --outdir outputs.1 --ncpu 1 --Resol 50  --exe ech2o_iso --cfg config_forward --isTrck 1 --nthreads 1  --trimB 366 --trimL 731
