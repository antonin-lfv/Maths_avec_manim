import streamlit as st
import numpy as np
from manim import (
    ThreeDAxes,
    Arrow,
    ORIGIN,
    RED,
    GREEN,
    BLUE,
    Transform,
    ThreeDScene,
    PI,
)
from pathlib import Path
from config import CSS

st.set_page_config(page_title="3D transformation", layout="wide")
st.write(CSS, unsafe_allow_html=True)


# Fonction pour générer l'animation avec Manim
def create_3d_transformation_animation(matrix):

    class Scene_class(ThreeDScene):
        def construct(self):
            # Création du repère 3D
            axes = ThreeDAxes()
            self.add(axes)

            # Vecteurs unitaires i, j, k
            i_vector = Arrow(ORIGIN, [1, 0, 0], buff=0, color=RED)  # Axe x
            j_vector = Arrow(ORIGIN, [0, 1, 0], buff=0, color=GREEN)  # Axe y
            k_vector = Arrow(ORIGIN, [0, 0, 1], buff=0, color=BLUE)  # Axe z

            # Ajout des vecteurs au repère
            self.add(i_vector, j_vector, k_vector)

            # Déplacer la caméra pour mieux voir le repère en 3D (vue sur le côté)
            self.set_camera_orientation(phi=70 * PI / 180, theta=45 * PI / 180)

            # Vecteurs transformés selon la matrice de transformation 3x3
            transformed_i = Arrow(
                ORIGIN, [matrix[0][0], matrix[1][0], matrix[2][0]], buff=0, color=RED
            )
            transformed_j = Arrow(
                ORIGIN, [matrix[0][1], matrix[1][1], matrix[2][1]], buff=0, color=GREEN
            )
            transformed_k = Arrow(
                ORIGIN, [matrix[0][2], matrix[1][2], matrix[2][2]], buff=0, color=BLUE
            )

            # Animation de la transformation
            self.begin_ambient_camera_rotation(rate=0.3)
            self.wait(1)
            self.play(  # Faire tourner la caméra vers la droite avec la méthode move_camera
                Transform(i_vector, transformed_i, run_time=2),
                Transform(j_vector, transformed_j, run_time=2),
                Transform(k_vector, transformed_k, run_time=2),
            )
            self.wait(2)
            self.stop_ambient_camera_rotation()

    scene = Scene_class()
    scene.render()
    temp_file = Path("media/videos/1080p60/Scene_class.mp4")
    return temp_file


# Interface utilisateur Streamlit
st.title("Transformation Matricielle 3D avec Manim")

st.write("##")

# Demande à l'utilisateur de définir les éléments de la matrice de transformation
st.write("Entrez une matrice 3x3 pour effectuer la transformation sur le repère :")

col1, col2, col3, _, col4 = st.columns((1, 1, 1, 1, 2))

with col1:
    a = st.number_input("a", value=1.0, min_value=-3.0, max_value=3.0)
    d = st.number_input("d", value=0.0, min_value=-3.0, max_value=3.0)
    g = st.number_input("g", value=0.0, min_value=-3.0, max_value=3.0)
with col2:
    b = st.number_input("b", value=0.0, min_value=-3.0, max_value=3.0)
    e = st.number_input("e", value=1.0, min_value=-3.0, max_value=3.0)
    h = st.number_input("h", value=0.0, min_value=-3.0, max_value=3.0)
with col3:
    c = st.number_input("c", value=0.0, min_value=-3.0, max_value=3.0)
    f = st.number_input("f", value=0.0, min_value=-3.0, max_value=3.0)
    i = st.number_input("i", value=1.0, min_value=-3.0, max_value=3.0)

# Afficher la matrice de transformation avec les valeurs entrées
col4.write("Votre matrice de transformation :")
col4.latex(
    rf"\begin{{bmatrix}} a & b & c \\ d & e & f \\ g & h & i \end{{bmatrix}}=\begin{{bmatrix}} {a} & {b} & {c} \\ {d} & {e} & {f} \\ {g} & {h} & {i} \end{{bmatrix}}"
)

# Créer la matrice de transformation
matrix = np.array([[a, b, c], [d, e, f], [g, h, i]])

if st.button("Appliquer la transformation"):
    with st.spinner("Création de l'animation..."):
        animation_file = create_3d_transformation_animation(matrix)
        _, video_col, _ = st.columns([1, 3, 1])
        video_col.video(
            str(animation_file), format="video/mp4", autoplay=True, loop=True
        )
