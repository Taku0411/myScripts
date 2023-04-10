#include <algorithm>
#include <filesystem>
#include <iostream>
#include <string>
#include <system_error>
#include <vector>

#include <vtkCellData.h>
#include <vtkDoubleArray.h>
#include <vtkPointData.h>
#include <vtkPoints.h>
#include <vtkSmartPointer.h>

#include <vtkUnstructuredGrid.h>
#include <vtkXMLUnstructuredGridReader.h>

#include <vtkAbstractArray.h>
#include <vtkCellLocator.h>

namespace fs = std::filesystem;

class info
{
	vtkIdType n_node; // number of node
	vtkIdType n_cell; // number of element
	std::vector<std::string> dataSet;
};

