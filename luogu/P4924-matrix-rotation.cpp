#include <iostream>
#include <vector>
#include <utility>

void rotate(
    std::vector<std::vector<int>>& vec,
    int x, 
    int y, 
    int r, 
    int dir
) {
    if (dir == 1) {
        for (int i = 1; i <= 2 * r; ++i) {
            for (int j = i + 1; j <= 2 * r + 1; ++j) {
                std::swap(vec[y - r - 1 + i][x - r - 1 + j], vec[y - r - 1 + j][x - r - 1 + i]);
            }
        }
        for (int i = y - r; i < y; ++i) {
            for (int j = x - r; j <= x + r; ++j) {
                std::swap(vec[i][j], vec[2 * y - i][j]);
            }
        }
    } else if (dir == 0) {
        for (int i = 1; i <= 2 * r ; ++i) {
            for (int j = 1; j <= 2 * r + 1 - i; ++j) {
                std::swap(vec[y - r - 1 + i][x - r - 1 + j], vec[y + r + 1 - j][x + r + 1 - i]);
            }
        }
        for (int i = y - r; i < y; ++i) {
            for (int j = x - r; j <= x + r; ++j) {
                std::swap(vec[i][j], vec[2 * y - i][j]);
            }
        }
    }
}

int main() {
    unsigned int n = 0, m = 0;
    std::cin >> n >> m;
    std::vector<std::vector<int>> matrix(n + 1, std::vector<int>(n + 1));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            matrix[i][j] = (i - 1) * n + j;
        }
    }
    for (int i = 1; i <= m; ++i) {
        int a, b, c, d;
        std::cin >> a >> b >> c >> d;
        rotate(matrix, b, a, c, d);
    }
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << "\n";
    }
    return 0;
}