class Solution(object):
  def isWinner(self, player1, player2):
    # Loop through the array calculating the score of player1.
    # - Have a score variable.
    # - For each number, check if the previous two are 10 or greater.
    # - If so, double the number and add it to the score variable.
    # - Else, just add the number to the score variable. 

    # Loop through the array calculating the score of player2. 

    # Write some if-statement logic to calculate who was the winner.

    # TC (Guess): O(N)
    # SC (Guess): O(1)

    scoreP1 = 0
    scoreP2 = 0

    for i in range(len(player1)):
      # Calculating the score for Player1.
      if (i-1 >= 0 and player1[i-1] >= 10) or (i-2 >= 0 and player1[i-2] >= 10):
        scoreP1 += 2*player1[i]
      else:
        scoreP1 += player1[i]
    
      # Calculating the score for Player2.
      if (i-1 >= 0 and player2[i-1] >= 10) or (i-2 >= 0 and player2[i-2] >= 10):
        scoreP2 += 2*player2[i]
      else:
        scoreP2 += player2[i]
      
    # Return the score.
    if scoreP1 > scoreP2:
      return 1
    elif scoreP2 > scoreP1:
      return 2

    return 0

foo = Solution();
print(foo.isWinner([3,5,7,6], [8,10,10,2]));