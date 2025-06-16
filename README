# NHL Beacon Goal Notifier

This project is a real-time NHL goal alert system built around a Raspberry Pi Zero 2 W. When your team scores (in this case, the Edmonton Oilers GO OIL!), the Pi triggers a beacon using a relay and GPIO output to simulate the goal light at real NHL games. The software continuously monitors the NHL live API and only activates during live games.

---

## 🛠️ Hardware Overview

* **Processor**: Raspberry Pi Zero 2 W
* **Power Supply**: 12V wall adapter
* **Voltage Regulation**: Off-the-shelf switching regulator drops 12V → 5V for the Pi and relay
* **Relay Control**: GPIO 5 triggers a relay to pass 12V to the beacon
* **Beacon Output**: Standard 12V beacon (external) connected via passthrough barrel jack
* **Enclosure**: Mounted in a black project box with the beacon decoupled for flexible mounting
* **Prototype Construction**: The circuit is built on prototype board and uses barrel jacks for input and output power management

---

## 📦 Software Overview

This repo consists of three Python modules:

### `main.py`

* Entry point for the script.
* Polls NHL API for upcoming games.
* Sleeps until the next game starts.
* When the game is live, continuously checks the current score.
* On a goal detection, activates GPIO 5 (relay) for 3 seconds.

### `ScheduleOBJ.py`

* Pulls the schedule for a specific NHL team using the unofficial NHL Stats API.
* Extracts game IDs and their scheduled start times.
* Converts all start times to local timezone.

### `GameOBJ.py`

* Uses a game ID to poll the `/boxscore` endpoint and check for score updates.
* Implements a basic scoring memory to detect if a new goal has occurred.

---

## 🚀 How to Deploy on Raspberry Pi

1. **Clone the repo or copy files to the Pi:**

   ```bash
   git clone https://github.com/your_username/nhl-beacon-notifier.git
   cd nhl-beacon-notifier
   ```

2. **Install dependencies:**

   ```bash
   sudo apt update
   sudo apt install python3-requests python3-rpi.gpio
   ```

3. **Run the script:**

   ```bash
   python3 main.py
   ```

---

## 💪 Development Notes

* If running on a PC for debug, comment out the GPIO lines in `main.py` and use the fallback print statements.
* The project uses the `boxscore` API instead of the full play-by-play feed for minimal polling delay and reduced bandwidth.
* A basic debounce mechanism is built-in to prevent false goal triggers.

---

## 📸 Hardware Snapshot

![Internal View](Images/Hardware.jpg)

---

## 🧠 Future Improvements

* Support multiple teams or game selection via command-line args
* Impliment mute button
* Add delay selector to help synchronize with watch party
* Convert to daemon service for auto-run at boot

---

## 📜 License

MIT License – idgaf.
