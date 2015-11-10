#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    //线段树 二叉搜索树
    //TLE
    // bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
    //     map<int, int> mapNums;
    //     for (std::vector<int>::iterator i = nums.begin(); i != nums.end(); ++i)
    //     {
    //        if(mapNums.find(*i) != mapNums.end())
    //         {
    //             if(i - nums.begin() - mapNums[*i] <= k){
    //                 return true;    
    //             }
    //         }
    //         mapNums[*i] = i-nums.begin();
    //         for (int j = 1; j <= t; ++j)
    //         {
    //             mapNums[*i+j] = i-nums.begin();
    //             mapNums[*i-j] = i-nums.begin();
    //         }
    //     }
    //     return false;
    // }
};
int main(){
    Solution s;
    std::vector<int> v;
    //v.push_back(1);
    v.push_back(2);
    // v.push_back(4);
    v.push_back(6);
    v.push_back(9);
    v.push_back(111);
    cout<<s.containsNearbyAlmostDuplicate(v, 1, 2)<<endl;
    return 0;   
}
