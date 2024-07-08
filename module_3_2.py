def send_email(message, recipient, sender = "university.help@gmail.com"):
    for x in [recipient, sender]:
        if not x.endswith((".com", ".ru", ".net")):
            return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    if recipient == sender:
        return "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}"

print(send_email('Privet!', 'rare_avis@ukr.net', "cheef@mail.ru"))


