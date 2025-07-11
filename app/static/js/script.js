document.addEventListener("DOMContentLoaded", function () {
  // Maintain scroll on status toggle
  const forms = document.querySelectorAll(".status-form");
  forms.forEach((form) => {
    form.addEventListener("submit", function () {
      localStorage.setItem("scrollY", window.scrollY);
    });
  });

  const savedY = localStorage.getItem("scrollY");
  if (savedY !== null) {
    window.scrollTo(0, parseInt(savedY));
    localStorage.removeItem("scrollY");
  }

  // ✅ Smooth progress bar animation
const fill = document.querySelector(".progress-fill");
  if (fill) {
    const start = parseFloat(fill.getAttribute("data-start")) || 0;
    const end = parseFloat(fill.getAttribute("data-end")) || 0;

    // Start from previous value
    fill.style.width = start + "%";

    // Animate to current value
    requestAnimationFrame(() => {
      fill.style.width = end + "%";
    });
  }});