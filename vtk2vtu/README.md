# vtk2vtu
This program converts vtkUnstructuredGrid into vtkXMLUnstructuredGrid with zlib compression.

# how to use
Just run vtk2vtu under some directories.   
vtk2vtu converts all *.vtk files into *.vtu files.

# how to build
~~~
cmake -B build 
cmake --build build
~~~
If some errors occured in configuration, cmake would not find VTK or Qt5 library.
For this problem,
~~~
cmake -B build -DVTK_DIR=<path to vtk-config.cmake> -DQt5_DIR=<path to Qt5Config.cmake>
~~~


