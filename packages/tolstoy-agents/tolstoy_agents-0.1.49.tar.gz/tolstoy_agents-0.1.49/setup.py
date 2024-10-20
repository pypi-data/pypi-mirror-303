from setuptools import setup, find_packages

setup(
    name='tolstoy_agents',                    # Package name
    version='0.1.49',                          # Initial version
    packages=find_packages(),                 # Automatically find packages in tolstoy_agents directory
    install_requires=[                        # List dependencies here
        # 'google-auth',
        # 'google-auth-oauthlib',
        # 'google-auth-httplib2',
        # 'google-api-python-client',
        # 'google-cloud-aiplatform',
        'langgraph==0.2.16',
        'langchain==0.2.15',
        'langchain-openai==0.1.23',
        'langchain-core==0.2.35'
    ],
    author='Tolstoy',                       # Your name
    author_email='tolstoy@gotolstoy.com',    # Your email
    description='Framework to create LLM agents',
    long_description=open('README.md').read(), # Optional: long description from README.md
    long_description_content_type='text/markdown', # Optional: if your README is in Markdown
    #url='https://github.com/yourusername/tolstoy_agents', # Optional: URL to your package repository
    classifiers=[                             # Optional: Classifiers to categorize the package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                  
)
