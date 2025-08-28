#!/bin/bash

#SBATCH --job-name=training_example
#SBATCH --account=p71550
##SBATCH --account=p70824 # training account, please uncomment for training
#SBATCH --nodes=2                    # Number of nodes
#SBATCH --ntasks-per-node=1          # Number of tasks per node
#SBATCH --cpus-per-task=256          # Number of CPU cores per task (including hyperthreading if needed)
#SBATCH --partition=zen3_0512_a100x2
#SBATCH --qos=admin
##SBATCH --qos=zen3_0512_a100x2 # qos for training
#SBATCH --gres=gpu:2                 # Number of GPUs per node
#SBATCH --output=../../output/%x-%j.out  # Output file
##SBATCH --reservation=

######################
### Set Environment ###
######################
module load miniconda3
eval "$(conda shell.bash hook)"
source /opt/sw/jupyterhub/envs/conda/vsc5/jupyterhub-huggingface-v2/modules  # Activate the conda environment

######################
#### Set Network #####
######################
# Get the IP address of the master node (head node)
nodes=$(scontrol show hostnames "$SLURM_JOB_NODELIST")
nodes_array=($nodes)
node_0=${nodes_array[0]}

NUM_PROCESSES=$(( SLURM_NNODES * SLURM_GPUS_ON_NODE ))

export MASTER_ADDR=$node_0
export MASTER_PORT=29500

######################
#### Prepare Launch ###
######################
# Configure Accelerate launch command

export LAUNCHER="accelerate launch \
    --config_file "../config/accelerate_config.yaml" \
    --machine_rank \$SLURM_PROCID \
    --main_process_ip $MASTER_ADDR \
    --main_process_port $MASTER_PORT \
    --num_processes $NUM_PROCESSES \
    --num_machines $SLURM_NNODES \
    "
export PROGRAM="../../examples/deepspeed_example.py"

START=$(date +%s.%N)
echo "START TIME: $(date)"

export SRUN_ARGS="--cpus-per-task $SLURM_CPUS_PER_TASK --jobid $SLURM_JOBID"
export OMP_NUM_THREADS=256
export CMD="$LAUNCHER $PROGRAM"

# Execute the command with srun to run on multiple nodes
srun $SRUN_ARGS ../start_train.sh "$CMD"

echo "END TIME: $(date)"
END=$(date +%s.%N)
RUNTIME=$(echo "$END - $START" | bc -l)
echo "Runtime: $RUNTIME"
