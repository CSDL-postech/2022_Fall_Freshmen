from BasicCodes.parser import parsing
from BasicCodes.visualization import *
import math

def getHPWL(net_list, cell_list, pad_list):
    # Enter your code here to get the HPWL
    return 0


if __name__ == '__main__':
    filename = "benchmarks/toy1"
    net_list, cell_list, pad_list = parsing(filename)

    draw_window(pad_list, cell_list, net_list, ver="visualization")
    HPWL = getHPWL(net_list, cell_list, pad_list)
    print("Initial HPWL:", HPWL)

