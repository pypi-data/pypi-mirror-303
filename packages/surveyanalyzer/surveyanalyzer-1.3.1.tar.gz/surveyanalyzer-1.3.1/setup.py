from setuptools import setup, find_packages

setup(
    name='surveyanalyzer',
    version='1.3.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'python-dotenv',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'wordcloud',
        'jaconv',
        'mecab-python3',
    ],
    url='https://github.com/lupin-oomura/SurveyAnalyzer.git',
    author='Shin Oomura',
    author_email='shin.oomura@gmail.com',
    description='A simple Comment Classification Tools',
)
