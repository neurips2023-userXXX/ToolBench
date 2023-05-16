from action_generator.components.manifest_llm import ManifestLLM


def test_openai():
    query = "whys is grass green?"

    llm = ManifestLLM(
        client_name="openai", model_name="text-curie-001", max_output_token=256
    )
    text, error = llm.generate(query)
    assert error is None, error
    print(f"q: {query} \na:\n{text} \n ----- openai ----- \n")
