import os
# Fix for OpenBLAS memory allocation issues
os.environ['OPENBLAS_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['NUMEXPR_NUM_THREADS'] = '1'

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analyse Descriptive", page_icon="📊", layout="wide")

FICHIER_DONNEES = "offres_emploi.csv"

st.title("📊 Analyse Descriptive du Marché")

if os.path.exists(FICHIER_DONNEES):
    try:
        # Load data with memory optimization
        df = pd.read_csv(FICHIER_DONNEES, low_memory=True)

        if df.empty:
            st.warning("Le fichier de données est vide.")
        else:
            # KPIs en haut
            c1, c2, c3 = st.columns(3)
            c1.metric("Total d'offres", len(df))
            c2.metric("Secteur Top", df['Secteur'].mode()[0])
            c3.metric("Expérience Moyenne", f"{round(df['Experience'].mean(), 1)} ans")

            st.divider()

            # Graphiques
            col_a, col_b = st.columns(2)

            with col_a:
                st.subheader("Répartition par Secteur")
                secteur_counts = df['Secteur'].value_counts()
                fig_pie = px.pie(values=secteur_counts.values, names=secteur_counts.index, hole=0.4,
                                 color_discrete_sequence=px.colors.qualitative.Bold)
                st.plotly_chart(fig_pie, use_container_width=True)

            with col_b:
                st.subheader("Expérience requise par Poste")
                top_posts = df['Poste'].value_counts().head(10).index
                df_filtered = df[df['Poste'].isin(top_posts)]
                fig_bar = px.bar(df_filtered, x='Poste', y='Experience', color='Secteur')
                st.plotly_chart(fig_bar, use_container_width=True)

            st.divider()
            st.subheader("Données Brutes")
            st.dataframe(df, use_container_width=True)

    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {str(e)}")
        st.info("Essayez de vérifier le format du fichier offres_emploi.csv")
else:
    st.warning("Aucune donnée disponible. Allez d'abord sur la page Collecte.")
