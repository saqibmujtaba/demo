from flask import Flask

# extensions
from flask_pymongo import PyMongo
from flask_wtf.csrf import CSRFProtect
from flask_moment import Moment
# from flask_images import Images
from flask_mail import Mail, Message
from flask_recaptcha import ReCaptcha
import ConfigStore as cnf

import os

# UPLOAD_PATH=cnf.getConfig('STORE', 'u_path')
s_uname=cnf.getConfig('STORE', 'serviceUsername')
s_upass=cnf.getConfig('STORE', 'servicePassword')
s_db=cnf.getConfig('STORE', 'serviceDB')

# WEB
s_host=cnf.getConfig('WEB', 'host')
s_port=cnf.getConfig('WEB', 'port')
s_id=cnf.getConfig('WEB', 'id')



# create application instance
app=Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'noreply@travel2kashmir.com',
    "MAIL_PASSWORD": 'passwordhere'
}

app.config['RECAPTCHA_SITE_KEY'] = cnf.getConfig('RECAPTCHA', 'RECAPTCHA_SITE_KEY')
app.config['RECAPTCHA_SITE_SECRET'] = cnf.getConfig('RECAPTCHA', 'RECAPTCHA_SITE_SECRET')
app.config['RECAPTCHA_ENABLED'] = cnf.getConfig('RECAPTCHA', 'RECAPTCHA_ENABLED')


# app.config["MONGO_URI"] = "mongodb://"+ s_uname +":" + s_upass +"@ds024778.mlab.com:24778/"+ s_db
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/"+ s_db
# app.config["MONGO_URI"] = cnf.getConfig('STORE', 'URI')
# app.config["MONGO_URI"] = "mongodb://rosepetal:63xwBcsYbfxuJ0lR@rosepetal-shard-00-00-kinxq.mongodb.net:27017,rosepetal-shard-00-01-kinxq.mongodb.net:27017,rosepetal-shard-00-02-kinxq.mongodb.net:27017/t2k?ssl=true&replicaSet=rosepetal-shard-0&authSource=admin&retryWrites=true"
# app.config["SERVER_NAME"] = 'localhost:5000' #str(s_host + ':' + s_port)


app.config.update(mail_settings)

# initializes extensions
mongo = PyMongo(app)
csrf = CSRFProtect(app)
moment = Moment(app)
recaptcha = ReCaptcha(app)
mail = Mail(app)
# images = Images(app)



# Importing views/routes
from t2k.api.routes import mod
from t2k.admin.routes import mod
from t2k.site.routes import mod
from t2k.hotels.routes import mod


# registering blueprint routes
app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')
app.register_blueprint(admin.routes.mod, url_prefix='/admin')
# app.register_blueprint(hotels.routes.mod,
#                             #url_prefix='/hotels'
#                             subdomain='<subdomain>'
#                             )
