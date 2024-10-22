from setuptools import setup
from pg_httpserver import VERSION

DIST_NAME = "pg_httpserver"
__author__ = "baozilaji@gmail.com"

setup(
	name=DIST_NAME,
	version=VERSION,
	description="python game: httpserver",
	packages=['pg_httpserver'],
	author=__author__,
	python_requires='>=3.9',
	# data_files=[
	# 	('pg_httpserver/static', ['static/swagger-ui/swagger-ui.css', 'static/swagger-ui/swagger-ui-bundle.js'])
	# ],
	install_requires=[
		'pg-redis>=0',
		'pg-resourceloader',
		'fastapi==0.115.2',
		'uvicorn==0.31.1'
	],
)
