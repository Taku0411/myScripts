#include <filesystem>
#include <iostream>
#include <string>
#include <vector>

#include <vtkDataReader.h>
#include <vtkUnstructuredGrid.h>
#include <vtkXMLUnstructuredGridReader.h>
#include <vtkXMLUnstructuredGridWriter.h>

namespace fs = std::filesystem;

bool converter(const fs::path &input_path) {
  auto reader = vtkSmartPointer<vtkXMLUnstructuredGridReader>::New();
  reader->SetFileName(input_path.c_str());
  reader->Update();
  fs::path export_path = input_path.stem().string() + "_test.vtu";
  auto writer = vtkSmartPointer<vtkXMLUnstructuredGridWriter>::New();
  writer->SetFileName(export_path.c_str());
  writer->SetInputData(reader->GetOutput());
  writer->SetCompressorTypeToLZMA();
  writer->SetCompressionLevel(9);
  writer->Write();
  std::cout << fs::relative(input_path) << " -> " << fs::relative(export_path)
            << std::endl;
  return true;
}

std::vector<fs::path> get_file_list(std::vector<std::string> &list) {
  std::vector<fs::path> file_list;
  list.erase(list.begin());
  for (auto &i : list) {
    auto x = fs::path(i);
    if (x.extension() == ".vtu")
      file_list.push_back(x);
  }
  return file_list;
}

int main(int argc, char **argv) {
  std::vector<std::string> args(argv, argv + argc);
  if (argc == 1) {
    std::cout << "usage: ./vtu_compressor <files>" << std::endl;
    std::cout
        << "This program is made for compress vtu files by LZMA algorithm."
        << std::endl;
    std::cout << "Note: Files will be overwritten." << std::endl;
    std::cout << "Compression ratio is the best, but takes much time to do"
              << std::endl;
    std::exit(0);
  }
  auto list = get_file_list(args);

  for (auto item : list)
    converter(item);
}
