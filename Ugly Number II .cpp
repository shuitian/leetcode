#include "stdio.h"
#include "math.h"
#include <iostream>
#include <vector>
using namespace std;

struct Node
{
    long val;
    Node *next;
    Node() : val(0), next(nullptr) {}
    Node(long x) : val(x), next(nullptr) {}
    Node(long x, Node *next) : val(x), next(next) {}
};

void setNext(Node* node, Node* next)
{
    node->next = next;
}

Node* buildOneList(std::vector<long> numbers)
{
    if(numbers.empty())
    {
        return NULL;
    }

    Node* head = new Node(numbers[0]);
    Node* head1 = head;
    for (std::vector<long>::iterator i = numbers.begin() + 1; i != numbers.end(); ++i)
    {
        Node* next = new Node(*i);
        setNext(head, next);
        head = next;
    }
    return head1;
}

void printNode(Node* head)
{
    Node* p = head;
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
    void insertLinkedList(Node* head, long value){
        if (!head)
        {
            return;
        }
        Node* front = NULL;
        while (head){
            long val = head->val;
            if (val < value)
            {
                front = head;
                head = front->next;
                if (!head){
                    front->next = new Node(value);
                }
            }else{
                Node* n = new Node(value, head);
                if(front){
                    front->next = n;
                }
                break;
            }
        }
    }
    int nthUglyNumber(int n) {
        Node* head = buildOneList(vector<long>{1});
        long val = 0;
        while (n --){
            val = head->val;
            if(val%5 == 0){
                insertLinkedList(head, val * 5);
            }else if(val%3 == 0){
                insertLinkedList(head, val * 3);
                insertLinkedList(head, val * 5);
            }else{
                insertLinkedList(head, val * 2);
                insertLinkedList(head, val * 3);
                insertLinkedList(head, val * 5);
            }
            head = head->next;

        }
        return val;
    }
};


int main(int argc, char const *argv[])
{
	Solution s;
	for (int i = 1; i < 1690; ++i)
	{
		printf("%d\n",s.nthUglyNumber(i));
        // break;
	}

    // Node* head1 = buildOneList(vector<int>{1,4,5});
    // printNode(head1);
    // s.insertLinkedList(head1, 3);
    // printNode(head1);
    // s.insertLinkedList(head1, 0);
    // printNode(head1);
    // s.insertLinkedList(head1, 6);
    // printNode(head1);
	return 0;
}




