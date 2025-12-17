# import logging

# # create logger
# di = logging.getLogger("data_ingestion")
# di.setLevel(logging.INFO)

# # create file handler
# di_file = logging.FileHandler("di_file.log")

# # create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

# # set formatter to file
# di_file.setFormatter(formatter)

# # add handler to logger  ✅ (IMPORTANT)
# di.addHandler(di_file)

# # log messages
# di.info("this is custom message for data ingestion")
# di.warning("this is a warning message for data ingestion")
import logging

me = logging.getLogger("model_eval")
model_handler = logging.FileHandler("model_eval.log")

formtter = logging.Formatter("%(asctime)s -%(name)s - %(message)s ")

model_handler.setFormatter(formtter)
me.addHandler(model_handler)

me.setLevel(logging.INFO)

me.info("this is custom message for model evaluation")
me.warning("this is a warning message for model evaluation")
