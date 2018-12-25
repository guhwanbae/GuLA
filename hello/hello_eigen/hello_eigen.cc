#include <iostream>

#include <Eigen/Dense>

int main() {
    // Translation matrix, Homogeneous form.
    // Shift x by 0.25, y by 0.5
    Eigen::Matrix3d t_mat {};
    t_mat << 1, 0, 0.25,
           0, 1, 0.5,
           0, 0, 1;
    // Homogeneous point, [0 0 1]
    const Eigen::Vector3d p_vec {0, 0, 1};

    std::cout << "Translation matrix(Shift x by 0.25, y by 0.5), T =\n"
              << t_mat << "\n\n";
    std::cout << "The homogeneous 2D point, vector p =\n" << p_vec << "\n\n";
    std::cout << "The translated(shifted) point, T*p = \n"
              << t_mat * p_vec << "\n";

    return 0;
}
