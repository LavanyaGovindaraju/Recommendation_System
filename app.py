from flask import Flask, request, jsonify
from data_processing import load_and_preprocess_data, prepare_surprise_dataset,split_train_test
from collaborative_filtering import train_collaborative_filtering, generate_item_recommendations
from utils import get_item_price

app = Flask(__name__)

# Load and preprocess the data
data = load_and_preprocess_data("data/data.csv")
dataset = prepare_surprise_dataset(data)
trainset, testset = split_train_test(dataset)

# Train collaborative filtering model
algo = train_collaborative_filtering(trainset)


@app.route('/get_bundle', methods=['GET'])
def get_bundle():
    # Get product ID from request parameters
    product_id = request.args.get('product_id')
    
    # Generate recommendations for the specified product ID
    if product_id:
        product_bundle = generate_item_recommendations(algo, trainset, product_id)
        bundle_price = sum(get_item_price(data, item) for item in product_bundle)
        return jsonify({'recommended_products': product_bundle, 'bundle_price': bundle_price})
    else:
        return jsonify({'error': 'Product ID is missing'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
