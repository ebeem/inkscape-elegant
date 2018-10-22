# inkscape-elegant
redesigned look for inkscape providing modern light & dark theme


This project's goal is to produce a more "elegant" and stylish inkscape theme, this includes a proper gtk theme and icons set.


## Sample
sample usage of tool and result on the default icons (black)
```
python change_colors.py black scalable scalable-black
python change_colors.py white scalable scalable-white
python change_colors.py "#6FC3DF" scalable scalable-blue
```

result:
![black icons](https://image.ibb.co/jGR25q/inkscape-1.png)
![white icons](https://image.ibb.co/hJbPJA/inkscape-2.png)
![custom blue icons](https://image.ibb.co/c7QJdA/inkscape-3.png)


## Setup
this project will produce a new set of icons that should be added to the current gtk icons theme<br>
the provided python tools copy all inkscape icons and modify their color to a desired one

sample usage of tool
```
#generate black icons to the directory "scalable-black"
python change_colors.py black scalable scalable-black

#generate white icons to the directory "scalable-white"
python change_colors.py white scalable scalable-white

#generate cyan icons (code #6FC3DF) to the directory "scalable-blue"
python change_colors.py "#6FC3DF" scalable scalable-blue
```

### Linux
the sub directories of the destination directory provided in the python tool should be copied to you current icons theme in scalable directory, for example: 
```
#generate white icons to the directory "scalable-white"
python change_colors.py white scalable scalable-white
```
in this case you will copy `scalable-white/actions` into your icon theme scalable directory <br>
usually, this should work since most icon theme inherit from `hicolor` (take backup of `hicolor` first) <br>
`sudo cp -dr scalable-white/. /usr/share/icons/hicolor/scalable`

if you use Adwaita icons <br>
`sudo cp -dr scalable-white/. /usr/share/icons/Adwaita/scalable`

=================================

yes, you can directly genereate to your icon-theme and get it done in one step instead of two<br>
`sudo python change_colors.py white scalable /usr/share/icons/Adwaita/scalable`<br>
however, it's not recommended<br>
`


### Mac OS X
todo

### Windows
todo

## Contribution
icons contrubution is more than welcome!<br>
to keep icons semantic, a common guidelines must be followed [todo], icons style was chosen to be so simple and yet elegant, the icons should only be outlined by one color (black), the stroke must be as thin as possible and should NOT be filled by any color.<br>
a great sample of good looking icons can be [found here](https://logosbynick.com/new-icons-for-inkscape/)

![Sample Icons](http://blog.logosbynick.com/wp-content/uploads/2016/04/RedesignedInkscapeIcons-1.png)

[by Nick Saporito](https://logosbynick.com/new-icons-for-inkscape/)

the default icons are black symbolic icons <br>
a set of redesigned icons can be found in `scalable/actions_elegant`<br>
new redesigned icons should bee added to `scalable/actions_elegant`, the python tool will be responsible for overriding the old default icon placed in `scalable/actions`

a set of the same icons is generated on-demand using the python tool `change_colors.py`,


## Credits
[new inkscape icons by Nick Saporito](https://logosbynick.com/new-icons-for-inkscape/)
