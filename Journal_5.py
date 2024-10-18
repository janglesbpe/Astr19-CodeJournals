import numpy as npy
from astropy.table import Table

#define main function
def main():
    x=npy.linspace(1,2*npy.pi, 1000)
    y=npy.sin(x)
    data_table= Table()
    data_table["x"]=x
    data_table["y"]=y
    print(data_table)

#if/then
if __name__ == '__main__':
    main()
