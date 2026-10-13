"""Check the RACE workshop environment.
Prints the versions of everything that matters, compares them against what we
resolved when the environment was frozen, confirms we are on CPU, confirms the
plugins are actually registered with napari, then opens napari with a test
image. If a window appears and nothing below says NOT WORKING, you are ready.
Send the whole output as text, not a screenshot, if anything goes wrong.
"""

import importlib.metadata as metadata
import os
import platform
import sys

EXPECTED = {
    "python": "3.11.16",
    "numpy": "2.0.2",
    "scikit-image": "0.26.0",
    "pandas": "3.0.6",
    "torch": "2.13.0",
    "napari": "0.9.2",
    "PyQt5": "5.15.11",
    "bioio": "3.5.1",
    "cellpose": "3.1.1.3",
    "cellpose-napari": "0.2.0",
    "napari-skimage-regionprops": "0.10.1",
    "napari-segment-blobs-and-things-with-membranes": "0.3.12",
    "bioio-tifffile": "1.3.1",
    "bioio-ome-tiff": "1.4.0",
    "bioio-czi": "3.0.1",
    "bioio-nd2": "2.5.0",
    "opencv-python-headless": "5.0.0.93",
    "ndevio": "0.10.0",
}

# import name -> distribution name, where they differ
PACKAGES = [
    ("numpy", "numpy"),
    ("skimage", "scikit-image"),
    ("pandas", "pandas"),
    ("torch", "torch"),
    ("napari", "napari"),
    ("bioio", "bioio"),
    ("cellpose", "cellpose"),
    ("cv2", "opencv-python-headless"),
    ("cellpose_napari", "cellpose-napari"),
    ("napari_segment_blobs_and_things_with_membranes",
     "napari-segment-blobs-and-things-with-membranes"),
    ("napari_skimage_regionprops", "napari-skimage-regionprops"),
]

# bioio format support comes from separate reader packages.
READERS = [
    ("bioio_tifffile", "bioio-tifffile"),
    ("bioio_ome_tiff", "bioio-ome-tiff"),
    ("bioio_czi", "bioio-czi"),
    ("bioio_nd2", "bioio-nd2"),
    # ndevio is the napari READER that wraps all of the above. bioio alone lets
    # Python open a .czi; ndevio is what lets you drag one onto the window.
    # Checked here by name so a missing one is reported as the cause, not just
    # as the symptom further down.
    ("ndevio", "ndevio"),
]

problems = []
mismatches = []


def installed_version(dist):
    try:
        return metadata.version(dist)
    except Exception:  # noqa: BLE001
        return None


def compare(dist, found):
    want = EXPECTED.get(dist)
    if want and found and found != want:
        mismatches.append((dist, want, found))
        return f"  (expected {want})"
    return ""


print("System")
py = sys.version.split()[0]
print(f"  {'python':<28} {py}{compare('python', py)}")
print(f"  {'platform':<28} {platform.platform()}")
print(f"  {'machine':<28} {platform.machine()}")
print()

print("Environment isolation")

conda_prefix = os.environ.get("CONDA_PREFIX")
if conda_prefix and os.path.normcase(os.path.realpath(conda_prefix)) != os.path.normcase(
    os.path.realpath(sys.prefix)
):
    problems.append(
        "you are not running the environment's Python - the shell says "
        f"{conda_prefix} but this interpreter is {sys.prefix}"
    )
    print("  NOT WORKING - wrong interpreter")
    print(f"    activated environment  {conda_prefix}")
    print(f"    running interpreter    {sys.prefix}")
    print()
    print("    Everything below will fail for this one reason. Run instead:")
    if os.name == "nt":
        env_python = os.path.join(conda_prefix, "python.exe")
        how = "check whether a different python is earlier on your PATH"
    else:
        env_python = os.path.join(conda_prefix, "bin", "python")
        how = "then check 'which -a python' and 'alias python' for the cause"
    print(f'      "{env_python}" {os.path.basename(__file__)}')
    print(f"    {how}.")
elif conda_prefix:
    print(f"  {'running the environment':<28} ok")
else:
    problems.append(
        "no environment is activated - run 'conda activate race-2026' first"
    )
    print("  NOT WORKING - no conda environment is activated")

env_prefix = os.path.normcase(sys.prefix)
leaked = [
    p for p in sys.path
    if p and "roaming" in os.path.normcase(p)
    and not os.path.normcase(p).startswith(env_prefix)
]
if leaked:
    problems.append(
        "user-site packages are on the path - run 'conda activate race-2026' "
        "first, and do not launch this from an IDE"
    )
    print("  NOT WORKING - packages outside the environment are on the path:")
    for p in leaked:
        print(f"    {p}")
else:
    print(f"  {'user-site excluded':<28} ok")
print(f"  {'environment':<28} {sys.prefix}")
print()

print("Packages")
for import_name, dist in PACKAGES:
    try:
        __import__(import_name)
    except Exception as exc:  # noqa: BLE001
        problems.append(dist)
        print(f"  {dist:<28} NOT WORKING - {type(exc).__name__}: {exc}")
        continue
    found = installed_version(dist) or "installed"
    print(f"  {dist:<28} {found}{compare(dist, found)}")
print()

print("Microscope format readers")
for import_name, dist in READERS:
    try:
        __import__(import_name)
    except Exception as exc:  # noqa: BLE001
        problems.append(dist)
        print(f"  {dist:<28} NOT WORKING - {type(exc).__name__}: {exc}")
        continue
    found = installed_version(dist) or "ok"
    print(f"  {dist:<28} {found}{compare(dist, found)}")
print()

# CPU-only is deliberate. 
try:
    import torch

    print("PyTorch")
    print("  version        ", torch.__version__)
    print("  CUDA build     ", torch.version.cuda or "no (correct)")
    print("  CUDA available ", torch.cuda.is_available(), "(should be False)")
    # torch.version.cuda is the test that matters, not cuda.is_available().
    # A CUDA wheel on a laptop with no GPU reports is_available() False while
    # still being the wrong build - three gigabytes larger, and it brings its
    # own OpenMP runtime, which clashes with conda's the moment bioio and
    # cellpose are imported together. Do not test for a "+cpu" suffix instead:
    # conda-forge's pytorch-cpu reports a plain version like 2.13.0, and only
    # pip wheels carry +cpu.
    if torch.version.cuda or torch.cuda.is_available():
        problems.append(
            f"torch {torch.__version__} is a CUDA build - we want CPU only. "
            "See the notes at the top of environment.yml."
        )
    print()
except Exception:  # noqa: BLE001
    pass

print("Reading an image and segmenting it")
try:
    import bioio  # noqa: F401
    from cellpose import models

    if not hasattr(models, "Cellpose"):
        problems.append(
            "cellpose 4 is installed - the napari plugin cannot drive it; "
            "the environment should pin cellpose<4"
        )
        print("  cellpose API                 WRONG MAJOR VERSION (need cellpose<4)")
    else:
        print("  bioio + cellpose together    ok")
except Exception as exc:  # noqa: BLE001
    problems.append(f"bioio and cellpose clash: {exc}")
    print(f"  NOT WORKING - {type(exc).__name__}: {exc}")
print()

print("Plugins registered with napari")
try:
    from npe2 import PluginManager

    pm = PluginManager.instance()
    pm.discover(include_npe1=True)
    widgets = [(str(w.plugin_name), str(w.display_name)) for w in pm.iter_widgets()]
    for label, needle in [
        ("cellpose", "cellpose"),
        ("classical segmentation", "blob"),
    ]:
        found = [w for w in widgets if needle in w[0].lower()]
        if found:
            print(f"  {label:<28} ok ({len(found)} widget(s))")
        else:
            problems.append(f"napari cannot see the {label} plugin")
            print(f"  {label:<28} NOT WORKING - napari cannot see it")

    for ext, label in [(".czi", "czi reader"), (".nd2", "nd2 reader")]:
        readers = [
            str(r.plugin_name) for r in pm.iter_compatible_readers([f"example{ext}"])
        ]
        if readers:
            print(f"  {label:<28} ok ({', '.join(readers)})")
        else:
            problems.append(
                f"no napari plugin can open {ext} files - napari will say "
                f"'no plugin found capable of reading'. The reader is ndevio."
            )
            print(f"  {label:<28} NOT WORKING - nothing can open {ext}")
except Exception as exc:  # noqa: BLE001
    problems.append(f"plugin check failed: {exc}")
    print(f"  NOT WORKING - {type(exc).__name__}: {exc}")
print()

DATA_EXPECTED = 9
if "--data" in sys.argv:
    idx = sys.argv.index("--data")
    folder = sys.argv[idx + 1] if len(sys.argv) > idx + 1 else "race-data"
    print("Test data")
    print(f"  folder                       {os.path.abspath(folder)}")
    if not os.path.isdir(folder):
        problems.append(f"data folder '{folder}' not found")
        print("  NOT WORKING - folder not found")
    else:
        czis = sorted(
            os.path.join(root, f)
            for root, _, files in os.walk(folder)
            for f in files
            if f.lower().endswith(".czi")
        )
        print(f"  {'files found':<28} {len(czis)} (expected {DATA_EXPECTED})")
        if len(czis) != DATA_EXPECTED:
            problems.append(
                f"found {len(czis)} .czi files, expected {DATA_EXPECTED} - "
                "the download may be incomplete"
            )
        try:
            from bioio import BioImage

            for path in czis:
                size_mb = os.path.getsize(path) / 1024 / 1024
                img = BioImage(path)
                shape = "x".join(str(d) for d in img.shape)
                print(f"    {os.path.basename(path):<34} {size_mb:6.1f} MB  {shape}")
        except Exception as exc:  # noqa: BLE001
            problems.append(f"could not open the data: {exc}")
            print(f"  NOT WORKING - {type(exc).__name__}: {exc}")
    print()

if mismatches:
    print("Different versions from the ones we froze:")
    for dist, want, found in mismatches:
        print(f"  {dist:<28} expected {want}, got {found}")
    print()
    print("  Not necessarily broken, but please mention it - it means your")
    print("  install resolved differently from the machines we tested on.")
    print()

if problems:
    print("Something is not right:")
    for p in problems:
        print("  -", p)
    print()
    print("MOST OF THE TIME THIS IS THE SAME THING, AND THIS FIXES IT.")
    print()
    print("conda's pip step sometimes stops partway without reporting an error,")
    print("so you get the packages that were named but not everything they need.")
    print("With the environment activated, copy this ONE line and run it:")
    print()
    print("  pip install --upgrade bioio bioio-ome-tiff bioio-tifffile "
          "bioio-czi bioio-nd2 ndevio \"cellpose<4\" cellpose-napari "
          "napari-segment-blobs-and-things-with-membranes "
          "napari-skimage-regionprops")
    print()
    print("Then run this script again. It is safe to run either command twice.")
    print()
    print("If it still fails, please send this whole output, as TEXT not a")
    print("screenshot, to the drop-in session or by e-mail before the course.")
    raise SystemExit(1)

# Qt is the classic silent failure: everything imports, no window ever appears.
print("Opening napari. Close the window when you can see it.")

import napari  # noqa: E402
from skimage.data import cells3d  # noqa: E402

viewer = napari.Viewer()
viewer.add_image(
    cells3d(),
    channel_axis=1,
    name=["membrane", "nuclei"],
    scale=(0.29, 0.26, 0.26),  # z, y, x in microns - anisotropic on purpose
)
napari.run()

print()
print("If a napari window opened, you are all set. See you in Warsaw.")
