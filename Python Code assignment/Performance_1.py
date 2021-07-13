"""
This is a simple program that will collect votes for certain candidates and calculate which candidate 
has colected the most votes
"""
#assigning variable names
minnie_votes, donald_votes, mickey_votes, goofy_votes = 0, 0, 0, 0

#Main loop for getting use input
while True:
    print ("The presidential candidates are:\n","1. Mickey Mouse\n","2. Donald Duck\n","3. Minnie Mouse\n","4. Goofy\n","Type 0 to quit")
    v=int(input("Vote? "))
    #Add to the correct tally based on the user input
    if v == 0:
        break
    elif v == 1:
        mickey_votes += 1
    elif v == 2:
        donald_votes += 1
    elif v == 3:
        minnie_votes += 1
    elif v == 4:
        goofy_votes += 1
    else:
        print ("invalid")

#Figures out which candidate has won based on the tallied votes
total_votes=mickey_votes+donald_votes+minnie_votes+goofy_votes
print(total_votes)
if mickey_votes>donald_votes and mickey_votes>minnie_votes and mickey_votes>goofy_votes:
    print("Mickey Mouse wins!")
    print(mickey_votes/total_votes*100,"% of the votes")
elif donald_votes>minnie_votes and donald_votes>goofy_votes and donald_votes>mickey_votes:
    print("Donald Duck wins!")
    print(donald_votes/total_votes*100,"% of the votes")
elif minnie_votes>goofy_votes and minnie_votes>mickey_votes and minnie_votes>donald_votes:
    print("Minnie Mouse wins!")
    print(minnie_votes/total_votes*100,"% of the votes")
elif goofy_votes>mickey_votes and goofy_votes>minnie_votes and goofy_votes>donald_votes:
    print("Goofy wins!")
    print(goofy_votes/total_votes*100,"% of the votes")
else:
    print("There was a tie!")
    print(f"There was a total {total_votes} votes, with {mickey_votes} votes for Micky, {donald_votes} votes for Donald, {minnie_votes} votes for Minnie, and {goofy_votes} votes for goofy" )