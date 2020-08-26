// Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

// Example 1:

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.
// Example 2:

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.
// Accepted

#include "stdio.h"
#include <math.h>
#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
private:
	std::map<int, int> valueMap;
	
public:
	int time = 0;
    int numSquares(int n) {
    	std::vector<int> v(n + 1, n + 1);

    	v[0] = 0;
    	v[1] = 1;
    	for (int i = 1; i <= (int)sqrt((double)n); ++i)
    	{
    		int squre = i * i;
    		for (int j = squre; j <= n; ++j)
    		{
    			time ++;
    			v[j] = min(v[j - squre] + 1, v[j]);
    		}
    	}
        return v[n];
    }
};

int main(int argc, char const *argv[])
{
	
	// printf("%d\n", s.numSquares(12));
	for (int i = 0; i < 100; ++i)
	{
		// s.time = 0;
		Solution s;
		std::cout<<s.time<<" "<<i<<" : "<<s.numSquares(i)<<std::endl;
	}
	return 0;
}