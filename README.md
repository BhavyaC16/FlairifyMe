# FlairifyMe
FlairifyMe is a Reddit Flair Detector for [r/india](https://www.reddit.com/r/india/) subreddit, that takes a post's URL as user input and predicts the flair for the post using a model generated by Logistic Regression. The web-application is hosted on Heroku at [FlairifyMe(https://flairify-me.herokuapp.com/)](https://flairify-me.herokuapp.com/).

The web-application also offers visual content and temporal analysis of the collected data.

## Directory Structure
The project has been developed using Python and several of its libraries and frameworks:
- Scikit-learn
- PRAW
- NLTK
- Flask
- numpy
- pandas
- PyMongo

The scraped data is saved and loaded as a MongoDB instance.The web-application is based on Flask, and deployed using Heroku.

Following is the description of the files and folders in the repository:

- [Data](https://github.com/BhavyaC16/FlairifyMe/tree/master/Data): Contains CSV files with preprocessed scraped data, the MongoDB Collections and scripts for scraping, and preprocessing and analysing data.
- [Models](https://github.com/BhavyaC16/FlairifyMe/tree/master/Models): Contains the machine learning model used for predicting flairs.
- [Training](https://github.com/BhavyaC16/FlairifyMe/tree/master/Training): Contains the script for text-classification.
- [templates](https://github.com/BhavyaC16/FlairifyMe/tree/master/templates): Contains HTML scripts for the web-application
- [app.py](https://github.com/BhavyaC16/FlairifyMe/blob/master/app.py): Used to start up the Flask server.
- [flair_predictor.py](https://github.com/BhavyaC16/FlairifyMe/blob/master/flair_predictor.py): Module to accept a valid URL and predict the post's flair by loading the model.
- [nltk.txt](https://github.com/BhavyaC16/FlairifyMe/blob/master/nltk.txt): Contains NLTK library dependencies for deployment on Heroku.
- [requirements.txt](https://github.com/BhavyaC16/FlairifyMe/blob/master/requirements.txt): Contains all dependencies for the project

## Usage
The web-application allows the user to enter a r/india URL and displays the predicted flair for the submitted post. The user can view content and temporal analysis of the scraped data by clicking on the 'Post Analysis' button on the top right corner of the page.

To run on a local server:
1. Clone the repository
```
git clone https://github.com/BhavyaC16/FlairifyMe.git
```
2. Create a virtual environment
```
python3 -m venv FlairifyMe
source FlairifyMe/bin/activate
cd FlairifyMe/
```
3. Finally, install the project dependencies
```
pip3 install -r requirements.txt
```
4. To run the server, execute the following command
```
python3 app.py
```

## Approach 
### Data Scraping
The python library PRAW has been used to scrape data from the subreddit r/india, with a total of 3,156 posts for 13 different flairs. The number of posts scraped per flair are as follows:
![alt text](https://github.com/BhavyaC16/FlairifyMe/blob/master/Data/Scripts/DataSplit.png)

### Data preprocessing
The data has been preprocessed using the NLTK library. The following procedures have been executed on the title, body and comments to clean the data:
1. Tokenizing and removing symbols
2. Removing stopwords
3. Stemming

Two separate databases have been prepared and saved as a MongoDB instance for training: one with stemming, and the other without stemming, as it is said to reduce prediction accuracy in certain cases by sources.

### Training 
The data has been loaded from MongoDB to a pandas DataFrame and split into 80-20 Training-Testing sets using scikit-learn.
Each of the post features: Title, Body, Comments, Title+Comments and Title+Body+Comments were trained on three algorithms: Naive Bayes, Linear SVM and Logistic Regression, for both datasets(with and without stemming).

Following are the results, summarized as a table:

![alt text](https://github.com/BhavyaC16/FlairifyMe/blob/master/Training/AccuracyStats.png)

After going through the flair-wise and overall prediction accuracies, the model trained using Title+Body+Comments on non-Stemmed data, using Logistic Regresssion was chosen. 

### Flair Prediction
The saved model is loaded for predicting the flair once the post features (title, body and comments) have been cleaned using NLTK. The returned result is displayed on the web-application.

## Future Extension
I plan on adding the following features to the project:
1. Improving the prediction by training the model on user inputs.
2. Creating a developer API to use FlairifyMe
3. Automating the script to allow users to develop prediction model for any subreddit entered by them.

## Learnings
This task has been a great learning experience for me as it was my first time working with Machine Learning and Natural Language Processing, and with most of the tools like Heroku and MongoDB, as well as several libraries like scikit-learn, nltk, praw and Flask.

## References
1. [Scraping Reddit](https://www.datasciencecentral.com/profiles/blogs/scraping-reddit)
2. [Pre-processing Data](https://pythonhealthcare.org/2018/12/14/101-pre-processing-data-tokenization-stemming-and-removal-of-stop-words/)
3. [Training Machine Learning Models with MongoDB](https://www.mongodb.com/blog/post/training-machine-learning-models-with-mongodb)
4. [Text-Classification](https://medium.com/@ageitgey/text-classification-is-your-new-secret-weapon-7ca4fad15788)
5. [Bag of Words in NLP](https://medium.com/greyatom/an-introduction-to-bag-of-words-in-nlp-ac967d43b428)
6. [Choosing a Text-Classifier](https://nlp.stanford.edu/IR-book/html/htmledition/choosing-what-kind-of-classifier-to-use-1.html)
7. [Text-Classification using Scikit-learn](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
8. [Deploying Flask app to Heroku](https://github.com/datademofun/heroku-basic-flask)
