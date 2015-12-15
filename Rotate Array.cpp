#include <iostream>
#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
    	int num =nums.size();
    	if(num == 0 || k == 0){
    		return;
    	}
    	k = num - k%num;
    	for (int i = 0; i < k; ++i)
    	{
    		nums.push_back(nums[i]);
    	}
       	for (std::vector<int>::iterator i = nums.begin(); i != nums.end(); )
       	{
       		nums.erase(i);
       		k--;
       		if(k<=0){
       			break;
       		}
       	}
    }
};

int main(int argc, char const *argv[])
{
	std::vector<int> nums;
	for (int i = 0; i < 10; ++i)
	{
		nums.push_back(i);
	}
	Solution s;
	s.rotate(nums,3);
	for (std::vector<int>::iterator i = nums.begin(); i != nums.end(); ++i)
	{
		cout<<(*i)<<endl;
	}
	return 0;
}