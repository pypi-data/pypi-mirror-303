from setuptools import setup, find_packages

setup(
    name="reconhecimento_facial",
    version="0.1",
    author="Lucas Azai",
    author_email="lucas.azai@gmail.com",
    description="Projeto de reconhecimento facial usando face_recognition e OpenCV",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Tipo de conteúdo, markdown é comum
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "face_recognition",
        "opencv-python"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Defina a versão mínima do Python, ajuste conforme necessário
    entry_points={
        'console_scripts': [
            'rodar_reconhecimento=main:main',  # Executa o reconhecimento facial pelo terminal
        ],
    },
)
