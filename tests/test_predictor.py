import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from predictor import calculate_future_score


def test_high_growth():

    result = calculate_future_score(
        study_hours=4,
        sleep_hours=8,
        exercise_days=5,
        projects=3
    )

    assert result["future_status"] == "High Growth"


def test_needs_improvement():

    result = calculate_future_score(
        study_hours=1,
        sleep_hours=5,
        exercise_days=1,
        projects=0
    )

    assert result["future_status"] == "Needs Improvement"