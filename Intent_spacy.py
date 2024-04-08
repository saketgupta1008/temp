import spacy
from spacy.tokens import DocBin
from spacy.training.example import Example
import random
from spacy.util import minibatch
import json

# Load your dataset
# Assuming a JSON format where each entry is {'text': 'Your text here', 'intent': 'IntentName'}
def load_data(file_path):
    texts, labels = [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for entry in data:
            texts.append(entry['text'])
            labels.append({"cats": {entry['intent']: 1}})
    return texts, labels

# Convert the dataset to spaCy's binary format
def convert_to_spacy_format(texts, labels, nlp):
    db = DocBin()
    for text, label in zip(texts, labels):
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, label)
        db.add(example.reference)
    return db

# Load your training and validation data
train_texts, train_labels = load_data('path/to/your/training_data.json')
valid_texts, valid_labels = load_data('path/to/your/validation_data.json')

# Load a blank or pre-existing spaCy model
nlp = spacy.blank("en")  # Use "en_core_web_sm" or other model for pre-existing models

# Add the text classifier to the pipeline
textcat = nlp.add_pipe("textcat", last=True)

# Add your labels to textcat
for label in set(label['cats'].keys() for label in train_labels):
    textcat.add_label(label)

# Convert the training and validation data to spaCy's binary format
train_data = convert_to_spacy_format(train_texts, train_labels, nlp)
valid_data = convert_to_spacy_format(valid_texts, valid_labels, nlp)

# Save the converted training and validation data
train_data.to_disk("./train.spacy")
valid_data.to_disk("./valid.spacy")

# Configuration for the training
config_str = """
[training]
train = "./train.spacy"
dev = "./valid.spacy"
"""

# Start the training
spacy.cli.train(config_str, overrides={"paths.train": "./train.spacy", "paths.dev": "./valid.spacy"})

# Save the trained model
nlp.to_disk("./trained_intent_model")

# Load the saved model and test it
nlp2 = spacy.load("./trained_intent_model")
test_text = "Sample text for intent classification"
doc = nlp2(test_text)
print(f"Predicted intent: {doc.cats}")
