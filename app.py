from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running!"

if __name__ == "__main__":
    print("Starting Flask app...")  # Debug print
    app.run(debug=True)
