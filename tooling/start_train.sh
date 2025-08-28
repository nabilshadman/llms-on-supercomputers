#!/usr/bin/env bash


echo "# hello from $SLURM_PROCID"
#ldd /home/fs71550/simeon/nccl-rdma-sharp-plugins/lib/libnccl-net.so
#ldd /home/fs71550/simeon/hpc-x/hpcx-v2.14-gcc-MLNX_OFED_LINUX-5-redhat8-cuda11-gdrcopy2-nccl2.16-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so

echo "# cuda devices: $CUDA_VISIBLE_DEVICES"

echo "# computed available resources:"

HWTHREADS=$( lscpu | grep "^Thread(s) per core:" | sed "s/.*:\s*//g" )
NUMA_CPU_BIND=$( numactl -s | grep "physcpubind:" | sed "s/.*:\s*//g" )
LOGICAL_CPUS=$( echo "$NUMA_CPU_BIND"| wc -w )
PHYSICAL_CPUS=$( echo "$LOGICAL_CPUS/$HWTHREADS" | bc )

echo "physical cpu count: $PHYSICAL_CPUS"
echo "logical cpu count: $LOGICAL_CPUS"

echo "# mem limits via python"
python3 ../mem_limit.py

echo "# starting actual command: \"$@\""
#bash -c "$@"
eval "$@"