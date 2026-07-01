"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
from pathlib import Path
def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    data_path = Path(__file__).resolve().parent.parent / "files" / "input"/ "tbl0.tsv"
    df = pd.read_csv(data_path, sep="\t")
    return len(df)

if __name__ == "__main__":
    print(pregunta_01())