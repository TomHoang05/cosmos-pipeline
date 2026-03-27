# Space Data Pipeline

This is a personal project to practice building a data pipeline. I’m starting with a space theme because I like the topic and there are plenty of open APIs (NASA, ISS tracking, etc.) to pull from. 

The main goal is to move past writing isolated scripts and actually handle the flow of data from an external source into a local database.

## What this does
Right now, the project is in the early stages of **Ingestion**:
* Fetching real-time coordinates of the International Space Station.
* (Planned) Pulling daily images and metadata from NASA's APOD API.
* (Planned) Tracking Near Earth Objects (asteroids) and their flyby data.

## Project Structure
* `ingestion/`: Python scripts that handle the API calls.
* `data/`: A local folder for temporary CSV or JSON storage (ignored by Git).
* `sql/`: SQL scripts for creating tables and managing the Postgres schema.

## Tech Used
* **Python**: Using `requests` for APIs and `psycopg2` for database connection.
* **PostgreSQL**: Local database for storing the telemetry.
* **DBeaver**: For manual SQL testing and data viewing.
