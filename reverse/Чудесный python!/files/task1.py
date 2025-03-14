import base64

def check_password(password):
    encoded_secret = b'TkFJVENURntINGNrX1MwXzN6fQ=='
    secret = base64.b64decode(encoded_secret).decode()
    if password == secret:
        return 'Flag Correct!'
    return 'Wrong! Try one more...'
if __name__ == '__main__':
    user_input = input('Write Flag: ')
    result = check_password(user_input)
    print(result)