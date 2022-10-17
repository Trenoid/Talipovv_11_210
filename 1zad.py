message = input("Введите сообщение") + "I"
count = 1
simvol = ""
vivodmessage = ""


while message != "quitI":

    for i in range(len(message)-1):
        if message[i] == message[i+1]:
            count += 1
            simvol = message[i]
        if message[i] != message[i+1]:
            if count == 1:
                vivodmessage += message[i]
            if count > 1:
                vivodmessage += simvol + str(count)
            count = 1


    print(vivodmessage)
    vivodmessage = ""
    message = input("Введите сообщение") + "I"
