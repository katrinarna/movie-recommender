from setuptools import setup, find_packages

setup(
    name="movie-recommender",
    version="0.1.0",
    description="A content-based movie recommendation system using cosine similarity and the TMDb API.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "pandas",
        "scikit-learn",
        "requests",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.7',
)

