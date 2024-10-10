Example: sending of minutes from a meeting
- layer Recorder
	- writes minutes
	- rules: minutes outline
	- request to Secretary: send a message [minutes;person list]
- layer Secretary
	- adds a header, footer, inserts into envelopes, write addresses
	- rules: commercial message form
	- request to Registry: send [message;addresses]
- layer Registry
	- stamps envelopes, places into a packet, send to a post office
	- rules: mail rules
Benefits:
– simpler decomposition and description of the entire process
– easy technology change (mail/e-mail, post/messenger)
– inter-layer co-operation (only Registry goes to the post)