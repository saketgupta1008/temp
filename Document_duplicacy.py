import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Example dataframes
# df1 = pd.DataFrame(columns=["id", "embedding", "chunk", "document_source", "last_chunk_accessed", "frequency", "dormancy"])
# df2 = pd.DataFrame(columns=["id", "embedding", "chunk", "document_source", "last_chunk_accessed", "frequency", "dormancy"])

# Step 1: Normalize Embeddings (Optional for better precision)
def normalize_embeddings(df):
    embeddings = np.stack(df['embedding'])
    normalized = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    df['embedding'] = list(normalized)
    return df

df1 = normalize_embeddings(df1)
df2 = normalize_embeddings(df2)

# Step 2: Initialize Results
results = []

# Step 3: Compare Embeddings Across Dataframes
for idx1, row1 in df1.iterrows():
    for idx2, row2 in df2.iterrows():
        sim = cosine_similarity([row1['embedding']], [row2['embedding']])[0][0]
        if sim == 1.0:  # Exact match
            results.append({
                "id_df1": row1['id'],
                "id_df2": row2['id'],
                "embedding": row1['embedding'],  # Embedding from either source
                "chunk": row1['chunk'],
                "document_source": row1['document_source'],
                "last_chunk_accessed": row1['last_chunk_accessed'],
                "frequency": row1['frequency'],
                "dormancy": row1['dormancy'],
                "duplicate": True
            })

# Step 4: Handle Non-Duplicates
# Add remaining non-duplicate entries
for idx1, row1 in df1.iterrows():
    if not any(r["id_df1"] == row1["id"] for r in results):
        results.append({
            "id_df1": row1['id'],
            "id_df2": None,
            "embedding": row1['embedding'],
            "chunk": row1['chunk'],
            "document_source": row1['document_source'],
            "last_chunk_accessed": row1['last_chunk_accessed'],
            "frequency": row1['frequency'],
            "dormancy": row1['dormancy'],
            "duplicate": False
        })

for idx2, row2 in df2.iterrows():
    if not any(r["id_df2"] == row2["id"] for r in results):
        results.append({
            "id_df1": None,
            "id_df2": row2['id'],
            "embedding": row2['embedding'],
            "chunk": row2['chunk'],
            "document_source": row2['document_source'],
            "last_chunk_accessed": row2['last_chunk_accessed'],
            "frequency": row2['frequency'],
            "dormancy": row2['dormancy'],
            "duplicate": False
        })

# Step 5: Convert Results to DataFrame
final_df = pd.DataFrame(results)

# View the final dataframe
print(final_df)
