# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:02:34 2022
@author: THSMCODING
"""
import pandas as ps
import numpy as np
import glob as gl

sources= gl.glob("./source*.csv")
cols = ("jour_de_tirage","date_de_tirage","numero_chance","combinaison_gagnante_en_ordre_croissant")
    
def check_keys_uniform():
    correct_headers=[h for h in cols]
    nb_files=len(sources)
    df_temp=[]
    if nb_files == 0:
        print("Check your file number!", nb_files, " files found") 
        return None
    for s in sources:
        df_col_list = ps.read_csv(s, sep=';').columns.values.tolist()
        for k in correct_headers:
            if k not in df_col_list:
                print("Missing some keys in file:", s.upper(), "Missing column :", k.upper())
                return
        df_temp.append(ps.read_csv(s, sep=';' , header=0, usecols=list(correct_headers)))
    df=ps.concat(d for d in df_temp)
    print("All keys in correct_headers have been found in every source file.")     
    print("FINAL DATAFRAME :", df.head(5))
    return True

def main():
    check_keys_uniform()    
    
if __name__ == "__main__":
    main()
    
