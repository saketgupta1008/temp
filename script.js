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
document.addEventListener('DOMContentLoaded', function() {
    var searchInput = document.getElementById('searchInput');
    var textToType = "Type your search query here...";
    var currentCharIndex = 0;
    var typingInterval = 200; // Typing speed in milliseconds
    var typingTimeout;

    // Function to type out the next character
    function typeCharacter() {
        if (currentCharIndex < textToType.length) {
            searchInput.value += textToType.charAt(currentCharIndex);
            currentCharIndex++;
            typingTimeout = setTimeout(typeCharacter, typingInterval);
        }
    }

    // Function to clear the timeout and the current text if it matches the placeholder text
    function handleClick() {
        clearTimeout(typingTimeout);
        // If the auto-typing isn't finished, we check if the current value matches the typed text
        if (searchInput.value === textToType.substring(0, currentCharIndex)) {
            searchInput.value = ''; // Clear the auto-typed text
        }
        // Remove the event listener so this only happens once
        searchInput.removeEventListener('click', handleClick);
    }

    // Add click event listener to the search input
    searchInput.addEventListener('click', handleClick);

    // Start typing automatically
    typeCharacter();
});
