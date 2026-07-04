from music21 import converter, instrument, note, chord
import glob
import pickle

notes = []

# Read both .mid and .midi files
midi_files = glob.glob("dataset/*.mid") + glob.glob("dataset/*.midi")

print(f"Found {len(midi_files)} MIDI files.\n")

for file in midi_files:
    print(f"Processing: {file}")

    try:
        midi = converter.parse(file)

        try:
            parts = instrument.partitionByInstrument(midi)

            if parts:
                notes_to_parse = parts.parts[0].recurse()
            else:
                notes_to_parse = midi.flat.notes

        except Exception:
            notes_to_parse = midi.flat.notes

        for element in notes_to_parse:

            if isinstance(element, note.Note):
                notes.append(str(element.pitch))

            elif isinstance(element, chord.Chord):
                notes.append(".".join(str(n) for n in element.normalOrder))

    except Exception as e:
        print(f"Skipped {file}")
        print(f"Reason: {e}\n")

print("\n--------------------------------")
print("Total Notes Extracted:", len(notes))
print("--------------------------------")

# Save extracted notes
with open("notes.pkl", "wb") as f:
    pickle.dump(notes, f)

print("\nnotes.pkl created successfully!")