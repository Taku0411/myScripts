project(vtk2vtu)
cmake_minimum_required(VERSION 3.24)
set(CMAKE_CXX_STANDARD 17)

find_package(OpenMP REQUIRED)
find_package(VTK)

add_executable(vtk2vtu vtk2vtu.cpp)

target_include_directories(vtk2vtu PRIVATE ${VTK_INCLUDE_DIRS})
target_link_libraries(vtk2vtu PRIVATE ${VTK_LIBRARIES} OpenMP::OpenMP_CXX)





