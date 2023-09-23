class Funk():
    def __init__(self):
        self.male_female_stat = 3.46
        self.heart_axis= {"NaN", 'ALAD', 'AXR', 'RAD', 'MID', 'SAG', 'ARAD', 'AXL', 'LAD'}
        self.stadium = {'Stadium II', 'Stadium III', 'Stadium I-II', 'Stadium I', 'Stadium II-III'}
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
    def sex(self,sex):
        if int(sex) == 1:
            return 1
        return 1/self.male_female_stat
    def age(self,age):
        return age/100
    def imt(self,weight,height):
        n_height = height/100
        imt = weight/n_height**2
        if imt <= 18:
            return 0.25
        elif 18 < imt <= 24:
            return 0.5
        if 24 < imt <= 30:
            return 0.75
        return 1
    def dependence_stadium(self,stad1,stad2):
        if stad1 in self.stadium and stad2 in self.stadium:
            return 1
        return 0
    def validated_by_human(self,validated_by_human):
        if validated_by_human == True:
            return 1
        return 0
    def pacemaker(self,pacemaker):
        if pacemaker != 'nan':
            return 0
        return 1


