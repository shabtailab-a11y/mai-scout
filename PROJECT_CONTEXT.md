# 📊 MAI Scout - Project Context Summary

## 🎯 What is MAI?

**MAI** = **Music Audience Insights**

A smart analytics platform for musicians/managers to:
- Analyze artist reach (Spotify followers, YouTube subscribers)
- View audience growth trajectory (Evolution feature)
- Create "link in bio" pages (Spotlight feature)
- Capture fan emails for marketing

**Live URL:** https://web-production-19d8d.up.railway.app/

---

## 🏗️ Tech Stack

### Backend
- **Framework:** Flask (Python)
- **APIs Used:**
  - Spotify API (artist data, top tracks, similar artists)
  - YouTube API (channel stats, videos)
  - RapidAPI (TikTok data - optional)
  - Last.fm API (optional)

### Frontend
- **HTML5** with Tailwind CSS
- **JavaScript** (vanilla, no frameworks)
- **Chart.js** (Evolution visualizations)

### Deployment
- **Railway.app** (auto-deploys on git push to main)
- **GitHub** (shabtailab-a11y/mai-scout)
- **Database:** In-memory storage (JSON-like, Python dict) + file-based for persistence

---

## ✨ Features

### 1️⃣ Scout (Main Feature)
Search any artist by name → get:
- Basic info (followers, genres, image)
- Top 5 tracks with preview players
- Similar artists recommendations
- Recent releases
- YouTube stats (subscribers, top videos, recent videos)
- TikTok stats (auto-detected from artist name)
- Geographic distribution (top 5 countries by follower %)
- MAI Pulse score (proprietary algorithm)

**How it works:**
1. User enters artist name
2. Spotify API search (best match)
3. Auto-fetch YouTube + TikTok data
4. Calculate MAI Pulse = (Popularity × 1.5) + (Followers ÷ 1,000)
5. Display results

**Formula:**
```
MAI Pulse Score = (Popularity × 1.5) + (Followers / 1000)
0-1000 = 🌱 EMERGENTE
1000-10,000 = ⭐ ESTABLECIDO
10,000-50,000 = 🚀 EN ASCENSO
>50,000 = 🔥 TENDENCIA GLOBAL
```

### 2️⃣ Evolution (Growth Trajectory)
**Available for:** Bad Bunny, Taylor Swift, Peso Pluma, Catriel y Paco Amoroso, Feli Colina

Shows historical audience growth with:
- **Line Chart:** Audience Growth Index (1 Index = ~1,000 listeners)
- **Bar Chart:** Growth Multipliers per era
- **Timeline:** Key eras with milestones
- **Key Audience Insights:** Quantified growth patterns (with multipliers)
- **Key Insights:** General observations

**Example (Bad Bunny):**
- 2016-17: Trap Breakout (Index 1)
- 2018: Colabs + Crossover (Index 12, x12.0 growth)
- 2019: X 100pre Tour (Index 20, x1.67 growth)
- 2020-22: Streaming Domination (Index 65, x3.25 growth)
- 2023-26: Global Icon (Index 80, x1.23 growth)

### 3️⃣ Spotlight (Link in Bio)
Create a shareable "link in bio" page for each artist:
- Public URL: `https://mai.app/spotlight/artist_name`
- Shows: Artist photo, genres, Spotify link, YouTube link
- Email subscription box for fans
- Tracks clicks and subscribers (in-memory for now)

**Current MVP:**
- Basic info display
- Email capture
- In-memory subscriber storage (resets on app restart)

**Planned Phase 2:**
- Auto-update when new releases detected
- Email notifications to subscribers
- Analytics dashboard
- Database persistence

---

## 📁 Project Structure

```
mai-scout/
├── app.py                      # Main Flask app (500+ lines)
│   ├── Spotify integration
│   ├── YouTube integration
│   ├── TikTok integration
│   ├── Evolution routes
│   └── Spotlight routes
│
├── index.html                  # Frontend (1400+ lines)
│   ├── HTML structure
│   ├── Tailwind CSS
│   ├── Chart.js visualizations
│   └── Vanilla JavaScript
│
├── evolution_data.py           # Mock data (400+ lines)
│   ├── Bad Bunny (6 eras)
│   ├── Taylor Swift (4 eras)
│   ├── Peso Pluma (3 eras)
│   ├── Catriel y Paco Amoroso (3 eras)
│   └── Feli Colina (4 eras)
│
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
├── .gitignore                  # Git ignore rules
├── Procfile                    # Railway deployment config
├── runtime.txt                 # Python version
└── README.md                   # Project documentation
```

---

## 🔑 Key API Endpoints

### Scout
```
POST /api/scout
Input:  { "artist_name": "Bad Bunny" }
Output: { artist: {...}, mai_pulse: {...} }
```

### TikTok (Auto)
```
POST /api/artist-tiktok
Input:  { "artist_name": "Bad Bunny" }
Output: { status: "found", tiktok: {...} }
        OR { status: "not_found" }
```

### Geography
```
POST /api/geography
Input:  { "artist_name": "Bad Bunny" }
Output: { top_countries: [...], total_followers: 123456789 }
```

### Evolution
```
POST /api/evolution
Input:  { "artist_name": "Bad Bunny" }
Output: { status: "available", data: { eras: [...], insights: [...] } }
        OR { status: "coming_soon" }
```

### Spotlight Subscribe
```
POST /api/spotlight-subscribe
Input:  { "artist_name": "Bad Bunny", "email": "fan@example.com" }
Output: { status: "success", message: "..." }
```

### Spotlight Full Content
```
GET /api/spotlight-full/<artist_slug>
Output: HTML content (for modal preview)
```

### Spotlight Public Page
```
GET /spotlight/<artist_slug>
Output: Full HTML page (sharable link)
```

---

## 🎨 UI Components

### Main Page
- Search box (3 buttons: Analyze, Evolution, Spotlight)
- Quick demo buttons: Bad Bunny, Taylor Swift, Peso Pluma, Catriel y Paco Amoroso, Feli Colina

### Results Section
- Artist info (image, name, genres, followers, popularity)
- MAI Pulse score with category
- Top 5 tracks with preview players
- Similar artists grid
- Recent releases
- YouTube stats (if available)
- TikTok stats (if available)

### Evolution Modal
- 3 tabs: Preview, Editor (future), Analytics
- Line chart: Audience Growth Index
- Bar chart: Growth Multipliers
- Timeline: Key eras with details
- Key Audience Insights (quantified)
- Key Insights (general observations)

### Spotlight Modal
- Full Spotlight preview (as it appears on public page)
- Copy link button (sticky at bottom)
- Email subscription form

---

## 🔐 Environment Variables

```bash
# Required
SPOTIPY_CLIENT_ID=<get from developer.spotify.com>
SPOTIPY_CLIENT_SECRET=<get from developer.spotify.com>
YOUTUBE_API_KEY=<get from console.cloud.google.com>

# Optional
LASTFM_API_KEY=<get from last.fm/api>
RAPIDAPI_KEY=<get from rapidapi.com>

# App Config
FLASK_ENV=development|production
DEBUG=True|False
PORT=5000
```

---

## 📊 Current Stats

- **Lines of Code:** ~2,000 (excluding comments)
- **Artists in Evolution:** 5 (with mock data)
- **API Integrations:** 4 (Spotify, YouTube, Last.fm, RapidAPI)
- **Features:** 3 (Scout, Evolution, Spotlight MVP)
- **GitHub Commits:** 30+
- **Deployment:** Railway.app (auto-deploy on push)

---

## 🚀 Latest Updates (Feb 2026)

1. **Evolution Feature**
   - Added quantified multipliers for growth
   - Added Key Audience Insights (with venue capacities)
   - Real Index values (1-80 range) for all artists

2. **Spotlight Feature**
   - Created "link in bio" feature (MVP)
   - Email subscription capture
   - Public shareable pages
   - In-memory subscriber tracking

3. **UI Improvements**
   - Made Audience Growth Index scale interpretable (1 Index = 1K listeners)
   - Added K-format Y-axis labels
   - Improved Evolution visualizations

4. **Data Updates**
   - Updated Audience Index with real values for all quick demo artists
   - Added Feli Colina (indie artist) as example
   - Improved Key Audience Insights copy (more analytical)

---

## 🎯 Next Steps (Phase 2)

1. **Spotlight Automation**
   - Detect new Spotify releases
   - Detect new YouTube videos
   - Auto-update Spotlight page
   - Send emails to subscribers

2. **Analytics Dashboard**
   - Click tracking (already collecting, need UI)
   - Subscriber trends
   - Traffic source analysis
   - Engagement metrics

3. **Database Migration**
   - Replace in-memory storage with SQLite/PostgreSQL
   - Persist artist data
   - Save subscriber lists
   - Analytics history

4. **Email System**
   - Integrate Sendgrid or Mailgun
   - Create email templates
   - Schedule release notifications
   - Unsubscribe management

5. **Premium Features**
   - Artist dashboard (own Spotlight management)
   - Custom branding
   - Advanced analytics
   - API access for third-party tools

---

## 📚 How to Use This Context

When working in Claude Code, you can:

1. **Ask about the architecture:**
   "How does the Evolution feature work?"
   
2. **Request features:**
   "Add dark mode toggle to the Spotlight page"
   
3. **Debug issues:**
   "Why is TikTok not loading for some artists?"
   
4. **Refactor code:**
   "Clean up the app.py to reduce duplication"

Always reference specific files:
- "In app.py line 150..."
- "Update the scout_artist() function..."
- "The evolution_data.py has 5 artists..."

---

## 🔗 Useful Links

- **GitHub:** https://github.com/shabtailab-a11y/mai-scout
- **Live Site:** https://web-production-19d8d.up.railway.app/
- **Spotify API Docs:** https://developer.spotify.com/documentation/web-api
- **YouTube API Docs:** https://developers.google.com/youtube/v3
- **Railway Docs:** https://docs.railway.app/
- **Flask Docs:** https://flask.palletsprojects.com/

---

**Ready to work? Go to CLAUDE_CODE_MIGRATION.md for setup instructions!** 🚀
