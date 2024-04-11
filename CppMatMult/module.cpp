#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <vector>
using namespace std;


std::vector<std::vector<int>> multiplyMatrices(const std::vector<std::vector<int>>& A, const std::vector<std::vector<int>>& B) {
    int rowsA = A.size();
    int colsA = A[0].size();
    int rowsB = B.size();
    int colsB = B[0].size();

    // Check if matrices can be multiplied (columns of A must equal rows of B)
    if (colsA != rowsB) {
        throw std::invalid_argument("Matrices cannot be multiplied. Columns of first matrix must equal rows of second matrix.");
    }

    // Create a result matrix with appropriate dimensions
    std::vector<std::vector<int>> C(rowsA, std::vector<int>(colsB, 0));

    // Perform matrix multiplication
    for (int i = 0; i < rowsA; ++i) {
        for (int k = 0; k < colsB; ++k) {
            for (int j = 0; j < colsA; ++j) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return C;
}



namespace py = pybind11;

PYBIND11_MODULE(CppMatMult, m) {
    m.def("fast_multiply", &multiplyMatrices, R"pbdoc( Multiply Two Matrices very fast using two 2D arrays)pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = VERSION_INFO;
#else
    m.attr("__version__") = "dev";
#endif
}