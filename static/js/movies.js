const modalEl = document.getElementById('movie-modal');

const movieModal = new bootstrap.Modal(modalEl, {});
const movieCards = document.getElementById('movies-container');

let movieModalData = null;
let movieModalType = 'create';

movieCards.addEventListener('click', async (event) => {
    const target = isCardClick(event.path);
    if (target) {
        modalEl.dataset.type = 'update';
        modalEl.classList.remove('movie-create');
        modalEl.classList.add('movie-update');
        const id = target.dataset.id;
        movieModalData = await fetch(`http://localhost:5000/movies/${id}`).then(r => r.json());
        setModalInfo(movieModalData);
        movieModal.toggle();
    }
});

modalEl.addEventListener('show.bs.modal', () => {
    movieModalType = modalEl.dataset.type;
    checkCanSaveMovie();
})
modalEl.addEventListener('hidden.bs.modal', () => {
    modalEl.dataset.type = 'create';
    modalEl.classList.add('movie-create');
    modalEl.classList.remove('movie-update');
    resetMovieModal();
})
const createMovieButton = document.getElementById('create-movie-button');
const movieForm = document.getElementById('movie-form');

const modalCoverInput = document.getElementById('movie-modal-cover-upload');
const modalBannerInput = document.getElementById('movie-modal-banner-upload');
const modalTitleInput = document.getElementById('movie-modal-title-input');
const modalDescriptionInput = document.getElementById('movie-modal-description-input');
const modalDateInput = document.getElementById('movie-modal-date-input');
const modalSaveButton = document.getElementById('movie-modal-submit-button');

const modalCoverPreview = document.getElementById('movie-modal-cover-preview');
const modalBannerPreview = document.getElementById('movie-modal-banner-preview');
const movieModelRolesContainer = document.getElementById('movie-model-roles-container');

createMovieButton.addEventListener('click', () => {
    movieModal.toggle();
});

modalCoverPreview.addEventListener('click', () => {
    modalCoverInput.click();
});
modalBannerPreview.addEventListener('click', () => {
    modalBannerInput.click();
});
modalCoverInput.addEventListener('change', (event) => {
    setModalPreviewCover();
    checkCanSaveMovie();
});
modalBannerInput.addEventListener('change', (event) => {
    setModalPreviewBanner();
    checkCanSaveMovie();
});
modalTitleInput.addEventListener('keyup', () => {
    checkCanSaveMovie();
});
modalDateInput.addEventListener('keyup', () => {
    checkCanSaveMovie();
});

function checkCanSaveMovie() {
    if (!modalTitleInput.value.trim() || !modalDescriptionInput.value.trim() || !modalDateInput.value.trim() || (movieModalType === 'create' && (!modalCoverInput.files.length || !modalCoverInput.files.length))) {
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
 * @param movie {object}
 */
function setModalInfo(movie) {
    movieForm.action = `/movies/${movie.id}`;
    modalTitleInput.value = movie.title;
    modalDescriptionInput.value = movie.description;
    modalBannerPreview.src = `http://localhost:5000/public/images/${movie.banner.filename}`;
    modalCoverPreview.src = `http://localhost:5000/public/images/${movie.cover.filename}`;
    modalDateInput.value = formatDate(movie.date);
    for (let i = 0; i < 2; i++) {
        const wrapper = document.createElement('div');

        const firstNameWrapper = document.createElement('div');
        const lastNameWrapper = document.createElement('div');
        const roleWrapper = document.createElement('div');

        const firstName = document.createElement('input');
        const lastName = document.createElement('input');
        const role = document.createElement('input');

        wrapper.className = "row movie-roles";

        firstNameWrapper.className = "col";
        lastNameWrapper.className = "col";
        roleWrapper.className = "col";

        firstName.className = "form-control";
        lastName.className = "form-control";
        role.className = "form-control";

        firstName.placeholder = "Voornaam"
        lastName.placeholder = "Achternaam"
        role.placeholder = "Personage"

        firstNameWrapper.append(firstName);
        lastNameWrapper.append(lastName);
        roleWrapper.append(role);

        wrapper.append(firstNameWrapper, lastNameWrapper, roleWrapper);
        movieModelRolesContainer.appendChild(wrapper);
    }
}

function resetMovieModal() {
    movieForm.action = `/movies`;
    modalTitleInput.value = '';
    modalDescriptionInput.value = '';
    modalBannerPreview.src = ``;
    modalCoverPreview.src = ``;
    modalDateInput.value = '';
}

/**
 *
 * @param date {string}
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    if (!date) {
        return null;
    }
    const year = date.getFullYear();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    if (month < 10) {
        month = '0' + month;
    }
    if (day < 10) {
        day = '0' + day;
    }

    return `${year}-${month}-${day}`;
}
