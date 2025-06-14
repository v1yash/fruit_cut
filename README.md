🍉 Fruit Cutter Game
A fast-paced and fun fruit-slicing game built using Python and Pygame. Slice fruits as they fly into the air, earn points based on their size, and aim for the high score before time runs out!

🚀 Features
Multiple fruits (Apple, Banana, Watermelon, Pineapple) with unique images and slice animations

Mouse-based slicing mechanism

Three difficulty modes: Simple, Medium, and Hard

Time selection: 1 min, 2 min, 3 min

Real-time scoreboard and high score tracking per mode (saved permanently)

Smooth animations and clean UI

🎮 How to Play
Select a difficulty mode and time using the buttons on screen.

Slice fruits by clicking and dragging across them.

Points are awarded based on fruit size:

Small: 15 pts

Medium: 10 pts

Large: 5 pts

Try to beat the high score before the timer ends!

🕹️ Controls
Mouse Click + Drag – Slice fruits

Click Buttons – Select mode and timer

📦 Requirements
Python 3.x

Pygame
Install with:

bash
Copy code
pip install pygame
📁 Project Structure
bash
Copy code
main.py                # Main game loop
fruit.py               # Fruit class and image loading
high_scores.txt        # (Deprecated, replaced by mode-based score files)
scores_simple.txt      # High score for Simple mode
scores_medium.txt      # High score for Medium mode
scores_hard.txt        # High score for Hard mode
/assets/
    apple.png
    apple_half1.png
    apple_half2.png
    banana.png
    banana_half1.png
    banana_half2.png
    watermelon.png
    watermelon_half1.png
    watermelon_half2.png
    pineapple.png
    pineapple_half1.png
    pineapple_half2.png
▶️ Running the Game
Make sure your terminal is inside the project folder and all fruit images are placed inside an assets/ directory. Then run:

bash
Copy code
python main.py
🔒 High Score Tracking
High scores are saved permanently in files:

scores_simple.txt

scores_medium.txt

scores_hard.txt

Each mode tracks its own top score across game sessions.

🧑‍💻 Author
Developed by Yash Vaghasiya
