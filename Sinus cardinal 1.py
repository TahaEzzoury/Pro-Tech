import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip, AudioClip
import os


# Set the wd
directory = 'C:\\Users\\tahae\\OneDrive\\Bureau\\2A\\ProTech'
os.chdir(directory)

# Paramètres de la vidéo
duration = 10  # Durée en secondes
fps = 24       # Images par seconde

# Fonction sinus cardinal à sonifier et à visualiser
def sinc(x):
    return np.sinc(x / np.pi)

# Création du graphique
def make_frame(t):
    x = np.linspace(-10, 10, 1000)
    y = sinc(x)
    current_x = (t / duration) * 20 - 10  # Mise à l'échelle de t
    current_y = sinc(current_x)

    fig, ax = plt.subplots()
    ax.plot(x, y, lw=2)
    ax.scatter([current_x], [current_y], color='red')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-0.5, 1)  # Ajustement de la plage y

    # Convertir le graphique en image numpy
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return image

# Génération du son
def make_sound(t):
    current_x = (t / duration) * 20 - 10
    current_y = sinc(current_x)
    frequency = (current_y + 1) * 220 + 220  # Ajustement de la fréquence

    # Générer un échantillon sonore pour ce moment
    return 0.5 * np.sin(frequency * 2 * np.pi * t)

# Création de la vidéo
video = VideoClip(make_frame, duration=duration)

# Création de la piste audio
audio = AudioClip(make_sound, duration=duration)
video = video.set_audio(audio)

# Sauvegarde de la vidéo
video.write_videofile("Sonification_de_sinc.mp4", fps=fps)
