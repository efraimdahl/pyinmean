cmake_minimum_required(VERSION 3.14)
project(pyima)

set(CMAKE_CXX_STANDARD 17)

# Add pybind11 as a subdirectory (or however you've included it)
add_subdirectory(pybind11)

# Add imacpp source files
set(IMACPP_SOURCES
    imacpp/MeterCollection.cpp
    imacpp/MetroWeights_Mazzola.cpp
    imacpp/Metrum.cpp
    imacpp/OnsetGroup_Memory.cpp
    imacpp/imacpp.cpp  # Add other necessary files if any
)

# Create the static library for imacpp
add_library(imacpp STATIC ${IMACPP_SOURCES})
# Explicitly set position independent code for imacpp
set_target_properties(imacpp PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Include imacpp headers
include_directories(imacpp)

# Create the Python module and link imacpp
pybind11_add_module(pyima bindings.cpp)
target_link_libraries(pyima PRIVATE imacpp)

