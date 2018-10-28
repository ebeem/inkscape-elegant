import os
import shutil
import sys

from constants import THEME_NAME, ELEGANT_THEME_DIRECTORY

copy_from = sys.argv[1]
current_theme_name = sys.argv[2]

if current_theme_name == THEME_NAME:
    print("you are currently using " + current_theme_name + " checking inherited theme ...")
    with open(ELEGANT_THEME_DIRECTORY + 'index.theme') as f:
        for line in f:
            if line.startswith("Inherits="):
                current_theme_name = line[len("Inherits="):]
        raise Exception("could not find theme inherited by current inkscape-elegant theme, change you currrent "
                        "theme and try again")

if os.path.exists(ELEGANT_THEME_DIRECTORY):
    print('deleting old theme ' + ELEGANT_THEME_DIRECTORY)
    shutil.rmtree(ELEGANT_THEME_DIRECTORY)

os.makedirs(ELEGANT_THEME_DIRECTORY)
print('copying ' + copy_from + ' to ' + ELEGANT_THEME_DIRECTORY + 'scalable')
shutil.copytree(copy_from, ELEGANT_THEME_DIRECTORY + 'scalable')
text_file = open(ELEGANT_THEME_DIRECTORY + 'index.theme', "w")
text_file.write("""
[Icon Theme]
Name=inkscape-elegant
Comment=Redesigned elegant inkscape icons

Inherits=""" + str(current_theme_name) + """
Directories=scalable/actions

[scalable/actions]
MinSize=8
Size=16
MaxSize=512
Context=Actions
Type=Scalable
        """)

text_file.close()
print('writing inheritance from ' + str(current_theme_name))
