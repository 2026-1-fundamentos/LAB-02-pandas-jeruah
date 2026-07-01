"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
from pathlib import Path
import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """

    data_path = Path(__file__).resolve().parent.parent / "files" / "input"/ "tbl1.tsv"
    df = pd.read_csv(data_path, sep="\t")
    return sorted(df["c4"].str.upper().unique())

if __name__ == "__main__":
    print(pregunta_06())