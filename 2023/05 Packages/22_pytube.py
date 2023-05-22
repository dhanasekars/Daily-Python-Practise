""" 
Created on : 18/05/23 6:41 am
@author : ds  
"""

from pytube import YouTube


video_url = "https://www.youtube.com/watch?v=PWDQpEBq_pU"
yt = YouTube(video_url)

print(yt.views)

streams = yt.streams

stream = streams[0]
# print(stream)
# print(stream.resolution)
# print(stream.mime_type)
# print(stream.filesize)

title = yt.title
description = yt.description
duration = yt.length
view_count = yt.views
thumbnail_url = yt.thumbnail_url

# Print video metadata
print("Title:", title)
# print("Description:", description)
print("Duration (in seconds):", duration)
print("View Count:", view_count)
print("Thumbnail URL:", thumbnail_url)