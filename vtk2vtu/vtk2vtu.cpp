#include <iostream>
#include <vector>
#include <string>
#include <filesystem>
#include <omp.h>

#include <vtkUnstructuredGrid.h>
#include <vtkUnstructuredGridReader.h>
#include <vtkXMLUnstructuredGridWriter.h>

namespace fs = std::filesystem;


bool converter(const fs::path &input_path)
{
    auto reader = vtkSmartPointer<vtkUnstructuredGridReader>::New();
    reader->SetFileName(input_path.c_str());
    reader->ReadAllScalarsOn();
    reader->ReadAllVectorsOn();
    reader->ReadAllTensorsOn();
    reader->Update();
    fs::path export_path = input_path.string() + ".vtu";
    auto writer = vtkSmartPointer<vtkXMLUnstructuredGridWriter>::New();
    writer->SetFileName(export_path.c_str());
    writer->SetInputData(reader->GetOutput());
    writer->Write();
    std::cout << fs::relative(input_path) << " -> " << fs::relative(export_path) << std::endl;
    return true;
}

std::vector<fs::path> get_file_list()
{
    std::vector<fs::path> file_list;
    for(const fs::directory_entry &x: fs::directory_iterator(fs::current_path()))
    {
        if(x.path().extension() == ".vtk")
            file_list.push_back(x.path());
    }
    return file_list;
}

int main(int argc, char** argv)
{
  std::vector<std::string> args(argv, argv + argc);
  if(argc != 1)
  {
      std::cout << "usage: this program converts all .vtk files in current directory to compressed vtu file" << std::endl;
      std::exit(1);
  }
  auto list = get_file_list();

  std::cout << omp_get_max_threads() << std::endl;
#pragma omp parallel for
  for(auto item:list) converter(item);
}

