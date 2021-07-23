from random import randrange


from src import animal

def main():
    #Make these animals anything you want!
    animals = [animal.Animal('cow', 'data/cow.wav', 'data/cow.png'),
               animal.Animal('cow', 'data/cow.wav', 'data/cow.png'),
               animal.Animal('cow', 'data/cow.wav', 'data/cow.png')]
    for i in range(3):
        random_animal = animals[randrange(len(animals))]
        see_and_say(random_animal)

def see_and_say(random_animal):
    #See introduction video for description of these methods
    random_animal.see()
    random_animal.say()

if __name__ == '__main__':
    main()
