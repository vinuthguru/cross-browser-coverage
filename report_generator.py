def write_report(text, output_path="coverage_recommendation.md"):
    with open(output_path, "w") as f:
        f.write(text)
    print(f"Report written to {output_path}")

# --- cli.py ---
from context_builder import build_context_from_csv
from optimizer_model import run_optimizer_llm
from report_generator import write_report

if __name__ == "__main__":
    context = build_context_from_csv("example_data/usage.csv")
    result = run_optimizer_llm(context)
    write_report(result)
