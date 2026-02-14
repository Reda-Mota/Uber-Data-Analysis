# 🚖 Uber Ride Analysis Project

### 📊 Business Intelligence & Data Science Case Study

**Author:** Reda El Motassadiq  
**Role:** Data Analyst & Future AI Engineer  
**Tools:** Python, Pandas, Matplotlib, Seaborn

---

## 📝 Executive Summary
This project analyzes a dataset of **Uber ride bookings** to uncover patterns in urban mobility, revenue generation, and operational efficiency. By leveraging Python's data science stack, the analysis transforms raw booking logs into actionable business insights regarding peak hours, cancellation reasons, and high-demand locations.

## 🎯 Key Objectives
1.  **Revenue Optimization:** Identify the most profitable vehicle types.
2.  **Demand Forecasting:** Pinpoint "Rush Hours" to optimize driver allocation.
3.  **Operational Health:** Diagnose the root causes of driver cancellations.
4.  **Geospatial Analysis:** Map out the top pickup zones and "Golden Routes."

---

## 🛠️ Technical Approach & Methodology

### 1. Data Cleaning & Preprocessing
* **Handling Missing Values:** Imputed nulls in `Booking Value` and `Ride Distance`.
* **Type Conversion:** Converted object columns to numeric and datetime formats for calculation.
* **Text Processing:** Cleaned string columns (removed quotes/whitespace) using `str.strip()`.

### 2. Feature Engineering
* **`Booking_Timestamp`:** Merged Date and Time columns for temporal analysis.
* **`Route`:** Created a new feature combining Origin → Destination to track specific travel paths.
* **`Price_Per_KM`:** Calculated a custom efficiency metric (`Booking Value` / `Ride Distance`).

---

## 📈 Key Insights & Findings

| Category | Insight | Business Implication |
| :--- | :--- | :--- |
| **💰 Top Revenue** | **Auto (Rickshaw)** generates the highest total revenue. | Strategy should focus on supporting the mass market (Auto) rather than just luxury segments. |
| **⏰ Peak Time** | **18:00 (6 PM)** is the absolute peak hour. | Implement surge pricing or driver incentives during the evening commute window. |
| **🚫 Cancellation** | **"Customer coughing/sick"** is a top reason for driver cancellation. | Drivers prioritize health safety; the platform may need better health protocols. |
| **📍 Hotspots** | Demand is highly concentrated in specific **Commercial & Transit Hubs**. | Driver positioning should be proactive in these zones before peak hours. |

---

## 💻 How to Run This Project
1.  Clone the repository:
    ```bash
    git clone [https://github.com/Reda-Mota/Uber-Ride-Analysis.git](https://github.com/Reda-Mota/Uber-Ride-Analysis.git)
    ```
2.  Install required libraries:
    ```bash
    pip install pandas matplotlib seaborn
    ```
3.  Open the Jupyter Notebook:
    ```bash
    jupyter notebook Uber_Analysis.ipynb
    ```

---

## 📬 Contact
If you have any questions or suggestions, feel free to reach out:
* **GitHub:** [RedaElMotassadiq](https://github.com/Reda-Mota)
* **Email:** [redamota03@gmail.com]

> *"Data is not just numbers; it's a story waiting to be told."*
