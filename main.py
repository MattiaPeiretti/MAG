import constants
import api

class MAG:
    def __init__(self):
        imageRetriever = api.ImageRetriever('')
        print(imageRetriever.set_query('curiosity', 1099))
        imageRetriever.run()

def main():
    mag = MAG()


if __name__ == '__main__':
    main()