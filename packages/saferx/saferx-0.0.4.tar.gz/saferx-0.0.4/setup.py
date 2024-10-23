from setuptools import setup, find_packages
import setuptools

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    
    name='saferx', # 모듈 이름
    version='0.0.4', # 버전
    long_description= long_description, # READ.md에 보통 모듈 해놓음
    long_description_content_type= 'text/markdown',

    description='safer package', 
    author='rirakang',
    author_email='rirakang@gachon.ac.kr',
    
    url='https://github.com/gachon-CCLab/SAFER_LIB.git',
    install_requires = ['torch','pandas','numpy','scikit-learn'],
    include_package_data=True,
    packages = setuptools.find_packages(),
    package_data={
        'gsecure': [
            'model1/model/tft_model.pkl',
            'model2/model/final_model.pkl'
        ],
    },
    python_requires=">=3.6" #파이썬 최소 요구 버전


)