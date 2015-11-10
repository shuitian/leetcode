#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> mapNums;
        for (std::vector<int>::iterator i = nums.begin(); i != nums.end(); ++i)
        {
            if(mapNums[*i] == 1)
                return true;
            mapNums[*i] ++;
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
    cout<<s.containsDuplicate(v)<<endl;
    return 0;   
}
