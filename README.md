# MAI — Music Audience Insights

Real-time Spotify artist analytics with dark mode UI.

## Features

- 🎵 Search artists by name
- 📊 MAI Pulse Score (popularity algorithm)
- 🎭 Similar artists recommendation
- 🎵 Top 5 tracks with preview
- 📺 YouTube stats integration
- 🆕 Latest releases
- 🎨 Dark mode interface

## Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
export SPOTIPY_CLIENT_ID="your_id_here"
export SPOTIPY_CLIENT_SECRET="your_secret_here"
export YOUTUBE_API_KEY="your_youtube_key_here"

# Run Flask
python app.py
```

Visit: http://localhost:5000

## Deploy on Railway

1. Create account at [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Railway auto-detects Python
4. Add environment variables:
   - `SPOTIPY_CLIENT_ID`
   - `SPOTIPY_CLIENT_SECRET`
   - `YOUTUBE_API_KEY`
5. Deploy! 🚀

## API Keys

Get free API keys from:
- **Spotify**: https://developer.spotify.com/dashboard
- **YouTube**: https://console.cloud.google.com

No cost until massive scale (100k+ requests/month).

## Tech Stack

- Flask (backend)
- HTML5 + TailwindCSS (frontend)
- Spotify Web API
- YouTube Data API
- SQLite

---

Made with ❤️
