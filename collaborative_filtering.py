from surprise import KNNBasic, accuracy

def train_collaborative_filtering(trainset, user_based=False):
    # Define the user-item collaborative filtering algorithm
    algo = KNNBasic(k=3, sim_options={'user_based': user_based})

    # Train the algorithm on the training set
    algo.fit(trainset)
    return algo

def evaluate_collaborative_filtering(algo, testset):
    # Make predictions on the testing set
    predictions = algo.test(testset)

    # Evaluate the predictions
    rmse = accuracy.rmse(predictions)
    return rmse

def generate_user_recommendations(algo, trainset, user_id, top_n=10):
    uid = trainset.to_inner_uid(user_id)
    if uid is not None:
        recommendations = algo.get_neighbors(uid, k=top_n)
        product_bundle_user = [trainset.to_raw_iid(iid) for iid in recommendations]
        return product_bundle_user
    else:
        print("User ID", user_id, "not found in the training set.")
        return []

def generate_item_recommendations(algo, trainset, item_id, top_n=10):
    iid = trainset.to_inner_iid(item_id)
    if iid is not None:
        recommendations = algo.get_neighbors(iid, k=top_n)
        product_bundle_item = [trainset.to_raw_iid(iid) for iid in recommendations]
        return product_bundle_item
    else:
        print("Item ID", item_id, "not found in the training set.")
        return []