package main

import (
    "github.com/gin-gonic/gin"
    "HTMX-golang/src/controllers"
)

func main() {
    r := gin.Default()

    r.LoadHTMLGlob("templates/*")

    r.Static("/static", "./static")

    r.GET("/", controllers.IndexController)

    r.GET("/part-one", controllers.PartOneController)

    r.GET("/part-two", controllers.PartTwoController)

    r.GET("/part-three", controllers.PartThreeController)

    r.GET("/part-four", controllers.PartFourController)

    r.GET("/image", controllers.ImageSwapController)

    r.GET("/clock-time", controllers.ClockTimeController)

    r.GET("/message", controllers.MessageController)

    r.GET("/message/slow", controllers.MessageSlowController)

    r.Run(":8080")
}
