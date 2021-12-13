class MemberVO:
    def __init__(self,id,pwd,name):
        self.id = id
        self.pwd = pwd
        self.name = name

    def __str__(self):
        return '{0} {1} {2}'.format(self.id, self.pwd, self.name)

    pass

