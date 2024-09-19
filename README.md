# Overview💟
This repo contains how we can plot the live graph of iot sensor readings live on cloud without any thirdparty intervention,which would reduce the **15second** delay in data plotting.
Which would be very useful for monitoring medical conditions using ecg sensor or other.
# Flow of work💟
i.Take ecg,ppg data with arduino and body temperature with esp32🩺

ii.Plot ecg,ppg data with python lib matplotlib,and take the body temperature in thingpeak🩺

iii.With flask and localtunnel host a website to show these graph plotting live , that can be accessed from anywhere in the world and live plotting can be seen.🩺

# Future plan with this project💟
Add heart disease prediction analysis in the website,which will come handy in case of emergency in remote zones of world.Already a arrhythmia detection repo is made.Also there are plans after the arrhythmia detection is merged in the website.

