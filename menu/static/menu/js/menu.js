const linksContainer = document.getElementById('menu-link-container')

const links = linksContainer.querySelectorAll('a');

links.forEach(link => link.addEventListener('click', (e) => {
    let activeLinks = linksContainer.querySelectorAll('.active');

    for (let i = 0; i < activeLinks.length; i++) {
        activeLinks[i].classList.toggle('active');
    }

    e.target.classList.add('active');
}));