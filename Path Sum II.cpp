#include <iostream>
#include <queue>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
	std::vector<vector<int>> vs;
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
		std::vector<int> v;
		hasPathSum(root, sum, v);
		return vs;
    }

    bool hasPathSum(TreeNode* root, int sum, std::vector<int> v){
    	if(root == NULL){
    		return false;
    	}else {
    		v.push_back(root->val);
    	}
    	if(root->val == sum && root->left == NULL && root->right == NULL){
    		vs.push_back(v);
    		return true;
    	}else {
    		bool b1 = hasPathSum(root->left,sum-root->val, v);
    		bool b2 = hasPathSum(root->right,sum-root->val, v);
    		return b1|b2;
    	}
    }
};

int main(int argc, char const *argv[])
{
	Solution s;
	TreeNode root(1);
	TreeNode r1(2);
	TreeNode r2(3);
	TreeNode r3(4);
	TreeNode r4(5);
	TreeNode r5(6);
	root.left = &r1;
	root.right = &r2;
	r1.left = &r3;
	r2.left = &r5;
	r1.right = &r4;
	vector<vector<int>> vs = s.pathSum(&root, 10);
	for (std::vector<vector<int>>::iterator i = vs.begin(); i != vs.end(); ++i)
	{
		for (std::vector<int>::iterator j = (*i).begin(); j != (*i).end(); ++j)
		{
			cout<<(*j);
		}cout<<endl;;
	}
	return 0;
}