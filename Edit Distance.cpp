#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
	int minDistance(string word1, string word2) {
		// if(word1.empty())return word2.size();
		// if(word2.empty())return word1.size();
		std::vector<std::vector<int>> v; 
		for (int i = 0; i <= word1.size(); ++i)
		{
			std::vector<int> col;
			// v.push_back(col);
			for (int j = 0; j <= word2.size(); ++j)
			{
				if(i == 0){
					col.push_back(j);
					continue;
				}
				if(j == 0){
					col.push_back(i);
					continue;
				}

				int minValue = word1.size() + word2.size() + 1;

				if(i != 0){
					minValue = min(minValue, v[i-1][j] + 1);
				}
				if(j != 0){
					// cout<<v[i].size()<<'-'<<j<<endl;
					minValue = min(minValue, col[j-1] + 1);
				}
				if(i != 0 && j != 0){
					if(word1[i-1] == word2[j-1]){
						minValue = min(minValue, v[i-1][j-1]);
					}else{
						minValue = min(minValue, v[i-1][j-1] + 1);
					}
				}
				col.push_back(minValue);
			}

			v.push_back(col);
		}

		// for (int i = 0; i <= word1.size(); ++i)
		// {
		// 	for (int j = 0; j <= word2.size(); ++j)
		// 	{
		// 		cout<<v[i][j]<<'-';
		// 	}
		// 	cout<<endl;
		// }

		return v[word1.size()][word2.size()];
	}
};

int main(int argc, char const *argv[])
{
	Solution s;
	// cout<<s.minDistance("intention", "execution")<<endl;
	cout<<s.minDistance("sea", "eat")<<endl;
	cout<<s.minDistance("", "")<<endl;
	cout<<s.minDistance("se", "e")<<endl;
	return 0;
}