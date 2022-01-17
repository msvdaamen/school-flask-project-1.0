const modalEl = document.getElementById('movie-modal');

const movieModal = new bootstrap.Modal(modalEl, {});
const movieCards = document.getElementById('movies-container');

let movieModalData = null;

movieModal.toggle();
movieCards.addEventListener('click', async (event) => {
    const target = isCardClick(event.path);
    if (target) {
        const id = target.dataset.id;
        movieModalData = await fetch(`http://localhost:5000/movies/${id}`).then(r => r.json());
        setModalInfo(target, movieModalData);
        movieModal.toggle();
    }
});

modalEl.addEventListener('hide.bs.modal', () => {
    console.log('hide modal');
})

// document.getElementById('movie-modal-save-button').addEventListener('click', async () => {
//     const id = movieModalData.id;
//     const fileInput = document.getElementById('movie-modal-image');
//     const cover = fileInput.files[0];
//     const title = 'test';
//     const payload = new FormData();
//     payload.append('cover', cover, cover.name);
//     payload.append('title', title);
//     const response = await fetch(`http://localhost:5000/movies/${id}`, {
//         method: 'POST',
//         body: payload
//     }).then(r => r.json());
//     console.log(response)
// });


document.getElementById('movie-modal-preview-banner').addEventListener('click', () => {
    document.getElementById('movie-modal-banner-file-upload').click();
});
document.getElementById('movie-modal-cover-file-upload').addEventListener('change', (event) => {
    setModalPreviewBanner();
});
document.getElementById('movie-modal-banner-file-upload').addEventListener('change', (event) => {
    setModalPreviewBanner();
});
document.getElementById('movie-modal-preview-banner-preview').addEventListener('click', () => {
    document.getElementById('movie-modal-banner-file-upload').click();
});

function setModalPreviewBanner() {
    if (document.getElementById('movie-modal-preview-banner')) {
        document.getElementById('movie-modal-preview-banner').remove();
    }
    const file = document.getElementById('movie-modal-banner-file-upload').files[0];
    document.getElementById('movie-modal-preview-banner-preview').src = URL.createObjectURL(file);
}

function setModalPreviewCover() {
    const file = document.getElementById('movie-modal-cover-upload').files[0];
    document.getElementById('movie-modal-preview-caver-preview').src = URL.createObjectURL(file);
}


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
    document.getElementById('movie-modal-title').innerText = movie.title;
}
