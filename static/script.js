async function askQuestion() {
    const userQuestion = document.getElementById('userQuestion').value;
    const responseBox = document.getElementById('responseBox');
    const button = document.querySelector('button');

    if (!userQuestion) {
        alert('Please enter a question!');
        return;
    }

    // Disable the button and show loading indicator
    button.disabled = true;
    button.innerText = 'Generating...';
    responseBox.innerText = 'Loading...';

    try {
        // Make a POST request to the backend
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: userQuestion }),
        });

        const data = await response.json();

        // Display the generated response or error
        if (data.response) {
            responseBox.innerText = data.response;
        } else if (data.error) {
            responseBox.innerText = 'Error: ' + data.error;
        }
    } catch (error) {
        responseBox.innerText = 'An error occurred: ' + error.message;
    } finally {
        // Re-enable the button and reset its text
        button.disabled = false;
        button.innerText = 'Generate Response';
    }
}
