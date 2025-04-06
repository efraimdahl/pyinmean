cmake_minimum_required(VERSION 3.14)
project(pyinmean)

set(CMAKE_CXX_STANDARD 17)

add_subdirectory(extern/pybind11)

# Add imacpp source files
set(IMACPP_SOURCES
    imacpp/MeterCollection.cpp
    imacpp/MetroWeights_Mazzola.cpp
    imacpp/Metrum.cpp
    imacpp/OnsetGroup_Memory.cpp
    imacpp/imacpp.cpp
)

# Create the static library and enable PIC
add_library(imacpp STATIC ${IMACPP_SOURCES})
set_target_properties(imacpp PROPERTIES POSITION_INDEPENDENT_CODE ON)

include_directories(imacpp)

# Build the Python module
pybind11_add_module(pyinmean bindings.cpp)
target_link_libraries(pyinmean PRIVATE imacpp)
