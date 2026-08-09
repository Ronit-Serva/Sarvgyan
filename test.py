from tavily import TavilyClient

tavily_client = TavilyClient(api_key="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")
response = tavily_client.search("Who is Leo Messi?", include_answer=True)

print('Answer:', response['answer'])
