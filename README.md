# air_guitar
<img src="https://img.shields.io/github/license/nilutpolkashyap/air_guitar?style=for-the-badge">&nbsp;<img src ="https://img.shields.io/github/languages/code-size/nilutpolkashyap/air_guitar?style=for-the-badge">

# Air Guitar using Mediapipe and OpenCV in Python

## About Project

This project is a gesture-based Air Guitar that can be played by people with the help of hand gestures. This project uses the Mediapipe library in python to get body pose estimation and then using pose estimation, the joint coordinates are extracted. We have used only x and y coordinates of body joints for this project. <br>
The user can play various guitar chords by changing the positions of their left hand to simulate guitar frets for playing different chords. The right hand can be used to do the swing motion to simulate the guitar swings for playing chords. The user can raise their left hand above their nose to change the chords from Major to Minor and vice versa. <br>
For playing the chord sound, Playsound library in Python is used.

## Software Used
- Python 3.x

## Libraries Used 
- playsound (Use pip install playsound==1.2.2 )
- mediapipe (pip install mediapipe)
- opencv (pip install opencv-python)

## Clone this Repository 
``` git clone https://github.com/nilutpolkashyap/air_guitar.git ```

## Run the Code
``` python air_guitar_main.py ```

## Output 
<div align="center">
<img  alt="Fusion360 Model" width="100%" src="https://gitlab.com/nilutpolkashyap/git_images/-/raw/main/air_guitar/mediapipe/mediapipe_output.png" />
</div>

## Output Video🎬 - https://youtu.be/vjEA95j5z_4


## Project Created by - 
- Nilutpol Kashyap - [nilutpolkashyap](https://github.com/nilutpolkashyap)
- Priyanka Kashyap - [thepriyankakashyap](https://github.com/thepriyankakashyap)

 Created as part of hackathon submission to [Do-Re-Mi Hacks 3](https://do-re-mi-hacks-3.devpost.com)

Hackathon Submission Link - [Air Guitar](https://devpost.com/software/air-guitar-bxi0ut)

Guitar Chords collected from 
 [https://sampleswap.org](https://sampleswap.org/filebrowser-new.php?d=INSTRUMENTS+%28MULTISAMPLED%29%2FGUITAR%2Fclean+electric+guitar+chords%2F)
