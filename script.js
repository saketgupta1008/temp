document.getElementById('toggleNavbar').addEventListener('click', function() {
    const navbar = document.getElementById('navbar');
    if (navbar.style.left === '0px') {
        navbar.style.left = '-200px';
    } else {
        navbar.style.left = '0px';
    }
});


function download() {
    alert('Download initiated!');
}

function reset() {
    alert('Resetting values!');
}

function clearText() {
    alert('Clearing text!');
}

function logout() {
    alert('Logging out!');
}

function help() {
    alert('Showing help!');
}



document.addEventListener('DOMContentLoaded', function() {
    var modeToggle = document.getElementById('modeToggle');
    console.log(modeToggle);  // Should log the input element or null if not found

    if (modeToggle) {
        modeToggle.addEventListener('change', function() {
            console.log("Checkbox state:", this.checked);  // Logs true or false
            document.body.classList.toggle('dark-mode', this.checked);
        });
    } else {
        console.log("Checkbox with ID 'modeToggle' not found");
    }
});

modeToggle.addEventListener('change', function() {
    console.log("Checkbox state:", this.checked);
    document.body.classList.toggle('dark-mode', this.checked);
    localStorage.setItem('darkMode', this.checked); // Save the state in local storage
});

// On page load, check local storage and update the theme
document.addEventListener('DOMContentLoaded', function() {
    const savedMode = localStorage.getItem('darkMode') === 'true'; // Retrieve the mode
    modeToggle.checked = savedMode;
    document.body.classList.toggle('dark-mode', savedMode);
});
