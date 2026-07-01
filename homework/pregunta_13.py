"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from pathlib import Path
from unittest import result
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    data_path = Path(__file__).resolve().parent.parent / "files" / "input"/ "tbl0.tsv"
    data_path2 = Path(__file__).resolve().parent.parent / "files" / "input"/ "tbl2.tsv"
    df = pd.read_csv(data_path, sep="\t")
    df2 = pd.read_csv(data_path2, sep="\t")
    merged_df = pd.merge(df, df2, on='c0')
    result = merged_df.groupby('c1')['c5b'].sum()
    return result

if __name__ == "__main__":
    print(pregunta_13())