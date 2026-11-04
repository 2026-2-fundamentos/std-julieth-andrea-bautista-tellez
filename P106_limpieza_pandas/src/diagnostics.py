from pathlib import Path

import pandas as pd

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "submission" / "ventas.csv"


def main():
    df = pd.read_csv(INPUT_FILE)

    # Cambiar esta columna en cada diagnóstico
    column = "contact_email"

    series = df[column]

    print(f"\nColumna: {column}")
    print(f"Filas: {len(series)}")
    print(f"Valores faltantes: {series.isna().sum()}")
    print(f"Valores únicos: {series.nunique(dropna=True)}")

    print("\nValores encontrados:")

    for value in sorted(
        series.drop_duplicates().dropna(),
        key=lambda value: str(value).lower(),
    ):
        print(repr(value))


if __name__ == "__main__":
    main()