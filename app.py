import os
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="QU Bobcat Recruitment Intelligence",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(61,141,222,0.22), transparent 32%),
        radial-gradient(circle at top right, rgba(255,184,28,0.18), transparent 28%),
        linear-gradient(135deg, #020617 0%, #08111f 45%, #0D223F 100%);
    color: white;
}

.block-container {
    padding-top: 1.4rem;
    padding-bottom: 3rem;
}

.hero {
    padding: 32px;
    border-radius: 30px;
    background: linear-gradient(135deg, rgba(0,47,108,0.98), rgba(13,34,63,0.92), rgba(255,184,28,0.16));
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 24px 70px rgba(0,0,0,0.45);
}

.hero-title {
    font-size: 48px;
    font-weight: 950;
    color: white;
    margin-bottom: 8px;
}

.hero-subtitle {
    color: #dbeafe;
    font-size: 18px;
}

.intel-banner {
    margin-top: 18px;
    padding: 18px 22px;
    border-radius: 22px;
    background: linear-gradient(90deg, rgba(0,47,108,0.92), rgba(61,141,222,0.35), rgba(255,184,28,0.18));
    border: 1px solid rgba(255,255,255,0.14);
    box-shadow: 0 0 30px rgba(61,141,222,0.16);
}

.glass {
    padding: 24px;
    border-radius: 24px;
    background: rgba(255,255,255,0.075);
    border: 1px solid rgba(255,255,255,0.16);
    box-shadow: 0 12px 34px rgba(0,0,0,0.26);
}

.gold {
    padding: 24px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(255,184,28,0.22), rgba(255,255,255,0.06));
    border: 1px solid rgba(255,184,28,0.36);
    box-shadow: 0 12px 34px rgba(0,0,0,0.28);
}

.ai {
    padding: 25px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(61,141,222,0.28), rgba(13,34,63,0.88));
    border: 1px solid rgba(61,141,222,0.36);
    box-shadow: 0 12px 34px rgba(0,0,0,0.32);
}

.plotly-graph-div {
    border-radius: 22px;
    overflow: hidden;
    box-shadow: 0 0 28px rgba(61,141,222,0.18);
    border: 1px solid rgba(255,255,255,0.08);
}

[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 0 18px rgba(0,0,0,0.25);
}

[data-testid="stMetricValue"] {
    font-size: 26px;
    color: white;
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 16px;
    padding: 12px 18px;
    background: rgba(255,255,255,0.08);
    color: white;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #002F6C, #3D8DDE);
    color: white;
}

.badge {
    display: inline-block;
    padding: 8px 13px;
    margin: 5px 5px 5px 0;
    border-radius: 999px;
    background: rgba(255,184,28,0.18);
    border: 1px solid rgba(255,184,28,0.38);
    color: white;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA PATHS
# =========================================================
DATA_PATH = os.path.expanduser("~/Desktop/student_visa_consulate_master.csv")
LOGO_PATH = os.path.expanduser("~/Desktop/qu_bobcat_logo.png")

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# =========================================================
# POST TO COUNTRY MAP
# =========================================================
post_country_map = {
    "Hyderabad": "India", "Mumbai": "India", "New Delhi": "India", "Chennai": "India", "Kolkata": "India",
    "Beijing": "China", "Shanghai": "China", "Guangzhou": "China", "Shenyang": "China", "Wuhan": "China",
    "Hong Kong": "Hong Kong", "AIT Taipei": "Taiwan",
    "Seoul": "South Korea",
    "Tokyo": "Japan", "Osaka": "Japan", "Osaka/Kobe": "Japan", "Naha": "Japan",

    "Ho Chi Minh City": "Vietnam", "Hanoi": "Vietnam",
    "Bangkok": "Thailand", "Chiang Mai": "Thailand",
    "Manila": "Philippines", "Jakarta": "Indonesia", "Singapore": "Singapore",
    "Kuala Lumpur": "Malaysia", "Bandar Seri Begawan": "Brunei",
    "Dili": "Timor-Leste",

    "Kathmandu": "Nepal", "Dhaka": "Bangladesh", "Colombo": "Sri Lanka",
    "Islamabad": "Pakistan", "Karachi": "Pakistan",

    "Dubai": "United Arab Emirates", "Abu Dhabi": "United Arab Emirates",
    "Doha": "Qatar", "Kuwait City": "Kuwait",
    "Riyadh": "Saudi Arabia", "Jeddah": "Saudi Arabia", "Dhahran": "Saudi Arabia",
    "Amman": "Jordan", "Jerusalem": "Israel", "Tel Aviv": "Israel",
    "Beirut": "Lebanon", "Baghdad": "Iraq", "Erbil": "Iraq",
    "Almaty": "Kazakhstan", "Astana": "Kazakhstan",
    "Tashkent": "Uzbekistan", "Baku": "Azerbaijan", "Yerevan": "Armenia",
    "Tbilisi": "Georgia", "Ulaanbaatar": "Mongolia",

    "London": "United Kingdom", "Belfast": "United Kingdom",
    "Paris": "France", "Madrid": "Spain",
    "Frankfurt": "Germany", "Berlin": "Germany", "Munich": "Germany",
    "Dublin": "Ireland", "Rome": "Italy", "Milan": "Italy", "Naples": "Italy", "Florence": "Italy",
    "Amsterdam": "Netherlands", "Brussels": "Belgium", "Bern": "Switzerland",
    "Vienna": "Austria", "Warsaw": "Poland", "Krakow": "Poland",
    "Bucharest": "Romania", "Sofia": "Bulgaria", "Athens": "Greece",
    "Lisbon": "Portugal", "Prague": "Czech Republic", "Bratislava": "Slovakia",
    "Budapest": "Hungary", "Belgrade": "Serbia", "Zagreb": "Croatia",
    "Ljubljana": "Slovenia", "Copenhagen": "Denmark", "Stockholm": "Sweden",
    "Oslo": "Norway", "Helsinki": "Finland",
    "Ankara": "Turkey", "Istanbul": "Turkey",

    "Abidjan": "Cote d'Ivoire", "Abuja": "Nigeria", "Lagos": "Nigeria",
    "Accra": "Ghana", "Addis Ababa": "Ethiopia",
    "Nairobi": "Kenya", "Harare": "Zimbabwe",
    "Cape Town": "South Africa", "Johannesburg": "South Africa", "Durban": "South Africa",
    "Dakar": "Senegal", "Kampala": "Uganda", "Dar es Salaam": "Tanzania",
    "Lusaka": "Zambia", "Maputo": "Mozambique",
    "Cairo": "Egypt", "Casablanca": "Morocco", "Algiers": "Algeria",
    "Bamako": "Mali", "Conakry": "Guinea", "Freetown": "Sierra Leone",
    "Banjul": "Gambia", "Gaborone": "Botswana",

    "Mexico City": "Mexico", "Guadalajara": "Mexico", "Monterrey": "Mexico",
    "Ciudad Juarez": "Mexico", "Hermosillo": "Mexico",
    "Bogota": "Colombia", "Lima": "Peru",
    "Quito": "Ecuador", "Guayaquil": "Ecuador",
    "Sao Paulo": "Brazil", "Brasilia": "Brazil", "Rio de Janeiro": "Brazil", "Porto Alegre": "Brazil",
    "Buenos Aires": "Argentina", "Santiago": "Chile",
    "Kingston": "Jamaica", "Santo Domingo": "Dominican Republic",
    "Guatemala City": "Guatemala", "Georgetown": "Guyana",
    "Asuncion": "Paraguay",

    "Toronto": "Canada", "Montreal": "Canada", "Vancouver": "Canada", "Calgary": "Canada", "Halifax": "Canada",
    "Sydney": "Australia", "Melbourne": "Australia",
    "Auckland": "New Zealand",
    "Apia": "Samoa", "Majuro": "Marshall Islands", "Kolonia": "Micronesia", "Koror": "Palau"
}

df["country_mapped"] = df["post"].map(post_country_map)

if "country" in df.columns:
    df["country"] = df["country_mapped"].fillna(df["country"])
else:
    df["country"] = df["country_mapped"]

df = df.drop(columns=["country_mapped"])

# Main focus = F1. Secondary side layer = J1.
f1 = df[(df["visa_class"] == "F1") & (df["country"].notna())].copy()
j1 = df[(df["visa_class"] == "J1") & (df["country"].notna())].copy()

# =========================================================
# MAP CENTERS
# =========================================================
country_centers = {
    "India": (22.97, 78.65), "China": (35.86, 104.19), "Vietnam": (14.05, 108.27),
    "Nepal": (28.39, 84.12), "Bangladesh": (23.68, 90.35), "Pakistan": (30.37, 69.34),
    "Zimbabwe": (-19.01, 29.15), "Nigeria": (9.08, 8.67), "Ghana": (7.94, -1.02),
    "Kenya": (-0.02, 37.90), "South Africa": (-30.55, 22.93),
    "South Korea": (35.90, 127.76), "Japan": (36.20, 138.25), "Taiwan": (23.69, 120.96),
    "Brazil": (-14.23, -51.92), "Colombia": (4.57, -74.29), "Mexico": (23.63, -102.55),
    "United Kingdom": (55.37, -3.43), "France": (46.22, 2.21), "Germany": (51.16, 10.45),
    "Italy": (41.87, 12.56), "Spain": (40.46, -3.74),
    "Philippines": (12.87, 121.77), "Indonesia": (-0.78, 113.92),
    "Saudi Arabia": (23.88, 45.07), "United Arab Emirates": (23.42, 53.84),
    "Turkey": (38.96, 35.24), "Canada": (56.13, -106.34), "Australia": (-25.27, 133.77)
}

# =========================================================
# HELPER FUNCTIONS
# =========================================================
def month_name(m):
    names = {
        1: "January", 2: "February", 3: "March", 4: "April",
        5: "May", 6: "June", 7: "July", 8: "August",
        9: "September", 10: "October", 11: "November", 12: "December"
    }
    return names.get(int(m), str(m))

def safe_growth(country_df):
    temp = country_df[country_df["month"] <= 9]
    yearly = temp.groupby("year")["issuances"].sum()

    if 2023 in yearly.index and 2025 in yearly.index and yearly.loc[2023] > 0:
        return ((yearly.loc[2025] - yearly.loc[2023]) / yearly.loc[2023]) * 100

    return None

def seasonality_cv(country_df):
    monthly = country_df.groupby("month")["issuances"].sum()
    if monthly.mean() == 0:
        return None
    return monthly.std() / monthly.mean()

def tier_from_volume(total):
    if total >= 100000:
        return "Tier 1: Core Priority Market"
    elif total >= 25000:
        return "Tier 2: High-Potential Market"
    elif total >= 8000:
        return "Tier 3: Strategic Niche Market"
    else:
        return "Tier 4: Monitor Market"

def recommendation(country, total, growth, cv, peak_month, top_post, j1_total):
    tier = tier_from_volume(total)

    if growth is None:
        growth_line = "Comparable Jan–Sep growth is not available."
    elif growth >= 10:
        growth_line = f"The market shows positive comparable Jan–Sep growth of {growth:.1f}%."
    elif growth <= -10:
        growth_line = f"The market shows a comparable Jan–Sep decline of {abs(growth):.1f}%, so the trend should be interpreted cautiously."
    else:
        growth_line = f"The market appears relatively stable, with comparable Jan–Sep movement of {growth:.1f}%."

    if cv is None:
        season_line = "Seasonality could not be calculated."
    elif cv >= 1:
        season_line = "This is a highly seasonal F1 market, so outreach should begin earlier before peak visa months."
    elif cv >= 0.65:
        season_line = "This market has moderate F1 seasonality and benefits from planned campaign timing."
    else:
        season_line = "This market is relatively stable across the year."

    return f"""
    **{country}** is classified as **{tier}** for F1 recruitment.

    {growth_line} {season_line}

    The strongest observed F1 post is **{top_post}**, and the peak F1 visa month is **{month_name(peak_month)}**.

    **J1 side signal:** This market recorded **{j1_total:,} J1 issuances** in the mapped dataset. J1 activity can support exchange, scholar, visiting student, and global engagement conversations, but F1 remains the main enrollment recruitment signal.

    **Recommended QU action:** align international outreach, applicant follow-up, and I-20 support before the peak F1 visa cycle.

    **Important note:** visa issuance volume shows student mobility activity, not individual approval probability.
    """

def live_ai_context(country, total, growth, cv):
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key:
        return None

    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"""
        Provide a concise current geopolitical and international student mobility context for {country}
        in relation to U.S. F1 and J1 visa issuances and university recruitment.

        Do not claim visa issuance equals approval chance.
        Use 4 short bullets.

        Dataset context:
        Total F1 issuances: {total}
        Comparable Jan-Sep F1 growth: {growth}
        F1 Seasonality CV: {cv}
        """

        response = client.responses.create(
            model="gpt-4.1-mini",
            tools=[{"type": "web_search"}],
            input=prompt
        )

        return response.output_text

    except Exception as e:
        return f"Live AI unavailable: {e}"

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    if os.path.exists(LOGO_PATH):
        st.image(LOGO_PATH, width=260)
    else:
        st.markdown("## 🐾 QU Bobcats")

    st.markdown("### 🎛️ Control Center")

    countries = sorted(f1["country"].dropna().unique())

    selected_country = st.selectbox(
        "Select country",
        countries,
        index=countries.index("India") if "India" in countries else 0
    )

    compare_defaults = [x for x in ["India", "China", "Vietnam", "Nepal", "Zimbabwe"] if x in countries]

    compare_countries = st.multiselect(
        "Compare countries",
        countries,
        default=compare_defaults
    )

    st.markdown("---")
    st.caption("Built for QU International Admissions.")

# =========================================================
# COUNTRY DATA
# =========================================================
country_data = f1[f1["country"] == selected_country].copy()
j1_country_data = j1[j1["country"] == selected_country].copy()

country_total = int(country_data["issuances"].sum())
active_posts = int(country_data["post"].nunique())

j1_total = int(j1_country_data["issuances"].sum())
j1_posts = int(j1_country_data["post"].nunique())

top_posts = (
    country_data.groupby("post")["issuances"]
    .sum()
    .reset_index()
    .sort_values("issuances", ascending=False)
)

top_post = top_posts.iloc[0]["post"] if len(top_posts) > 0 else "N/A"

j1_top_posts = (
    j1_country_data.groupby("post")["issuances"]
    .sum()
    .reset_index()
    .sort_values("issuances", ascending=False)
)

j1_top_post = j1_top_posts.iloc[0]["post"] if len(j1_top_posts) > 0 else "N/A"

month_totals = (
    country_data.groupby("month")["issuances"]
    .sum()
    .reset_index()
    .sort_values("issuances", ascending=False)
)

peak_month = int(month_totals.iloc[0]["month"]) if len(month_totals) > 0 else 0

j1_month_totals = (
    j1_country_data.groupby("month")["issuances"]
    .sum()
    .reset_index()
    .sort_values("issuances", ascending=False)
)

j1_peak_month = int(j1_month_totals.iloc[0]["month"]) if len(j1_month_totals) > 0 else 0

growth = safe_growth(country_data)
cv = seasonality_cv(country_data)
tier = tier_from_volume(country_total)

# =========================================================
# HERO
# =========================================================
st.markdown("""
<div class="hero">
    <div class="hero-title">🐾 QU Bobcat Global Recruitment Intelligence</div>
    <div class="hero-subtitle">
        Interactive F1 recruitment analytics with J1 exchange mobility shown as a secondary intelligence layer.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="intel-banner">
    <h3 style="color:white; margin-bottom:6px;">🐾 Recruitment Intelligence Engine</h3>
    <p style="color:#E5E7EB; margin-bottom:0;">
    F1 remains the main enrollment recruitment signal. J1 is included on the side to show exchange, scholar, and global mobility activity.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

k1, k2, k3, k4, k5, k6, k7 = st.columns(7)

k1.metric("Country", selected_country)
k2.metric("F1 Issuances", f"{country_total:,}")
k3.metric("F1 Posts", active_posts)
k4.metric("J1 Issuances", f"{j1_total:,}")
k5.metric("J1 Posts", j1_posts)
k6.metric("F1 Peak Month", month_name(peak_month))
k7.metric("Tier", tier.split(":")[0])

# =========================================================
# TABS
# =========================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "🌍 Command Map",
    "🏛️ Country Deep Dive",
    "📊 Global Rankings",
    "🧠 Strategy Console"
])

# =========================================================
# TAB 1 — MAP
# =========================================================
with tab1:
    st.markdown("### 🌍 Global F1 Recruitment Command Map")

    country_rank = (
        f1.groupby("country")["issuances"]
        .sum()
        .reset_index()
        .sort_values("issuances", ascending=False)
    )

    country_lat_lon = {
        "India": (22.97, 78.65), "China": (35.86, 104.19), "Vietnam": (14.05, 108.27),
        "Nepal": (28.39, 84.12), "Bangladesh": (23.68, 90.35), "Pakistan": (30.37, 69.34),
        "Zimbabwe": (-19.01, 29.15), "Nigeria": (9.08, 8.67), "Ghana": (7.94, -1.02),
        "Kenya": (-0.02, 37.90), "South Africa": (-30.55, 22.93),
        "South Korea": (35.90, 127.76), "Japan": (36.20, 138.25), "Taiwan": (23.69, 120.96),
        "Brazil": (-14.23, -51.92), "Colombia": (4.57, -74.29), "Mexico": (23.63, -102.55),
        "United Kingdom": (55.37, -3.43), "France": (46.22, 2.21), "Germany": (51.16, 10.45),
        "Italy": (41.87, 12.56), "Spain": (40.46, -3.74), "Ireland": (53.14, -7.69),
        "Philippines": (12.87, 121.77), "Indonesia": (-0.78, 113.92), "Thailand": (15.87, 100.99),
        "Saudi Arabia": (23.88, 45.07), "United Arab Emirates": (23.42, 53.84),
        "Turkey": (38.96, 35.24), "Canada": (56.13, -106.34), "Australia": (-25.27, 133.77),
        "Argentina": (-38.41, -63.61), "Chile": (-35.67, -71.54), "Peru": (-9.19, -75.02),
        "Ecuador": (-1.83, -78.18), "Jamaica": (18.10, -77.29),
        "Dominican Republic": (18.74, -70.16), "Malaysia": (4.21, 101.98),
        "Singapore": (1.35, 103.82), "Kazakhstan": (48.01, 66.92), "Mongolia": (46.86, 103.84),
        "Egypt": (26.82, 30.80), "Morocco": (31.79, -7.09),
        "Romania": (45.94, 24.96), "Bulgaria": (42.73, 25.48),
        "Poland": (51.91, 19.15), "Sweden": (60.13, 18.64),
        "Norway": (60.47, 8.46), "Netherlands": (52.13, 5.29),
        "Belgium": (50.50, 4.47), "Switzerland": (46.81, 8.22),
        "Austria": (47.52, 14.55), "Czech Republic": (49.81, 15.47),
        "Hungary": (47.16, 19.50), "Serbia": (44.02, 21.00),
        "Croatia": (45.10, 15.20), "Denmark": (56.26, 9.50),
        "New Zealand": (-40.90, 174.88)
    }

    country_rank["lat"] = country_rank["country"].map(lambda x: country_lat_lon.get(x, (None, None))[0])
    country_rank["lon"] = country_rank["country"].map(lambda x: country_lat_lon.get(x, (None, None))[1])

    map_data = country_rank.dropna(subset=["lat", "lon"]).copy()
    map_data["bubble_size"] = (map_data["issuances"] / map_data["issuances"].max()) * 80 + 8

    selected_data = map_data[map_data["country"] == selected_country]

    fig_map = go.Figure()

    fig_map.add_trace(
        go.Scatter(
            x=map_data["lon"],
            y=map_data["lat"],
            mode="markers+text",
            text=map_data["country"],
            textposition="top center",
            marker=dict(
                size=map_data["bubble_size"],
                color=map_data["issuances"],
                colorscale=[[0, "#3D8DDE"], [1, "#FFB81C"]],
                showscale=True,
                colorbar=dict(title="F1 Issuances"),
                line=dict(width=1.5, color="white"),
                opacity=0.85
            ),
            hovertemplate="<b>%{text}</b><br>F1 Issuances: %{marker.color:,.0f}<extra></extra>",
            name="Countries"
        )
    )

    if not selected_data.empty:
        fig_map.add_trace(
            go.Scatter(
                x=selected_data["lon"],
                y=selected_data["lat"],
                mode="markers+text",
                text=[f"🐾 {selected_country}"],
                textposition="bottom center",
                marker=dict(
                    size=34,
                    color="#FFB81C",
                    line=dict(width=4, color="white"),
                    symbol="star"
                ),
                hovertemplate=f"<b>{selected_country}</b><br>Selected Market<extra></extra>",
                name="Selected Country"
            )
        )

    fig_map.update_layout(
        title="Interactive Global Recruitment Signal Map",
        height=720,
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(13,34,63,0.45)",
        xaxis=dict(
            title="Longitude",
            range=[-180, 180],
            gridcolor="rgba(255,255,255,0.12)",
            zerolinecolor="rgba(255,255,255,0.25)"
        ),
        yaxis=dict(
            title="Latitude",
            range=[-60, 75],
            gridcolor="rgba(255,255,255,0.12)",
            zerolinecolor="rgba(255,255,255,0.25)"
        ),
        margin=dict(l=20, r=20, t=70, b=20)
    )

    st.plotly_chart(fig_map, use_container_width=True)

    st.markdown(f"""
    <div class="gold">
        <h3>🐾 Selected Market: {selected_country}</h3>
        <p>This command map shows countries as recruitment signal bubbles. Bigger and brighter bubbles indicate stronger F1 student visa issuance activity.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# TAB 2 — COUNTRY DEEP DIVE
# =========================================================
with tab2:
    left, right = st.columns([2, 1])

    with left:
        monthly = country_data.groupby("date")["issuances"].sum().reset_index()

        fig_area = px.area(
            monthly,
            x="date",
            y="issuances",
            markers=True,
            title=f"Monthly F1 Trend — {selected_country}",
            color_discrete_sequence=["#FFB81C"]
        )

        fig_area.update_traces(line=dict(width=4, shape="spline"))
        fig_area.update_layout(
            template="plotly_dark",
            height=520,
            hovermode="x unified",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(13,34,63,0.35)"
        )

        st.plotly_chart(fig_area, use_container_width=True)

    with right:
        fig_posts = px.bar(
            top_posts.head(10),
            x="issuances",
            y="post",
            orientation="h",
            title="Top F1 Consulates / Posts",
            text_auto=True,
            color="issuances",
            color_continuous_scale=["#3D8DDE", "#FFB81C"]
        )

        fig_posts.update_layout(
            template="plotly_dark",
            height=520,
            yaxis=dict(autorange="reversed"),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(13,34,63,0.35)"
        )

        st.plotly_chart(fig_posts, use_container_width=True)

    c1, c2 = st.columns(2)

    with c1:
        month_line = country_data.groupby("month")["issuances"].sum().reset_index().sort_values("month")

        fig_season = px.bar(
            month_line,
            x="month",
            y="issuances",
            title=f"F1 Seasonality Pattern — {selected_country}",
            text_auto=True,
            color="issuances",
            color_continuous_scale=["#0D223F", "#3D8DDE", "#FFB81C"]
        )

        fig_season.update_layout(
            template="plotly_dark",
            height=430,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(13,34,63,0.35)"
        )

        st.plotly_chart(fig_season, use_container_width=True)

    with c2:
        top5 = top_posts.head(5)["post"].tolist()

        post_month = (
            country_data[country_data["post"].isin(top5)]
            .groupby(["month", "post"])["issuances"]
            .sum()
            .reset_index()
        )

        fig_post_month = px.line(
            post_month,
            x="month",
            y="issuances",
            color="post",
            markers=True,
            line_shape="spline",
            title="Top F1 Consulate Seasonality"
        )

        fig_post_month.update_layout(
            template="plotly_dark",
            height=430,
            hovermode="x unified",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(13,34,63,0.35)"
        )

        st.plotly_chart(fig_post_month, use_container_width=True)

    medals = ["🥇", "🥈", "🥉", "🏅", "🏅"]
    badge_html = ""

    for i, row in top_posts.head(5).reset_index(drop=True).iterrows():
        badge_html += f"<span class='badge'>{medals[i]} {row['post']}: {int(row['issuances']):,} F1</span>"

    st.markdown("### 🏅 Top F1 Post Badges")
    st.markdown(badge_html, unsafe_allow_html=True)

    st.markdown("## 🎓 F1 vs J1 Mobility Comparison")

    compare_visa = df[
        (df["country"] == selected_country) &
        (df["visa_class"].isin(["F1", "J1"]))
    ]

    compare_visa = (
        compare_visa
        .groupby(["date", "visa_class"])["issuances"]
        .sum()
        .reset_index()
    )

    fig_compare_visa = px.line(
        compare_visa,
        x="date",
        y="issuances",
        color="visa_class",
        markers=True,
        line_shape="spline",
        title=f"F1 vs J1 Trends — {selected_country}",
        color_discrete_map={
            "F1": "#FFB81C",
            "J1": "#3D8DDE"
        }
    )

    fig_compare_visa.update_layout(
        template="plotly_dark",
        height=500,
        hovermode="x unified",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(13,34,63,0.35)"
    )

    st.plotly_chart(fig_compare_visa, use_container_width=True)

# =========================================================
# TAB 3 — GLOBAL RANKINGS
# =========================================================
with tab3:
    country_rank = (
        f1.groupby("country")["issuances"]
        .sum()
        .reset_index()
        .sort_values("issuances", ascending=False)
    )

    fig_rank = px.bar(
        country_rank.head(35),
        x="country",
        y="issuances",
        title="Top F1 Recruitment Countries",
        text_auto=True,
        color="issuances",
        color_continuous_scale=["#3D8DDE", "#FFB81C"]
    )

    fig_rank.update_layout(
        template="plotly_dark",
        height=620,
        xaxis_tickangle=-45,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(13,34,63,0.35)"
    )

    st.plotly_chart(fig_rank, use_container_width=True)

    compare_data = (
        f1[f1["country"].isin(compare_countries)]
        .groupby(["date", "country"])["issuances"]
        .sum()
        .reset_index()
    )

    fig_compare = px.line(
        compare_data,
        x="date",
        y="issuances",
        color="country",
        markers=True,
        line_shape="spline",
        title="F1 Country Comparison Over Time"
    )

    fig_compare.update_layout(
        template="plotly_dark",
        height=560,
        hovermode="x unified",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(13,34,63,0.35)"
    )

    st.plotly_chart(fig_compare, use_container_width=True)

    j1_rank = (
        j1.groupby("country")["issuances"]
        .sum()
        .reset_index()
        .sort_values("issuances", ascending=False)
    )

    fig_j1_rank = px.bar(
        j1_rank.head(20),
        x="country",
        y="issuances",
        title="Top J1 Mobility Countries Side View",
        text_auto=True,
        color="issuances",
        color_continuous_scale=["#0D223F", "#3D8DDE"]
    )

    fig_j1_rank.update_layout(
        template="plotly_dark",
        height=520,
        xaxis_tickangle=-45,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(13,34,63,0.35)"
    )

    st.plotly_chart(fig_j1_rank, use_container_width=True)

    st.dataframe(country_rank, use_container_width=True, height=360)

# =========================================================
# TAB 4 — STRATEGY CONSOLE
# =========================================================
with tab4:
    growth_text = "N/A" if growth is None else f"{growth:.1f}%"
    cv_text = "N/A" if cv is None else f"{cv:.2f}"
    j1_peak_text = "N/A" if j1_peak_month == 0 else month_name(j1_peak_month)

    st.markdown(f"""
    <div class="ai">
        <h3>🧠 Recruitment Strategy Console</h3>
        <p><b>Country:</b> {selected_country}</p>
        <p><b>Total F1 Issuances:</b> {country_total:,}</p>
        <p><b>Top F1 Consulate/Post:</b> {top_post}</p>
        <p><b>Comparable Jan–Sep F1 Growth:</b> {growth_text}</p>
        <p><b>F1 Seasonality CV:</b> {cv_text}</p>
        <p><b>Market Tier:</b> {tier}</p>
        <hr>
        <p><b>J1 Side Signal:</b> {j1_total:,} issuances</p>
        <p><b>Top J1 Post:</b> {j1_top_post}</p>
        <p><b>J1 Peak Month:</b> {j1_peak_text}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(recommendation(selected_country, country_total, growth, cv, peak_month, top_post, j1_total))

    with st.expander("🌐 Optional live country context"):
        st.caption("This requires an OPENAI_API_KEY in Terminal. If not enabled, use the data-driven recommendation above.")

        if st.button("Generate live country context"):
            with st.spinner("Generating current country context..."):
                result = live_ai_context(selected_country, country_total, growth, cv)

            if result:
                st.markdown(result)
            else:
                st.info("Live context is not enabled. Add OPENAI_API_KEY to use this feature.")

    st.markdown("""
    <div class="glass">
        <h3>Interpretation Note</h3>
        <p>F1 is the main recruitment/enrollment signal. J1 is included as a secondary signal for exchange, visiting scholar, and broader global mobility patterns. Visa issuance volume is not the same as approval probability.</p>
    </div>
    """, unsafe_allow_html=True)
