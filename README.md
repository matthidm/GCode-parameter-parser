# GCode-converter
Parses a Gcode/txt file and fills in the variables.

Running the script will pop-up a dialog to let you choose a input file. Currently .gcode and .txt are supported but others are easy to add. The file should have the variables defined within and before the first usage. A variable can be defined in the following way

```
;VAR name value
```
Watch out: "VAR" should be uppercase, followed by a space, the name of the variable, a space and the value (integer or float). 


# Supported variables
* ZH (Z-Height): this corosponds to the layer height
* ER (Extrusion Rate): Coefficient to be multiplied by the distance traveled
