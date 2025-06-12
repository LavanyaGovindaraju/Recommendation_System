#  🛍️ Recommendation System and Price Prediction

A data-driven system designed to recommend product bundles using collaborative filtering and predict product prices through regression modeling. The solution is designed for integration into e-commerce or retail platforms, supporting both API-based access and standalone batch predictions.
---

## 📦 Features

- **Personalized Product Bundling** using collaborative filtering (user-based and item-based)
- **Dynamic Price Prediction** for unit prices using regression models
- **Flask-based API** for serving recommendations and bundle pricing
- **Docker Support** for easy deployment
- **Interactive CLI Interface** for testing and configuration
- **Extensible Codebase** for experimenting with rule-based, statistical, or ML approaches

---

## Setup

1. **Create a Virtual Environment**
   - Install Python 3.8 if you haven't already.
   - Open a terminal or command prompt.
   - Navigate to your project directory.
   - Create a virtual environment named `venv`:
     ```
     python3.8 -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```

2. **Install Dependencies**
   - Once inside the virtual environment, install the required libraries using `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```
     
3. **Prepare the Data**
   - Extract the data zip file into the `data` folder:
     ```
     unzip data/data.zip -d data/
     ```

4. **Run the Flask  API Server**
   - Start the Flask application to serve bundles through the API endpoint:
     ```
     python app.py

     ```

5. **Using Docker**:
   - Alternatively, you can use Docker to containerize the Flask application:
     - Make sure you have Docker installed on your system.
     - Build the Docker image:
       ```
       docker build -t bundle-api .
       ```
     - Run the Docker container:
       ```
       docker run -p 5000:5000 bundle-api
       ```

## 🚀 How to Use

You can interact with the system either via the command line or by using the built-in API.
---

Run the `main.py` script with the following command-line arguments:

`--collab_filter`: Specify the type of collaborative filtering to use. Choose between 'user' for user-based collaborative filtering and 'item' for item-based collaborative filtering. Default is 'item'.

`--user_id`: (Optional) User ID for user-based collaborative filtering.

`--item_id`: (Optional) Item ID for item-based collaborative filtering.

```
python main.py --collab_filter item --item_id 22733
                     
                     or

python main.py --collab_filter user --user_id 17850.0

```

- The Flask application exposes an endpoint `/get_bundle` that takes a product ID as a parameter and returns a list of products in the bundle along with the total bundle price.
- You can access the API endpoint using the ngrok URL provided when running the Flask application or via `http://localhost:5000/get_bundle?product_id=<product_id>` when running Docker.

### Note:
Make sure to replace `<product_id>` with the actual product ID you want to query. The endpoint will return a JSON response containing the bundle of products and the total bundle price.


### 📈 Solution Design & Rationale

---

### 🧠 Recommendation Strategy

A machine learning–based collaborative filtering approach is used to model user–product interactions. This allows for:

- Capturing complex patterns in user behavior  
- Scaling with data volume  
- Automatically adapting to product trends  

> **Note:** The current implementation uses **K-Nearest Neighbors (KNN)** due to its interpretability and simplicity.

---

### 📊 Data Splitting Strategy

The current system uses a **random train–test split**, which ensures diverse evaluation samples.

Alternative strategies to consider:

- **Time-based split**: Useful for temporal datasets where real-time generalization is critical  
- **User segments**: Enables A/B testing across user demographics  
- **Product categories**: Helps validate performance within subdomains of the catalog  

---

### 🛒 Bundle Size Logic

The number of items in each recommended bundle can be tuned based on:

- **Business goals**: Revenue vs. user satisfaction  
- **User preferences**: Short vs. long recommendation lists  
- **Model metrics**: Precision, recall, and diversity  
- **A/B testing outcomes**: Click-through rate and conversion insights  

> **Default setting**: Recommends **10 products** per bundle

---

### 💰 Bundle Price Calculation

Bundle price is calculated by summing the **unit prices** of all products in the recommendation list.

> **Note:** This logic can be extended to incorporate:
> - Discount rules
> - Price thresholds
> - Promotional pricing schemes

---

### 📊 Business Evaluation

To measure and communicate the impact of this system:

1. **Define KPIs**: e.g., conversion rate, cart size, revenue uplift  
2. **Establish Baseline**: Compare with prior recommendation systems or manual bundling  
3. **Run A/B Tests**: Benchmark model-enabled recommendations against a control group  
4. **Analyze Results**:
   - Visual performance reports
   - Case studies of successful bundles
   - Metric comparisons (e.g., +x% revenue)

> **Current Result**: Model achieved an **RMSE of 0.0033** for price prediction during training

---

### 🔍 Price Prediction Details

The regression model estimates **unit prices** based on existing features.

To improve this capability, the following additional data would be beneficial:

- **Product metadata**: Category, brand, dimensions  
- **Market data**: Trends, competitor pricing  
- **User behavior**: Purchase history, segments  
- **Temporal features**: Seasonality, discounts, or promotions  








