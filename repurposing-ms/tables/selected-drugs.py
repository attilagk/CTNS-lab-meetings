#!/usr/bin/env python3
import pandas as pd

df = pd.read_csv('selected-drugs.txt', sep='\t')
df.to_latex('selected-drugs.tex', index=False)
