const translateBtn = document.getElementById("translateBtn");
const translatedText = document.getElementById("translatedText");
const copyBtn = document.getElementById("copyBtn");
const speakBtn = document.getElementById("speakBtn");

translateBtn.addEventListener("click", async () => {

    const text = document.getElementById("inputText").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;

    if (text.trim() === "") {
        alert("Please enter some text.");
        return;
    }

    translatedText.textContent = "Translating...";

    try {

        const response = await fetch(
            `https://api.mymemory.translated.net/get?q=${encodeURIComponent(text)}&langpair=${sourceLang}|${targetLang}`
        );

        const data = await response.json();

        translatedText.textContent =
            data.responseData.translatedText;

    } catch (error) {

        console.error(error);
        translatedText.textContent =
            "Translation failed!";
    }
});

copyBtn.addEventListener("click", () => {

    const text = translatedText.textContent;

    if (!text || text === "Translating...") {
        alert("Nothing to copy.");
        return;
    }

    navigator.clipboard.writeText(text);
    alert("Copied!");
});

speakBtn.addEventListener("click", () => {

    const text = translatedText.textContent;

    if (!text || text === "Translating...") {
        alert("Nothing to speak.");
        return;
    }

    const speech = new SpeechSynthesisUtterance(text);

    const targetLang = document.getElementById("targetLang").value;

    if (targetLang === "hi") {
        speech.lang = "hi-IN";
    } else if (targetLang === "fr") {
        speech.lang = "fr-FR";
    } else if (targetLang === "es") {
        speech.lang = "es-ES";
    } else if (targetLang === "de") {
        speech.lang = "de-DE";
    } else {
        speech.lang = "en-US";
    }

    speechSynthesis.speak(speech);
});