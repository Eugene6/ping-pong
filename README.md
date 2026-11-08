# 🏓 Online Ping Pong

Welcome to the definitive, fully functional 2D online multiplayer Ping Pong game! Powered by Python and Pygame, this project features a polished local network setup, allowing two players to jump into action instantly.

---

## 🔧 Features

* ✅ Complete server and client (player) setup.
* ✅ Ball and paddle physics.
* ✅ Win condition set at 10 points.
* ✅ Waiting room system for the second player.
* ✅ Collision events (for sound effects).

---

## 🛠️ Tech Stack

* **Language:** Python
* **Core Library:** Pygame
* **Data Protocol:** JSON-based state sync over sockets

---

## 🚀 How to Run the Project

### 1. Download the Project
You can clone the repository using Git (replace with your repository link if needed):
```bash
git clone https://github.com/Eugene6/ping-pong.git
```

### 2. Start the Server
Open `server.py` and run it:
```bash
python server.py
```

### 3. Launch the Clients (Run 2 Times)
Open two separate terminal windows (on the same computer or on different computers across the network) and run `client.py`:
```bash
python client.py
```

⚠️ **Important:** All files must be located in the same folder. The server should only be launched **once**, while `client.py` must be run separately for each of the two players.

---

## 🛠️ How It Works

### Server (`server.py`)
* Waits for **two players** to connect.
* Manages the core game loop: moves the ball, handles collisions, and broadcasts the current **game state**.
* Receives control commands (`UP`, `DOWN`) from the players.

### Client (`client.py`)
* Establishes a connection to the server.
* Renders the game screen, paddles, ball, and real-time score.
* Sends keyboard inputs (`W` / `S`) directly to the server.

---

🏆 **Good luck!**
