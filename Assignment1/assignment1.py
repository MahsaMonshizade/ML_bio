import numpy as np
import pandas as pd
import scanpy as sc

print('hi')
ATAC_seq = sc.read_mtx(
    'GSE126074_AdBrainCortex_SNAREseq_chromatin.counts.mtx.gz')

cols_names = pd.read_csv('GSE126074_AdBrainCortex_SNAREseq_chromatin.barcodes.tsv.gz', header = None)
rows_names = pd.read_csv('GSE126074_AdBrainCortex_SNAREseq_chromatin.peaks.tsv.gz', header = None)

print('bye')
ATAC_df = ATAC_seq.to_df()
ATAC_df.columns = cols_names
ATAC_df.index = rows_names
print(ATAC_df)