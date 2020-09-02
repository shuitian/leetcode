// 11. Container With Most Water
// Medium

// 6801

// 608

// Add to List

// Share
// Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

// Note: You may not slant the container and n is at least 2.

 



// The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

// Example:

// Input: [1,8,6,2,5,4,8,3,7]
// Output: 49

#include <iostream>
#include <vector>
#include <stack>
#include <utility>
#include <algorithm>
using namespace std;

class Solution {
public:
	int debug = 0;
	int left = 0;
	int right = 0;
	int maxArea1(vector<int>& height) {
    	int size = height.size();
        int maxValue = 0;
        for (int i = 0; i < size; ++i)
        {
            for (int j = i + 1; j < size; ++j)
            {
            	int value = min(height[i],height[j]) * abs(i - j);
            	if(value > maxValue){
            		left = i;
            		right = j;
            		maxValue = value;
            	}
            }
        }
        return maxValue;
    }

    int maxArea(vector<int>& height) {
        std::stack<pair<int, int>> upList;
        std::stack<pair<int, int>> downList;
    	for (int i = 0; i < height.size(); ++i)
        {
        	int value = height[i];
        	
            if(upList.empty()){
            	upList.push(make_pair(i, value));
            }else{
            	pair<int, int> t = upList.top();
            	if(value > t.second){
            		upList.push(make_pair(i, value));
            	}
            }
        }

        for (int i = height.size() - 1; i >= 0; --i)
        {
        	int value = height[i];
        	
            if(downList.empty()){
            	downList.push(make_pair(i, value));
            }else{
            	pair<int, int> t = downList.top();
            	if(value > t.second){
            		downList.push(make_pair(i, value));
            	}
            }
        }

        printStack(upList);
        printStack(downList);
        pair<int, int> p1 = upList.top();
        upList.pop();
        pair<int, int> p2 = downList.top();
        downList.pop();
        int value = calcValue(p1, p2);
        left = p1.first;
        right = p2.first;
        while(!upList.empty() or !downList.empty()){
        	int maxValue = value;
        	int side = 0;
        	pair<int, int> key;
        	
        	// printStack(upList);
        	// printStack(downList);
        	if(!upList.empty()){
        		pair<int, int> t = upList.top();
        		int leftValue = calcValue(t, p2);
        		if(leftValue >= maxValue){
        			maxValue = leftValue;
        			side = 1;
        			key = t;
        		}
        	}
        	if(!downList.empty()){
        		pair<int, int> t = downList.top();
        		int rightValue = calcValue(p1, t);
        		if(rightValue >= maxValue){
        			maxValue = rightValue;
        			side = 2;
        			key = t;
        		}
        	}

        	if(side == 1){
        		upList.pop();
        		value = maxValue;
        		p1 = key;
        		left = p1.first;
        	}else if(side == 2){
        		downList.pop();
        		value = maxValue;
        		p2 = key;
        		right = p2.first;
        	}else{
                if(!upList.empty())upList.pop();
                if(!downList.empty())downList.pop();
        	}
        }


        return value;
    }

    int calcValue(pair<int,int> p1, pair<int,int> p2){
    	if(debug){
	    	cout<<"calc "<<p1.first<<"-"<<p2.first<<":"<<min(p1.second, p2.second) * abs(p1.first - p2.first)<<endl;
	    }
    	return min(p1.second, p2.second) * abs(p1.first - p2.first);
    }

    void printStack(std::stack<pair<int, int>> s){
    	if(debug){
	    	_printStack(s);
	    	cout<<endl;
    	}
	}

    void _printStack(std::stack<pair<int, int>> s){
    	if(s.empty()){
    		return;
    	}
    	pair<int, int> t = s.top();
    	s.pop();
    	_printStack(s);
    	cout<<t.first<<" "<<t.second<<";";
    	s.push(t);
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	s.debug = 1;
	// std::vector<int> v{1,8,6,2,5,4,8,3,7};
	// cout<<s.maxArea(v)<<endl;
	// std::vector<int> v1{1,2,3,4,5,6};
	// cout<<s.maxArea(v1)<<endl;
	// std::vector<int> v1{1,1};
	// cout<<s.maxArea(v1)<<endl;
	// std::vector<int> v2{1,2,1};
	// cout<<s.maxArea(v2)<<endl;
	std::vector<int> v3{159,157,139,51,98,71,4,125,48,125,64,4,105,79,136,169,113,13,95,88,190,5,148,17,152,20,196,141,35,42,188,147,199,127,198,49,150,154,175,199,80,191,3,137,22,92,58,87,57,153,175,199,110,75,16,62,96,12,3,83,55,144,30,6,23,28,56,174,183,183,173,15,126,128,104,148,172,163,35,181,68,162,181,179,37,197,193,85,10,197,169,17,141,199,175,164,180,183,90,115};
	cout<<s.maxArea(v3);
	cout<<",left:"<<s.left<<",right:"<<s.right<<endl;
	cout<<s.maxArea1(v3);
	cout<<",left:"<<s.left<<",right:"<<s.right<<endl;
	return 0;
}