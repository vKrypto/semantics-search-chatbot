import requests
from llms import OllamaRestAPIBasedGenerator
from main import search_query_and_create_context, search_title

q_map = {
    "How does message compression affect data flow in Kafka?": [
        "What impact does compressing messages have on Kafka's data throughput?",
        # "In Kafka, how does enabling compression influence data transmission?",
        # "How is Kafka’s data flow affected when message compression is used?",
        # "What are the effects of using message compression on Kafka performance?",
        # "Does compressing Kafka messages change how data moves through the system?",
        # "How does Kafka handle data flow when compression is turned on?",
        # "What role does message compression play in Kafka’s streaming efficiency?",
        # "How does enabling compression alter Kafka’s data pipeline behavior?",
        # "What changes occur in Kafka data transfer when compression is applied?",
        # "How does Kafka’s data handling differ with and without message compression?",
    ]
}

# for q, sep in q_map.items():
#     print(f"{q}:")
#     print("Possible resp:")
#     res = search_title(q)
#     tab = "\t"
#     print(f"Top 5 results for {q}:")
#     for i, r in enumerate(res):
#         score = r.get("_score", 0) - 1  #  converting to --> [-1, 1] scale again
#         r = r.get("_source", {})
#         print(tab, f"{i}. {r['title']}: Score: {score}")

#     for i, s in enumerate(sep):
#         res = search_title(s)
#         print(tab, f"Top 5 results for {s}:")
#         for i, r in enumerate(res):
#             score = r.get("_score", 0) - 1  #  converting to --> [-1, 1] scale again
#             r = r.get("_source", {})
#             print(tab, tab, f"{i}. {r['title']}: Score: {score}")

query = "I am getting multiple unusual messages how can I stop that?"
context = search_query_and_create_context(query)

ollama = OllamaRestAPIBasedGenerator("llama3.2", context)
queries = ["Hi", query, "Thanks", "can you tell me about my last question asked ?"]

for query in queries:
    print(f"Query: {query}")
    res, timings = ollama.get_response(query)
    print(f"Response: {res}")
    print(f"Timings: {timings}")
    print("-" * 20)
