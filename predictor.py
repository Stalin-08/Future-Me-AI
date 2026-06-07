def calculate_future_score(
    study_hours: int,
    sleep_hours: int,
    exercise_days: int,
    projects: int
) -> dict:

    career_score = (
        (study_hours * 12) +
        (projects * 15) +
        (exercise_days * 8)
    )

    career_score = min(career_score, 100)

    burnout_risk = max(
        0,
        100 - (
            sleep_hours * 10 +
            exercise_days * 2
        )
    )

    productivity_index = min(
        100,
        int(
            (study_hours * 8) +
            (projects * 12)
        )
    )

    learning_consistency = min(
        100,
        int(study_hours * 10)
    )

    if career_score >= 80:
        future_status = "High Growth"

        recommendation = (
            "Excellent progress. Continue building advanced projects."
        )

    elif career_score >= 50:
        future_status = "Moderate Growth"

        recommendation = (
            "Increase project work and maintain consistent study habits."
        )

    else:
        future_status = "Needs Improvement"

        recommendation = (
            "Focus on studying regularly and improving your routine."
        )

    return {
        "career_score": career_score,
        "burnout_risk": burnout_risk,
        "productivity_index": productivity_index,
        "learning_consistency": learning_consistency,
        "future_status": future_status,
        "recommendation": recommendation
    }