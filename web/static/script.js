// 1. Dark Mode Toggle
document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;

    if (darkModeToggle) {
        darkModeToggle.addEventListener("click", function () {
            body.classList.toggle("dark-mode");

            // Save preference in localStorage
            if (body.classList.contains("dark-mode")) {
                localStorage.setItem("theme", "dark");
                darkModeToggle.textContent = "☀️ Light Mode";
            } else {
                localStorage.setItem("theme", "light");
                darkModeToggle.textContent = "🌙 Dark Mode";
            }
        });

        // Load saved theme
        const savedTheme = localStorage.getItem("theme");
        if (savedTheme === "dark") {
            body.classList.add("dark-mode");
            darkModeToggle.textContent = "☀️ Light Mode";
        }
    }
});

// 2. Collapsible Sections
function initCollapsibles() {
    const collapsibles = document.querySelectorAll(".collapsible");

    collapsibles.forEach(collapsible => {
        collapsible.addEventListener("click", function () {
            this.classList.toggle("active");
            const content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
            } else {
                content.style.display = "block";
            }
        });
    });
}

// 3. Add Copy Button to Code Blocks
function addCopyButtons() {
    const preBlocks = document.querySelectorAll("pre");

    preBlocks.forEach(pre => {
        const copyBtn = document.createElement("button");
        copyBtn.className = "copy-btn";
        copyBtn.innerText = "📋 Copy";
        copyBtn.onclick = () => {
            const text = pre.innerText;
            navigator.clipboard.writeText(text).then(() => {
                copyBtn.innerText = "✅ Copied!";
                setTimeout(() => copyBtn.innerText = "📋 Copy", 2000);
            });
        };

        pre.parentNode.insertBefore(copyBtn, pre);
    });
}

// 4. Search Filter Functionality
function initSearchFilter() {
    const searchBox = document.getElementById("searchInput");
    if (!searchBox) return;

    searchBox.addEventListener("input", function () {
        const filter = searchBox.value.toLowerCase();
        const items = document.querySelectorAll(".report-item");

        items.forEach(item => {
            const text = item.textContent.toLowerCase();
            if (text.includes(filter)) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });
    });
}

// 5. Initialize on page load
document.addEventListener("DOMContentLoaded", function () {
    initCollapsibles();
    addCopyButtons();
    initSearchFilter();
});