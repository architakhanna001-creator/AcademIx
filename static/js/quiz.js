let quizSubmitted = false;

// =========================
// Quiz Progress
// =========================

function updateProgress() {

    const answered = document.querySelectorAll(
        '#quizForm input[type="radio"]:checked'
    ).length;

    const total = correctAnswers.length;

    const percentage = Math.round((answered / total) * 100);

    const bar = document.getElementById("quizProgress");

    if (bar) {

        bar.style.width = percentage + "%";

        bar.innerText = percentage + "%";

    }

}

// =========================
// Submit Quiz
// =========================

function submitQuiz() {

    if (quizSubmitted) {
        return;
    }

    quizSubmitted = true;

    let score = 0;

    const answers = document.querySelectorAll(".correct-answer");

    for (let i = 0; i < correctAnswers.length; i++) {

        const selected = document.querySelector(
            `input[name="q${i}"]:checked`
        );

        const options = document.querySelectorAll(
            `input[name="q${i}"]`
        );

        options.forEach(option => {

            option.disabled = true;

            if (option.value.trim() === correctAnswers[i].trim()) {

                option.parentElement.style.color = "#198754";
                option.parentElement.style.fontWeight = "bold";

            }

        });

        if (selected) {

            if (selected.value.trim() === correctAnswers[i].trim()) {

                score++;

            } else {

                selected.parentElement.style.color = "#dc3545";

            }

        }

        if (answers[i]) {
            answers[i].style.display = "block";
        }

    }

    const percentage = Math.round(
        (score / correctAnswers.length) * 100
    );

    const box = document.getElementById("scoreBox");

    box.style.display = "block";

    box.className = "alert alert-success mt-4";

    let message = "";

    if (percentage >= 90) {

        message = "🏆 Outstanding! Excellent work!";

        if (typeof confetti !== "undefined") {

            confetti({
                particleCount: 180,
                spread: 90,
                origin: { y: 0.6 }
            });

        }

    }

    else if (percentage >= 75) {

        message = "🎉 Great job! Keep it up!";

    }

    else if (percentage >= 50) {

        message = "👍 Good effort! Review the incorrect answers and try again.";

    }

    else {

        message = "📚 Keep studying! Practice makes perfect.";

    }

    box.innerHTML = `
        <h3>${message}</h3>
        <hr>
        <h4>Score: ${score} / ${correctAnswers.length}</h4>
        <h4>${percentage}%</h4>
    `;

    const submitButton = document.querySelector("#quizForm button");

    if (submitButton) {

        submitButton.disabled = true;

        submitButton.innerText = "Quiz Submitted";

    }

    const restartButton = document.getElementById("restartQuiz");

    if (restartButton) {

        restartButton.style.display = "inline-block";

    }

    window.scrollTo({

        top: document.body.scrollHeight,

        behavior: "smooth"

    });

}