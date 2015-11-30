#include <iostream>
#include <vector>
#include <time.h>
#include <stdlib.h>
using namespace std;
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        for (std::vector<std::vector<int>>::iterator i = grid.begin(); i != grid.end(); ++i)
        {
        	for (std::vector<int>::iterator j = (*i).begin(); j != (*i).end(); ++j)
        	{
        		//cout<<*j<<' ';
        	}//cout<<endl;
        }
        vector<vector<int>> sum = grid;
        for (std::vector<std::vector<int>>::iterator i = sum.begin(); i != sum.end(); ++i)
        {
        	for (std::vector<int>::iterator j = (*i).begin(); j != (*i).end(); ++j)
        	{
        		if(i == sum.begin()){
        			if(j == (*i).begin()){
        				;
        			}else {
        				*j = *j + *(j-1);
        			}
        		}else {
        			if(j == (*i).begin()){
        				*j = *j + *((*(i-1)).begin());
        			}else {
        				int a = *j /*+ *(j-1)*/ + *((*(i-1)).begin()+(j-(*i).begin()));
        				int b = *j + *(j-1) /*+ *((*(i-1)).begin()+(j-(*i).begin()))*/;
        				if(a>b){
        					*j = b;
        				}else {
        					*j = a;
        				}
        			}
        		}
        		if((i+1)== sum.end() && (j+1) == (*i).end()){
        			return *j;
        		}
        		//cout<<*j<<' ';
        	}//cout<<endl;
        }
        return 0;
    }
};

#define count 1
int main(int argc, char const *argv[])
{
	srand((unsigned)time(NULL));
	Solution s;
	vector<vector<int>> grid;
	for (int i = 0; i < count; ++i)
	{
		std::vector<int> row;
		for (int j = 0; j < count; ++j)
		{
			row.push_back(rand()%9+1);
		}
		grid.push_back(row);
	}
	cout<<s.minPathSum(grid)<<endl;
	return 0;
}