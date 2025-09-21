# 🤖 AI Persona Architect

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An interactive web application built with Streamlit that uses machine learning to segment customers into distinct personas and suggests targeted marketing strategies.

This project is designed to showcase skills in data analysis, machine learning, and building user-friendly data applications. It takes raw customer data, performs clustering, and provides actionable business insights in a clean, interactive dashboard.

---

## ✨ Key Features

-   **📤 Dynamic Data Upload:** Upload any customer CSV file to start the analysis.
-   **📊 Interactive EDA:** Explore the data with interactive charts and visualizations powered by Plotly.
-   **🧠 AI-Powered Segmentation:** Uses K-Means clustering to automatically group customers into a specified number of personas.
-   **✏️ Custom Persona Naming:** Give meaningful names to each AI-generated persona.
-   **🚀 Actionable Strategies:** Get rule-based marketing strategy suggestions for each distinct persona.
-   **📥 Downloadable Results:** Download the final segmented data as a CSV for further use.

---

## 📸 Application Demo

![AI Persona Architect Dashboard](demo.png)
---

## 🛠️ Tech Stack

-   **Core Language:** Python
-   **Web Framework:** Streamlit
-   **Data Manipulation:** Pandas
-   **Machine Learning:** Scikit-learn
-   **Interactive Visualizations:** Plotly

---

## ⚙️ Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [your-repository-link]
    cd [your-repository-name]
    ```
    2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
    The application will open in your web browser.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.