from flask import Flask, jsonify, request, render_template
from predictor import calculate_future_score
from models import db, Prediction

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///futureme.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db.init_app(app)


# =========================
# FRONTEND ROUTES
# =========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/scenario-page")
def scenario_page():
    return render_template("scenario.html")


# =========================
# BACKEND API ROUTES
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    study = int(request.form["study"])
    sleep = int(request.form["sleep"])

    result = calculate_future_score(
        study_hours=study,
        sleep_hours=sleep,
        exercise_days=4,
        projects=2
    )

    return render_template(
    "result.html",
    result=result
)

@app.route("/scenario")
def scenario():

    current = calculate_future_score(
        study_hours=1,
        sleep_hours=5,
        exercise_days=1,
        projects=0
    )

    improved = calculate_future_score(
        study_hours=4,
        sleep_hours=8,
        exercise_days=5,
        projects=3
    )

    return jsonify({
        "current_future": current,
        "improved_future": improved
    })


@app.route("/history")
def history():

    predictions = Prediction.query.all()

    results = []

    for prediction in predictions:
        results.append({
            "id": prediction.id,
            "career_score": prediction.career_score,
            "burnout_risk": prediction.burnout_risk,
            "future_status": prediction.future_status
        })

    return jsonify(results)


@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.get_json()

    result = calculate_future_score(
        study_hours=data["study_hours"],
        sleep_hours=data["sleep_hours"],
        exercise_days=data["exercise_days"],
        projects=data["projects"]
    )

    prediction = Prediction(
        study_hours=data["study_hours"],
        sleep_hours=data["sleep_hours"],
        exercise_days=data["exercise_days"],
        projects=data["projects"],
        career_score=result["career_score"],
        burnout_risk=result["burnout_risk"],
        future_status=result["future_status"]
    )

    db.session.add(prediction)
    db.session.commit()

    return jsonify(result)


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)