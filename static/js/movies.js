const modalEl = document.getElementById('movie-modal');

const movieModal = new bootstrap.Modal(modalEl, {});
const movieCards = document.getElementById('movies-container');

let movieModalData = null;

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

const modalCoverInput = document.getElementById('movie-modal-cover-upload');
const modalBannerInput = document.getElementById('movie-modal-banner-upload');
const modalTitleInput = document.getElementById('movie-modal-title-input');
const modalDateInput = document.getElementById('movie-modal-date-input');
const modalSaveButton = document.getElementById('movie-modal-submit-button');

const modalCoverPreview = document.getElementById('movie-modal-cover-preview');
const modalBannerPreview = document.getElementById('movie-modal-banner-preview');

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
modalCoverPreview.addEventListener('click', () => {
    modalCoverInput.click();
});
modalBannerPreview.addEventListener('click', () => {
    modalBannerInput.click();
});
modalCoverInput.addEventListener('change', (event) => {
    setModalPreviewCover();
});
modalBannerInput.addEventListener('change', (event) => {
    setModalPreviewBanner();
});
modalTitleInput.addEventListener('keyup', () => {
    checkCanSaveMovie();
});
modalDateInput.addEventListener('keyup', () => {
    checkCanSaveMovie();
});

movieModal.toggle();
checkCanSaveMovie();

function checkCanSaveMovie() {
    if (!modalTitleInput.value.trim() || !modalDateInput.value.trim()) {
        modalSaveButton.disabled = true;
        return;
    }
    modalSaveButton.disabled = false;
}

function setModalPreviewCover() {
    const file = modalCoverInput.files[0];
    modalCoverPreview.src = URL.createObjectURL(file);
}
function setModalPreviewBanner() {
    const file = modalBannerInput.files[0];
    modalBannerPreview.src = URL.createObjectURL(file);
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
