"""Play a small repertoire of melodies from the command line.

Usage: python example.py "Happy Birthday"
"""

import math
import os
import struct
import subprocess
import sys
import tempfile
import wave


SONGS = {
	"Moonlight Sonata": [("C#4", .5), ("G#3", .5), ("C#4", .5), ("E4", .5),
						  ("G#4", .5), ("C#4", .5), ("G#3", .5), ("C#4", .5)] * 2,
	"Eine Kleine Nachtmusik": [("G4", .35), ("G4", .35), ("D5", .35), ("B4", .35),
								("G4", .35), ("D5", .35), ("B4", .35), ("G4", .7)],
	"Happy Birthday": [("G4", .3), ("G4", .15), ("A4", .5), ("G4", .5), ("C5", .5),
						("B4", .9), ("G4", .3), ("G4", .15), ("A4", .5), ("G4", .5),
						("D5", .5), ("C5", .9)],
	"Jingle Bells": [("E4", .35), ("E4", .35), ("E4", .7), ("E4", .35), ("E4", .35),
					  ("E4", .7), ("E4", .35), ("G4", .35), ("C4", .5), ("D4", .5),
					  ("E4", 1.0)],
}

NOTE_NAMES = {name: i for i, name in enumerate(("C", "C#", "D", "D#", "E", "F",
												  "F#", "G", "G#", "A", "A#", "B"))}


def frequency(note):
	if note == "R":
		return 0
	name, octave = note[:-1], int(note[-1])
	return 440 * 2 ** ((NOTE_NAMES[name] + (octave + 1) * 12 - 69) / 12)


def play(song):
	rate = 44100
	samples = bytearray()
	for note, seconds in song:
		count = int(rate * seconds)
		freq = frequency(note)
		for i in range(count):
			value = 0 if not freq else int(12000 * math.sin(2 * math.pi * freq * i / rate))
			samples.extend(struct.pack("<h", value))
	with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as output:
		path = output.name
	try:
		with wave.open(path, "wb") as wav:
			wav.setnchannels(1)
			wav.setsampwidth(2)
			wav.setframerate(rate)
			wav.writeframes(samples)
		if sys.platform == "darwin":
			subprocess.run(["afplay", path], check=True)
		elif os.name == "nt":
			import winsound
			winsound.PlaySound(path, winsound.SND_FILENAME)
		else:
			subprocess.run(["aplay", "-q", path], check=True)
	finally:
		os.unlink(path)


if __name__ == "__main__":
	title = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else None
	if title not in SONGS:
		print("Choose a song:")
		for number, name in enumerate(SONGS, 1):
			print(f"{number}. {name}")
		choice = input("Selection: ").strip()
		title = list(SONGS)[int(choice) - 1]
	print(f"Playing {title}...")
	play(SONGS[title])
