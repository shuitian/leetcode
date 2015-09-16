#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
class Solution {
public:
	int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
       	int number = gas.size() ;
       	int i =0;
       	int sum = 0;
       	int j =0;
       	int k = number-1;
       	while(j <= k)
       	{
	       	sum = sum+gas[j] - cost[j];
	       	j = j+1;
			while (sum<0 && j <= k)
			{
	       		sum = sum + gas[k] - cost[k];
	       		k = k -1;
	       	}
	   	}
       	if (sum<0)
       	{
       		return -1;
		}else {
			return (k+1)%number;
       	}
	}
};

int main()
{
	Solution s;
while(true)
{
	std::vector<int> gas;
	std::vector<int> cost;
	int c, g, n, t;
	cin>>t;
	cout<<t<<endl;
	for (int i = 0; i < t; ++i)
	{
		scanf("%d%d",&g, &c);
		gas.push_back(g);
		cost.push_back(c);
	}
	cout<<s.canCompleteCircuit(gas, cost);
}
}