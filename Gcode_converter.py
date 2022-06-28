import re
import os
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def error_message(msg):
    print(msg)
    input("Click ENTER to exit")
    exit()

def parse_line(line:str, params:dict) -> str:
    if "ER" in line:
        if "ER" not in params:
            error_message("ERROR: Undefined parameter used: ER")
        else:
            x = re.findall("X-?(\d+\.?\d*)", line)
            y = re.findall("Y-?(\d+\.?\d*)", line)
            x = float(x[0]) if len(x) == 1 else 0
            y = float(y[0]) if len(y) == 1 else 0
            l = math.sqrt(x**2+y**2)
            return line.replace("ER", f"E {params['ER']*l:.2f}")

    elif "ZH" in line:
        if "ZH" not in params:
            error_message("ERROR: Undefined parameter used: ZH")
        return line.replace("ZH", f"Z {params['ZH']:.2f}")
    else:
        return line

def search_parameters(line:str, params:dict):
    if "VAR" in line:
        tokens = line.split(" ")
        if len(tokens) != 3:
            error_message("ERROR: variable undefined")
        params[tokens[1]] = float(tokens[2])

    
def main():
    # Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    input_file = askopenfilename(initialdir = os.getcwd(), filetypes=[("Gcode","*.gcode"), ("Text","*.txt")])
    output_file = input_file.replace(".","_output.")
    params = dict()

    with open(input_file, "r") as infile:
        with open(output_file, "w") as outfile:
            outfile.write(";This code was parsed and adjusted by a python script\n")
            for line in infile.readlines():
                search_parameters(line, params)
                outfile.write(parse_line(line, params))

if __name__=="__main__":
    main()
