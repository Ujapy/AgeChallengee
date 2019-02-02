from sys import exit
from random import randint
from textwrap import dedent
from sys import argv
"""script, AgeGroupTxt = argv
msg = open(AgeGroupTxt)
print(msg.read())
msg.close()"""
print("Remeber to press the 'enter key' on ur keyboard after each input. Thanks")
#Get user name
user_name = input("Player's Name: ")
#Capitalize the first letter of the name
user_name = user_name.capitalize()
if user_name.lower() == 'exit':
#exit if the input is 'exit'
    print("*********Goodbye!***********")
    exit()
class Stages(object):
    def enter(self):
        print(dedent("""
                    Due to alien inversion, we are taking necessary precaution
                    on the development of this scene"""))
        exit(1)

class Engine(object):
    def __init__(self, stage_map):
        self.stage_map = stage_map

    def play(self):
        current_stage = self.stage_map.opening_stage()
        last_scene = self.stage_map.next_stage('end')

        while current_stage != last_scene:
            next_stage_name = current_stage.enter()
            current_stage = self.stage_map.next_stage(next_stage_name)
            #current_stage.enter()
        


class Demote(Stages):

    lesson = [
            "You can't cheat nature",
            "There are better way to scale through this",
            "This choice can lead to an early grave",
            "Hmmm! Are you sure this is the right approach?",
            "Certain decisions are sucidial"]
            #random msg u get when an input is beyond the program scope

    def enter(self):
        print(Demote.lesson[randint(0, len(self.lesson)-1)], user_name)
        #print random  lesson 
        print(dedent("""To return to previous stage enter the appropriate stage Letter
                    C = Children stage
                    T = Teenage stage
                    A = Adult stage
                    E = Exit
                """))
        stage_entry = input(" Stage:")
        stage_entry.capitalize()
        #Takes u back to a stage(Class) in the program
        if stage_entry == "c":
            return 'child'
        elif stage_entry =="t":
            return 'teenager'
        elif stage_entry =="a":
            return 'adult'
        elif stage_entry == "e":
            exit()
        else:
            print("That's not a stage letter")
            return 'demote'

class Child(Stages):
    def enter(self):
        print(dedent("""
                %r, Welcome to the child section. This Stage is centered on child behaviors
                i.e children aged 4-12.
                    """)% user_name)
        print(dedent("""
                        Choose three(3) good behavior from the options lettered A-E \n
                        Remember %s, to enter only the alphabet that correspond to your
                        choice of good behavior
                        """ %user_name))

        behaviors = {
                    'A':'I respect my elders and others',
                    'B':'I like watching television all day',
                    'C':"I apologise when i'm wrong",
                    'D':'I leave house chores to the girls',
                    'E':'I do my homework',
                        }
        #Dictionary of behaviors to choose from
        for k,v in behaviors.items():
            print(k,v)
        #Print the key and value  pair in the dictionary(behaviors)

        answers = ['A','C', 'E']
        #The correct answers to the options in behaviors
        choosen_answer = []
        #The reply the user chooses will be appended here
        reply = input("Good behavior: ")
        #Prompt the user to choose a good behavior 
        reply = reply.capitalize()
        #Capitalize the input(reply)
        choosen_answer.append(reply)
        #Append the reply to the empty list(Choosen_answer)
        if reply.lower() =='exit':
        #This help to exit the program
            print("**************GoodBye!**************************")
            exit()
        while reply in answers:
            reply = input("\n Another good behavior: ")
            reply = reply.capitalize()
        #If the first reply is among the list(answer), continue  and capitalize each input
            if reply in choosen_answer:
            #This make sure u don't select thesame option twice
                print("\nYou can't select '%s' twice\n"%reply)
            else:
                choosen_answer.append(reply)
            #If the input is not among the already selected option, append to list(choosen_answer)
                if sorted(choosen_answer) == sorted(answers):
                #Sorted the list(choosen_reply) to match with the list(answer)
                    print("Good work")
                    print("You have selected the options")

                    for i in choosen_answer:
                        print(i,'\n')
                    print("A = ",behaviors['A'],"\n", "C = ", behaviors['C'], "\n", "E = ", behaviors['E'])
                    #Print the correct answer
                    print("These are really good behaviors for a child")
                    return 'teenager'
                    #Move to the next stage(Teenage Class)
        while reply in behaviors and reply not in answers:
        #return to child (Begin again) if input is in the options but not the real answer
            print("\nThe option %s is not a good behavior.\n Try again\n"%reply)
            return 'child'
        while reply not in behaviors: #Demote u if the input is outside the scope of the behaviors
            print("Haba! That's not among the available options")
            return 'demote'



class Teenager(Stages):

    def enter(self):
        print("\n","#     "*12,"\n")
        print("%s, Welcome to 'Tennage' stage. Hope u learnt something from the Children section?" %user_name)
        print(dedent("""
                Teenagers face real problems on a daily basis
                during the most awkward growth stages of their lives;
                between 13 and 19-years-old. During this time,
                teens are exposed to some overwhelming external and internal struggles.
                Some of these are:
        """))

        t_challenges = dedent(("""
                        -Self-Esteem and Body Image
                        -Stress
                        -Bullying
                        -Depression
                        -Cyber Addiction
                        -Drinking and Smoking
                        -Underage Sex
                        -Child Abuse
                        -Peer-Pressure and Competition
                        -Eating Disorders\n
                    """))
        print(t_challenges)
        print("*"*7)
        print(dedent("""
                From the options below,
                choose 4 ways u can help Teenagers overcome these struggles \n """))
        t_overcome = {
            'A':'Challenges are normal so leave them alone',
            'B':'Spend quality time with them',
            'C':'Engage them in honest and open communication',
            'D':'Shower wealth on them',
            'E':'Enforce appropriate disciplinary measures if need be',
            'F':"Maybe it's time for them to be on their own",
            'G':'Understand the cause of the struggles\n'
            }
        for k,v in t_overcome.items():
            print(k,v)

        answers= ['B','C','E','G']
        choosen_answer =[]

        reply = input("Ways to overcome: ")
        reply = reply.capitalize()
        choosen_answer.append(reply)
        if reply.lower() =='exit':
            print("**************GoodBye!**************************")
            exit()
        while reply in answers:
            reply = input("\n Another way: ")
            reply = reply.capitalize()

            if reply in choosen_answer:
                print("\nYou can't select '%s' twice\n"%reply)
            else:
                choosen_answer.append(reply)
                if sorted(choosen_answer) == sorted(answers):
                    print("Good work")
                    print("You have selected the options")

                    for i in choosen_answer:
                        print(i,'\n')
                    print("B = ",t_overcome['B'],"\n", "C = ", t_overcome['C'], "\n", "E = ", t_overcome['E'], "\n" "G = ", t_overcome['G'])
                    print("Wow! Parenting is going to be a very task for u. Welldone!")
                    return 'adult'

        while reply in t_overcome and reply not in answers:
            print("\nThe option %s is not a good behavior.\n Try again\n"%reply)
            return 'teenager'
        while reply not in t_overcome:
            print("Haba! That's not among the available options")
            return 'demote'


class Adult(Stages):

    def enter(self):
        print("\n************Adult Section***********\n")
        print(dedent("""
                Congratulations %s, you made it to the last section of the game.\n
                As it was once written: When I was a child, I talked like a child,
                I thought like a child, I reasoned like a child.
                When I became a man, I put childish ways behind me.

                This means there are certain attributes or qualities
                an adult is suppose to possess.

                Select five of these qualities from the option below:

                """ %user_name))

        adult_qualities = {
            'A':'You take responsibility for yourself',
            'B':'Employ the principle of "An eye for an eye"',
            'C':"If two wrong deeds doesn't make it right, try three",
            'D':'Proper money management',
            'E':'Self centeredness',
            'F':'Accepts correctional criticism',
            'G':'Open mindedness',
            'H':'Proper anger management',
            'I':'Confidence',
            'J':'Being Judgemental'
                }
        for k,v in adult_qualities.items():
            print(k,v)

        answers = ['A','D', 'F', 'G','H','I',]
        choosen_answers = []
        reply = input("Option: ")
        reply = reply.capitalize()
        choosen_answers.append(reply)
        if reply.lower() =='exit':
            exit()
        while reply in answers:
            reply = input("\nAnother Option:")
            reply = reply.capitalize()
            if reply in choosen_answers:
                print("\nSorry, you've selected '%s' already. Try another option\n" %reply)
            else:
                choosen_answers.append(reply)
                if sorted(choosen_answers) == sorted(answers):
                    print("\nYou've selected the options:\n")

                    for i in choosen_answers:
                        print(i)
                    print(
                        "\n",
                        'A = ', adult_qualities['A'],"\n" 'D = ', adult_qualities['D'],"\n"
                        'F = ', adult_qualities['F'],"\n" 'G = ', adult_qualities['G'],"\n"
                        'H = ', adult_qualities['H'],"\n" 'I = ', adult_qualities['I'],
                        "\n")
                    return 'finished'

        while reply in adult_qualities and reply not in  answers:
            print("\nThe option '%s' is not among the available options\n"%reply)
            return 'adult'

        while reply not in adult_qualities:
            return 'demote'

class Finished(Stages):
    def enter(self):
        print(dedent("""
                ogbenee! Senior! Almighty %s
                A big congratulations %s, you successfully completed this game.
                """)% (user_name, user_name))

class Map(object):
    stages = {
        'teenager':Teenager(),
        'child':Child(),
        'demote':Demote(),
        'adult':Adult(),
        'finished':Finished()
        }
    
    def __init__(self, start_stage):
        self.start_stage = start_stage

    def next_stage(self, stage_name):
        val = Map.stages.get(stage_name)
        return val

    def opening_stage(self):
        return self.next_stage(self.start_stage)

a_map = Map('child')
a_game = Engine(a_map)
a_game.play()