# extract.py

import os
import argparse
import logging
import requests
import pandas as pd

from features import agregar_indicadores
from transform import analizar_semanas_con_gap
from load import load_to_sqlite

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_weekly_data(symbol: str, api_key: str, start_date: str = None, end_date: str = None) -> pd.DataFrame:
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": symbol,
        "interval": "1week",
        "apikey": api_key,
        "format": "JSON",
        "outputsize": 5000,
    }
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date

    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    if "values" not in data:
        raise ValueError(f"Unexpected API response: {data}")

    df = pd.DataFrame(data["values"])
    df["datetime"] = pd.to_datetime(df["datetime"])
    df = df.sort_values("datetime").reset_index(drop=True)
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df

def main():
    parser = argparse.ArgumentParser(
        description="Pipeline ETL para NVDA: extrae datos, añade indicadores, detecta gaps y carga en SQLite"
    )
    parser.add_argument("--api-key",   help="Your Twelve Data API key")
    parser.add_argument("--symbol",    default="NVDA",               help="Ticker symbol")
    parser.add_argument("--start",     default="1999-01-01",         help="Start date (YYYY-MM-DD)")
    parser.add_argument("--raw-csv",   default="nvda_semanal.csv",    help="Output CSV for raw weekly data")
    parser.add_argument("--gaps-csv",  default="nvda_gaps.csv",       help="Output CSV for gap analysis")
    parser.add_argument("--sqlite-db", default="nvda.db",            help="SQLite database file")
    parser.add_argument("--table",     default="gaps_nvda",          help="Table name in SQLite")
    args = parser.parse_args()

    api_key = args.api_key or os.getenv("TWELVEDATA_API_KEY")
    if not api_key:
        logging.error("Debe proporcionar --api-key o configurar TWELVEDATA_API_KEY")
        return

    logging.info(f"🔄 Iniciando pipeline para {args.symbol} desde {args.start}")

    # Paso 1: Extraer
    df = get_weekly_data(args.symbol, api_key, start_date=args.start)
    logging.info(f"Datos descargados: {len(df)} filas")

    # Paso 2: Enriquecer con indicadores
    df = agregar_indicadores(df)
    logging.info("Indicadores técnicos añadidos")

    # Paso 3: Detectar gaps
    df_gaps = analizar_semanas_con_gap(df)
    logging.info("Gaps analizados")

    # Paso 4: Guardar en CSV
    df.to_csv(args.raw_csv, index=False)
    df_gaps.to_csv(args.gaps_csv, index=False)
    logging.info(f"Archivos CSV guardados: {args.raw_csv}, {args.gaps_csv}")

    # Paso 5: Cargar en SQLite
    load_to_sqlite(df_gaps, db_path=args.sqlite_db, table_name=args.table)
    logging.info(f"Datos cargados en SQLite: {args.sqlite_db} (tabla {args.table})")

if __name__ == "__main__":
    main()

