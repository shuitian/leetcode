package main

import (
	"fmt"
	"strings"
)

func toLowerCase(str string) string {
    return strings.ToLower(str)
}

func main() {
	s := "Hello World!"
	fmt.Println(toLowerCase(s))
}