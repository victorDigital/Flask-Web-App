let darkModeOn = true;

const createStorage = (name, value) => {
    localStorage.setItem(name, value);
};

const getStorage = (name) => {
    return localStorage.getItem(name);
};

const deleteStorage = (name) => {
    localStorage.removeItem(name);
};

const toggleDarkMode = () => {
    if (document.body.classList.contains('dark-mode')) {
        document.body.classList.remove('dark-mode');
        createStorage('theme', 'light');
        darkModeOn = false;
    } else {
        document.body.classList.add('dark-mode');
        createStorage('theme', 'dark');
        darkModeOn = true;
    }
};

document.getElementById('dark-mode-toggle').addEventListener('click', toggleDarkMode);

document.addEventListener("DOMContentLoaded", function () {
    if (getStorage('theme') === 'dark') {
        document.body.classList.add('dark-mode');
        darkModeOn = true;
    } else {
        document.body.classList.remove('dark-mode');
        darkModeOn = false;
    }
    if (darkModeOn) {
        if (!document.body.classList.contains('dark-mode')) {
            document.body.classList.add('dark-mode');
        }
    } else {
        if (document.body.classList.contains('dark-mode')) {
            document.body.classList.remove('dark-mode');
        }
    }
});