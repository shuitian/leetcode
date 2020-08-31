#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    	if(s.empty()){
    		return 0;
    	}
    	int length = s.length(),maxLength = 0;

    	std::unordered_map<char, int> charMap;

    	for (int start = 0,end = 1; start < length; ++start)
    	{
    		charMap[s[start]] = 1;
	    	for (end = std::max(end, start + 1); end < length; ++end)
	    	{
	    		char c = s[end];
	    		if(charMap.count(c)){
	    			charMap[c] = 2;
	    			break;
	    		}
	    		charMap[c] = 1;
	    	}

	    	if(end - start > maxLength){
    			maxLength = end - start;
    		}
	    	charMap.erase(s[start]);
	    }

    	return maxLength;
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	std::cout<<s.lengthOfLongestSubstring("abcabcbb")<<std::endl;
	std::cout<<s.lengthOfLongestSubstring("bbbbb")<<std::endl;
	std::cout<<s.lengthOfLongestSubstring("pwwkew")<<std::endl;
	return 0;
}