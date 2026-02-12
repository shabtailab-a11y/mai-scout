# 🚀 MAI Scout - Claude Code Migration Guide

## ¿Qué es Claude Code?

Claude Code es la interfaz de Claude.ai que permite trabajar con código directamente en el navegador:
- Editor de código integrado
- Ejecución de comandos (git, Python, Node, etc.)
- Manejo de archivos y carpetas
- Integración con GitHub

## 📋 Antes de Empezar

### Requisitos
1. **Claude.ai** account con acceso a Claude Code
2. **GitHub** account (ya tienes: shabtailab-a11y)
3. **Git** instalado localmente (`git --version`)
4. **Python 3.11+** instalado (`python --version`)
5. **Node.js** (opcional, solo si quieres frontend tooling)

### Lo que prepararé para ti

1. **`mai-scout.zip`** - Código completo del proyecto
2. **`PROJECT_CONTEXT.md`** - Resumen ejecutivo (qué se hizo, cómo funciona)
3. **`SETUP_INSTRUCTIONS.md`** - Paso a paso para levantar el proyecto localmente
4. **`CLAUDE_CODE_INSTRUCTIONS.md`** - Instrucciones específicas para Claude Code

---

## 🎯 Instrucciones Paso a Paso

### PASO 1: Descargar los Archivos

Ve a esta sesión de OpenClaw y descarga:
- `mai-scout.zip`
- `PROJECT_CONTEXT.md`
- `SETUP_INSTRUCTIONS.md`

### PASO 2: Preparar tu Computadora

```bash
# 1. Descomprime el ZIP
unzip mai-scout.zip
cd mai-scout

# 2. Crea un virtual environment Python
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Configura variables de entorno
cp .env.example .env
# Edita .env y agrega tus keys (ver PROJECT_CONTEXT.md)

# 5. Conecta a GitHub
git remote set-url origin https://github.com/shabtailab-a11y/mai-scout.git
```

### PASO 3: Abre en Claude Code

1. Ve a **Claude.ai**
2. Click **"Artifacts"** o **"Code"** (depende versión)
3. Click **"Create New"** → **"Upload Files/Folder"**
4. Sube la carpeta `mai-scout` completa

### PASO 4: Comienza a Trabajar

En Claude Code, puedes:

```bash
# Ver el estado del proyecto
git status
git log --oneline -10

# Crear una rama para tu feature
git checkout -b feature/nombre-feature

# Hacer cambios (editar archivos en el editor)
# → Edita app.py, index.html, etc.

# Ver cambios
git diff

# Commit y push
git add -A
git commit -m "Descripción del cambio"
git push origin feature/nombre-feature

# En GitHub, crea un PR para revisar antes de mergear a main
```

### PASO 5: Flujo de Trabajo Recomendado

**Para cada feature/mejora:**

```bash
1. git pull origin main                    # Sincroniza con remoto
2. git checkout -b feature/tu-feature      # Nueva rama
3. Haz cambios en el código
4. git add -A && git commit -m "..."       # Commit
5. git push origin feature/tu-feature      # Push
6. En GitHub: crea Pull Request
7. Review el PR
8. Mergea a main
9. git checkout main && git pull           # Sincroniza localmente
```

---

## 📚 Archivos Clave del Proyecto

```
mai-scout/
├── app.py                  # Backend Flask (principales routes, APIs)
├── index.html              # Frontend HTML5 (UI principal)
├── evolution_data.py       # Datos de Evolution (Bad Bunny, Taylor Swift, etc.)
├── requirements.txt        # Python dependencies (pip install)
├── .env.example            # Template de variables de entorno
├── .gitignore              # Archivos no a trackear
├── README.md               # Documentación
└── data/                   # (Si existe) datos persistentes
```

### Endpoints Principales

```
GET  /                           → Página principal
POST /api/scout                  → Buscar artista
POST /api/artist-tiktok          → Traer TikTok automático
POST /api/evolution              → Datos de Evolution
POST /api/spotlight-subscribe    → Suscribirse a Spotlight
GET  /spotlight/<artist_slug>    → Página pública del artista
```

---

## 🔑 Variables de Entorno Necesarias

Copia `.env.example` a `.env` y completa:

```bash
# Spotify
SPOTIPY_CLIENT_ID=<tu_id>
SPOTIPY_CLIENT_SECRET=<tu_secret>

# YouTube
YOUTUBE_API_KEY=<tu_api_key>

# Optional
LASTFM_API_KEY=<tu_api_key>
RAPIDAPI_KEY=<tu_api_key>  # Para TikTok

# App Config
FLASK_ENV=development
PORT=5000
```

**Dónde obtener keys:**
- Spotify: https://developer.spotify.com/dashboard
- YouTube: https://console.cloud.google.com
- Last.fm: https://www.last.fm/api/account/create
- RapidAPI: https://rapidapi.com/marketplace/tiktok-scraper7

---

## 🧪 Testear Localmente

```bash
# Levanta el servidor
python app.py

# Abre en navegador
http://localhost:5000

# Backend logs aparecerán en terminal
```

---

## 🔄 Sincronización entre Máquinas

**Si trabajas en múltiples máquinas:**

```bash
# Siempre sincroniza antes de empezar
git pull origin main

# Siempre pusheá cuando termines
git push origin tu-rama
```

---

## ⚠️ Notas Importantes

1. **No commitees `.env`** - Está en `.gitignore`, eso es correcto
2. **Usa ramas** - Nunca edites `main` directamente
3. **Pushea frecuente** - Así tienes backup en GitHub
4. **Comunica cambios grandes** - Si cambias arquitectura, avisa
5. **Railway auto-despliega** - Cuando mergeas a `main`, Railway redeploya automático

---

## 🆘 Si Algo Falla

### "pip install failed"
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### "ModuleNotFoundError"
```bash
pip install flask flask-cors spotipy google-auth-oauthlib
```

### "Port 5000 already in use"
```bash
# Usa otro puerto
python app.py --port 5001
# O mata el proceso que usa 5000
lsof -ti:5000 | xargs kill -9  # macOS/Linux
```

### "GitHub authentication failed"
```bash
# Configura git con tu nombre
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Usa SSH en lugar de HTTPS (recomendado)
git remote set-url origin git@github.com:shabtailab-a11y/mai-scout.git
```

---

## 📞 Próximos Pasos

1. ✅ Descarga los archivos
2. ✅ Corre SETUP_INSTRUCTIONS.md
3. ✅ Abre en Claude Code
4. ✅ Comienza con un pequeño cambio (ej: edit README.md)
5. ✅ Commit y push para verificar que todo funciona
6. ✅ Luego, features grandes

---

## 🎯 Qué Hacer Después

Una vez tengas todo corriendo localmente, puedes:

- **Mejorar Spotlight** (la característica nueva)
- **Agregar más artistas a Evolution**
- **Implementar Fase 2 de Spotlight** (automatización, emails, analytics)
- **Refactorizar código** (limpiar, optimizar)
- **Agregar tests unitarios**
- **Mejorar UI/UX**

---

**¿Ready? ¡Vamos!** 🚀
