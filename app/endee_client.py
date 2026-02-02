# # import requests

# # ENDEE_URL = "http://localhost:8080"
# # INDEX_NAME = "rag_documents"

# # # def add_vector(id, vector, metadata):
# # #     payload = {
# # #         "vectors": [
# # #             {
# # #                 "id": id,
# # #                 "values": vector,
# # #                 "metadata": metadata
# # #             }
# # #         ]
# # #     }

# # #     res = requests.post(
# # #         f"{ENDEE_URL}/indexes/{INDEX_NAME}/vectors",
# # #         json=payload,
# # #         headers={"Content-Type": "application/json"}
# # #     )

# # #     if res.status_code not in (200, 201):
# # #         raise Exception(f"Endee insert failed: {res.status_code} {res.text}")

# # def search_vector(query_vector, top_k=3):
# #     payload = {
# #         "vector": query_vector,
# #         "top_k": top_k
# #     }

# #     res = requests.post(
# #         f"{ENDEE_URL}/indexes/{INDEX_NAME}/search",
# #         json=payload
# #     )

# #     if res.status_code != 200:
# #         raise Exception(f"Endee search failed: {res.status_code} {res.text}")

# #     return res.json().get("results", [])

# import requests

# ENDEE_URL = "http://localhost:8080"
# INDEX_NAME = "rag_documents"

# def search_vector(query_vector, top_k=3):
#     payload = {
#         "vector": query_vector,
#         "k": top_k   # ⚠️ this version uses "k" not top_k/topK
#     }

#     res = requests.post(
#         f"{ENDEE_URL}/indexes/{INDEX_NAME}/search",  # correct base path
#         json=payload,
#     )

#     if res.status_code != 200:
#         raise Exception(f"Endee search failed: {res.status_code} {res.text}")

#     data = res.json()

#     # v0.1.0 returns "matches" not "results"
#     return data.get("matches", [])
