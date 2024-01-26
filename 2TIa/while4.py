unconfirmed_users = ['Alicja','Bartek','Kinga']
confirmed_users = []
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"Weryfikacja użytkownika {current_user}")
    confirmed_users.append(current_user)
print( "\nZwryfikowani użytkownicy")
for user in confirmed_users:
    print( user )