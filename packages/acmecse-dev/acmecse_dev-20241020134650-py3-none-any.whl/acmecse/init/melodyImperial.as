@name melodyImperial
@description Activate melody 1 @ wemosd1
@onKey 1

;; Use another originator as the Cwemosd1 one
(print "Play Imperial March")
(create-resource (get-config "cse.originator") "cse-in/Cwemosd1/melody"
	{ "m2m:cin": {
		"con" : "1"
	}})
