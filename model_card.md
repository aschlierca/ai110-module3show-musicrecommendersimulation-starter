# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

## VibeFinder 1.0

## 2. Intended Use

VibeFinder recommends songs from a small catalog based on a user’s preferred genre, mood, and energy level. It was created for classroom learning to demonstrate how content-based recommendation systems work, not for real music apps.
Prompts:

---

## 3. How the Model Works

The system compares each song’s genre, mood, and energy to the user’s preferences. Genre matches give 2 points, mood matches give 1 point, and up to 1 point is added for energy similarity, then the top 5 songs are recommended.

---

## 4. Data

Describe the dataset the model uses.

The dataset contains 10 songs in a CSV file with genres like pop, lofi, rock, ambient, jazz, synthwave, and indie pop. Many major genres such as hip hop, R&B, classical, and country are missing, which limits recommendation variety.

---

## 5. Strengths

The model works well when the user’s preferences match songs in the dataset. For example, pop/happy ranked Sunrise City first and rock/intense ranked Storm Runner first with scores near 4.

---

## 6. Limitations and Bias

Genre is weighted more heavily than other features, so songs with the same genre usually rank highest even if mood or energy differ. The small dataset also reduces variety, especially for genres with only one song.

---

## 7. Evaluation

Testing showed the pop/happy profile ranked Golden Horizon first with a score of about 3.98, while the rock/intense profile ranked Thunder Road first with a score near 3.99. The ambient/chill high-energy edge case ranked Starlight Drift first, but it had a low energy similarity of around 0.38, showing the system struggles when energy preferences do not match the genre well.

---

## 8. Future Work

Future improvements include adding 50+ songs from more genres like hip hop and R&B. The model could also add collaborative filtering and features like danceability and valence.

---

## 9. Personal Reflection

This project showed that even a simple scoring system can produce reasonable recommendations with clear preferences. Real platforms like Spotify likely perform better because they learn from user listening behavior rather than only stated preferences.
