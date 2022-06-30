# GCode-parameter-parser
The goal of the main script is enable the use of variables in gcode. The variables can be declared in the gcode file itself or as arguments to the script. The extension is usefull when testing the effect of parameters (for example: extrusion rate) of the physical result.

## Supported variables
* ZH (Z-Height): this corosponds to the layer height
* ER (Extrusion Rate): Coefficient to be multiplied by the distance traveled

# Usage

## Using command line
| Flag | Command | Parameter | Description|
| --- | --- | --- | --- |
| -F | --filename | input files | 0..n files to parse|
| -O | --open | open parsed files |
| -P | --params  | list of parameters with values | 0..2n variable-value pairs |
| -ER | --extrusion_rate | Extrusion rate ||
| -ZH | --z_heigth | Z heigth ||

Note:
* If no (valid) files are given as input, a UI will pop up to let you choose files.
* -P overrules the specific parameter assignments
* In-file parameter assignment overrules command parameters, exception-cases


## Using the UI
It is recommended to declare all parameters in the beginning of the file. Yet, the parser only requires a variable to be declare before the first usage to allow substitution.
To declare a variable following code can be added:
```
;VAR name value
```
* Note that the semicolon is used to start a comment, this comment is kept after parsing to later refer to the used variables.
* Watch out: "VAR" should be uppercase, followed by a space, the name of the variable, a space and the value (integer or float). 

## Running the script
Running the script will pop-up a dialog to let you choose a input file(s). Afterwards, ER and ZH will be asked to define using a new dialog. Once completed, the script should have created a new file(s) with the initial filename(s) extended by "_output" in the same directory as the initial file(s).
