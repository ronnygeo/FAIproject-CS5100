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
# REF_USER_ID = "pEVf8GRshP9HUkSpizc9LA"
# REF_USER_ID = "DrWLhrK8WMZf7Jb-Oqc7ww"
REF_USER_ID = "Iu3Jo9ROp2IWC9FwtWOaUQ"
# REF_USER_ID = "3gIfcQq5KxAegwCPXc83cQ"
# REF_USER_ID = "5lq4LkrviYgQ4LJNsBYHcA"


#200 review range
# REF_USER_ID = "A3mpjzazkSDkua4cPSayYA"
#  REF_USER_ID = "wNqwKWaRjClmcKsoJJRFow"
# REF_USER_ID = "2l2lRFuHLdyGjAuusqPDag"
# REF_USER_ID = "QlOc_cKy_7Fs-Pg0vi9NAg"
# REF_USER_ID = "gUr8qs00wFAk851yHMlgRQ"
# REF_USER_ID = "WdzFfqEoVWqh8bp9mkzPfA"

#100 review range
# REF_USER_ID = "22glItKiH7hQRWszhmcohw"
# REF_USER_ID = "22-6yC05pgWbLupHZTjQig"
# REF_USER_ID =  "crHk39O5I5ZEpzNQz6XgAw"
# REF_USER_ID = "0tYlK-FieQXAdmTQ9DWTbA"
# REF_USER_ID = "PuTmcfPDLNUAKo68LmdZOA"

USER_TRAINING_FACTOR = .75

KNN_NEIGHBOURS = 5

ENABLE_DISTANCE_FILTER = False
DISTANCE_TO_FILTER = 10

ENABLE_TIME_FILTER = False
TIME_TO_FILTER = datetime.today()

PLOT_RESULTS = False

# USE_FRIENDS = False
USE_FRIENDS = True

# MAIN_COLLECTION = db.user_review_friends