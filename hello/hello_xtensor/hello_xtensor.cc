#include <iostream>

#include "xtensor/xarray.hpp"
#include "xtensor/xio.hpp"
#include "xtensor/xbuilder.hpp"
#include "xtensor-blas/xlinalg.hpp"

int main() {
    // Using template argument to explictly specify element data-type.
    // Mimicking the Numpy interface in python.
    // id_mat = numpy.eye(3)
    const xt::xarray<double> id_mat = xt::eye(3);
    const xt::xarray<double> vec_p {3.0, 4.0, 5.0};

    std::cout << "Identical matrix, I = \n" << id_mat << "\n";
    std::cout << "Point, vector p = " << vec_p << "\n";

    // Mimicking the Numpy interface in python.
    // res = numpy.dot(id_mat, vec_p)
    //
    // Many functions in the numpy.linalg(dot, svd...) is implemented
    // in xtensor-blas(xt::linalg namespace). To use this functonalities
    // link the numerical libraries, BLAS and LAPACK.
    auto res = xt::linalg::dot(id_mat, vec_p);
    std::cout << "I * p = " << res << "\n";

    return 0;
}
