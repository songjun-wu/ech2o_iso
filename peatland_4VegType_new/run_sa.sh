#!/bin/sh

cd ../cali_$1

# SA sampling
python3 Multi_ECH2O.py  --mode sensi_morris  --MSinit 1 --MSspace radial --NumTraj 1 --file def_50m_sa.py --outdir outputs.1  --Resol 50  --ncpu 1

# SA runs
python3 Multi_ECH2O.py  --mode sensi_morris --MSinit 0 --MSspace radial --NumTraj 1 --file def_50m_sa.py --outdir outputs.1 --ncpu 1 --Resol 50  --exe ech2o_iso --cfg config_cali --isTrck 1 --nthreads 1 --trimB 366 --trimL 731