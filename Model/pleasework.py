import numpy as np
import pickle
import json
from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

# Load model and column information
with open("../Model/columns.json", 'r') as col:
    columns = json.load(col)
    locations = columns['data_columns'][3:]

with open("../Model/bangalore_home_prices_model.pickle", 'rb') as m:
    model = pickle.load(m)


def process_inputs(location,bhk,sqft,bath):
    loc_index=locations.index(location.lower())
    x = np.zeros(len(columns['data_columns']))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(model.predict([x])[0], 2)

print(process_inputs("1st Phase JP Nagar",3,1000,3))
@app.get("/get_col")
def get_col():
    return locations


