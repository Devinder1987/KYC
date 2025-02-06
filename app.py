from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins
@app.route("/")
def home():
    return "Flask API is running!"

@app.route("/price-compare")
def price_compare():
    return [
        {
            "Uline_name":"Anti-Static",
            "packaging_name":"Anti-static",
            "uline_price":90.9090909091,
            "packaging_price":95.99
        },
        {
            "Uline_name":"Boxes, Corrugated",
            "packaging_name":"boxes - corrugated",
            "uline_price":80.0,
            "packaging_price":77.48
        },
        {
            "Uline_name":"Bubble Cushioning",
            "packaging_name":"bubble, foam & cushioning",
            "uline_price":71.4285714286,
            "packaging_price":74.52
        },
        {
            "Uline_name":"Edge Protectors",
            "packaging_name":"edge protectors",
            "uline_price":86.6666666667,
            "packaging_price":78.7
        },
        {
            "Uline_name":"Envelopes and Mailers",
            "packaging_name":"envelopes & mailers",
            "uline_price":75.0,
            "packaging_price":81.65
        },
        {
            "Uline_name":"Facilities Maintenance",
            "packaging_name":"facilities maintenance",
            "uline_price":90.9090909091,
            "packaging_price":98.02
        },
        {
            "Uline_name":"Gloves",
            "packaging_name":"gloves",
            "uline_price":83.3333333333,
            "packaging_price":90.59
        },
        {
            "Uline_name":"Janitorial Supplies",
            "packaging_name":"janitorial supplies",
            "uline_price":89.4736842105,
            "packaging_price":92.46
        },
        {
            "Uline_name":"Labels",
            "packaging_name":"labels",
            "uline_price":83.3333333333,
            "packaging_price":75.18
        },
        {
            "Uline_name":"Markers \/ Stencils",
            "packaging_name":"markers & stencils",
            "uline_price":83.3333333333,
            "packaging_price":87.32
        },
        {
            "Uline_name":"Material Handling",
            "packaging_name":"material handling",
            "uline_price":88.2352941176,
            "packaging_price":85.44
        },
        {
            "Uline_name":"Moving Boxes and Supplies",
            "packaging_name":"moving boxes & supplies",
            "uline_price":75.0,
            "packaging_price":77.28
        },
        {
            "Uline_name":"Packing List Envelopes",
            "packaging_name":"packing list envelopes",
            "uline_price":86.3636363636,
            "packaging_price":89.85
        },
        {
            "Uline_name":"Retail",
            "packaging_name":"retail",
            "uline_price":83.3333333333,
            "packaging_price":75.78
        },
        {
            "Uline_name":"Safety Products",
            "packaging_name":"safety products",
            "uline_price":86.6666666667,
            "packaging_price":93.58
        },
        {
            "Uline_name":"Strapping",
            "packaging_name":"strapping",
            "uline_price":88.8888888889,
            "packaging_price":80.87
        },
        {
            "Uline_name":"Tags",
            "packaging_name":"tags",
            "uline_price":75.0,
            "packaging_price":75.23
        },
        {
            "Uline_name":"Tape",
            "packaging_name":"tape",
            "uline_price":75.0,
            "packaging_price":73.82
        },
        {
            "Uline_name":"Warehouse Equipment \/ Supplies",
            "packaging_name":"warehouse supplies",
            "uline_price":66.6666666667,
            "packaging_price":67.99
        }
    ]

if __name__ == "__main__":
    print("Starting Flask app...")  # Debug print
    # app.run(debug=True)
    import os
    port = int(os.environ.get("PORT", 10000))  # Use Render's provided port
    app.run(host="0.0.0.0", port=port, debug=True)
