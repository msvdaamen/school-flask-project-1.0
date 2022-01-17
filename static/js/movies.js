const modalEl = document.getElementById('movie-modal');

const movieModal = new bootstrap.Modal(modalEl, {});
const movieCards = document.getElementById('movies-container');

let movieModalData = null;

movieCards.addEventListener('click', async (event) => {
    const target = isCardClick(event.path);
    if (target) {
        const id = target.dataset.id;
        const movie = await fetch(`http://localhost:5000/movies/${id}`).then(r => r.json());
        setModalInfo(target, movie);
        movieModal.toggle();
    }
});

modalEl.addEventListener('hide.bs.modal', () => {
    console.log('hide modal');
})

function isCardClick(path) {
    for (const target of path) {
        if (target.classList && target.classList.contains('movie-card')) {
            return target;
        }
    }
    return null;
}

/**
 *
 * @param modal {HTMLDivElement}
 */
function setModalInfo(modal, movie) {
    console.log(movie);
    document.getElementById('movie-modal-title').innerText = movie.title;
}
