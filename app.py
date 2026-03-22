from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":

        soil = request.form["soil"]
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        rainfall = float(request.form["rainfall"])

        # Soil to NPK + pH Mapping
        if soil == "Clayey Alluvial":
            N, P, K, ph = 70, 50, 45, 7.2

        elif soil == "Loamy Clayey Loam":
            N, P, K, ph = 65, 45, 40, 6.8

        elif soil == "Fertile Loam":
            N, P, K, ph = 75, 55, 50, 6.5

        elif soil == "Black Soil":
            N, P, K, ph = 60, 40, 35, 7.5

        elif soil == "Deep Loam":
            N, P, K, ph = 68, 48, 42, 6.7

        elif soil == "Acidic Loam":
            N, P, K, ph = 55, 35, 30, 5.8

        elif soil == "Well Drained Loam":
            N, P, K, ph = 62, 42, 38, 6.6

        elif soil == "Sandy Loam":
            N, P, K, ph = 45, 30, 25, 6.2

        elif soil == "Red Soil":
            N, P, K, ph = 50, 35, 30, 6.0

        elif soil == "Rich Loam":
            N, P, K, ph = 72, 52, 47, 6.9

        else:
            N, P, K, ph = 50, 30, 30, 6.5

        prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])

        return render_template("index.html",
                               prediction=prediction[0],
                               soil=soil,
                               N=N, P=P, K=K, ph=ph,
                               temperature=temperature,
                               humidity=humidity,
                               rainfall=rainfall)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
