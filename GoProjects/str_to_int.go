package main

import "fmt"

func main() {
	value := StringToInt("1")

	// check if value is int type
	if value == 1 {
		println("value is int type")
	}
}

func StringToInt(str string) int {
	var i int
	fmt.Sscanf(str, "%d", &i)
	return i
}
