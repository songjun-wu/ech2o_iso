#!/bin/sh


#SBATCH --job-name="cali"
#SBATCH --qos=medium
#SBATCH --account=vewa
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --partition=computehm

# SA sampling
python3 Multi_ECH2O.py  --mode sensi_morris  --MSinit 1 --MSspace radial --NumTraj 5 --file def_50m_sa.py --outdir outputs.1  --Resol 50  --ncpu 1

# SA runs
python3 Multi_ECH2O.py  --mode sensi_morris --MSinit 0 --MSspace radial --NumTraj 5 --file def_50m_sa.py --outdir outputs.1 --ncpu 1 --Resol 50  --exe ech2o_iso --cfg config_sa --isTrck 1 --nthreads 4


# calibration sampling
#python3 Multi_ECH2O.py  --mode calib_sampling  --file def_50m_cali.py --outdir outputs.1 --sampling LHS   --Resol 50  --ncpu 1


# calibration runs
#python3 Multi_ECH2O.py  --mode calib_runs --file def_50m_cali.py --outdir outputs.1 --ncpu 1 --Resol 50  --exe ech2o_iso --cfg config_cali --isTrck 1 --nthreads 1



