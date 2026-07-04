# 🎵 Music Generation with AI

## Objective
This project generates new music using an LSTM-based Recurrent Neural Network trained on MIDI files.

## Features
- Reads MIDI dataset
- Extracts musical notes using music21
- Trains an LSTM neural network
- Generates new note sequences
- Converts generated notes into a playable MIDI file

## Technologies
- Python
- TensorFlow / Keras
- music21
- NumPy

## Project Structure

music-generation-ai/
│── dataset/
│── preprocess.py
│── train.py
│── generate.py
│── convert.py
│── requirements.txt
│── notes.pkl
│── generated_notes.pkl
│── music_model.keras
│── generated_music.mid

## How to Run

pip install -r requirements.txt

python preprocess.py

python train.py

python generate.py

python convert.py

## Output

generated_music.mid

## Author

Amber Kumar Tiwary