;;
;;	getConfiguration.as
;;
;;	This script is supposed to be called by the test system via the upper tester interface
;;

@name getConfiguration
@description Return the current value of a configuration value
@usage getConfiguration <key>
@uppertester

(if (!= argc 2)
	(	(log-error "Wrong number of arguments: getConfiguration <key>")
		(quit-with-error)))

(setq key (argv 1))
(if (not (has-config key))
	(	(log-error "Unknown key: ${(key)}")
		(quit-with-error)
	)
)
(log "Get configuration for key: ${(key)}")
(quit (get-config key))
