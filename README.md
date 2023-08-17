# cs50x
This is my CS50x Final Project. 

## Pricey

### Video Demo: <https://youtu.be/09CZvdmaIn0>
---

### Description:

### Introduction
The world is growing fast and human minds are being replaced by computers. Recently I listened to ML podcast by CS50 and found that I'm really interested in Machine Learning. So I started exploring the depth of ML ocean, Deep Learning.
As my first project in ML, I decided to design a price prediction model to use former data of a ticker (symbol of company or currency in stock market) to predict price of different stock markets and currencies in the future.

### How the Algorithm works?
##### Decision Trees
A decision tree is a non-parametric supervised learning algorithm, which is utilized for both classification and regression tasks. It has a hierarchical, tree structure, which consists of a root node, branches, internal nodes and leaf nodes. (source: [IBM](https://www.ibm.com/topics/decision-trees "What is a Decision Tree?"))
##### Why Not Predicting future?
At first, we want to make sure how accurate the model is, so we will use the data from past few years except past month to train the model and predict past month worth and compare them to real market. There are some modifications which can be done to the model to get more accurate results. Whenever we get an accurate model, it can be shifted a month and predict future prices. (TODO in the FUTURE)

### How to use?
Before doing anything, make sure to run `pip install -r requirements.txt` to install required libraries.
Simply run `python main.py`, then enter a valid ticker (like "AAPL" for Apple Inc., "GOOGL" for Google Inc., "USD" for US Dollar, etc.) and hit enter. The model will use data from Yahoo Finance API of past few years, to train and predict the future price of the market.

![Project output](/Figure_1.png?raw=true "APPL")

In figure above, you can see the predicted vs real value for Apple Inc. stock.


### Technical
In this project, the analysis will be done on data with following packages:
- `yfinance` is used to communicate with Yahoo Finance API
- `numpy` will be a bridge between yahoo finance API and scikit-learn
- `scikit-learn` will train our ML model
- `matplotlib` to plot data and make the analyzed data visual

### Modification
You are welcome to edit the date range within the program by editing `start_date` and `end_date` to include more or less data.
The only limit (which is from server side) is that you can only make 2000 requests per hour per IP.
you may test the result by testing the neural network for any currency or company you want. But keep in mind to enter the formal ticker which can be easily found on the internet.

### TODO
I will try to improve the neural network and make it more efficient.
After having an efficient algorithm, it's time for future predictions.

I'm in the beginning of my long road in ML. There are a lot to do 👨🏻‍💻
---

HBD to me 🥳
Dec 26, 2022
Amin.
