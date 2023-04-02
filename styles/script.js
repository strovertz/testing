const nav = document.querySelector('nav');
const iframe = document.querySelector('iframe');

// Fecha o menu lateral quando um item é clicado
nav.addEventListener('click', () => {
  nav.classList.remove('open');
});

// Abre o menu lateral quando o botão é clicado
document.querySelector('.menu-btn').addEventListener('click', () => {
  nav.classList.toggle('open');
});

// Redimensiona o tamanho do iframe de acordo com a altura da janela
function resizeIframe() {
  iframe.style.height = `${window.innerHeight - iframe.offsetTop}px`;
}

window.addEventListener
