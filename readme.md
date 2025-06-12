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

🚀 How to Use
Launch the system from the command line to run the recommendation and price prediction logic:

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


## Analysis of the Given Task

### Implement a solution of your choice for recommending product bundles e.g. rule-based, statistics, or ML-based solution. Please describe any reasoning behind your solution.

For recommending product bundles, an ML-based solution is highly effective due to its ability to learn from historical data and make predictions based on patterns it identifies. This approach can capture complex relationships between products that might not be apparent through rule-based or statistical methods alone.

#### Reasoning:

* Personalization: ML models can learn user preferences over time, recommending bundles that are more likely to be of interest to individual users.

* Scalability: As the dataset grows, the model can adapt to new products and user behaviors without manual intervention.

* Efficiency: By leveraging machine learning algorithms, the system can efficiently process large volumes of data to identify optimal bundles.

#### Note: Additionally, my prior experience includes working with ML algorithms such as KNN. Given the available resources, I chose to utilize this method.

### Provide a splitting to train and test datasets. Discuss possible different splitting criteria. What other splitting criteria would you choose if you could gather more features/data?

#### Splitting Criteria:

1. Random Split: A common approach where the dataset is randomly divided into training and testing sets. This ensures that the model is tested on unseen data.

2. Time-based Split: If the data includes timestamps, splitting the dataset based on time can help the model learn from past data and test its performance on more recent data.

Alternative Splitting Criteria with More Features:

3. User Demographics: If available, splitting the dataset based on user demographics (age, location, etc.) can help in testing the model's performance across different user segments.

4. Product Categories: Splitting based on product categories can be useful if the goal is to test the model's ability to recommend bundles within specific product lines.

#### Note: I have chosen random split as it provides a straightforward and unbiased way to divide the data into training and testing sets, ensuring that the model's performance can be evaluated on diverse samples from the dataset.

### Discuss the size of the output list and how it can be decided per product

The size of our output list, which is essentially the number of items in our recommendation list, can be determined by a variety of factors that are crucial for optimizing user experience and achieving business goals.

1. Business Goals Alignment:

* Determine the size of the recommendation list based on business objectives.
* For revenue maximization, consider recommending a larger number of high-margin products.
* For enhancing customer satisfaction, opt for a smaller, personalized selection.

2. User Preferences Consideration:

* Tailor the size of the recommendation list to accommodate user preferences.
* Some users may prefer longer lists with more options, while others may prefer shorter, focused lists.

3. Model Performance Evaluation:

* Assess recommendation model performance using metrics like precision, recall, and diversity of recommendations.
* Adjust the size of the output list based on model performance and desired trade-offs.

4. Experimentation and Testing:

* Conduct A/B tests to experiment with different list sizes.
* Analyze user engagement metrics such as click-through rates, conversion rates, and revenue generated from recommended products.

5. Iterative Refinement:

* Continuously refine the recommendation system based on experimentation results and user feedback.
* Iterate on the size of the recommendation list to optimize user engagement and achieve business objectives.

#### Note: I have selected default value of 10 products to recommend

### Discuss/implement any price computation per bundle e.g. the sum of products’ prices

#### Define Bundles: 
Determine which products are included in each bundle and specify the pricing rules for the bundle (e.g., fixed price, discounted price, percentage discount).

#### Calculate Bundle Price: 
For each bundle, calculate the total price based on the individual prices of the products included. You can apply any discounts or special pricing logic as needed.

#### Note: For this implementation, I have used simple total sum of products price

### How would you evaluate the business impact of the solution and share the outcome with the internal stakeholders?

To evaluate the business impact of the solution and share the outcome with internal stakeholders, we can follow these steps:

1. Define Key Performance Indicators (KPIs): Identify relevant KPIs that align with your business goals, such as revenue, conversion rate, customer satisfaction, and retention.

2. Baseline Measurement: Establish a baseline measurement of the KPIs before implementing the recommendation system. This will serve as a benchmark for evaluating the impact of the solution.

3. A/B Testing: Conduct A/B tests to compare the performance of the recommendation system with a control group. Randomly assign users to either the group receiving recommendations or the control group.

4. Measure Impact: Monitor the KPIs for both groups over a defined period. Analyze the data to determine whether the recommendation system has a positive impact on the KPIs.

5. Iterate and Optimize: Based on the results, iterate on the recommendation system to optimize its performance. Experiment with different algorithms, recommendation strategies, and list sizes to maximize the business impact.

#### Sharing the Outcome:

* Data Visualization: Use charts and graphs to visually represent the impact of the solution.
* Case Studies: Share specific examples of successful bundle recommendations and their outcomes.
* Quantitative Analysis: Provide a detailed analysis of the metrics collected to quantify the business impact.

#### Note:  The model's performance evaluation has been based on the Root Mean Square Error (RMSE) score, with the model achieving an impressive RMSE score of 0.0033 during training.

### Implement a regression model for the products’ prices (UnitPrice) prediction. Is the provided data sufficient to predict the price? What other data would you like to gather to improve your solution?

The provided data might not be sufficient for accurate price prediction. Additional data that could improve the solution includes:

* Product attributes (e.g., category, brand, weight, dimensions)
* Market trends and economic indicators
* Competitor prices and promotions
* Customer demographics and purchasing behavior







