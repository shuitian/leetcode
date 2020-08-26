#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};


void setNext(ListNode* node, ListNode* next)
{
	node->next = next;
}

ListNode* buildOneList(std::vector<int> numbers)
{
	if(numbers.empty())
	{
		return NULL;
	}

	ListNode* head = new ListNode(numbers[0]);
	ListNode* head1 = head;
	for (std::vector<int>::iterator i = numbers.begin() + 1; i != numbers.end(); ++i)
	{
		ListNode* next = new ListNode(*i);
		setNext(head, next);
		head = next;
	}
	return head1;
}

void printListNode(ListNode* head)
{
	ListNode* p = head;
	while(p)
	{
		std::cout<<p->val;
		p = p->next;
		if(p)
		{
			std::cout<<"->";
		}
	}
	std::cout<<endl;
}

class Solution {

public:
	Solution(){}
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		vector<ListNode*> v = {l1, l2};
        return mergeKLists(v);
    }

	ListNode* mergeKLists(vector<ListNode*>& lists) 
	{
		ListNode* head = new ListNode(0);
		ListNode* tail = head;
		for (std::vector<ListNode*>::iterator i = lists.begin(); i != lists.end(); )
		{
			if(!(*i))
			{
				lists.erase(i);
			}
			else
			{
				++i;
			}
		}
		while(!lists.empty())
		{
		 	mergeOne(tail, lists);
		 	tail = tail->next;
		 	// printListNode(head);
		}

		return head->next;
	}

	void mergeOne(ListNode* tail, vector<ListNode*>& lists) 
	{
		ListNode* minHead = getMinHeadListNode(lists);
		std::vector<ListNode*>::iterator iter=std::find(lists.begin(),lists.end(),minHead);
		lists.erase(iter);
		if(minHead->next)
		{
			lists.push_back(minHead->next);
		}

		tail->next = minHead;
	}

	ListNode* getMinHeadListNode(vector<ListNode*>& lists)
	{
		int minVal = lists[0]->val;
		ListNode* minHead = lists[0];
		for (std::vector<ListNode*>::iterator i = lists.begin(); i != lists.end(); ++i)
		{
			if((*i)->val < minVal)
			{
				minVal = (*i)->val;
				minHead = *i;
			}
		}
		return minHead;
	}
};



int main()
{
	Solution s;
	ListNode* head1 = buildOneList(vector<int>{1,4,5});
	printListNode(head1);
	ListNode* head2 = buildOneList(vector<int>{1,3,4});
	printListNode(head2);
	ListNode* head3 = buildOneList(vector<int>{2,6});
	printListNode(head3);
	vector<ListNode*> lists = {head1, head2, head3};
	ListNode* head = s.mergeTwoLists(head1, head2);
	printListNode(head);
	// ListNode* head = s.mergeKLists(lists);
	// printListNode(head);
	// lists = {buildOneList(vector<int>{})};
	// head = s.mergeKLists(lists);
	// printListNode(head);
	return 0;
}