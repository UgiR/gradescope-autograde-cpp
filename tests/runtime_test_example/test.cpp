#include <chrono>
#include "student_file.h"
#include "catch.hpp"

// you would most likely be testing a function in 'student_file.h'
int quadratic(int n) {
    int total = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            total += 1;
        }
    }
    return total;
}

TEST_CASE( "Test 01", "Example Project" )
{
    const int    N = 10000;
    const double RATIO = 2.25;

    auto t1 = std::chrono::high_resolution_clock::now();
    quadratic(N);
    auto t2 = std::chrono::high_resolution_clock::now();
    auto execTime_N = t2 - t1;

    t1 = std::chrono::high_resolution_clock::now();
    quadratic(2 * N);
    t2 = std::chrono::high_resolution_clock::now();
    auto execTime_2N = t2 - t1;

    double observed = execTime_2N / execTime_N;

    SECTION("Runtime complexity must be linear") {
        REQUIRE(observed <= RATIO);
    }




}