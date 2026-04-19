import os
# Fix for OpenBLAS memory allocation issues
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'

import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Collecte de Données", page_icon="📝", layout="wide")

# Configuration fichier
FICHIER_DONNEES = "offres_emploi.csv"

st.title("Enregistrement des Offres")
st.write("Remplissez le formulaire pour alimenter la base de données.")

# Utilisation de colonnes pour centrer le formulaire
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    with st.form("form_collecte", clear_on_submit=True):
        st.subheader("Détails de l'annonce")
        poste = st.text_input("Intitulé du poste", placeholder="ex: Ingénieur DevOps")
        secteur = st.selectbox("Secteur", ["Banque", "Télécoms", "Startup", "Administration", "Industrie"])
        competences = st.multiselect("Compétences clés", 
            ["Python", "Java", "Cisco", "Cloud", "SQL", "React", "Docker", "Sécurité"])
        experience = st.number_input("Années d'expérience", 0, 20, 1)
        
        submit = st.form_submit_button("Sauvegarder l'offre")
        
        if submit:
            if poste and competences:
                nouvelle_ligne = pd.DataFrame([{
                    "Poste": poste,
                    "Secteur": secteur,
                    "Competences": ", ".join(competences),
                    "Experience": experience,
                    "Date": pd.Timestamp.now().strftime("%d/%m/%Y")
                }])
                
                if os.path.exists(FICHIER_DONNEES):
                    nouvelle_ligne.to_csv(FICHIER_DONNEES, mode='a', header=False, index=False)
                else:
                    nouvelle_ligne.to_csv(FICHIER_DONNEES, index=False)
                
                st.success("Données enregistrées avec succès !")
                st.balloons()
            else:
                st.error("Veuillez remplir les champs obligatoires.")
