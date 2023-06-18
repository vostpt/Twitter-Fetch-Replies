# Twitter Fetch Replies

## What does this do?
This script asks for the tweet ID and the target account, and fetches the replies to that tweet. 

### Example
If you want to get the replies to [this tweet](https://twitter.com/NatGeo/status/1667743460990898176) from National Geographic

The **ID** will be **1667743460990898176** and the **account** will be **NatGeo**

## Purpose 

This script was developed as a part of a toolkit to classify tweets in diverse use cases, such as emergencies, disinformation, and online hate speech

## Running the Script 

1. Clone the repo
2. Create a *config.ini* file in the same folder with the following structure


[Twitter]

ConsumerKey = your_consumer_key

ConsumerSecret = your_consumer_secret

AccessToken = your_access_token

AccessSecret = your_access_secret

3. If you don't have virtualenv installed  run  **$ pip3 install virtualenv**
4. Go to the folder where the repo is, using Terminal
5. run **$ virtualenv --python=python3 .**
6. run **$ pip install -r requirements.txt**
7. run **$ python3 app.py**


