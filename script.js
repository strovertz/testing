// Função para abrir/fechar o menu lateral
function toggleMenu() {
  const menu = document.querySelector(".menu");
  menu.classList.toggle("menu-open");
}

// Função para ajustar a altura do iframe de acordo com a altura da janela
function adjustIframeHeight() {
  const iframe = document.querySelector("#map-iframe");
  iframe.style.height = window.innerHeight - 200 + "px";
}

// Chama a função para ajustar a altura do iframe inicialmente
adjustIframeHeight();

// Chama a função para ajustar a altura do iframe sempre que a janela for redimensionada
window.addEventListener("resize", adjustIframeHeight);

// Seleciona todos os links do menu
const menuLinks = document.querySelectorAll(".menu a");

// Adiciona um listener de clique em cada link do menu
menuLinks.forEach(function(link) {
  link.addEventListener("click", function(e) {
    // Previne o comportamento padrão do clique em um link
    e.preventDefault();

    // Remove a classe 'active' de todos os links do menu
    menuLinks.forEach(function(link) {
      link.classList.remove("active");
    });

    // Adiciona a classe 'active' ao link clicado
    this.classList.add("active");

    // Altera a URL do iframe para a URL do link clicado
    const href = this.getAttribute("href");
    const iframe = document.querySelector("#map-iframe");
    iframe.src = href;
  });
});
