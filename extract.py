import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load .env from the same folder as this script
from pathlib import Path
load_dotenv(Path(__file__).resolve().parent / ".env", override=True)

def fetch_trending_media():
    api_key = os.getenv("TMDB_API_KEY")

    if not api_key:
        raise ValueError(
            "TMDB_API_KEY is missing. Check your .env file."
        )

    url = "https://api.themoviedb.org/3/trending/all/week"

    print("Connecting to TMDB API...")

    try:
        response = requests.get(
            url,
            params={
                "api_key": api_key,
                "language": "en-US",
                "page": 1
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])

        if not results:
            print("No trending media returned by the API.")
            return

        df = pd.DataFrame(results)

        df.to_csv("raw_media.csv", index=False)

        print("Extraction successful!")
        print(f"Records fetched: {len(df)}")
        print("File created: raw_media.csv")

    except requests.exceptions.Timeout:
        print("Request timed out. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print(f"TMDB HTTP error: {error}")
        print(response.text[:500])

    except requests.exceptions.RequestException as error:
        print(f"Network error: {error}")


if __name__ == "__main__":
    fetch_trending_media()



