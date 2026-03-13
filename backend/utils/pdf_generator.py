import matplotlib
matplotlib.use("Agg")  # ESSENTIAL for Render/Cloud environments
import matplotlib.pyplot as plt

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

import io
import os
import requests
from datetime import datetime

# ======================================================
# FONT SETUP — UTF-8 SUPPORT FOR ₹ SYMBOL
# ======================================================
def setup_fonts():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    regular_font = os.path.join(base_dir, "DejaVuSans.ttf")
    bold_font = os.path.join(base_dir, "DejaVuSans-Bold.ttf")

    font_urls = {
        regular_font: "https://github.com/mhardcastle/DejaVu-Sans-TTF/raw/master/DejaVuSans.ttf",
        bold_font: "https://github.com/mhardcastle/DejaVu-Sans-TTF/raw/master/DejaVuSans-Bold.ttf"
    }

    for path, url in font_urls.items():
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    with open(path, "wb") as f:
                        f.write(response.content)
            except:
                pass

    try:
        if os.path.exists(regular_font):
            pdfmetrics.registerFont(TTFont("DejaVu", regular_font))
            pdfmetrics.registerFont(TTFont("DejaVu-Bold", bold_font))
            matplotlib.rcParams["font.family"] = "DejaVu Sans"
            return "DejaVu", "DejaVu-Bold"
    except:
        pass
    return "Helvetica", "Helvetica-Bold"

MAIN_FONT, BOLD_FONT = setup_fonts()

# ======================================================
# PDF REPORT GENERATOR
# ======================================================
def create_visual_report(data, prob, risk, report_path):
    # Ensure directory exists
    report_dir = os.path.dirname(report_path)
    if report_dir and not os.path.exists(report_dir):
        os.makedirs(report_dir, exist_ok=True)

    c = canvas.Canvas(report_path, pagesize=letter)
    width, height = letter
    curr = "₹" if MAIN_FONT == "DejaVu" else "Rs."

    # 1. BULLETPROOF DATA SANITIZATION
    # This prevents the "float conversion" errors from crashing the report
    def clean_num(key, default=0.0):
        val = data.get(key, default)
        if val is None or val == "": return default
        try:
            return float(str(val).replace(',', '').replace('₹', '').strip())
        except:
            return default

    income = clean_num('income', 1.0) # Avoid 0 for division
    emi = clean_num('emi', 0.0)
    loan = clean_num('loan', 0.0)
    tenure = int(clean_num('tenure', 0.0))
    on_time = int(clean_num('ontime', 0.0))
    delays = int(clean_num('delays', 0.0))
    credit = int(clean_num('credit', 0.0))

    # Calculate ratios for the visual charts
    emi_ratio = (emi / income) * 100 if income > 0 else 0
    repayment_consistency = (on_time / (on_time + delays + 1)) * 100

    # 2. HEADER
    c.setFillColorRGB(0.17, 0.24, 0.31)
    c.rect(0, 730, width, 70, fill=1)
    c.setFillColor(colors.white)
    c.setFont(BOLD_FONT, 20)
    c.drawCentredString(width / 2, 755, "BNPL Risk Assessment Report")

    # 3. EXECUTIVE SUMMARY
    c.setFillColor(colors.black)
    c.setFont(BOLD_FONT, 13)
    c.drawString(50, 710, "1. Executive Summary")
    c.line(50, 705, 562, 705)

    c.setFont(BOLD_FONT, 11)
    c.drawString(60, 685, f"Report Profile: {data.get('name', 'N/A')}")

    # Risk Color Logic
    v_color = colors.green
    risk_str = str(risk).upper()
    if "HIGH" in risk_str: v_color = colors.red
    elif "MEDIUM" in risk_str: v_color = colors.orange

    c.setFillColor(v_color)
    c.roundRect(350, 675, 180, 25, 10, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont(BOLD_FONT, 10)
    c.drawCentredString(440, 682, f"Final Risk Verdict: {risk_str}")

    c.setFillColor(colors.black)
    c.setFont(BOLD_FONT, 10)
    c.drawString(60, 660, "Financial Snapshot")
    c.setFont(MAIN_FONT, 9)
    y = 645
    snapshot = [
        f"• Monthly Income: {curr}{income:,.2f}", 
        f"• Requested Loan: {curr}{loan:,.2f}", 
        f"• Monthly EMI: {curr}{emi:,.2f}", 
        f"• Loan Tenure: {tenure} Months",
        f"• Credit Score: {credit}"
    ]
    for text in snapshot:
        c.drawString(70, y, text)
        y -= 13

    # 4. VISUAL ANALYSIS (CHARTS)
    c.setFont(BOLD_FONT, 13)
    c.drawString(50, 580, "2. Visual Data Analytics")
    c.line(50, 575, 562, 575)

    def draw_chart(fig, x, y, w, h):
        try:
            buf = io.BytesIO()
            fig.savefig(buf, format="png", dpi=100, bbox_inches='tight')
            buf.seek(0)
            c.drawImage(ImageReader(buf), x, y, w, h)
            plt.close(fig)
            buf.close()
        except Exception as e:
            print(f"Chart Error: {e}")

    # Chart 1: Risk Probability
    fig1, ax1 = plt.subplots(figsize=(4, 2))
    ax1.barh(["Risk Prob"], [prob], color='red' if prob > 0.5 else 'green')
    ax1.set_xlim(0, 1)
    ax1.set_title("ML Probability Score")
    draw_chart(fig1, 310, 440, 230, 120)

    # Chart 2: EMI to Income Ratio
    fig2, ax2 = plt.subplots(figsize=(4, 2))
    ax2.bar(["EMI Burden %"], [emi_ratio], color='skyblue')
    ax2.axhline(50, color='red', linestyle="--", label="Risk Limit")
    ax2.set_ylim(0, 100)
    ax2.set_title("Debt-to-Income Analysis")
    draw_chart(fig2, 60, 440, 230, 120)

    # 5. SYSTEM RECOMMENDATIONS
    c.setFont(BOLD_FONT, 13)
    c.drawString(50, 380, "3. System Recommendations")
    c.line(50, 375, 562, 375)
    
    c.setFont(MAIN_FONT, 10)
    s_y = 355
    if "HIGH" in risk_str:
        suggs = ["• High risk detected. Require manual income verification.",
                 "• Debt-to-income ratio exceeds safe parameters.",
                 "• Repayment history shows significant delays."]
    else:
        suggs = ["• Maintain a healthy Debt-to-Income ratio below 40%.",
                 "• Ensure on-time payments to improve future credit limits.",
                 "• Financial profile qualifies for standard processing."]
    
    for s in suggs:
        c.drawString(65, s_y, s)
        s_y -= 15

    # FOOTER
    c.setFillColorRGB(0.17, 0.24, 0.31)
    c.rect(0, 0, width, 30, fill=1)
    c.setFillColor(colors.white)
    c.setFont(MAIN_FONT, 8)
    c.drawCentredString(width/2, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | BNPL Risk Engine v2.0")

    c.showPage()
    c.save()