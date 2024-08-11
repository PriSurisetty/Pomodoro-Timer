# Pomodoro Study Timer

This is a simple Pomodoro timer application built with Python and Tkinter. It helps users manage their study sessions by following the Pomodoro Technique, which alternates between work periods and short breaks.



[!Watch the video](https://github.com/user-attachments/assets/e06de5bb-5e10-4228-98da-d558e66f5a91)

**Note**: The video is sped up, but the timer accurately shows the real-time duration in seconds/minutes.


## Features

- **Work Sessions**: Focused 25-minute work sessions.
- **Short Breaks**: 5-minute breaks after each work session.
- **Long Breaks**: 20-minute breaks after every four work sessions.
- **Visual Timer**: Displays a countdown timer to keep track of work and break times.
- **Progress Tracking**: Uses checkmarks to track the number of completed work sessions.

## Usage

1. **Start the Timer**: Click the "Start" button to begin a work session.
2. **Work and Break**: The app will automatically switch between work and break periods. The label at the top will indicate whether it's time to "Work" or "Break."
3. **Reset the Timer**: If you need to stop and reset the timer, click the "Reset" button. This will clear the current timer and reset your progress.

## Project Structure

- **main.py**: The main script containing the Pomodoro timer logic and user interface.
- **tomato.png**: Image used for the visual representation of the timer.

## Installation

To run the Pomodoro Study Timer on your machine:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/pomodoro-timer.git

2. **Navigate to the project directory**:
   ```bash
   cd pomodoro-timer
4. **Ensure you have Python installed. You can run the program with the following command**:
   ```bash
   python main.py
  
## How It Works:

- **Timer Mechanism**: The timer alternates between work sessions and breaks. After 4 work sessions, a longer break is triggered.
- **Countdown Function**: The countdown function updates the timer every second and automatically transitions between work and break periods.
- **UI Setup**: The Tkinter library is used to create the graphical user interface, with a canvas to display the timer and buttons to control the application.


