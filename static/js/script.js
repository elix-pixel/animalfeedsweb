// Open/closed badge based on the shop's local time (Africa/Nairobi).
// Hours: Mon-Sat 7:00-19:00, Sun 8:00-17:00.
(function () {
  const badge = document.getElementById("open-status");
  if (!badge) return;

  function update() {
    const now = new Date();
    const day = now.getDay(); // 0 = Sunday
    const hour = now.getHours() + now.getMinutes() / 60;

    let openHour = 7, closeHour = 19;
    if (day === 0) {
      openHour = 8;
      closeHour = 17;
    }

    const isOpen = hour >= openHour && hour < closeHour;
    badge.textContent = isOpen ? "Open now" : "Closed now";
    badge.classList.toggle("closed", !isOpen);
  }
  update();
  setInterval(update, 60000);
})();

// Mobile menu toggle
(function () {
  const toggle = document.querySelector(".menu-toggle");
  const links = document.querySelector(".nav-links");
  if (!toggle || !links) return;
  toggle.addEventListener("click", () => {
    const open = links.style.display === "flex";
    links.style.display = open ? "none" : "flex";
    links.style.cssText += open
      ? ""
      : "position:absolute; top:100%; left:0; right:0; background:#F3EBDA; flex-direction:column; padding:20px 32px; border-bottom:1px solid rgba(43,33,24,0.14); gap:16px;";
  });
})();
