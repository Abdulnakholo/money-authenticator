from flask import Flask, render_template , request
import pickle
import sklearn
app = Flask("__name__")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/" , methods = ["POST"])
def sub():
    if request.method == 'POST':
        model = pickle.load(open("models/model.pkl" , "rb"))
        variance = request.form["Variance"]
        skewness = request.form["Skewness"]
        curtosis = request.form["Curtosis"]
        entropy = request.form["Entropy"]

        variance = float(variance)
        skewness = float(skewness)
        curtosis = float(curtosis)
        entropy = float(curtosis)
        prediction = model.predict([[variance,skewness,curtosis,entropy]])

        if prediction == 1:
            prediction = "Original"

        else:
            prediction = "NOT original"


    return render_template("index.html" , prediction = prediction)

if __name__ == "__main__":
    app.run(debug = True)
