// =========================
// AcademIx Loading Screen
// =========================

const uploadForm = document.getElementById("uploadForm");

if (uploadForm) {

    uploadForm.addEventListener("submit", function () {

        const overlay = document.getElementById("loadingOverlay");

        const loadingBar = document.getElementById("loadingBar");

        const loadingPercent = document.getElementById("loadingPercent");

        const loadingText = document.getElementById("loadingText");

        overlay.style.display = "flex";

        let progress = 0;

        const messages = [

            {
                progress: 0,
                text: "📄 Reading your PDF..."
            },

            {
                progress: 15,
                text: "🧠 Understanding your notes..."
            },

            {
                progress: 35,
                text: "📝 Generating Summary..."
            },

            {
                progress: 55,
                text: "🗂 Creating Flashcards..."
            },

            {
                progress: 75,
                text: "❓ Preparing Quiz..."
            },

            {
                progress: 92,
                text: "✨ Finalizing Study Material..."
            }

        ];

        loadingBar.style.width = "0%";
        loadingPercent.innerHTML = "0%";
        loadingText.innerHTML = messages[0].text;

        const interval = setInterval(function () {

            if (progress >= 98) {

                clearInterval(interval);

                return;

            }

            progress++;

            loadingBar.style.width = progress + "%";

            loadingPercent.innerHTML = progress + "%";

            for (let i = messages.length - 1; i >= 0; i--) {

                if (progress >= messages[i].progress) {

                    loadingText.innerHTML = messages[i].text;

                    break;

                }

            }

        }, 80);

    });

}

// =========================
// Dark Mode
// =========================

const themeToggle = document.getElementById("themeToggle");

// Load saved theme

if (localStorage.getItem("theme") === "dark") {

    document.body.classList.add("dark-mode");

    if (themeToggle) {

        themeToggle.innerHTML = "☀️ Light Mode";

    }

}

// Toggle theme

if (themeToggle) {

    themeToggle.addEventListener("click", function () {

        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {

            localStorage.setItem("theme", "dark");

            themeToggle.innerHTML = "☀️ Light Mode";

        }

        else {

            localStorage.setItem("theme", "light");

            themeToggle.innerHTML = "🌙 Dark Mode";

        }

    });

}