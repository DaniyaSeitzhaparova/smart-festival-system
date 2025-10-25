package main

import (
	"fmt"
	"math/rand"
	"time"
)

type CompostData struct {
	Temperature float64
	Volume      float64
}

func readSensor() CompostData {
	return CompostData{
		Temperature: 30 + rand.Float64()*10,
		Volume:      2 + rand.Float64()*5,
	}
}

func main() {
	rand.Seed(time.Now().UnixNano())
	fmt.Println("[Eco-Composting] Starting compost sensor data stream...")
	for i := 0; i < 3; i++ {
		data := readSensor()
		fmt.Printf("Reading %d → Temp: %.2f°C | Volume: %.2f kg\n", i+1, data.Temperature, data.Volume)
		time.Sleep(1 * time.Second)
	}
}
// Update: improved compost data refresh rate
