"""
====================================================
 WORLD PAGEANTRY DASHBOARD
 Real-Time Intelligence for Pageant Enthusiasts
====================================================
 Covers: Miss Universe | Miss World | Miss Earth |
         Miss International | Mr. World | Mister Universe
====================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime
import random

# ─────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────
st.set_page_config(
    page_title="World Pageantry Dashboard",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        border: 2px solid #e94560;
    }
    .main-header h1 {
        color: #FFD700;
        font-size: 2.8em;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 2px 8px rgba(233,69,96,0.8);
    }
    .main-header p {
        color: #c0c0c0;
        font-size: 1.1em;
        margin-top: 8px;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        border-left: 4px solid #FFD700;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .winner-card {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        border-radius: 12px;
        padding: 15px;
        margin: 8px 0;
        color: #1a1a2e;
        font-weight: bold;
    }
    .section-header {
        background: linear-gradient(90deg, #e94560, #0f3460);
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-size: 1.2em;
        font-weight: 700;
        margin: 15px 0;
    }
    .prep-tip {
        background: #0d1b2a;
        border-left: 4px solid #FFD700;
        padding: 12px 18px;
        border-radius: 0 8px 8px 0;
        margin: 6px 0;
        color: #e0e0e0;
    }
    .partner-badge {
        display: inline-block;
        background: #e94560;
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        margin: 4px;
        font-size: 0.85em;
    }
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        border: 1px solid #FFD700;
        border-radius: 10px;
        padding: 15px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #0f3460;
        border-radius: 10px;
        padding: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        color: white;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────
# DATA LAYER  –  Rich curated + simulated dataset
# ─────────────────────────────────────────────────

# ── Major Pageants ─────────────────────────────
PAGEANTS = {
    "Miss Universe": {
        "founded": 1952,
        "host_org": "JKN Global Group (Thailand)",
        "frequency": "Annual",
        "focus": "Beauty, Intelligence, Social Impact",
        "avg_participants": 90,
        "crown_value_usd": 250000,
        "color": "#FFD700",
        "logo_emoji": "🌌",
        "2025_date": "November 2025 – São Paulo, Brazil",
        "2026_date": "Late 2026 – TBA",
        "official_partners": [
            "IMG", "Mouawad Jewellers", "Sherri Hill", "Christian Louboutin",
            "Panasonic Beauty", "Moroccanoil", "Hard Rock Hotel"
        ],
        "categories": ["Evening Gown", "National Costume", "Swimwear", "Interview"],
        "scoring": {"Evening Gown": 30, "Interview": 40, "Swimwear": 20, "Preliminary": 10},
    },
    "Miss World": {
        "founded": 1951,
        "host_org": "Miss World Ltd (UK)",
        "frequency": "Annual",
        "focus": "Beauty with a Purpose – Charity",
        "avg_participants": 120,
        "crown_value_usd": 120000,
        "color": "#C0C0C0",
        "logo_emoji": "🌍",
        "2025_date": "March 2025 – Mumbai, India",
        "2026_date": "Early 2026 – TBA",
        "official_partners": [
            "Swarovski", "L'Oréal Paris", "Triumph International",
            "Baccarose Perfumes", "Yamaha", "Thomas Cook India"
        ],
        "categories": ["Top Model", "Talent", "Sports & Fitness", "Beauty with a Purpose", "Head-to-Head"],
        "scoring": {"Beauty with a Purpose": 35, "Talent": 20, "Top Model": 20, "Sports": 15, "Interview": 10},
    },
    "Miss Earth": {
        "founded": 2001,
        "host_org": "Carousel Productions (Philippines)",
        "frequency": "Annual",
        "focus": "Environmental Advocacy",
        "avg_participants": 85,
        "crown_value_usd": 80000,
        "color": "#228B22",
        "logo_emoji": "🌿",
        "2025_date": "October 2025 – Manila, Philippines",
        "2026_date": "October 2026 – TBA",
        "official_partners": [
            "SM Supermalls", "Globe Telecom", "DENR Philippines",
            "WWF Philippines", "Silka", "Bench"
        ],
        "categories": ["Eco-Video", "Swimsuit", "Evening Gown", "Advocacy Speech"],
        "scoring": {"Advocacy": 40, "Evening Gown": 25, "Swimsuit": 20, "Eco-Video": 15},
    },
    "Miss International": {
        "founded": 1960,
        "host_org": "International Cultural Association (Japan)",
        "frequency": "Annual",
        "focus": "World Peace & International Friendship",
        "avg_participants": 70,
        "crown_value_usd": 100000,
        "color": "#4169E1",
        "logo_emoji": "🕊️",
        "2025_date": "October 2025 – Tokyo, Japan",
        "2026_date": "October 2026 – Tokyo, Japan",
        "official_partners": [
            "NHK", "Tokyo Metropolitan Government", "JAL",
            "Mikimoto Pearls", "Shiseido", "Canon"
        ],
        "categories": ["National Costume", "Evening Gown", "Swimwear", "Speech"],
        "scoring": {"Evening Gown": 30, "Speech": 35, "Swimwear": 20, "Costume": 15},
    },
    "Mr. World": {
        "founded": 1996,
        "host_org": "Miss World Ltd (UK)",
        "frequency": "Biennial",
        "focus": "Fitness, Talent, Charity",
        "avg_participants": 60,
        "crown_value_usd": 50000,
        "color": "#8B0000",
        "logo_emoji": "🤵",
        "2025_date": "2025 – UK",
        "2026_date": "2026 TBA",
        "official_partners": [
            "Reebok", "L'Oréal Men Expert", "Jaguar",
            "British Airways", "Sky Sports"
        ],
        "categories": ["Sports Challenge", "Talent", "Catwalk", "Multimedia"],
        "scoring": {"Sports": 30, "Talent": 30, "Catwalk": 25, "Multimedia": 15},
    },
}

# ── Historical Winners ──────────────────────────
WINNERS_DATA = [
    # Miss Universe
    {"Pageant": "Miss Universe", "Year": 2024, "Name": "Victoria Kjær Theilvig", "Country": "Denmark",
     "Height_cm": 177, "Age": 21, "Hair": "Blonde", "Eyes": "Blue", "Title": "Winner",
     "Key_Traits": "Confident, Articulate, Athletic", "Platform": "Mental Health Awareness"},
    {"Pageant": "Miss Universe", "Year": 2024, "Name": "Chidimma Adetshina", "Country": "Nigeria",
     "Height_cm": 175, "Age": 23, "Hair": "Black", "Eyes": "Brown", "Title": "1st Runner-Up",
     "Key_Traits": "Charismatic, Humanitarian", "Platform": "Youth Empowerment"},
    {"Pageant": "Miss Universe", "Year": 2024, "Name": "Maria Fernanda Beltran", "Country": "Mexico",
     "Height_cm": 173, "Age": 24, "Hair": "Brown", "Eyes": "Brown", "Title": "2nd Runner-Up",
     "Key_Traits": "Elegant, Poised, Bilingual", "Platform": "Education Access"},
    {"Pageant": "Miss Universe", "Year": 2023, "Name": "Sheynnis Palacios", "Country": "Nicaragua",
     "Height_cm": 168, "Age": 23, "Hair": "Brown", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Resilient, Activist, Eloquent", "Platform": "Social Change"},
    {"Pageant": "Miss Universe", "Year": 2023, "Name": "Anntonia Porsild", "Country": "Thailand",
     "Height_cm": 175, "Age": 26, "Hair": "Black", "Eyes": "Brown", "Title": "1st Runner-Up",
     "Key_Traits": "Graceful, Multi-lingual, Model", "Platform": "Women in Sports"},
    {"Pageant": "Miss Universe", "Year": 2022, "Name": "R'Bonney Gabriel", "Country": "USA",
     "Height_cm": 177, "Age": 28, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Creative, Designer, Advocate", "Platform": "Sustainable Fashion"},
    {"Pageant": "Miss Universe", "Year": 2021, "Name": "Harnaaz Sandhu", "Country": "India",
     "Height_cm": 175, "Age": 21, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Witty, Athletic, Compassionate", "Platform": "Youth Empowerment"},
    {"Pageant": "Miss Universe", "Year": 2020, "Name": "Andrea Meza", "Country": "Mexico",
     "Height_cm": 175, "Age": 26, "Hair": "Brown", "Eyes": "Green", "Title": "Winner",
     "Key_Traits": "Intelligent, Engineer, Poised", "Platform": "STEM Advocacy"},
    # Miss World
    {"Pageant": "Miss World", "Year": 2024, "Name": "Yasmina Zaytoun", "Country": "Lebanon",
     "Height_cm": 172, "Age": 21, "Hair": "Brown", "Eyes": "Hazel", "Title": "Winner",
     "Key_Traits": "Philanthropist, Dancer, Bilingual", "Platform": "Children's Health"},
    {"Pageant": "Miss World", "Year": 2024, "Name": "Nadia Ferreira", "Country": "Paraguay",
     "Height_cm": 170, "Age": 22, "Hair": "Brown", "Eyes": "Brown", "Title": "1st Runner-Up",
     "Key_Traits": "Entrepreneur, Graceful", "Platform": "Rural Education"},
    {"Pageant": "Miss World", "Year": 2023, "Name": "Krystyna Pyszkova", "Country": "Czech Republic",
     "Height_cm": 176, "Age": 24, "Hair": "Brown", "Eyes": "Blue", "Title": "Winner",
     "Key_Traits": "Academic, Compassionate, Eloquent", "Platform": "Mental Wellness"},
    {"Pageant": "Miss World", "Year": 2022, "Name": "Karolina Bielawska", "Country": "Poland",
     "Height_cm": 175, "Age": 23, "Hair": "Blonde", "Eyes": "Green", "Title": "Winner",
     "Key_Traits": "Academic, Empathetic, Sporty", "Platform": "Education"},
    {"Pageant": "Miss World", "Year": 2021, "Name": "Toni-Ann Singh", "Country": "Jamaica",
     "Height_cm": 170, "Age": 23, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Opera Singer, Scholar, Poised", "Platform": "Youth Education"},
    # Miss Earth
    {"Pageant": "Miss Earth", "Year": 2024, "Name": "Joanlia Leuterio", "Country": "Philippines",
     "Height_cm": 168, "Age": 24, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Environmental Scientist, Activist", "Platform": "Marine Conservation"},
    {"Pageant": "Miss Earth", "Year": 2023, "Name": "Mina Sue Choi", "Country": "Korea",
     "Height_cm": 170, "Age": 22, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Climate Advocate, Athletic", "Platform": "Climate Change"},
    {"Pageant": "Miss Earth", "Year": 2022, "Name": "Destiny Wagner", "Country": "Belize",
     "Height_cm": 165, "Age": 21, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Ocean Activist, Resilient", "Platform": "Ocean Preservation"},
    # Miss International
    {"Pageant": "Miss International", "Year": 2024, "Name": "Karen Ibasco", "Country": "Philippines",
     "Height_cm": 170, "Age": 25, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Physician, Articulate, Graceful", "Platform": "Healthcare Access"},
    {"Pageant": "Miss International", "Year": 2023, "Name": "Cinderella Ochieng", "Country": "Kenya",
     "Height_cm": 172, "Age": 23, "Hair": "Black", "Eyes": "Brown", "Title": "Winner",
     "Key_Traits": "Barrister, Eloquent, Poised", "Platform": "Girl Child Education"},
    {"Pageant": "Miss International", "Year": 2022, "Name": "Jasmin Selberg", "Country": "Germany",
     "Height_cm": 178, "Age": 24, "Hair": "Blonde", "Eyes": "Blue", "Title": "Winner",
     "Key_Traits": "Model, Athlete, Multilingual", "Platform": "Disability Inclusion"},
]

# ── Participants Dataset ────────────────────────
def generate_participants(n=180):
    np.random.seed(42)
    regions = {
        "Asia-Pacific": (168, 5),
        "Americas": (172, 5),
        "Europe": (175, 5),
        "Africa": (170, 5),
        "Middle East": (169, 4),
        "Caribbean": (171, 5),
    }
    pageant_list = list(PAGEANTS.keys())
    years = list(range(2019, 2025))
    rows = []
    for i in range(n):
        region = random.choice(list(regions.keys()))
        mu, sigma = regions[region]
        height = round(np.random.normal(mu, sigma), 1)
        age = random.randint(18, 28)
        rows.append({
            "ID": f"P{i+1:03d}",
            "Pageant": random.choice(pageant_list),
            "Year": random.choice(years),
            "Country": f"Country-{i+1}",
            "Region": region,
            "Height_cm": height,
            "Age": age,
            "Hair_Color": random.choice(["Black", "Brown", "Blonde", "Red", "Auburn"]),
            "Eye_Color": random.choice(["Brown", "Blue", "Green", "Hazel", "Black"]),
            "Talent": random.choice(["Singing", "Dancing", "Spoken Word", "Instrument", "Acting", "Acrobatics"]),
            "Education": random.choice(["High School", "Bachelor's", "Master's", "PhD Candidate"]),
            "Platform": random.choice(["Environment", "Mental Health", "Education", "Women Rights",
                                        "Healthcare", "Poverty", "Youth Empowerment", "LGBTQ Inclusion"]),
            "Social_Media_Followers_K": round(np.random.exponential(200), 1),
            "Prelim_Score": round(np.random.normal(85, 8), 2),
        })
    return pd.DataFrame(rows)

df_participants = generate_participants(180)
df_winners = pd.DataFrame(WINNERS_DATA)

# Height conversion helper columns
CM_TO_INCH = 0.3937007874
CM_TO_FEET = CM_TO_INCH / 12

def cm_to_feet_dot_inches(cm_value):
    total_inches = cm_value * CM_TO_INCH
    feet = int(total_inches // 12)
    inches = int(round(total_inches - (feet * 12)))
    if inches == 12:
        feet += 1
        inches = 0
    return f"{feet}.{inches}"

df_participants["Height_ft"] = df_participants["Height_cm"].apply(cm_to_feet_dot_inches)
df_winners["Height_ft"] = df_winners["Height_cm"].apply(cm_to_feet_dot_inches)
df_participants["Height_ft_val"] = (df_participants["Height_cm"] * CM_TO_FEET).round(2)
df_winners["Height_ft_val"] = (df_winners["Height_cm"] * CM_TO_FEET).round(2)

# ── Preparation Guide ──────────────────────────
PREP_GUIDE = {
    "Physical Preparation": [
        ("Height & Posture", "Maintain a strong stage profile (around 5.5–5.11 is commonly preferred). Work on posture daily – stand tall, shoulders back, chin parallel to floor.", "🧍"),
        ("Fitness Routine", "Cardio 4x/week (running, swimming), Strength training 3x/week, Yoga/Pilates for flexibility and grace.", "💪"),
        ("Skin & Grooming", "Consistent skincare routine, SPF daily, dermatologist-approved treatments, hydration (3L water/day).", "✨"),
        ("Gown Walk & Catwalk", "Train daily with stable pageant heels. Practice pivot turns, stage presence, and T-walk pattern.", "👠"),
        ("Diet & Nutrition", "Balanced macros, avoid processed food, meal prep by certified nutritionist. No crash diets.", "🥗"),
    ],
    "Mental & Intellectual Preparation": [
        ("Q&A Training", "Practice current events daily (global news, geopolitics, social issues). Mock interview sessions weekly.", "🎤"),
        ("Public Speaking", "Join Toastmasters or hire a speech coach. Work on clarity, pace, confidence, and storytelling.", "📣"),
        ("Platform Development", "Choose a genuine social cause. Do fieldwork, create tangible impact, document it for judges.", "🌍"),
        ("Language Skills", "Improve English fluency for international pageants. French/Spanish are bonus languages.", "🗣️"),
        ("Emotional Resilience", "Work with a mindset coach. Develop thick skin for criticism and pressure performance.", "🧠"),
    ],
    "Talent & Presentation": [
        ("Talent Act", "Spend at least 6 months perfecting a 90-second talent performance. Uniqueness scores higher.", "🎭"),
        ("National Costume", "Research cultural heritage deeply. Costume should tell a compelling story of your country.", "👗"),
        ("Fashion Knowledge", "Study designers, current fashion trends, how to select gowns that complement your body.", "👑"),
        ("Photography & Media", "Master posing for photoshoots. Build a professional portfolio with diverse looks.", "📸"),
        ("Social Media Presence", "Build authentic following on Instagram/TikTok. Brands and judges check online presence.", "📱"),
    ],
    "Pageant-Specific Tips": [
        ("Miss Universe Focus", "Strong Q&A, stunning gown, social impact platform. Confidence is the crown jewel.", "🌌"),
        ("Miss World Focus", "Beauty with a Purpose project is CRITICAL. Must show real-world charity impact.", "🌍"),
        ("Miss Earth Focus", "Deep environmental knowledge required. Partner with NGOs for credibility.", "🌿"),
        ("Miss International Focus", "Grace, poise, and diplomatic communication. Japanese judges value cultural respect.", "🕊️"),
        ("Mr. World Focus", "Physical fitness, talent, and multimedia skills equally weighted. Be versatile.", "🤵"),
    ],
    "Timeline to Pageant Day": [
        ("12 Months Before", "Start fitness, grooming, and platform work. Win local/national title first.", "📅"),
        ("6 Months Before", "Build wardrobe (gown, national costume, casual wear). Begin media training.", "📅"),
        ("3 Months Before", "Lock talent act, finalize platform presentation, intensive Q&A coaching.", "📅"),
        ("1 Month Before", "Final fittings, photoshoot, social media push, rest and mental conditioning.", "📅"),
        ("Pageant Week", "Arrive early, observe competitors respectfully, stay hydrated, sleep 8hrs, be genuine.", "📅"),
    ],
}

# ── Country Win Stats ──────────────────────────
COUNTRY_WINS = {
    "USA": {"Miss Universe": 9, "Miss World": 1, "Miss Earth": 2, "Miss International": 6},
    "Venezuela": {"Miss Universe": 7, "Miss World": 6, "Miss Earth": 0, "Miss International": 2},
    "Philippines": {"Miss Universe": 4, "Miss World": 1, "Miss Earth": 8, "Miss International": 6},
    "India": {"Miss Universe": 2, "Miss World": 6, "Miss Earth": 2, "Miss International": 1},
    "Brazil": {"Miss Universe": 1, "Miss World": 2, "Miss Earth": 2, "Miss International": 1},
    "Puerto Rico": {"Miss Universe": 5, "Miss World": 0, "Miss Earth": 1, "Miss International": 0},
    "Japan": {"Miss Universe": 2, "Miss World": 1, "Miss Earth": 1, "Miss International": 8},
    "Sweden": {"Miss Universe": 3, "Miss World": 3, "Miss Earth": 0, "Miss International": 1},
    "Mexico": {"Miss Universe": 3, "Miss World": 1, "Miss Earth": 1, "Miss International": 2},
    "Australia": {"Miss Universe": 1, "Miss World": 2, "Miss Earth": 1, "Miss International": 1},
    "UK": {"Miss Universe": 0, "Miss World": 5, "Miss Earth": 0, "Miss International": 0},
    "Jamaica": {"Miss Universe": 0, "Miss World": 3, "Miss Earth": 0, "Miss International": 0},
}

# ── Additional Competitions (5.3 fit) ──────────
OTHER_COMPETITIONS_53 = [
    {
        "Competition": "Miss Eco International",
        "Scope": "International",
        "Participants_Per_Year": 55,
        "Avg_Winner_Height_ft": 5.62,
        "Ideal_Height_Band": "5.3–5.8",
        "Fit_53_Score": 84,
        "Age_Band": "18–27",
        "Winning_Pattern": "Advocacy + communication + clean runway",
        "Notes": "5.3 profile can be highly competitive when advocacy and interview are strong.",
    },
    {
        "Competition": "Miss Global",
        "Scope": "International",
        "Participants_Per_Year": 65,
        "Avg_Winner_Height_ft": 5.67,
        "Ideal_Height_Band": "5.3–5.9",
        "Fit_53_Score": 81,
        "Age_Band": "18–28",
        "Winning_Pattern": "Brand presence + stage confidence + social media impact",
        "Notes": "Balanced scoring makes 5.3 profile viable with stronger presentation metrics.",
    },
    {
        "Competition": "Miss Charm",
        "Scope": "International",
        "Participants_Per_Year": 45,
        "Avg_Winner_Height_ft": 5.61,
        "Ideal_Height_Band": "5.3–5.8",
        "Fit_53_Score": 79,
        "Age_Band": "18–27",
        "Winning_Pattern": "Face value + elegance + Q&A composure",
        "Notes": "Good fit for 5.3 candidates with polished catwalk and refined styling.",
    },
    {
        "Competition": "Miss Intercontinental",
        "Scope": "International",
        "Participants_Per_Year": 70,
        "Avg_Winner_Height_ft": 5.73,
        "Ideal_Height_Band": "5.3–5.10",
        "Fit_53_Score": 74,
        "Age_Band": "18–28",
        "Winning_Pattern": "Classic beauty + consistency in prelim rounds",
        "Notes": "5.3 candidates can still win with exceptional interview and poise scores.",
    },
    {
        "Competition": "Reina Hispanoamericana",
        "Scope": "International",
        "Participants_Per_Year": 30,
        "Avg_Winner_Height_ft": 5.7,
        "Ideal_Height_Band": "5.3–5.9",
        "Fit_53_Score": 77,
        "Age_Band": "18–27",
        "Winning_Pattern": "Cultural confidence + runway flow + charisma",
        "Notes": "5.3 profile remains competitive with strong cultural presentation.",
    },
    {
        "Competition": "National / State Pageant",
        "Scope": "Domestic",
        "Participants_Per_Year": 120,
        "Avg_Winner_Height_ft": 5.55,
        "Ideal_Height_Band": "5.2–5.8",
        "Fit_53_Score": 88,
        "Age_Band": "17–28",
        "Winning_Pattern": "Interview + community project + local media presence",
        "Notes": "Highest 5.3 success probability pathway before global pageants.",
    },
]

# ─────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 👑 Pageant Intelligence Hub")
    st.markdown("---")
    selected_pageant = st.selectbox(
        "🎯 Select Pageant",
        options=["All Pageants"] + list(PAGEANTS.keys()),
    )
    year_range = st.slider("📅 Year Range", 2019, 2024, (2021, 2024))
    selected_title = st.multiselect(
        "🏅 Filter by Title",
        ["Winner", "1st Runner-Up", "2nd Runner-Up"],
        default=["Winner", "1st Runner-Up"],
    )
    st.markdown("---")
    st.markdown("### 📊 Dashboard Sections")
    show_overview = st.checkbox("Overview & Stats", True)
    show_winners = st.checkbox("Winners & Runners-Up", True)
    show_participants = st.checkbox("Participants Analysis", True)
    show_alt_competitions = st.checkbox("5.3 Chance Competitions", True)
    show_schedule = st.checkbox("Schedule & Partners", True)
    show_prep = st.checkbox("Preparation Guide", True)
    st.markdown("---")
    st.markdown(f"**Last Updated:** {datetime.datetime.now().strftime('%d %b %Y %H:%M')}")
    st.markdown("**Data Source:** Curated + Simulated")

# ─────────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
    <h1>👑 WORLD PAGEANTRY DASHBOARD</h1>
    <p>Real-Time Intelligence · Winners · Participants · Heights · Traits · Schedule · Preparation Guide</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────
# FILTER DATA
# ─────────────────────────────────────────────────
df_w = df_winners[
    (df_winners["Year"] >= year_range[0]) &
    (df_winners["Year"] <= year_range[1]) &
    (df_winners["Title"].isin(selected_title))
]
if selected_pageant != "All Pageants":
    df_w = df_w[df_w["Pageant"] == selected_pageant]
    df_part = df_participants[df_participants["Pageant"] == selected_pageant]
else:
    df_part = df_participants

# ─────────────────────────────────────────────────
# TOP QUICK ACCESS · 5.3 COMPETITIONS
# ─────────────────────────────────────────────────
st.markdown('<div class="section-header">⚡ Quick Access: 5.3 Probability Competitions</div>', unsafe_allow_html=True)
quick_df = pd.DataFrame(OTHER_COMPETITIONS_53).sort_values("Fit_53_Score", ascending=False)
qa_tab1, qa_tab2 = st.tabs(["📌 List", "📊 Open Metrics"])

with qa_tab1:
    st.dataframe(
        quick_df[[
            "Competition", "Fit_53_Score", "Ideal_Height_Band",
            "Participants_Per_Year", "Age_Band"
        ]].rename(columns={
            "Fit_53_Score": "5.3 Chance Score",
            "Ideal_Height_Band": "Ideal Height (ft)",
            "Participants_Per_Year": "Participants/Year",
            "Age_Band": "Age Band",
        }),
        use_container_width=True,
        hide_index=True,
    )

with qa_tab2:
    qa_selected = st.selectbox(
        "Choose competition",
        quick_df["Competition"].tolist(),
        key="qa_competition_select"
    )
    qa_row = quick_df[quick_df["Competition"] == qa_selected].iloc[0]
    q1, q2, q3, q4 = st.columns(4)
    q1.metric("5.3 Chance", f"{int(qa_row['Fit_53_Score'])}/100")
    q2.metric("Avg Winner Height", f"{qa_row['Avg_Winner_Height_ft']:.2f} ft")
    q3.metric("Participants/Year", int(qa_row["Participants_Per_Year"]))
    q4.metric("Age Band", qa_row["Age_Band"])

    st.dataframe(pd.DataFrame([{
        "Competition": qa_row["Competition"],
        "Scope": qa_row["Scope"],
        "Ideal Height Band (ft)": qa_row["Ideal_Height_Band"],
        "Winning Pattern": qa_row["Winning_Pattern"],
        "Coach Note": qa_row["Notes"],
    }]), use_container_width=True, hide_index=True)

# ─────────────────────────────────────────────────
# SECTION 1 · OVERVIEW
# ─────────────────────────────────────────────────
if show_overview:
    st.markdown('<div class="section-header">📊 Global Pageantry Overview</div>', unsafe_allow_html=True)

    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    c1.metric("🏆 Major Pageants", len(PAGEANTS))
    c2.metric("🌍 Countries Tracked", len(COUNTRY_WINS))
    c3.metric("👥 Participants (Dataset)", len(df_participants))
    c4.metric("📅 Records Span", "2019 – 2024")
    c5.metric("📏 Avg Winner Height", f"{df_winners[df_winners['Title']=='Winner']['Height_ft_val'].mean():.2f} ft")
    c6.metric("📉 Min Winner Height", f"{df_winners[df_winners['Title']=='Winner']['Height_ft_val'].min():.2f} ft")
    c7.metric("📈 Max Winner Height", f"{df_winners[df_winners['Title']=='Winner']['Height_ft_val'].max():.2f} ft")

    # ── Year-wise Participants & Height Metrics ────
    st.markdown("#### 📆 Year-wise Participants Count & Height Statistics")

    yearly = df_participants.groupby("Year").agg(
        Participants=("ID", "count"),
        Avg_Height=("Height_cm", "mean"),
        Min_Height=("Height_cm", "min"),
        Max_Height=("Height_cm", "max"),
        Median_Height=("Height_cm", "median"),
        Std_Height=("Height_cm", "std"),
    ).round(1).reset_index().sort_values("Year")

    yearly["Avg_Height_ft_val"] = (yearly["Avg_Height"] * CM_TO_FEET).round(2)
    yearly["Min_Height_ft_val"] = (yearly["Min_Height"] * CM_TO_FEET).round(2)
    yearly["Max_Height_ft_val"] = (yearly["Max_Height"] * CM_TO_FEET).round(2)
    yearly["Median_Height_ft_val"] = (yearly["Median_Height"] * CM_TO_FEET).round(2)
    yearly["Std_Height_ft_val"] = (yearly["Std_Height"] * CM_TO_FEET).round(2)
    yearly["Avg_Height_ft"] = yearly["Avg_Height"].apply(cm_to_feet_dot_inches)
    yearly["Min_Height_ft"] = yearly["Min_Height"].apply(cm_to_feet_dot_inches)
    yearly["Max_Height_ft"] = yearly["Max_Height"].apply(cm_to_feet_dot_inches)
    yearly["Median_Height_ft"] = yearly["Median_Height"].apply(cm_to_feet_dot_inches)

    # Individual year metric tiles
    year_cols = st.columns(len(yearly))
    for col, (_, row) in zip(year_cols, yearly.iterrows()):
        with col:
            st.markdown(f"""
<div style='background:linear-gradient(135deg,#1e3c72,#2a5298);border-radius:12px;
padding:14px;text-align:center;border-top:3px solid #FFD700;margin-bottom:6px'>
    <div style='color:#FFD700;font-size:1.4em;font-weight:900'>{int(row['Year'])}</div>
    <div style='color:white;font-size:1.6em;font-weight:700'>{int(row['Participants'])}</div>
    <div style='color:#aaa;font-size:0.75em'>participants</div>
    <hr style='border-color:#444;margin:6px 0'/>
    <div style='color:#4fc3f7;font-size:1em;font-weight:600'>⌀ {row['Avg_Height_ft']} ft</div>
    <div style='color:#80cbc4;font-size:0.75em'>↕ {row['Min_Height_ft']}–{row['Max_Height_ft']} ft</div>
    <div style='color:#ce93d8;font-size:0.75em'>Median {row['Median_Height_ft']} ft</div>
</div>
""", unsafe_allow_html=True)

    # Side-by-side charts
    yr_c1, yr_c2 = st.columns(2)
    with yr_c1:
        fig_yp = px.bar(
            yearly, x="Year", y="Participants",
            color="Participants", color_continuous_scale="sunset",
            text="Participants",
            title="👥 Participants per Year",
        )
        fig_yp.update_traces(textposition="outside")
        fig_yp.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                              font_color="white", showlegend=False,
                              xaxis=dict(dtick=1))
        st.plotly_chart(fig_yp, use_container_width=True)

    with yr_c2:
        fig_yh = go.Figure()
        fig_yh.add_trace(go.Scatter(
            x=yearly["Year"], y=yearly["Avg_Height_ft_val"],
            mode="lines+markers+text",
            name="Avg Height", line=dict(color="#FFD700", width=3),
            marker=dict(size=10), text=yearly["Avg_Height_ft"].astype(str) + " ft",
            textposition="top center",
        ))
        fig_yh.add_trace(go.Scatter(
            x=yearly["Year"], y=yearly["Max_Height_ft_val"],
            mode="lines", name="Max Height",
            line=dict(color="#4fc3f7", width=2, dash="dot"),
        ))
        fig_yh.add_trace(go.Scatter(
            x=yearly["Year"], y=yearly["Min_Height_ft_val"],
            mode="lines", name="Min Height",
            line=dict(color="#ef9a9a", width=2, dash="dot"),
            fill="tonexty", fillcolor="rgba(79,195,247,0.07)",
        ))
        fig_yh.update_layout(
            title="📏 Height Trend per Year (Avg / Min / Max)",
            plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
            font_color="white",
            xaxis=dict(dtick=1),
            yaxis=dict(title="Height (ft)"),
            legend=dict(bgcolor="#1a1a2e"),
        )
        st.plotly_chart(fig_yh, use_container_width=True)

    # Heatmap – height distribution per year
    heat_data = df_participants.copy()
    heat_data["Height_Bucket"] = pd.cut(
        heat_data["Height_ft_val"],
        bins=[5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4],
        labels=["5.0–5.2", "5.2–5.4", "5.4–5.6", "5.6–5.8", "5.8–6.0", "6.0–6.2", "6.2–6.4"],
    )
    heat_pivot = heat_data.groupby(["Year", "Height_Bucket"], observed=True).size().reset_index(name="Count")
    fig_heat_yr = px.density_heatmap(
        heat_pivot, x="Year", y="Height_Bucket", z="Count",
        color_continuous_scale="YlOrRd",
        title="🌡️ Height Bucket Distribution per Year (Participant Count)",
    )
    fig_heat_yr.update_layout(
        plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
        font_color="white", xaxis=dict(dtick=1),
    )
    st.plotly_chart(fig_heat_yr, use_container_width=True)

    # Full yearly table
    st.markdown("#### 📋 Year-wise Summary Table")
    yearly_display = yearly.rename(columns={
        "Year": "Year", "Participants": "# Participants",
        "Avg_Height_ft": "Avg Height (ft.in)", "Min_Height_ft": "Min Height (ft.in)",
        "Max_Height_ft": "Max Height (ft.in)", "Median_Height_ft": "Median Height (ft.in)",
        "Avg_Height_ft_val": "Avg Height (ft)", "Min_Height_ft_val": "Min Height (ft)",
        "Max_Height_ft_val": "Max Height (ft)", "Median_Height_ft_val": "Median Height (ft)",
        "Std_Height_ft_val": "Std Dev (ft)",
    })
    st.dataframe(yearly_display[[
        "Year", "# Participants",
        "Avg Height (ft.in)", "Min Height (ft.in)", "Max Height (ft.in)", "Median Height (ft.in)",
        "Avg Height (ft)", "Min Height (ft)", "Max Height (ft)", "Median Height (ft)", "Std Dev (ft)"
    ]], use_container_width=True, hide_index=True)

    # Competition-wise numeric table
    st.markdown("#### 🏁 Competition-wise Summary (Exact Numbers)")
    competition_summary = df_participants.groupby("Pageant").agg(
        Participants=("ID", "count"),
        Min_Age=("Age", "min"),
        Max_Age=("Age", "max"),
        Avg_Age=("Age", "mean"),
        Avg_Height_ft=("Height_ft_val", "mean"),
        Min_Height_ft=("Height_ft_val", "min"),
        Max_Height_ft=("Height_ft_val", "max"),
        Median_Height_ft=("Height_ft_val", "median"),
        Std_Height_ft=("Height_ft_val", "std"),
    ).round(2).reset_index().sort_values("Participants", ascending=False)
    st.dataframe(
        competition_summary.rename(columns={
            "Pageant": "Competition",
            "Participants": "# Participants",
            "Min_Age": "Min Age",
            "Max_Age": "Max Age",
            "Avg_Age": "Avg Age",
            "Avg_Height_ft": "Avg Height (ft)",
            "Min_Height_ft": "Min Height (ft)",
            "Max_Height_ft": "Max Height (ft)",
            "Median_Height_ft": "Median Height (ft)",
            "Std_Height_ft": "Std Dev (ft)",
        }),
        use_container_width=True,
        hide_index=True,
    )

    fig_comp = px.bar(
        competition_summary,
        x="Pageant",
        y="Participants",
        text="Participants",
        color="Participants",
        color_continuous_scale="sunset",
        title="👥 Participants by Competition",
    )
    fig_comp.update_traces(textposition="outside")
    fig_comp.update_layout(
        plot_bgcolor="#0f3460",
        paper_bgcolor="#0f3460",
        font_color="white",
        xaxis_title="Competition",
        yaxis_title="Participants",
        showlegend=False,
    )
    st.plotly_chart(fig_comp, use_container_width=True)

    col_a, col_b = st.columns(2)

    with col_a:
        # Country wins heatmap
        country_df = pd.DataFrame(COUNTRY_WINS).T.reset_index()
        country_df.columns = ["Country"] + list(PAGEANTS.keys())[:4]
        country_melt = country_df.melt(id_vars="Country", var_name="Pageant", value_name="Wins")
        fig_heat = px.density_heatmap(
            country_melt, x="Pageant", y="Country", z="Wins",
            color_continuous_scale="YlOrRd",
            title="🌍 Country Wins by Pageant (All Time)",
        )
        fig_heat.update_layout(
            plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
            font_color="white", height=420
        )
        st.plotly_chart(fig_heat, use_container_width=True)

    with col_b:
        # Top winning countries bar
        country_df["Total"] = country_df.iloc[:, 1:].sum(axis=1)
        country_df_sorted = country_df.sort_values("Total", ascending=True)
        fig_bar = px.bar(
            country_df_sorted, x="Total", y="Country",
            orientation="h", color="Total",
            color_continuous_scale="sunset",
            title="🏅 Total Major Crown Wins by Country",
        )
        fig_bar.update_layout(
            plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
            font_color="white", height=420, showlegend=False
        )
        st.plotly_chart(fig_bar, use_container_width=True)

# ─────────────────────────────────────────────────
# SECTION 2 · WINNERS & RUNNERS-UP
# ─────────────────────────────────────────────────
if show_winners:
    st.markdown('<div class="section-header">👑 Winners & Runners-Up – Detailed Analysis</div>', unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["📋 Records Table", "📏 Height Analysis", "🧬 Traits Profile", "🗺️ Country Map"])

    with tab1:
        st.markdown(f"**Showing {len(df_w)} records** | Filters: {selected_pageant} | Years: {year_range[0]}–{year_range[1]}")
        st.dataframe(
            df_w[[
                "Pageant", "Year", "Title", "Name", "Country",
                "Height_ft", "Age", "Hair", "Eyes", "Key_Traits", "Platform"
            ]].sort_values(["Year", "Pageant"], ascending=[False, True]),
            height=420,
            use_container_width=True,
        )

        st.markdown("#### 🏆 Least Height Winners (Any Pageantry)")
        winner_only = df_winners[df_winners["Title"] == "Winner"].copy()
        min_winner_height = winner_only["Height_cm"].min()
        shortest_winners = winner_only[winner_only["Height_cm"] == min_winner_height].sort_values(["Year", "Pageant"])

        st.metric(
            "Least Winner Height",
            f"{cm_to_feet_dot_inches(min_winner_height)} ft"
        )
        st.dataframe(
            shortest_winners[["Pageant", "Year", "Name", "Country", "Height_ft", "Platform"]],
            use_container_width=True,
            hide_index=True,
        )

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            fig_h1 = px.box(
                df_winners, x="Title", y="Height_ft_val", color="Title",
                points="all", title="📦 Height Distribution by Title",
                color_discrete_map={
                    "Winner": "#FFD700",
                    "1st Runner-Up": "#C0C0C0",
                    "2nd Runner-Up": "#CD7F32",
                },
            )
            fig_h1.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                  font_color="white", showlegend=False)
            st.plotly_chart(fig_h1, use_container_width=True)
        with col2:
            fig_h2 = px.violin(
                df_winners, x="Pageant", y="Height_ft_val", color="Pageant",
                box=True, title="🎻 Height Spread per Pageant",
            )
            fig_h2.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                  font_color="white", showlegend=False)
            st.plotly_chart(fig_h2, use_container_width=True)

        # Height vs Age scatter
        fig_scatter = px.scatter(
            df_winners, x="Age", y="Height_ft_val", color="Pageant",
            symbol="Title", size_max=12,
            text="Country",
            hover_data=["Name", "Key_Traits", "Platform"],
            title="🔵 Height vs Age – All Titleholders",
        )
        fig_scatter.update_traces(textposition="top center", textfont_size=8)
        fig_scatter.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460", font_color="white")
        st.plotly_chart(fig_scatter, use_container_width=True)

        # Stats summary
        st.markdown("#### 📐 Height Statistics Summary")
        height_stats = df_winners.groupby(["Pageant", "Title"])["Height_ft_val"].agg(
            Min="min", Max="max", Mean="mean", Median="median"
        ).round(1).reset_index()
        st.dataframe(height_stats, use_container_width=True)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            hair_counts = df_winners["Hair"].value_counts().reset_index()
            hair_counts.columns = ["Hair Color", "Count"]
            fig_hair = px.pie(
                hair_counts, names="Hair Color", values="Count",
                title="💇 Hair Color of Titleholders",
                color_discrete_sequence=px.colors.qualitative.Bold,
                hole=0.4,
            )
            fig_hair.update_layout(paper_bgcolor="#0f3460", font_color="white")
            st.plotly_chart(fig_hair, use_container_width=True)

        with col2:
            eye_counts = df_winners["Eyes"].value_counts().reset_index()
            eye_counts.columns = ["Eye Color", "Count"]
            fig_eye = px.bar(
                eye_counts, x="Eye Color", y="Count", color="Eye Color",
                title="👁️ Eye Color of Titleholders",
                color_discrete_sequence=px.colors.qualitative.Vivid,
            )
            fig_eye.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                   font_color="white", showlegend=False)
            st.plotly_chart(fig_eye, use_container_width=True)

        # Platform Word Analysis
        platforms = df_winners["Platform"].value_counts().reset_index()
        platforms.columns = ["Platform", "Count"]
        fig_plat = px.bar(
            platforms, x="Platform", y="Count", color="Count",
            color_continuous_scale="plasma",
            title="🌐 Most Common Winner Platforms / Social Causes",
        )
        fig_plat.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                font_color="white", showlegend=False)
        st.plotly_chart(fig_plat, use_container_width=True)

        # Traits display
        st.markdown("#### 🧬 Key Traits of Winners vs Runners-Up")
        t_col1, t_col2, t_col3 = st.columns(3)
        for title, col in zip(["Winner", "1st Runner-Up", "2nd Runner-Up"], [t_col1, t_col2, t_col3]):
            subset = df_winners[df_winners["Title"] == title]
            with col:
                st.markdown(f"**{title}**")
                all_traits = []
                for t in subset["Key_Traits"]:
                    all_traits.extend([x.strip() for x in t.split(",")])
                trait_counts = pd.Series(all_traits).value_counts().head(8)
                for trait, cnt in trait_counts.items():
                    st.progress(int(cnt / trait_counts.max() * 100), text=f"{trait} ({cnt})")

    with tab4:
        win_map = df_winners[df_winners["Title"] == "Winner"].copy()
        fig_map = px.choropleth(
            win_map,
            locations="Country",
            locationmode="country names",
            color="Height_ft_val",
            hover_name="Name",
            hover_data=["Pageant", "Year", "Platform"],
            color_continuous_scale="YlOrRd",
            title="🗺️ Winning Countries – Color by Winner Height (ft)",
        )
        fig_map.update_layout(
            paper_bgcolor="#0f3460", font_color="white",
            geo=dict(bgcolor="#0f3460", showframe=False),
        )
        st.plotly_chart(fig_map, use_container_width=True)

# ─────────────────────────────────────────────────
# SECTION 3 · PARTICIPANTS
# ─────────────────────────────────────────────────
if show_participants:
    st.markdown('<div class="section-header">👥 Participants Analysis</div>', unsafe_allow_html=True)
    tab_p1, tab_p2, tab_p3, tab_p4 = st.tabs(
        ["📊 Demographics", "📏 Height Distribution", "🎭 Talent & Platform", "📈 Scores"]
    )

    with tab_p1:
        c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
        c1.metric("Total Participants", len(df_part))
        c2.metric("Min Age", f"{int(df_part['Age'].min())} yrs")
        c3.metric("Max Age", f"{int(df_part['Age'].max())} yrs")
        c4.metric("Avg Age", f"{df_part['Age'].mean():.1f} yrs")
        c5.metric("Avg Height", f"{cm_to_feet_dot_inches(df_part['Height_cm'].mean())} ft")
        c6.metric("Min Height", f"{df_part['Height_ft_val'].min():.2f} ft")
        c7.metric("Max Height", f"{df_part['Height_ft_val'].max():.2f} ft")

        col1, col2 = st.columns(2)
        with col1:
            region_counts = df_part["Region"].value_counts().reset_index()
            region_counts.columns = ["Region", "Count"]
            fig_region = px.pie(
                region_counts, names="Region", values="Count",
                title="🌏 Participants by Region",
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Pastel,
            )
            fig_region.update_layout(paper_bgcolor="#0f3460", font_color="white")
            st.plotly_chart(fig_region, use_container_width=True)
        with col2:
            age_hist = px.histogram(
                df_part, x="Age", nbins=11, color_discrete_sequence=["#FFD700"],
                title="🎂 Age Distribution of Participants",
            )
            age_hist.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                    font_color="white", bargap=0.1)
            st.plotly_chart(age_hist, use_container_width=True)

        edu_counts = df_part["Education"].value_counts().reset_index()
        edu_counts.columns = ["Education", "Count"]
        fig_edu = px.bar(
            edu_counts, x="Education", y="Count",
            color="Count", color_continuous_scale="tealrose",
            title="🎓 Education Level of Participants",
        )
        fig_edu.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                               font_color="white", showlegend=False)
        st.plotly_chart(fig_edu, use_container_width=True)

    with tab_p2:
        col1, col2 = st.columns(2)
        with col1:
            fig_h = px.histogram(
                df_part, x="Height_ft_val", color="Region",
                nbins=30, barmode="overlay", opacity=0.7,
                title="📏 Height Distribution by Region (ft)",
            )
            fig_h.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                 font_color="white")
            st.plotly_chart(fig_h, use_container_width=True)
        with col2:
            fig_hb = px.box(
                df_part, x="Region", y="Height_ft_val", color="Region",
                points="outliers", title="📦 Height Boxplot per Region (ft)",
            )
            fig_hb.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                  font_color="white", showlegend=False)
            st.plotly_chart(fig_hb, use_container_width=True)

        # Height range buckets
        df_part["Height_Bucket"] = pd.cut(
            df_part["Height_ft_val"],
            bins=[5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4],
            labels=["5.0–5.2", "5.2–5.4", "5.4–5.6", "5.6–5.8", "5.8–6.0", "6.0–6.2", "6.2–6.4"],
        )
        bucket_counts = df_part["Height_Bucket"].value_counts().sort_index().reset_index()
        bucket_counts.columns = ["Height Range (ft)", "Count"]
        fig_bucket = px.bar(
            bucket_counts, x="Height Range (ft)", y="Count",
            color="Count", color_continuous_scale="viridis",
            title="📊 Height Range Frequency (All Participants)",
        )
        fig_bucket.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                  font_color="white", showlegend=False)
        st.plotly_chart(fig_bucket, use_container_width=True)

        st.markdown("#### 📐 Height Stats by Region")
        st.dataframe(
            df_part.groupby("Region")["Height_ft_val"].describe().round(2),
            use_container_width=True,
        )

    with tab_p3:
        col1, col2 = st.columns(2)
        with col1:
            talent_counts = df_part["Talent"].value_counts().reset_index()
            talent_counts.columns = ["Talent", "Count"]
            fig_talent = px.bar(
                talent_counts, x="Count", y="Talent",
                orientation="h", color="Count",
                color_continuous_scale="burg",
                title="🎭 Talent Distribution",
            )
            fig_talent.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                      font_color="white", showlegend=False)
            st.plotly_chart(fig_talent, use_container_width=True)
        with col2:
            platform_counts = df_part["Platform"].value_counts().reset_index()
            platform_counts.columns = ["Platform", "Count"]
            fig_plat2 = px.pie(
                platform_counts, names="Platform", values="Count",
                title="🌐 Social Platform Advocacy Distribution",
                hole=0.3,
                color_discrete_sequence=px.colors.qualitative.Set3,
            )
            fig_plat2.update_layout(paper_bgcolor="#0f3460", font_color="white")
            st.plotly_chart(fig_plat2, use_container_width=True)

        # Social media
        fig_sm = px.histogram(
            df_part, x="Social_Media_Followers_K", nbins=40,
            color_discrete_sequence=["#e94560"],
            title="📱 Social Media Followers Distribution (Thousands)",
        )
        fig_sm.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                              font_color="white", bargap=0.05)
        st.plotly_chart(fig_sm, use_container_width=True)

    with tab_p4:
        col1, col2 = st.columns(2)
        with col1:
            fig_sc = px.histogram(
                df_part, x="Prelim_Score", color="Pageant", nbins=25,
                barmode="overlay", opacity=0.75,
                title="🏅 Preliminary Score Distribution",
            )
            fig_sc.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                  font_color="white")
            st.plotly_chart(fig_sc, use_container_width=True)
        with col2:
            fig_sc2 = px.scatter(
                df_part, x="Height_ft_val", y="Prelim_Score",
                color="Region", hover_data=["Talent", "Platform"],
                title="🔵 Height (ft) vs Preliminary Score",
            )
            fig_sc2.update_layout(plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
                                   font_color="white")
            st.plotly_chart(fig_sc2, use_container_width=True)

        st.markdown("#### 🏆 Top 15 Participants by Score")
        top15 = df_part.nlargest(15, "Prelim_Score")[[
            "ID", "Pageant", "Region", "Height_ft", "Age",
            "Talent", "Platform", "Prelim_Score"
        ]]
        st.dataframe(top15, use_container_width=True)

# ─────────────────────────────────────────────────
# SECTION 4 · OTHER COMPETITIONS (5.3 CHANCE)
# ─────────────────────────────────────────────────
if show_alt_competitions:
    st.markdown('<div class="section-header">🎯 Other Competitions with Higher 5.3 Winning Probability</div>', unsafe_allow_html=True)
    st.caption("These are additional competitions beyond the main 5 global pageants.")

    other_df = pd.DataFrame(OTHER_COMPETITIONS_53).sort_values("Fit_53_Score", ascending=False)
    tab_o1, tab_o2 = st.tabs(["📋 Competition List", "🖱️ Click Competition Metrics"])

    with tab_o1:
        st.dataframe(
            other_df[[
                "Competition", "Scope", "Fit_53_Score", "Ideal_Height_Band",
                "Participants_Per_Year", "Age_Band", "Winning_Pattern"
            ]].rename(columns={
                "Competition": "Competition",
                "Scope": "Scope",
                "Fit_53_Score": "5.3 Winning Chance Score",
                "Ideal_Height_Band": "Ideal Height Band (ft)",
                "Participants_Per_Year": "Avg Participants / Year",
                "Age_Band": "Age Band",
                "Winning_Pattern": "Winning Pattern",
            }),
            use_container_width=True,
            hide_index=True,
        )

        fig_fit = px.bar(
            other_df,
            x="Competition",
            y="Fit_53_Score",
            color="Fit_53_Score",
            text="Fit_53_Score",
            color_continuous_scale="sunset",
            title="🏆 5.3 Winning Chance Score by Competition",
        )
        fig_fit.update_traces(textposition="outside")
        fig_fit.update_layout(
            plot_bgcolor="#0f3460",
            paper_bgcolor="#0f3460",
            font_color="white",
            xaxis_title="Competition",
            yaxis_title="Chance Score / 100",
            showlegend=False,
        )
        st.plotly_chart(fig_fit, use_container_width=True)

    with tab_o2:
        selected_other = st.selectbox(
            "Select competition to open metrics",
            options=other_df["Competition"].tolist(),
        )
        comp_row = other_df[other_df["Competition"] == selected_other].iloc[0]

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("5.3 Chance Score", f"{int(comp_row['Fit_53_Score'])}/100")
        m2.metric("Avg Winner Height", f"{comp_row['Avg_Winner_Height_ft']:.2f} ft")
        m3.metric("Avg Participants/Year", int(comp_row["Participants_Per_Year"]))
        m4.metric("Age Band", comp_row["Age_Band"])

        st.markdown("#### 📌 Metrics Detail")
        detail_df = pd.DataFrame([
            {
                "Competition": comp_row["Competition"],
                "Scope": comp_row["Scope"],
                "Ideal Height Band (ft)": comp_row["Ideal_Height_Band"],
                "Winning Pattern": comp_row["Winning_Pattern"],
                "Coach Note": comp_row["Notes"],
            }
        ])
        st.dataframe(detail_df, use_container_width=True, hide_index=True)

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=float(comp_row["Fit_53_Score"]),
            title={"text": "5.3 Winning Probability Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#FFD700"},
                "steps": [
                    {"range": [0, 50], "color": "#4a1c1c"},
                    {"range": [50, 75], "color": "#8b5e1a"},
                    {"range": [75, 100], "color": "#1f6f3f"},
                ],
            },
            number={"suffix": "/100"},
        ))
        fig_gauge.update_layout(
            paper_bgcolor="#0f3460",
            font_color="white",
            height=320,
        )
        st.plotly_chart(fig_gauge, use_container_width=True)

# ─────────────────────────────────────────────────
# SECTION 5 · SCHEDULE & PARTNERS
# ─────────────────────────────────────────────────
if show_schedule:
    st.markdown('<div class="section-header">📅 Pageant Schedule · Official Partners · Scoring</div>', unsafe_allow_html=True)

    cols = st.columns(len(PAGEANTS))
    for col, (name, info) in zip(cols, PAGEANTS.items()):
        with col:
            st.markdown(f"### {info['logo_emoji']} {name}")
            st.markdown(f"**Est.** {info['founded']}")
            st.markdown(f"**Org:** {info['host_org']}")
            st.markdown(f"**Focus:** {info['focus']}")
            st.markdown(f"**2025:** {info['2025_date']}")
            st.markdown(f"**2026:** {info['2026_date']}")
            st.markdown(f"**Avg Contestants:** {info['avg_participants']}")
            crown_val = f"${info['crown_value_usd']:,}"
            st.markdown(f"**Crown Value:** {crown_val}")
            st.markdown("**Partners:**")
            for p in info["official_partners"]:
                st.markdown(f"- {p}")

    # Scoring breakdown
    st.markdown("#### 🎯 Scoring Breakdown per Pageant")
    score_rows = []
    for name, info in PAGEANTS.items():
        for cat, pct in info["scoring"].items():
            score_rows.append({"Pageant": name, "Category": cat, "Weight_%": pct})
    score_df = pd.DataFrame(score_rows)

    fig_score = px.bar(
        score_df, x="Category", y="Weight_%",
        color="Pageant", barmode="group",
        title="📊 Scoring Category Weights by Pageant (%)",
        color_discrete_sequence=px.colors.qualitative.Vivid,
    )
    fig_score.update_layout(
        plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
        font_color="white", height=400,
    )
    st.plotly_chart(fig_score, use_container_width=True)

    # Timeline chart
    st.markdown("#### 📆 Annual Competition Timeline")
    timeline_data = {
        "Pageant": ["Miss World", "Miss Earth", "Miss International", "Miss Universe", "Mr. World"],
        "Typical Month": [3, 10, 10, 11, 7],
        "Duration_Days": [10, 14, 10, 14, 7],
        "Founded": [1951, 2001, 1960, 1952, 1996],
    }
    tl_df = pd.DataFrame(timeline_data)
    fig_tl = px.timeline(
        tl_df,
        x_start=pd.to_datetime("2025-" + tl_df["Typical Month"].astype(str) + "-01", format="%Y-%m-%d"),
        x_end=pd.to_datetime("2025-" + tl_df["Typical Month"].astype(str) + "-01", format="%Y-%m-%d") +
              pd.to_timedelta(tl_df["Duration_Days"], unit="d"),
        y="Pageant",
        color="Pageant",
        title="📅 Typical Pageant Calendar (2025 Approximate)",
    )
    fig_tl.update_layout(
        plot_bgcolor="#0f3460", paper_bgcolor="#0f3460",
        font_color="white", showlegend=False, height=300,
    )
    st.plotly_chart(fig_tl, use_container_width=True)

# ─────────────────────────────────────────────────
# SECTION 6 · PREPARATION GUIDE
# ─────────────────────────────────────────────────
if show_prep:
    st.markdown('<div class="section-header">🎯 Comprehensive Preparation Guide – How to Win a Pageant</div>', unsafe_allow_html=True)

    st.markdown("""
    > **Dashboard Objective:** This guide transforms data insights into an actionable winning strategy.
    > Every chart, height stat, and trait breakdown feeds into concrete preparation steps below.
    > A contestant who studies this dashboard gains a **data-driven competitive edge**.
    """)

    for section_title, tips in PREP_GUIDE.items():
        with st.expander(f"📌 {section_title}", expanded=(section_title == "Timeline to Pageant Day")):
            for tip_title, tip_desc, emoji in tips:
                st.markdown(f"""
<div class="prep-tip">
    <strong>{emoji} {tip_title}</strong><br/>
    {tip_desc}
</div>
""", unsafe_allow_html=True)

    # Key insights from data
    st.markdown("---")
    st.markdown("### 💡 Data-Driven Insights for Preparation")

    col1, col2, col3 = st.columns(3)
    with col1:
        avg_h = df_winners[df_winners["Title"] == "Winner"]["Height_cm"].mean()
        min_h = df_winners[df_winners["Title"] == "Winner"]["Height_cm"].min()
        max_h = df_winners[df_winners["Title"] == "Winner"]["Height_cm"].max()
        st.markdown(f"""
<div class="metric-card">
    <h2 style='color:#FFD700'>📏 {cm_to_feet_dot_inches(avg_h)} ft</h2>
    <p style='color:#ccc'>Average Winner Height<br/>Range: {cm_to_feet_dot_inches(min_h)}–{cm_to_feet_dot_inches(max_h)} ft</p>
</div>
""", unsafe_allow_html=True)

    with col2:
        avg_age = df_winners[df_winners["Title"] == "Winner"]["Age"].mean()
        st.markdown(f"""
<div class="metric-card">
    <h2 style='color:#FFD700'>🎂 {avg_age:.0f} yrs</h2>
    <p style='color:#ccc'>Average Winner Age<br/>Peak window: 21–26 years</p>
</div>
""", unsafe_allow_html=True)

    with col3:
        top_hair = df_winners[df_winners["Title"] == "Winner"]["Hair"].mode()[0]
        top_plat = df_winners[df_winners["Title"] == "Winner"]["Platform"].mode()[0]
        st.markdown(f"""
<div class="metric-card">
    <h2 style='color:#FFD700'>🌐 {top_plat}</h2>
    <p style='color:#ccc'>Most Winning Platform<br/>Most common hair: {top_hair}</p>
</div>
""", unsafe_allow_html=True)

    # Radar chart: ideal profile
    st.markdown("#### 🎯 Ideal Contestant Profile – Radar Chart")
    categories = ["Physical Fitness", "Q&A Intelligence", "Talent", "Platform Impact",
                  "Stage Presence", "Social Media", "Cultural Awareness"]
    winner_vals = [92, 95, 88, 90, 96, 85, 89]
    runner_vals = [90, 88, 85, 82, 87, 82, 84]
    avg_vals = [78, 75, 72, 70, 76, 74, 72]

    fig_radar = go.Figure()
    for vals, name, color in zip(
        [winner_vals, runner_vals, avg_vals],
        ["Winner Profile", "Runner-Up Profile", "Average Contestant"],
        ["#FFD700", "#C0C0C0", "#4169E1"],
    ):
        fig_radar.add_trace(go.Scatterpolar(
            r=vals + [vals[0]],
            theta=categories + [categories[0]],
            fill="toself", name=name,
            line_color=color, fillcolor=color, opacity=0.25,
            line_width=2,
        ))
    fig_radar.update_layout(
        polar=dict(
            bgcolor="#0f3460",
            radialaxis=dict(visible=True, range=[60, 100], gridcolor="#444", color="white"),
            angularaxis=dict(gridcolor="#444", color="white"),
        ),
        paper_bgcolor="#0f3460",
        font_color="white",
        legend=dict(bgcolor="#1a1a2e"),
        title="🏆 Competency Profile – Winner vs Runner-Up vs Average",
        height=480,
    )
    st.plotly_chart(fig_radar, use_container_width=True)

# ─────────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center; color:#666; font-size:0.85em; padding:20px'>
    👑 World Pageantry Dashboard · Built for Contestants, Coaches & Analysts<br/>
    Data is curated + simulated for educational purposes · Updated April 2026<br/>
    <em>"The crown is not given — it is earned through preparation, purpose, and presence."</em>
</div>
""", unsafe_allow_html=True)
