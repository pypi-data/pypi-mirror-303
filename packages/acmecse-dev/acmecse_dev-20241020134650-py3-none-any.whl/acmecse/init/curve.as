@name curve
@onKey ä

(setq count 50)

(include-script "functions")

;;	Create data container
(eval-if-resource-exists "CAdmin" "cse-in/dataContainer" 
  nil
  '((setq cnt { "m2m:cnt" : {
		  "rn" : "dataContainer"
		}})
	 (create-resource "CAdmin" "${get-config \"cse.resourceName\"}" 
	 	(set-json-attribute cnt "m2m:cnt/mni" count))))
	

	;; (create-resource "CAdmin" "${get-config \"cse.resourceName\"}" 
	;; { "m2m:cnt" : {
	;;   "rn" : "dataContainer",
	;;   "mni" : ${count}  ;; Max number of instances
	;; }}))
(setq v 0.5)
(dotimes (i count)
  ((sleep (random 2 8))
   (setq v (+ v (random -0.1 0.1)))
   (create-resource "CAdmin" "${get-config \"cse.resourceName\"}/dataContainer" 
	 { "m2m:cin" : {
	   "con" : "${v}"
	 }})))
	 
	 ;;  "con" : "${(round (random) 2)}"
(print "done")