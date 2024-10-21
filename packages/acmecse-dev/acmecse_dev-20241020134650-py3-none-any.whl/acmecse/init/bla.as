@name scratch
@onKey ü
@tuiTool
@tuiInput Attribute


(setq result (http 'get "http://localhost:8080/cse-in"   ;; Operation and URL
    { "X-M2M-RI":"1234",                     ;; Header fields
        "X-M2M-RVI": "4",
        "X-M2M-Origin": "CAdmin",
        "Content-type": "application/json;ty=3" }
))

;; (setq result (http 'get "http://localhost:8080/cse-in"   ;; Operation and URL
;;     '(("X-M2M-RI" "1234")
;; 	  ('X-M2M-RVI "4")
;; 	  ('X-M2M-Origin "CAdmin")
;; 	  ('Content-type "application/json;ty=3"))
;; ))

(setq result (http 'get "http://localhost:8000"))

(print result)
	
(quit)

(print (filter (lambda (x) (== x 1)) '(1 2 3 4 5 6 7 8 9 10)))
(print (filter (lambda (x) (< x 4)) '(1 2 3 4 5 6 7 8 9 10)))
;; (print (filter (lambda (x) ("a")) '(1 2 3 4 5 6 7 8 9 10)))
(print (filter (lambda (x) (== x "a")) '("a" "b" "c" )))
(print (filter (lambda (x) (== x "a")) '()))
(print () )

(print (reverse "hallo"))
(print (reverse ()))
(print (reverse '(1 2 3 4 5 6 7 8 9 10)))
;; (print (reverse '(1 2 3 4 5 6 7 8 9 10) '(1 2 3 4 5 6 7 8 9 10)))

(print(all true true true))
(print(all false false true))
(print(all '(false false true)))
(print(all '()))
(print(any '(true true true)))
(print(any true))
(print(any false))
(print(any '()))

(print (zip '(1 2 3 4 5)))
(print (zip '(1 2 3 4 5) '(6 7 8 9 10)))
(print (zip '(1 2 3 4 5) '()))


(print(any false false false))
(print(any false false true))
(print(any '(false false true)))
(print(any '(false false false)))
(if (not (any '(false false false)))
	(print "true")
	(print "false"))

(print (min 1 2 3 4 5 6 7 8 9 10))
(print (min '(1 2 3 4 5 6 7 8 9 10)))
(print (min '()))
;; (print (min 1 2 () 4 5 6 7 8 9 10))
;; (print (min '(1 2 () 4 5 6 7 8 9 10)))
(print (max 1 2 3 4 5 6 7 8 9 10))
(print (max '(1 2 3 4 5 6 7 8 9 10)))
(print (max '(1 2 3 4 5 6 7 8 9 11) '(1 2 3 4 5 6 7 8 9 12)))
(print (max '()))
(print (max "abc" "ABC"))

(print "[b]Map") ;; test
(print (map (lambda (x y) (+ x y)) '(1 2 3) '(4 6 7 8) ))
(print (map '+ '(1 2 3) '(4 6 7 8)))
(print (map '+ '() '(4 6 7 8)))
;; (assert (== 1 2))
;; (print (if x) )
(print "Reduce")
(setq lst '(1 2 3 4 5 6 7 8 9 10))
(setq lst2 '(1 2 3 "4" 5 6 7 8 9 10))

(defun do-mul (x y)
		(* x y))

(defun do-add (x y)
		(+ ))

(print (reduce '+ '()))
(print (reduce '+ '() ()))
(print (reduce '+ '(1 2 3 4 5) 10))
(print (reduce (lambda (x y) (+ x y)) '(1 2 3 4 5)))
(quit)

;; ((print (reduce 'do-add lst )))
;; (print (reduce 'do-mul lst2 ))
(print (reduce 'do-mul lst 100 ))
(print (reduce 'do-mul () ))
(print (reduce 'do-mul () 99))
(print (reduce '+ lst ))

(print (reduce '+ lst))
(print (reduce '+ lst 100 ))
(print (reduce '+ () ))
(print (reduce '+ () 99))
(quit)
;; (print (reduce (lambda (x y) (+ x y)) lst1 lst2))


;; (print ((lambda (x) (* x 4)) 2))
(print "Map")
(setq lst '(1 2 3 4 5 6 7 8 9 10))
(defun pri (x)
		(* x 4))

(print (map 'pri lst))
(print (map (lambda (x) (* 2 x)) lst))

(quit)



;; (clear-console)

;; (if (!= argc 2)
;; 	((print "[red]Add one identifier without spaces")
;; 	 (quit)))
;; (dolist (t (cse-attribute-infos (argv 1)))
;; 	(
;; 	 (print "[dodger_blue2]attribute  = " (nth 1 t))
;; 	 (print "[dark_orange]short name = " (nth 0 t))
;; 	 (print "type       = " (nth 2 t) nl)))

;; (quit)

(print "next")



(print 'test)


(dolist (i '(1 2 3 4 5 6 7 8 9 10))
	(print i))                   ;; print 1..10

(setq result 0)
(dolist (i '(1 2 3 4 5 6 7 8 9 10) result)
	(setq result (+ result i)))  ;; sum 1..10
(print result)                   ;; 55


(defun x ()
	(print "hallo"))

(print (dotimes (var 10)
	(print var)))

(print (dolist (var '(1 2 3 4 5 6 7 8 9 10) result)
	((print var)
	 (setq result var))))
( print result)



(setq result 0)
(dotimes (i 10 result)
	(setq result (+ result i)))  ;; sum 1..10
(print result)


;;(setq result 23)
(print (dotimes (var (+ 1 1) result) ((x) (setq result var))))


(print '(1 2 3 4 5 6 7 8 9 10))

(print nil)

(tui-notify "test" )
(tui-notify "test" "title" )
(tui-notify "test" "title" "default")
(tui-notify "test" "title" "information")
(tui-notify "test" "title" "warning")
(tui-notify "test" "title" "error" )
(tui-notify "test" "title" "error" nil )
(tui-notify "test" "title" "error" 5 )

