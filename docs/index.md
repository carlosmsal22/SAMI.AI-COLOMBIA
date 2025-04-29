<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SAMI.AI COLOMBIA - Inteligencia Artificial para Mercados Colombianos</title>
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
            background: #3e8e41;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 60px 0 40px;
            margin-bottom: 30px;
        }

        /* Stats Banner */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
            margin: 40px 0;
            text-align: center;
        }

        .stat-value {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }

        /* Features Section */
        .features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 30px;
            margin: 50px 0;
        }

        .feature-card {
            background: white;
            border-radius: 10px;
            padding: 25px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 2.5em;
            margin-bottom: 15px;
            color: var(--secondary);
        }

        /* CTA Section */
        .cta-section {
            background: linear-gradient(135deg, var(--primary), #1a252f);
            color: white;
            padding: 60px 40px;
            border-radius: 10px;
            text-align: center;
            margin: 60px 0;
        }

        .cta-button {
            display: inline-block;
            background: var(--accent);
            color: white;
            padding: 15px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            margin-top: 20px;
            transition: all 0.3s ease;
        }

        .cta-button:hover {
            background: #c0392b;
            transform: scale(1.05);
        }

        /* Footer */
        footer {
            margin-top: 50px;
            text-align: center;
            padding: 30px 0;
            border-top: 1px solid #eee;
            font-size: 0.9em;
            color: #7f8c8d;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .stats-grid, .features {
                grid-template-columns: 1fr;
            }
            
            .btn-language {
                top: 10px;
                right: 10px;
                padding: 8px 15px;
                font-size: 0.9em;
            }
        }
    </style>
</head>
<body>
    <a id="language-switcher" class="btn-language">English Version</a>

    <div id="content-es">
        <!-- HERO SECTION -->
        <div class="hero">
            <img src="assets/img/logo.png" width="220" alt="SAMI.AI COLOMBIA">
            <p style="font-size: 1.4em; font-weight: 300;">
                <strong>INTELIGENCIA ARTIFICIAL ESPECIALIZADA EN MERCADOS COLOMBIANOS</strong>
            </p>
        </div>

        <!-- STATS BANNER -->
        <div class="stats-grid">
            <div>
                <div class="stat-value" style="color: var(--accent);">+92%</div>
                <div>Cobertura de mercado</div>
            </div>
            <div>
                <div class="stat-value" style="color: #2ecc71;">15K</div>
                <div>Fuentes analizadas</div>
            </div>
            <div>
                <div class="stat-value" style="color: #3498db;">0.5s</div>
                <div>Velocidad de respuesta</div>
            </div>
            <div>
                <div class="stat-value" style="color: #9b59b6;">100%</div>
                <div>Enfoque Colombia</div>
            </div>
        </div>

        <!-- FEATURES SECTION -->
        <div class="features">
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Análisis en Tiempo Real</h3>
                <p>Monitoreo constante de tendencias y cambios en el mercado colombiano con actualizaciones en tiempo real.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <h3>Datos Precisos</h3>
                <p>Información verificada y procesada mediante algoritmos avanzados para máxima precisión.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🚀</div>
                <h3>Soluciones Adaptables</h3>
                <p>Herramientas personalizables para diferentes sectores de la economía colombiana.</p>
            </div>
        </div>

        <!-- CTA SECTION -->
        <div class="cta-section">
            <h2>Transforma tu negocio con inteligencia artificial</h2>
            <p>Únete a las empresas líderes que ya están utilizando SAMI.AI para tomar decisiones basadas en datos.</p>
            <a href="#contacto" class="cta-button">Solicitar Demo</a>
        </div>

        <!-- TESTIMONIALS -->
        <div style="margin: 60px 0; text-align: center;">
            <h2>Lo que dicen nuestros clientes</h2>
            <div style="max-width: 700px; margin: 30px auto; font-style: italic;">
                "SAMI.AI ha revolucionado nuestra forma de entender el mercado colombiano. Los insights que obtenemos nos dan una ventaja competitiva invaluable."
                <div style="margin-top: 15px; font-weight: bold;">- Carlos Méndez, Director Financiero</div>
            </div>
        </div>
    </div>

    <div id="content-en" style="display:none;">
        <!-- HERO SECTION (English) -->
        <div class="hero">
            <img src="assets/img/logo.png" width="220" alt="SAMI.AI COLOMBIA">
            <p style="font-size: 1.4em; font-weight: 300;">
                <strong>AI SPECIALIZED IN COLOMBIAN MARKET ANALYSIS</strong>
            </p>
        </div>

        <!-- STATS BANNER (English) -->
        <div class="stats-grid">
            <div>
                <div class="stat-value" style="color: var(--accent);">+92%</div>
                <div>Market coverage</div>
            </div>
            <div>
                <div class="stat-value" style="color: #2ecc71;">15K</div>
                <div>Data sources analyzed</div>
            </div>
            <div>
                <div class="stat-value" style="color: #3498db;">0.5s</div>
                <div>Response speed</div>
            </div>
            <div>
                <div class="stat-value" style="color: #9b59b6;">100%</div>
                <div>Colombia-focused</div>
            </div>
        </div>

        <!-- FEATURES SECTION (English) -->
        <div class="features">
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Real-Time Analysis</h3>
                <p>Constant monitoring of trends and changes in the Colombian market with real-time updates.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔍</div>
                <h3>Accurate Data</h3>
                <p>Verified information processed through advanced algorithms for maximum accuracy.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🚀</div>
                <h3>Adaptable Solutions</h3>
                <p>Customizable tools for different sectors of the Colombian economy.</p>
            </div>
        </div>

        <!-- CTA SECTION (English) -->
        <div class="cta-section">
            <h2>Transform your business with artificial intelligence</h2>
            <p>Join the leading companies already using SAMI.AI to make data-driven decisions.</p>
            <a href="#contact" class="cta-button">Request Demo</a>
        </div>

        <!-- TESTIMONIALS (English) -->
        <div style="margin: 60px 0; text-align: center;">
            <h2>What our clients say</h2>
            <div style="max-width: 700px; margin: 30px auto; font-style: italic;">
                "SAMI.AI has revolutionized how we understand the Colombian market. The insights we gain provide invaluable competitive advantage."
                <div style="margin-top: 15px; font-weight: bold;">- Carlos Méndez, Financial Director</div>
            </div>
        </div>
    </div>

    <footer>
        <p>This site is open source. <a href="https://github.com/your-repo" target="_blank">Improve this page</a>.</p>
        <p>SAMI.AI COLOMBIA © 2023 - All rights reserved</p>
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
</body>
</html>
