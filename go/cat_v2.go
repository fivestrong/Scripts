package main

import (
	"os"
	"fmt"
	"flag"
	"io/ioutil"
	"bufio"
)


func main() {

	flag.Usage = func(){
		fmt.Println("Usage:Test Flag Module")
		flag.PrintDefaults()
	}

	lineNmubers := flag.Bool("n", false, "Line Numbers")
	
	flag.Parse()
	for _, filename := range flag.Args(){
		var Numbser = 1
		if *lineNmubers {
			inFile, _ := os.Open(filename)
			defer inFile.Close()
			scanner := bufio.NewScanner(inFile)
			scanner.Split(bufio.ScanLines)
			for scanner.Scan(){
				fmt.Println(Numbser, scanner.Text())
				Numbser += 1
			}

		}else{
			dat, err := ioutil.ReadFile(filename)
			if err != nil{
				fmt.Println("file %s is not exist", filename)
				os.Exit(1)
			}
			fmt.Print(string(dat))
		}

	}
}