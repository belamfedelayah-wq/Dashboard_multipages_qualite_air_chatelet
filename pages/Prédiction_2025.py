import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt



# X = variable explicative (année)
X = st.session_state.df_plot["ANNEE"].values.reshape(-1, 1)

# y = variable cible (le polluant choisi)
y = st.session_state.df_plot[st.session_state.choix_polluant].values

# Modèle
model = LinearRegression()
model.fit(X, y)

# Prédiction 2025
annee_pred = np.array([[2025]])
pred_2025 = model.predict(annee_pred)[0]

st.write(f"### Prédiction de '{st.session_state.choix_polluant}' pour 2025 ") #: **{pred_2025:.2f}**
st.caption(f"Variable {st.session_state.choix_polluant} chosie dans Introduction (à modifier si besoin)")


#graph de prédiction
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(st.session_state.df_plot["ANNEE"], y, marker="o", label="Données réelles")

# Ajouter la prédiction
ax.scatter(2025, pred_2025, color="red", label="Prédiction 2025")
ax.plot([st.session_state.df_plot["ANNEE"].iloc[-1], 2025],
        [y[-1], pred_2025],
        linestyle="--",
        color="red")

ax.set_title(f"Évolution et prédiction de {st.session_state.choix_polluant}")
ax.set_xlabel("Année")
ax.set_ylabel("Valeur moyenne")
ax.legend()

st.pyplot(fig)
