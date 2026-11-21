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

// Celular e tablet: botão "Menu" abre e fecha a lista do topo.
document.querySelectorAll(".menu-abrir").forEach(function (botao) {
  var topo = botao.closest(".topo");
  if (!topo) return;
  function define(aberto) {
    topo.classList.toggle("aberto", aberto);
    botao.setAttribute("aria-expanded", aberto ? "true" : "false");
  }
  botao.addEventListener("click", function () {
    define(!topo.classList.contains("aberto"));
  });
  // Fecha ao escolher um destino (inclusive âncoras da mesma página, como #contato).
  topo.querySelectorAll(".menu a").forEach(function (link) {
    link.addEventListener("click", function () { define(false); });
  });
  document.addEventListener("keydown", function (ev) {
    if (ev.key === "Escape" && topo.classList.contains("aberto")) {
      define(false);
      botao.focus();
    }
  });
});
