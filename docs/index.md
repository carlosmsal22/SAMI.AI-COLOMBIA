<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAMI.AI COLOMBIA | Inteligencia Artificial para Mercados</title>
    <style>
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
        .hero {
            text-align: center;
            padding: 40px 0;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin: 40px 0;
        }
        .feature-card {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            border-top: 4px solid var(--secondary);
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin: 40px 0;
        }
        .testimonial {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin: 40px 0;
        }
        .whatsapp-float {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #25D366;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            z-index: 1000;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
        .offer-popup {
            position: fixed;
            bottom: 20px;
            left: 20px;
            background: linear-gradient(135deg, #ff7676, #f54ea2);
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(245, 78, 162, 0.4);
            max-width: 300px;
            z-index: 1000;
        }
        .data-source {
            background-color: #f1c40f;
            color: #000;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 800;
        }
        .partner-logos {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
            align-items: center;
            margin-top: 20px;
        }
        .partner-logos img {
            width: 150px;
            height: auto;
            max-height: 80px;
            object-fit: contain;
            filter: grayscale(100%) opacity(0.9);
            transition: all 0.3s ease;
        }
        .partner-logos img:hover {
            filter: grayscale(0) opacity(1);
            transform: scale(1.1);
        }
    </style>
</head>
<body>

<!-- HERO SECTION -->
<div class="hero">
    <img src="LOGO.png" width="220" alt="SAMI.AI COLOMBIA">
    <p style="font-size: 1.4em; font-weight: 300;">
        <strong>INTELIGENCIA ARTIFICIAL ESPECIALIZADA EN MERCADOS COLOMBIANOS</strong>
    </p>
</div>

<!-- STATS BANNER -->
<div class="stats-grid">
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

<!-- MAIN FEATURE CARD -->
<div class="feature-card">
    <h2 style="font-size: 1.8em; color: var(--primary); text-align: center; margin-bottom: 25px;">
        🔍 COMPATIBLE CON LAS FUENTES MÁS PODEROSAS DEL PAÍS
    </h2>
    <div style="font-size: 1.3em; line-height: 1.8; text-align: center; font-weight: bold;">
        <span style="color: var(--accent);">• Estratos socioeconómicos (1-6)</span><br>
        <span style="color: #3498db;">• Culturas: Paisa, Rolo, Costeño, Caleño</span><br>
        <span style="color: #2ecc71;">• Datos oficiales: </span>
        <span class="data-source">SIC.gov.co</span>, 
        <span class="data-source">DANE</span>, 
        <span class="data-source">INVIMA</span><br>
        <span style="color: #9b59b6;">• Plataformas clave: </span>
        <span class="data-source">ReclameAquí</span>, 
        <span class="data-source">Éxito</span>, 
        <span class="data-source">Twitter/X</span>
    </div>
    <p style="text-align: center; margin-top: 25px; font-size: 1.1em;">
        <em>+20 fuentes adicionales disponibles</em> 📊
    </p>
</div>

<!-- TESTIMONIAL -->
<div class="testimonial">
    <div style="display: flex; align-items: center; margin-bottom: 15px;">
        <img src="https://i.imgur.com/ejemplo.jpg" width="60" style="border-radius: 50%; margin-right: 15px;">
        <div>
            <div style="font-weight: bold;">Carlos Andrés Pérez</div>
            <div style="font-size: 0.9em; color: #7f8c8d;">Director de Marketing, Éxito</div>
        </div>
        <img src="exito-logo.png" width="80" style="margin-left: auto;">
    </div>
    <p style="font-style: italic; font-size: 1.1em;">
        "SAMI.AI nos reveló insights culturales que aumentaron un 30% nuestra efectividad en campañas regionales. ¡Imprescindible!"
    </p>
</div>

<!-- COMPARISON TABLE -->
<table class="comparison-table">
    <tr style="background-color: var(--primary); color: white;">
        <th style="padding: 15px; text-align: left;">Característica</th>
        <th style="padding: 15px; text-align: center;">Métodos Tradicionales</th>
        <th style="padding: 15px; text-align: center;">SAMI.AI</th>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
        <td style="padding: 15px; font-weight: bold;">Tiempo análisis</td>
        <td style="padding: 15px; text-align: center;">2-3 semanas</td>
        <td style="padding: 15px; text-align: center; color: var(--secondary); font-weight: bold;">2 minutos</td>
    </tr>
    <tr style="border-bottom: 1px solid #ddd;">
        <td style="padding: 15px; font-weight: bold;">Costo promedio</td>
        <td style="padding: 15px; text-align: center;">$15M COP</td>
        <td style="padding: 15px; text-align: center; color: var(--secondary); font-weight: bold;">$1.5M COP</td>
    </tr>
</table>

<!-- TRUST BADGES -->
<div style="text-align: center; margin: 40px 0;">
    <div style="display: inline-flex; align-items: center; background-color: var(--light-bg); padding: 10px 20px; border-radius: 8px;">
        ★★★★★ <span style="font-weight: bold; margin-left: 10px;">4.9/5</span>
        <span style="margin: 0 10px;">|</span>
        <span>+150 empresas confían en SAMI.AI</span>
    </div>
    <div style="margin-top: 30px;">
        <p style="font-size: 0.9em; margin-bottom: 15px; color: #7f8c8d;">Recomendado por:</p>
        <div class="partner-logos">
            <img src="https://i.ibb.co/MD7x6Hcx/logo1.png" alt="Partner 1">
            <img src="https://i.ibb.co/1JKfvRzn/logo2.png" alt="Partner 2">
            <img src="https://i.ibb.co/rRJZbcpW/logo3.png" alt="Partner 3">
        </div>
    </div>
</div>

<!-- VIDEO DEMO -->
<div style="text-align: center; margin: 40px 0;">
    <h3>🔮 Mira a SAMI.AI en acción:</h3>
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); margin: 20px 0;">
        <iframe src="https://www.youtube.com/embed/tu-video" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"></iframe>
    </div>
</div>

<!-- CASE STUDIES -->
<details style="margin: 25px 0; border: 1px solid #ddd; border-radius: 8px; padding: 15px;">
    <summary style="font-weight: bold; font-size: 1.1em; cursor: pointer;">📌 Caso Éxito: Campaña para Éxito en Medellín</summary>
    <p style="margin-top: 15px;">
        <strong>Resultados:</strong> +37% engagement en campañas Paisas usando insights culturales de SAMI.AI.<br>
        <strong>Técnica:</strong> Cross-analysis entre datos de SIC y preferencias regionales.
    </p>
</details>

<!-- WHATSAPP FLOAT -->
<a href="https://wa.me/573001234567?text=¡Hola!%20Vi%20SAMI.AI%20y%20quiero%20saber%20más" class="whatsapp-float">
    <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="30">
</a>

<!-- SPECIAL OFFER -->
<div id="special-offer" class="offer-popup">
    <div style="font-weight: bold; font-size: 1.2em; margin-bottom: 10px;">🚀 ¡Oferta Lanzamiento!</div>
    <p>50% OFF en tu primer análisis (Solo hasta <span id="countdown" style="font-weight: bold;">24:00 hrs</span>)</p>
    <a href="mailto:abermudez@theinsightsai.com?subject=Quiero%20mi%20descuento%20SAMI.AI&body=Hola,%20estoy%20interesado%20en%20la%20oferta%20de%20lanzamiento" style="display: inline-block; background: white; color: #f54ea2; padding: 8px 15px; border-radius: 5px; font-weight: bold; margin-top: 10px; text-decoration: none;">¡QUIERO MI DESCUENTO!</a>
    <button onclick="document.getElementById('special-offer').style.display='none'" style="position: absolute; top: 5px; right: 5px; background: none; border: none; color: white; font-weight: bold; cursor: pointer;">X</button>
</div>

<script>
  // Timer de 24 horas
  function updateCountdown() {
    const now = new Date();
    const end = new Date();
    end.setHours(23, 59, 59, 999);
    
    const diff = end - now;
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    
    document.getElementById('countdown').innerHTML = 
      `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
  }
  setInterval(updateCountdown, 60000);
  updateCountdown();
</script>

</body>
</html>
