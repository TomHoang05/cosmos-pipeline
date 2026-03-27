import os
import time
import psycopg2
import requests
from dotenv import load_dotenv

# load .env variables into memory
load_dotenv()

def ingestion():

    # connect to postgres using .env variables
    try:
        connect = psycopg2.connect(
            host = os.getenv('DB_HOST'),
            database = os.getenv('DB_NAME'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            port = os.getenv('DB_PORT')
        )
        cursor = connect.cursor()
        print("connected to postgres")

        # create table in postgres if not exists
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS iss_position (
                id SERIAL PRIMARY KEY,
                longitude FLOAT,
                latitude FLOAT,
                timestamp INT,
                recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """ 
        )
        connect.commit()

        # record 5 values
        for i in range(5):
            #fetch data from api
            response = requests.get("http://api.open-notify.org/iss-now.json")
            data = response.json()

            longitude = data['iss_position']['longitude']
            latitude = data['iss_position']['latitude']
            timestamp = data['timestamp']

            # load data into table
            cursor.execute(""" 
                INSERT INTO iss_position (longitude, latitude, timestamp)
                VALUES (%s, %s, %s)
                """, (longitude, latitude, timestamp)
            )
            connect.commit()
            print("data recorded")
            time.sleep(15)
        cursor.close()
        connect.close()

    except Exception as e:
        print(f"Error: {e}")

# run ingestion
if __name__ == "__main__":
    ingestion()