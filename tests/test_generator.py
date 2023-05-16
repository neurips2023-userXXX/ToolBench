from action_generator import RagGenerator


def test_rag_generator():
    generator = RagGenerator(
        client_name="openai",
        model_name="text-curie-001",
        context_dir="data/home_search/v0",
        max_output_token=256,
        top_k_api=10,
        top_k_example=3,
        query_template="Task: {query} (Answer in code only)\nActions:\n",
    )
    query = "Find a home with 12 bed above $961000 in Birmingham."
    prompt, text, error = generator.generate(query)
    assert error is None, error
    print(f"q: {prompt} \na:\n{text} \n ----- openai ----- \n")
