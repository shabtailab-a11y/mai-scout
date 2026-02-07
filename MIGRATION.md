# 🚀 MAI Migration Guide
## Music Audience Insights - Setup & Deployment

**Last Updated:** 2026-02-07  
**Current Status:** Ready for production migration

---

## 📋 Pre-Migration Checklist

- ✅ Git repository: `https://github.com/shabtailab-a11y/mai-scout.git`
- ✅ All code backed up to GitHub (main branch)
- ✅ Environment variables documented (.env.example)
- ✅ Dependencies locked (requirements.txt)
- ✅ Procfile configured for Railway/Heroku

---

## 🔧 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/shabtailab-a11y/mai-scout.git
cd mai-scout
```

### 2. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
```

Then edit `.env` and fill in your API credentials:
- `SPOTIPY_CLIENT_ID` - From Spotify Developer Dashboard
- `SPOTIPY_CLIENT_SECRET` - From Spotify Developer Dashboard
- `YOUTUBE_API_KEY` - From Google Cloud Console
- `LASTFM_API_KEY` - From Last.fm API (optional)

### 5. Start the Server

```bash
# Development mode
python app.py

# Production mode (with Gunicorn)
gunicorn app:app

# Custom port
python app.py --port 8000
```

Server runs on: `http://localhost:5000`

---

## 📦 Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Backend** | Flask | 3.0.0 |
| **Web Server** | Gunicorn | 21.2.0 |
| **Language** | Python | 3.11+ |
| **APIs** | Spotify, YouTube | Latest |
| **Frontend** | HTML5 + CSS3 + JS | Vanilla |
| **Deployment** | Docker / Railway | Latest |

---

## 📋 Critical Dependencies

```
Flask==3.0.0                          # Web framework
Flask-CORS==4.0.0                     # CORS support
spotipy==2.22.1                       # Spotify API client
google-api-python-client==2.106.0     # YouTube API client
google-auth-httplib2==0.2.0           # Google auth
google-auth-oauthlib==1.2.0           # Google OAuth
requests==2.31.0                      # HTTP library
gunicorn==21.2.0                      # Production WSGI server
```

**Note:** `beautifulsoup4` and `lxml` have been REMOVED (no longer used)

---

## 🚀 Deployment Options

### Option A: Railway (Current - Recommended)

1. Connect GitHub repo to Railway
2. Set environment variables in Railway dashboard
3. Auto-deploy on `git push` to main branch

**Current URL:** `https://web-production-19d8d.up.railway.app/`

```bash
# Manual deployment
railway up
```

### Option B: Google Antigravity (New Target)

1. Clone repo to Antigravity environment
2. Create `.env` from `.env.example`
3. Run: `python app.py` or `gunicorn app:app`

### Option C: Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "app:app"]
```

Build & run:
```bash
docker build -t mai-scout .
docker run -p 5000:5000 --env-file .env mai-scout
```

---

## 🔍 Project Structure

```
mai-scout/
├── app.py                    # Main Flask application
├── reports.py               # Reports server (port 5003)
├── index.html              # Frontend UI
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── Procfile               # Railway/Heroku config
├── runtime.txt            # Python version specification
├── MIGRATION.md          # This file
├── DEPLOYMENT.md         # Deployment notes
└── reports/
    ├── chartmetric_api_research.md
    ├── demographics_scraper_demo.py
    ├── cities_database.html
    └── cities_database.csv
```

---

## 🔌 API Endpoints

### Spotify Integration
- `POST /api/scout` - Get artist data + geography
  - Request: `{"artist_name": "Bad Bunny"}`
  - Response: Artist profile, MAI Pulse score, demographics

- `POST /api/search` - Search for artists
  - Request: `{"query": "artist name"}`
  - Response: List of matching artists

- `POST /api/geography` - Get geographic distribution
  - Request: `{"artist_name": "Bad Bunny"}`
  - Response: Top 5 countries with listener counts

### Reports Server (Optional - port 5003)
- `GET /reports` - Index of all reports
- `GET /reports/cities` - Cities database (JSON)
- `GET /reports/chartmetric` - Chartmetric research
- `GET /reports/demographics-scraper` - Demographics scraper docs

---

## 🔐 Security Notes

1. **Never commit .env** - It's in .gitignore for a reason
2. **API Keys are sensitive** - Keep them private
3. **Database credentials** - Should be in environment variables only
4. **CORS enabled** - Check `app.py` for allowed origins

---

## 📊 Monitoring & Logs

### Railway
- Logs visible in Railway dashboard
- Real-time deployment status
- Performance metrics

### Local Development
```bash
# Enable debug logging
export FLASK_DEBUG=True
python app.py
```

### Production
Use Gunicorn with logging:
```bash
gunicorn app:app --access-logfile - --error-logfile - --log-level info
```

---

## 🚨 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'spotipy'"
**Solution:** `pip install -r requirements.txt`

### Issue: "API Authentication Failed"
**Solution:** Check .env file, verify API keys are correct

### Issue: "Port 5000 already in use"
**Solution:** `python app.py --port 8000` or `lsof -ti:5000 | xargs kill`

### Issue: "CORS errors in browser"
**Solution:** Already enabled in app.py, but verify origin headers

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-XX | Initial deployment (Railway) |
| 1.1 | 2026-02-07 | Add reports server, update docs |
| 1.2 | 2026-02-07 | Pre-migration to Antigravity |

---

## 🔄 Post-Migration Steps

After deployment to Google Antigravity:

1. ✅ Verify environment variables are set
2. ✅ Test `/` endpoint (should return index.html)
3. ✅ Test `/api/scout` with sample artist
4. ✅ Verify database connections (if any)
5. ✅ Check logs for errors
6. ✅ Monitor performance metrics
7. ✅ Update DNS/routing if needed

---

## 📞 Support

- **Repository:** https://github.com/shabtailab-a11y/mai-scout
- **Issues:** Use GitHub issues for bug reports
- **Documentation:** See README.md and DEPLOYMENT.md

---

**Status:** ✅ Ready for migration to Google Antigravity

Generated: 2026-02-07 16:14 UTC
