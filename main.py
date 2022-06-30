import re
import os
import math
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import argparse
from tkinter.simpledialog import askfloat

parser = argparse.ArgumentParser()
parser.add_argument('-F', '--filename',
                    dest='input_file',
                    help='Input file',
                    type=str,
                    nargs='+'
                    )

parser.add_argument("-ER", "--extrusion_rate",
                    dest='ER',
                    help='Parameter: Extrusion rate',
                    type=float,
                    )

parser.add_argument("-ZH", "--z_heigth",
                    dest='ZH',
                    help='Parameter: Z heigth',
                    type=float,
                    )
parser.add_argument("-P", "--params",
                    dest="params",
                    help='Parameters to use',
                    type=str,
                    nargs="+"
                    )
parser.add_argument("-O", "--open",
                    dest="open",
                    help="Open files output files",
                    action='store_true')

def parse_line(line:str, params:dict) -> str:
    if "ER" in params and "ER" in line:
        x = re.findall("X-?(\d+\.?\d*)", line)
        y = re.findall("Y-?(\d+\.?\d*)", line)
        x = float(x[0]) if len(x) == 1 else 0
        y = float(y[0]) if len(y) == 1 else 0
        l = math.sqrt(x**2+y**2)
        return line.replace("ER", f"E {params['ER']*l:.2f}")

    elif "ZH" in params and "ZH" in line:
        return line.replace("ZH", f"Z {params['ZH']:.2f}")
    else:
        return line

def search_parameters(line:str):
    if "VAR" in line:
        tokens = line.split(" ")
        if len(tokens) != 3:
            print("ERROR: variable undefined")
            input("Click ENTER to exit")
            exit()
        return tokens[1], float(tokens[2])
    

def parse_file(filename:str, params:dict = dict()):
    with open(filename, "r") as infile:
        with open(filename.replace(".", "_output."), "w") as outfile:
            outfile.write(";This code was parsed and adjusted by a python script\n")
            for line in infile.readlines():
                new_param = search_parameters(line)
                if new_param:
                    params[new_param[0]] = new_param[1]
                outfile.write(parse_line(line, params))


def main():
    args = parser.parse_args()
    params = dict()
    if args.ER:
        params["ER"] = args.ER[0]
    if args.ZH:
        params["ZH"] = args.ZH[0]
    if args.params:
        for i in range(0,len(args.params),2):
            params[args.params[i]] = float(args.params[i+1])

    if args.input_file:
        input_files = [file for file in args.input_file if os.path.exists(file)]
    else:
        input_files = askopenfilenames(initialdir = os.getcwd(), filetypes=[("Gcode","*.gcode"), ("Text","*.txt"), ("Other files", "*")])
        if "ER" not in params:
            params["ER"] = askfloat("Input", "Input an the extrusion rate")
        if "ZH" not in params:
            params["ZH"] = askfloat("Input", "Input an the z-heigth")
    
    

    for file in input_files:
        parse_file(file, params)

    if args.open:
        for file in input_files:
            os.startfile(file.replace(".", "_output."))

if __name__=="__main__":
    main()
