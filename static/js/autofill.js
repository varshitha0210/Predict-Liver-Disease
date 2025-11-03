document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("testForm");

    // Autofill inputs on page load
    const autofillInputs = () => {
        const inputs = form.querySelectorAll("input[type='text']");
        inputs.forEach(input => {
            const savedValue = localStorage.getItem(input.id);
            if (savedValue) {
                input.value = savedValue;
            }
        });
    };

    // Save inputs to local storage on change
    const saveInputs = () => {
        const inputs = form.querySelectorAll("input[type='text']");
        inputs.forEach(input => {
            input.addEventListener("input", () => {
                localStorage.setItem(input.id, input.value);
            });
        });
    };

    // Initialize
    autofillInputs();
    saveInputs();
});
