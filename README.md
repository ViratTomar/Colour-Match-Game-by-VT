# 🎨 Color Match Game (Python + Pygame)

A fast-reaction colour matching game built with [Pygame](https://www.pygame.org/).  
You’re shown a **large colour swatch at the top** and a **grid of coloured tiles below**.  
Your task is to **click the tile that matches the target colour** as quickly as possible.  
The game tracks your **score, reaction time, best time, average time and accuracy**.

---

## 📸 Features

- **Clear UI** – Target colour swatch with centered text at the top.
- **4×4 grid of tiles** – Each round randomly generates colours.
- **Performance tracking** – Best time, average time and accuracy shown live.
- **Penalty for mistakes** – Wrong clicks reduce your score.
- **Keyboard controls** – Press `R` to reset stats, `ESC` to quit.

---

## 🚀 Installation

1. Make sure you have **Python 3.8+** installed.  
2. Install [Pygame](https://pypi.org/project/pygame/):

   ```bash
   pip install pygame
Download or clone this repository.

Run the game:

bash
Copy code
python color_match_game.py

🕹️ How to Play

At the top of the window you’ll see a large colour swatch labelled “TARGET COLOR.”

Below it is a grid of 16 coloured squares.

Click the tile whose colour matches the target swatch as fast as possible.

The game will immediately show a new target colour and reshuffle the grid.

The stats panel shows:

Score – increases with correct clicks, decreases with wrong clicks.

Best Time – your fastest reaction time.

Average Time – rolling average of your last 10 reactions.

Accuracy – % of correct clicks over total attempts.

Press R at any time to reset your stats.

Press ESC or close the window to quit.

⚙️ Customisation
You can easily tweak the following in color_match_game.py:

Variable	Purpose	Default
grid_rows / grid_cols	Size of the grid	4×4
tile_size	Width/height of each tile	110 px
color_list	List of available colours (RGB tuples)	8 colours
font_big / font_small	Fonts for title and stats	SysFont(None, 48 / 28)

Examples:

python
Copy code
grid_rows, grid_cols = 5, 5  # 5x5 grid
tile_size = 90               # slightly smaller tiles
You can also add new colours to color_list:

python
Copy code
color_list.append((139,69,19))  # Brown

📝 Controls

Action	Key / Mouse
Click a colour tile	Left Mouse Button
Reset stats	R key
Quit game	ESC key or close window

🧩 Roadmap / Ideas
Countdown timer or per-round time limit.

Sound effects and animations for correct/incorrect clicks.

Leaderboard with saved high scores.

Difficulty levels (hide colour names, reduce time window).

Pull requests welcome!

📄 License
MIT License. You’re free to use, modify, and distribute this game.

Enjoy playing and improving your reaction time! 🎉
