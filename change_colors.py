from lxml import etree
import glob, os, sys

if len(sys.argv) < 3:
    print(
"""    
    Usage: change_colors.py [color] [actions_source] [actions_destination]
    available colors:
        - white
        - black
        - hex_code(e.g. #ff00aa)
    actions_source: name of the scalable directory which contains the actions directory
    actions_destination: name of the directory to move generated actions directory to        
""")
    exit(0)

color = sys.argv[1]
input_dir = sys.argv[2]
output_dir = sys.argv[3]

icons_dirs = ['actions/', 'actions_elegant/']

if color == 'white':
    color = '#ffffff'
elif color == 'black':
    color = '#000000'

if not input_dir.endswith(("/")):
    input_dir += '/'

if not output_dir.endswith(("/")):
    output_dir += '/'
    

for icons_dir in icons_dirs:
    if not os.path.exists(output_dir + icons_dir.replace('_elegant','')):
        os.makedirs(output_dir + icons_dir.replace('_elegant',''))

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
                        style = path.attrib['style'].replace('color:#000000', 'color:' + color).replace('fill:#000000', 'fill:' + color)
                    else:
                        style = path.attrib['style'] + ";fill:" + color

            if 'stroke:#000000' in style:
                style = style.replace('stroke:#000000', "stroke:" + color)
            path.set("style", style)
            
        doc.write(open(output_dir + icons_dir.replace('_elegant','') + os.path.basename(file), 'wb'))
        print(file + " => " + output_dir + icons_dir.replace('_elegant','') + os.path.basename(file))
