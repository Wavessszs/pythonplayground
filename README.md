# Python Playground

A collection of Python projects, experiments, and small desktop utilities built while learning and exploring different areas of Python development.

The repository includes graphical applications, automation scripts, computer-vision experiments, and command-line programs. Projects vary in scope and maturity; some are prototypes or learning exercises rather than production-ready applications.

## Projects

### Desktop applications

- **Tkinter Kiosk** — A food-ordering kiosk interface with menu items, a shopping cart, order confirmation, and an order summary.
- **Personality Test** — An interactive Tkinter experience that combines questionnaire-style choices with a branching narrative.
- **FNAF Movement Simulation** — A Tkinter grid-based simulation that models randomized character movement between positions.

### Computer vision

- **Webcam Gesture System** — Uses OpenCV and MediaPipe Hands to track hand landmarks through a webcam. It detects when the index fingertip reaches one of the screen corners and displays the corresponding image.

### QR code utilities

- **QR Code Generator** — Creates a QR code image from a supplied text payload.
- **QR Code Reader** — Reads and decodes QR codes from an image using OpenCV and pyzbar.

### Small scripts and experiments

- **Borderlands Gun Generator** — Generates randomized weapon names using predefined factions, descriptors, and weapon-name components.
- **ASCII Decoder** — A terminal animation that randomly generates characters until it matches a target string.
- **Tkinter Login Interface** — A basic GUI experiment with username/password input and account creation.
- **Database Text Renamer** — A file-processing utility that removes specified SQL text fragments and standalone occurrences of a character using regular expressions.
- **Notepad Typing Automation** — Uses PyAutoGUI to open Notepad and type a predefined string.

## Technologies and libraries

- Python
- Tkinter
- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI
- qrcode
- pyzbar
- Standard library modules such as `random`, `time`, `json`, `os`, and `re`

Not every library is required for every project. Install dependencies based on the project you intend to run.

## Running a project

1. Clone the repository:

   ```bash
   git clone https://github.com/Wavessszs/pythonplayground.git
   cd pythonplayground
   ```

2. Install the dependencies required by the selected project. For example:

   ```bash
   pip install opencv-python mediapipe numpy qrcode pyzbar pyautogui
   ```

3. Run a Python script from its directory. For example:

   ```bash
   python fnaf.py
   ```

Some projects require additional setup:
- Webcam projects need a working camera and compatible OpenCV/MediaPipe installations.
- Tkinter applications require a Python installation with Tk support.
- The QR code reader may require the ZBar library in addition to the Python package.
- PyAutoGUI scripts interact with the desktop and should be run only when you understand the actions they perform.

## Notes

- This repository is a collection of independent projects, not one integrated application.
- Some scripts contain hardcoded example values or depend on local files and resources.
- Review each project's code and dependencies before running it.
- Contributions and improvements may be added as the projects are revisited.

## License

See [LICENSE](LICENSE).
