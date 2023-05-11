""" 
Created on : 02/05/23 4:27 pm
@author : ds  
"""

from pydub import AudioSegment
import ffmpeg

input_audio = ffmpeg.input('New Recording 3.m4a')
output_audio = ffmpeg.output(input_audio, "example.mp3")
ffmpeg.run(output_audio)