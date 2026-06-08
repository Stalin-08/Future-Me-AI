def calculate_future_score(
    study_hours: int,
    sleep_hours: int,
    exercise_days: int,
    projects: int
) -> dict:
    """
    Calculate a user's future growth score based on study,
    sleep, exercise, and project activity.

    Parameters:
        study_hours (int): Hours studied per day
        sleep_hours (int): Hours slept per day
        exercise_days (int): Days exercised per week
        projects (int): Number of completed projects

    Returns:
        dict: Contains career score, burnout risk,
              productivity index, future status,
              and recommendation.
    """

    # Calculate career growth score
    career_score = (
        (study_hours * 12) +
        (projects * 15) +
        (exercise_days * 8)
    )

    # Limit score to a maximum of 100
    career_score = min(career_score, 100)

    # Calculate burnout risk
    # More sleep and exercise reduce burnout
    burnout_risk = max(
        0,
        100 - (
            sleep_hours * 10 +
            exercise_days * 2
        )
    )

    # Calculate productivity score
    productivity_index = min(
        100,
        int(
            (study_hours * 8) +
            (projects * 12)
        )
    )

    # Measure study consistency
    learning_consistency = min(
        100,
        int(study_hours * 10)
    )

    # Determine future status
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

    # Return all calculated values
    return {
        "career_score": career_score,
        "burnout_risk": burnout_risk,
        "productivity_index": productivity_index,
        "learning_consistency": learning_consistency,
        "future_status": future_status,
        "recommendation": recommendation
    }