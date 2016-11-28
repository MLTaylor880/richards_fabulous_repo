from pets.pets import Pet

if __name__ == '__main__':
    print 'This is the story of my pet!'
    spritz = Pet('Spritz', 'cat')
    print 'My pet is %s, a very happy %s' % (spritz.name, spritz.type)
    spritz.wants_to_play()
    spritz.wants_to_eat()
    print 'Oh no! We should feed and play with %s!' % spritz.name
    amount_to_feed = raw_input('How many times do you want to feed %s? ' % spritz.name)
    for x in range(0, int(amount_to_feed)):
        spritz.feed()
    amount_to_play = raw_input('How many times do you want to play with %s? ' % spritz.name)
    for x in range(0, int(amount_to_play)):
        spritz.play()
    print 'How is %s doing now?' % spritz.name
    spritz.wants_to_play()
    spritz.wants_to_eat()
    print 'Bye %s, you have been an awesome %s!' % (spritz.name, spritz.type)
