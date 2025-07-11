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

  const fill = document.querySelector(".progress-fill");

  if (fill) {
    const end = parseFloat(fill.getAttribute("data-end")) || 0;
    const start = parseFloat(localStorage.getItem("prevProgress")) || 0;

    fill.style.width = start + "%";

    requestAnimationFrame(() => {
      fill.style.transition = "width 1s ease-in-out";
      fill.style.width = end + "%";
    });

    localStorage.setItem("prevProgress", end);
  }
  });