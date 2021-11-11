# A Deep-Learning Chatbot

## Chatbot Features

Among other things, the bot can:

1. Chat with you
2. Help you with Google Search
3. Get the weather of any city
4. Get the top trending news in India at that moment
5. Get the top ten globally popular songs at that moment
6. Set a timer for you and so on

#### To check the complete list of capabilities and how to access them, type 'help' in the message box

## Dataset

The dataset used for training was self-populated and is stored as Intents.json in chatbot_codes. The data from this file was used to create the pickle files for words and classes. The pre-trained model with weights is available as mymodel.h5 in the same file.

## How to Use on your System

To run it locally on your system, follow these steps:

1. Clone this repository onto your system. On Command Prompt, run the following command:

```
git clone git@github.com:dash-anurag/Chat-Bot.git
```

2. Change your directory to Chatbot:

```
cd Chatbot
```

3. Make sure you have all the required libraries listed in requirements.txt. In case any of the libraries are missing, install them using pip. Type this command into your Command Prompt, replacing 'your-library-name' by the required library name:

```
pip install your-library-name
```

4. Then run the follwing commands to run the application:

```
export FLASK_APP=chatbot.py
flask run
```

5. Enter the url provided after running the previous commands into your web browser
