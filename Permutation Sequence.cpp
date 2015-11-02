#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
#include <sstream>
using namespace std;
class Solution {
public:
	std::vector<int> numbers;
	vector<int> v;
	Solution(){
		v.push_back(1);
		v.push_back(1);
		v.push_back(2);
		v.push_back(6);
		v.push_back(24);
		v.push_back(120);
		v.push_back(720);
		v.push_back(720*7);
		v.push_back(720*7*8);
		v.push_back(720*7*8*9);
		numbers.push_back(1);
		numbers.push_back(2);
		numbers.push_back(3);
		numbers.push_back(4);
		numbers.push_back(5);
		numbers.push_back(6);
		numbers.push_back(7);
		numbers.push_back(8);
		numbers.push_back(9);
	}

    string getPermutation(int n, int k) {
    	k=k-1;
    	string s = "";
    	string s1;
		for (int i = n-1; i >= 0; --i)
		{
			int num = 0;
			while(k>=v[i]){
				k-=v[i];
				num++;
			}
			stringstream stream;  
        	stream<<numbers[num];
        	stream>>s1;
        	s+=s1;
        	numbers.erase(numbers.begin()+num);
		}
		return s; 
    }
};

int main(int argc, char const *argv[])
{
	for (int i = 1; i <= 24; ++i)
	{
		Solution s;
		cout<<s.getPermutation(4,i)<<endl;
	}
	return 0;
}