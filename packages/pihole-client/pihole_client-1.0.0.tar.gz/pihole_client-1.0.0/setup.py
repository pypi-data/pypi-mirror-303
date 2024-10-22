from setuptools import setup

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(name='pihole_client',
      version='1.0.0',
      description='Execute API calls to Pi-hole from python code',
       long_description=readme(),
      long_description_content_type='text/markdown',
      install_requires=[
            'requests==2.32.3', 
            'urllib3==2.2.3',
            'pydantic==2.9.2'
      ],
      license = "MIT",
      packages=['pihole_client'],
      url='https://github.com/ErilovNikita/pihole-client',
      author_email='minitwiks@gmail.com',
      zip_safe=False)