from voice_cloning.generation import *

sound_path = r"test.wav"
speech_text = "Please use this package carefully"

generated_wav = speech_generator(
    voice_type = "indian",
    sound_path = sound_path, 
    speech_text=  speech_text
    )

play_sound(generated_wav)

save_sound(generated_wav, filename="voice output", noise_reduction=True)