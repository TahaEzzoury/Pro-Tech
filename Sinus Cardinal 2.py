import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from moviepy.editor import *
import os


# Set the wd
directory = 'C:\\Users\\tahae\\OneDrive\\Bureau\\2A\\ProTech'
os.chdir(directory)

# Paramètres de la vidéo et de l'audio
duration = 10  # Durée en secondes
fps = 24       # Images par seconde
sampling_rate = 44100  # Taux d'échantillonnage pour l'audio

# Fonction sinus cardinal
def sinc(x):
    return np.sinc(x / np.pi)

# Génération du signal audio
t = np.linspace(0, duration, duration * sampling_rate, endpoint=False)
frequencies = (sinc((t / duration) * 20 - 10) + 1) * 220 + 220
audio_signal = 0.5 * np.sin(2 * np.pi * frequencies * t)
audio_signal = np.int16(audio_signal / np.max(np.abs(audio_signal)) * 32767)

# Sauvegarde du fichier audio
write("sinc_sound.wav", sampling_rate, audio_signal)

# Création des images pour chaque cadre de la vidéo
for frame_number in range(duration * fps):
    t = frame_number / fps
    x = np.linspace(-10, 10, 1000)
    y = sinc(x)
    current_x = (t / duration) * 20 - 10
    current_y = sinc(current_x)

    fig, ax = plt.subplots()
    ax.plot(x, y, lw=2)
    ax.scatter([current_x], [current_y], color='red')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-0.5, 1)
    plt.savefig(f"frame_{frame_number}.png")
    plt.close()

# Assemblage de la vidéo avec ffmpeg
clip = ImageSequenceClip([f"frame_{i}.png" for i in range(duration * fps)], fps=fps)
audio = AudioFileClip("sinc_sound.wav")
video = clip.set_audio(audio)
video.write_videofile("Sonification_de_sinc.mp4", fps=fps)
