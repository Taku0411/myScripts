project(vtu_compression)
cmake_minimum_required(VERSION 3.24)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(VTK)

add_executable(vtu_compression vtk_compression.cpp)

target_include_directories(vtu_compression PRIVATE ${VTK_INCLUDE_DIRS})
target_link_libraries(vtu_compression PRIVATE ${VTK_LIBRARIES})





