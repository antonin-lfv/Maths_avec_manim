import streamlit as st
from manim import Scene, Arrow, RED, ORIGIN, Transform, NumberLine
from pathlib import Path
from config import CSS

st.set_page_config(page_title="1D transformation", layout="wide")
st.write(CSS, unsafe_allow_html=True)


# Fonction pour générer l'animation avec Manim
def create_1d_transformation_animation(scalar):

    class Scene_class(Scene):
        def construct(self):
            # Création d'une ligne numérique pour représenter l'axe des x
            number_line = NumberLine(x_range=[-5, 5, 1], include_numbers=True)
            self.add(number_line)

            # Vecteur sur l'axe des x, de longueur exactement 1
            vector = Arrow(ORIGIN, [1, 0, 0], buff=0, color=RED)

            # Ajout du vecteur initial
            self.add(vector)

            # Transformation du vecteur
            transformed_vector = Arrow(ORIGIN, [scalar, 0, 0], buff=0, color=RED)

            # Animation de la transformation
            self.wait(1)
            self.play(Transform(vector, transformed_vector))
            self.wait(1)

    temp_file = Path("media/videos/1080p60/Scene_class.mp4")
    scene = Scene_class()
    scene.render()
    return temp_file


# Interface utilisateur Streamlit
st.title("Transformation Scalaire 1D avec Manim")

st.write("##")

# Demande à l'utilisateur d'entrer le scalaire de transformation
st.write("Entrez un scalaire pour effectuer la transformation du vecteur :")

col1, _, col2 = st.columns([1, 1, 2])

with col1:
    scalar = st.number_input("Scalaire", value=1.0, min_value=-5.0, max_value=5.0)

with col2:
    # Afficher la transformation scalaire
    st.write(f"Votre transformation :")
    st.latex(rf"v \mapsto {scalar} \cdot v")

st.write("##")

# Créer la transformation scalaire
if st.button("Appliquer la transformation"):
    with st.spinner("Création de l'animation..."):
        animation_file = create_1d_transformation_animation(scalar)
        _, video_col, _ = st.columns([1, 3, 1])
        video_col.video(
            str(animation_file), format="video/mp4", autoplay=True, loop=True
        )
