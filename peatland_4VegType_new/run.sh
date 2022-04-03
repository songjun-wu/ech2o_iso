#!/bin/sh

export PATH="$PATH:/home/songjunwu/pcraster/bin"
export PYTHONPATH="${PYTHONPATH}:/home/songjunwu/pcraster/python"

# calibration sampling
python3 Multi_ECH2O.py  --mode calib_sampling  --file def_250m.py --outdir outputs.1 --sampling LHS   --Resol 50  --ncpu 1


# calibration runs
python3 Multi_ECH2O.py  --mode calib_runs --file def_250m.py --outdir outputs.1 --ncpu 1 --Resol 50  --exe ech2o_iso --cfg config --isTrck 0 --nthreads 1


