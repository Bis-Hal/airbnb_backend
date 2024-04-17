import pickle
import joblib

def getResponse():
    rating_model = joblib.load('./models/rating.pkl');
    price_model = joblib.load('./models/-price_hotel_owners_model.pkl');
    rating_prdiction = rating_model.predict(input_data)
    price_prediction = price_model.predict(X_train)
    print(rating_prdiction)

def test():
    rating_model = joblib.load('./models/rating.pkl');
    price_model = joblib.load('./models/-price_hotel_owners_model.pkl');
    X_train = [
        [1.0, 1.0, 2.0, 1.0, 2.0, 0, 48.858, 2.32125, 1.0, 8.627959388639653, 365.0, 0.0, 562.5]
    ] 
    input_data = {
    1.0,
    2.0,
    3.0,
    1.0,
    40.7128,
    -74.0060,
    0.5,
    rating.transform('Apartment'),
    rating.transform('Entire home/apt'),
    rating.transform('High'),
    1.0,
    2.0,
    100.0,
    50,
    1.0,
    365.0
}
    rating_prdiction = rating_model.predict(input_data)
    # price_prediction = price_model.predict(X_train)
    print(rating_prdiction)

# test()
