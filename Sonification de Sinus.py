import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip, AudioClip

# Paramètres de la vidéo
duration = 10  # Durée en secondes
fps = 24  # Images par seconde

# Fonction à sonifier et à visualiser
def f(x):
    return np.sin(x)

# Création du graphique
def make_frame(t):
    x = np.linspace(0, 2 * np.pi, 1000)
    y = f(x)
    current_x = (t / duration) * 2 * np.pi  # Mise à l'échelle de t
    current_y = f(current_x)

    fig, ax = plt.subplots()
    ax.plot(x, y, lw=2)
    ax.scatter([current_x], [current_y], color='red')
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)  # Ajustement de la plage y

    # Convertir le graphique en image numpy
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return image

# Génération du son
def make_sound(t):
    # Calculer la fréquence pour le moment actuel t
    current_x = (t / duration) * 2 * np.pi
    current_y = f(current_x)
    frequency = current_y * 440

    # Générer un échantillon sonore pour ce moment
    return 0.5 * np.sin(frequency * 2 * np.pi * t)


# Création de la vidéo
video = VideoClip(make_frame, duration=duration)

# Création de la piste audio
audio = AudioClip(make_sound, duration=duration)
video = video.set_audio(audio)

# Sauvegarde de la vidéo
video.write_videofile("Sonification_de_sinus.mp4", fps=fps)

