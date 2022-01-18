# New matrix factorisation system, based on:
# https://github.com/kimjingu/nonnegfac-python


# Import required modules
import numpy as np
import pandas as pd
import openpyxl
from nonnegfac.nmf import NMF
nmf = NMF()


# Read Excel and output as NumPy array
wb = openpyxl.load_workbook('r.xlsx', read_only=True)
ws = wb.active

data_rows = []
for row in ws['I2':'ALU5168']:
    data_cols = []
    for cell in row:
        data_cols.append(cell.value)
    data_rows.append(data_cols)
reviews = pd.DataFrame(data_rows)

wb.close()

    
# Script
def main():
    # Save estimated matrix as CSV file
    mat_reviews = reviews
    mat_restaurant_lf, mat_user_lf, info = nmf.run(mat_reviews, 500, None, 20)
    filled = np.around(np.dot(mat_restaurant_lf, mat_user_lf.T), 3)
    np.savetxt('r_filled.csv', filled, delimiter=',', fmt='%f')
