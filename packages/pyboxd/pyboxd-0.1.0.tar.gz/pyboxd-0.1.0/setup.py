from setuptools import setup, find_packages

setup(
    name='pyboxd',
    version='0.1.0',
    packages=find_packages(where="src"),  # Specify that packages are inside the src folder
    package_dir={"": "src"},  # Tell setuptools to look inside the 'src' folder
    install_requires=[],  # Add any dependencies if needed
    author='Juan Fernandez Cruz',
    author_email='fercruzjuan2002@gmail.com',
    description='A Python Letterboxd Webscraper Library with BeautifulSoup and Requests.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    url='https://github.com/yourusername/pyboxd',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
