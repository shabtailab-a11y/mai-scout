# 🚀 MAI — Deployment en Railway

## Paso 1: Preparar GitHub

```bash
cd /root/.openclaw/workspace/mai_scout

# Inicializar repo (si no existe)
git init

# Agregar archivos
git add .
git commit -m "initial: MAI v1 ready for production"

# Crear repo en GitHub
# 1. Ir a https://github.com/new
# 2. Crear repo "mai-scout"
# 3. NO inicializar con README (ya existe)
# 4. Copiar URL (https://github.com/YOUR_USER/mai-scout.git)

# Push a GitHub
git remote add origin https://github.com/YOUR_USER/mai-scout.git
git branch -M main
git push -u origin main
```

## Paso 2: Conectar Railway

1. **Ir a railway.app**
2. **Login con GitHub**
3. **Crear nuevo proyecto**
   - "Deploy from GitHub repo"
   - Buscar "mai-scout"
   - Seleccionar
   - Railway auto-detecta Python ✅

## Paso 3: Agregar Environment Variables

En Railway dashboard:
```
Variables → Add Variable

SPOTIPY_CLIENT_ID = e490c3b2db6744ce884b9d27f426d4f7
SPOTIPY_CLIENT_SECRET = 6cd469cf554842b29f009a9555894ace
YOUTUBE_API_KEY = AIzaSyCu5JG9wt4roONhqLbO9ca6m4wv6-JT3WA
```

## Paso 4: Deploy 🎉

Railway auto-despliega cuando pusheamos a GitHub.

**Tu URL pública estará lista en 2-3 minutos:**
```
https://mai-scout-production.railway.app
```

---

## Actualizar después

```bash
# Hacer cambios locales
# Commit + push
git add .
git commit -m "feature: add something"
git push

# Railway auto-redeploy automáticamente ✅
```

## Debug en Railway

Si algo falla:
1. Ir a "Deployments" en Railway dashboard
2. Ver logs en tiempo real
3. Ajustar variables de entorno si es necesario

---

**¡Listo! Ya estará público y gratis.** 🎵
