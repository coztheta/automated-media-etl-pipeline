
import pandas as pd
from pathlib import Path

# Use the folder containing this script
BASE_DIR = Path(__file__).resolve().parent
RAW_FILE = BASE_DIR / "raw_media.csv"
CLEAN_FILE = BASE_DIR / "clean_media.csv"


def transform_media():
    print("Starting data transformation...")

    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Cannot find {RAW_FILE}. Run extract.py first."
        )

    # Load raw data
    df = pd.read_csv(RAW_FILE)

    if df.empty:
        print("The raw file contains no records.")
        return

    print(f"Raw records: {len(df)}")

    # Normalize fields shared by movies and TV shows
    df["media_type"] = df.get(
        "media_type", pd.Series(index=df.index, dtype="object")
    )

    df["title"] = df.get(
        "title", pd.Series(index=df.index, dtype="object")
    ).fillna(
        df.get("name", pd.Series(index=df.index, dtype="object"))
    )

    df["release_date"] = df.get(
        "release_date", pd.Series(index=df.index, dtype="object")
    ).fillna(
        df.get("first_air_date", pd.Series(index=df.index, dtype="object"))
    )

    # Select and standardize useful columns
    columns = [
        "id",
        "media_type",
        "title",
        "release_date",
        "vote_average",
        "vote_count",
        "popularity",
        "original_language",
    ]

    for column in columns:
        if column not in df.columns:
            df[column] = pd.NA

    df = df[columns].copy()

    # Clean text columns
    df["title"] = df["title"].astype("string").str.strip()
    df["media_type"] = df["media_type"].fillna("unknown").astype("string")

    # Convert numeric columns safely
    for column in ["id", "vote_average", "vote_count", "popularity"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    # Parse dates and derive year
    df["release_date"] = pd.to_datetime(
        df["release_date"], errors="coerce"
    )
    df["release_year"] = df["release_date"].dt.year.astype("Int64")

    # Remove rows without a usable title or ID
    before = len(df)
    df = df.dropna(subset=["id", "title"])
    df = df[df["title"] != ""]
    df = df.drop_duplicates(subset=["id", "media_type"])

    # Save cleaned data
    df.to_csv(CLEAN_FILE, index=False, date_format="%Y-%m-%d")

    print(f"Clean records: {len(df)}")
    print(f"Rows removed: {before - len(df)}")
    print(f"File created: {CLEAN_FILE.name}")
    print("Transformation successful!")


if __name__ == "__main__":
    transform_media()
