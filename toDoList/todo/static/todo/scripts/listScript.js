document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tags').addEventListener('click', function(event) {
        event.stopPropagation();
        const dropdown = document.getElementById('tag-dropdown');
        dropdown.classList.toggle('show');
    });

    document.addEventListener('click', function(event) {
        const dropdown = document.getElementById('tag-dropdown');
        const tags = document.getElementById('tags');

        if (!tags.contains(event.target) && !dropdown.contains(event.target)) {
            dropdown.classList.remove('show');
        }
    });
});
