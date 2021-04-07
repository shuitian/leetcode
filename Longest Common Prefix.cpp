#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    	if(strs.empty()){
    		return "";
    	}
    	string ret = "";
        for (int i = 0; i < strs[0].size(); ++i)
        {
        	char c = strs[0][i];
        	for (int j = 0; j < strs.size(); ++j)
        	{
        		if(strs[j][i] != c){
        			return ret;
        		}
        	}
        	ret += c;
        	/* code */
        }
        return ret;
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	std::vector<string> v{
		"flower",
		"flow",
		"1fla",
	};
	cout<<s.longestCommonPrefix(v)<<endl;
	return 0;
}