# features.py
import pandas as pd

def agregar_indicadores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Añade columnas de indicadores técnicos semanales usando sólo pandas:
      - EMA 10 y EMA 20
      - RSI 14
      - Bollinger Bands (20, 2)
    """
    df = df.copy()

    # EMA
    df["ema_10"] = df["close"].ewm(span=10, adjust=False).mean()
    df["ema_20"] = df["close"].ewm(span=20, adjust=False).mean()

    # RSI
    delta = df["close"].diff()
    gain = delta.clip(lower=0).rolling(window=14).mean()
    loss = (-delta.clip(upper=0)).rolling(window=14).mean()
    rs = gain / loss
    df["rsi_14"] = 100 - (100 / (1 + rs))

    # Bollinger Bands
    rolling_mean = df["close"].rolling(window=20).mean()
    rolling_std  = df["close"].rolling(window=20).std()
    df["bb_middle"] = rolling_mean
    df["bb_upper"]  = rolling_mean + 2 * rolling_std
    df["bb_lower"]  = rolling_mean - 2 * rolling_std

    return df
