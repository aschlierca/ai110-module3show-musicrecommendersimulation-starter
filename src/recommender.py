from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        return "Explanation placeholder"


def load_songs(csv_path: str) -> List[Dict]:
    """Reads a CSV file of songs and converts fields into the correct data types."""
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)

    print(f"Total songs loaded: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculates how well a song fits user preferences and returns a score with explanations."""
    score = 0.0
    reasons = []

    if song['genre'].lower() == user_prefs.get('genre', '').lower():
        score += 2.0
        reasons.append("genre matched (+2.0)")

    if song['mood'].lower() == user_prefs.get('mood', '').lower():
        score += 1.0
        reasons.append("mood matched (+1.0)")

    energy_diff = abs(song['energy'] - user_prefs.get('energy', 0.5))
    energy_score = round(1.0 - energy_diff, 2)

    score += energy_score
    reasons.append(f"energy similarity (+{energy_score})")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Evaluates all songs and returns the top k highest scoring recommendations."""
    scored = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored.append((song, score, explanation))

    scored = sorted(scored, key=lambda x: x[1], reverse=True)

    return scored[:k]