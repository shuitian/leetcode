// 342. Power of Four
// Easy

// 687

// 237

// Add to List

// Share
// Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

// Example 1:

// Input: 16
// Output: true
// Example 2:

// Input: 5
// Output: false
// Follow up: Could you solve it without loops/recursion?

package main

import (
	"fmt"
	// "strconv"
)


func isPowerOfFour(num int) bool {
	if num == 0 {
		return false
	}
    for num != 1{
    	if num%4 != 0 {
    		return false
    	}else{
    		num >>= 2
    	}
    }
    return true
}

func main() {
	fmt.Println(isPowerOfFour(0))
	fmt.Println(isPowerOfFour(1))
	fmt.Println(isPowerOfFour(4))
	fmt.Println(isPowerOfFour(5))
}