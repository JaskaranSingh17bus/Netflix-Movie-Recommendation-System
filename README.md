# 🎬 Netflix Movie Recommender System

An end-to-end Machine Learning web application that recommends movies based on user preferences using **Item-Based Collaborative Filtering**. 

---

## 📌 Project Overview
Most recommendation engines just display data in a Jupyter notebook. This project takes it a step further by building a functional user interface using **Streamlit** and processing large-scale user rating matrices efficiently using a Correlation Matrix pivot table. To ensure high-quality suggestions, a filter of a minimum of 100 ratings per movie was implemented.

## 🛠️ Tech Stack & Concepts Used
* **Language:** Python 3.12
* **Libraries:** Pandas, NumPy, Streamlit, Machine Learning (Pickle)
* **Core Algorithm:** Collaborative Filtering, Correlation Analysis (`corrwith()`)
* **Deployment:** Local Host / Ready for Streamlit Cloud

## 📁 Repository Structure
* `app.py`: The main Streamlit application script containing UI layout and recommendation logic.
* `main.py`: Core data exploration and processing script.
* `requirements.txt`: Dependencies required to run the web application.
* `moviemat.pkl` & `ratings_summary.pkl`: Serialized pivot tables and data states for lightning-fast query loading.

---

## 🏃‍♂️ How to Run Locally

1. Clone this repository:
git clone https://github.com/JaskaranSingh17bus/Netflix-Movie-Recommendation-System.git

2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
python -m streamlit run app.py
