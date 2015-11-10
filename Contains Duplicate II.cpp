#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> mapNums;
        for (std::vector<int>::iterator i = nums.begin(); i != nums.end(); ++i)
        {
            if(mapNums.find(*i) != mapNums.end()){
                if(i-nums.begin() - mapNums[*i] <= k){
                    return true;    
                }
            }
            mapNums[*i] = i-nums.begin();
        }
        return false;
    }
};
int main(){
    Solution s;
    std::vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    v.push_back(1);
    v.push_back(4);
    v.push_back(4);
    cout<<s.containsNearbyDuplicate(v, 0)<<endl;
    return 0;   
}
