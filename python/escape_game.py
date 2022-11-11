#Escape game
print('''
            _      ()              ()      _
           / \     ||______________||     / \
          /___\    |                |    /___\
            |      |      ~@@~      |      |
           (_)     |_______  _______|     (_)
        ___/_\___  {_______}{_______}  ___/_\___
         |__~__|   %%%%%%%%%%%%%%%%%%   |__~__|
      ___|_____|__%%%%%%%%%%%%%%%%%%%%__|_____|___
         |     | %%%%%%%%%%%%%%%%%%%%%% |     |
          `=====%%%%%%%%%%%%%%%%%%%%%%%%=====`
         `=====%%%%%%%%%%%%%%%%%%%%%%%%%%=====`
        `=====%%%%%%%%%%%%%%%%%%%%%%%%%%%%=====`
       `=====/||||||||||||||||||||||||||||\=====`
      `======||||||||||||||||||||||||||||||======`
     `=======|||||||||||||||||||||||||||lc|=======`
    `==============================================`
   `================================================`
  `==================================================`
 `====================================================`
''')


print("Welcome to the escape room!\n")
print("Your goal is to make the right decisions and leave this place!\n")

choice1 = input('You\'re on your bed and you need to leave.Which side you wanna take? Type "left" or "right" ').lower()

if choice1 == 'left':
    choice2 = input('You\'ve left the bed.  Type "lantern" to look for a lanter or type "door" to try to find the door. ').lower()
    if choice2 == 'lantern':
        choice3 = input('You found the lantern. After lighting up the lantern you found a monster.What you gonna do?\nType "run" to run around the bedroom.\nType "fight" to try to win the fight.\nType "find" to look for the closest door. ').lower()
        if choice3 == 'fight':
            print("Congratulations! You killed the monster. You got back to your family again.")
        else:
            print("You'are dead. Game Over!")
    else:
        print("You'are dead. Game Over!") 
else:
    print("You'are dead. Game Over!")    
