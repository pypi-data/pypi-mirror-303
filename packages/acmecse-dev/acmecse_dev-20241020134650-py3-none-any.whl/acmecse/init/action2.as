
#
# separate action reference wie sri
#


(create-resource (get-config "cse.originator") "cse-in"
	{ "m2m:actr": { 
		"rn": "actr2",
		"evm": 3,

		"sri": "cse-in/cnt1",
		"evc" : { 
			"optr": 3,		
			"sbjt": "cni",
			"thld": 0
		},

		"orc": "cse-in/cnt2",
		"apv": {
			"op": 1,
			"fr": "CAdmin",
			"to": "cse-in/cnt2",
			"rqi": "1234",
			"rvi": "4",
			"ty": 4,
			"pc": { 
				"m2m:cin": {
					"con": "test2"
			}}
		} 
	}})
