document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const body = document.body;

    // Check stored theme preference
    if (localStorage.getItem("theme") === "light") {
        body.classList.add("light-theme");
        themeToggle.textContent = "🌞";
    }

    // Toggle theme on button click
    themeToggle.addEventListener("click", function () {
        body.classList.toggle("light-theme");

        // Save theme preference
        if (body.classList.contains("light-theme")) {
            localStorage.setItem("theme", "light");
            themeToggle.textContent = "🌞";
        } else {
            localStorage.setItem("theme", "dark");
            themeToggle.textContent = "🌙";
        }
    });
});
