import os
import pandas as pd


# Returns a list of xlsx files in the /Data folder
def get_files():
    files = []
    for file in os.listdir("input"):
        if file.endswith(".xlsx"):
            files.append(file)
    return files


# Returns a pandas DF with the content of the file
def read_file(filename):
    res = pd.read_excel(f"input/{filename}")
    return res


# Returns a list of pandas DFs with the content of all the files
def read_files():
    files = get_files()
    res = {filename: read_file(filename) for filename in files}
    return res
