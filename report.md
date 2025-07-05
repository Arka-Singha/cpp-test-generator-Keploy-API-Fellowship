# Test Generation Report

## 🔧 Approach
- Used CodeLlama (via Ollama) for initial test generation and refinement.
- Prompts written in strict YAML format.
- Tests improved iteratively across 3 steps:
  1. Generate tests
  2. Refine tests
  3. Fix build errors

## 📊 Code Coverage
- Tool used: `lcov`
- Coverage report available at: `coverage_html/index.html`

## ✅ Features
- Redundant test removal
- Google Test integration
- Build error handling
- LLM-based refinement

## 🚀 Notes
- Model used: `codellama`
- Test structure conforms to Keploy architecture.
