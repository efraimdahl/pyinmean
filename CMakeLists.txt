
cmake_minimum_required(VERSION 3.14)
project(pyinmean)

# Ensure you are using C++17
set(CMAKE_CXX_STANDARD 17)

# Add pybind11 as a subdirectory
add_subdirectory(pybind11)

# Add imacpp source files
set(IMACPP_SOURCES
    imacpp/MeterCollection.cpp
    imacpp/MetroWeights_Mazzola.cpp
    imacpp/Metrum.cpp
    imacpp/OnsetGroup_Memory.cpp
    imacpp/imacpp.cpp
)

# Create the static library (and enable PIC)
add_library(imacpp STATIC ${IMACPP_SOURCES})
set_target_properties(imacpp PROPERTIES POSITION_INDEPENDENT_CODE ON)

# Link the C++ standard library explicitly (optional, depending on your setup)
# target_link_libraries(imacpp PRIVATE stdc++)

# Specify include directories for imacpp
target_include_directories(imacpp PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/imacpp)

# Build the Python module
pybind11_add_module(pyinmean src/pyinmean/bindings.cpp)

# Link the imacpp library to the pyinmean Python module
target_link_libraries(pyinmean PRIVATE imacpp)

# Ensure Python extension is properly linked (optional)
# target_link_libraries(pyinmean PRIVATE Python::Python)
