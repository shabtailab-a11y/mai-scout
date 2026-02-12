# 🚀 MAI Scout - Ready for Claude Code

## 📦 What You're Getting

I've prepared **4 files** for you to migrate to Claude Code:

1. **`CLAUDE_CODE_MIGRATION.md`** ← START HERE
   - Overview of Claude Code
   - Step-by-step instructions
   - Troubleshooting guide

2. **`PROJECT_CONTEXT.md`** ← READ THIS SECOND
   - What MAI Scout is
   - Features explained
   - API endpoints reference
   - Architecture overview

3. **`SETUP_LOCAL.md`** ← FOLLOW THIS WHEN SETTING UP
   - Step-by-step local environment setup
   - How to get API keys
   - Testing instructions
   - Git workflow

4. **Source Code** (from GitHub)
   - Clone from: https://github.com/shabtailab-a11y/mai-scout
   - All files ready to edit in Claude Code

---

## 🎯 Quick Start (3 Steps)

### STEP 1: Download These Files
Save these 3 files to your computer:
- `CLAUDE_CODE_MIGRATION.md`
- `PROJECT_CONTEXT.md`
- `SETUP_LOCAL.md`

### STEP 2: Clone the Repo
```bash
git clone https://github.com/shabtailab-a11y/mai-scout.git
cd mai-scout
```

### STEP 3: Open in Claude Code
1. Go to Claude.ai
2. Click "Code" or "Artifacts"
3. Click "Upload Files"
4. Upload the `mai-scout` folder
5. You're ready to work!

---

## 📖 What to Do Next

### Reading Order

**BEFORE opening Claude Code:**
1. ✅ Read `CLAUDE_CODE_MIGRATION.md` (5 min)
2. ✅ Read `PROJECT_CONTEXT.md` (10 min)

**THEN follow:**
1. ✅ Read `SETUP_LOCAL.md` (15 min)
2. ✅ Clone repo and run locally (30 min)
3. ✅ Test all features work (10 min)
4. ✅ Open in Claude Code and start building!

---

## 💻 Using Claude Code

Once everything is set up locally, you can:

### In Claude Code, ask things like:

**Architecture Questions:**
```
"Explain how the Evolution feature works"
"What does the MAI Pulse formula do?"
"How is TikTok data fetched?"
```

**Feature Requests:**
```
"Add a dark mode toggle to the homepage"
"Create a favorites list for artists"
"Add export to PDF for Evolution charts"
```

**Code Changes:**
```
"Refactor the scout_artist() function to reduce duplication"
"Add error handling to the Spotlight page"
"Optimize the API calls"
```

**Debugging:**
```
"Why is Evolution not loading for some artists?"
"TikTok stats show errors - debug this"
"The Spotlight form isn't working - fix it"
```

### Workflow in Claude Code:

1. **Edit files** in the editor
2. **Run terminal commands** (git, python, etc.)
3. **Test locally** (python app.py)
4. **Commit changes** (git add -A && git commit)
5. **Push to GitHub** (git push origin feature-branch)
6. **Create PR** on GitHub for review

---

## 🎁 What's Included

### Backend (app.py)
- Flask server
- Spotify integration
- YouTube integration
- TikTok integration
- Evolution endpoints
- Spotlight endpoints

### Frontend (index.html)
- Search interface
- Artist results display
- Evolution modals with charts
- Spotlight preview
- Responsive design
- Dark mode

### Data (evolution_data.py)
- 5 artists with complete evolution data
- Quantified growth metrics
- Key audience insights

### Configuration
- `.env.example` (template)
- `requirements.txt` (dependencies)
- `Procfile` (Railway deployment)
- `.gitignore` (what not to commit)

---

## 🚀 After Local Setup

Once you've got it running locally and pushed to GitHub, you can:

### Phase 2 Features (Ready to Build)
- [ ] Spotlight automation (detect releases)
- [ ] Email notifications to subscribers
- [ ] Analytics dashboard
- [ ] Database migration (from in-memory to SQLite)
- [ ] Artist management dashboard
- [ ] Premium features

### Improvements
- [ ] Add more artists to Evolution
- [ ] Better TikTok integration
- [ ] Mobile app (React Native?)
- [ ] API for third-party tools
- [ ] Artist authentication
- [ ] Custom Spotlight branding

---

## ⚠️ Important Notes

### Security
- **Never commit `.env`** - It's in `.gitignore`, keep it that way
- **Don't expose API keys** in chat or public places
- Use environment variables for all secrets

### GitHub
- **Always use branches** - Never edit `main` directly
- **Push frequently** - Backup your changes
- **Write clear commit messages** - Future you will thank you

### API Keys
- Spotify: Free, need account
- YouTube: Free, need Google account
- Last.fm: Free, optional
- RapidAPI (TikTok): Free tier available, optional

### Rate Limits
- Spotify: Very generous for development
- YouTube: 10,000 quota units/day (plenty for dev)
- RapidAPI: Check their limits (usually fine for dev)

---

## 🆘 Common Issues

### "Everything's broken after setup"
1. Check that venv is activated: `(venv)` should be in your terminal
2. Check `.env` file exists and has valid API keys
3. Restart Flask: `Ctrl+C` then `python app.py`
4. Check for error messages in the terminal

### "Claude Code won't open the folder"
1. Make sure folder is unzipped
2. Try uploading individual files instead
3. Or clone fresh from GitHub within Claude Code

### "API errors after first run"
1. Double-check your API keys in `.env`
2. Verify they're valid on their respective websites
3. Wait a few seconds - APIs sometimes need time to activate

### "Git not working in Claude Code"
1. Configure git:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"
   ```
2. Use HTTPS (not SSH) for simpler authentication
3. Generate GitHub token if needed: https://github.com/settings/tokens

---

## 📞 Still Need Help?

### Documentation Files (Read in Order)
1. `CLAUDE_CODE_MIGRATION.md` - Overview & setup
2. `PROJECT_CONTEXT.md` - What the app does
3. `SETUP_LOCAL.md` - Step-by-step local setup
4. `README.md` (in mai-scout folder) - General docs

### In Claude Code
- Ask Claude to explain any part of the code
- Say: "Explain what this function does" + paste code
- Say: "Help me debug this error" + paste error message

### GitHub Issues
- You can create issues on GitHub if something is broken
- Tag with `bug` or `feature request`

---

## ✨ Ready to Go?

1. **Download the 3 instruction files** (this folder)
2. **Follow SETUP_LOCAL.md** on your computer
3. **Test everything works locally**
4. **Open in Claude Code**
5. **Start building Phase 2!**

---

## 🎯 First Tasks in Claude Code

Once you're set up, try these easy wins:

1. **Update README.md** with new features
2. **Add a comment** in app.py and commit
3. **Change the page title** in index.html
4. **Add a new artist** to evolution_data.py
5. **Improve the UI** (CSS tweaks)

These get you comfortable with the workflow before tackling bigger features.

---

**Welcome to Claude Code development! 🚀**

Start with `CLAUDE_CODE_MIGRATION.md` and you'll be building in minutes.

Questions? Ask Claude in Code - it's really smart about this stuff.
