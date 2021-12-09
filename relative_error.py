import pandas as pd
import sys
from subprocess import call

def compute_relative():
    analytical = pd.read_csv("sensitivity.dat", delim_whitespace=True, header=None)
    analytical_len = len(analytical)

    fdm = pd.read_csv("sensitivity_fdm.dat", delim_whitespace=True, header=None)
    fdm_len = len(fdm)

    if(analytical_len != fdm_len):
        print("the data size of sensitivity does not matched\n EXIT")
        sys.exit()

    output = open("relative_error.dat", "w")
    for i in range(50):
        rerror = abs((analytical[1][i] - fdm[1][i])/fdm[1][i]) * 100
        output.write("{} {:e}\n".format(i, rerror))
    output.close()

def plot_relative_error():
    args =  '''
                set terminal qt font "Arial, 20";
                set output "relative_error.svg";
                set xlabel "Element ID" font "Arial, 28";
                set ylabel "Relative Erorr (%)" font "Arial, 30";
                plot "relative_error.dat" with lines linewidth 2.5 notitle;
                pause -1;
            '''
    call([ "gnuplot", "-e", args])

def plot_sensitivity():
    args =  '''
                set terminal qt font "Arial, 20";
                set output "sensitivity.svg";
                set xlabel "Element ID"  font "Arial, 28";
                set ylabel "Sensitivity" font "Arial, 30";
                set key bottom right;
                set key box;
                plot
                'sensitivity.dat'      with lines      linewidth 2.5                      title "Adjoint Method",
                'sensitivity_fdm.dat'                  pt 13 ps 1.5  title "FDM" ;
                pause -1;
            '''
    call([ "gnuplot", "-e", args])

compute_relative()

plot_sensitivity()
plot_relative_error()