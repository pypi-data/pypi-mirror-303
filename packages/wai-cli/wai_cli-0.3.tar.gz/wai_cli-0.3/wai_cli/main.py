import argparse
import json
import os
import requests

CONFIG_DIR = os.path.expanduser('~/.config/wai')
API_KEY_FILE = os.path.join(CONFIG_DIR, 'api_key.txt')


def ensure_config_dir():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)


def save_api_key(api_key):
    ensure_config_dir()
    with open(API_KEY_FILE, 'w') as f:
        f.write(api_key)


def load_api_key():
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as f:
            return f.read().strip()
    return None


def delete_api_key():
    if os.path.exists(API_KEY_FILE):
        os.remove(API_KEY_FILE)

def print_version():
    print("wai version 0.1")


def login():
    api_key = input("Введите ваш API ключ: ")
    save_api_key(api_key)
    print("API ключ сохранен.")


def logout():
    delete_api_key()
    print("API ключ удален.")


def prompt(prompt_text, instructions_text):
    api_key = load_api_key()
    if api_key is None:
        print("Ошибка: необходимо выполнить вход (login). ")
        return

    url = f"https://beta.ai.katskov.tech/api/api/?key={api_key}"
    data = {
        "instructions": instructions_text,
        "prompt": prompt_text
    }
    response = requests.post(url, json=data)

    if response.status_code in [200, 201]:
        answer = response.json().get('answer', 'Нет ответа от API.')
        print(answer)
    else:
        print(f"Ошибка запроса: {response.status_code} {response.text}")


def main():
    parser = argparse.ArgumentParser(prog='wai', description='Утилита для взаимодействия с Ваи.')
    subparsers = parser.add_subparsers(dest='command', help='Команды для работы с утилитой:')

    # Подкоманда 'version'
    version_parser = subparsers.add_parser('version', help='Выводит версию утилиты.')

    # Подкоманда 'login'
    login_parser = subparsers.add_parser('login', help='Запрашивает и сохраняет API ключ.')

    # Подкоманда 'logout'
    logout_parser = subparsers.add_parser('logout', help='Удаляет сохраненный API ключ.')

    # Подкоманда 'prompt'
    prompt_parser = subparsers.add_parser('prompt', help='Отправляет запрос на API.')
    prompt_parser.add_argument(
        '--prompt',
        type=str,
        help='Текст запроса к API. Если указан только текст, используется без явного указания.'
    )
    prompt_parser.add_argument(
        '--instructions',
        type=str,
        help='Инструкции для API при отправке запроса.'
    )

    # Чтение аргументов
    args = parser.parse_args()

    if args.command == 'version':
        print_version()
    elif args.command == 'login':
        login()
    elif args.command == 'logout':
        logout()
    elif args.command == 'prompt':
        if args.prompt and args.instructions:
            prompt(args.prompt, args.instructions)
        elif args.prompt:
            # Если указано только --prompt
            prompt(args.prompt, "")
        else:
            print("Ошибка: требуется указать --prompt или просто текст запроса.")
    else:
        parser.print_help()  # Печатает справку, если не была выбрана команда


if __name__ == '__main__':
    main()