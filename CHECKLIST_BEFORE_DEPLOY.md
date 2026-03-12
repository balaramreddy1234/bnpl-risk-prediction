# ✅ Pre-Deployment Checklist for Render

## Backend Files ✓

- [ ] `backend/app.py` - Updated for production (PORT from environment)
- [ ] `backend/requirements.txt` - All dependencies listed
- [ ] `backend/config.py` - Configuration file exists
- [ ] `backend/database/` - Database initialization files present
- [ ] `backend/ml/` - ML modules for predictions
- [ ] `backend/models/` - Random Forest model files (optional for deployment)
- [ ] `backend/utils/` - Utility functions (risk_score, pdf_generator, etc.)
- [ ] `backend/templates/` - Helper templates
- [ ] `backend/tests/` - Test files

## Frontend Files ✓

- [ ] `frontend/index.html` - Home page (redirects to dashboard if logged in)
- [ ] `frontend/pages/` - All pages (login, register, dashboard, predict, upload, etc.)
- [ ] `frontend/css/` - Stylesheets loaded
- [ ] `frontend/js/` - JavaScript files for functionality
- [ ] `frontend/assets/` - Images and other assets

## Deployment Configuration Files ✓

- [ ] `Procfile` - Web service startup command
- [ ] `runtime.txt` - Python version (3.11.4)
- [ ] `.gitignore` - Excludes unnecessary files
- [ ] `requirements.txt` - Dependencies with versions (in `backend/`)
- [ ] `DEPLOYMENT_GUIDE.md` - This deployment guide
- [ ] `RENDER_QUICKSTART.md` - Quick reference

## Git & GitHub Setup ✓

- [ ] GitHub account created
- [ ] Git initialized in project (`git init`)
- [ ] GitHub repository created (public or private)
- [ ] Code pushed to GitHub (`git push origin main`)
- [ ] Repository accessible from Render

## App Configuration ✓

- [ ] `SECRET_KEY` defined in app (can be changed in Render env vars)
- [ ] Flask-CORS enabled for frontend
- [ ] Session management configured (24-hour lifetime)
- [ ] Database auto-initialization working
- [ ] Authentication routes protected with `@login_required`
- [ ] All API endpoints have error handling

## Database ✓

- [ ] SQLite database initialized locally with `init_db.py`
- [ ] User table created with columns for login
- [ ] Predictions table created
- [ ] Database migrations handled automatically
- [ ] File permissions allow database creation on Render

## Authentication System ✓

- [ ] `/register` endpoint working (creates password hash)
- [ ] `/login` endpoint working (creates session)
- [ ] `/logout` endpoint working (clears session)
- [ ] `/auth/check` endpoint created (verifies user logged in)
- [ ] Protected routes redirect to login page
- [ ] Dashboard shows "Welcome, [Username]!" when logged in
- [ ] Navbar shows user profile on protected pages

## Frontend Features ✓

- [ ] Home page shows Login/Register buttons (if not logged in)
- [ ] Home page redirects to Dashboard (if logged in)
- [ ] Dashboard is default landing page
- [ ] Top-right shows "Welcome, [Username]!" with dropdown
- [ ] Logout button clears session
- [ ] Protected pages (Upload, Predict, EMI History, etc.) require login
- [ ] All pages have consistent navbar header
- [ ] CSS and JS files load correctly

## ML Model ✓

- [ ] Random Forest model trained and saved (`random_forest_model.pkl`)
- [ ] Scaler fitted and saved (`scaler.pkl`)
- [ ] Models located in `backend/models/`
- [ ] Model loading in `app.py` handles errors gracefully
- [ ] Prediction endpoint (`/predict`) working locally

## File Upload Feature ✓

- [ ] Upload directory created (`backend/uploads/`)
- [ ] Report directory created (`backend/reports/`)
- [ ] File size limit set (16MB in app.py)
- [ ] CSV and PDF parsing working
- [ ] Predictions stored in database

## Common Issues Fixed ✓

- [ ] No `debug=True` in production code
- [ ] PORT environment variable read from system
- [ ] Gunicorn in requirements.txt (WSGI server)
- [ ] Absolute paths for static files
- [ ] Frontend served from correct directory
- [ ] Database connection string configurable

## Render Dashboard Setup ✓

- [ ] Account created on https://render.com
- [ ] GitHub repository connected
- [ ] Web Service created
- [ ] **Environment Variables Set:**
  - [ ] `FLASK_DEBUG=False`
  - [ ] `SECRET_KEY=[your-secure-key]`
  - [ ] `PORT=[auto-assigned by Render]`
- [ ] **Build Command:** `pip install -r backend/requirements.txt`
- [ ] **Start Command:** `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
- [ ] Instance type selected (free or paid)

## Pre-Deployment Testing ✓

- [ ] Ran `python backend/app.py` locally - no errors
- [ ] Visited `http://127.0.0.1:5000` - page loads
- [ ] Home page shows without login
- [ ] Created test user (register page)
- [ ] Logged in - redirects to dashboard
- [ ] Dashboard shows username
- [ ] Can access predict page - protected
- [ ] Can access upload page - protected
- [ ] Logout button works - redirects to home
- [ ] Opened protected page without login - redirects to login
- [ ] Database file created (`.db` file exists)
- [ ] All CSS and JS load (no 404 errors in console)

## Secret Management ✓

- [ ] `SECRET_KEY` changed from default
- [ ] Password hashing using `werkzeug.security`
- [ ] Session cookies are HTTPOnly
- [ ] No API keys in source code (use env vars)
- [ ] CORS properly configured

## Post-Deployment Testing ✓

After deploying to Render, test:
- [ ] Visit app URL - home page loads
- [ ] Register new user - works
- [ ] Login - redirects to dashboard
- [ ] Dashboard shows username
- [ ] Can make predictions
- [ ] Can upload CSV files
- [ ] Can view history
- [ ] Logout - session cleared
- [ ] Check application logs on Render - no errors
- [ ] Database auto-initialized on first run

## Performance Optimization ✓

- [ ] Gunicorn workers configured (usually auto on Render)
- [ ] Static files served efficiently
- [ ] Database queries optimized
- [ ] ML model loaded once (not on every request)
- [ ] Image compression for uploads

## Security Review ✓

- [ ] HTTPS enabled (automatic on Render)
- [ ] CORS headers configured correctly
- [ ] Session expiration set (24 hours)
- [ ] Password minimum requirements enforced
- [ ] User input validated and sanitized
- [ ] SQL injection protection (using parameterized queries)
- [ ] XSS protection (HTTPOnly cookies)

## Documentation ✓

- [ ] README.md describes project
- [ ] DEPLOYMENT_GUIDE.md detailed deployment steps
- [ ] RENDER_QUICKSTART.md quick reference
- [ ] Code comments explaining key functions
- [ ] Database schema documented

## Final Steps ✓

- [ ] Review all files in Git (`.gitignore` working?)
- [ ] Commit final changes: `git commit -m "Ready for Render deployment"`
- [ ] Push to GitHub: `git push origin main`
- [ ] Start deployment on Render
- [ ] Monitor logs during deployment
- [ ] Test functionality on deployed app
- [ ] Set up monitoring alerts

---

## 🎯 Deployment Status

**Before Deploying:** _____ (Check all boxes above)
**Deploying:** ✓ Code pushed to GitHub
**Testing:** ✓ App working on Render
**Live:** ✓ Users can access the app

---

**Total Prep Time:** ~30 minutes
**Deployment Time:** 5-10 minutes
**Total Time:** ~40 minutes

**You're ready to deploy! 🚀**
