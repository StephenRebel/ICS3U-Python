"""
This is a simple program that will collect votes for certain candidates and calculates which candidate 
has colected the most votes, or if a tie has occured
"""
class ValueOutOfRange(Exception):
  pass

#assigning variable names
votes = [0,0,0,0]

#function to sort through tie cases
def tie_cases(votes):
    tie_case = []
    for x in range(len(votes)):
        if votes[x] == max(votes):
            if x == 0:
                tie_case.append("Mickey Mouse")
            if x == 1:
                tie_case.append("Donald Duck")
            if x == 2:
                tie_case.append("Minnie Mouse")
            if x == 3:
                tie_case.append("Goofy")
    return(tie_case)

#Main loop for getting use input
while True:
    #Try except with custom exception to avid unwanted input
    try:
        print ("\nThe presidential candidates are:\n1. Mickey Mouse\n2. Donald Duck\n3. Minnie Mouse\n4. Goofy\nType 0 to quit")
        v=int(input("Vote? "))
        if v >= 0 and v <= 4:
            if v == 0:
                break
            else:
                votes[v-1] += 1
        else:
            print ("invalid")
            raise ValueOutOfRange
    
    except ValueOutOfRange:
        print("This value is not within acceptable range")
    
    except ValueError:
        print("This is not an acceptable input")

#Figures out which candidate has won based on the tallied votes
total_votes = sum(votes)
print(f"The total number of votes was: {total_votes}")
winner = votes.index(max(votes))
tie = votes.count(max(votes))
if tie > 1:
    winner = 5

#Outputs the oncluding winner or tir message
if total_votes == 0:
    print(f"There were {total_votes} votes, therefore no one won this election!")
elif winner == 0:
    print("Mickey Mouse wins!")
    print(round(votes[0]/total_votes*100, 2),"% of the votes")
elif winner == 1:
    print("Donald Duck wins!")
    print(round(votes[1]/total_votes*100, 2),"% of the votes")
elif winner == 2:
    print("Minnie Mouse wins!")
    print(round(votes[2]/total_votes*100, 2),"% of the votes")
elif winner == 3:
    print("Goofy wins!")
    print(round(votes[3]/total_votes*100, 2),"% of the votes")
else:
    #Determins who the tie was between and prints their names
    print("There was a tie!")
    tie_case = tie_cases(votes)
    print(f"The tie was between candidates {tie_case}")