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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q){
        	return true;
        }
        if((p && !q) || (!p && q)){
        	return false;
        }
        if(p->val != q->val){
        	return false;
        }
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};

int main(int argc, char const *argv[])
{
	TreeNode n2(2);
	TreeNode n3(3);
	TreeNode n1(1, &n2, &n3);

	TreeNode n4(2);
	TreeNode n5(3);
	TreeNode n6(1, &n5, &n4);
	Solution s;
	cout<<s.isSameTree(&n1, &n6);
	return 0;
}