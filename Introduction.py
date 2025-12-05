import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt



qualite = pd.read_csv("qualite-de-lair-mesuree-dans-la-station-chatelet-2021-maintenant.csv", sep=";")

# Conversion de la colonne "DATE/HEURE"
qualite["DATE/HEURE"] = pd.to_datetime(qualite["DATE/HEURE"], errors="coerce", utc=True)

# Création des colonnes ANNEE / MOIS / JOUR
qualite["ANNEE"] = qualite["DATE/HEURE"].dt.year
qualite["MOIS"] = qualite["DATE/HEURE"].dt.month
qualite["JOUR"] = qualite["DATE/HEURE"].dt.day


# Supprimer les lignes où ANNEE == 2025 car pas complète, trop de NA, et supp la colonne date heure mtn que jai 3 colonnes equivalentes
qualite = qualite[qualite["ANNEE"] != 2025]
qualite = qualite.drop(columns=["DATE/HEURE"])


polluants = ["NO", "NO2", "PM10", "CO2", "TEMP", "HUMI"]
for col in polluants:
    # Remplacer la virgule par un point puis convertir en float
    qualite[col] = pd.to_numeric(qualite[col].astype(str).str.replace(",", "."), errors="coerce")



#-----affichage
st.title("Dashboard : Qualité de l'air - Station Châtelet / Analyse des polluants mesurés entre 2021 et 2024")
    

#st.caption("Tableau de donnée filtré")
#st.dataframe(qualite.head())


st.caption("Tableau de données filtré par année")
annees_dispo = sorted(qualite["ANNEE"].unique())
choix_annee = st.selectbox("Année", annees_dispo)
st.dataframe(qualite[qualite["ANNEE"] == choix_annee])

#----------------
polluant_par_annee = (
    qualite.groupby("ANNEE")[polluants]
    .mean()
    .reset_index()
)
# Convertir ANNEE en entier pour l'affichage
polluant_par_annee["ANNEE"] = polluant_par_annee["ANNEE"].astype(int)

st.subheader("Evolution au fil du temps") 
st.markdown(
    '<span style="background-color:#D3E5F8; padding:4px; border-radius:4px">'
    'Choisissez un polluant ou une autre variable :</span>',
    unsafe_allow_html=True
)
choix_polluant = st.selectbox("", polluants)
df_plot = polluant_par_annee[["ANNEE", choix_polluant]]


#-----graph

couleurs_polluants = {
    "NO": "#220901",
    "NO2": "#621708",
    "PM10": "#941b0c",
    "CO2": "#bc3908",
    "TEMP": "#f6aa1c",
    "HUMI": "#ffea00",
}

color = couleurs_polluants.get(choix_polluant)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df_plot["ANNEE"], df_plot[choix_polluant], marker="o", color = color)

ax.set_xticks(df_plot["ANNEE"])  # une tick par année
ax.set_xticklabels(df_plot["ANNEE"].astype(int))  # labels en int
ax.set_title(f"Évolution moyenne de {choix_polluant} entre 2021 et 2024")
ax.set_xlabel("Année")
ax.set_ylabel("Valeur moyenne")
ax.grid(True, linestyle="--", alpha=0.6)

st.pyplot(fig)

#interpretation, widget a l'aide de la documentation Streamlit
txt = st.text_area("Interprétation",
    "La température et le CO2 ne font qu'augmenter depuis 2020, seule l'humidité a connu une petite chute en 2022 avant de croitre à nouveau."
)


st.session_state.qualite = qualite
st.session_state.polluants = polluants
st.session_state.df_plot = df_plot
st.session_state.choix_polluant = choix_polluant

