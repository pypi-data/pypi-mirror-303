from setuptools import setup, find_packages

setup(
    name='grant_funding_assistant',
    version='0.4',
    description='This is a multiagent system which can help researchers create grant funding proposals based on their research profile and funding guidelines',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Akshay P R',
    author_email='akshaypr314159@gmail.com',
    url='https://github.com/Dorcatz123/grant_funding_assistant',
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        'crewai',
        'crewai_tools',
        'langchain_community',
        'Ipython'

    ],
    entry_points={
        'console_scripts': [
            'grant_funding_assistant = grant_funding_assistant.main:main',  # Define the console command and entry point
        ],
    },


    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',  # Specify the Python version your project supports
)
