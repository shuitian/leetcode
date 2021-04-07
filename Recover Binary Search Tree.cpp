#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
    void recoverTree(TreeNode* root) {
        if(!root){
        	return
        }

        int val = root.val;
        if(root->left && root->right){
        	int left = root->left.val;
        	int right = root->left.val;
        	if(left <= val && val <= right){
        		return;
        	}
        	if(left <= val && val <= right){
        		return;
        	}
        	if(left <= val && val > right){
        		change()
        	}
        }
        else{

        }
    }
};

void lfsNode(TreeNode* root){
	if(!root){
		return;
	}

	lfsNode(root->left);
	cout<<root->val<<' ';
	lfsNode(root->right);
}

int main(int argc, char const *argv[])
{
	TreeNode n2(2, nullptr, nullptr);
	TreeNode n3(3, nullptr, &n2);
	TreeNode n1(1, &n3, nullptr);
	Solution s;
	lfsNode(&n1);
	s.recoverTree(&n1);
	lfsNode(&n1);
	return 0;
}