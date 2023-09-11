# vtu_compression 
This program is made for compress vtu files by LZMA algorithm.
Note: Files will be overwritten.

# how to use
usage: ./vtu_compressor <files>

# how to build
~~~
cmake -B build 
cmake --build build
~~~
If some errors occured in configuration, cmake would not find VTK library.
For this problem,
~~~
cmake -B build -DVTK_DIR=<path to vtk-config.cmake>
~~~


