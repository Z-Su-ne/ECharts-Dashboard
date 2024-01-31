const popupBtn = document.getElementById("popupBtn");
const popupOverlay = document.getElementById("popupOverlay");
const closeBtn = document.getElementById("closeBtn");

popupBtn.addEventListener("click", () => {
  popupOverlay.style.display = "flex";
  document.addEventListener("keydown", closePopupOnKey);
});

function closePopupOnKey(event) {
  if (event.key !== "Escape") {
    popupOverlay.style.display = "none";
    document.removeEventListener("keydown", closePopupOnKey);
  }
}

closeBtn.addEventListener("click", () => {
  popupOverlay.style.display = "none";
  document.removeEventListener("keydown", closePopupOnKey);
});



popupBtn.addEventListener("click", () => {
  popupOverlay.style.display = "block";
});

closeBtn.addEventListener("click", () => {
  popupOverlay.style.display = "none";
});
