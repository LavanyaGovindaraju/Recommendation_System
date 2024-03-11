# main.py
import argparse
from data_processing import load_and_preprocess_data, prepare_surprise_dataset, split_train_test
from collaborative_filtering import train_collaborative_filtering, evaluate_collaborative_filtering, generate_user_recommendations, generate_item_recommendations
from price_prediction import train_linear_regression_model, evaluate_regression_model
from utils import get_item_price


def main(args):
    
    # Data Processing
    data = load_and_preprocess_data("data/data.csv")

    # Collaborative Filtering
    dataset = prepare_surprise_dataset(data)
    trainset, testset = split_train_test(dataset)
    
    if args.collab_filter == "user":
        algo = train_collaborative_filtering(trainset)
        evaluate_collaborative_filtering(algo, testset)
        
        # Generate recommendations for a specific user
        user_id = args.user_id
        top_n = 10
        item_recommendations = generate_user_recommendations(algo, trainset, user_id, top_n)
        print("Top", top_n, "recommendations for user", user_id, ":", item_recommendations)
    
    elif args.collab_filter == "item":
        algo_item = train_collaborative_filtering(trainset)
        evaluate_collaborative_filtering(algo_item, testset)
        
        # Generate recommendations for a specific item
        item_id = args.item_id
        top_n = 10
        item_recommendations = generate_item_recommendations(algo_item, trainset, item_id, top_n)
        print("\nTop", top_n, "recommendations for item", item_id, ":", item_recommendations)
        
        bundle_price = sum(get_item_price(data, item) for item in item_recommendations)
        print("Total price of the final bundle:", bundle_price)

    print('\nEvaluation of Regression Model\n')
    # Price Prediction
    X = data[['Quantity']]
    y = data['UnitPrice']
    model, X_test, y_test = train_linear_regression_model(X, y)
    evaluate_regression_model(model, X_test, y_test)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recommendation System and Price Prediction')
    parser.add_argument('--collab_filter', choices=['user', 'item'], default='item', help='Specify collaborative filtering type: user or item')
    parser.add_argument('--user_id',       type=float,               default=None,   help='User ID for user-based collaborative filtering')
    parser.add_argument('--item_id',       type=str,                 default=None,    help='Item ID for item-based collaborative filtering')
    args = parser.parse_args()
    main(args)
 