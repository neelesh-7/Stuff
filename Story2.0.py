print('This is a game')
print('The rules are simple')
print('I say something')
print('And you respond with watever i tell you to respond with to pick your option')
print('Got it?')
answer = raw_input('y or n: ')

if answer == 'n':
 	print('This is a game')
 	print('The rules are simple')
 	print('I say something')
 	print('And you respond with whatever i tell you to respond with to pick your option')
 	print('Got it?')
 	answer = input('y or n: ')

 	if answer == 'n':
 		print('you are trolling, please restart and actually answer.')

        if answer == 'y':
 	        print('great, im glad you understand, now onto the game')

 #choose character
print('now that you are ready to play, please choose your character')
print('you get 3 options')
print('1=fighter 2=thief 3=wizard')
print('fighter has the most health and the best normal attacks but no special abilities')
print('theif has low health good regular attacks and the SNEAKY special ability')
print('wizard has low health and low regular attacks but limited uses of some powerfull spells')

kit = input('choose 1 2 or 3: ')

if kit == '1':
    print('you have selected fighter')
print('you have 50 health')
hp = 50
print('your attacks to 5 damage')
attack = 5
print('you dont have any special abilities')

if kit == '2':
 	print('you have selected theif')
print('you have 35 health')
hp = 35
print('your attacks do 3 damage')
attack = 3
print('you have sneaking abilities')
print('this means there is a chance enemies wont see you')

if kit == '3':
 	print('you have selected wizard')
 	print('you have 25 health')
 	hp = 25
 	print('your attacks do 2 damage')
 	attack = 2
 	print('you have spellcasting abilities')
 	spells = '5'
 	print('your can cast spells 5 times')
 	print('your first spell heals you for 7 health')
 	print('your second spell damages enemies for 15')
 	print('your third spell protects you when resting at checkpoints')
 #game start
print('you start your adventure in a dungeon')
print('you have no memory of how you got there')
print('but all you have on you is your walking stick')
print('the ground feels like a damp sand')
print('and you feel quite thirst and hungry')
print('you notice the cave has two exits')
print('you can hear the sound of rushing water coming from one')
print('1=towards the sound of water 2=away')

path = input('Choose 1 or 2: ')

if path == 1:
 	print('you head towards the sound of water')
 	print('as you aproach you begin to smell smoke and fire')
 	print('that must be a great sign you think')
 	print('a fire usually means people and they might be able to help you')
 	print('once you get close though you realize this fire belongs to no people, it was made by 3 goblins')
 	print('the goblins start coming at you and you know your only option is to fight')
 	print('attack does damage to your enemy')
 	print('spell does damage to your enemy')
 	print('heal restores your health')
 	print('flee gives you a chance of escaping but is only available sometimes')
 	print("sometimes you wont get to choose at all because the developer was lazy; er um i mean uhhhh...")
 	print('time for combat')

 	print("you lunge out and smack the first goblin with your staff")
 	print("the goblin recoils and it and the rest of the goblins run off")

 	print("you still dont know the way out but at least you have a place to rest for the night")

 	print("you wake up to a bright light in your face")
 	print("its the sun streaming down on your face as you find yourself in you bed and realize it was all a dream")

if path == "2":
 	print("you walk through this path")
 	print("you now have to choose another path")
 	input("choose another path, either 1 or 2: ")

 	if path == "1":
 		print("you find the treasure of ultimate derp jaimil nice cut g you have officialy won")

 	if path == "2":
 		print("you had the option to win an amazing price, but instead you will be forced to watch pepa pig forever, sucks to be you loser")