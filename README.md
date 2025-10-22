# Weather Dashboard Backend

## Overview

This is the **backend** for a Weather Dashboard project. It is a Python-based FastAPI application that:

- Fetches live weather data from the **OpenWeather API**
- Stores weather information in a **MySQL database**
- Exposes endpoints that are consumed by a **React frontend**

This backend serves as the foundation for a full-stack weather dashboard, allowing the frontend to retrieve and display current weather data and historical records.

---

## Features

- **Fetch Weather Data**: Calls OpenWeather API to get temperature and humidity for a given city.
- **Store Data**: Inserts fetched weather data into a MySQL table for historical tracking.
- **API Endpoints**:
  - `GET /weather/{city}` → Fetches current weather for the given city and saves it to the database.
  - _(Optional)_ `GET /weather_history` → Returns recent weather records stored in the database.
- **Error Handling**: Returns meaningful error messages if the API key is invalid or the database operation fails.

---

## Technologies Used

- **Python 3**
- **FastAPI** (Web framework)
- **Requests** (HTTP client for API calls)
- **MySQL** (Database for storing weather data)
- **python-dotenv** (Load environment variables)
- **Uvicorn** (ASGI server)

---

## Setup & Installation

1. **Clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/weather-dashboard-backend.git
cd weather-dashboard-backend
```
