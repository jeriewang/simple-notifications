import platform

if platform.system()!='Darwin':
	raise Exception("This package only works on macOS")

if not 10<=int(platform.mac_ver()[0].split('.')[1])<=14:
	raise Exception("This package only supports macOS 10.10 to 10.14")

from setuptools import setup

setup(
	name="simple-notifications",
	install_requires=[
		'pyobjc-core',
		'pyobjc-framework-cocoa',
	],
	packages=['simple_notifications'],
	package_data={
	    'simple_notifications':["*.md","*.so"]
	},
	zip_safe=False,
	version='0.1.1',

	python_requires=">=2.7,>=3.5,<=3.7",

	author="Jerry Wang",
	description="A simple package for sending notifications in macOS",
	long_description=open('README.md').read(),
	long_description_content_type="text/markdown",
	author_email="yrrejkk@gmail.com",
	keywords="macOS notification notifications nc",
	include_package_data=True,
	project_urls={
	"GitHub":"https://github.com/pkqxdd/simple-notifications",
	},
	license="MIT"
)