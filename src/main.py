import glob
from pathlib import Path

path = glob.glob("/home/zenoxlu/Documents/DevApps/gdrive-automation-script/src/dist/*")

paths = []

for i in path:
    # getSlash = i
    # sliceFileName = []
    # sliceFileName.append(getSlash)
    fullpath = Path(i)
    paths.append(fullpath.name)

for k in paths:
    print(k)