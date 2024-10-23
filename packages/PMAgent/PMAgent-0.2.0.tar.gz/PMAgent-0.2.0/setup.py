from setuptools import setup, find_packages

setup(
    name='PMAgent',
    version='0.2.0',
    author='Laxman Khatri',
    author_email='khatrilaxman1997@gmail.com',
    description='A PMAgent is an Expert Technical Professional with comprehensive knowledge across multiple domains including Full Stack Development, Data Science, Data Analysis, DevOps, and Machine Learning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/JKL404/PMAgent',
    packages=find_packages(),
    install_requires=[
        'openai==1.50.2',
        'groq==0.6.0',
        'mistune==3.0.2',
        'requests',
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
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
    ],
    python_requires='>=3.9',
)
