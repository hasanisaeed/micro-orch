import setuptools

setuptools.setup(name="morch",
                 version="1.0.0",
                 author="Saeed Hasani Borzadaran",
                 author_email="hassanisaeed19@gmail.com",
                 description="SAGA Python Microservice Orchestrator",
                 long_description_content_type="text/markdown",
                 url="https://github.com/hasanisaeed/morch",
                 keywords='microservice, saga, patterns, microservice patterns, saga pattern',
                 python_requires='>=3.9',
                 install_requires=["asyncapi==0.14.1",
                                   "uvicorn==0.22.0",
                                   "typer==0.9.0",
                                   "PyYAML==6.0.1",
                                   "Jinja2==3.1.2",
                                   "apidaora==0.28.0",
                                   "markdown==3.4.3"
                                   ],
                 project_urls={"Bug Tracker": "https://github.com/hasanisaeed/morch/issues/new",
                               },
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: MIT License",
                              "Operating System :: OS Independent",
                              ],
                 )
