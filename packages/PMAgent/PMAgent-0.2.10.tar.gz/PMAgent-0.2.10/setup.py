from setuptools import setup, find_packages

setup(
    name='PMAgent',
    version='0.2.10',
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
        # Programming Language
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Development Status :: 4 - Beta',
        # Additional relevant classifiers
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Build Tools',
        'Topic :: System :: Systems Administration',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Natural Language :: English',

    ],
    python_requires='>=3.9',
)
