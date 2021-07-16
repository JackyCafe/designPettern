from decorator_pattern import Person


class Engineer(Person):
    def __init__(self, name, skill):
        super(Engineer, self).__init__(name)
        self._skill = skill

    def getSkill(self):
        return self._skill

    def wear(self):
        print(f"我是 {self.getSkill()} 工程師 {self._name}" ,end=",")
        super(Engineer, self).wear()


class Teacher(Person):
    def __init__(self, name,title):
        super(Teacher, self).__init__(name)
        self._title = title

    def getTitle(self):
        return self._title

    def wear(self):
        print(f"我是 {self._name} {self.getSkill()} ", end=",")
        super(Teacher, self).wear()
