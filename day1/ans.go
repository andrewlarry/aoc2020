package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func parseInput() ([]int, error) {
	file, err := os.Open("day1/input.txt")
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return nil, err
		}
		lines = append(lines, i)
	}

	return lines, nil
}

func findTwoNums(nums []int, target int) ([2]int, bool) {
	if len(nums) < 2 {
		return [2]int{-1, -1}, false
	}

	numMap := make(map[int]int)
	for _, num := range nums {
		if otherNum, ok := numMap[num]; ok {
			return [2]int{num, otherNum}, true
		}
		numMap[target-num] = num
	}

	return [2]int{-1, -1}, false
}

func part1(nums []int, target int) (int, bool) {
	two, ok := findTwoNums(nums, target)
	if !ok {
		return -1, false
	}

	return two[0] * two[1], true
}

func part2(nums []int, target int) (int, bool) {
	if len(nums) < 3 {
		return -1, false
	}

	for i, num := range nums {
		rest := append(nums[:i], nums[i+1:]...)
		if two, ok := findTwoNums(rest, target-num); ok {
			return num * two[0] * two[1], true
		}
	}

	return -1, false
}

func main() {
	println("AoC 2020 Day 1\n")

	target := 2020
	nums, err := parseInput()
	if err != nil {
		log.Fatal(err)
	}

	println("Solving part 1...")
	ans := "N/A"
	num, ok := part1(nums, target)
	if ok {
		ans = strconv.Itoa(num)
	}
	fmt.Printf("The answer is: %v\n\n", ans)

	println("Solving part 2...")
	ans = "N/A"
	num, ok = part2(nums, target)
	if ok {
		ans = strconv.Itoa(num)
	}
	fmt.Printf("The answer is: %v\n\n", ans)
}
