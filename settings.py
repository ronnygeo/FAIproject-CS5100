from datetime import datetime

SYS_ENCODING_UTF = "utf8"
JSON_FILE_PATH = "static/json/"
JSON_FILE_NAME = "kGgAARL2UmvCcTRfiscjug_reviews_business_model.json"
REF_USER_NAME = "Bob"
# no review no friends
# REF_USER_ID = "3EcK_7CmaQNzUgsgJnQc7w"
# initial case, 2322 friends, 783 reviews
# REF_USER_ID = "kGgAARL2UmvCcTRfiscjug"
#other cases
# REF_USER_ID = "9A2-wSoBUxlMd3LwmlGrrQ"
REF_USER_ID = "DrWLhrK8WMZf7Jb-Oqc7ww"
# REF_USER_ID = "Iu3Jo9ROp2IWC9FwtWOaUQ"
# REF_USER_ID = "3gIfcQq5KxAegwCPXc83cQ"
# REF_USER_ID = "ia1nTRAQEaFWv0cwADeK7g"
# REF_USER_ID = "glRXVWWD6x1EZKfjJawTOg"
# REF_USER_ID = "uZbTb-u-GVjTa2gtQfry5g"
# REF_USER_ID = "5lq4LkrviYgQ4LJNsBYHcA"
# REF_USER_ID = "pEVf8GRshP9HUkSpizc9LA"


USER_TRAINING_FACTOR = .75

KNN_NEIGHBOURS = 5

ENABLE_DISTANCE_FILTER = False
DISTANCE_TO_FILTER = 10

ENABLE_TIME_FILTER = False
TIME_TO_FILTER = datetime.today()

PLOT_RESULTS = False

USE_FRIENDS = False

# MAIN_COLLECTION = db.user_review_friends