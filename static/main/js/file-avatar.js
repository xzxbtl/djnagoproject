document.addEventListener('DOMContentLoaded', function() {
    const input = document.querySelector('.input-file-input');
    const text = document.querySelector('.input-file-text');

    input.addEventListener('change', function() {
        text.textContent = this.files[0].name;
    });
});