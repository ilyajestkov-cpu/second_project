import os
from dotenv import load_dotenv


def print_author():
    load_dotenv()  # загружает переменные из .env
    author = os.getenv("AUTHOR")  # читает значение AUTHOR
    print(f"Автор проекта: {author}")


print_author()
