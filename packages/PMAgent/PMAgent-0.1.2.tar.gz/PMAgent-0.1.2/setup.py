from setuptools import setup, find_packages

setup(
    name='PMAgent',
    version='0.1.2',
    author='Laxman Khatri',
    author_email='khatrilaxman1997@gmail.com',
    description='A Python agent for refactoring and modifying code using OpenAI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JKL404/PMAgent',  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests',  # Example dependency, add others as needed
    ],
    entry_points={
        'console_scripts': [
            'pmagent=pmagent.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
