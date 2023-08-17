# Pricey

### Video Demo: [https://youtu.be/09CZvdmaIn0](https://youtu.be/09CZvdmaIn0)
---

### Description:

### Introduction
The world is advancing rapidly, and human minds are being augmented by computers. Inspired by an ML podcast by CS50, I delved into the realm of Machine Learning, particularly Deep Learning. My inaugural ML project involves crafting a price prediction model that leverages historical ticker data (symbols representing companies or currencies in the stock market) to forecast prices across various stock markets and currencies.

### How the Algorithm Works?
##### Decision Trees
A decision tree is a non-parametric supervised learning algorithm, adept at both classification and regression tasks. It features a hierarchical tree structure, comprising a root node, branches, internal nodes, and leaf nodes. (Source: [IBM](https://www.ibm.com/topics/decision-trees "What is a Decision Tree?"))

##### Evaluating Future Predictions
To ensure model accuracy, the initial phase involves training the model on past data from preceding years, excluding the most recent month. Predictions for the past month are then compared against actual market performance. Subsequent enhancements to the model can potentially facilitate future price predictions. (TODO in the FUTURE)

### How to Use?
Begin by running `pip install -r requirements.txt` to install necessary libraries. Execute `python main.py`, and input a valid ticker symbol (e.g., "AAPL" for Apple Inc., "GOOGL" for Google Inc., "USD" for US Dollar, etc.). The model will employ data from Yahoo Finance API spanning several years for training and predicting future market prices.

![Project Output](/Figure_1.png?raw=true "APPL")

In the figure above, a comparison between predicted and actual values for Apple Inc. stock is depicted.

### Technical
This project employs the following packages for data analysis:
- `yfinance` facilitates communication with Yahoo Finance API
- `numpy` serves as a bridge between Yahoo Finance API and scikit-learn
- `scikit-learn` is employed for training the ML model
- `matplotlib` is used for data visualization and analysis

### Modification
You are welcome to adjust the date range within the program by modifying `start_date` and `end_date` to encompass more or less data. It's important to note that there is a server-side limit of 2000 requests per hour per IP address. Feel free to test the neural network's performance on various currencies or companies, provided you input the proper ticker symbol readily available online.

### TODO
My journey in the field of ML is just beginning, and there is much to explore 👨🏻‍💻. I aim to refine and optimize the neural network, striving for increased efficiency. Once the algorithm is finely tuned, I look forward to venturing into future predictions.

Amin.

HBD to me 🥳
Dec 26, 2022
