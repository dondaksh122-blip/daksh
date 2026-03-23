from flask import Flask, request
import requests

app = Flask(__name__)

API_URL = "http://87.120.165.68:17000/"
API_KEY = "f0c649e78aa843ff"


@app.route("/")
def home():
    return "API Running"


@app.route("/number")
def number():

    num = request.args.get("num")

    if not num:
        return "Number missing"

    params = {
        "api_key": API_KEY,
        "NumberInfo": num
    }

    r = requests.get(API_URL, params=params)
    data = r.json()

    if data["status"] != "success":
        return "❌ No Result"

    results = data["results"]

    text = f"✅ {len(results)} Results Found:\n\n"

    for i, res in enumerate(results, start=1):

        address = str(res.get("address", "N/A")).replace("!", " ")

        text += f"🔹 Result {i}:\n"
        text += f"📱 Mobile: {res.get('mobile','N/A')}\n"
        text += f"👤 Name: {res.get('name','N/A')}\n"
        text += f"👴 Father's Name: {res.get('father_name','N/A')}\n"
        text += f"🏠 Address: {address}\n"
        text += f"🔴 Circle: {res.get('circle','N/A')}\n"
        text += f"🆔 Aadhar/ID: {res.get('aadhar','N/A')}\n"
        text += f"📞 Alternate Mobile: {res.get('alternate_mobile','N/A')}\n\n"

    text += "👤 Powered by @Mahakal1814"

    return text


if __name__ == "__main__":
    app.run()
