# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27419615")

API_HASH = os.environ.get("API_HASH", "2f4b181296f0a2615a85471a1c72df44")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7962557432:AAFeUsaO2Me3nl0DaVLvKUv0Io783R_lFH4") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Otaku_Atlas") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "rohitl3031")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://rohitl3031:CNHkZh4Nkgv0mUuJ@cluster0.cgmci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/f68485a91495405874fbf-e850a37999c8e3aee0.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1534632634').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
