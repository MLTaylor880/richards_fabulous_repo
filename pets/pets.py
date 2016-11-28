class Pet(object):

    def __init__(self, name, type, gender='Male'):
        self.name = name
        self.type = type
        self.gender = gender
        self.hunger = 0
        self.boredom = 10

    def feed(self):
        if self.hunger < 5:
            print '%s eats some food!' % self.name
            self.hunger += 1
        else:
            print '%s knocks your food on the ground.' % self.name

    def play(self):
        if self.boredom > 6:
            print '%s runs around like a maniac!' % self.name
            self.boredom -= 1
        else:
            print '%s just stares at you.' % self.name

    def wants_to_play(self):
        if self.boredom >= 6:
            print 'Your pet %s is really bored! You should play with it more!' % self.name
        else:
            print 'Your pet %s just wants to sleep. Leave it alone!' % self.name

    def wants_to_eat(self):
        if self.hunger < 3:
            print 'Your pet %s is pretty hungry. You should feed it!' % self.name
        else:
            print 'Your pet %s doesn\'t need to eat right now.' % self.name
