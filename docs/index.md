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
        /* Nuevos estilos para logos más grandes */
        .partner-logos img {
            width: 140px !important;  /* Aumenté de 120px a 140px */
            max-height: 70px !important;
            transition: all 0.3s ease;
        }
        .partner-logos img:hover {
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

<!-- SECCIÓN LOGOS PARTNERS (ACTUALIZADA) -->
<div style="text-align: center; margin: 40px 0;">
    <div style="display: inline-flex; align-items: center; background-color: var(--light-bg); padding: 10px 20px; border-radius: 8px;">
        ★★★★★ <span style="font-weight: bold; margin-left: 10px;">4.9/5</span>
        <span style="margin: 0 10px;">|</span>
        <span>+150 empresas confían en SAMI.AI</span>
    </div>
    <div style="margin-top: 30px;">
        <p style="font-size: 0.9em; margin-bottom: 15px; color: #7f8c8d;">Recomendado por:</p>
        <div class="partner-logos" style="display: flex; justify-content: center; gap: 30px; flex-wrap: wrap; align-items: center;">
            <!-- Logos 20% más grandes -->
            <img src="https://i.ibb.co/MD7x6Hcx/logo1.png" 
                 alt="Partner 1"
                 style="filter: grayscale(100%) opacity(0.9);"
                 onmouseover="this.style.filter='grayscale(0) opacity(1)'"
                 onmouseout="this.style.filter='grayscale(100%) opacity(0.9)'">
            
            <img src="https://i.ibb.co/1JKfvRzn/logo2.png" 
                 alt="Partner 2"
                 style="filter: grayscale(100%) opacity(0.9);"
                 onmouseover="this.style.filter='grayscale(0) opacity(1)'"
                 onmouseout="this.style.filter='grayscale(100%) opacity(0.9)'">
            
            <img src="https://i.ibb.co/rRJZbcpW/logo3.png" 
                 alt="Partner 3"
                 style="filter: grayscale(100%) opacity(0.9);"
                 onmouseover="this.style.filter='grayscale(0) opacity(1)'"
                 onmouseout="this.style.filter='grayscale(100%) opacity(0.9)'">
        </div>
    </div>
</div>

<!-- [El resto de tu código permanece igual...] -->

</body>
</html>
