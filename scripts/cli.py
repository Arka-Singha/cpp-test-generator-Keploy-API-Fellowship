import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.generate.generate_tests import generate_tests
from scripts.generate.refine_tests import refine_tests
from scripts.fix.fix_build_errors import fix_build_errors

def main():
    print("Choose an option:")
    print("1. Generate tests")
    print("2. Refine tests")
    print("3. Fix build errors")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        generate_tests()
    elif choice == "2":
        refine_tests()
    elif choice == "3":
        fix_build_errors()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
