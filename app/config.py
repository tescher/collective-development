import os


class base_config(object):
	SITE_NAME = 'The Public School'
	SERVER_NAME = os.environ.get('SERVER_NAME')
	SECRET_KEY = os.environ.get('SECRET_KEY','secrets')
	MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost')
	MAIL_PORT = os.environ.get('MAIL_PORT', 1025)
	DEFAULT_SCHOOL = 'www' # In "single-school" mode, or the root within "multi-school" mode

	# Check if we are running in a Docker container
	if os.environ.get('DB_PORT_27017_TCP_ADDR'):
		MONGODB_SETTINGS = {
			'db': 'collectivedevelopment',
			'host': os.environ.get('DB_PORT_27017_TCP_ADDR'),
			'port': int(os.environ.get('DB_PORT_27017_TCP_PORT')),
			'connecttimeoutms': 10000,
		}
	else:
		MONGODB_SETTINGS = {
			'db': 'collectivedevelopment',
		}
	ACCEPT_LANGUAGES = ['zh']
	BABEL_DEFAULT_LOCALE = 'en'


class dev_config(base_config):
	DEBUG = True
	ASSETS_DEBUG = True


class test_config(base_config):
	TESTING = True
	WTF_CSRF_ENABLED = False
