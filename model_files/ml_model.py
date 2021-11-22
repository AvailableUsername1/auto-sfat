#Copy all useful stuff about the model from jupter notebook
#Dependencies
import pandas as pd
import numpy as np


def price_prediction(data, model):
    #Doing some cleaning
    del data["submit"]
    data["Year"] = int(data["Year"])
    data["Engine"] = int(data["Engine"])
    data["Distance"] = int(data["Distance"])


    if type(data) == dict:
        if (type(data) == list):
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame(data, index=[0])
    else:
        df = data

    #need to add a new column with all 0's because im dumb
    dumbPrice = pd.Series([0 for price in range(df.shape[0])], name="Price")
    fullDF = df.join(dumbPrice)


    prediction = model.predict(fullDF)
    return prediction