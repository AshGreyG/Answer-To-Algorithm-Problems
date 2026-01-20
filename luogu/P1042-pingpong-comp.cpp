#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <cmath>

int main() {
    std::vector<std::string> score;
    std::string input;
    while (std::cin >> input) {
        score.push_back(input);
        if (input.find('E') != std::string::npos) {
            break;
        }
    }

    std::vector<std::pair<unsigned int, unsigned int>> rate_11, rate_21;
    unsigned int 
        count_11_w = 0, count_11_l = 0, 
        count_21_w = 0, count_21_l = 0;

    for (const auto& line : score) {
        for (const auto ch : line) {
            if (ch == 'W') {
                ++count_11_w;
                ++count_21_w;
            } else if (ch == 'L') {
                ++count_11_l;
                ++count_21_l;
            } else if (ch == 'E') {
                break;
            }
            if (
                (count_11_w >= 11 || count_11_l >= 11) && 
                std::abs(static_cast<int>(count_11_w) - static_cast<int>(count_11_l)) >= 2
            ) {
                rate_11.emplace_back(count_11_w, count_11_l);
                count_11_w = count_11_l = 0;
            }
            if (
                (count_21_w >= 21 || count_21_l >= 21) && 
                std::abs(static_cast<int>(count_21_w) - static_cast<int>(count_21_l)) >= 2
            ) {
                rate_21.emplace_back(count_21_w, count_21_l);
                count_21_w = count_21_l = 0;
            }
            
        }
    }

    // end calculate rate
    //   1. notice that count_11(21)_w(l) may not be 0, so we need to deal with
    //     the last non-zero score rate
    //   2.notice that count_11(21)_w(l) are `unsigned int`, if we want to use 
    //     it to calculate `abs`, we must use `static_cast<int>`

    rate_11.emplace_back(count_11_w, count_11_l);
    rate_21.emplace_back(count_21_w, count_21_l);

    std::string output_11 = "", output_21 = "";
    for (const auto& rate : rate_11) {
        output_11 += std::to_string(rate.first)
                  +  ":"
                  +  std::to_string(rate.second)
                  +  "\n";
    }
    for (const auto& rate : rate_21) {
        output_21 += std::to_string(rate.first)
                  +  ":"
                  +  std::to_string(rate.second)
                  +  "\n";
    }
    std::cout << output_11 << "\n" << output_21;

    // end output

    return 0;
}