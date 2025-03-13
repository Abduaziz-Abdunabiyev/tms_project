document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("dark-mode-toggle");
    const body = document.body;

    // Check if dark mode was enabled before
    if (localStorage.getItem("darkMode") === "enabled") {
        body.classList.add("dark-mode");
        console.log("Dark mode enabled from localStorage");
    }

    toggleButton.addEventListener("click", function () {
        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
            localStorage.setItem("darkMode", "disabled");
            console.log("Dark mode deactivated");
        } else {
            body.classList.add("dark-mode");
            localStorage.setItem("darkMode", "enabled");
            console.log("Dark mode activated");
        }
    });
});
