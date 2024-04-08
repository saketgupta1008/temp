import pandas as pd
from sklearn.preprocessing import LabelBinarizer

# Load the dataset
df = pd.read_csv('path_to_your_file.csv')

# Assuming the CSV has two columns: 'query' and 'intent'
X = df['query']  # Features
y = df['intent']  # Labels

# Convert the 'intent' column to one-hot encoding
label_binarizer = LabelBinarizer()
Y_one_hot = label_binarizer.fit_transform(y)

# Now, Y_one_hot is a NumPy array containing the one-hot encoded labels
# If you need to reverse the one-hot encoding to check what labels correspond to:
intent_labels = label_binarizer.inverse_transform(Y_one_hot)

# Example: Print the first 5 queries and their one-hot encoded intents
print("Queries:", X[:5].to_list())
print("One-hot encoded intents:\n", Y_one_hot[:5])
