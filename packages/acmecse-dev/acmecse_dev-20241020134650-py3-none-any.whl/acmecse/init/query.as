@name querytest
@onKey 9

(print "Query")
;; (query-resource '(& (> x 100) (== rn "cnt1234") (== 2 (+ 1 1)))
(query-resource 
	'(& (> x 100) (== rn "cnt1234"))
	{ "m2m:cnt": {
		"rn": "cnt1234",
	  	"x": 123
	}})


(print (== '(1 2 3) 1))
(print (== ((1) (2)) 2))
;;(print (* '(1 3 2) 2))

(print (and '(false false false) true))

(print (* (+ 3 3) 7))  ;; Return 42
(print (* 6 7))        ;; Returns 42