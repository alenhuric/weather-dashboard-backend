from fastapi import FastAPI, HTTPException
from app.weather import fetch_weather
from app.database import get_db_connection

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city: str):
    try:
        data = fetch_weather(city)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather_data (city, temperature, humidity) VALUES (%s, %s, %s)",
            (data["city"], data["temperature"], data["humidity"])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return data
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=str(e))
