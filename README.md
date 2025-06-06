**Resume Parser**

A Python-based tool using spaCy for extracting structured information from resumes, designed to automate and streamline the process of resume analysis for recruitment, HR, and data processing applications.

# <a name="_4eo6j4cs72ur"></a>**Installation Steps**
## <a name="_sfyltky7dan2"></a>**Clone the Repository**
```
git clone https://github.com/sxm-003/resume-parser.git

cd resume-parser
```
## <a name="_803gouyi2fqf"></a>**Install Dependencies**
```
pip install -r requirements.txt
```

**Training Your Own Custom spaCy Model**

To train your own Named Entity Recognition (NER) model with spaCy, please follow the steps below for a streamlined and professional workflow:

**1. Data Preparation**

Begin by converting your annotated NER JSON data into spaCy's efficient DocBin format. Use the provided spacy_conversion.py program and insert training data in ./Data_batch or update the filepath in the spacy_conversion.py.
Run:

```

spacy_conversion.py

```

This ensures your data is in the optimal format for spaCy training.

**2. Training the Model**

A default configuration file, config.cfg, is included in the repository. This configuration is set up to train a transformer-based model (RoBERTa-base) utilizing GPU acceleration. Tune the hyperparameters within config.cfg to best suit your dataset and objectives.

To initiate training, use the following command:

```

python -m spacy train config.cfg --output ./model_output --paths.train ./Data_batch/train_data.spacy --paths.dev ./Data_batch/test_data.spacy

```

`    `--output ./model\_output: Directory where the trained model will be saved.

`    `--paths.train: Path to your training data in spaCy format.

`    `--paths.dev: Path to your validation (test) data in spaCy format.

**3. Data Availability**

For your convenience, pre-converted data in spaCy's format is already available within the Data\_batch directory:

`    `Training data: Data_batch/train_data.spacy

`    `Test/Development data: Data_batch/test_data.spacy

You can use these files directly for training and evaluation, or replace them with your own data as needed.

**4. Customization**

Feel free to modify the config.cfg file to adjust model architecture, optimizer settings, batch sizes, learning rates, or other hyperparameters to optimize performance for your specific use case.

**Parsing resume**

To extract structured information from resumes using the provided script, follow these steps:

**1. Prepare Your Resumes**

`    `Upload your resume files (PDF or text) into the ./resume directory.

`    `If a resume folder already exists, simply place your files there.

`    `You can also update the resume folder path in the code if you prefer a different location—the script allows you to specify or modify the input path as needed.

`    `Sample resumes are already provided in the resume folder for testing and demonstration purposes.

**2. Run the Parser**

Execute the following command in your terminal:

```

python resume_parser.py

```

The script will automatically process the resumes in the specified folder.

**3. Output**

After running the script, you will receive the parsed information as a Python dictionary, containing extracted details such as names, skills, education, and other details.


Kindly submit pull requests for you custom trained model on the model branch. 


