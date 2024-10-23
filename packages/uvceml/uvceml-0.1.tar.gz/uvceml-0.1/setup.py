from setuptools import setup

setup(
    name='uvceml',
    version='0.1',
    py_modules=['uvceml'],  # this should be the name of your Python file without the .py extension
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'pgmpy',
    ],
    author='Ganesh',
    author_email='ganesh4study@email.com',
    description='A Python package implementing various machine learning algorithms of uvce',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
