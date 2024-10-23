from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f.readlines()]


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='xmlAnomalyDetection',
    version='8.0',
    packages=find_packages(),
    install_requires=install_requires,
    author='Talha Yousuf',
    author_email='th05691@gmail.com',
    entry_points="""
        [console_scripts]
        xml_anomaly_detection=xmlAnomalyDetection.cli:main
    """,
    include_package_data=True,
    description='A tool for detecting anomalies in XML data',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
