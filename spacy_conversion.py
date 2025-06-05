import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import json
from sklearn.model_selection import train_test_split

# Load the training data from a JSON file
resume_info= json.load(open('train_data.json','r'))

def convert_spacyDocBin(log_file,data):
    """
    Converts raw text and annotation data into spaCy DocBin format for training.
    Args:
        log_file: File object for logging error messages.
        data: List of tuples, each containing text and its annotations.
    Returns:
        DocBin: A DocBin object containing processed documents.
    """
    #Initializing blank NLP pipeline English
    nlp = spacy.blank('en')
    db = DocBin()
    # Iterate over each text and its annotations with a progress bar using tqdm
    for text,annotation in tqdm(data):
        doc = nlp.make_doc(text)
        annotation = annotation['entities']

        ents =[]
        entity_indices = []
        # Process each entity annotation
        for start, end, label in annotation:
            # Check for overlapping entities
            skip_entity = False
            for index in range(start,end):
                if index in entity_indices:
                    skip_entity = True
                    break
            if skip_entity == True:
                continue

            # Mark these indices as used to prevent overlaps
            entity_indices = entity_indices + list(range(start,end))

            #Create a span for the entity in the Doc
            #Be sure to verify alignment_mode, Do not use 'compact' for the defualt submitted train_data.json
            try:
                span = doc.char_span(start,end, label = label, alignment_mode = 'strict')
            except:
                continue
            # If span creation failed, error is logged with the indices and text
            if span is None:
                err_data = str([start,end]) + "   " +str(text) + "\n"
                log_file.write(err_data)
            # Add the valid span to the list of entities
            else:
                ents.append(span)
        # Assign the entities to the Doc and add it to the DocBin
        try:
            doc.ents = ents
            db.add(doc)
        except:
            pass
    return db

#Splitting batch into train and test set
train, test = train_test_split(resume_info, test_size =0.1)


log_file = open('error.txt','w')
# Convert the train and test data spaCy DocBin format and save to disk
db = convert_spacyDocBin(log_file,train)
db.to_disk('train_data.spacy')

db= convert_spacyDocBin(log_file,test)
db.to_disk('test_data.spacy')

log_file.close()
