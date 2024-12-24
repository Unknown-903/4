import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "22409622"))
API_HASH = os.environ.get("API_HASH", "16353e2a4d45ff8be4a2037cca158749")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7592060282:AAGQ3kD8gqY52U7enFEazj0DczlMl0hW9vM")
ADMIN = int(os.environ.get("ADMIN", ""))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002384039357")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002473870713"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Bash_X_Bots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://envs.sh/7H9.jpg")
