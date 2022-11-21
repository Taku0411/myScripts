import vtk
import sys
from concurrent.futures import ThreadPoolExecutor
import os

if(len(sys.argv) == 1):
    print("Usage: python3 VTKascii2binary {filename}")
    sys.exit(1)

def write(filename):
	reader = vtk.vtkUnstructuredGridReader()
	reader.SetFileName(filename)
	reader.ReadAllScalarsOn()
	reader.ReadAllVectorsOn()
	reader.ReadAllTensorsOn()
	reader.Update()
	writer = vtk.vtkXMLUnstructuredGridWriter()
	writer.SetFileName("{}.vtu".format(filename))
	writer.SetInputData(reader.GetOutput())
	writer.Write()
	print(" {} > {}.vtu".format(filename, filename))
	
	


with ThreadPoolExecutor(max_workers=6, thread_name_prefix="thread") as executor:
	for filename in sys.argv[1:]:
		executor.submit(write, filename)