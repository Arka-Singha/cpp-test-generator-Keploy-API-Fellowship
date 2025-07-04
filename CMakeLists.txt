cmake_minimum_required(VERSION 3.10)
project(UnitTests)

enable_testing()

# Download and link GoogleTest
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/heads/main.zip
)
FetchContent_MakeAvailable(googletest)

# Add source files
add_executable(test_runner
  tests/test_main.cpp
  input/main.cpp
)

target_link_libraries(test_runner gtest gtest_main)

include(GoogleTest)
gtest_discover_tests(test_runner)
