

// Check for SpeechRecognition API support
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition;

// Initialize speech recognition
if (SpeechRecognition) {
    recognition = new SpeechRecognition();
    recognition.continuous = false; // Stop recognition after one result
    recognition.interimResults = false; // Get final results only

    // On speech result event
    recognition.onresult = function(event) {
        const spokenText = event.results[0][0].transcript; // Get the spoken text
        addUserMsg(spokenText); // Display the spoken text in the chat
        eel.getUserInput(spokenText); // Send the spoken text to the server
    };

    // Start speech recognition when button is clicked
    document.getElementById("userInputButton").addEventListener("click", function() {
        recognition.start(); // Start recognizing speech
    });

    // Handle errors
    recognition.onerror = function(event) {
        console.error("Speech recognition error: ", event.error);
    };
} else {
    console.warn("Speech recognition not supported in this browser.");
}

// User pressed enter '13'
document.getElementById("userInput").addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
        // Cancel the default action
        event.preventDefault();
        // Process event
        getUserInput();
    }
});

eel.expose(addUserMsg);
eel.expose(addAppMsg);

function addUserMsg(msg) {
    const element = document.getElementById("messages");
    element.innerHTML += '<div class="message from ready rtol">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    // Add delay for animation to complete and then modify class to => "message from"
    const index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message from"), 500);
}

function addAppMsg(msg) {
    const element = document.getElementById("messages");
    element.innerHTML += '<div class="message to ready ltor">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    // Add delay for animation to complete and then modify class to => "message to"
    const index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message to"), 500);
}

function changeClass(element, index, newClass) {
    console.log(newClass + ' ' + index);
    element.children[index].className = newClass;
}

function getUserInput() {
    const element = document.getElementById("userInput");
    const msg = element.value;
    if (msg.length != 0) {
        element.value = "";
        eel.getUserInput(msg);
    }
}
