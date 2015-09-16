#include <vector>
#include <string.h>
#include <iostream>
using namespace std;
class Solution {
	public:
		vector<int> twoSum(vector<int> &numbers, int target) {
			std::vector<int> copy;
			copy = numbers;
			// for (int i = 0; i < copy.size(); ++i)
			// {
			// 	cout<<copy[i]<<' ';
			// 	/* code */
			// }cout<<endl;
			// memcpy(copy, numbers, sizeof(copy));
			this->qsort(numbers, 0, numbers.size()-1);
			// for (int i = 0; i < numbers.size(); ++i)
			// {
			// 	cout<<numbers[i]<<' ';
			// 	/* code */
			// }cout<<endl;
			int i = 0, j = numbers.size()-1;
			while(numbers[i]+numbers[j] != target && i<j)
			{
				if (numbers[i]+numbers[j]<target && i<j)
				{
					i++;
					/* code */
				}
				if (numbers[i]+numbers[j]>target && i<j)
				{
					j--;
					/* code */
				}
			}
			std::vector<int> v;
			for (int x = 0; x < copy.size(); ++x)
			{
				if(copy[x]== numbers[i] || copy[x]== numbers[j])
					v.push_back(x+1);
				/* code */
			}
			// for (int x = 0; x < copy.size(); ++x)
			// {
			// 	if(copy[x]== numbers[j])
			// 		v.push_back(x+1);		
			// 	/* code */
			// }
			// cout<<i<<' '<<j<<' '<<endl;;
			// v.push_back(i+1);
			// v.push_back(j+1);
			// for (int i = 0; i < v.size(); ++i)
			// {
			// 	cout<<v[i]<<' ';
			// 	/* code */
			// }
        		return v;
		}

		void qsort(std::vector<int>& numbers, int begin, int end){

			int number = numbers[(begin+end)/2];
			int i = begin;
			int j = end; 
			while(i<=j)
			{
				while(numbers[i]<number && i<=j){
					i++;
				}
				while(numbers[j]>number && i<=j){
					j--;
				}
				if(i<=j)
				{
					int temp = numbers[i];
					numbers[i] = numbers[j];
					numbers[j] = temp;
					i++;
					j--;	
				}
			}
			if(begin<j)qsort(numbers, begin, j);
			if(i<end)qsort(numbers, i, end);
		}
};

int main(int argc, char const *argv[])
{
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
	
	return 0;
}