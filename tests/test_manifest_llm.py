from action_generator.components.manifest_llm import ManifestLLM


def test_openai():
    query = "whys is grass green?"

    llm = ManifestLLM(
        client_name="openai", model_name="text-curie-001", max_output_token=256
    )
    text, error = llm.generate(query)
    assert error is None, error
    print(f"q: {query} \na:\n{text} \n ----- openai ----- \n")


# def test_openai():
#     query = "whys is grass green?"

#     llm = ManifestLLM(
#         client_name="huggingface",
#         model_name="facebook/opt-iml-30b",
#         client_connection="http://10.10.1.98:5000",
#         max_output_token=256,
#     )
#     text = llm.generate(query)
#     print(f"q: {query} \na:\n{text} \n ----- huggingface ----- \n")
