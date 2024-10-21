from setuptools import setup, find_packages

setup(
    name='srvllm',
    version='0.0.0',
    author='Yao Fu',
    description='A brief description of sl-llm',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # Add your project's dependencies here, e.g.,
        # 'some_package>=1.0',
    ],
)
