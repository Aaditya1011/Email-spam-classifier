Email/SMS Spam Classifier

This project is an email/SMS spam classification model built using the Multinomial Naive Bayes classifier from the scikit-learn library. It classifies messages as either "spam" or "valid" based on the content of the message. The model achieves an impressive accuracy of 97%.

Features
Data Preprocessing:

Converts input text to lowercase.
Removes punctuation and stopwords.
Applies stemming to improve feature consistency.
Model:

The classification model is built using the Multinomial Naive Bayes algorithm from scikit-learn.
Accuracy:

The model has an accuracy of 97% on the test dataset.
Deployment:

The model is deployed using Streamlit, a web application framework, allowing for easy interaction and testing of the model via a user-friendly interface.
Requirements
To run the project, you will need to have the following Python libraries installed:

scikit-learn: For the Naive Bayes classification.
nltk: For text processing (tokenization, stopwords removal, and stemming).
streamlit: For building the interactive deployment interface.
pandas: For handling the dataset.
numpy: For numerical operations.

1. You can install the required libraries by running:

pip install scikit-learn nltk streamlit pandas numpy

2. Installation and Setup

Clone the repository:
git clone https://github.com/yourusername/spam-classifier.git


Install the dependencies:
cd spam-classifier
pip install -r requirements.txt

Download the NLTK stopwords and punkt:
Open a Python shell and run the following commands to ensure the NLTK resources are available:

import nltk
nltk.download('stopwords')
nltk.download('punkt')
Run the Streamlit app:

In the terminal, run:

streamlit run app.py
This will launch a Streamlit web interface in your default browser, where you can input email or SMS messages to classify them as spam or valid.

How It Works
Text Preprocessing:

When a user inputs a message, the input is first converted to lowercase.
Punctuation marks and stopwords (common words such as "the", "and", etc.) are removed to focus on the important words.
Stemming is performed using the NLTK library to reduce words to their root form (e.g., "running" becomes "run").
Prediction:

The processed input text is passed through the trained Multinomial Naive Bayes model to predict whether the message is spam or valid.
The output is displayed to the user in the Streamlit interface.

Project Structure

spam-classifier/
│
├── models/
    ├── model.pkl        # Pretrained Naive Bayes model
    └──vectorizer.pkl    # vectorization model.
├── notebook             # jupyter notebook
├── app.py               # Streamlit app for deploying the model
├── requirements.txt     # List of required Python libraries
├── spam.csv        # Dataset of labeled spam and valid messages
└── README.md            # This file

Example Usage
Launch the app by running:

bash
Copy
streamlit run app.py
On the Streamlit interface, enter a message in the provided text box and click "Classify".

The model will return whether the message is classified as "Spam" or "Valid".

Model Performance
Accuracy: 97% on the test set.
Precision and Recall: High scores for both classes, making the model reliable for spam detection in real-world applications.
Contributing
Feel free to fork the repository and contribute to this project. If you encounter any issues or have suggestions for improvements, open an issue or submit a pull request.

License
This project is open-source and available under the MIT License.

