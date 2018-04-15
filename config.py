class Config(object):
	"""
	Common configs
	"""

class DevelopmentConfig(Config):
	"""
	Development configs
	"""
	DEBUG = True
	SQLALCEHMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production configs
	"""
	DEBUG = False

app_config={
	'development': DevelopmentConfig,
	'production': ProductionConfig
}