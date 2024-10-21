@name rebootWemosD1
@description Reboot wemosd1
@onKey 3

;; Use another originator as the Cwemosd1 one
(print "reboot Wemos D1")

(update-resource (get-config "cse.originator") "cse-in/Cwemosd1Node/reboot"
	{ "m2m:rbo": {
		"rbo" : true
	}})
