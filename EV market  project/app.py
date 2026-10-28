"""
=============================================================================
Electric Vehicle Market Performance & Insights
College Project Web Application
Framework: Python Flask
=============================================================================
This application serves an academic analytics presentation website for an
Electric Vehicle (EV) market study. It embeds published Tableau Public
visualizations (Dashboard and Story) and provides comprehensive project
documentation, objectives, dataset details, and architecture information.
=============================================================================
"""

import os
import re
from flask import Flask, render_template, request

app = Flask(__name__)

# =============================================================================
# 1. EDITABLE TABLEAU PUBLIC CONFIGURATION
# =============================================================================
# INSTRUCTIONS FOR COLLEGE STUDENTS:
# Replace the empty strings below with your published Tableau Public URLs.
#
# Examples:
#   TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
#   TABLEAU_STORY_URL     = "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
#
# If left as "" or placeholder, the website will display a helpful, elegant
# guide card explaining how to publish and copy your Tableau link.
# =============================================================================

TABLEAU_DASHBOARD_URL = "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
TABLEAU_STORY_URL = "https://public.tableau.com/views/Electricvehiclemarketperformanceandinsights/EVMarketDashboard?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"

# =============================================================================
# 2. PROJECT METADATA & ACADEMIC DOCUMENTATION
# (You can freely customize student name, college, year, or supervisor)
# =============================================================================
PROJECT_METADATA = {
    "title": "Electric Vehicle Market Performance & Insights",
    "subtitle": "Interactive Academic Visual Analytics & Market Trend Exploration",
    "project_category": "Data Analytics & Business Intelligence Project",
    "academic_year": "2025 - 2026",
    "degree_program": "B.Tech / B.E / B.Sc / MCA / M.Sc - Data Science / CSE / IT",
    "institution": "Department of Computer Science & Engineering / Data Analytics",
    "project_team": {
        "student_name": "Student / Project Team",
        "roll_number": "EV-DS-2026-001",
        "guide_name": "Project Supervisor / Faculty Mentor"
    },
    "kpis": [
        {
            "label": "Total EV Records Analyzed",
            "value": "150,000+",
            "subtext": "Registered vehicles in core dataset",
            "icon": "car"
        },
        {
            "label": "Dominant Technology",
            "value": "BEV (78%)",
            "subtext": "Battery Electric vs 22% PHEV",
            "icon": "battery"
        },
        {
            "label": "Peak Electric Range",
            "value": "337 Miles",
            "subtext": "Top single-charge consumer range",
            "icon": "gauge"
        },
        {
            "label": "Market Leader Share",
            "value": "Tesla (~52%)",
            "subtext": "Followed by Nissan, Chevy, Ford",
            "icon": "trophy"
        }
    ],
    "objectives": [
        {
            "title": "Adoption & Growth Trajectory",
            "desc": "Track the historical growth of electric vehicle registrations over the past decade to quantify the shift toward sustainable electric mobility."
        },
        {
            "title": "Battery Technology & Range Analysis",
            "desc": "Examine the technical gap between pure Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) across battery ranges and model years."
        },
        {
            "title": "Manufacturer Competitiveness & Market Share",
            "desc": "Identify leading automakers, quantify their market shares, and uncover how legacy automakers are competing against specialized EV innovators."
        },
        {
            "title": "Clean Fuel Incentive (CAFV) Eligibility",
            "desc": "Evaluate the distribution of vehicles eligible for Clean Alternative Fuel Vehicle benefits and the impact of range thresholds on consumer qualification."
        },
        {
            "title": "Geographic Concentration & Urban Clusters",
            "desc": "Map adoption density across counties and cities to pinpoint high-penetration EV hubs versus underserved regional markets."
        }
    ],
    "dataset": {
        "name": "Electric Vehicle Population Data",
        "source": "State Department of Licensing (DOL) / Public Open Data Registry",
        "description": "Comprehensive registry records of Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) currently registered, tracking technical specifications, clean fuel eligibility, and location.",
        "attributes": [
            {"name": "VIN (1-10)", "type": "Categorical (Identifier)", "desc": "First 10 characters of the unique Vehicle Identification Number."},
            {"name": "County & City", "type": "Geographic", "desc": "County and municipality where the electric vehicle is officially registered."},
            {"name": "Model Year", "type": "Numerical (Temporal)", "desc": "Year of manufacture, used to chart technological evolution from 2010 to present."},
            {"name": "Make & Model", "type": "Categorical", "desc": "Automaker brand (e.g., Tesla, Nissan, Chevrolet, Ford) and vehicle model name."},
            {"name": "Electric Vehicle Type", "type": "Categorical", "desc": "Category flag: Battery Electric Vehicle (BEV) or Plug-in Hybrid Electric Vehicle (PHEV)."},
            {"name": "CAFV Eligibility", "type": "Categorical", "desc": "Clean Alternative Fuel Vehicle eligibility status based on zero-emission battery range thresholds."},
            {"name": "Electric Range (mi)", "type": "Numerical (Continuous)", "desc": "Certified single-charge electric driving range in miles."},
            {"name": "Base MSRP ($)", "type": "Numerical (Currency)", "desc": "Manufacturer's Suggested Retail Price where available (0 indicates unlisted/standard model)."}
        ]
    },
    "technologies": [
        {
            "name": "Python 3",
            "category": "Backend & Preprocessing",
            "role": "Environment execution, data auditing, script execution, and serving the local application."
        },
        {
            "name": "Flask",
            "category": "Web Framework",
            "role": "Lightweight WSGI Python web framework delivering modular templates, routing, and dynamic Tableau configuration."
        },
        {
            "name": "Tableau Public",
            "category": "Business Intelligence",
            "role": "Data modeling, calculation fields, interactive dashboards with filters, parameters, and multi-slide narrative Stories."
        },
        {
            "name": "HTML5 & CSS3",
            "category": "Frontend Presentation",
            "role": "Modern, responsive blue-and-white theme featuring card layouts, status badges, and mobile-friendly grids."
        },
        {
            "name": "Vanilla JavaScript",
            "category": "Interactivity",
            "role": "Minimal client-side logic for section tab switching, mobile menu toggle, fullscreen mode, and URL copying."
        }
    ]
}


def clean_tableau_url(url: str) -> str:
    """
    Format and sanitize a Tableau Public URL for embedding in an <iframe>.
    
    Ensures that essential Tableau embed query parameters are included:
      - :showVizHome=no (prevents opening Tableau Public homepage chrome)
      - :embed=true     (forces iframe-friendly embed mode)
      - :toolbar=yes    (allows standard presentation toolbar)
    """
    if not url or not isinstance(url, str):
        return ""
    
    cleaned = url.strip()
    if not cleaned or "tableau.com" not in cleaned.lower():
        # Not a valid or set Tableau URL
        return ""

    # Remove trailing fragments or unwanted parameters if needed
    cleaned = cleaned.split("#")[0]

    # For Tableau Public embeds, strip transient sharing parameters
    # (such as :redirect=auth, :origin=viz_share_link, :sid=) which
    # can trigger unwanted authentication checks or blank screens in iframes
    base = cleaned.split("?")[0]
    return f"{base}?:showVizHome=no&:embed=true&:toolbar=yes"


@app.route("/")
@app.route("/<section>")
def home(section="overview"):
    """
    Single-page presentation router. Accepts an optional section
    parameter ('overview', 'dashboard', 'story', 'about') so students
    can directly link or bookmark specific project sections.
    """
    valid_sections = ["overview", "dashboard", "story", "about"]
    active_section = section.lower() if section.lower() in valid_sections else "overview"

    # Process Tableau embed links
    dashboard_embed = clean_tableau_url(TABLEAU_DASHBOARD_URL)
    story_embed = clean_tableau_url(TABLEAU_STORY_URL)

    return render_template(
        "index.html",
        project=PROJECT_METADATA,
        active_section=active_section,
        # Processed embed links for iframes
        dashboard_url=dashboard_embed,
        story_url=story_embed,
        # Raw links for display / verification
        raw_dashboard_url=TABLEAU_DASHBOARD_URL.strip(),
        raw_story_url=TABLEAU_STORY_URL.strip(),
        has_dashboard=bool(dashboard_embed),
        has_story=bool(story_embed)
    )


if __name__ == "__main__":
    # Host on 127.0.0.1 (localhost) on port 5000 with debug mode enabled
    print("\n" + "=" * 60)
    print(" ELECTRIC VEHICLE MARKET PERFORMANCE & INSIGHTS")
    print(" Flask Development Server Running")
    print("=" * 60)
    print(" Local Web URL : http://127.0.0.1:5000")
    print(" Dashboard URL : " + (TABLEAU_DASHBOARD_URL if TABLEAU_DASHBOARD_URL.strip() else "[Not configured in app.py - Instructions displayed in UI]"))
    print(" Story URL     : " + (TABLEAU_STORY_URL if TABLEAU_STORY_URL.strip() else "[Not configured in app.py - Instructions displayed in UI]"))
    print("=" * 60 + "\n")
    app.run(host="127.0.0.1", port=5000, debug=True)

