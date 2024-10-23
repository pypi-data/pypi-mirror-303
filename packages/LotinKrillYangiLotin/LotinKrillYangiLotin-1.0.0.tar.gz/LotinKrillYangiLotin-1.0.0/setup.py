from setuptools import setup, find_packages

setup(
    name='LotinKrillYangiLotin',
    version='1.0.0',
    author='dasturbek',
    author_email='sobirovogabek0409@gmail.com',
    description='Dasturdan o‘zbek tilidagi matnlarni yozuv shaklini'
                'almashtirishda va yangi lotin alifbosini joriy qilishda'
                'foydalanish mumkin!',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ddasturbek/LotinKrillYangiLotin',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
