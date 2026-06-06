def calculate_future_score(
    study_hours: int,
    sleep_hours: int,
    exercise_days: int,
    projects: int
) -> dict:

    career_score = (
        study_hours * 10 +
        projects * 15 +
        exercise_days * 5
    )

    burnout_risk = max(
        0,
        100 - (sleep_hours * 10)
    )

    if career_score >= 80:
        future_status = "High Growth"
    elif career_score >= 50:
        future_status = "Moderate Growth"
    else:
        future_status = "Needs Improvement"

    return {
        "career_score": career_score,
        "burnout_risk": burnout_risk,
        "future_status": future_status
    }