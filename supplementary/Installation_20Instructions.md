Dear participant,

On 19–21 October 2026 we will have the "**Bioimaging data analysis: from zero to machine learning hero**", the course you have registered for.

## Program

The course runs over three days, Monday 19 to Wednesday 21 October from 09h00 – 17h00. Refreshments and lunch will be provided. More information can be found on the [training webpage.](https://training.vib.be/all-trainings/bioimaging-data-analysis-zero-machine-learning-hero)

Across the three days you will work with QuPath, Ilastik and napari, and finish with a session on your own data.

## Get ready for the course

Prior to the course, please set up your laptop using the steps below.

| **\#** | **What** | **Roughly how long** |
|----|----|----|
| 1 | Install QuPath and ilastik | 15 minutes |
| 2 | Create a Google account and log in to BAND | 10 minutes |
| 3 | Install the Python environment for napari | 30–45 minutes |
| 4 | Create a free Hugging Face account | 5 minutes |
| 5 | Download the dataset folder | 10 minutes (on a good connection) |
| 6 | Tell us about your data | 20 minutes |
| 7 | Read the Python primer | 20 minutes |

## 1. Install QuPath and ilastik

Both are single installers with everything bundled.

| **Software** | **Download link** |
|---|---|
| QuPath | [qupath.github.io](https://qupath.github.io/) |
| ilastik | [ilastik.org/download](https://www.ilastik.org/download) |

Install the latest version for your operating system.

## 2. A Google account, and BAND

The deep learning session on Wednesday runs on **BAND**, a virtual desktop you use through your browser. There is nothing to install, but **BAND signs you in with a Google account**, so you need one.

1.  Create or find a Gmail account you can use.

2.  Log in to **both** of these once before the course:

    - [band.vm.fedcloud.eu](https://band.vm.fedcloud.eu) (CESNET)

    - [bandv1.denbi.uni-tuebingen.de](https://bandv1.denbi.uni-tuebingen.de) (Tübingen)

3.  Confirm a desktop actually launches for you.

[Usage documentation (need permission, just ask for it)](https://docs.google.com/document/d/1xh9c2tQw6f9_wS4VX6hFbbY7YLBd5FozTfiMV9HweO0/edit?usp=sharing)

## 3. The Python environment for napari

### Install Miniforge

- Download and run the installer for your system from [conda-forge.org/download](https://conda-forge.org/download/). Accept the defaults.

### Build the environment

- Download the environment file environment.yml [here](https://drive.google.com/file/d/1SGLsZ-zDuS4dn8yMuYwCzsMe5jmhmb1n/view?usp=drive_link) and the python script check_install.py [here](https://drive.google.com/file/d/1WoRvURSQ3vQjfg9AAQoA6sr9oJpgG_I_/view?usp=drive_link).

- Open a terminal — Miniforge Prompt on Windows, which you find by searching the Start menu, or Terminal on macOS. It is a plain window with text in it. Copy in the lines below one at a time, waiting for each to finish before starting the next.

- Tip: do not type the file paths. Type each line up to the space at the end, then drag the file - environment.yml for the first line, check_install.py for the last - from File Explorer or Finder straight into the terminal window. The full path appears by itself. Two things to watch on Windows: make sure there really is a space before the path, and if your user name or folder contains a space, put quote marks around the whole path after you drop it.

```bash
conda env create -f path/to/environment.yml
conda activate race-2026
python path/to/check_install.py
```

The check prints a list of what it found. You do not need to understand it - just look for two things. First, no line says NOT WORKING. Second, a napari window opens, and its Plugins menu lists cellpose and napari-segment-blobs-and-things-with-membranes. You do not need to click them.

## 4. A Hugging Face account

Sign up at [huggingface.co/join](https://huggingface.co/join).

## 5. The test data

Everything you need to download is in [Datasets](https://drive.google.com/drive/folders/16tz1rfQInvQDE1hxa9OsjHVkTK13aoxB?usp=drive_link). Download the whole thing. It holds the images for every session.

## 6. Tell us about your data

Wednesday afternoon is a bring-your-own-data session.

Download the [**Discuss your data template.pptx**](https://docs.google.com/presentation/d/17mQ8UluO_t8pJ7WBxJ-B0mzWLOdNCF21/edit?usp=drive_link&ouid=101701290708489608971&rtpof=true&sd=true), fill in the slide about your own work then save it into the [**Discuss Your Data Complete Templates Folder**](https://drive.google.com/drive/folders/1-6-wWR7gEBtPnvA0XTC36m1nc88OCf-q?usp=drive_link). Please make sure you have some of your data in original format on your laptop to work on.

## 7. Read the Python primer

Also in the folder: [**A primer for Python for bioimage analysis**.](https://docs.google.com/document/d/1SgbMhB1K6NmGuukmWr37yCNpMzAx_vrD/edit?usp=drive_link&ouid=101701290708489608971&rtpof=true&sd=true)

It is not a course and there is nothing to memorise. It exists so that the vocabulary on the slides — array, layer, label image — is not brand new when you meet it.

We look forward to seeing you there!
