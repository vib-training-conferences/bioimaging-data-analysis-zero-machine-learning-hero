# Python setup for bioimage analysis 

This is intended as a short orientation that might help you run and understand how we use Python for bioimage analysis.

## What Python actually is 

Python is a programming language, and also the program that runs your code. On its own it can do arithmetic and handle text, and not much that's useful to us. Everything we actually care about, like reading a proprietary microscope file format, segmenting cells, drawing a plot, comes from libraries.

### Libraries
A library is code somebody else has written and published so you don't have to. Python can’t load all available libraries when it starts, that'd be slow and it has no idea which you want. So you see at the top of a script stuff like:

```python
import numpy as np
from skimage.measure import regionprops
```

The first line says load [numpy](https://numpy.org/), and lets me call it np for short (this is a common shortening you will see across the field not just me!). The second says out of [scikit-image](https://scikit-image.org/), just get me [regionprops](https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_regionprops.html). Once you've imported something it's available for the rest of that session. If you see ModuleNotFoundError, it means the library isn't installed in the environment you're using. More about environments in the next section.

Some relevant examples of libraries are listed below:

- **numpy:** An image is a grid of numbers, and a way Python can hold these numbers is through a numpy array.

- **bioio:** Reads (a lot of!) microscope file formats.

- **scikit-image:** General image processing — filters, thresholds, measuring objects.

- **cellpose:** a deep learning algorithm (actually a few) that finds cells.

- **pandas:** Tables. Think of a spreadsheet you can write code against.

- **matplotlib:** Plots and displaying images.

- **napari**: A multi-dimensional image viewer you drive from Python, but you can also use buttons and widgets inside of napari if you are more used to software with GUIs.

### What an image looks like to Python

When you load an image into Python you get a numpy array: a grid of numbers with a shape. The shape is just the size along each axis, and you can always ask for it:

```python
img.shape
# (1, 3, 1, 1884, 1884)
```

That is one timepoint, three channels, one z-plane, and 1884 by 1884 pixels. The order matters enormously and mix ups can cause misery. Nothing stops you treating the channel axis as if it were z; the code runs, you get a picture, and the picture is wrong. If a result looks strange, printing the shape is almost always the first thing worth doing.

Selecting part of an array uses square brackets, one entry per axis:

nuclei = img\[0, 2\] \# timepoint 0, channel 2, all of z, y and x

### 

### Label images

This is the one to take away, because nearly everything in the course is a label image.

When you segment an image you do not get a picture of outlines. You get another array, the same width and height as the original, where every pixel holds a whole number saying which object it belongs to. Background is 0. The first cell is 1 everywhere it covers, the second is 2, and so on.

So counting objects is just asking for the largest number present, and pulling out a single cell is asking which pixels carry its number:

labels.max() \# 153 -\> there are 153 objects  
cell_7 = labels == 7 \# True where object 7 is, False everywhere else

### Doing the same thing to every file

Most real analysis is one recipe applied to a folder. In Python that is a loop.

```python
from pathlib import Path

for filename in Path("race-data").glob("*.czi"):
    print(filename.name)
    # read it, segment it, measure it, save the numbers
```

Everything indented under the for line happens once per file.

### Environments, and why they exist
An environment is a folder containing a copy of Python plus a specific set of libraries at specific versions. Environment and dependency problems are probably the number one source of pain when trying to use Python. You should keep each project in its own environment. The other reason is being able to reproduce things. If you publish a number, you want to be able to rebuild the exact set of library versions that produced it. Environments make that more possible; installing everything in one big pile does not.

## Where do libraries actually come from?

When you ask your environment manager to install a library, it has to download it from somewhere. PyPI (the Python Package Index) is essentially an app store for Python code. Tools like pip and uv download exclusively from here.

On the other hand, conda and mamba pull from their own separate storage repositories (the most common one is called conda-forge).

#### Environment managers you'll come across

- **conda / mamba:** the most common probably. Lots of tutorials assume it. Works fine, can be slow, and the "activate the right environment first" step is easy to forget.

- **venv + pip:** built into Python. Fine, but only handles PyPI packages and won't manage Python versions.

- **uv:** New, very fast, pip-compatible

- **pixi:** New and fast, and it handles both conda packages and PyPI packages, and it is per-project by default.

### Notebooks

A Jupyter notebook is a document made of cells. Some are code, some are text. You run a code cell and its output appears directly underneath it. That's why they suit this kind of work. You segment some cells, look at the result, change a parameter, look again. Doing that as a script means re-running everything from the top each time.

#### Some usage tips

- Shift+Enter runs a cell and moves to the next.

- All cells share one memory. A variable made in cell 3 is still there in cell 10.

- Order of execution is what counts, not order on screen. If you run cell 8, then go back and edit and run cell 2, the notebook is now in a state that doesn't match reading it top to bottom. The \[1\], \[2\] numbers in the left margin tell you the real order.

- When something makes no sense, restart. Kernel → Restart Kernel and Run All Cells.

- Once analysis is settled it may make sense to move it out of the notebook into a .py file.

## If you move on to .py scripts

I would say **Visual Studio Code (VS Code)** is probably what I would recommend getting used to. It is a free code editor that (I think!) has become the standard. It plays well with Jupyter notebooks and can recognise your environments and has a built-in terminal so you can write your script, run your environment and test your code all in one window. It has many extensions that could add functionality you might like including the use of agentic AIs within it.

### Small note I don’t know where else to put: File Paths on Windows machines

Before you can analyse an image, you have to tell Python where it lives on your computer. If you are on a Windows machine, this is a classic trap. Windows uses backslashes in its file paths (e.g., C:\User\Data\image.tif), but in Python, a backslash is a special "escape" character (for example, \n is the hidden code for a new line).

If you just paste a standard Windows path into Python, it will likely crash because it misinterprets those backslashes. The easiest fix is to put a lowercase r (for "raw") right before the quote marks. This tells Python to read the text exactly as written:

filepath = r"C:\User\Data\microscope_image.tif"
