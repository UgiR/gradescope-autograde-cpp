// This file is included in order for the example test to run.
// You would likely be testing a submitted file, such as ../student_file.h

#include <iostream>

void fn() {
    if (true) {
        if (true) {
            if (true) {
                if (true) {
                    std::cout << "this code smells." << std::endl;
                }
            }
        }
    }
}

int main() {}