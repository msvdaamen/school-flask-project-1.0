const modalEl = document.getElementById('movie-modal');

const movieModal = new bootstrap.Modal(modalEl, {});
const movieCards = document.getElementById('movies-container');

movieCards.addEventListener('click', (event) => {
    if (isCardClick(event.path)) {
        movieModal.show();
    }
});

function isCardClick(path) {
    for (const target of path) {
        if (target.classList && target.classList.contains('movie-card')) {
            return true;
        }
    }
    return null;
}
