from flask import Flask, render_template, request, jsonify
import openai
import requests
import datetime
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Delhi"

def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}"
    response = requests.get(url)
    data = response.json()
    return {
        "temp_c": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"],
        "icon": data["current"]["condition"]["icon"]
    }

def get_time():
    return datetime.datetime.now().strftime("%A, %d %B %Y %I:%M %p")

def ask_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

@app.route("/")
def index():
    weather = get_weather()
    time = get_time()
    return render_template("index.html", weather=weather, time=time)

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["prompt"]
    answer = ask_gpt(user_input)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)