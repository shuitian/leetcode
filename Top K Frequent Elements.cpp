#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
using namespace std;

void printVector(std::vector<int> &v){
	for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i)
	{
		cout<<*i<<'-';
	}
	cout<<endl;
}

class Solution {
public:

	void adjustHeap(std::vector<int> &heap, int start, std::map<int, int>& numsMap){
		// 从start开始向下调整成小顶堆
		int value = heap[start];
		int left = start * 2 + 1;
		int right = start * 2 + 2;

		int minNode = start;
		if(left < heap.size() && numsMap[heap[left]] < numsMap[heap[minNode]]){
			minNode = left;
		}
		if(right < heap.size() && numsMap[heap[right]] < numsMap[heap[minNode]]){
			minNode = right;
		}

		if(minNode != start){
			int t = heap[start];
			heap[start] = heap[minNode];
			heap[minNode] = t;
			adjustHeap(heap, minNode, numsMap);
		}
	}

    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::vector<int> heap;
        std::map<int, int> numsMap;
        if(k <= 0){
        	return heap;
        }

        for (int i = 0; i < nums.size(); ++i)
        {
        	int value = nums[i];
        	if(numsMap.find(value) == numsMap.end()){
        		numsMap[value] = 1;
        	}else{
        		numsMap[value] ++;
        	}

        	if(heap.size() < k){
        		if(numsMap[value] == 1){
	        		heap.push_back(value);
	        		adjustHeap(heap, 0, numsMap);
	        	}
        	}else{
        		// 如果不在heap中，比较大小
        		auto p = find(heap.begin(), heap.end(), value);
        		if(p == heap.end()){
        			if(numsMap[value] > numsMap[heap[0]]){
        				heap[0] = value;
        				adjustHeap(heap, 0, numsMap);
        			}
        		// 如果在heap中，需要修改，然后调整堆
        		}else{
        			adjustHeap(heap, p-heap.begin(), numsMap);
        		}

        	}
        	// printVector(heap);
        }

        return heap;

    }
};


int main(int argc, char const *argv[])
{
	Solution s;
	// std::vector<int> input{1,1,2,2,1,3};
	std::vector<int> input{4,1,-1,2,-1,2,3};
	std::vector<int> v = s.topKFrequent(input, 2);
	printVector(v);
	return 0;
}