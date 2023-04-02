// Função para inicializar o AOS (Animate on Scroll)
document.addEventListener('DOMContentLoaded', function() {
  AOS.init();
});

// Get the menu toggle element
const menuToggle = document.querySelector('.menu-toggle');

// Get the main navigation element
const mainNav = document.querySelector('.main-nav');

// Get the nav logo element
const navLogo = document.querySelector('.nav-logo');

// Get the nav links element
const navLinks = document.querySelector('.nav-links');

// Toggle the menu and logo when the menu toggle is clicked
menuToggle.addEventListener('click', function() {
  mainNav.classList.toggle('open');
  navLogo.classList.toggle('open');
});

// Seleciona todos os links do menu principal
const mainNavLinks = document.querySelectorAll('.main-nav a');

// Adiciona um listener de clique em cada link do menu principal
mainNavLinks.forEach(function(link) {
  link.addEventListener('click', function() {
    mainNav.classList.remove('open');
    navLogo.classList.remove('open');
  });
});

// Função para exibir imagens em um modal
const imagens = document.querySelectorAll(".portfolio-item img");
const modal = document.querySelector("#modal");
const modalImg = document.querySelector("#modal-img");

imagens.forEach(function(img) {
  img.addEventListener("click", function() {
    modalImg.src = img.src;
    modal.style.display = "block";
  });
});

modal.addEventListener("click", function() {
  modal.style.display = "none";
});

// Dados do portfólio
const portfolioData = [
  {
    image: 'images/portfolio-1.jpg',
    title: 'Project 1',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla malesuada eros quis enim lobortis.',
    link: '#'
  },
  {
    image: 'images/portfolio-2.jpg',
    title: 'Project 2',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla malesuada eros quis enim lobortis.',
    link: '#'
  },
  {
    image: 'images/portfolio-3.jpg',
    title: 'Project 3',
    description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla malesuada eros quis enim lobortis.',
    link: '#'
  }
];

// Função para gerar os itens do portfólio dinamicamente
function generatePortfolioItems() {
  const portfolioItems = document.querySelector('.portfolio-items');

  portfolioData.forEach(function(item) {
    const li = document.createElement('li');
    li.classList.add('portfolio-item');
    li.setAttribute('data-aos', 'fade-up');

    const img = document.createElement('img');
    img.src = item.image;
    img.alt = 'Portfolio Item';

    const overlay = document.createElement('div');
    overlay.classList.add('portfolio-item-overlay');

    const title = document.createElement('h3');
    title.classList.add('portfolio-item-title');
    title.innerText = item.title;

    const description = document.createElement('p');
    description.classList.add('portfolio-item-description');
    description.innerText = item.description;

    const link = document.createElement('a');
    link.classList.add('btn', 'btn-secondary');
    link.href = item.link;
    link.innerText = 'View Project';

    overlay.appendChild(title);
    overlay.appendChild(description);
    overlay.appendChild(link);

    li.appendChild(img);
    li.appendChild(overlay);

    portfolioItems.appendChild(li);
  });
}
// Chama a função para gerar os itens do portfólio dinamicamente
generatePortfolioItems();
