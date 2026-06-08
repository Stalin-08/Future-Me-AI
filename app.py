from flask import Flask, jsonify, request, render_template
from predictor import calculate_future_score
from models import db, Prediction

app = Flask(__name__)

# =========================
# Database Configuration
# =========================

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///futureme.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

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


# =========================
# PREDICTION ROUTE
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


# =========================
# SCENARIO SIMULATOR
# =========================

@app.route("/scenario", methods=["GET", "POST"])
def scenario():

    result = None

    if request.method == "POST":

        skill_a = int(request.form["skill_a"])
        exp_a = int(request.form["experience_a"])

        skill_b = int(request.form["skill_b"])
        exp_b = int(request.form["experience_b"])

        score_a = skill_a * 10 + exp_a * 5
        score_b = skill_b * 10 + exp_b * 5

        if score_a > score_b:
            result = "Scenario A has higher future potential"

        elif score_b > score_a:
            result = "Scenario B has higher future potential"

        else:
            result = "Both scenarios have equal future potential"

    return render_template(
        "scenario.html",
        result=result
    )


# =========================
# HISTORY API
# =========================

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


# =========================
# API ROUTE
# =========================

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


# =========================
# MAIN
# =========================

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True, port=5001)