#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        for (int i = 0; i < nums.size(); ++i)
        {
        	int value = nums[i];
        	while(value <= nums.size() && value > 0 && nums[value - 1] != nums[i]){
	        	int t = nums[value - 1];
	        	nums[value - 1] = nums[i];
	        	nums[i] = t;
	        	value = nums[i];
	        }
        }
        // for (int i = 0; i < nums.size(); ++i)
        // {
        // 	cout<<nums[i]<<':';
        // }
        // cout<<endl;
        for (int i = 0; i < nums.size(); ++i)
        {
        	// cout<<nums[i]<<'-';
        	if(nums[i] != i + 1){
        		return i + 1;
        	}
        }
	    return nums.size() + 1;
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	// std::vector<int> v{3,1,2,4};
	// std::vector<int> v{-1,4,2,1,9,10};
	std::vector<int> v{1,1};
	// [-1,4,2,1,9,10]
	// std::vector<int> v{};
	cout<<s.firstMissingPositive(v)<<endl;
	std::vector<int> v1{7,8,9,1,10};
	cout<<s.firstMissingPositive(v1)<<endl;
	return 0;
}