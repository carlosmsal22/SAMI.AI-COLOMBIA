// Switcher de idioma
document.addEventListener('DOMContentLoaded', function() {
  const languageBtn = document.querySelector('.btn-language');
  
  if (languageBtn) {
    languageBtn.addEventListener('click', function(e) {
      e.preventDefault();
      const esContent = document.getElementById('content-es');
      const enContent = document.getElementById('content-en');
      
      if (esContent.style.display === 'none') {
        // Cambiar a Español
        esContent.style.display = 'block';
        enContent.style.display = 'none';
        languageBtn.textContent = 'English Version';
        languageBtn.style.background = '#4CAF50';
      } else {
        // Cambiar a Inglés
        esContent.style.display = 'none';
        enContent.style.display = 'block';
        languageBtn.textContent = 'Versión en Español';
        languageBtn.style.background = '#e74c3c';
      }
    });
  }

  // [Añade aquí otras funcionalidades como el countdown]
});
