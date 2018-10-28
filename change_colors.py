import glob
import os
import subprocess
import sys
import shutil

from lxml import etree
from sys import platform
from constants import THEME_NAME, ICONS_DIRS, ELEGANT_THEME_DIRECTORY, WINDOWS_ICONS_PATH


def has_option(option_name):
    if len(sys.argv) < 5:
        return False

    for i in range(4, len(sys.argv)):
        if sys.argv[i] == option_name:
            return True

    return False


def create_elegant_icons_theme(copy_from):
    if platform == "linux" or platform == "linux2":
        print("linux machine")
        try:
            current_theme_name = subprocess.check_output(
                ['gsettings', 'get', 'org.gnome.desktop.interface', 'icon-theme']) \
                                     .decode("utf-8").replace('\n', '')[1:-1]

            if current_theme_name == THEME_NAME:
                print("you are currently using " + current_theme_name + " checking inherited theme ...")
                with open(ELEGANT_THEME_DIRECTORY + 'index.theme') as f:
                    find_word = "Inherits="
                    length = len(find_word)
                    theme_found = False

                    for line in f:
                        if len(line) > length and line[:length] == find_word:
                            current_theme_name = line[length:]
                            theme_found = True
                            break

                    if not theme_found:
                        raise Exception(
                            "could not find theme inherited by current inkscape-elegant theme, change you currrent "
                            "theme and try again")

            print("current theme is " + current_theme_name)
        except Exception as error:
            print('an error occurred while trying to get current icon-theme: ' + str(error))
            current_theme_name = input(
                'looks like gsettings is not installed, you need to enter you current gtk-icon-theme > ')

        try:
            subprocess.check_output(['sudo', 'python', os.path.dirname(os.path.realpath(__file__))
                                     + '/create_theme_icons.py', copy_from, current_theme_name])
            subprocess.check_output(['gsettings', 'set', 'org.gnome.desktop.interface', 'icon-theme', THEME_NAME]) \
                .decode("utf-8").replace('\n', '')
            print('successfully updated current icon theme to ' + THEME_NAME)
        except Exception as error:
            print('an error occurred while trying to set current icon-theme: ' + str(error))
            print('looks like gsettings is not installed, you need to set the icon-theme '
                  '[' + THEME_NAME + '] yourself, we recommend using gnome-tweaks tool')
    elif platform == "darwin":
        # OS X
        print("mac os machine")
    elif platform == "win32":
        print("windows machine")
        if os.path.exists(WINDOWS_ICONS_PATH):
            print('deleting old theme ' + WINDOWS_ICONS_PATH)
            shutil.rmtree(WINDOWS_ICONS_PATH)
        shutil.copytree(copy_from, WINDOWS_ICONS_PATH)
        print('successfully applied theme')


def analyze_color(color):
    if color == 'white':
        return '#ffffff'
    elif color == 'black':
        return '#000000'
    return color


def analyze_input_directory(input_dir):
    if not input_dir.endswith("/"):
        return input_dir + '/'
    return input_dir


def copy_icons_with_color(input_dir, output_dir, color):
    for icons_dir in ICONS_DIRS:
        if not os.path.exists(output_dir + icons_dir.replace('_elegant', '')):
            os.makedirs(output_dir + icons_dir.replace('_elegant', ''))

        for file in glob.glob(input_dir + icons_dir + "*.svg"):
            doc = etree.parse(file)

            for path in doc.xpath('//*[local-name()="path"]'):
                # resolve default icons
                style = "fill:" + color
                if "style" in path.attrib:
                    # paths to skip
                    if 'fill:none' in path.attrib['style']:
                        style = path.attrib['style']
                    else:
                        # resolve Nick Saporito's icons
                        if 'color:#000000' in path.attrib['style'] or 'fill:#000000' in path.attrib['style']:
                            style = path.attrib['style'].replace('color:#000000', 'color:' + color).replace(
                                'fill:#000000', 'fill:' + color)
                        else:
                            style = path.attrib['style'] + ";fill:" + color

                if 'stroke:#000000' in style:
                    style = style.replace('stroke:#000000', "stroke:" + color)
                path.set("style", style)

            doc.write(open(output_dir + icons_dir.replace('_elegant', '') + os.path.basename(file), 'wb'))
            print(file + " => " + output_dir + icons_dir.replace('_elegant', '') + os.path.basename(file))


# arguments check
if len(sys.argv) < 4:
    print(
        """
    Usage: change_colors.py [color] [actions_source] [actions_destination] [OPTIONS...]
    available colors:
        - white
        - black
        - hex_code(e.g. #ff00aa)
    actions_source: name of the scalable directory which contains the actions directory
    actions_destination: name of the directory to move generated actions directory to       

    Available options:
         -c, --create-theme             creates a new icon theme that inherits current theme and apply it
""")
    exit(0)

COLOR = sys.argv[1]
INPUT_DIR = sys.argv[2]
OUTPUT_DIR = sys.argv[3]
CREATE_THEME = has_option('--create-theme') or has_option('-c')


def main():
    color = analyze_color(COLOR)
    input_dir = analyze_input_directory(INPUT_DIR)
    output_dir = analyze_input_directory(OUTPUT_DIR)
    copy_icons_with_color(input_dir, output_dir, color)

    if CREATE_THEME:
        create_elegant_icons_theme(output_dir)


if __name__ == '__main__':
    main()
