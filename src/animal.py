from playsound import playsound
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



class Animal:

  def __init__(self, name, sound, pic):
    self.name = name
    self.sound = sound
    self.pic = pic

  def see(self):
    img = mpimg.imread(self.pic)
    plt.imshow(img)

  def say(self):
    playsound(self.sound)