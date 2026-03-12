# 🏦 BNPL EMI Default Risk Assessment System

An AI-powered web application for predicting EMI (Equated Monthly Installment) default risk using machine learning. Built with Flask, React-style vanilla JS, and a Random Forest model.

**Live Demo:** https://bnpl-emi-risk.onrender.com (When deployed)

---

## 📋 Features

### 🔐 Authentication & Security
- User registration with password hashing
- Email/password login with session management
- Protected pages that require authentication
- 24-hour session expiration
- HTTPOnly cookies for XSS prevention

### 📊 Risk Assessment
- **Individual Predictions:** Enter EMI details and get instant risk classification
- **Batch Analysis:** Upload CSV/PDF files with multiple applicants
- **Risk Categories:** Low Risk, Medium Risk (Pending), High Risk (Declined)
- **Smart Suggestions:** Proactive recommendations to improve eligibility
- **PDF Reports:** Downloadable detailed risk reports

### 📈 Machine Learning
- **Random Forest Classifier:** Trained on 1,000+ applicant records
- **Feature Engineering:** EMI-to-income ratio, payment delay ratio
- **Probability Scoring:** Confidence percentage for each prediction
- **Explainability:** Transparent decision factors shown to users

### 💾 Data Management
- **Prediction History:** Track all assessments over time
- **Batch Processing:** Analyze up to 1,000 applicants per file
- **Data Persistence:** SQLite database stores all records
- **Filter & Search:** Sort predictions by status and date

### 🎨 User Interface
- **Responsive Design:** Works on desktop and mobile
- **Dashboard:** Central hub for all features
- **Intuitive Forms:** Step-by-step prediction process
- **Risk Transparency:** Detailed explanation of decision factors

---

## 🚀 Quick Start

### Option 1: Local Development (Recommended for testing)

#### Prerequisites
- Python 3.11+
- Git
- pip package manager

#### Setup

```bash
# Clone (or extract) your project
cd c:\Users\ayilu\OneDrive\Desktop\Documents\mp1

# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

**Visit:** http://127.0.0.1:5000

#### Default Test Account
- Email: test@example.com
- Password: Test@123456

(Create one first if needed)

---

### Option 2: Deploy to Render (Easy cloud hosting)

#### Quick Deploy (5 minutes)

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "BNPL Risk Assessment System"
   git remote add origin https://github.com/YOUR_USERNAME/bnpl-emi-risk.git
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Visit https://render.com
   - Click New → Web Service
   - Select your GitHub repository
   - Set Build: `pip install -r backend/requirements.txt`
   - Set Start: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
   - Click Create Web Service

3. **Wait** 5-10 minutes for deployment
4. **Visit** your app URL (shown in Render dashboard)

**For detailed instructions, see [RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)**

---

## 📁 Project Structure

```
mp1/
├── backend/                    # Flask backend
│   ├── app.py                 # Main Flask application
│   ├── config.py              # Configuration settings
│   ├── requirements.txt        # Python dependencies
│   ├── database/              # Database setup & schema
│   │   ├── db_connection.py
│   │   ├── init_db.py
│   │   └── schema.sql
│   ├── ml/                    # Machine learning modules
│   │   ├── train_model.py
│   │   ├── predict.py
│   │   ├── data_preprocessing.py
│   │   └── evaluate_model.py
│   ├── models/                # Saved ML models
│   │   ├── random_forest_model.pkl
│   │   └── scaler.pkl
│   ├── utils/                 # Utility functions
│   │   ├── risk_score.py
│   │   ├── pdf_generator.py
│   │   └── validators.py
│   ├── uploads/               # User uploads directory
│   ├── reports/               # Generated PDF reports
│   └── tests/                 # Test files
│
├── frontend/                  # Web UI
│   ├── index.html            # Home page
│   ├── pages/                # Web pages
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── predict.html
│   │   ├── upload.html
│   │   ├── emi_history.html
│   │   ├── transparency.html
│   │   └── admin.html
│   ├── css/                  # Stylesheets
│   │   ├── base.css
│   │   ├── dashboard.css
│   │   ├── forms.css
│   │   └── tables.css
│   ├── js/                   # JavaScript
│   │   ├── auth.js           # Auth & logout
│   │   ├── dashboard.js
│   │   ├── predict.js
│   │   ├── upload.js
│   │   └── prediction_history.js
│   └── assets/               # Images & files
│       └── profile_pics/     # User profile photos
│
├── dataset/                  # Training data
│   ├── raw_bnpl_data.csv
│   ├── cleaned_bnpl_data.csv
│   └── feature_engineered.csv
│
├── docs/                     # Documentation
├── deployment/               # Deployment configs
└── Deployment files:
    ├── Procfile              # Render startup command
    ├── runtime.txt           # Python version
    ├── .gitignore            # Git exclusions
    ├── RENDER_QUICKSTART.md  # 5-min deployment guide
    ├── DEPLOYMENT_GUIDE.md   # Complete guide
    ├── CHECKLIST_BEFORE_DEPLOY.md
    └── DEPLOYMENT_SUMMARY.md
```

---

## 🔧 Technology Stack

### Backend
- **Framework:** Flask 2.3.2
- **WSGI Server:** Gunicorn 21.2.0 (production)
- **Authentication:** werkzeug.security (password hashing)
- **Database:** SQLite3
- **ML Library:** Scikit-learn 1.3.0
- **Data Processing:** Pandas 2.0.3, NumPy 1.24.3
- **PDF Generation:** ReportLab 4.0.5, PyPDF2
- **CORS:** Flask-CORS 4.0.0

### Frontend
- **HTML/CSS/JavaScript** (Vanilla, no frameworks)
- **Responsive Design:** CSS Grid & Flexbox
- **Icons:** Unicode & ASCII art
- **Storage:** Browser localStorage, HTTP sessions

### Deployment
- **Hosting:** Render.com (or any WSGI-compatible platform)
- **Database Server:** SQLite (local) / PostgreSQL (production)
- **File Storage:** Local filesystem / AWS S3 (production)
- **Domain:** Custom domain support available

---

## 📊 How It Works

### 1. User Registration & Login
```
User → Register (email, password) → Database
     → Login → Flask session → Secure cookie
```

### 2. Individual Risk Prediction
```
User input (Income, Loan, EMI, etc.)
     ↓
Feature Engineering
     ↓
Random Forest Model
     ↓
Risk Score (probability 0-1)
     ↓
Classification (Low/Medium/High)
     ↓
Smart Suggestions + PDF Report
```

### 3. Batch File Analysis
```
CSV/PDF Upload (up to 1,000 records)
     ↓
Data Parsing & Validation
     ↓
Feature Engineering
     ↓
Parallel Predictions
     ↓
Categorization (Eligible/Pending/Declined)
     ↓
Summary Report
```

### 4. Data Storage
```
User Account → SQLite Database
Predictions → History Table
Feedback → Feedback Table
```

---

## 🎯 API Endpoints

All endpoints require authentication unless noted.

### Authentication
- `POST /register` - Create account
- `POST /login` - User login
- `GET /logout` - Clear session
- `GET /auth/check` - Check if logged in

### User Profile
- `GET /user/profile` - Get user info
- `POST /user/update` - Update profile
- `POST /user/change-password` - Change password

### Predictions
- `POST /predict` - Single prediction
- `POST /upload` - Batch upload & analysis
- `GET /user/prediction-history` - View history
- `POST /user/delete-history` - Delete predictions
- `POST /generate-member-pdf` - Generate report

### Support
- `POST /user/feedback` - Submit feedback
- `GET /download-report/<filename>` - Download PDF

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | ~87% |
| Precision | ~85% |
| Recall | ~89% |
| Model Type | Random Forest |
| Training Samples | 1000+ |
| Features | 9 (7 input + 2 engineered) |

---

## 🔒 Security Features

✅ **Password Security**
- Minimum 8 characters, 4 letters, 2 numbers, 2 special chars
- Hashed with werkzeug.security.generate_password_hash

✅ **Session Management**
- HTTPOnly cookies (no JavaScript access)
- 24-hour expiration
- Secure SameSite attribute

✅ **Data Protection**
- SQLite database on server
- User passwords never logged
- File uploads in secure directory

✅ **API Security**
- CORS configured for frontend only
- Protected routes with @login_required
- Input validation on all endpoints

---

## 🚀 Deployment Options

### Render.com (Recommended - Easy)
- Free tier available (750 hrs/month)
- Auto-deploy on GitHub push
- Built-in HTTPS
- See [RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)

### Heroku (Traditional)
- Paid only (~$7/month minimum)
- Similar setup to Render

### AWS EC2 (Advanced)
- Full control
- Higher cost
- Requires AWS knowledge

### Azure App Service
- Microsoft cloud
- Good integration with Visual Studio

### DigitalOcean
- Simple droplets
- ~$5/month

---

## 📝 Configuration

### Local Development
Edit `backend/config.py`:
```python
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")
SECRET_KEY = "your-secret-key"
```

### Production (Render)
Set environment variables in Render dashboard:
```
FLASK_DEBUG=False
SECRET_KEY=your-production-secret-key
PORT=auto-assigned
```

---

## 🧪 Testing

### Test Account Credentials
```
Email: test@example.com
Password: Test@123456
```

Or create a new account via the register page.

### Sample Test Data
Use the CSV in `dataset/` folder for batch testing.

---

## 📚 Documentation

- **[RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)** - 5-min deploy guide
- **[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)** - Complete deployment docs
- **[CHECKLIST_BEFORE_DEPLOY.md](CHECKLIST_BEFORE_DEPLOY.md)** - Pre-deploy checklist
- **[DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)** - Deployment overview

---

## ❓ FAQ

**Q: Can I use this for production?**
A: Yes! Follow the deployment guides. Use PostgreSQL for better scalability.

**Q: How many users can it handle?**
A: Free tier handles ~100 concurrent users. Upgrade for more.

**Q: Is my data safe?**
A: Yes. Passwords are hashed, sessions are secure. But don't enter real sensitive data in testing.

**Q: Can I customize the ML model?**
A: Yes! Check `backend/ml/train_model.py` to retrain with your data.

**Q: How do I backup my data?**
A: Download the SQLite database (`bnpl.db`) from the server.

**Q: Can I add more features?**
A: Absolutely! The code is modular and well-documented.

---

## 🤝 Contributing

Want to improve this project?

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

Proprietary - BNPL EMI Risk Assessment System
For internal use only.

---

## 👨‍💻 Developer Info

**Version:** 1.0.0
**Last Updated:** March 12, 2026
**Python Version:** 3.11+
**Status:** Production Ready

---

## 🆘 Support

### Troubleshooting
1. Check [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) troubleshooting section
2. Review application logs
3. Test locally before deploying

### Getting Help
- Read Flask docs: https://flask.palletsprojects.com
- Check Render docs: https://render.com/docs
- Review code comments in `backend/app.py`

---

## 🎉 Next Steps

1. **Deploy** your app using [RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)
2. **Test** all features thoroughly
3. **Monitor** performance with Render dashboard
4. **Gather** user feedback
5. **Improve** model with real data

---

**Ready to deploy? Start with [RENDER_QUICKSTART.md](RENDER_QUICKSTART.md)! 🚀**

---

## 📞 Contact

For questions about this project, please check the documentation files included.

**Happy Risk Assessment! 🏦📊**
