**Note:** This is an experimental project I'm developing for my graduation thesis. It's not ready to be used yet.

# pyFluxClient
[![PyPI version](https://badge.fury.io/py/pyfluxc.svg)](https://badge.fury.io/py/pyfluxc)

## Usage
Client initialization
```
>>> import pyfluxclient as flux
>>> fclient = flux.FluxClient('localhost', 8086)
>>> mybucket = 'mycoolbucket/autogen'
```
Query crafting
```
>>> query = FluxQueryFrom(mybucket).range("-24h).limit(3).keep(columns=["_time", "_measurement", "_value"])
>>> print(query)
from(bucket:"mybucket") |> range(start:-24h, stop:now()) |> limit(n: 3, offset: 0)
```
Query InfluxDB endpoint
```
>>> query_result = fclient(query)
>>> query_result.dframe.head()
                    _time     _value       _measurement
0     2020-03-12 20:37:00   0.000000            asn:rtt
1     2020-03-12 20:38:00   0.000000            asn:rtt
2     2020-03-12 20:39:00   0.000000            asn:rtt
```
## Schema exploration
#### Retrieve first and last timestamp
```
>>> fclient.bucket_timerange(mybucket)
(Timestamp('2020-03-12 20:36:45'), Timestamp('2020-03-14 19:24:05'))
```
#### Show measurements
```
>>> qres = fclient.show_measurements(mybucket, "-24h")
>>> qres.dframe
                        _value
0                      asn:rtt
1           asn:tcp_keep_alive
2                 asn:tcp_lost
3         asn:tcp_out_of_order
4      asn:tcp_retransmissions
..                         ...
```
#### Show Tag Keys from measurement 
```
>>> qres = fclient.show_tag_keys(mybycket, "asn:tcp_keep_alive", "-24h")
>>> qres.dframe
         _field
0  packets_rcvd
1  packets_sent
```
