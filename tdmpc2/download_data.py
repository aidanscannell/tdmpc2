#!/usr/bin/env python3
from huggingface_hub import hf_hub_download


DATASET = {"mt30": 4, "mt80": 20}

for name in DATASET.keys():
    for chunk in range(DATASET[name]):
        filename = f"{name}/chunk_{chunk}.pt"
        print(f"Downloading {filename}")
        hf_hub_download(
            repo_id="nicklashansen/tdmpc2", filename=filename, repo_type="dataset"
        )
