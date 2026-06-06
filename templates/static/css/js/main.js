<script src="{{ url_for('static', filename='js/main.js') }}"></script>
async function predictFuture() {

    const data = {
        study_hours: Number(document.getElementById("study_hours").value),
        sleep_hours: Number(document.getElementById("sleep_hours").value),
        exercise_days: Number(document.getElementById("exercise_days").value),
        projects: Number(document.getElementById("projects").value)
    };

    const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML =
        `
        <h3>Prediction Result</h3>
        <p>Career Score: ${result.career_score}</p>
        <p>Burnout Risk: ${result.burnout_risk}</p>
        <p>Future Status: ${result.future_status}</p>
        `;
}