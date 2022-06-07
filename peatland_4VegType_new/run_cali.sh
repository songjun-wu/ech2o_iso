#!/bin/sh


cd ../cali_$1

# calibration sampling
python3 Multi_ECH2O.py  --mode calib_sampling  --file def_50m_cali.py --outdir outputs.1 --sampling LHS   --Resol 50  --ncpu 1


# calibration runs
python3 Multi_ECH2O.py  --mode calib_runs --file def_50m_cali.py --outdir outputs.1 --ncpu 1 --Resol 50  --exe ech2o_iso --cfg config_cali --isTrck 1 --nthreads 1 --trimB 366 --trimL 731
