import pickle
from music21 import stream, note, chord, instrument

# Load generated notes
with open("generated_notes.pkl", "rb") as f:
    prediction_output = pickle.load(f)

offset = 0
output_notes = []

for pattern in prediction_output:

    # Chord
    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")
        notes = []

        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            notes.append(new_note)

        new_chord = chord.Chord(notes)
        new_chord.offset = offset
        output_notes.append(new_chord)

    # Single Note
    else:
        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()
        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)

midi_stream.write("midi", fp="generated_music.mid")

print("✅ Music generated successfully!")
print("✅ File saved as generated_music.mid")