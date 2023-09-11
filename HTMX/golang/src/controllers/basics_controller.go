package controllers

import (
    "github.com/gin-gonic/gin"
    "net/http"
		"time"
)

func ImageSwapController(c *gin.Context) {
    c.HTML(http.StatusOK, "sections_swap.tmpl", gin.H{})
}

func ClockTimeController(c *gin.Context) {
	currentTime := time.Now()
	loc, _ := time.LoadLocation("Europe/Madrid")
	spanishTime := currentTime.In(loc)
	month := spanishTime.Format("Jan")
	weekDay := spanishTime.Format("Monday")

	c.HTML(http.StatusOK, "sections_swap_next.tmpl",  gin.H{
		"hour": spanishTime.Hour(),
		"minute": spanishTime.Minute(),
		"day": spanishTime.Day(),
		"month": month,
		"week_day": weekDay,
	})
}

func MessageController(c *gin.Context) {
		message := c.Query("message")

		c.HTML(http.StatusOK, "sections_post_message.tmpl", gin.H{
			"message": message,
		})
}

func MessageSlowController(c *gin.Context) {
		message := c.Query("message")

		time.Sleep(1 * time.Second)

		c.HTML(http.StatusOK, "sections_post_message.tmpl", gin.H{
			"message": message,
		})
}
