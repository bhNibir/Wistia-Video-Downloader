import requests
import m3u8
import subprocess
from tqdm import tqdm
import os


url     = input("URL: ")
name    = input("Give Your File Name: ")

## FILE AND FOLDER MANGE

if not os.path.exists("video"):
    os.mkdir("video")

BASE_DIR    = os.getcwd()
VIDEO_DIR   = os.path.join(BASE_DIR, "video")
file_ts     = os.path.join(VIDEO_DIR, f'{name}.ts')
file_mp4    = os.path.join(VIDEO_DIR, f'{name}.mp4')
ffmpeg_dir    = os.path.join(BASE_DIR, "ffmpeg","bin","ffmpeg.exe")



## DOWNLOAD LOADING TS FILE

r = requests.get(url)
m3u8_master = m3u8.loads(r.text)
segments = m3u8_master.data['segments']
persent = len(segments)



with open(file_ts, 'wb') as f:

    for segment in tqdm(segments):
        uri = segment['uri']
        r = requests.get("https://embedwistia-a.akamaihd.net"+uri)
        f.write(r.content)

        
##CONVERT TS TO MP4 FORMET
import ffmpy

ff = ffmpy.FFmpeg(
    executable=ffmpeg_dir,
    inputs={ file_ts: None},
    outputs={file_mp4: None}
)
ff.cmd
ff.run()    

os.remove(file_ts)
print("Download Complete ... ")

