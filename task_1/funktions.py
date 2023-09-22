class Funk():
    def __init__(self):
        self.stadium = {'unknown', "nan", 'Stadium II', 'Stadium III', 'Stadium I-II', 'Stadium I', 'Stadium II-III'}
    def infarction_stadium(self,stadium):
        if stadium == "unknown" or stadium == "nan":
            return 0
        elif stadium == "Stadium I":
            return 0.2
        elif stadium == 'Stadium I-II':
            return 0.4
        elif stadium == 'Stadium II':
            return 0.6
        elif stadium == 'Stadium II-III':
            return 0.8
        return 1
