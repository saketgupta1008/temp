import spacy
from spacy.pipeline.textcat import TextCategorizer
from spacy.tokens import DocBin
import random

# Load spaCy English model
nlp = spacy.blank("en")

# Define your categories
categories = ["category1", "category2"]

# Initialize TextCategorizer component
textcat = nlp.add_pipe("textcat", last=True)
for category in categories:
    textcat.add_label(category)

# Load and preprocess your data
train_data = [
    ("Text 1", {"cats": {"category1": 1, "category2": 0}}),
    ("Text 2", {"cats": {"category1": 0, "category2": 1}}),
    # Add more training data...
]

# Convert data to spaCy Doc objects
random.shuffle(train_data)  # Shuffle the training data
for text, annotations in train_data:
    doc = nlp.make_doc(text)
    example = (doc, annotations)
    textcat.update([example])

# Train the text categorizer
n_iter = 10
for i in range(n_iter):
    random.shuffle(train_data)
    for text, annotations in train_data:
        doc = nlp.make_doc(text)
        example = (doc, annotations)
        textcat.update([example])

# Save the trained model
output_dir = "/path/to/save/model"
nlp.to_disk(output_dir)

# Load the trained model
loaded_model = spacy.load(output_dir)

# Test the model
test_text = "Test text"
doc = loaded_model(test_text)
print(doc.cats)
