# transform.py
import pandas as pd

def analizar_semanas_con_gap(df: pd.DataFrame) -> pd.DataFrame:
    """
    Añade a df columnas:
      - gap_alcista: True si la apertura de la semana i fue mayor que el cierre de la semana i-1
      - cierre_alcista: True si el cierre de la semana i fue mayor que su apertura
      - etiqueta: clasificación combinada
    """
    df = df.copy()
    df["gap_alcista"] = False
    df["cierre_alcista"] = False
    df["etiqueta"] = "sin_gap_alcista"

    for i in range(1, len(df)):
        cierre_anterior = df.loc[i-1, "close"]
        apertura_actual = df.loc[i, "open"]
        cierre_actual = df.loc[i, "close"]

        gap = apertura_actual - cierre_anterior
        cierre_sube = cierre_actual > apertura_actual

        df.loc[i, "gap_alcista"] = gap > 0
        df.loc[i, "cierre_alcista"] = cierre_sube

        if gap > 0 and cierre_sube:
            df.loc[i, "etiqueta"] = "gap_alcista + cierre_alcista"
        elif gap > 0 and not cierre_sube:
            df.loc[i, "etiqueta"] = "gap_alcista + cierre_bajista"

    return df
