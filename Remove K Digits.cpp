#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
    	if(k >= num.size()){
    		return "0";
    	}

    	string left = "";
    	int next = 0;
        for (int i = 0; i < k; ++i)
        {
        	char n = num[next];
        	if(left.empty() || n >= left.back()){
        		left.push_back(num[next]);
        		i--;
        		next ++;
        	}else {
        		left.pop_back();
	        }
        }


        left = left + num.substr(next);
        for (int i = 0; i < left.size(); ++i)
        {
        	if(left[i] != '0'){
        		left = left.substr(i);
        		return left;
        	}
        }
        return "0";
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	// cout<<s.removeKdigits("1432219",3)<<endl;
	// cout<<s.removeKdigits("1432219",6)<<endl;
	// cout<<s.removeKdigits("400",1)<<endl;
	// cout<<s.removeKdigits("10200",1)<<endl;
	// cout<<s.removeKdigits("10",2)<<endl;
	cout<<s.removeKdigits("112",1)<<endl;
	cout<<s.removeKdigits("123456",1)<<endl;
	cout<<s.removeKdigits("12345654321",3)<<endl;
	return 0;
}