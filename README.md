# AI-Powered Smart Mirror 🪞

This project turns your Raspberry Pi 5 into an intelligent smart mirror that combines utility with innovation. It displays real-time weather, date, and time, and uses OpenAI’s GPT-4 to answer your voice or text-based questions, acting as a personal assistant embedded in a mirror. The interface is built with Flask and HTML/CSS and can be customized easily. You can also connect a PIR motion sensor to automatically wake the display when someone is nearby. It’s a perfect blend of AI, IoT, and user-centric design for modern home setups.


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
