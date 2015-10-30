#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
	string Letters[10] = {
		" ",
		"",
		"abc",
		"def",
		"ghi",
		"jkl",
		"mno",
		"pqrs",
		"tuv",
		"wxyz"
	};

    vector<string> letterCombinations(string digits) {
    	std::vector<string> v;
    	if(digits.size() != 0)
    	{
    		loop(v, "", digits, 0);
    	}
        return v;
    }

    void loop(std::vector<string> &v, string s, string digits, int step){
    	for (int i = 0; i < Letters[digits[step]-'0'].size(); ++i)
    	{
    		if(step == digits.size()-1)
    		{
    			v.push_back(s+Letters[digits[step]-'0'][i]);
    		}
    		else 
    		{
    			loop(v, s+Letters[digits[step]-'0'][i], digits, step+1);
    		}
    	}
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	string digits = "23";
	std::vector<string> v = s.letterCombinations(digits);
	for (std::vector<string>::const_iterator i = v.begin(); i != v.end(); ++i)
	{
		cout<<*i<<endl;
	}
	return 0;
}