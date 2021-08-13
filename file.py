import datetime

class Database:
    def __init__(self, type, info):

        namefile = "dados/" + type + "/" + type + "_" + datetime.datetime.now().strftime('%m_%d_%Y__%H_%M_%S') + ".txt"
        file = open(namefile, 'w', encoding='utf8')
        file.write(str(info)+"\n")
        file.close()

