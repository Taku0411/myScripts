project(vtu2plot)
cmake_minimum_required(VERSION 3.24)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)


find_package(VTK)

add_executable(vtu2plot vtu2plot.cpp)

target_include_directories(vtu2plot PRIVATE ${VTK_INCLUDE_DIRS})
target_link_libraries(vtu2plot PRIVATE ${VTK_LIBRARIES})





