class ClassScore:
    def __init__(self):
        self.name = ''
        self.studentNo = ''
        self.Korean = 0
        self.English = 0
        self.Math = 0

    def Clear(self):
        self.name = ''
        self.studentNo = ''
        self.Korean = 0
        self.English = 0
        self.Math = 0

class Main:
    def __init__(self):
        self.scoreDict = {}
        self.classScore = ClassScore()

    def main(self):
        self.classScore.name = 'Iron-man'
        self.classScore.studentNo = '2342524'
        self.classScore.Korean = 93
        self.classScore.English = 87
        self.classScore.Math = 98

        self.scoreDict[('Iron-Man', '2342524')] = self.classScore

        self.classScore.Clear()

        self.classScore.name = 'Thor'
        self.classScore.studentNo = '2342525'
        self.classScore.Korean = 76
        self.classScore.English = 65
        self.classScore.Math = 44

        self.scoreDict[('Thor', '2342525')] = self.classScore

        print('Iron-Man Korean Score : {}'.format(self.scoreDict[('Iron-Man', '2342524')].Korean))
        print('Thor Math Score : {}'.format(self.scoreDict[('Thor', '2342525')].Math))


if __name__ == "__main__":
    main = Main()
    main.main()