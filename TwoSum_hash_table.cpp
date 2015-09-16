#include <vector>
#include <string.h>
#include <iostream>
#include <limits.h>
using namespace std;
class Solution {
	public:
		vector<int> twoSum(vector<int> &numbers, int target) {
			int min= INT_MAX,max = -1;
			for (int i = 0; i < numbers.size(); ++i)
			{
				if (numbers[i]>max)
				{
					max = numbers[i];
					/* code */
				}
				if (numbers[i]<min)
				{
					min = numbers[i];
					/* code */
				}
				/* code */
			}
			int *hashTable = new int[max-min+1];
			memset(hashTable, 0 , sizeof(int)*(max-min+1));
			for (int i = 0; i < numbers.size(); ++i)
			{
				hashTable[numbers[i]-min] = 1;
				/* code */
			}
			
			int i = min, j = max;
		
			while(i+j != target && i<j)
			{
				if (i+j<target && i<j )
				{
					i++;
					/* code */
				}
				if ( i+j>target && i<j)
				{
					j--;
					/* code */
				}
				
				while(hashTable[i-min]==0 && i<j){
					i++;
				}
				while(hashTable[j-min]==0 && i<j){
					j--;
				}
			}
			std::vector<int> v;
			for (int x = 0; x < numbers.size(); ++x)
			{
				if(numbers[x]== i || numbers[x]== j)
					v.push_back(x+1);
				/* code */
			}
			delete []hashTable;
        		return v;
		}

		
};

int main(int argc, char const *argv[])
{
while(1){
	// cout<<sizeof(int);
	Solution solution;
	std::vector<int> v;
	int t,target;
	cin>>t>>target;
	for (int i = 0; i < t; ++i)
	{
		int j;
		cin>>j;
		v.push_back(j);
		/* code */
	}
	std::vector<int> newv = solution.twoSum(v, target);
	for (int i = 0; i < newv.size(); ++i)
	{
		cout<<newv[i]<<' ';
		/* code */
	}
	cout<<endl;	
}
	return 0;
}