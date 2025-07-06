# 🚀 C++ Unit Test Generator using TinyLlama | Keploy API Fellowship - Session 5

This project is built as part of the **Keploy API Fellowship - Session 5** and aims to automatically generate, refine, and fix unit tests for C++ applications using **LLMs like TinyLlama** via **Ollama**.

---

## 📌 Objective

To build a CLI tool that:

1. **Generates** unit tests for a given C++ project using a local LLM.
2. **Refines** those tests to remove duplicates and improve structure.
3. **Fixes** build errors automatically by feeding error logs back to the LLM.

---

## 🧩 Tech Stack

- **C++** (main application)
- **Google Test** (testing framework)
- **CMake** (build system)
- **Python + YAML** (LLM integration logic)
- **Ollama + TinyLlama** (Local LLM)

---

## 🏗️ Folder Structure

```
├── build/                 # Build output directory
├── input/                # Contains input C++ files
├── prompts/              # YAML prompts for generate/refine/fix steps
├── scripts/              # Python logic to run LLM for test generation
│   ├── generate/         # Generate & refine logic
│   └── fix/              # Fix build error logic
├── tests/                # Generated test files (GTest compatible)
├── CMakeLists.txt        # Build configuration
├── cli.py                # Command-line interface script
└── README.md             # This file
```

---

## ⚙️ How It Works

### Step 1️: Generate Tests

```bash
python scripts/cli.py
# Choose option: 1
```

✅ Output: `Tests generated successfully.`

### Step 2️: Refine Tests

```bash
python scripts/cli.py
# Choose option: 2
```

✅ Output: `Tests refined using LLM.`

### Step 3️: Fix Build Errors (if needed)

```bash
python scripts/cli.py
# Choose option: 3
```

✅ Output: `Build errors resolved using LLM.`

### Step 4️: Build & Run Tests

```bash
cd build
cmake ..
cmake --build .
ctest --output-on-failure
```

✅ Output:

```
100% tests passed, 0 tests failed out of 1
```

> 🔬 Test run includes:

```
Test #1: PersonTest.ToJsonOutput .......... Passed ✅
```

---

## 📊 Architecture Flow

> The system follows a strict prompt + feedback loop using YAML prompts:

### 🔄 Generation, Refinement, Fixing (Prompt + LLM Architecture)

1. **Initial Generation**

   - Input: `main.cpp` + `generate_prompt.yaml`
   - Output: GTest-style test file (e.g., `test_main.cpp`)

2. **Refinement**

   - Input: test file + `refine_prompt.yaml`
   - Output: Deduplicated and cleaned test

3. **Fix Build**

   - Input: Build logs + test + `fix_build_prompt.yaml`
   - Output: Error-resolved test file

4. **Final Execution**

   - Integrated with CMake + GoogleTest
   - Coverage optionally enabled using `--coverage`

>![image](https://github.com/user-attachments/assets/beef30cd-4421-47d3-ab34-c21064338d97)


---

## 🧠 Model Used

- **TinyLlama via Ollama** was used to run local inference and generate all test cases based on prompt YAMLs. It is suitable for limited RAM in local systems.

---

## 📄 Prompts Overview

Located in `/prompts`:

- `generate_prompt.yaml`: For test generation
- `refine_prompt.yaml`: For deduplication and cleanup
- `fix_build_prompt.yaml`: For fixing errors using compiler logs

---

## 📈 Coverage & Output

- ✅ Google Test used for execution
- ✅ `ctest` shows 100% pass rate on refined tests
- ⛳ LLM-generated tests matched function signatures in `main.cpp`
- ✅ No build or linker error after final test refinement

---

## 🎑️ Final Result Screenshots

> CLI Flow

> ![WhatsApp Image 2025-07-05 at 14 12 39_30b43687](https://github.com/user-attachments/assets/753d4554-1ea2-429a-998b-8b99d2fd61e1)



> CTest Passing Output

>![WhatsApp Image 2025-07-05 at 18 05 23_2f70e05b](https://github.com/user-attachments/assets/3a207f4a-deb6-49bd-b5e3-3bebb50a8937)

>

> Alternate Run + Debug

>![WhatsApp Image 2025-07-06 at 06 16 34_8168b344](https://github.com/user-attachments/assets/26250d0c-6241-43a1-be1b-0554553fb66e)
>![WhatsApp Image 2025-07-06 at 08 21 24_af62677a](https://github.com/user-attachments/assets/98bd9017-74db-4342-b40a-aa2fb6fe5ee2)


---

## ✅ Conclusion

This tool demonstrates how LLMs like TinyLlama can automatically generate, refine, and validate C++ unit tests locally using a strict prompt-based system. It can greatly accelerate unit test development in legacy or undocumented C++ codebases.

---

## 📢 Social Post (Optional)

> 🔗 https://www.linkedin.com/posts/arka-singha-99413225b_keployfellowship-aifortesting-opensource-activity-7347573418898149376-54gR?utm_source=share&utm_medium=member_desktop&rcm=ACoAAD_pwgABrdCtiHghxJ-0vZmAtmksMh7rwDY

---

