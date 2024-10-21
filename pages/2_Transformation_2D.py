import streamlit as st
import numpy as np
from manim import Scene, Arrow, ORIGIN, RED, GREEN, Transform, NumberPlane
from pathlib import Path
from config import CSS

st.set_page_config(page_title="2D transformation", layout="wide")
st.write(CSS, unsafe_allow_html=True)


# Fonction pour générer l'animation avec Manim
def create_2d_transformation_animation(matrix):

    class Scene_class(Scene):
        def construct(self):
            axes = NumberPlane()
            self.add(axes)

            i_vector = Arrow(ORIGIN, [1, 0, 0], buff=0, color=RED)
            j_vector = Arrow(ORIGIN, [0, 1, 0], buff=0, color=GREEN)

            self.add(i_vector, j_vector)

            transformed_i = Arrow(
                ORIGIN, [matrix[0][0], matrix[1][0], 0], buff=0, color=RED
            )
            transformed_j = Arrow(
                ORIGIN, [matrix[0][1], matrix[1][1], 0], buff=0, color=GREEN
            )

            self.wait(1)
            self.play(
                Transform(i_vector, transformed_i), Transform(j_vector, transformed_j)
            )
            self.wait(1)

    temp_file = Path("media/videos/1080p60/Scene_class.mp4")
    scene = Scene_class()
    scene.render()
    return temp_file


# Interface utilisateur Streamlit
st.title("Transformation Matricielle 2D avec Manim")

st.write("##")

# Demande à l'utilisateur de définir les éléments de la matrice de transformation
st.write("Entrez une matrice 2x2 pour effectuer la transformation sur le repère :")

col1, col2, _, col3 = st.columns((1, 1, 1, 2))

with col1:
    a = st.number_input("a", value=1.0, min_value=-3.0, max_value=3.0)
    c = st.number_input("c", value=0.0, min_value=-3.0, max_value=3.0)
with col2:
    b = st.number_input("b", value=0.0, min_value=-3.0, max_value=3.0)
    d = st.number_input("d", value=1.0, min_value=-3.0, max_value=3.0)
with col3:
    # Afficher la matrice de transformation avec les valeurs entrées
    st.write("Votre matrice de transformation :")
    st.latex(
        rf"\begin{{bmatrix}} a & b \\ c & d \end{{bmatrix}} = \begin{{bmatrix}} {a} & {b} \\ {c} & {d} \end{{bmatrix}}"
    )

# Créer la matrice de transformation
matrix = np.array([[a, b], [c, d]])

if st.button("Appliquer la transformation"):
    with st.spinner("Création de l'animation..."):
        animation_file = create_2d_transformation_animation(matrix)
        _, video_col, _ = st.columns([1, 3, 1])
        video_col.video(
            str(animation_file), format="video/mp4", autoplay=True, loop=True
        )
