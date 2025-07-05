@echo off
mkdir build
cd build
cmake ..
cmake --build .
cd ..
build\Debug\test_runner.exe

REM Assuming lcov setup or using lcov in WSL:
REM Generate coverage info (adjust paths)
lcov --capture --directory . --output-file coverage.info
genhtml coverage.info --output-directory coverage_html

echo [INFO] Coverage report generated in coverage_html/
