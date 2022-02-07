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
    if (isAUth) {
        checkCanSaveMovie();
    }
})
modalEl.addEventListener('hidden.bs.modal', () => {
    modalEl.dataset.type = 'create';
    modalEl.classList.add('movie-create');
    modalEl.classList.remove('movie-update');
    resetMovieModal();
})
const createMovieButton = document.getElementById('create-movie-button');
const addMovieRoleButton = document.getElementById('add-movie-role-button');
const movieForm = document.getElementById('movie-form');

const modalCoverInput = document.getElementById('movie-modal-cover-upload');
const modalBannerInput = document.getElementById('movie-modal-banner-upload');
const modalTitleInput = document.getElementById('movie-modal-title-input');
const modalDescriptionInput = document.getElementById('movie-modal-description-input');
const modalDateInput = document.getElementById('movie-modal-date-input');
const modelDirectorFirstNameInput = document.getElementById('movie-modal-director-first-name');
const modelDirectorLastNameInput = document.getElementById('movie-modal-director-last-name');
const modalSaveButton = document.getElementById('movie-modal-submit-button');

const modalCoverPreview = document.getElementById('movie-modal-cover-preview');
const modalBannerPreview = document.getElementById('movie-modal-banner-preview');
const movieModelRolesContainer = document.getElementById('movie-model-roles-container');

movieModelRolesContainer.addEventListener('click', el => {
    const saveTarget = isRoleSaveButton(el.path);
    const deleteTarget = isRoleDeleteButton(el.path);
    if (saveTarget) {
        createRol(saveTarget);
    } else if(deleteTarget) {
        removeRol(deleteTarget.dataset.id);
    }
})

if (isAUth) {
    createMovieButton.addEventListener('click', () => {
        movieModal.toggle();
    });
    addMovieRoleButton.addEventListener('click', () => {
        addMovieRole()
    });
}

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
function isRoleSaveButton(path) {
    for (const target of path) {
        if (target.classList && target.classList.contains('role-save')) {
            return target;
        }
    }
    return null;
}

function isRoleDeleteButton(path) {
    for (const target of path) {
        if (target.classList && target.classList.contains('role-remove')) {
            return target;
        }
    }
    return null;
}


function addMovieRole(roleObj) {
	const wrapper = document.createElement('div');

	const firstNameWrapper = document.createElement('div');
	const lastNameWrapper = document.createElement('div');
	const roleWrapper = document.createElement('div');
    const actionWrapper = document.createElement('div');

	const firstName = document.createElement('input');
	const lastName = document.createElement('input');
	const role = document.createElement('input');
    const saveButton = document.createElement('button');
    const deleteButton = document.createElement('button');

	wrapper.className = "row movie-roles";

	firstNameWrapper.className = "col";
	lastNameWrapper.className = "col";
	roleWrapper.className = "col";
    actionWrapper.className = "col btn-group";

	firstName.className = "form-control";
	lastName.className = "form-control";
	role.className = "form-control";
    saveButton.className = "btn-sm btn btn-primary role-save";
    deleteButton.className = "btn-sm btn btn-danger role-remove";

	firstName.placeholder = "Voornaam"
	lastName.placeholder = "Achternaam"
	role.placeholder = "Personage"
    saveButton.innerHTML = "<i class=\"fa fa-save\"></i>"
    deleteButton.innerHTML = "<i class=\"fa fa-trash\"></i>"
    saveButton.setAttribute('type', 'button');
	deleteButton.setAttribute('type', 'button');

    if (roleObj) {
        firstName.value = roleObj.first_name;
        lastName.value = roleObj.last_name;
        role.value = roleObj.role;
        wrapper.id = 'role-' + roleObj.id;
        deleteButton.dataset.id = roleObj.id;
        if (!isAUth) {
            firstName.disabled = true;
            lastName.disabled = true;
            role.disabled = true;
        } else {
            actionWrapper.append(deleteButton);
        }
    } else {
        firstName.id = 'add-role-firstname';
        lastName.id = 'add-role-lastname';
        role.id = 'add-role-role';
        actionWrapper.append(saveButton);
        addMovieRoleButton.classList.add('d-none');
        wrapper.id = 'create-role';
    }

	firstNameWrapper.append(firstName);
	lastNameWrapper.append(lastName);
	roleWrapper.append(role);

	wrapper.append(firstNameWrapper, lastNameWrapper, roleWrapper, actionWrapper);
	movieModelRolesContainer.appendChild(wrapper);
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
    modelDirectorFirstNameInput.value = movie.director.first_name;
    modelDirectorLastNameInput.value = movie.director.last_name;
    for (const role of movie.roles) {
        addMovieRole(role);
    }
}

function resetMovieModal() {
    movieForm.action = `/movies`;
    modalTitleInput.value = '';
    modalDescriptionInput.value = '';
    modalBannerPreview.src = ``;
    modalCoverPreview.src = ``;
    modalDateInput.value = '';
    movieModelRolesContainer.innerHTML = "";
    modelDirectorFirstNameInput.value = "";
    modelDirectorLastNameInput.value = "";
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


async function createRol() {
    const firstName = document.getElementById('add-role-firstname').value;
    const lastName = document.getElementById('add-role-lastname').value;
    const role = document.getElementById('add-role-role').value;
    if (!firstName || !lastName || !role) {
        return;
    }
    const formData = new FormData();
    formData.set('first_name', firstName);
    formData.set('last_name', lastName);
    formData.set('role', role);

    const data = await fetch(`http://localhost:5000/movies/${movieModalData.id}/role`, {
        method: 'POST',
        body: formData
    }).then(r => r.json());
    document.getElementById('create-role').remove();
    addMovieRole(data);

    addMovieRoleButton.classList.remove('d-none');
}

async function removeRol(id) {
    const data = await fetch(`http://localhost:5000/movies/${movieModalData.id}/role/${id}/delete`, {
        method: 'POST'
    }).then(r => r.json());
    document.getElementById('role-' + id).remove();
}
 if (!isAUth) {
     const inputs = document.querySelectorAll('input');
     const textareas = document.querySelectorAll('textarea');
     for (const input of inputs) {
         input.disabled = true;
     }
     for (const textarea of textareas) {
         textarea.disabled = true;
     }
 }
