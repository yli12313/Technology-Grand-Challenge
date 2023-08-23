# LINK: https://leetcode.com/problems/gas-station/

class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    # Approach 1: Used ChatGPT and used the GPT solution.

    # TC: O(N)
    # SC: O(1)

    # NOTE: The key point is that: you can only form a cycle when the sum of all the values in [gas]
    # is greater than or equal to the sum of all the values in [cost]. Given that in the for() loop 
    # the computation is 'total_gas += gas[i]-cost[i]', we therefore know that the computation in the 
    # final return statement is 'total_gas >= 0'.

    # Setting the variables. When you set the problem up, you have to start with:
    #   1) total_gas
    #   2) current_gas
    #   3) station
    total_gas = 0
    current_gas = 0
    station = 0
    
    # Looping through the gas stations.
    for i in range(len(gas)):
      # Calculating the total gas that's in the car.
      total_gas += gas[i]-cost[i]

      # Calculating the current gas that the car gets at the current gas station.
      current_gas += gas[i]-cost[i]

      # If you can't get to the next station from the current station, then reset
      # the station 'station=i+1' and set 'current_gas = 0'.
      if current_gas < 0:
        station = i+1
        current_gas = 0

    # If the total_gas is non-negative once you reach the end, you've created a cycle
    # and you can return station. Else return -1. Moreover, the return statment here is of
    # the form: return (exp if exp else exp)

    # The return statement's key trick is the following part: 'total_gas >= 0'
    return station if total_gas >= 0 else -1

foo = Solution();
print(foo.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]));
