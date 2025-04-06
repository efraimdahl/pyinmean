#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // for std::vector support
#include "imacpp/onsets2ima.cpp"  // or a header file if available

namespace py = pybind11;

PYBIND11_MODULE(pyima, m) {
    m.def("get_normalized_ima", &getNormalizedIMA,
          py::arg("onsets"), py::arg("spectral") = false,
          R"pbdoc(
            Compute normalized IMA from onsets.

            Args:
                onsets (List[int]): List of onset indices.
                spectral (bool): Whether to compute spectral IMA.

            Returns:
                List[float]: Normalized IMA values.
          )pbdoc");
}
