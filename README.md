# retroimagify
Convert your images to the 80's retro computer look with this Python script. 

The algorithm used to convert colors is the "low-cost approximation" algorithm as presented [here](https://www.compuphase.com/cmetric.htm).

The currently supported retrocomputers (their palettes and resolutions) are the following:
![CSupported retro systems](https://github.com/t33bu/retroimagify/blob/master/Itsukushima.png)
Original image [Itsukushima Gate](https://en.wikipedia.org/wiki/Itsukushima_Shrine#/media/File:Itsukushima_Gate.jpg) by Jordy Meow (CC BY-SA 3.0). The palettes are retrieved from free [Lospec Palette List](https://lospec.com/palette-list).

## Command line options:

**-o \<system name>** where you need to input the name of output system. The system must have corresponding <system_name>.txt file that describes its screen resolution and color palette. For example _-o bbcm_ converts to the screen resolution and color palette of BBC Micro. 
  
**-noresize** to retain the original dimensions of the image.

### Example usage:
_python retroimagify.py -noresize -o c64 image.png_

## Palette file format

The first line is the screen resolution: width,height

The following lines contain the RGB value of a color per line: r,g,b

Hexadecimal numbers are used
```
140,c8      # screen resoution
00,00,00    # colors...
ff,55,ff
55,ff,ff
ff,ff,ff
```

