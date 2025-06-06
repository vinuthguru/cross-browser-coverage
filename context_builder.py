import pandas as pd

def build_context_from_csv(file_path):
    df = pd.read_csv(file_path)
    context = """You are an AI agent helping optimize cross-browser and device test coverage.
Given the following real user browser and device usage data, suggest the minimum browser/device combinations to cover at least 80% of the user sessions.

"""
    for _, row in df.iterrows():
        context += f"Browser: {row['browser']}, Device: {row['device']}, Sessions: {row['sessions']}\n"
    return context
