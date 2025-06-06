import openai

def run_optimizer_llm(context):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or gpt-3.5-turbo for cheaper usage
        messages=[
            {"role": "system", "content": "You are a QA optimization assistant."},
            {"role": "user", "content": context}
        ]
    )
    return response["choices"][0]["message"]["content"]
