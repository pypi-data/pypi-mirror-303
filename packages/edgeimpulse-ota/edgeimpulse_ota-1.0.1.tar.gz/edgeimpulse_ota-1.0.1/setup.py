from distutils.core import setup


setup(
    name='edgeimpulse_ota',
    packages=['edgeimpulse_ota'],
    version='1.0.1',
    license='MIT',
    description='OTA updates for Edge Impulse models',
    author='Simone Salerno',
    author_email='support@eloquentarduino.com',
    url='https://github.com/eloquentarduino/python-edgeimpulse-ota',
    keywords=[
        'ML',
        'Edge AI'
    ],
    install_requires=[
        'Jinja2',
        'requests'
    ],
    package_data={
        'edgeimpulse_ota': ['templates/*.jinja']
    },
)
