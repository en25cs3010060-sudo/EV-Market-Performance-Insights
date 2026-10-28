# ⚡ Electric Vehicle Market Performance & Insights

> **Academic Capstone & Data Analytics Project**  
> Built with **Python Flask**, **Tableau Public**, **HTML5**, **CSS3**, and **Vanilla JavaScript**.

---

## 📌 Project Overview

**"Electric Vehicle Market Performance & Insights"** is an academic visual analytics platform designed to study the growth trajectory, technological evolution, and geographic distribution of Electric Vehicles (EVs). 

The application integrates interactive **Tableau Public Dashboards and Stories** inside a modern, responsive **blue-and-white analytics web portal** powered by **Python Flask**.

---

## 🎯 Project Objectives

1. **Adoption & Growth Trajectory:** Chart historical EV registrations (2011–Present) to quantify adoption velocity and the shift from niche to mass-market acceptance.
2. **Powertrain Breakdown (BEV vs. PHEV):** Contrast pure Battery Electric Vehicles (BEVs) against Plug-in Hybrid Electric Vehicles (PHEVs) across market share and consumer preferences.
3. **Battery Range & Technology Evolution:** Analyze the distribution and progress of certified single-charge battery ranges across model years.
4. **Manufacturer Competitiveness:** Identify leading automakers (e.g., Tesla, Nissan, Chevrolet, Ford, BMW) and quantify their respective market shares.
5. **Geographic Distribution & CAFV Incentives:** Map registration density across counties and assess vehicle eligibility for Clean Alternative Fuel Vehicle (CAFV) benefits.

---

## 📊 Dataset Details

- **Dataset Name:** Electric Vehicle Population Data
- **Source:** State Department of Licensing (DOL) / Public Open Data Registry
- **Volume:** 150,000+ Cleaned Vehicle Registration Records
- **Key Attributes:**
  - `VIN (1-10)`: Unique Vehicle Identification Number prefix
  - `County & City`: Geographic registration location
  - `Model Year`: Year of vehicle manufacture (temporal analysis)
  - `Make & Model`: Vehicle manufacturer brand and model designation
  - `Electric Vehicle Type`: Battery Electric Vehicle (BEV) vs. Plug-in Hybrid Electric Vehicle (PHEV)
  - `Clean Alternative Fuel Vehicle (CAFV) Eligibility`: Clean fuel program rebate status
  - `Electric Range`: Certified single-charge driving range in miles
  - `Base MSRP`: Manufacturer Suggested Retail Price

> **Data Architecture Note:**  
> In accordance with academic best practices, this project presents data cleaned and modeled in Python and Tableau. It does not fabricate or claim unbuilt SQL/database connections.

---

## 🛠️ Technology Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | Python 3 | Runtime environment, data scripting, and local application server |
| **Framework** | Flask 3.x | Lightweight WSGI web framework, dynamic URL injection, template routing |
| **BI & Analytics** | Tableau Public | Multi-chart interactive dashboards, calculated fields, and guided 4-chapter story points |
| **Frontend UI** | HTML5 & CSS3 | Semantic markup, responsive blue-and-white theme, CSS Grid & Flexbox |
| **Scripting** | Vanilla JavaScript | Client-side tab navigation, fullscreen toggle, mobile menu, snippet copying |

---

## 📁 Project Structure

```text
EV market project/
│
├── app.py                 # Flask server & Tableau URL configuration
├── requirements.txt       # Python dependencies (Flask)
├── README.md              # Project documentation & Windows execution guide
│
├── templates/
│   └── index.html         # Responsive presentation template (Overview, Dashboard, Story, About)
│
└── static/
    ├── style.css          # Blue-and-white modern EV analytics stylesheet
    └── script.js          # Minimal JavaScript for section navigation & embed controls
```

---

## 🚀 Step-by-Step Setup & Running on Windows

Follow these steps to run the project on your Windows machine:

### 1. Open Windows PowerShell or Command Prompt
Open the project directory in PowerShell or Command Prompt:
```powershell
cd "c:\Users\adhis\EV market  project"
```

### 2. (Recommended) Create & Activate a Virtual Environment
Creating a virtual environment ensures dependencies remain isolated and clean:
```powershell
# Create the virtual environment
python -m venv venv

# Activate on Windows PowerShell:
.\venv\Scripts\Activate.ps1

# (OR if using Windows Command Prompt cmd.exe):
venv\Scripts\activate.bat
```

> **PowerShell Execution Policy Tip:**  
> If PowerShell displays a script execution error, run this command once in PowerShell:  
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

### 3. Install Required Dependencies
Install Flask using `pip`:
```powershell
python -m pip install -r requirements.txt
```

### 4. (Optional) Configure Your Tableau Public URLs in `app.py`
Open `app.py` in your preferred editor (VS Code, Notepad++, or Notepad).  
Find lines 27–28:

```python
# Paste your published Tableau Public URLs here:
TABLEAU_DASHBOARD_URL = ""
TABLEAU_STORY_URL = ""
```

- If you **have published links**, paste them inside the quotes:
  ```python
  TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
  TABLEAU_STORY_URL = "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
  ```
- If you **haven't published yet**, leave them empty `""`! The website includes a **graceful fallback mode** that displays setup instructions and visual mockup previews for your presentation.

### 5. Launch the Flask Application
Run the Flask server:
```powershell
python app.py
```

You will see terminal output similar to:
```text
============================================================
 ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS
 Flask Development Server Running
============================================================
 Local Web URL : http://127.0.0.1:5000
============================================================
```

### 6. View in Web Browser
Open your favorite web browser (Chrome, Edge, Firefox) and navigate to:
```text
http://127.0.0.1:5000
```

---

## 🌐 How to Get Your Tableau Public Embed Links

1. Open **Tableau Desktop** or **Tableau Public**.
2. Click **File &rarr; Save to Tableau Public As...** (or press `Ctrl + S`).
3. Sign in to your free [Tableau Public account](https://public.tableau.com/).
4. Once published in your browser:
   - Click the **Share** icon (located in the bottom-right toolbar of your visualization).
   - In the popup dialog, copy the **Link** (e.g., `https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link`).
5. Open `app.py`, paste into `TABLEAU_DASHBOARD_URL` or `TABLEAU_STORY_URL`, and save.
6. Refresh `http://127.0.0.1:5000` to see your live, interactive Tableau visual embedded directly!

---

## 🎨 Website Features & Sections

- **Overview:** Executive summary, 4 research pillars (Growth, Powertrains, Automakers, Geography), project workflow stages, and live KPI summary cards.
- **Dashboard:** Interactive container for your Tableau Public Dashboard with full-width responsive layout, **Fullscreen mode**, **Reload** button, and **Open in Tableau** shortcut.
- **Story:** Narrative-driven Tableau Story container designed for step-by-step presentation of market insights.
- **About:** Comprehensive documentation of project objectives, dataset schema dictionary, preprocessing methodology, technology stack, and student/mentor credits.
- **Graceful Fallback UI:** If URLs are missing or left as default, the application displays step-by-step instructions and preview mockup cards so the page remains complete and polished during demonstrations.

---

## 🔧 Windows Troubleshooting

| Issue | Solution |
| :--- | :--- |
| `'python' is not recognized as an internal or external command` | Add Python to your Windows system PATH during installation, or use `py app.py`. |
| `Script execution disabled on this system` in PowerShell | Run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in your PowerShell window. |
| `Address already in use` (Port 5000 occupied) | Edit `app.py` line 208 and change `port=5000` to `port=5050` or another free port. |
| Tableau visualization shows blank or white box | Verify your workbook is published publicly on Tableau Public and not set to private/hidden. |

---

## 🎓 College Viva / Presentation Talking Points

- **Why Flask?** Flask provides a lightweight, modular Python backend that easily links analytical data configurations to modern web templates without heavy overhead.
- **Why Tableau Public?** Tableau enables multi-dimensional slicing, cross-filtering, and storytelling for business intelligence users without requiring manual SQL queries.
- **Key Insight to Highlight:** Battery Electric Vehicles (BEVs) have outpaced Plug-in Hybrids (PHEVs), with average electric ranges exceeding 250–300 miles in recent model years, driven by battery density advancements and charging infrastructure expansion.

