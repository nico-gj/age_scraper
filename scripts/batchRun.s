#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=100
#SBATCH --time=24:00:00
#SBATCH --mem=50GB
#SBATCH --job-name=scraper
#SBATCH --mail-type=END
#SBATCH --mail-user=nj995@nyu.edu
#SBATCH --output=slurm_%j.out

module purge
module load python3/intel/3.6.3
python scraper.py
