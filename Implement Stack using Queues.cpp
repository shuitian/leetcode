#include <iostream>
#include <queue>
using namespace std;
class Stack {
public:
    queue<int> q1;
    queue<int> q2;
    // Push element x onto stack.
    void push(int x) {
        q1.push(x);
    }

    // Removes the element on top of the stack.
    void pop() {
        if(q1.empty()){
            while(q2.size() > 1){
                q1.push(q2.front());
                q2.pop();
            }
            q2.pop();
        }else {
            while(q1.size() > 1){
                q2.push(q1.front());
                q1.pop();
            }
            q1.pop();
        }
    }

    // Get the top element.
    int top() {
        if(q1.empty()){
            return q2.back();
        }else {
            return q1.back();
        }
    }

    // Return whether the stack is empty.
    bool empty() {
        return q1.empty() && q2.empty();
    }
};

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}