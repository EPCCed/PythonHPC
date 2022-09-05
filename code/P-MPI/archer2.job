#!/bin/bash

# Slurm job options (name, compute nodes, job time)
#SBATCH --job-name=traffic
#SBATCH --time=00:05:00
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --nodes=1
#SBATCH --tasks-per-node=128
#SBATCH --cpus-per-task=1
#SBATCH --partition=standard
#SBATCH --qos=reservation
#SBATCH --reservation=ta083_797464

module load cray-python

# Launch the parallel job on the requested resources

srun --unbuffered --distribution=block:block --hint=nomultithread \
     python traffic.py
