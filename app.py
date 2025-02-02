from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

if __name__ == "__main__":
    print("Starting Flask app...")  # Debug print
    # app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 10000))  # Use Render's provided port
    app.run(host="0.0.0.0", port=port, debug=True)
