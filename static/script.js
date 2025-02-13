document.getElementById("run").addEventListener("click", function () {
    const codeEditor = document.getElementById("code-editor");
    const outputFrame = document.getElementById("outputFrame");
    const selectLang = document.querySelector("#lang select").value;
    const userInput = document.getElementById("user-input").value; 
    const userCode = codeEditor.value;

    fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: userCode, language: selectLang, user_input: userInput }) 
    })
    .then(response => response.json())
    .then(data => {
        outputFrame.value = data.output;
    })
    .catch(error => {
        console.error("Error:", error);
        outputFrame.value = "Error: " + error;
    });
});
