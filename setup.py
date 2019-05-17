from setuptools import setup, find_packages

setup(
    name='agentk',
    version='0.0.1',
    py_modules=['agentk'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Jinja2',
        'sendgrid',
        'click',
        'lookerapi',
        'cloudinary'
    ],
    entry_points='''
        [console_scripts]
        agentk=cli:cli
    ''',
)