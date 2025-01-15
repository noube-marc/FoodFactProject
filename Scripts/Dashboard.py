import streamlit as st

st.title("Tableau de bord Food Fact project")

st.write("J'ai déployé cette application Streamlit pour permettre aux utilisateurs d'interagir avec elle. En effet, le tableau de bord ne peut pas être affiché directement, car vous n'avez pas accès au modèle sémantique. C'est pourquoi j'ai créé cette petite page Streamlit pour vous permettre d'accéder au tableau.")

tableau_url = "https://app.fabric.microsoft.com/reportEmbed?reportId=2a75c61d-eb3c-4256-b4b5-d954b369c302&autoAuth=true&ctid=08e06420-c505-4a4e-b259-e7ceee464ce8"
st.components.v1.iframe(width=1140, height=541.25, src="https://app.fabric.microsoft.com/reportEmbed?reportId=2a75c61d-eb3c-4256-b4b5-d954b369c302&autoAuth=true&ctid=08e06420-c505-4a4e-b259-e7ceee464ce8")