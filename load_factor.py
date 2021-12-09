import pandas as pd
import sys
from subprocess import call

def plot_load_factor():
    args =  '''
                set terminal qt font "Arial, 27";
                set output "sensitivity.svg";
                set xlabel "t (s)"  font "Arial, 28";
                set ylabel "load factor" font "Arial, 30";
                set yrange [0.0:1.0];
                plot 
                'load_factor.dat'      with lines      linewidth 5  notitle;
                pause -1;
            '''
    call([ "gnuplot", "-e", args])

plot_load_factor()