#include <vector>
#include <iostream>
#include <map>
#include <queue>
#include <utility>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        // bool confirm[board.size()][board[0].size()];
        std::map<pair<int, int>, int> oPos;
    	for (int i = 0; i < board.size(); ++i)
		{
			auto _list = board[i];
			for (int j = 0; j < _list.size(); ++j)
			{
				if(_list[j] == 'O'){
					oPos[{i,j}] = 0;
				}
			}
		}

		for (auto i = oPos.begin(); i != oPos.end(); ++i)
		{
			int x = i->first.first;
			int y = i->first.second;
			int state = i->second;
			if(state == 0){
				search(board, oPos, x, y);
			}
		}

		for (auto i = oPos.begin(); i != oPos.end(); ++i)
		{
			int x = i->first.first;
			int y = i->first.second;
			int state = i->second;
			// cout<<x<<'-'<<y<<'-'<<state<<endl;
			if(state == 2){
				board[x][y] = 'X';
			}
		}
    }

    bool isBorder(vector<vector<char>>& board, int x, int y){
    	return x == 0 || y == 0 || x == board.size() - 1 || y == board[0].size() - 1;
    }

    bool isValid(vector<vector<char>>& board, int x, int y){
    	return x < 0 || y < 0 || x > board.size() - 1 || y > board[0].size() - 1;
    }

    void search(vector<vector<char>>& board, map<pair<int, int>, int>& oPos, int x, int y){
    	// cout<<"search"<<x<<y<<endl;
    	if(isBorder(board, x, y)){
    		// 1 mean O->O
    		oPos[{x,y}] = 1;
    		return;
    	}
    	queue<pair<int, int>> q;
    	q.push({x,y});
    	// 2 mean O->X
    	int state = 2;
    	std::map<pair<int, int>, int> history;
    	history[{x,y}] = 1;
    	while(!q.empty()){
    		pair<int, int> current = q.front();
    		// cout<<"current"<<current.first<<current.second<<endl;
    		q.pop();
    		x = current.first;
    		y = current.second;
    		// if is borde
    		if(isBorder(board, current.first, current.second)){
    			// not change
    			state = 1;
    		}

    		for (int i = 0; i < 4; ++i)
    		{
    			auto next = make_pair(x + (((i+1)&1) * (i - 1)), y + ((i&1) * (-i + 2)));
    			// cout<<i<<':'<<x<<y<<next.first<<next.second<<endl;
	    		// skip history
	    		if(history.find(next) != history.end()){
	    			continue;
	    		}
	    		if(isValid(board, next.first, next.second)){
	    			continue;
	    		}
	    		// is X
	    		auto it = oPos.find(next);
	    		if(it == oPos.end()){
	    			continue;
	    		}
	    		// find changed O
	    		if(it->second == 1){
	    			// not changed
	    			state = 1;
	    		}else{
	    			q.push(next);
	    			history[next] = 1;
	    		}
    		}
    	}
		for (auto i = history.begin(); i != history.end(); ++i)
		{
			// change to X
			oPos[i->first] = state;
		}
    }
};

void printVecVec(vector<vector<char>>& board){
	cout<<"print!"<<endl;
	for (int i = 0; i < board.size(); ++i)
	{
		auto _list = board[i];
		for (int j = 0; j < _list.size(); ++j)
		{
			cout<<_list[j]<<' ';
		}
		cout<<endl;
	}
}

int main(int argc, char const *argv[])
{

	// std::vector<std::vector<char>> board{
	// 	{'X','X','X','X'},
	// 	{'X','O','O','X'},
	// 	{'X','X','O','X'},
	// 	{'X','O','X','X'},
	// };
	std::vector<std::vector<char>> board{
		{'O','X','X','O','X'},
		{'X','O','O','X','O'},
		{'X','O','X','O','X'},
		{'O','X','O','O','O'},
		{'X','X','O','X','O'},
	};
	Solution s;
	printVecVec(board);
	s.solve(board);
	printVecVec(board);
	return 0;
}