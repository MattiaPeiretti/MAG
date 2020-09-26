import constants
import api
import gui as GUI

class MAG:
    def __init__(self):
        imageRetriever = api.ImageRetriever('')
        gui = GUI.MAG_GUI()
        gui.mainloop()
        print(imageRetriever.set_query('curiosity', 1099))
        imageRetriever.run()
        print(imageRetriever.images())

def main():
    mag = MAG()


if __name__ == '__main__':
    main()