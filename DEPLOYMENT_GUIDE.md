# 🚀 BNPL EMI Risk Assessment - Render Deployment Guide

## Prerequisites

1. **GitHub Account** - Create one at https://github.com
2. **Render Account** - Sign up at https://render.com (free tier available)
3. **Git installed** - Download from https://git-scm.com

---

## Step 1: Push Your Project to GitHub

### 1.1 Initialize Git Repository

```bash
cd c:\Users\ayilu\OneDrive\Desktop\Documents\mp1
git init
```

### 1.2 Add All Files

```bash
git add .
```

### 1.3 Create Initial Commit

```bash
git commit -m "Initial commit: BNPL EMI Risk Assessment System"
```

### 1.4 Create a New Repository on GitHub

- Go to https://github.com/new
- **Repository name:** `bnpl-emi-risk` (or any name you prefer)
- **Description:** "AI-Powered BNPL EMI Default Risk Assessment System"
- **Public or Private:** Choose based on preference
- Click **Create repository**

### 1.5 Push to GitHub

Replace `YOUR_USERNAME` with your GitHub username:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bnpl-emi-risk.git
git push -u origin main
```

---

## Step 2: Update app.py for Production

The app needs one small modification for Render. Replace the last line in `backend/app.py`:

**OLD:**
```python
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

**NEW:**
```python
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "False") == "True"
    app.run(debug=debug, host="0.0.0.0", port=port)
```

Then commit and push:

```bash
git add backend/app.py
git commit -m "Update app.py for production deployment on Render"
git push
```

---

## Step 3: Deploy on Render

### 3.1 Sign Up on Render

Go to https://render.com and click **Sign up** (use GitHub for easier setup)

### 3.2 Create a New Web Service

1. Click **New +** → **Web Service**
2. **Connect GitHub repository:**
   - Click **Connect GitHub account** (if not connected)
   - Find and select your `bnpl-emi-risk` repository
   - Click **Connect**

### 3.3 Configure Deployment Settings

Fill in the following fields:

| Field | Value |
|-------|-------|
| **Name** | `bnpl-emi-risk` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r backend/requirements.txt` |
| **Start Command** | `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app` |
| **Instance Type** | `Free` (for testing) or `Paid` (for production) |

### 3.4 Set Environment Variables (if needed)

Click **Advanced** → **Add Environment Variable**

**Optional variables:**
```
FLASK_DEBUG=False
SECRET_KEY=your-random-secret-key-here
```

To generate a secure SECRET_KEY, run:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Or use a strong passphrase.

### 3.5 Deploy

1. Click **Create Web Service**
2. Render will automatically build and deploy your app
3. Wait for deployment to complete (5-10 minutes)
4. Your app URL will be: `https://bnpl-emi-risk.onrender.com`

---

## Step 4: Verify Deployment

Once deployed, visit: `https://YOUR_RENDER_URL.onrender.com`

You should see:
- ✅ Home page with Login/Register buttons
- ✅ Database initialized
- ✅ ML model loaded
- ✅ Flask app running

---

## Step 5: Troubleshooting

### Issue: Build Failed

**Check logs:** Click your service → **Logs** tab

Common fixes:
- Ensure `requirements.txt` is in `backend/` directory
- Check Python version compatibility (3.11 recommended)
- Verify no syntax errors in `app.py`

### Issue: App Crashes After Deploy

Check the **Logs** tab for error messages. Common causes:
- Missing environment variables
- Database connection issues
- ML model not found

### Issue: Static Files Not Loading

If CSS/JS files aren't loading:
1. The app should serve frontend from `../frontend` directory
2. Ensure paths in `app.py` are correct

### Issue: Database Errors

On first deploy:
- Render creates a new SQLite database automatically
- Run DB initialization: Check logs for `✅ Database fully initialized`
- The app handles migrations automatically

---

## Step 6: Enable Custom Domain (Optional)

1. In Render dashboard, click your service
2. Go to **Settings**
3. Click **Add Custom Domain**
4. Enter your domain (e.g., `bnpl.yourdomain.com`)
5. Follow DNS configuration instructions

---

## Step 7: Auto-Deploy on GitHub Push

Render automatically deploys whenever you push to GitHub!

```bash
# Make changes locally
git add .
git commit -m "Feature: Add new functionality"
git push origin main
# Render will automatically redeploy!
```

---

## Important Notes

### Database
- Uses **SQLite** (stored on Render's filesystem)
- Data persists between deployments
- For production, consider migrating to PostgreSQL:
  - PostgreSQL add-on: Free tier available on Render
  - Update connection string in `config.py`

### File Uploads
- Uploaded files stored in `backend/uploads/`
- **⚠️ Warning:** Files deleted when service is spun down (free tier)
- For production: Use AWS S3 or similar cloud storage

### ML Models
- `random_forest_model.pkl` and `scaler.pkl` should be in `backend/models/`
- Ensure these files are in Git (or download on deploy)

### Session Security
- Change the `SECRET_KEY` in `app.py` to a production value
- Add to Render environment variables for security

---

## Production Checklist

- [ ] Push code to GitHub
- [ ] Update `app.py` for production
- [ ] Set up Render account
- [ ] Create Web Service on Render
- [ ] Configure environment variables
- [ ] Verify deployment works
- [ ] Test login/logout functionality
- [ ] Check file uploads work
- [ ] Test ML predictions
- [ ] Monitor logs for errors

---

## Free Tier Limitations

Render's free tier includes:
- ✅ 750 hours/month of service
- ✅ Automatic HTTP-to-HTTPS redirects
- ✅ Auto-deploy on GitHub push
- ⚠️ Service spins down after 15 mins of inactivity (file uploads lost)
- ⚠️ Shared resources (may be slower)

**For production:** Upgrade to paid plan or enable "Keep Alive"

---

## Support

- **Render Docs:** https://render.com/docs
- **Flask Docs:** https://flask.palletsprojects.com
- **Gunicorn Docs:** https://gunicorn.org

---

## Next Steps After Deployment

1. **Collect User Data:** Create admin panel to monitor users
2. **Enable Logging:** Set up error tracking (e.g., Sentry)
3. **Add Email Alerts:** Notify users of predictions
4. **Optimize ML Model:** Improve accuracy with more training data
5. **Mobile App:** Create React Native or Flutter app
6. **Custom Domain:** Purchase domain and configure DNS

---

**Happy Deploying! 🚀**
