prompt = "\n Powiedz coś o sobie, a wyświetlę"
prompt += "\nNapisz 'koniec' aby zakończyć"
active = True
while active:
    message = input(prompt)
    if message == 'koniec':
        active = False
    else:
        print(message)