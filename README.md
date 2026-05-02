# Python Study Projects

This repository contains small Python study projects and practice apps. Each folder is a self-contained exercise in solving a problem, building a simple UI, interacting with websites or APIs, or creating a small desktop/web app.

---

## Project Categories

### Games

| Project | Description | Technologies |
|---------|-------------|--------------|
| [Snake Game](./snake_game/) | Classic Snake arcade game with score tracking and persistent high score | `turtle` |
| [Pong Game](./pong_game/) | Two-player Pong with collision detection and scoring | `turtle` |
| [Turtle Crossing](./turtle_crossing/) | Frogger-style obstacle avoidance game with increasing difficulty | `turtle` |
| [Turtle Race](./turtle_race.py) | Randomized turtle racing simulation with user betting | `turtle` |
| [US State Guessing Game](./us_state/) | Geography quiz to place all 50 states on a blank map | `turtle`, `pandas` |
| [Quizzler App](./quizzler-app/) | Multiple-choice quiz app using trivia API data | `tkinter`, Open Trivia API |

---

### GUI Applications

| Project | Description | Technologies |
|---------|-------------|--------------|
| [Password Manager](./password-manager/) | Password generator and storage helper with search and clipboard support | `tkinter`, `pyperclip`, `json` |
| [Flash Card](./flash%20card/) | French vocabulary flashcard app with auto-flip and progress tracking | `tkinter`, `pandas` |
| [Pomodoro Timer](./pomodoro/) | Study timer implementing the Pomodoro technique with work/break cycles | `tkinter` |

---

### Automation & Bots

| Project | Description | Technologies |
|---------|-------------|--------------|
| [Gym Auto Booking](./gym_auto_booking/) | Selenium bot that books gym classes automatically and retries waitlists | `selenium` |
| [Twitter Complain Bot](./twitter_complain_bot/) | Internet speed check and Twitter complaint poster | `selenium` |
| [Birthday Wisher](./Birthday%20Wisher/) | Automatically sends birthday emails to contacts from a CSV file | `smtplib`, `pandas` |
| [Bot Automation](./bot/) | Selenium practice script for automating web interactions and searching Wikipedia | `selenium` |

---

### Web & API Projects

| Project | Description | Technologies |
|---------|-------------|--------------|
| [Flight Deals](./flight-deals/) | Finds cheap flights and records results to a Google Sheet | `requests`, Kiwi.com API, Google Sheets API |
| [Stock News](./stock%20news/) | Monitors stock price swings and sends news alert notifications | `requests`, Alpha Vantage, NewsAPI, Twilio |
| [Rain Alert](./rain_alert/) | Weather forecast checker that warns if rain is expected | `requests`, OpenWeatherMap API |
| [ISS Overhead](./issoverhead/) | Email alert when the ISS passes overhead at night | `requests`, `smtplib` |
| [Amazon Price Tracker](./amazon_price_tracker/) | Scrapes Amazon product pages and notifies when the price drops | `requests`, `BeautifulSoup`, `smtplib` |
| [Habit Tracker](./habit-tracker/) | Tracks daily habits with Pixela API graphing | `requests`, Pixela API |
| [Hello Flask](./hello_flask/) | Flask web app examples, including a number guessing game | `Flask` |

---

### Data & Scripting

| Project | Description | Technologies |
|---------|-------------|--------------|
| [CSV Read/Write](./csv_read_write/) | Reads and processes CSV datasets like weather and squirrel census data | `pandas`, `numpy` |
| [NATO Alphabet](./NATO%20alphabet/) | Converts text to NATO phonetic alphabet code words | `pandas` |

---

### Study Scripts & Experiments

| File | Description |
|------|-------------|
| [`beatiful_soup.py`](./beatiful_soup.py) | BeautifulSoup web scraping examples |
| [`turle_draw.py`](./turle_draw.py) | Turtle graphics drawing with keyboard control |
| [`turtle_race.py`](./turtle_race.py) | Simple turtle race simulation |
| [`Other_Tkinter_Widgets.py`](./Other_Tkinter_Widgets.py) | Tkinter widget experiments and examples |
| [`main.py`](./main.py) | General Python practice script |
| [`pandas_study.py`](./pandas_study.py) | Pandas learning and data manipulation examples |

---

## Notes

- `coverage/` contains coverage analysis outputs and is not a standalone app.
- Some projects require API keys, email credentials, or web driver setup. Inspect the project `main.py` or folder files for configuration details.

---

## Tech Stack

- GUI: `tkinter`, `turtle`
- Web scraping: `BeautifulSoup`, `requests`, `selenium`
- Data: `pandas`, `numpy`
- APIs: OpenWeatherMap, Alpha Vantage, NewsAPI, Kiwi.com, Google Sheets, Twilio, Pixela, Open Trivia
- Email / notifications: `smtplib`, Twilio SMS
- Web: `Flask`

---

## Setup

Most projects use environment variables or a `config.py` for credentials. Check each project before running.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # if present, otherwise install needed packages manually
```
