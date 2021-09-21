# import datetime
# "dados/" + type + "/" + type + "_" + datetime.datetime.now().strftime('%m_%d_%Y__%H_%M_%S') + ".txt"
class Database:
    def __init__(self, type_name, info):
        file_name = "dados/" + type_name + "/" + type_name + ".txt"
        file = open(file_name, 'w', encoding='utf8')
        file.write(str(info)+"\n")
        file.close()
