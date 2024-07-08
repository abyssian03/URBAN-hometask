def send_email(message, recipient, sender = "university.help@gmail.com"):
    for dom in [".com", ".ru", ".net"]:
        if recipient.endswith(dom):
            flag1 = True
        if sender.endswith(dom):
            flag2 = True
    if not flag1 or not flag2:
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    elif recipient == sender:
        return "Нельзя отправить письмо самому себе!"
    elif sender == "university.help@gmail.com":
        return f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        return f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}"

print(send_email('Privet!', 'rare_avis@ukr.net', "cheef@mail.ru"))


