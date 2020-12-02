package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type policy struct {
	char  byte
	small int
	big   int
}

func parseInput() ([]string, error) {
	file, err := os.Open("day2/input.txt")
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	return lines, nil
}

func parsePolicy(policyStr string) (policy, error) {
	parts := strings.Split(policyStr, " ")
	nums := strings.Split(parts[0], "-")
	small, err := strconv.Atoi(nums[0])
	big, err := strconv.Atoi(nums[1])
	if err != nil {
		return policy{}, err
	}

	return policy{parts[1][0], small, big}, nil
}

func solver(rows []string, validator func(string, policy) bool) (int, bool) {
	count := 0
	for _, row := range rows {
		parts := strings.Split(row, ":")
		rowPolicy, err := parsePolicy(strings.TrimSpace(parts[0]))
		if err != nil {
			return -1, false
		}

		if validator(strings.TrimSpace(parts[1]), rowPolicy) {
			count++
		}
	}

	return count, true
}

func part1(rows []string) (int, bool) {
	validator := func(password string, p policy) bool {
		count := 0
		for i := 0; i < len(password); i++ {
			if password[i] == p.char {
				count++
			}
		}
		return (p.small <= count) && (count <= p.big)
	}

	return solver(rows, validator)
}

func part2(rows []string) (int, bool) {
	validator := func(password string, p policy) bool {
		return (password[p.small-1] == p.char) != (password[p.big-1] == p.char)
	}

	return solver(rows, validator)
}

func main() {
	println("AoC 2020 Day 2\n")

	rows, err := parseInput()
	if err != nil {
		log.Fatal(err)
	}

	println("Solving part 1...")
	ans := "N/A"
	num, ok := part1(rows)
	if ok {
		ans = strconv.Itoa(num)
	}
	fmt.Printf("The answer is: %v\n\n", ans)

	println("Solving part 2...")
	ans = "N/A"
	num, ok = part2(rows)
	if ok {
		ans = strconv.Itoa(num)
	}
	fmt.Printf("The answer is: %v\n\n", ans)
}
