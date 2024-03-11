
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    # Load dataframe from csv with specified encoding
    data = pd.read_csv(file_path, encoding='latin1')

    # Filter out records with Quantity <= 0
    data = data.loc[data['Quantity'] > 0]

    # Drop rows with missing CustomerID
    data = data.dropna(subset=['CustomerID'])

    # Create a 'TotalPrice' column
    data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

    # Normalize Quantity and UnitPrice columns
    data_norm = data.copy()
    scaler = MinMaxScaler()
    data_norm[['Quantity', 'UnitPrice']] = scaler.fit_transform(data_norm[['Quantity', 'UnitPrice']])

    return data_norm

def prepare_surprise_dataset(data):
    # Define the Reader object
    reader = Reader(rating_scale=(0, 1))  # Rating scale is normalized now

    # Load the dataset
    dataset = Dataset.load_from_df(data[['CustomerID', 'StockCode', 'Quantity']], reader)

    return dataset

def split_train_test(dataset):
    # Split the dataset into training and testing sets
    trainset, testset = train_test_split(dataset, test_size=0.2, random_state=42)
    return trainset, testset
