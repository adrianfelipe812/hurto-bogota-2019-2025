"""Une los archivos Excel anuales descargados desde la fuente oficial.

Uso: coloca los .xlsx de 2019–2025 en data/raw/ y ejecuta:
    python scripts/prepare_data.py
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUTPUT = ROOT / "Hurto_a_personas.csv"
REQUIRED = {"Año", "Mes", "Departamento", "Cantidad"}

files = sorted(RAW.glob("*.xlsx"))
if not files:
    raise SystemExit("No hay .xlsx en data/raw/. Descarga los archivos anuales de la Policía Nacional.")

frames = []
for path in files:
    frame = pd.read_excel(path, engine="openpyxl")
    missing = REQUIRED.difference(frame.columns)
    if missing:
        raise ValueError(f"{path.name}: faltan columnas requeridas: {sorted(missing)}")
    frame["__source_file"] = path.name
    frames.append(frame)

combined = pd.concat(frames, ignore_index=True)
combined.to_csv(OUTPUT, sep="|", index=False, encoding="utf-8-sig")
print(f"Datos combinados: {len(combined):,} filas, {len(files)} archivos -> {OUTPUT.name}")
