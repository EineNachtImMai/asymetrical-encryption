def RSAencode(message: str, n: int, c: int) -> str:
    encoded_message = []
    for character in message:
        clear = ord(character)
        encoded = (clear ** c) % n
        encoded_message.append(str(encoded))
    final_encoded = " ".join(encoded_message)
    return(final_encoded)


def RSAdecode(message: str, n: int, d: int) -> str:
    decoded_message = []
    message_list = message.split()
    for character in message_list:
        encoded = int(character)
        encoded = (encoded ** d) % n
        clear = chr(encoded)
        decoded_message.append(clear)
    final_decoded = "".join(decoded_message)
    return(final_decoded)


if __name__ == '__main__':
    print(RSAencode(input("what message do you want to encode?"), 86147, 85541))
    print(RSAdecode(input("what message do you want to decode?"), 86147, 58541))
