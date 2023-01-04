# TODO - Function description
def replaceUserNameInMessage(message: str, textToReplace:str, userName: str):
    if not isinstance(message, str) or not isinstance(textToReplace, str) or not isinstance(userName, str):
        raise TypeError("Input must be a string.")
    return message.replace(textToReplace, userName)