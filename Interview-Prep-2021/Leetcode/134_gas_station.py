# LINK: https://leetcode.com/problems/gas-station/

class Solution(object):
  def canCompleteCircuit(self, gas, cost):
    # Approach 1: Used ChatGPT and used the GPT solution.

    # TC: O(N)
    # SC: O(1)

    # NOTE: The key point is that: you can only form a cycle when the sum of all the values in [gas]
    # is greater than or equal to the sum of all the values in [cost]. Given that in the for-loop() 
    # the computation is 'total_gas += gas[i]-cost[i]', the computation that we have to therefore check
    # in the final return statement is 'total_gas >= 0'.

    # Setting the variables.
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
      # the station and set current_gas = 0.
      if current_gas < 0:
        station = i+1
        current_gas = 0

    # If the total_gas is non-negative once you reach the end, you've created a cycle
    # and you can return station. Else return -1.
    return station if total_gas >= 0 else -1

foo = Solution();
print(foo.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]));