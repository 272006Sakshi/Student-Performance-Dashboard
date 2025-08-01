# 🎓 Student Performance Dashboard

An interactive and visually engaging Streamlit web app to analyze and visualize student academic performance based on marks across five subjects. Designed to support educators, analysts, and students in understanding individual and group performance trends.

---

## 📌 Project Objective

To develop a responsive dashboard that:
- Accepts a CSV file of student marks.
- Computes total, average, and grade.
- Visualizes subject-wise averages and grade distributions.
- Highlights the topper and allows grade-based filtering.

---

## 📁 Dataset Overview

The dataset contains records of 100 students and includes:

| Column       | Description                     |
|--------------|----------------------------------|
| `StudentID`  | Unique student identifier        |
| `Name`       | Full name of the student         |
| `Math`       | Marks in Mathematics             |
| `Science`    | Marks in Science                 |
| `English`    | Marks in English                 |
| `History`    | Marks in History                 |
| `Computer`   | Marks in Computer Science        |

🎯 The app calculates:
- `Total`: Sum of all subject marks
- `Average`: Mean score
- `Grade`: A (90+), B (80–89), C (70–79), D (60–69), F (<60)

---

## 🛠️ Tech Stack

| Layer       | Tools Used                  |
|-------------|-----------------------------|
| 🖥 Frontend  | Streamlit                   |
| 🧠 Backend   | Python, Pandas              |
| 📊 Charts    | Plotly                      |
| 📁 Data      | CSV file (student marks)    |

---

## 📊 Features

- 📥 CSV file upload with real-time table preview
- 📈 Bar chart: Subject-wise average marks
- 🥧 Pie chart: Grade distribution
- 🏆 Topper highlight with total score
- 🎯 Grade-based student filtering
- 📎 Clean, responsive layout using Streamlit columns

---

## ⚙️ How to Run the App

### 1. Clone this Repository
```bash
git clone https://github.com/yourusername/student-performance-dashboard.git
cd student-performance-dashboard
