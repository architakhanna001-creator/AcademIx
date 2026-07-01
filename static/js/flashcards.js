// ======================================
// StudyMate AI - Flashcards
// ======================================

let currentCard = 0;

document.addEventListener("DOMContentLoaded", function () {

    // Stop if there are no flashcards
    if (typeof flashcards === "undefined" || flashcards.length === 0) {
        return;
    }

    const flashcard = document.getElementById("flashcard");
    const question = document.getElementById("flashcardQuestion");
    const answer = document.getElementById("flashcardAnswer");
    const counter = document.getElementById("cardCounter");

    const prevBtn = document.getElementById("prevCard");
    const nextBtn = document.getElementById("nextCard");

    // -------------------------
    // Load Card
    // -------------------------

    function loadCard(index) {

        question.textContent = flashcards[index].question;
        answer.textContent = flashcards[index].answer;

        counter.textContent =
            `Card ${index + 1} of ${flashcards.length}`;

        flashcard.classList.remove("flipped");

        prevBtn.disabled = (index === 0);
        nextBtn.disabled = (index === flashcards.length - 1);

    }

    // -------------------------
    // Flip Card
    // -------------------------

    flashcard.addEventListener("click", function () {

        flashcard.classList.toggle("flipped");

    });

    // -------------------------
    // Previous
    // -------------------------

    prevBtn.addEventListener("click", function () {

        if (currentCard > 0) {

            currentCard--;

            loadCard(currentCard);

        }

    });

    // -------------------------
    // Next
    // -------------------------

    nextBtn.addEventListener("click", function () {

        if (currentCard < flashcards.length - 1) {

            currentCard++;

            loadCard(currentCard);

        }

    });

    // -------------------------
    // Keyboard Support
    // -------------------------

    document.addEventListener("keydown", function (event) {

        if (event.key === "ArrowRight") {

            nextBtn.click();

        }

        if (event.key === "ArrowLeft") {

            prevBtn.click();

        }

        if (event.key === " ") {

            event.preventDefault();

            flashcard.click();

        }

    });

    // -------------------------
    // First Card
    // -------------------------

    loadCard(0);

});