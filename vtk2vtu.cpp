#include <iostream>
#include <vector>
#include <string>
#include <filesystem>

#include <vtk-9.2/vtkUnstructuredGrid.h>
#include <vtk-9.2/vtkUnstructuredGridReader.h>

namespace fs = std::filesystem;

int main(int argc, char** argv)
{
  std::vector<std::string> args(argv, argv + argc);
  fs::path path = args[1];
  if(!exists(path)) 
  {
    std::cout << "no such file or directory: "  << path << std::endl;
      std::exit(1);
  }
  auto reader = vtkUnstructuredGridReader();
}

