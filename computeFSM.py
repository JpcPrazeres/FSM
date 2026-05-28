import os
import sys
import pickle
import argparse

import pandas as pd
from sklearn import preprocessing as pre

sys.path.append(
    r"C:\Users\joaop\OneDrive\Desktop\CenasRFE\PYTHON\FSM\utils"
)

import utils as ut


# ==========================================================
# Utilities
# ==========================================================

def makeFolders(folder):
    if not os.path.isdir(folder):
        os.makedirs(folder)


# ==========================================================
# Arguments
# ==========================================================

parser = argparse.ArgumentParser()

parser.add_argument("-i","--Input",help="Feature file to evaluate (.xlsx)")
parser.add_argument("-m","--Model",default="FSM/Model/Ridge_6.sav",help="Saved model path")

args = parser.parse_args()


# ==========================================================
# Output folders
# ==========================================================

folderResults = os.path.join(os.getcwd(),"FSM")

makeFolders(folderResults)


# ==========================================================
# Load model
# ==========================================================

with open(args.Model, "rb") as f:
    model = pickle.load(f)

print("Loaded:", args.Model)


# ==========================================================
# Load features
# ==========================================================

eval_data = pd.read_excel(args.Input,engine="openpyxl")

X = eval_data.drop(["src", "ppc", "mos"],axis=1)

cols = X.columns


# ==========================================================
# Keep same normalization logic
# ==========================================================

scaler = pre.MinMaxScaler()
print(X)
X = scaler.fit_transform(X)

X = pd.DataFrame(X,columns=cols)


# ==========================================================
# Predict
# ==========================================================

y_pred = model.predict(X)
print(y_pred)

# ==========================================================
# Save results
# ==========================================================

df_pred = pd.DataFrame({"CloudName": eval_data["ppc"],"FSM": y_pred})

csv_out = os.path.join(folderResults,"FSM_Results.csv")

xlsx_out = os.path.join(folderResults,"FSM_Results.xlsx")

df_pred.to_csv(csv_out,index=False)

df_pred.to_excel(xlsx_out,index=False)

print("Saved:")
print(csv_out)
print(xlsx_out)
