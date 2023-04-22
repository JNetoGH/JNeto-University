import os


class TxtFileManager:

    @staticmethod
    def create(file_name: str):
        file = open(TxtFileManager.addDotTxtIfMissing(file_name), "x")
        file.close()

    @staticmethod
    def write(file_name: str, text: str):
        file = open(TxtFileManager.addDotTxtIfMissing(file_name), "w")
        file.write(text)
        file.close()

    @staticmethod
    def copy(file_copied_name: str, file_target_name: str):
        read = open(TxtFileManager.addDotTxtIfMissing(file_copied_name))
        text = read.read()
        TxtFileManager.write(f"{file_target_name}.txt", str(text))

    @staticmethod
    def delete(file_name: str):
        os.remove(TxtFileManager.addDotTxtIfMissing(file_name))

    @staticmethod
    def addDotTxtIfMissing(file_name: str) -> str:
        t2 = file_name[-1]
        x = file_name[-2]
        t1 = file_name[-3]
        if not (t2 == "t" == t1 and x == "x"):
            return f"{file_name}.txt"
        else:
            return file_name


TxtFileManager.create("adioasjdiasdj")