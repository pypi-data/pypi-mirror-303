from setuptools import setup, find_packages

setup(
    name='rocketAouaichia',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='hafsa',
    author_email='your.email@example.com',
    description='A package for simulating rockets and shuttles',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/yourusername/rocket',  # Replace with your actual URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
