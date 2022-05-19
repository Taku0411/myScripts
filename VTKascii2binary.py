import vtk
import sys

print(sys.argv)
if(len(sys.argv) != 2):
    print("Usage: python3 VTKascii2binary YourFileName")
    sys.exit(1)

filename = sys.argv[1]

reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName(filename)
reader.Update()


writer = vtk.vtkUnstructuredGridWriter()
# writer = vtk.vtkXMLUnstructuredGridWriter()
writer.SetFileName("bin_{}".format(filename))
writer.SetInputData(reader.GetOutput())
writer.SetFileTypeToBinary()
writer.Write()