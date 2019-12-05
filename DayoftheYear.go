// package main

import (
	// "fmt"
	"strconv"
)

func isLeapYear(year int) bool {
	if year % 100 == 0{
		return year % 400 == 0
	}
	return year % 4 == 0
}

func dayOfYear(date string) int {
	year, _ := strconv.Atoi(date[0:4])
	month, _ := strconv.Atoi(date[5:7])
	day, _ := strconv.Atoi(date[8:10])
	month -- 
	total := 0
	monthDay := [12]int{31,28,31,30,31,30,31,31,30,31,30,31}
	for i := 0; i < 12; i++ {
		if i < month{

			total = total + monthDay[i]
		}
		if i == month{
			total = total + day
		}
	}

	if month > 1 && isLeapYear(year){
		total ++
	}
	return total
}

// func main() {
// 	// fmt.Println(isLeapYear(1900))
// 	// fmt.Println(isLeapYear(1904))
// 	// fmt.Println(isLeapYear(2000))
// 	fmt.Println(dayOfYear("2019-01-09"))
// 	fmt.Println(dayOfYear("2019-02-10"))
// 	fmt.Println(dayOfYear("2003-03-01"))
// 	fmt.Println(dayOfYear("2004-03-01"))
// }