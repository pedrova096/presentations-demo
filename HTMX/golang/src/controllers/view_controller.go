package controllers

import (
    "github.com/gin-gonic/gin"
    "net/http"
)

type NavPage struct {
    Prev string
    Next string
}

func getNavPage(index int) NavPage {
    pages := []string{"/part-one", "/part-two", "/part-three", "/part-four"}
    prev := "#"
    next := "#"
    if index > 0 {
        prev = pages[index-1]
    }
    if index < len(pages)-1 {
        next = pages[index+1]
    }
    return NavPage{Prev: prev, Next: next}
}

func IndexController(c *gin.Context) {
    c.HTML(http.StatusOK, "index.tmpl", gin.H{
        "title": "Main website",
    })
}

func PartOneController(c *gin.Context) {
    navPage := getNavPage(0)
    c.HTML(http.StatusOK, "part_one.tmpl", navPage)
}

func PartTwoController(c *gin.Context) {
    navPage := getNavPage(1)
    c.HTML(http.StatusOK, "part_two.tmpl", navPage)
}

func PartThreeController(c *gin.Context) {
    navPage := getNavPage(2)
    c.HTML(http.StatusOK, "part_three.tmpl", navPage)
}

func PartFourController(c *gin.Context) {
    navPage := getNavPage(3)
    c.HTML(http.StatusOK, "part_four.tmpl", navPage)
}
