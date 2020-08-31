// # 10. Regular Expression Matching
// # Hard

// # 4556

// # 731

// # Add to List

// # Share
// # Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

// # '.' Matches any single character.
// # '*' Matches zero or more of the preceding element.
// # The matching should cover the entire input string (not partial).

// # Note:

// # s could be empty and contains only lowercase letters a-z.
// # p could be empty and contains only lowercase letters a-z, and characters like . or *.
// # Example 1:

// # Input:
// # s = "aa"
// # p = "a"
// # Output: false
// # Explanation: "a" does not match the entire string "aa".
// # Example 2:

// # Input:
// # s = "aa"
// # p = "a*"
// # Output: true
// # Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
// # Example 3:

// # Input:
// # s = "ab"
// # p = ".*"
// # Output: true
// # Explanation: ".*" means "zero or more (*) of any character (.)".
// # Example 4:

// # Input:
// # s = "aab"
// # p = "c*a*b"
// # Output: true
// # Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
// # Example 5:

// # Input:
// # s = "mississippi"
// # p = "mis*is*p*."
// # Output: false"

#include <iostream>
using namespace std;


class Solution {
public:
    bool isMatch(string s, string p) {
        // cout<<" match  "<<s<<"     "<<p<<endl;
        // p与s相同
        if(p == s){
            return true;
        }

        // 不相同，且有空
        if(p.empty()){
            return false;
        }

        // 错误的re
        if(p[0] == '*'){
            return false;
        }

        if(p.length() == 1){
            if(p == "."){
                return s.length() == 1;
            }
            return false;
        }

        // 如果re不是a*XXX或者.*XXX
        if(p[1] != '*'){
            // 只有第一个字符匹配才行
            if(s.empty()){
                return false;
            }
            if(s[0] == p[0] or p[0] == '.'){
                return isMatch(s.substr(1, s.length() - 1), p.substr(1, p.length() - 1));
            }
            return false;
        }

        // 如果re是.*XXX
        if(p[0] == '.'){
            if(p == ".*"){
                return true;
            }
            for (int i = 0; i <= s.length(); ++i)
            {
                if(isMatch(s.substr(i, s.length() - i), p.substr(2, p.length() - 2))){
                    return true;
                }
            }
            return false;
        }

        // 如果re是a*XXX，不是.*XXX
        for (int i = 0; i < s.length(); ++i)
        {
            if(s[i] == p[0]){
                if(isMatch(s.substr(i, s.length() - i), p.substr(2, p.length() - 2))){
                    return true;
                }
            }else{
                return isMatch(s.substr(i, s.length() - i), p.substr(2, p.length() - 2));
            }
        }
        return isMatch("", p.substr(2, p.length() - 2));
    }
};

int main(int argc, char const *argv[])
{
 Solution s;
 cout<<s.isMatch("a", ".*..a*")<<endl;
 // cout<<s.isMatch("a", ".")<<endl;
 // cout<<s.isMatch("a", "a")<<endl;
 // cout<<s.isMatch("a", "c")<<endl;

 // cout<<s.isMatch("", ".*")<<endl;
 // cout<<s.isMatch("aa", "a")<<endl;
 // cout<<s.isMatch("aa", "a*")<<endl;
 // cout<<s.isMatch("aa", ".*")<<endl;
 // cout<<s.isMatch("aab", "c*a*b")<<endl;
 // cout<<s.isMatch("mississippi", "mis*is*p*.")<<endl;
 return 0;
}