from setuptools import setup, find_packages

setup(
    name='z_score_target_engagement',  
    version='2.2.12',                    
    packages=find_packages(),            
    include_package_data=True,          
    package_data={
        'z_score_target_engagement': ['data/*.json',
                                      'data/*.txt',],  
    },
)
