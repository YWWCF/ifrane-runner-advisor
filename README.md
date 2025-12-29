# 🏃‍♂️ Ifrane Runner Advisor

A specialized, weather-driven gear advisor designed for high-altitude runners training in the unique climate of Ifrane, Morocco.

## 🎯 The Problem
Training for a semi-marathon in Ifrane (1,665m) presents a constant challenge: "What should I wear today?". Drastic temperature shifts and high-altitude winds make choosing gear difficult. I built this program to solve my own daily dilemma and help fellow runners at Al Akhawayn University (AUI) optimize their performance through better gear selection.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **API:** [OpenWeatherMap](https://openweathermap.org/api)
* **Security:** `python-dotenv` for Environment Variable Management
* **Libraries:** `requests`

## 🚀 Features
* **Hyper-Local Data:** Uses precise GPS coordinates for the Ifrane/AUI campus to ensure accuracy.
* **Scientific Recommendations:** Implements the "10-degree rule" (dressing for 10 degrees warmer than the actual temp) to suggest the most efficient gear.
* **Security-First:** Built using professional standards where private API keys are kept hidden from the source code.
* **Error Resilience:** Gracefully handles connection failures or invalid API requests without crashing.

## 📦 Setup & Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YWWCF/ifrane-runner-advisor.git
   ```
2. **Install dependencies:**

```Bash  
pip install requests python-dotenv
```

3. **Configure Environment Variables:**

1.Create a file named .env in the root directory.

2.Add your OpenWeatherMap API key to the file:
```Bash
  openweather_api_key=your_actual_api_key_here
```
  

4. **Simply run the script via your terminal:**

```Bash
python runner_advisor.py
```

__________________________________________________________________________________________
**👨‍💻 About the Developer:**

Youssef Mouddou is a Computer Science Freshman at Al Akhawayn University in Ifrane. This project is part of my journey to master Python and secure API integration early in my academic career.

Current Focus: Building software solutions for real-world problems.

Personal Goal: Training for the 2026 Marrakech Semi-Marathon! 🏃‍♂️
