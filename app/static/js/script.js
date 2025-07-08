console.log("To-Do app JavaScript loaded")
document.addEventListener("DOMContentLoaded", function () {
  const forms = document.querySelectorAll(".status-form");

  forms.forEach((form) => {
    form.addEventListener("submit", function () {
      // Save scroll position before reload
      localStorage.setItem("scrollY", window.scrollY);
    });
  });

  // On page load, restore scroll position
  const savedY = localStorage.getItem("scrollY");
  if (savedY !== null) {
    window.scrollTo(0, parseInt(savedY));
    localStorage.removeItem("scrollY");
  }
});
