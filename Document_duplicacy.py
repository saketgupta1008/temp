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





import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Normalize embeddings for all dataframes
def normalize_embeddings(df):
    embeddings = np.stack(df['embedding'])
    normalized = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)
    df['embedding'] = list(normalized)
    return df

# Step 2: Function to compare embeddings and find duplicates
def find_duplicates(vector_dbs):
    results = []
    num_dbs = len(vector_dbs)

    # Normalize embeddings for all databases
    for i in range(num_dbs):
        vector_dbs[i] = normalize_embeddings(vector_dbs[i])

    # Compare all databases pairwise
    for i in range(num_dbs):
        for j in range(i, num_dbs):  # Compare each database with itself and others
            db1 = vector_dbs[i]
            db2 = vector_dbs[j]

            for idx1, row1 in db1.iterrows():
                for idx2, row2 in db2.iterrows():
                    sim = cosine_similarity([row1['embedding']], [row2['embedding']])[0][0]
                    if sim == 1.0:  # Exact match
                        results.append({
                            "id": row1['id'],
                            "embedding": row1['embedding'],
                            "chunk": row1['chunk'],
                            "document_source": row1['document_source'],
                            "last_chunk_accessed": row1['last_chunk_accessed'],
                            "frequency": row1['frequency'],
                            "dormancy": row1['dormancy'],
                            "duplicate": True,
                            "source_category": f"Duplicate between vector_db{i+1} and vector_db{j+1}"
                        })

    # Step 3: Handle Non-Duplicates
    # Add non-duplicate entries
    for i in range(num_dbs):
        db = vector_dbs[i]
        for idx, row in db.iterrows():
            if not any(row["id"] == res["id"] for res in results):
                results.append({
                    "id": row['id'],
                    "embedding": row['embedding'],
                    "chunk": row['chunk'],
                    "document_source": row['document_source'],
                    "last_chunk_accessed": row['last_chunk_accessed'],
                    "frequency": row['frequency'],
                    "dormancy": row['dormancy'],
                    "duplicate": False,
                    "source_category": f"vector_db{i+1}"
                })

    # Step 4: Convert Results to DataFrame
    return pd.DataFrame(results)

# Example usage
# Create sample dataframes representing vector databases
vector_dbs = []
for i in range(3):  # Simulating 3 vector databases
    df = pd.DataFrame({
        "id": [f"doc{i*3+j}" for j in range(3)],
        "embedding": [np.random.rand(3).tolist() for _ in range(3)],  # Random embeddings
        "chunk": [f"chunk{i*3+j}" for j in range(3)],
        "document_source": [f"source{i+1}" for _ in range(3)],
        "last_chunk_accessed": [f"2024-11-17 10:{30+j}:00" for j in range(3)],
        "frequency": [10+j for j in range(3)],
        "dormancy": [5+j for j in range(3)],
    })
    vector_dbs.append(df)

# Find duplicates and generate results
final_df = find_duplicates(vector_dbs)

# View the final dataframe
print(final_df)

