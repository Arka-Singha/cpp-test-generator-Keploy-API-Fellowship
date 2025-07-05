cmake_minimum_required(VERSION 3.10)
project(UnitTests)

# Enable testing and set C++ standard
enable_testing()
set(CMAKE_CXX_STANDARD 17)

# Enable code coverage flags only for GCC
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    message(STATUS "Enabling code coverage flags")
    add_compile_options(--coverage)
    link_libraries(gcov)
endif()

# Enable code coverage flags
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} --coverage")
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} --coverage")

# Download and setup GoogleTest & GoogleMock
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/refs/heads/main.zip
)
FetchContent_MakeAvailable(googletest)

# Collect test sources
set(TEST_SOURCES
  tests/test_main.cpp
)

# Optional: append generated test files if they exist
if(EXISTS "${CMAKE_SOURCE_DIR}/tests/test_persons_controller.cpp")
  list(APPEND TEST_SOURCES tests/test_persons_controller.cpp)
endif()

# Optional: Future files
# if(EXISTS "${CMAKE_SOURCE_DIR}/tests/test_jobs_controller.cpp")
#   list(APPEND TEST_SOURCES tests/test_jobs_controller.cpp)
# endif()

# Create the test executable
add_executable(test_runner
  ${TEST_SOURCES}
)

# Link GoogleTest and GoogleMock
target_link_libraries(test_runner
  gtest
  gtest_main
  gmock
  gmock_main
)

# Include test discovery
include(GoogleTest)
gtest_discover_tests(test_runner)

# Optional: Verbose test output
set(CMAKE_CTEST_ARGUMENTS "--output-on-failure")
