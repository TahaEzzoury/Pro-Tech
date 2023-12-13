import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip, AudioClip
from scipy.io.wavfile import write

# Paramètres de la vidéo
duration = 10  # Durée en secondes
fps = 24  # Images par seconde

# Fonction à sonifier et à visualiser
def f(x):
    return x ** 2

# Création du graphique
def make_frame(t):
    x = np.linspace(0, 1, 500)
    y = f(x)
    current_x = t / duration
    current_y = f(current_x)

    fig, ax = plt.subplots()
    ax.plot(x, y, lw=2)
    ax.scatter([current_x], [current_y], color='red')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Convertir le graphique en image numpy
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return image

# Génération du son
def make_sound(t):
    current_y = f(t / duration)
    frequency = 440 + current_y * 440  # Exemple de mapping de la fréquence
    return np.sin(frequency * 2 * np.pi * t)

# Création de la vidéo
video = VideoClip(make_frame, duration=duration)

# Création de la piste audio
audio = AudioClip(make_sound, duration=duration)
video = video.set_audio(audio)

# Sauvegarde de la vidéo
video.write_videofile("Sonification_y=x².mp4", fps=fps)
