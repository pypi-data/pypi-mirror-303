import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SKIE", # 모듈 이름
    version="0.3.3", # 버전
    author="knut_urban", # 제작자
    author_email="tnekf0314@ut.ac.kr", # contact
    description="prototype-used-in-skie", # 모듈 설명
    long_description=open('README.md').read(), # README.md에 보통 모듈 설명을 해놓는다.
    long_description_content_type="text/markdown",
    url="",
    install_requires=[ # 필수 라이브러리들을 포함하는 부분인 것 같음, 다른 방식으로 넣어줄 수 있는지는 알 수 없음
    "pandas",
    "numpy",
    "scipy",
    "geopandas",
    "pydeck",
    "simplejson"
    ],
    package_data={'': ['LICENSE.txt', 'requirements.txt']}, # 원하는 파일 포함, 제대로 작동되지 않았음
    include_package_data=True,
    packages = setuptools.find_packages(), # 모듈을 자동으로 찾아줌
    python_requires=">=3.8.6", # 파이썬 최소 요구 버전
)