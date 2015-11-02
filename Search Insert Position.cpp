#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
    	int i;
    	for (i = 0; i < nums.size(); ++i)
    	{
    		if(target <= nums[i])
    			return i;
    	}
    	return i;
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	vector<int> v;
	v.push_back(1);
	v.push_back(3);
	v.push_back(5);
	v.push_back(6);
	int t = 9;
	while(t--)
	{
		cout<<t<<"  "<<s.searchInsert(v,t)<<endl;
	}
	return 0;
}