#include <iostream>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
    	if(s.empty()){
    		return "";
    	}
    	int l = s.length(), left = 0, right = 0;
        bool dp[l][l];
        for (int i = l - 1; i >= 0; --i)
        {
        	for (int j = i; j < l; ++j)
        	{
        		if(i == j){
        			dp[i][j] = 1;
        		}else{
        			if(s[i] == s[j] and (i + 1 == j or dp[i+1][j-1] == 1)){
        				dp[i][j] = 1;
        				if(j - i > right - left){
        					right = j;
        					left = i;
        				}
        			}
        			else{
        				dp[i][j] = 0;
        			}
        		}
        	}
        }
        // for (int i = 0; i < l; ++i)
        // {
        // 	for (int j = 0; j < l; ++j)
	       //  {
	       //  	std::cout<<dp[i][j]<<" ";
	       //  }
	       //  std::cout<<endl;
        // }
        
        return s.substr(left, right - left + 1);
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	std::cout<<s.longestPalindrome("")<<std::endl;
	std::cout<<s.longestPalindrome("babad")<<std::endl;
	std::cout<<s.longestPalindrome("aba")<<std::endl;
	std::cout<<s.longestPalindrome("cbbd")<<std::endl;
	return 0;
}