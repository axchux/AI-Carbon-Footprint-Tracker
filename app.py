from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_carbon(km, electricity):
    transport_emission = km * 0.21
    electricity_emission = electricity * 0.5
    return transport_emission + electricity_emission

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        km = float(request.form["km"])
        electricity = float(request.form["electricity"])
        result = calculate_carbon(km, electricity)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)