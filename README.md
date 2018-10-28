# inkscape-elegant
Redesigned look for inkscape providing modern light & dark theme


This project's goal is to produce a more "elegant" and stylish inkscape theme, this includes a proper gtk theme and icons set.


## Sample
sample usage of tool and result on the default icons (black)
```
python change_colors.py black scalable scalable-generated --create-theme
python change_colors.py white scalable scalable-generated --create-theme
python change_colors.py "#6FC3DF" scalable scalable-generated --create-theme
```

result:
![black icons](https://image.ibb.co/jGR25q/inkscape-1.png)
![white icons](https://image.ibb.co/hJbPJA/inkscape-2.png)
![custom blue icons](https://image.ibb.co/c7QJdA/inkscape-3.png)

### Dependencies
```
pip install lxml
```

## Usage

### Linux
if you use the optional argument```--create-theme``` the tool will automatically detect your current icon-theme and create a new theme called inkscape-elegant that inherits the current one and apply it

```
#generate white icons to the directory "scalable-generated" and create a new icon-theme and apply it
python change_colors.py white scalable scalable-generated --create-theme
```

```
#generate black icons to the directory "scalable-generated" and create a new icon-theme and apply it
python change_colors.py black scalable scalable-generated --create-theme
```


### Mac OS X
todo

### Windows
Note: run the cmd as an administrator as the icons will be written in program files
Note: expected inkscape installation path is C:\Program Files\Inkscape
```
#generate white icons to the directory "scalable-generated" and create a new icon-theme and apply it
python change_colors.py white scalable scalable-generated --create-theme
```

```
#generate black icons to the directory "scalable-generated" and create a new icon-theme and apply it
python change_colors.py black scalable scalable-generated --create-theme
```

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
