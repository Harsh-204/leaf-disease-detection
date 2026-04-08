import streamlit as st
import requests
import json

# Set Streamlit theme to premium light mode
st.set_page_config(
    page_title="Leaf Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Modern Premium CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

    /* Global fonts and background */
    .stApp {
        background: radial-gradient(circle at top right, #e8f5e9 0%, #f1f8e9 40%, #ffffff 100%);
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    h1, h2, h3, .disease-title, .hero-title {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
        background: rgba(255, 255, 255, 0.4);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        border: 1px solid rgba(255,255,255,0.8);
        box-shadow: 0 10px 40px rgba(0,0,0,0.03);
        margin-bottom: 2rem;
    }
    .hero-title {
        color: #1b5e20;
        font-size: 3.5rem;
        font-weight: 700;
        letter-spacing: -1px;
        margin-bottom: 0.2rem;
        background: linear-gradient(135deg, #2e7d32 0%, #004d40 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        color: #546e7a;
        font-size: 1.2rem;
        font-weight: 500;
    }

    /* Glassmorphism Result Card */
    .result-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
        padding: 2.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px 0 rgba(31, 38, 135, 0.08);
    }

    .disease-title {
        color: #1b5e20;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    /* Badges */
    .badge-container {
        display: flex;
        gap: 10px;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    .info-badge {
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
        color: #2e7d32;
        border-radius: 50px;
        padding: 0.4rem 1rem;
        font-size: 0.95rem;
        font-weight: 600;
        border: 1px solid rgba(76, 175, 80, 0.2);
    }
    .info-badge.severity-high {
        background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
        color: #c62828;
        border-color: rgba(244, 67, 54, 0.2);
    }
    .info-badge.healthy {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        color: #1565c0;
        border-color: rgba(33, 150, 243, 0.2);
    }

    /* Progress bars for severity/confidence */
    .metric-label {
        font-size: 0.95rem;
        color: #546e7a;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }

    /* Timestamp */
    .timestamp {
        color: #90a4ae;
        font-size: 0.85rem;
        text-align: right;
        margin-top: 2rem;
        font-weight: 500;
    }

    /* Streamlit overrides */
    div.stButton > button {
        background: linear-gradient(135deg, #43a047 0%, #2e7d32 100%);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 2rem;
        font-family: 'Outfit', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(67, 160, 71, 0.3);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(67, 160, 71, 0.4);
        background: linear-gradient(135deg, #4caf50 0%, #388e3c 100%);
        color: white;
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.2rem !important;
        }
        .hero-subtitle {
            font-size: 1rem !important;
        }
        .hero-container {
            padding: 1.5rem 1rem 1rem 1rem !important;
        }
        .disease-title {
            font-size: 1.8rem !important;
        }
        .result-card {
            padding: 1.5rem !important;
        }
        div.stButton > button {
            padding: 0.5rem 1rem !important;
            font-size: 1rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# Main Header / Hero
st.markdown("""
    <div class="hero-container">
        <div style="font-size: 3.5rem; margin-bottom: -10px;">🌿</div>
        <h1 class="hero-title">Plant Health AI</h1>
        <p class="hero-subtitle">Upload a leaf image to Instantly detect diseases and get precision treatment plans.</p>
    </div>
""", unsafe_allow_html=True)

api_url = "http://localhost:8000"

# Main Layout
col1, space, col2 = st.columns([1, 0.1, 1.3])

with col1:
    st.markdown("### 📸 Image Input")
    
    tab1, tab2 = st.tabs(["📁 Upload", "📸 Capture"])
    
    uploaded_file = None
    
    with tab1:
        upload_img = st.file_uploader("Select a clear leaf image", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
        if upload_img is not None:
            st.image(upload_img, caption="Selected Leaf Image", use_container_width=True, clamp=True)
            uploaded_file = upload_img
            
    with tab2:
        camera_img = st.camera_input("Take a picture of a leaf", label_visibility="collapsed")
        if camera_img is not None:
            uploaded_file = camera_img

with col2:
    if uploaded_file is None:
        st.info("👋 Upload an image of a plant leaf in the panel on the left to begin analysis.")
    else:
        st.markdown("### 🔍 Diagnostics")
        analyze_btn = st.button("Analyze Leaf", use_container_width=True)
        
        if analyze_btn:
            with st.spinner("AI is analyzing the leaf parameters..."):
                try:
                    files = {
                        "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                    response = requests.post(f"{api_url}/disease-detection-file", files=files)
                    
                    if response.status_code == 200:
                        result = response.json()

                        # HTML building for the result card
                        if result.get("disease_type") == "invalid_image":
                            st.markdown("""
                            <div class='result-card'>
                                <div class='disease-title' style='color:#d32f2f;'>⚠️ Unrecognized Image</div>
                                <div class="badge-container">
                                    <span class='info-badge severity-high'>Invalid Scan</span>
                                </div>
                                <p style='color: #455a64; font-size: 1.05rem;'>The uploaded image does not appear to be a plant leaf. Please upload a clear image of a single leaf.</p>
                            </div>
                            """, unsafe_allow_html=True)

                        elif result.get("disease_detected"):
                            # Metrics extraction
                            conf = result.get('confidence', 0)
                            sev = result.get('severity', 'Unknown')
                            
                            sev_class = "severity-high" if sev.lower() in ['high', 'severe'] else ""
                            
                            st.markdown(f"""
                            <div class='result-card'>
                                <div class='disease-title'>🦠 {result.get('disease_name', 'Unknown Disease')}</div>
                                <div class='badge-container'>
                                    <span class='info-badge'>Type: {result.get('disease_type', 'Pathogen').capitalize()}</span>
                                    <span class='info-badge {sev_class}'>Severity: {sev.capitalize()}</span>
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            # Render confidence natively
                            st.markdown(f"<div class='metric-label'>AI Confidence: {conf}%</div>", unsafe_allow_html=True)
                            st.progress(int(conf))
                            st.write("")

                            # Interactive Expanders for Details
                            with st.expander("🩺 Observed Symptoms", expanded=True):
                                for symptom in result.get("symptoms", []):
                                    st.markdown(f"- {symptom}")
                            
                            with st.expander("🔬 Possible Causes", expanded=False):
                                for cause in result.get("possible_causes", []):
                                    st.markdown(f"- {cause}")
                                    
                            with st.expander("💊 Recommended Treatment", expanded=True):
                                st.success("Follow these steps to recover your plant:")
                                for treat in result.get("treatment", []):
                                    st.markdown(f"1. {treat}")

                            st.markdown(f"<div class='timestamp'>🕒 Analyzed at {result.get('analysis_timestamp', 'Unknown')}</div>", unsafe_allow_html=True)
                            
                        else:
                            # Healthy leaf case
                            conf = result.get('confidence', 0)
                            st.markdown(f"""
                            <div class='result-card' style='border-color: #a5d6a7;'>
                                <div class='disease-title' style='color:#2e7d32;'>✅ Perfectly Healthy</div>
                                <div class='badge-container'>
                                    <span class='info-badge healthy'>Status: Optimal</span>
                                </div>
                                <p style='color: #455a64; font-size: 1.05rem;'>No pathogens or stress indicators were detected. Your plant is thriving!</p>
                            </div>
                            """, unsafe_allow_html=True)
                            
                            st.markdown(f"<div class='metric-label'>AI Confidence: {conf}%</div>", unsafe_allow_html=True)
                            st.progress(int(conf))
                            
                            st.markdown(f"<div class='timestamp'>🕒 Analyzed at {result.get('analysis_timestamp', 'Unknown')}</div>", unsafe_allow_html=True)

                    else:
                        st.error(f"API Error ({response.status_code}): Could not connect to analysis engine.")
                except Exception as e:
                    st.error(f"System Error: {str(e)}")
