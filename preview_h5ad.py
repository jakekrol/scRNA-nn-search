#!/usr/bin/env python3
import anndata as ad
import pandas as pd
import sys
import numpy as np

# Get the .h5ad file from command line arguments
h5ad_file = sys.argv[1]
type = sys.argv[2]
explore = sys.argv[3]

# Load the .h5ad file
adata = ad.read_h5ad(h5ad_file)

# Extract the data, index, and columns
if type == 'encode':
    matrix_data = adata.X
    index = adata.obs['barcodes']
    columns = adata.var['genes']

    # Check if matrix_data is a sparse matrix and convert to dense if necessary
    if not isinstance(matrix_data, np.ndarray):
        matrix_data = matrix_data.toarray()

    # Create the DataFrame
    df = pd.DataFrame(matrix_data, index=index, columns=columns)
if type == 'cxg':
    df = adata.to_df()
    df.columns = adata.var['gene_name']

# Print the head and shape of the DataFrame
print("Head of the DataFrame:")
print(df.head())

print("\nShape of the DataFrame:")
print(df.shape)

if explore:
    breakpoint()