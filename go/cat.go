package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func run() int{
	if len(os.Args) == 1{
		reader := bufio.NewReader(os.Stdin)
		for {
			text, err := reader.ReadString('\n')
			if err != nil{
				return 1
			}
			fmt.Print(text)
		}
	} else {
		args := os.Args[1:]

		for _, v := range args{
			b, err := ioutil.ReadFile(v)
			if err != nil{
				fmt.Println(fmt.Errorf("cat: %s: No such file or directory", v))
				return 1
			}
			fmt.Print(string(b))
		}
	}
	return 0
}

func main(){
	os.Exit(run())
}