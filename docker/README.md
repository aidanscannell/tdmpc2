## Install for AMD GPU (e.g. LUMI)
Install with:
``` sh
TDMPC2_CONTAINER_DIR=/scratch/project_462000462/tdmpc2/container
mkdir  $TDMPC2_CONTAINER_DIR
module load LUMI
module load lumi-container-wrapper
conda-containerize new --mamba --prefix $TDMPC2_CONTAINER_DIR environment.yml
conda-containerize update $TDMPC2_CONTAINER_DIR --post-install post-install-amd.txt
```

To run experiments add container to path with:
```sh
export PATH="/scratch/project_462000462/tdmpc2/container/bin:$PATH"
```
