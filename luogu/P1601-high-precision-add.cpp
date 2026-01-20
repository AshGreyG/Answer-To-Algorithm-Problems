#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int main() {
    std::string a, b, max_str = "", min_str = "";
    std::cin >> a >> b;
    if (a == "0" && b == "0") {
        std::cout << "0";
        return 0;
    }
    std::vector<int> output(std::max(a.length(), b.length()) + 2, 0);
    if (a.length() >= b.length()) {
        std::for_each(a.rbegin(), a.rend(), [&] (char ch) { max_str += ch; });
        std::for_each(b.rbegin(), b.rend(), [&] (char ch) { min_str += ch; });
    } else {
        std::for_each(b.rbegin(), b.rend(), [&] (char ch) { max_str += ch; });
        std::for_each(a.rbegin(), a.rend(), [&] (char ch) { min_str += ch; });
    }
    unsigned int sum = 0;
    for (int i = 0, len = min_str.length(); i < len; ++i) {
        sum = max_str[i] - '0' + min_str[i] - '0' + output[i];
        output[i] = sum % 10;
        output[i + 1] += sum / 10;
    }
    for (int i = min_str.length(), m = max_str.length(); i < m; ++i) {
        sum = output[i] + max_str[i] - '0';
        output[i] = sum % 10;
        output[i + 1] += sum / 10;
    }
    bool check = false;
    std::string output_str = "";
    for (auto i = output.rbegin(); i <= output.rend() - 1; ++i) {
        if (*i != 0) check = true;
        if (check) output_str += std::to_string(*i);
    }
    std::cout << output_str;
    return 0;
}