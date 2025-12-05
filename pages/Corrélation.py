import streamlit as st
import matplotlib.pyplot as plt




# Calcul de la corrélation entre les colonnes polluantes
correlation_polluants = st.session_state.qualite[st.session_state.polluants].corr()

import seaborn as sns


# seaborn pour l'esthétique
st.subheader("Corrélation entre polluants")
fig, ax = plt.subplots(figsize=(8, 6))

sns.heatmap(
    correlation_polluants,
    annot=True,          # valeurs sur les cases
    fmt=".2f",           # 2 décimales
    cmap="coolwarm",     # palette de couleur
    cbar=True,           # barre de couleur
    linewidths=0.5,      # séparations des cases
    linecolor="white",   # couleur des séparations
    ax=ax
)
st.pyplot(fig)

txt = st.text_area("Interprétation",
    "On remarque en premier lieu le fait que la température n'est reliée à aucune variable. Pourtant on pourrait penser que le CO2 puisse affecter la température moyenne..."
)
txt = st.text_area("Interprétation",
    "Les deux variables les plus corrélées entre elles sont les variables NO (Monoxyde d'azote) et NO2 (Dioxyde d'azote)."
    "Ce n'est d'ailleurs pas étonnant car Il est formé par l'oxydation du monoxyde d'azote dans l'atmosphère. " \
    "Le NO2 est un oxydant fort et contribue à la formation d'ozone troposphérique, un polluant atmosphérique majeur.  " \
    ""
    "Heureusement comme montré au dessus grâce au graphique d'évolution des polluants, on sait que le NO2 a subit une grande chute depuis 2020 et ne cesse de décroitre année après année."
)

