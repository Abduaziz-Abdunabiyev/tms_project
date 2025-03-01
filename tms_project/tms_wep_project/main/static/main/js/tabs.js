document.addEventListener("DOMContentLoaded", function() {
    const upperTabs = document.querySelectorAll(".upper-tab");
    const subTabContainers = document.querySelectorAll(".sub-tabs");

    upperTabs.forEach(tab => {
        tab.addEventListener("click", function(event) {
            event.preventDefault();

            // Remove active class from all upper tabs
            upperTabs.forEach(t => t.classList.remove("active"));
            this.classList.add("active");

            // Hide all lower tab containers
            subTabContainers.forEach(container => container.classList.remove("active"));

            // Show the selected lower tab section
            const targetId = this.getAttribute("data-target");
            document.getElementById(targetId).classList.add("active");
        });
    });
});
