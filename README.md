# 🏋️ Workout Tracker with Nutritionix & Sheety

This Python project allows users to input their workout activities in plain English (e.g., "ran 3 miles", "cycled for 20 minutes") and automatically logs the duration, type, and calories burned into a Google Sheet using the [Nutritionix API](https://www.nutritionix.com/business/api) and [Sheety](https://sheety.co/).

## 🚀 Features

- Natural language input for workouts
- Real-time calorie & duration calculation using Nutritionix
- Auto-logging to Google Sheets via Sheety API
- Timestamped workout entries
- Simple terminal-based interaction

## 📦 Requirements

- Python 3.x
- `requests` library (Install via `pip install requests`)

## 🔑 API Setup

1. **Nutritionix API**
   - Sign up at [Nutritionix](https://developer.nutritionix.com/)
   - Get your `APP_ID` and `API_KEY`

2. **Sheety API**
   - Go to [Sheety](https://sheety.co/)
   - Create a new project and spreadsheet
   - Get your unique Sheety API endpoint
   - Generate a Bearer token for authorization

## 🔧 Configuration

In the script, replace the placeholders with your actual values:

```python
API_KEY = "your_nutritionix_api_key"
APP_ID = "your_nutritionix_app_id"
SHEETY_URL = "https://api.sheety.co/your_project_id/your_username/workouts"
YOUR_TOKEN = "your_sheety_bearer_token"
