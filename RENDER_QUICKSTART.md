# 🚀 Quick Deploy to Render - Step-by-Step

## 5 Minute Setup Guide

### Step 1: Push to GitHub (5 min)

```powershell
# Open PowerShell in your project folder
cd c:\Users\ayilu\OneDrive\Desktop\Documents\mp1

# Initialize git
git init
git add .
git commit -m "BNPL EMI Risk - Ready for Render deployment"

# Create repo on GitHub (https://github.com/new) and get the URL
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bnpl-emi-risk.git
git push -u origin main
```

---

### Step 2: Deploy on Render (3 min)

1. **Visit:** https://render.com
2. **Sign up** → Connect GitHub
3. **Click:** New → Web Service
4. **Select** your `bnpl-emi-risk` repository
5. **Fill in settings:**
   - **Name:** `bnpl-emi-risk`
   - **Environment:** Python 3
   - **Build:** `pip install -r backend/requirements.txt`
   - **Start:** `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
6. **Click:** Create Web Service
7. **Wait:** 5-10 minutes for deployment

---

### Step 3: Test Your App

✅ Visit: `https://bnpl-emi-risk.onrender.com`
- Should see home page with Login/Register buttons
- Check logs for any errors

---

## 🎯 What Happens During Deploy

1. **Build Phase:**
   - Render pulls your code from GitHub
   - Installs Python 3.11
   - Installs dependencies from `requirements.txt`
   - Sets up gunicorn WSGI server

2. **Run Phase:**
   - Starts Flask app on Render server
   - Database auto-initializes
   - ML models load
   - Ready to accept users

---

## 🛠️ Environment Variables (Optional)

Click **Advanced** in Render settings and add:

```
FLASK_DEBUG=False
SECRET_KEY=your-secure-key-here
DATABASE_URL=sqlite:///bnpl.db
```

---

## 📝 Files Created for Deployment

✅ `Procfile` - Startup command for Render
✅ `runtime.txt` - Python version specification
✅ `DEPLOYMENT_GUIDE.md` - Detailed guide with troubleshooting
✅ `.gitignore` - Ignores unnecessary files

---

## ✨ Auto-Deploy Magic

Every time you push to GitHub:
```bash
git add .
git commit -m "Your message"
git push origin main
```

Render automatically deploys! No manual steps needed.

---

## 📊 Monitor Your App

1. **Logs:** https://dashboard.render.com → Select service → Logs tab
2. **Metrics:** CPU, Memory, Request count
3. **Deployments:** History of all deployments

---

## 🚨 Common Issues

| Issue | Fix |
|-------|-----|
| Build fails | Check logs, ensure `requirements.txt` exists |
| App crashes | Set `FLASK_DEBUG=False` in environment |
| Files not loading | Check paths in `app.py` |
| Login doesn't work | Database initializing, wait 1 minute |

---

## 💡 Pro Tips

1. **Keep Free:** Use free tier but add "Keep Alive" for $7/month
2. **Better Uploads:** Use AWS S3 for file storage (not local disk)
3. **Email Alerts:** Integrate SendGrid for notifications
4. **Custom Domain:** Buy domain and update DNS settings
5. **Backups:** Download SQLite database before updates

---

## 📚 Full Guide

See `DEPLOYMENT_GUIDE.md` for complete documentation including:
- PostgreSQL setup
- Custom domains
- Production checklist
- Troubleshooting

---

**Questions?** Check https://render.com/docs
