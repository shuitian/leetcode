#include <iostream>
#include <vector>
using namespace std;
// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
	Data* data;
	int i =100;
public:
	Iterator(const vector<int>& nums){};
	Iterator(const Iterator& iter){};
	virtual ~Iterator(){};
	// Returns the next element in the iteration.
	int next(){return i++;};
	// Returns true if the iteration has more elements.
	bool hasNext() const{return true;};
};


class PeekingIterator : public Iterator {
public:
	bool cache = false;
	int peekCache;
	PeekingIterator(const vector<int>& nums) : Iterator(nums) {
	    // Initialize any member here.
	    // **DO NOT** save a copy of nums and manipulate it directly.
	    // You should only use the Iterator interface methods.

	}

    // Returns the next element in the iteration without advancing the iterator.
	int peek() {
        if(!cache){
            cache = true;
            peekCache = Iterator::next();
        }
        return peekCache;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	int next() {
	    if(cache){
	        cache = false;
	        return peekCache;
	    }else {
	        return Iterator::next();
	    }
	}

	bool hasNext() const {
	    if(cache){
	        return true;
	    }else {
	        return Iterator::hasNext();
	    }
	}
};

int main(int argc, char const *argv[])
{
	std::vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.push_back(3);
	v.push_back(4);
	PeekingIterator p(v);
	cout<<p.hasNext()<<endl;
	cout<<p.peek()<<endl;
	cout<<p.peek()<<endl;
	cout<<p.next()<<endl;
	cout<<p.next()<<endl;
	cout<<p.peek()<<endl;
	cout<<p.peek()<<endl;
	cout<<p.next()<<endl;
	cout<<p.hasNext()<<endl;
	cout<<p.peek()<<endl;
	cout<<p.hasNext()<<endl;
	cout<<p.next()<<endl;
	cout<<p.hasNext()<<endl;
	return 0;
}