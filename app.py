from flask import Flask, jsonify
from predictor import calculate_future_score

app = Flask(__name__)

@app.route("/")
def home():
    return "FutureMe AI Backend Running"


@app.route("/predict")
def predict():

    result = calculate_future_score(
        study_hours=3,
        sleep_hours=8,
        exercise_days=4,
        projects=2
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)