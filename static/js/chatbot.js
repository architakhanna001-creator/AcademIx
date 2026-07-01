// ----------------------------
// Get Elements
// ----------------------------
console.log("Chatbot JS Loaded");

const chatWindow = document.getElementById("chatWindow");
const questionInput = document.getElementById("questionInput");
const sendButton = document.getElementById("sendButton");

// Only run chatbot if elements exist
if (chatWindow && questionInput && sendButton) {

    // ----------------------------
    // Add Message Bubble
    // ----------------------------

    function addMessage(message, sender) {

        const bubble = document.createElement("div");

        bubble.className =
            sender === "user"
                ? "alert alert-primary text-end"
                : "alert alert-light";

        bubble.innerText = message;

        chatWindow.appendChild(bubble);

        chatWindow.scrollTop = chatWindow.scrollHeight;

    }

    // ----------------------------
    // Thinking Animation
    // ----------------------------

    function showThinking() {

        const bubble = document.createElement("div");

        bubble.className = "alert alert-warning";

        bubble.id = "thinkingBubble";

        bubble.innerHTML = "🤖 <i>StudyMate AI is thinking...</i>";

        chatWindow.appendChild(bubble);

        chatWindow.scrollTop = chatWindow.scrollHeight;

    }

    function removeThinking() {

        const bubble = document.getElementById("thinkingBubble");

        if (bubble) {

            bubble.remove();

        }

    }

    // ----------------------------
    // Send Question
    // ----------------------------

    async function sendQuestion() {

        const question = questionInput.value.trim();

        if (question === "") return;

        addMessage(question, "user");

        questionInput.value = "";

        showThinking();

        try {

            const response = await fetch("/ask-ai", {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    question: question

                })

            });

            const data = await response.json();

            removeThinking();

            addMessage(data.answer, "ai");

        }

        catch (error) {

            removeThinking();

            addMessage("❌ Something went wrong.", "ai");

            console.error(error);

        }

    }

    // ----------------------------
    // Send Button
    // ----------------------------

    sendButton.addEventListener("click", sendQuestion);

    // ----------------------------
    // Press Enter
    // ----------------------------

    questionInput.addEventListener("keydown", function (event) {

        if (event.key === "Enter" && !event.shiftKey) {

            event.preventDefault();

            sendQuestion();

        }

    });

    // ----------------------------
    // Example Question Buttons
    // ----------------------------

    const exampleButtons = document.querySelectorAll(".example-question");

    exampleButtons.forEach(button => {

        button.addEventListener("click", function () {

            questionInput.value = this.innerText;

            sendQuestion();

        });

    });

}