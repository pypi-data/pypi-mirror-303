from setuptools import setup

setup(name='cjk6_source_ci_secrets',
      version='0.0.26',
      description='A secrets scanner for CI/CD forked from ci_secrets.',
      author='Christian Kang',
      author_email='christiankang56@gmail.com',
      url="https://github.com/cjk6-source/ci_secrets",
      packages=['cjk6_source_ci_secrets'],
      install_requires=["gitpython","detect_secrets"],
      entry_points={
        'console_scripts': [
            'cjk6_source_ci_secrets = cjk6_source_ci_secrets:main'
        ]
      },
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Security",
        "Topic :: Software Development"
      ])
