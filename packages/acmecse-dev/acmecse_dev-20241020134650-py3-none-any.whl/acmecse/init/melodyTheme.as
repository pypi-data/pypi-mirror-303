@name melodyTheme
@description Activate melody 2 @ wemosd1
@onKey 2

;; Use another originator as the Cwemosd1 one
(print "Play Star Wars Theme")

(create-resource (get-config "cse.originator") "cse-in/Cwemosd1/melody"
	{ "m2m:cin": {
		"con" : "2"
	}})
