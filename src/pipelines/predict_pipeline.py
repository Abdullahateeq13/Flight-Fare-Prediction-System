# import sys
# import pandas as pd
# import datetime
# from src.exception import CustomException
# from src.utils import load_object

# class PredictPipeline:
#     def __init__(self) -> None:
#         pass

#     def predict(self, features):
#         try:
#             model_path = 'artifacts\model.pkl'
#             model = load_object(file_path=model_path)
#             preds = model.predict(features)
#             return preds
        
#         except Exception as e:
#             raise CustomException(e, sys)
    

# class CustomData:
#     def __init__(self,
#             dep_time: datetime,
#             arrival_time: datetime,
#             source: str,
#             destination: str,
#             stops: int,
#             airline: str):
        
#         self.dep_time = dep_time
#         self.arrival_time = arrival_time
#         self.source = source
#         self.destination = destination
#         self.stops= stops
#         self.airline = airline

#     def get_data_as_dataframe(self):
#         try:
#             custom_data_input_dict = {
#                 "dep_time": [self.dep_time],
#                 "arrival_time": [self.arrival_time],
#                 "source": [self.source],
#                 "destination": [self.destination],
#                 "stops": [self.stops],
#                 "airline": [self.airline]
#             }

#             return pd.DataFrame(custom_data_input_dict)
#         except Exception as e:
#             raise CustomException(e, sys)

            