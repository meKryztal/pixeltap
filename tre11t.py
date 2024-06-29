import sys
import json
import time
import hmac
import hashlib
import requests
from datetime import datetime
from colorama import *
from urllib.parse import unquote
import random

init(autoreset=True)


class Data:
    def __init__(self, init_data, userid, username, secret):
        self.init_data = init_data
        self.userid = userid
        self.username = username
        self.secret = secret


class PixelTod:
    def __init__(self):
        self.DEFAULT_COUNTDOWN = 7 * 3600  # Интервал между повтором скрипта, 7 часов дефолт
        self.INTERVAL_DELAY = 3  # Интервал между каждым аккаунтом, 3 секунды дефолт
        self.base_headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en,en-US;q=0.9",
            "Host": "api-clicker.pixelverse.xyz",
            "X-Requested-With": "org.telegram.messenger",
            'origin': 'https://sexyzbot.pxlvrs.io/',
            'referer': 'https://sexyzbot.pxlvrs.io/',
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        }

    def get_secret(self, userid):
        rawr = "adwawdasfajfklasjglrejnoierjboivrevioreboidwa"
        secret = hmac.new(rawr.encode("utf-8"), str(userid).encode("utf-8"), hashlib.sha256).hexdigest()
        return secret

    def data_parsing(self, data):
        return {key: value for key, value in (i.split('=') for i in unquote(data).split('&'))}

    def main(self):

        with open("initdata.txt", "r") as file:
            datas = file.read().splitlines()

        self.log(f'{Fore.LIGHTYELLOW_EX}Обнаружено аккаунтов: {len(datas)}')
        if not datas:
            self.log(f'{Fore.LIGHTYELLOW_EX}Пожалуйста, введите свои данные в initdata.txt')
            sys.exit()

        print('-' * 50)
        while True:
            for no, data in enumerate(datas):
                self.log(f'{Fore.LIGHTYELLOW_EX}Номер аккаунта: {Fore.LIGHTWHITE_EX}{no + 1}')
                data_parse = self.data_parsing(data)
                user = json.loads(data_parse['user'])
                userid = str(user['id'])
                first_name = user.get('first_name')
                last_name = user.get('last_name')
                username = user.get('username')

                self.log(f'{Fore.LIGHTYELLOW_EX}Аккаунт: {Fore.LIGHTWHITE_EX}{first_name} {last_name}')
                secret = self.get_secret(userid)
                new_data = Data(data, userid, username, secret)
                self.process_account(new_data)
                print('-' * 50)
                self.countdown(self.INTERVAL_DELAY)
            self.countdown(self.DEFAULT_COUNTDOWN)

    def process_account(self, data):
        self.get_me(data)
        self.daily_reward(data)
        self.get_mining_proccess(data)
        self.auto_buy_pet(data)
        self.auto_upgrade_pet(data)
        self.daily_combo(data)

    def countdown(self, t):
        while t:
            one, two = divmod(t, 3600)
            three, four = divmod(two, 60)
            print(f"{Fore.LIGHTWHITE_EX}Ожидание до {one:02}:{three:02}:{four:02} ", flush=True, end="\r")
            t -= 1
            time.sleep(1)
        print("                          ", flush=True, end="\r")

    def api_call(self, url, data=None, headers=None, method='GET'):
        while True:
            try:
                if method == 'GET':
                    res = requests.get(url, headers=headers)
                elif method == 'POST':
                    res = requests.post(url, headers=headers, data=data)
                else:
                    raise ValueError(f'Не поддерживаемый метод: {method}')

                if res.status_code == 401:
                    self.log(f'{Fore.LIGHTRED_EX}{res.text}')

                open('.http.log', 'a', encoding='utf-8').write(f'{res.text}\n')
                return res
            except (
            requests.exceptions.ConnectionError, requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout,
            requests.exceptions.Timeout):
                self.log(f'{Fore.LIGHTRED_EX}Ошибка подключения соединения!')
                continue

    def get_me(self, data: Data):
        url = 'https://api-clicker.pixelverse.xyz/api/users'
        headers = self.prepare_headers(data)
        res = self.api_call(url, None, headers)

        if not res.text:
            self.log(f'{Fore.LIGHTRED_EX}Пустой ответ от API get_me.')
            return

        try:
            response_json = res.json()
            balance = response_json.get('clicksCount', 'N/A')
            self.log(f'{Fore.LIGHTYELLOW_EX}Общий баланс: {Fore.LIGHTWHITE_EX}{balance}')
        except json.JSONDecodeError:
            self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API get_me. Ответ: {res.text}')

    def daily_reward(self, data: Data):
        url = 'https://api-clicker.pixelverse.xyz/api/daily-rewards'
        headers = self.prepare_headers(data)
        res = self.api_call(url, None, headers)

        if not res.text:
            self.log(f'{Fore.LIGHTRED_EX}Пустой ответ от API ежедневного вознаграждения.')
            return

        try:
            response_json = res.json()
        except json.JSONDecodeError:
            self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API ежедневного вознаграждения. Ответ: {res.text}')
            return

        if response_json.get('todaysRewardAvailable'):
            url_claim = 'https://api-clicker.pixelverse.xyz/api/daily-rewards/claim'
            res = self.api_call(url_claim, '', headers, method='POST')

            if not res.text:
                self.log(f'{Fore.LIGHTRED_EX}Пустой ответ от API на запрос ежедневного вознаграждения.')
                return

            try:
                claim_response = res.json()
                amount = claim_response.get('amount', 'N/A')
                self.log(f'{Fore.LIGHTYELLOW_EX}Ежедневное вознаграждение: {Fore.LIGHTWHITE_EX}{amount}')
            except json.JSONDecodeError:
                self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API на запрос ежедневного вознаграждения. Ответ: {res.text}')
        else:
            self.log(f'{Fore.LIGHTYELLOW_EX}Ежедневное вознаграждение уже забирали!')

    def get_mining_proccess(self, data: Data):
        url = "https://api-clicker.pixelverse.xyz/api/mining/progress"
        headers = self.prepare_headers(data)
        res = self.api_call(url, None, headers)

        if not res.text:
            self.log(f'{Fore.LIGHTRED_EX}Пустой ответ от API прогресса майнинга.')
            return

        try:
            response_json = res.json()
        except json.JSONDecodeError:
            self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API прогресса майнинга. Ответ: {res.text}')
            return

        available = response_json.get('currentlyAvailable', 0)
        min_claim = response_json.get('minAmountForClaim', float('inf'))
        self.log(f'{Fore.LIGHTYELLOW_EX}Доступная сумма: {Fore.LIGHTWHITE_EX}{available}')

        if available > min_claim:
            url_claim = 'https://api-clicker.pixelverse.xyz/api/mining/claim'
            res = self.api_call(url_claim, '', headers, method='POST')

            if not res.text:
                self.log(f'{Fore.LIGHTRED_EX}Пустой ответ от API на запрос майнинга.')
                return

            try:
                claim_response = res.json()
                claim_amount = claim_response.get('claimedAmount', 'N/A')
                self.log(f'{Fore.LIGHTYELLOW_EX}Забрал с майнинга: {Fore.LIGHTWHITE_EX}{claim_amount }')
            except json.JSONDecodeError:
                self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API на запрос майнинга. Ответ: {res.text}')
        else:
            self.log(f'{Fore.LIGHTRED_EX}Сумма слишком мала чтоб забрать!')

    def auto_buy_pet(self, data: Data):
        url = 'https://api-clicker.pixelverse.xyz/api/pets/buy?tg-id={self.tg_id}&secret={self.secret}'
        headers = self.prepare_headers(data)
        res_buy_pet = self.api_call(url, data=json.dumps({}), headers=headers, method='POST')
        if res_buy_pet.status_code == 200 or res_buy_pet.status_code == 201:
            try:
                buy_pet_data = res_buy_pet.json()
                pet_name = buy_pet_data.get('pet', {}).get('name', 'Unknown')
                self.log(f'{Fore.LIGHTYELLOW_EX}Купил питомца: {Fore.LIGHTWHITE_EX}{pet_name}!')
            except json.JSONDecodeError:
                self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API покупки питомца.')
        else:
            self.log(f'{Fore.LIGHTRED_EX}Еще не прошел кулдаун покупки нового питомца.')

    def auto_upgrade_pet(self, data: Data):
        url = 'https://api-clicker.pixelverse.xyz/api/pets'
        headers = self.prepare_headers(data)
        res = self.api_call(url, None, headers)
        pets = res.json().get('data', [])

        if pets:
            while True:
                pets_sorted = sorted(pets, key=lambda pet: pet['userPet']['level'])

                for pet in pets_sorted:
                    pet_name = pet["name"].strip()
                    pet_id = pet['userPet']['id']
                    url_upgrade = f'https://api-clicker.pixelverse.xyz/api/pets/user-pets/{pet_id}/level-up'
                    res_upgrade = self.api_call(url_upgrade, '', headers, method='POST')

                    if res_upgrade.status_code == 200 or res_upgrade.status_code == 201:
                        self.log(f'{Fore.LIGHTYELLOW_EX}Улучшил питомца: {Fore.LIGHTWHITE_EX}{pet_name} Lv.{pet["userPet"]["level"]}')
                        time.sleep(3)
                    else:
                        error_message = res_upgrade.json().get('message', 'Unknown error')
                        self.log(f'{Fore.LIGHTRED_EX}Не удалось улучшить питомца: {pet_name}, Ответ: {error_message}')
                        return

                    res = self.api_call(url, None, headers)
                    pets = res.json().get('data', [])
                    break
        else:
            self.log(f'{Fore.LIGHTRED_EX}Нету питомцев для улучшения')

    def daily_combo(self, data: Data):
        id_pets_list = [
            "0a6306e5-cc33-401a-9664-a872e3eb2b71",
            "571523ae-872d-49f0-aa71-53d4a41cd810",
            "78e0146f-0dfb-4af8-a48d-4033d3efdd39",
            "7c3a95c6-75a3-4c62-a20e-896a21132060",
            "8074e9c5-f6c2-4012-bfa2-bcc98ceb5175",
            "d364254e-f22f-4a43-9a1c-5a7c71ea9ecd",
            "dc5236dc-06be-456b-a311-cccedbd213ca",
            "e8c505ed-df93-47e0-bd2e-0e664d09ba86",
            "ef0adeca-be18-4503-9e9a-d93c22bd7a6e",
            "f097634a-c8e8-4de9-b707-575d20c5fd88",
            "50e9e942-36d5-4f19-9bb7-c892cb956fff",
            "7ee9ed52-c808-4187-a942-b53d972cd399",
            "36621a17-81f3-4d5d-b4e1-4b0cf51d4610",
            "90a07a32-431a-4299-be59-598180ee4a8c",
            "45f2e16e-fb64-4e15-a3fa-2fb99c8d4a04",
            "3bfab57c-a57f-48d9-8819-c93c9f531478",
            "341195b4-f7d8-4b9c-a8f1-448318f32e8e",
            "bc3f938f-8f4c-467b-a57d-2b40cd500f4b",
            "f82a3b59-913d-4c57-8ffd-9ac954105e2d",
            "d59cd843-1b53-4131-9966-641d41aa634b"
        ]

        id_pets = random.sample(id_pets_list, 4)

        url_current_game = "https://api-clicker.pixelverse.xyz/api/cypher-games/current"
        headers = self.prepare_headers(data)
        res_current_game = self.api_call(url_current_game, None, headers)

        if res_current_game.status_code == 200 and res_current_game.text:
            try:
                game_data = res_current_game.json()
            except json.JSONDecodeError:
                self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API списка комбо.')
                return

            if game_data['status'] == "ACTIVE":
                game_id = game_data.get('id')
                id_pets = [pet_id.strip() for pet_id in id_pets]
                payload = {pet_id: len(id_pets) - id_pets.index(pet_id) - 1 for pet_id in id_pets}

                url_answer = f"https://api-clicker.pixelverse.xyz/api/cypher-games/{game_id}/answer"
                headers['Content-Type'] = 'application/json'
                res_answer = self.api_call(url_answer, data=json.dumps(payload), headers=headers, method='POST')

                if res_answer.status_code == 200 or res_answer.status_code == 201:
                    try:
                        answer_data = res_answer.json()
                        reward_amount = answer_data.get('rewardAmount', 'N/A')
                        self.log(f'{Fore.LIGHTYELLOW_EX}Успешно запросил комбо: {Fore.LIGHTWHITE_EX}{reward_amount}')
                    except json.JSONDecodeError:
                        self.log(f'{Fore.LIGHTRED_EX}Не удалось декодировать JSON-ответ от API запроса комбо.')
                else:
                    self.log(f'{Fore.LIGHTRED_EX}Не удалось запросить комбо: {res_answer.text}')
            else:
                self.log(f'{Fore.LIGHTRED_EX}Сегодня комбо уже получен!')
        else:
            self.log(f'{Fore.LIGHTRED_EX}Сегодня комбо уже получен!')

    def prepare_headers(self, data: Data):
        headers = self.base_headers.copy()
        headers.update({
            'initData': data.init_data,
            'secret': data.secret,
            'tg-id': data.userid
        })
        if data.username:
            headers['username'] = data.username
        return headers

    def log(self, message):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{Fore.LIGHTBLACK_EX}[{now}]{Style.RESET_ALL} {message}")


if __name__ == "__main__":
    try:
        app = PixelTod()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
