'''implement a class called player that represents a cricket player.The player should have a 
method called play() which prints"The player is playing cricket".Derive two classes,batsman and
bowler,from the player class.Override the play() method in each derived class to print "the batsman 
is batting"and "The bowler is bowling",respectively.Write a program to create objects of both the
batsman and bowler classes and call the play()method for each object.'''


# define the base class player
class player:
  def play(self):
    printf("the player is playing cricket.")
    
#define the derived class batsman
class batsman(player):
  def play(self):
    printf("the batsman is battinng.")
    
#define the derived class bowler
class bowler(player):
def play(Self):
  printf("the bowler is bowling.")

#create objects of batsman and bowler class
batsman=batsman()
bowler=bowler()

#call the play() method for each object
batsman.play()
bowler.play()





  