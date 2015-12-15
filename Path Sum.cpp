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
	queue<int> q;
    bool hasPathSum(TreeNode* root, int sum) {
    	if(root == NULL){
    		return false;
    	}
    	if(root->val == sum && root->left == NULL && root->right == NULL){
    		return true;
    	}else {
    		bool b1 = hasPathSum(root->left,sum-root->val);
    		bool b2 = hasPathSum(root->right,sum-root->val);
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
	cout<<s.hasPathSum(&root, 5);
	return 0;
}