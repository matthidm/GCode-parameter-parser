# GCode-parameter-parser
The goal of the main script is enable the use of variables in gcode. This is done by extending the gcode keywords and parsing the file to transform it back back substituting the variables in. The extension is usefull when testing the effect of parameters (for example: extrusion rate) of the physical result.

## Supported variables
* ZH (Z-Height): this corosponds to the layer height
* ER (Extrusion Rate): Coefficient to be multiplied by the distance traveled

# Usage

## Preparing a file
It is recommended to declare all parameters in the beginning of the file. Yet, the parser only requires a variable to be declare before the first usage to allow substitution.
To declare a variable following code can be added:
```
;VAR name value
```
* Note that the semicolon is used to start a comment, this comment is kept after parsing to later refer to the used variables.
* Watch out: "VAR" should be uppercase, followed by a space, the name of the variable, a space and the value (integer or float). 

## Running the script

Running the script will pop-up a dialog to let you choose a input file. Once completed, the script should have created a new file with the initial filename extended by "_output" in the same directory as the initial file.
