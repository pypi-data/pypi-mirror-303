from setuptools import setup, find_packages

setup(
  name='Flask-LPackages',
  version='1.0.0',
  author='Alexandr246',
  author_email='alexandr246@vk.com',
  description='Packages I need in my flask app',
  long_description='Packages I need in my flask app',
  long_description_content_type='text/plain',
  packages=find_packages(),
  install_requires=['Flask==3.0.3',
                    'Flask-Login==0.6.3',
                    'Flask-SQLAlchemy==3.1.1',
                    'Flask-Migrate==4.0.7',
                    'Flask-WTF==1.2.1',
                    'python-dotenv==1.0.1',
                    'Werkzeug==3.0.4'],
  classifiers=[
    'Programming Language :: Python :: 3.9',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='packages list l flask app',
  python_requires='>=3.9'
)