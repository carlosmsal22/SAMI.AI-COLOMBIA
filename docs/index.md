<a id="language-switcher" class="btn-language">English Version</a>

<div id="content-es">

<style>
/* Estilos generales */
:root {
  --primary: #2c3e50;
  --secondary: #4CAF50;
  --accent: #e74c3c;
  --light-bg: #f8f9fa;
  --dark-text: #2c3e50;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: var(--dark-text);
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  animation: fadeIn 1s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Botón de idioma */
.btn-language {
  position: fixed;
  top: 20px;
  right: 20px;
  background: var(--secondary);
  color: white;
  padding: 10px 20px;
  border-radius: 25px;
  font-weight: bold;
  z-index: 1000;
  border: none;
  cursor: pointer;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
  transition: all 0.3s ease;
}

.btn-language:hover {
  transform: scale(1.05);
}

/* [Todos tus otros estilos originales...] */
</style>

<!-- HERO SECTION -->
<div class="hero" style="text-align: center; padding: 40px 0;">
    <img src="assets/img/logo.png" width="220" alt="SAMI.AI COLOMBIA">
    <p style="font-size: 1.4em; font-weight: 300;">
        <strong>INTELIGENCIA ARTIFICIAL ESPECIALIZADA EN MERCADOS COLOMBIANOS</strong>
    </p>
</div>

<!-- STATS BANNER -->
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 40px 0;">
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: var(--accent);">+92%</div>
        <div>Cobertura de mercado</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #2ecc71;">15K</div>
        <div>Fuentes analizadas</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #3498db;">0.5s</div>
        <div>Velocidad de respuesta</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #9b59b6;">100%</div>
        <div>Enfoque Colombia</div>
    </div>
</div>

<!-- [Todas tus otras secciones en español...] -->

</div>

<div id="content-en" style="display:none;">

<!-- HERO SECTION (English) -->
<div class="hero" style="text-align: center; padding: 40px 0;">
    <img src="assets/img/logo.png" width="220" alt="SAMI.AI COLOMBIA">
    <p style="font-size: 1.4em; font-weight: 300;">
        <strong>AI SPECIALIZED IN COLOMBIAN MARKET ANALYSIS</strong>
    </p>
</div>

<!-- STATS BANNER (English) -->
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 15px; margin: 40px 0;">
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: var(--accent);">+92%</div>
        <div>Market coverage</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #2ecc71;">15K</div>
        <div>Data sources analyzed</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #3498db;">0.5s</div>
        <div>Response speed</div>
    </div>
    <div style="text-align: center;">
        <div style="font-size: 2em; font-weight: bold; color: #9b59b6;">100%</div>
        <div>Colombia-focused</div>
    </div>
</div>

<!-- [Todas tus otras secciones en inglés...] -->

</div>

<footer style="margin-top: 50px; text-align: center; padding: 20px; border-top: 1px solid #eee;">
    <p>This site is open source. <a href="https://github.com/your-repo" target="_blank">Improve this page</a>.</p>
</footer>

<script>
// Language Switcher
document.getElementById('language-switcher').addEventListener('click', function() {
    const esContent = document.getElementById('content-es');
    const enContent = document.getElementById('content-en');
    const btn = this;
    
    if (esContent.style.display === 'none') {
        esContent.style.display = 'block';
        enContent.style.display = 'none';
        btn.textContent = 'English Version';
        btn.style.background = '#4CAF50';
    } else {
        esContent.style.display = 'none';
        enContent.style.display = 'block';
        btn.textContent = 'Versión en Español';
        btn.style.background = '#e74c3c';
    }
});

// Countdown Timer
function updateCountdown() {
    const now = new Date();
    const end = new Date();
    end.setHours(23, 59, 59, 999);
    
    const diff = end - now;
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    
    const countdownEl = document.getElementById('countdown');
    if (countdownEl) {
        countdownEl.innerHTML = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
    }
}
setInterval(updateCountdown, 60000);
updateCountdown();
</script>
