# **!!! THIS IS AN ALPHA VERSION OF GRANDQC REPOSITORIUM !!!**


<div align="center">
  <img src="Figures/logo.png" width="600"/>
  <div>&nbsp;</div>

[![badge](https://img.shields.io/badge/Team-Tolkach-blue)](https://tolklab.de/team)
[![paper](https://img.shields.io/badge/Paper-revision-red)](...)
[![version](https://img.shields.io/badge/Version-1.0.0-green)](...)

</div>

<div align="center">
    <img src="Figures/merge1.gif" height="200" width="500"/>
    <img src="Figures/merge2.gif" height="200" width="500"/>
</div>

## Introduction

GrandQC is an open source artifacts segmentation toolbox based on PyTorch.

The main branch works with **PyTorch 2+**. 

The System is **Ubuntu 22.04**.

<details open>
<summary>Major features</summary>

- **GrandQC Design**

  GrandQC is composed of two components: tissue segmentation and artifact segmentation. Tissue segmentation serves as the foundation for artifact segmentation, offering a more precise tissue target for detecting artifacts

- **Comprehensive Artifact Segmentation**

  GrandQC offers advanced detection of all common artifacts on segmented whole slide images (WSI), including tissue folding, pen marks, bubbles, edges, black spots, foreign objects, and out-of-focus areas. This level of coverage surpasses that of any existing open-source quality control tools.

- **High efficiency**

  For tissue segmentation, GrandQC processes a whole slide image (WSI) in an average of 0.4 seconds. Artifact segmentation takes between 27 and 45 seconds per WSI, depending on the model and magnification level.

- **Models with Different Magnifications**

  To balance efficiency and segmentation quality, GrandQC offers three models trained at different magnifications: **5x, 7x, and 10x**. Higher magnifications result in more accurate artifact segmentation but require longer processing times.

- **State of the art**

  We performed an extensive comparison with existing open-source tools, demonstrating that GrandQC significantly outperforms them across multiple metrics.

- **Building a Benchmark**
  
  We analyzed whole slide images (WSI) from various institutions and hospitals across different countries to develop a comprehensive quality benchmark. This benchmark enables each hospital and institution to evaluate their tissue slide preparation processes and make targeted improvements.

- **Scanner Selection Assistant**
  
  GrandQC allows for direct comparison of different scanners by analyzing the same batch of tissue slides. This helps in identifying the strengths and weaknesses of each scanner, particularly in relation to out-of-focus issues.

</details>

## Installation

### Install Dependencies
> conda create -n grandqc python==3.10 -y && conda activate grandqc
> 
> git clone xxx && cd GrandQC
> 
> pip install -r requirement.txt

### Install Openslide
> conda install -c conda-forge openslide openslide-python

## How to use different versions (5x ,7x, 10x)

The default version is 7x (Checkpoint: v35_E14.pth)

To use 5x and 10x checkpoints, the `main.py` script should be modified.

For 5x, use:

```commandline
MODEL_QC_NAME = 'v33_E40.pth'

MPP_MODEL_1 = 2
```
For 10x, use:

```commandline
MODEL_QC_NAME = 'v36_E21.pth'
MPP_MODEL_1 = 1
```


### For WSIs with the form of `.svs` (Leica), `.ndpi` (Hamamatsu), `.tiff` (Philips)

Fot this case, you need to use the scripts in `01_WSI_inference_OPENSLIDE_QC`:

```commandline
cd 01_WSI_inference_OPENSLIDE_QC
```

- Tissue Segmentation

Before running the Tissue-Segmentation script, you need to define the slides path **SLIDE_FOLDER** and **OUTPUT_DIR** in `run_tis.sh` first and then run:
```commandline
sh run_tis.sh
```

- Artifacts Segmentation

Similar to the Tissue Segmentation, before running the Artifacts-Segmentation script, you need to define the slides path **SLIDE_FOLDER** and **OUTPUT_DIR** in `run_art.sh` first and then run:

```commandline
sh run_art.sh
```

### For WSIs with the form of `ome.tiff`

Fot this case, you need to use the scripts in `03_WSI_inference_OME_TIFF`:

```commandline
cd 03_WSI_inference_OME_TIFF
```

abd then same as the usage above.

## Citation

If you use GrandQC or benchmark in your research, please cite this project.

```
comming soon
```

## License

This project is released under the [Apache 2.0 license](LICENSE).
