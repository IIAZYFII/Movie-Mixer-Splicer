import random as rand

from moviepy.editor import *
import os
files = []
path  = "C:\path\to\folder\with\movies"

for file in os.listdir(path):
        files.append(file)

number_of_movies = len(files) - 1
clips = []

#number of clips you want to splice
amount_of_splices = 10

#Maximum clip size
max_clip_size = 300

#Minimum clip size
minimum_clip_size = 0
for i in range(amount_of_splices):
    clip_number = rand.randint(0,number_of_movies)
    file_path = path + '/' + files[clip_number]
    clip = VideoFileClip(file_path)
    length_of_clip = clip.duration
    beginning_clip = rand.uniform(minimum_clip_size, length_of_clip)
    end_clip = length_of_clip + 1
    while(end_clip > length_of_clip):
        end_clip = beginning_clip + rand.randint(minimum_clip_size, max_clip_size)


    new_clip = clip.subclip(beginning_clip, end_clip)
    clips.append(new_clip)



final_clip = concatenate_videoclips(clips, method='compose')

final_clip.write_videofile("final.mp4")