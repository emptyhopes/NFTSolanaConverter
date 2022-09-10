import base58

from Config.Config import Config

class Decode:
    bytes = base58.b58decode(Config.PrivateKey)
    length = len(bytes) - 1
    values = map(lambda byte: str(byte), bytes)

    def __main__ () :
        Decode.Algorithm()

    def Algorithm () :

        PublicKey = ""

        for index, value in enumerate(Decode.values):

            if index == 0:
                PublicKey = "[" + PublicKey + value

            if index != 0 and index != Decode.length:
                PublicKey = PublicKey + "," + value

            if index == Decode.length:
                PublicKey = PublicKey + "," + value + "]"

        print(PublicKey)

            