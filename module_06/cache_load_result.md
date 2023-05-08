# Результат нагрузочного тестирования сервиса /author/

## Без кеширования
wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8081/
wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8081/
wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/

## С кешированием
wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8082/
wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8082/
wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8082/


| Result |Test 1|Test 1(cache)Test 2|Test 2(cache)|Test 3|Test 3 (cache)|
|:-------|:-----|:-----|:-----|
| Duration (sec) |60|60|60|60|60|
| Threads |1|1|10|10|50|50|
| Connections |1|1|10|10|50|50|
| Avg Latency (ms) |6.85|2.91|69.01|19.59|171.05|
| Stdev Latency (ms) |3.07|2.99|20.20|7.40|136.08|
| Max Latency (ms) |42.59|74.08|194.30|115.74|356.78|453.96|
| +/- Stdev Latency (%) |89.56|95.60|80.71|89.55|47.22|55.00|
| Avg Req/Sec |149.22|383.38|14.67|52.01|7.55|5.77|
| Stdev Req/Sec |30.48|76.05|5.22|12.28|6.92|7.10|
| Max Req/Sec |212.00|490.00|40.00|130.00|30.00|30.00|
| +/- Stdev Req/Sec (%) |60.77|71.95|48.46|80.00|87.10|88.57|

Latency Distribution
| 50% (ms) |6.02|2.21|61.92|17.50|113.25|366.42|
| 75% (ms) |7.47|2.97|77.51|20.17|332.26|401.25|
| 90% (ms) |18.79|4.02|96.84|26.38|342.89|441.07|
| 99% (ms) |18.79|14.23|136.16|51.06|356.78|453.96|


| Requests in 1 min |8931|22893|8722|31201|36|40|
| Data in 1 min |2.48 Mb|6.29 Mb|2.51 Mb|8.91 Mb|10.48 Kb|11.65 Kb|
| Requests/sec |148.64|381.52|145.17|519.16|0.60|0.67|
| Transfer/sec |42.24 Kb|107.30|42.70 Kb|151.75 Kb|178.54 B|198.40 B|


**Выводы:**
