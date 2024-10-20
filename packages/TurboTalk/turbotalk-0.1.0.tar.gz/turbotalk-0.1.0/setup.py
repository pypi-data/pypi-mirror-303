from setuptools import setup, find_packages

setup(
    name='TurboTalk',  # Updated name
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'g4f',
        'colorama',
    ],
    description='A chatbot module using g4f and colorama.',
    author='Rushi Soni',
    author_email='rushisoni1209@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
