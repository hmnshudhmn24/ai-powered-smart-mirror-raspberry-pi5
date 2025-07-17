# AI-Powered Smart Mirror 🪞

Turn your Raspberry Pi 5 into a futuristic smart mirror that shows the weather, date/time, and lets you ask questions using OpenAI's GPT model.

## 🔧 Features

- Real-time weather updates
- Live date and time
- Voice/text-based interaction with GPT-4
- Flask-powered backend
- Beautiful smart mirror UI (customizable)
- PIR sensor support (optional for screen activation)

## 🚀 Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/ai-powered-smart-mirror.git
cd ai-powered-smart-mirror
```

### 2. Install Dependencies

```bash
pip install flask openai requests
```

### 3. Set Environment Variables

```bash
export OPENAI_API_KEY=your_openai_key
export WEATHER_API_KEY=your_weatherapi_key
```

### 4. Run the Server

```bash
python app.py
```

Visit `http://<your_pi_ip>:5000` on your smart mirror display.

## 🧠 Using GPT-4

This project uses GPT-4 API. To ask something, click "Ask Mirror" and input your question. You’ll get an intelligent response in real-time.

## 🌐 Weather Data

Powered by [WeatherAPI.com](https://www.weatherapi.com/). Sign up and get a free API key.
