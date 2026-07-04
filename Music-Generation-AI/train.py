import pickle
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dropout, Dense
from tensorflow.keras.utils import to_categorical

# ----------------------------
# Load notes
# ----------------------------
with open("notes.pkl", "rb") as f:
    notes = pickle.load(f)

# Use only first 10,000 notes for faster training
notes = notes[:10000]

print("Total Notes Used:", len(notes))

# ----------------------------
# Create vocabulary
# ----------------------------
pitchnames = sorted(set(notes))

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

sequence_length = 100

network_input = []
network_output = []

for i in range(len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in sequence_in])
    network_output.append(note_to_int[sequence_out])

n_patterns = len(network_input)

print("Training Patterns:", n_patterns)

# ----------------------------
# Reshape input
# ----------------------------
network_input = np.reshape(
    network_input,
    (n_patterns, sequence_length, 1)
)

network_input = network_input / float(len(pitchnames))

network_output = to_categorical(network_output)

# ----------------------------
# Build LSTM Model
# ----------------------------
model = Sequential()

model.add(
    LSTM(
        256,
        input_shape=(network_input.shape[1], network_input.shape[2]),
        return_sequences=True
    )
)

model.add(Dropout(0.3))

model.add(LSTM(256))

model.add(Dense(128, activation="relu"))

model.add(Dropout(0.3))

model.add(Dense(len(pitchnames), activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam"
)

# ----------------------------
# Train Model
# ----------------------------
print("\nTraining Started...\n")

model.fit(
    network_input,
    network_output,
    epochs=5,
    batch_size=64
)

# ----------------------------
# Save Model
# ----------------------------
model.save("music_model.keras")

print("\nTraining Completed Successfully!")
print("Model saved as music_model.keras")