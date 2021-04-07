// #include <vector>
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
	int k = 0;
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int number = getNextNumber(head, n);
        if(number < n){
        	return head->next;
        }
        else{
        	return head;
        }

    }

    int getNextNumber(ListNode *head, int n){
    	if(head){
    		int number = getNextNumber(head->next, n) + 1;
    		if(number == n){
    			if(head->next){
	    			head->next = head->next->next;
	    		}
    		}
    		return number;
    	}
    	return -1;
    }

};

void printListNode(ListNode * head){
	while(head){
		cout<<head->val<<' ';
		head = head->next;
	}
	cout<<endl;
}

int main(int argc, char const *argv[])
{
	Solution s;
	// ListNode a(1);
	// ListNode b(2, &a);
	// ListNode c(3, &b);
	// ListNode d(4, &c);
	// ListNode e(5, &d);
	// ListNode f(6, &e);
	// ListNode g(7, &f);
	ListNode g(7);
	printListNode(&g);
	cout<<s.getNextNumber(&g, 10)<<endl;
	ListNode* p =  s.removeNthFromEnd(&g, 7);
	printListNode(p);
	return 0;
}