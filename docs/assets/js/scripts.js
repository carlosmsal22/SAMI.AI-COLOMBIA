document.addEventListener('DOMContentLoaded', function() {
    const languageBtn = document.getElementById('languageBtn');
    const spanishContent = document.getElementById('spanishContent');
    const englishContent = document.getElementById('englishContent');
    
    languageBtn.addEventListener('click', function() {
        if (spanishContent.style.display === 'none') {
            // Cambiar a Español
            spanishContent.style.display = 'block';
            englishContent.style.display = 'none';
            languageBtn.textContent = 'English Version';
            languageBtn.style.background = '#4CAF50';
            document.documentElement.lang = 'es';
        } else {
            // Cambiar a Inglés
            spanishContent.style.display = 'none';
            englishContent.style.display = 'block';
            languageBtn.textContent = 'Versión en Español';
            languageBtn.style.background = '#e74c3c';
            document.documentElement.lang = 'en';
        }
    });
});