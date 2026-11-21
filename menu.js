// Abre/fecha a lista "Áreas de atuação" no clique, sem rolar a página.
document.querySelectorAll(".submenu").forEach(function (sub) {
  var botao = sub.querySelector(".submenu-botao");
  if (!botao) return;
  function define(aberto) {
    sub.classList.toggle("aberto", aberto);
    botao.setAttribute("aria-expanded", aberto ? "true" : "false");
  }
  botao.addEventListener("click", function () {
    define(!sub.classList.contains("aberto"));
  });
  document.addEventListener("click", function (ev) {
    if (!sub.contains(ev.target)) define(false);
  });
  sub.addEventListener("focusout", function (ev) {
    if (!sub.contains(ev.relatedTarget)) define(false);
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" && sub.classList.contains("aberto")) {
      define(false);
      botao.focus();
    }
  });
});
