Create a function called unique_ips_from_logs that parses logs from the Linkerd service mesh and returns unique IP addresses based on the provided direction (inbound or outbound).

Here is a sample of the Linkerd logs:

2023-01-12T15:31:46+04:00 [159.441666s] DEBUG ThreadId(04) inbound:accept{peer.addr=11.0.206.69:46018}
2023-01-12T15:31:47+04:00 [159.341731s] DEBUG ThreadId(04) inbound:accept{peer.addr=11.0.206.47:46018}
2023-01-12T15:31:47+04:00 [159.341731s] INFO ThreadId(01)  linkerd_app_outbound::http::proxy_connection_close: Received unmeshed response with l5d-proxy-connection set
2023-01-12T15:31:47+04:00 [159.450323s] DEBUG ThreadId(08) outbound:accept{peer.addr=11.0.63.66:46028}
2023-01-12T15:31:48+04:00 [159.351365s] DEBUG ThreadId(08) outbound:accept{peer.addr=11.0.25.73:46028}
2023-01-12T15:31:48+04:00 [159.351365s] INFO ThreadId(01) outbound:proxy{addr=10.131.149.70:14268}:rescue{client.addr=10.131.106.4:52464}: linkerd_app_core::errors::respond: Request failed error=error trying to connect: connect timed out after 10s error.sources=[connect timed out after 10s]
2023-01-12T15:31:48+04:00 [159.350370s] DEBUG ThreadId(08) outbound:accept{peer.addr=11.0.56.77:46028}
2023-01-12T15:31:49+04:00 [159.291666s] DEBUG ThreadId(04) inbound:accept{peer.addr=11.0.206.69:46018}

Your task is to implement the unique_ips_from_logs function that takes two arguments:

logs (list of strings): A list of log entries as shown above.
direction (string): Either "inbound" or "outbound," indicating the direction of network traffic.
The function should return a list of unique IP addresses that match the specified direction. In the case of the sample logs, if the direction is "inbound," the function should return ['11.0.206.69', '11.0.206.47'].
