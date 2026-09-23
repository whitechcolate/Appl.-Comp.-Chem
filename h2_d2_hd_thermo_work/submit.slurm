#!/bin/bash
#SBATCH --job-name=h2-d2-hd-dg
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:30:00
#SBATCH --output=slurm-%j.out

set -euo pipefail
MAESTRO_ALLOW_RAW=1 maestro-python h2_d2_hd_delta_g.py
