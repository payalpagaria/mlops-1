import joblib
mind=joblib.load("marks_model.pkl")
mind.predict([[2]])