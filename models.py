from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Prediction(db.Model):
    __tablename__ = "predictions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    study_hours = db.Column(
        db.Integer,
        nullable=False
    )

    sleep_hours = db.Column(
        db.Integer,
        nullable=False
    )

    exercise_days = db.Column(
        db.Integer,
        nullable=False
    )

    projects = db.Column(
        db.Integer,
        nullable=False
    )

    career_score = db.Column(
        db.Integer,
        nullable=False
    )

    burnout_risk = db.Column(
        db.Integer,
        nullable=False
    )

    future_status = db.Column(
        db.String(50),
        nullable=False
    )

    def __repr__(self):
        return f"<Prediction {self.id}>"