import pickle
import random
import numpy as np

from tensorflow.keras.models import load_model

# Load trained model
model = load_model("music_model.keras")

# Load notes
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Use same subset as training
notes = notes[:10000]

pitchnames = sorted(set(notes))

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

sequence_length = 100

network_input = []

for i in range(len(notes) - sequence_length):
    sequence = notes[i:i + sequence_length]
    network_input.append([note_to_int[n] for n in sequence])

start = random.randint(0, len(network_input) - 1)

pattern = network_input[start]

prediction_output = []

print("Generating Music...\n")

for note_index in range(300):

    prediction_input = np.reshape(pattern, (1, len(pattern), 1))
    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(prediction_input, verbose=0)

    index = np.argmax(prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(index)
    pattern = pattern[1:]

print("\nGenerated Notes:\n")

print(prediction_output)

# Save generated notes
with open("generated_notes.pkl", "wb") as f:
    pickle.dump(prediction_output, f)

print("\nGenerated notes saved as generated_notes.pkl")