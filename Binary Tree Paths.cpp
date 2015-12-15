#include <iostream>
#include <queue>
#include <sstream>
using namespace std;
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
	std::vector<string> vs;
    vector<string> binaryTreePaths(TreeNode* root) {
        std::vector<int> v;
		hasPathSum(root, v);
		return vs;
    }

    bool hasPathSum(TreeNode* root, std::vector<int> v){
    	if(root == NULL){
    		return false;
    	}else {
    		v.push_back(root->val);
    	}
    	if(root->left == NULL && root->right == NULL){
    		string str = "";
    		for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i)
    		{
 				stringstream ss;
 				ss<<(*i);
 				if(i == v.begin()){
    				str = str + ss.str();
    			}else {
    				str = str + "->" + ss.str();
    			}
    		}
    		vs.push_back(str);
    		return true;
    	}else {
    		hasPathSum(root->left, v);
    		hasPathSum(root->right, v);
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
	vector<string> vs = s.binaryTreePaths(&root);
	for (std::vector<string>::iterator i = vs.begin(); i != vs.end(); ++i)
	{
		cout<<(*i)<<endl;;
	}
	return 0;
}