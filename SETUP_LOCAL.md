# 🚀 MAI Scout - Local Setup Instructions

## ✅ Prerequisites

Before starting, make sure you have:

- [ ] Python 3.11+ (`python --version`)
- [ ] Git installed (`git --version`)
- [ ] GitHub account with access to: https://github.com/shabtailab-a11y/mai-scout
- [ ] API keys (see "Get API Keys" section below)

---

## 📥 Step 1: Clone the Repository

```bash
# Navigate to your projects directory
cd ~/projects  # or wherever you want

# Clone the repo
git clone https://github.com/shabtailab-a11y/mai-scout.git
cd mai-scout

# Verify you're on main branch
git status  # Should show "On branch main"
```

---

## 🔧 Step 2: Create Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# You should see (venv) at the start of your terminal prompt
```

---

## 📦 Step 3: Install Python Dependencies

```bash
# Make sure you're in the mai-scout directory with venv activated
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Verify installation
pip list | grep -E "Flask|spotipy|google-auth"
```

Expected packages:
- flask
- flask-cors
- spotipy
- google-auth-oauthlib
- google-api-python-client
- requests

---

## 🔑 Step 4: Get API Keys

### Spotify API
1. Go to: https://developer.spotify.com/dashboard
2. Log in (create account if needed)
3. Create a "New App"
4. Accept terms and Create
5. You'll get:
   - `Client ID`
   - `Client Secret` (keep secret!)
6. Copy both

### YouTube API
1. Go to: https://console.cloud.google.com/
2. Create a new project (top left dropdown)
3. Enable APIs: Search for "YouTube Data API v3" and click Enable
4. Go to "Credentials" → Create Credentials → API Key
5. Copy your API Key

### (Optional) Last.fm API
1. Go to: https://www.last.fm/api/account/create
2. Fill out form
3. Copy your API Key

### (Optional) RapidAPI for TikTok
1. Go to: https://rapidapi.com/marketplace/tiktok-scraper7
2. Subscribe (free tier available)
3. Copy your API Key from the dashboard

---

## 🔐 Step 5: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your keys
nano .env  # or use your favorite editor

# Add your keys:
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
YOUTUBE_API_KEY=your_youtube_api_key
LASTFM_API_KEY=your_lastfm_api_key (optional)
RAPIDAPI_KEY=your_rapidapi_key (optional)

# Other settings (leave as-is for local development)
FLASK_ENV=development
DEBUG=True
PORT=5000
```

**⚠️ IMPORTANT:** Never commit `.env` to GitHub. It's in `.gitignore`, but double-check.

---

## ▶️ Step 6: Run the Application

```bash
# Make sure venv is activated and you're in mai-scout directory
python app.py

# You should see:
# * Running on http://0.0.0.0:5000/
# * Debug mode: on
```

---

## 🌐 Step 7: Open in Browser

1. Open your browser
2. Go to: **http://localhost:5000**
3. You should see the MAI Scout homepage with search box

---

## 🧪 Step 8: Test the Features

### Test Scout
1. Type an artist name: "Bad Bunny"
2. Click "🚀 Analyze"
3. You should see artist data, top tracks, YouTube stats, etc.

### Test Evolution
1. Search for "Taylor Swift"
2. Click "📈 Evolution"
3. You should see growth charts and audience insights

### Test Spotlight
1. Search for "Peso Pluma"
2. Click "✨ Spotlight"
3. You should see a preview of the "link in bio" page
4. Copy link button should work

---

## ⚠️ Troubleshooting

### "ModuleNotFoundError: No module named 'flask'"
```bash
# Make sure venv is activated (check for (venv) in terminal)
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Re-install requirements
pip install -r requirements.txt
```

### "Port 5000 already in use"
```bash
# Use a different port
python app.py --port 5001

# Or find what's using 5000:
# macOS/Linux:
lsof -i :5000
kill -9 <PID>

# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### "401 Unauthorized" errors (Spotify/YouTube)
- Double-check your API keys in `.env`
- Make sure `.env` is in the `mai-scout` directory
- Restart Flask: `Ctrl+C` then `python app.py`

### "Artist not found"
- The search uses Spotify API - artist must exist in Spotify
- Try spelling variations
- Try full artist name (not abbreviations)

### TikTok stats not loading
- If you don't have `RAPIDAPI_KEY`, TikTok will show placeholder data
- This is normal - TikTok is optional
- Get API key from: https://rapidapi.com/marketplace/tiktok-scraper7

---

## 📂 Project Structure Reference

```
mai-scout/
├── app.py                      # Flask backend (main code)
├── index.html                  # Frontend (HTML + CSS + JavaScript)
├── evolution_data.py           # Mock data for Evolution feature
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variables template
├── .env                        # ACTUAL variables (YOU create this - don't commit!)
├── .gitignore                  # What git should ignore
├── Procfile                    # Railway deployment config
├── runtime.txt                 # Python version for Railway
└── README.md                   # Project documentation
```

---

## 🔄 Git Workflow (Important!)

Always follow this workflow:

```bash
# 1. Start of day - sync with remote
git pull origin main

# 2. Create a feature branch (NEVER work on main directly)
git checkout -b feature/my-feature-name

# 3. Make changes to files...
# (edit app.py, index.html, etc.)

# 4. Check what changed
git status
git diff

# 5. Stage changes
git add -A

# 6. Commit with meaningful message
git commit -m "Add feature: description of what you did"

# 7. Push to GitHub
git push origin feature/my-feature-name

# 8. On GitHub, create a Pull Request
# (review changes, then merge to main)

# 9. Switch back to main and pull latest
git checkout main
git pull origin main
```

---

## 🎯 First Task: Verify Everything Works

```bash
# 1. Make sure venv is activated
source venv/bin/activate

# 2. Run the app
python app.py

# 3. In another terminal (venv still active):
curl http://localhost:5000/

# 4. You should see HTML output (the app is working!)
```

---

## 📝 Development Tips

### Hot Reload
Flask automatically reloads when you change files (because `DEBUG=True`).
Just edit a file and refresh the browser.

### Check Logs
Flask logs appear in the terminal where you ran `python app.py`.
Useful for debugging API calls, errors, etc.

### Edit HTML/CSS/JS
- Files in `index.html` → refresh browser to see changes
- No need to restart Flask for frontend changes

### Edit Python (Backend)
- Changes to `app.py` or `evolution_data.py` → Flask auto-reloads
- Check terminal for any error messages

---

## 🔗 Next Steps

Once everything is working locally:

1. Read `PROJECT_CONTEXT.md` to understand the architecture
2. Read the comments in `app.py` to understand the code
3. Try making a small change (edit README.md or add a comment)
4. Commit and push to test the workflow
5. Start building new features in Claude Code!

---

## 💡 Useful Resources

- **Flask Docs:** https://flask.palletsprojects.com/
- **Spotify API:** https://developer.spotify.com/documentation/web-api
- **YouTube API:** https://developers.google.com/youtube/v3/docs
- **Tailwind CSS:** https://tailwindcss.com/docs
- **Git Basics:** https://git-scm.com/doc

---

**All set? Test your setup and then open the project in Claude Code!** 🚀
