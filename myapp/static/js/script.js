const Readmore = document.querySelector('#read-more-btn');
const Additional = document.querySelector('#additional');

Readmore.addEventListener('click', (e) => {
    e.preventDefault();

    if (Additional.style.display === 'none') {
        Additional.style.display = 'block';
        Readmore.textContent = 'Read less';
    } else {
        Additional.style.display = 'none';
        Readmore.textContent = 'Read more';
    }
});
