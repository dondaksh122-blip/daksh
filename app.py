from flask import Flask, request
import requests

app = Flask(__name__)

API_URL = "https://ansh-apis.is-dev.org/api/numinfofree"
API_KEY = "anurag"


@app.route("/")
def home():
    return "Running"


@app.route("/number")
def number():

    num = request.args.get("num")

    if not num:
        return "❌ Number missing"

    params = {
        "key": API_KEY,
        "num": num
    }

    try:
        r = requests.get(API_URL, params=params, timeout=20)
        data = r.json()
    except:
        return "❌ API Error"

    if not data.get("success"):
        return "❌ No Result"

    results = data.get("result", [])

    text = f"Response:\n✅ {len(results)} Results Found:\n\n"

    for i, res in enumerate(results, start=1):

        text += f"🔹 Result {i}:\n"
        text += f"📱 Mobile: {res.get('mobile','N/A')}\n"
        text += f"👤 Name: {res.get('name','N/A')}\n"
        text += f"👴 Father's Name: {res.get('father_name','N/A')}\n"
        text += f"🏠 Address: {res.get('address','N/A')}\n"
        text += f"🔴 Circle: {res.get('circle','N/A')}\n"
        text += f"🆔 Aadhar/ID: {res.get('id_number','N/A')}\n"
        text += f"📞 Alternate Mobile: {res.get('alt_mobile','N/A')}\n\n"

    text += "👤 Powered by @Mahakal1814"

    return text


if __name__ == "__main__":
    app.run()
