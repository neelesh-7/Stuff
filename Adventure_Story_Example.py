#python Adventure_Story_Example.py
print ("John was walking down the path when he saw a")
x = raw_input("What did he see? (a dog, his friends, or his teacher): ")


if x == "a dog":
   print ("He saw a huge Dog, Immediatley, because of his fear, he started running the other way towards the woods. In the woods he found a tree, which he thought he could climb, so he decided to give it a try")

   z= input("What did he do? (climb the tree), (continue running), (or run back to see if the dog was gone): ")

   if z == "climb the tree":
       print ("John climbed the tree with pace, and sat up there for a while and his phone nearly died, until he got a call from an unkown caller")
       y= input("does he pick up the phone?: ")
       if y == "yes":
         print ("its his parents, and they tell him to return home")
       elif y == "no":
         print ("He doesnt pick up the phone so he spends the night in the tree and returns home in the morning before school")

   elif  z == "continue running":
       print ("He continued running until he got deep into the woods. He appeared to have lost his way, and his phone was about to die.")
       b = input ("He gets lost so what does he do?: (run around to find a way out) or (stay there): ") 
       if b== "run around to find a way out":
           print ("He luckily manages to find his way out and returns home")
       elif b== "stay there":
           print ("He stays there so he spends the night in the woods and returns home in the morning before school")

   elif z == "He ran back to see if the dog was gone":
       print ("John, after building up some courage, he ran back to check if the dog had gone, after checking for another couple minutes he makes a run for it an returns home")



elif x == "his teacher":
   print("He saw his teacher. He turned around immediatley and headed back towards home. He makes it home and goes out later with his friends. ")
