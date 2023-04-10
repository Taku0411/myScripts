#include "vtu2plot.hpp"

void read(const fs::path &path, int key) {

  // create reader
  vtkSmartPointer<vtkXMLUnstructuredGridReader> reader =
      vtkSmartPointer<vtkXMLUnstructuredGridReader>::New();
  reader->SetFileName(path.c_str());
  reader->Update();

  // get data array
  vtkSmartPointer<vtkUnstructuredGrid> grid = reader->GetOutput();

  // get number of nodes
  auto n_node = grid->GetNumberOfPoints();
  std::cout << n_node << std::endl;
  // if(key > n_node - 1)
  //{
  //	std::cout << "no such node ID: " << key << std::endl;
  //	std::cout << "maximum node ID: " << n_node << std::endl;
  //	std::abort();
  // }

  // create cell locator for fast search of the node ID
  vtkSmartPointer<vtkCellLocator> cellLocator =
      vtkSmartPointer<vtkCellLocator>::New();
  cellLocator->SetDataSet(grid);
  cellLocator->BuildLocator();

  // search for specified nodeID
  vtkIdType nodeId = key; // ID
  vtkIdType cellId;       // internal cell id
  double point[3];        // the coordinates of seached node is written this
  int subID;              // ???
  double dist2;           // the distance of key ID and result (0 means matched)

  grid->GetPoint(nodeId, point);
  cellLocator->FindClosestPoint(point, point, cellId, subID, dist2);

  std::cout << "nodeID: " << nodeId << std::endl;
  std::cout << "cellID: " << cellId << std::endl;
  std::cout << "point: " << point[0] << "," << point[1] << "," << point[2]
            << std::endl;
  std::cout << "subID: " << subID << std::endl;
  std::cout << "dist2: " << dist2 << std::endl;

	vtkSmartPointer<vtkDataArray> dataArray = grid->GetPointData()->GetArray("displacement");

	for(int i=0; i< dataArray->GetNumberOfTuples(); i++)
	{
		double tmp[3];
		dataArray->GetTuple(i, tmp);
		std::cout << tmp[0] << "," << tmp[1] << "," << tmp[2] << std::endl;
	}



}

int main(int argc, char **argv) {
  if (argc < 2) {
    std::cout << "Usage: ./vtu2plot <File patterns>" << std::endl;
    std::exit(0);
  }
  std::vector<fs::path> file_paths;

  // get all paths
  for (unsigned int i = 2; i < argc; i++) {
    file_paths.push_back(argv[i]);
  }
  // check file
  // for (auto &p : file_paths) {
  //  if (!fs::exists(p)) {
  //    std::cout << "no such file or directory: " << p << std::endl;
  //    std::exit(1);
  //  }
  //  std::cout << p << std::endl;
  //}

  std::cout << "file found" << std::endl;

  read(fs::path(argv[1]), std::stoi(argv[2]));
}
