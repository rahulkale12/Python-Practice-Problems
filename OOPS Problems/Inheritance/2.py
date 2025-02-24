#2.Create a Teacher class with teach() method and Researcher class with research(). Create a Professor class that inherits from both.


class Teacher:
    def teach(self):
        print("Teaching students...")

class Researcher:
    def research(self):
        print("Conducting research...")

class Professor(Teacher, Researcher):        #mutiple inheritance
    def guide(self):
        print("Guiding students in research...")


prof = Professor()
prof.teach()
prof.research()
prof.guide()
