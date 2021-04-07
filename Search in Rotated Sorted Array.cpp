#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        return _search(nums, 0, nums.size() - 1, target);
    }

	int _search(std::vector<int>& nums, int start, int end, int target){
		// cout<<start<<end<<endl;
		if(nums.empty()){
			return -1;
		}

		int startValue = nums[start];
        int endValue = nums[end];
        int mid = (end - start)/2 + start;
        // int mid = 
        int midValue = nums[mid];
        if(startValue == target){
        	// cout<<"?";
        	return start;
        }
        if(endValue == target){
        	// cout<<endValue<<target;
        	return end;
        }
        if(midValue == target){
        	// cout<<"1-"<<target;
        	return mid;
        }
        if(end - start < 2){
			return -1;
		}
        // mid in left part
        if(midValue > endValue){
        	if(target > midValue){
        		return _search(nums, mid, end, target);	
        	}
        	else{
        		if(target > startValue){
        			return _search(nums, start, mid, target);
        		}
        		else{
        			return _search(nums, mid, end, target);	
        		}
        	}
        }
        // mid in right part
        else{
        	if(target > midValue){
        		if(target < endValue){
        			return _search(nums, mid, end, target);	
        		}
        		else if(startValue > endValue){
        			return _search(nums, start, mid, target);
        		}else{
        			return -1;
        		}
        	}else{
        		return _search(nums, start, mid, target);
        	}
        }
	}
};

int main(int argc, char const *argv[])
{
	std::vector<int> v{11,12,13,14,15,16,17,18,19,20,21,22,23,24,0,1,2,4,5,6,7,8,9,10,};
	// std::vector<int> v{0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,};
	Solution s;
	cout<<s.search(v, 28);
	return 0;
}