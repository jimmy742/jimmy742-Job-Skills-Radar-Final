import os
# Fix for OpenBLAS memory allocation issues
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'

import streamlit as st

# Configuration globale
st.set_page_config(page_title="Job-Skills Radar", page_icon="🎯", layout="wide")

# CSS pour l'image de fond et le style moderne
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
        url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072");
        background-size: cover;
    }
    .main-card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        color: white;
        text-align: center;
    }
    h1, h2, h3 { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# Contenu de l'accueil
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("🎯 Bienvenue sur Job-Skills Radar")
st.subheader("Observatoire Intelligent de l'Emploi IT au Cameroun")
st.write("""
    Cette plateforme interactive permet de collecter en temps réel les besoins des entreprises 
    et d'analyser les compétences les plus demandées sur le marché local.
    
    **Instructions :**
    1. Allez dans l'onglet **Collecte** pour enregistrer de nouvelles offres.
    2. Consultez l'onglet **Analyse** pour voir les statistiques dynamiques.
""")
if st.button("Commencer l'analyse"):
    st.info("Utilisez le menu à gauche pour naviguer 👈")
st.markdown('</div>', unsafe_allow_html=True)