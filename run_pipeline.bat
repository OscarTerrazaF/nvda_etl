@echo off
REM — Moverse a la carpeta del propio .bat
cd /d %~dp0

REM — Activar el entorno virtual
call venv\Scripts\activate.bat

REM — Ejecutar el pipeline
python extract.py

echo.
echo --- Archivos generados en %cd% ---
dir /b nvda_semanal_2024.csv nvda_gaps_2024.csv nvda.db

pause
