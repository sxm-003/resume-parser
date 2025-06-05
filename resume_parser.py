import os
from pdfminer.high_level import extract_text
import spacy

# Path to the trained spaCy model, I will be updating the models
model_path = "/model/model1"

# Load the trained spaCy model for NER
try:
    nlp = spacy.load(model_path)
except Exception as err:   
    print(f"Unable to load the model: {err}")
    nlp = spacy.blank("en")  # fallback (will not extract entities)

def text_extractor(pdf_path):
    """
    Extracts text from a PDF file.
    Args:
        pdf_path: Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as err:
        print(f"Error in loading the resume at {pdf_path}: {err}")
        return ""

def identifier(text):
    """
    Identifies named entities in the given text using the loaded spaCy model.
    Args:
        text: Input text from which to extract entities.
    Returns:
        list: List of tuples (entity text, entity label) for entities with label "Skills" or "Name"or "Companies worked at" or "Designation" or "College Name" or "Graduation Year" or "Degree" oe "Email Address"
    """
    doc = nlp(text)
    # Extract entities and filter for only "Skills" or "Name" labels, can add other enitities specified above
    return [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ["Skills", "Name"]]

def parser(folder_path):
    """
    Parses all PDF files in a folder, extracts text, and identifies named entities.
    Args:
        folder_path: Path to the folder containing PDF files.
    Returns:
        dict: Dictionary mapping filenames to lists of identified entities.
    """
    results = {}
    for file in os.listdir(folder_path):
        # Only process PDF files
        if file.lower().endswith('.pdf'):
            file_path = os.path.join(folder_path, file)
            text = text_extractor(file_path)
            entities = identifier(text)
            results[file] = entities
    return results

# Path to the folder containing resume PDFs
folder_path = "/resume"

# Parse all resumes and extract specified entities
extracted_data = parser(folder_path)
print(extracted_data)

