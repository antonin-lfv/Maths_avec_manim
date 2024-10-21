import streamlit as st
from config import CSS

st.set_page_config(page_title="Accueil", page_icon=":house:", layout="wide")
st.write(CSS, unsafe_allow_html=True)

st.markdown(
    """
    <p class='title'>Bienvenue sur <span class='underlined_text'>L'algèbre linéaire avec Manim</span></p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# Description de l'application
st.markdown(
    """
<div class='description'>
Cette application interactive, développée avec <strong>Streamlit</strong> et <strong>Manim</strong>, vous permet de visualiser de manière intuitive et dynamique les transformations mathématiques en 1D, 2D et 3D.

##

### Fonctionnalités :
- **Transformations 1D** : Visualisez des transformations simples sur des vecteurs dans une dimension.
- **Transformations 2D** : Explorez les effets des matrices de transformation sur des vecteurs dans un plan bidimensionnel.
- **Transformations 3D** : Observez comment des matrices 3x3 affectent les vecteurs dans un espace tridimensionnel à l'aide d'animations interactives.
</div>
""",
    unsafe_allow_html=True,
)

# Boutons pour accéder aux pages 1D, 2D, 3D
st.write("##")

col1, col2, col3, _ = st.columns((1, 1, 1, 4))
col1.page_link("pages/1_Transformation_1D.py", label="Accéder à la page 1D")
st.write("##")
col2.page_link("pages/2_Transformation_2D.py", label="Accéder à la page 2D")
st.write("##")
col3.page_link("pages/3_Transformation_3D.py", label="Accéder à la page 3D")
