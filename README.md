# NVDA ETL

**Pipeline ETL para procesamiento de datos de cotizaciones de NVIDIA**  
**ETL pipeline for processing NVIDIA quote data**

---

## 📋 Descripción / Description

**ES:** Este proyecto implementa un flujo de extracción, transformación y carga (ETL) en Python para procesar datos de cotizaciones de NVIDIA (NVDA). Está diseñado para leer múltiples archivos CSV, limpiar y normalizar los datos, generar archivos semanales y mensuales, y almacenarlos en una base de datos SQLite lista para análisis.

**EN:** This project implements an Extract, Transform, Load (ETL) pipeline in Python to process NVIDIA (NVDA) quote data. It is designed to read multiple CSV files, clean and normalize the data, generate weekly and monthly reports, and store them in a SQLite database ready for analysis.

---

## 📖 Tabla de Contenidos / Table of Contents

1. [Características / Features](#-características--features)
2. [Tecnologías / Technologies](#-tecnologías--technologies)
3. [Instalación / Installation](#-instalación--installation)
4. [Uso / Usage](#-uso--usage)
5. [Estructura del Proyecto / Project Structure](#-estructura-del-proyecto--project-structure)
6. [Contribuciones / Contributing](#-contribuciones--contributing)
7. [Licencia / License](#-licencia--license)
8. [Contacto / Contact](#-contacto--contact)

---

## ✨ Características / Features

- **ES:** Lectura de archivos CSV de cotizaciones diarias y semanales.  
  **EN:** Reads daily and weekly NVDA quote CSV files.
- **ES:** Limpieza de datos: eliminación de valores faltantes, corrección de formatos de fecha y normalización de campos.  
  **EN:** Data cleaning: removal of missing values, date format correction, and field normalization.
- **ES:** Transformaciones semanales y mensuales para análisis temporal.  
  **EN:** Weekly and monthly transformations for time-series analysis.
- **ES:** Carga automática en SQLite (`nvda.db`).  
  **EN:** Automatic load into SQLite (`nvda.db`).
- **ES:** Scripts de utilidad (`run_pipeline.bat`, `transform.py`, `load.py`).  
  **EN:** Utility scripts (`run_pipeline.bat`, `transform.py`, `load.py`).

---

## 🛠️ Tecnologías / Technologies

- **ES:** Python 3.x  
  **EN:** Python 3.x
- **ES:** pandas  
  **EN:** pandas
- **ES:** sqlite3 / SQLAlchemy (SQLite)  
  **EN:** sqlite3 / SQLAlchemy (SQLite)
- **ES:** Git / GitHub para control de versiones  
  **EN:** Git / GitHub for version control
- **ES:** Windows / Git Bash (o terminal equivalente)  
  **EN:** Windows / Git Bash (or equivalent terminal)

---

## ⚙️ Instalación / Installation

```bash
# Clonar el repositorio
git clone https://github.com/OscarTerrazaF/nvda_etl.git
cd nvda_etl

# Crear y activar entorno virtual
python -m venv venv
# Windows PowerShell
env\Scripts\Activate.ps1
# o Git Bash
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

---

## 🚀 Uso / Usage

1. **ES:** Ejecutá el pipeline completo con:  
   ```bash
   python extract.py
   python transform.py
   python load.py
   ```  
   **EN:** Run the full pipeline with:
   ```bash
   python extract.py
   python transform.py
   python load.py
   ```

2. **ES:** También podés usar el script por lotes en Windows:  
   ```bash
   ./run_pipeline.bat
   ```  
   **EN:** You can also use the Windows batch script:
   ```bash
   ./run_pipeline.bat
   ```

3. **ES:** Verificá la base de datos SQLite con tu herramienta favorita (DB Browser, SQLite CLI).  
   **EN:** Inspect the SQLite database using your favorite tool (DB Browser, SQLite CLI).

---

## 🗂️ Estructura del Proyecto / Project Structure

```
nvda_etl/
├── extract.py        # Extracción de datos (CSV)
├── transform.py      # Limpieza y transformaciones
├── load.py           # Carga en SQLite
├── run_pipeline.bat  # Script por lotes para Windows
├── requirements.txt  # Dependencias Python
├── nvda.db           # Base de datos SQLite (resultado)
├── csv/              # Carpeta con archivos CSV de ejemplo
└── venv/             # Entorno virtual (ignorarlo en Git)
```

---

## 🤝 Contribuciones / Contributing

**ES:** ¡Se aceptan pull requests! Para cambios grandes, abrí un issue primero describiendo lo que querés modificar.  
**EN:** Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 Licencia / License

**ES:** Este proyecto está bajo la licencia MIT.  
**EN:** This project is licensed under the MIT License.

---

## 📞 Contacto / Contact

- **ES:** Oscar Terraza Figueroa – [GitHub](https://github.com/OscarTerrazaF) – [Email](mailto:oscarterrazaf@gmail.com)  
  **EN:** Oscar Terraza Figueroa – [GitHub](https://github.com/OscarTerrazaF) – [Email](mailto:oscarterrazaf@gmail.com)