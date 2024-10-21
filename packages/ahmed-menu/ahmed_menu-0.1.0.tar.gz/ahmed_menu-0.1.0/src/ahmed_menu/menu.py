def menu(**kwargs):
    """Returns the func value associated with the key in dict.
    if key is not available in the dict, the user is again prompted."""
    output = dict(kwargs)
    while True:
        user_key = input("choose your key: ")
        try:
            return output[user_key]()

        except KeyError as e:
            print(f"{e} not found ")



