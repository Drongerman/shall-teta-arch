# Результат нагрузочного тестирования сервиса /author/

## Среда выполнения
* CPU: 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz 2.80 GHz
* RAM: 32,0 ГБ


## Сводная таблица
| Result |Test 1|Test 1 (cache)|Test 2|Test 2 (cache)|Test 3|Test 3 (cache)|
|:-------|:------------|:------------|:------------|:------------|:------------|:------------|
| Duration (sec) |60|60|60|60|60|60|
| Threads |1|1|10|10|50|50|
| Connections |1|1|10|10|50|50|
| Avg Latency (ms) |6.85|2.91|69.01|19.59|171.05|255.51|
| Stdev Latency (ms) |3.07|2.99|20.20|7.40|136.08|175.36|
| Max Latency (ms) |42.59|74.08|194.30|115.74|356.78|453.96|
| +/- Stdev Latency (%) |89.56|95.60|80.71|89.55|47.22|55.00|
| Avg Req/Sec |149.22|383.38|14.67|52.01|7.55|5.77|
| Stdev Req/Sec |30.48|76.05|5.22|12.28|6.92|7.10|
| Max Req/Sec |212.00|490.00|40.00|130.00|30.00|30.00|
| +/- Stdev Req/Sec (%) |60.77|71.95|48.46|80.00|87.10|88.57|
| LD 50% (ms) |6.02|2.21|61.92|17.50|113.25|366.42|
| LD 75% (ms) |7.47|2.97|77.51|20.17|332.26|401.25|
| LD 90% (ms) |18.79|4.02|96.84|26.38|342.89|441.07|
| LD 99% (ms) |18.79|14.23|136.16|51.06|356.78|453.96|
| Requests in 1 min |8931|22893|8722|31201|36|40|
| Data in 1 min |2.48 Mb|6.29 Mb|2.51 Mb|8.91 Mb|10.48 Kb|11.65 Kb|
| Requests/sec |148.64|381.52|145.17|519.16|0.60|0.67|
| Transfer/sec |42.24 Kb|107.30 Kb|42.70 Kb|151.75 Kb|178.54 B|198.40 B|

**Выводы:**
* При увеличении числа потоков и соединений в 10 раз (до применения кэширования) повысились задержки в 5-10 раз, при этом количество запросов в секунду практически не изменилось (даже немного упало), а при повышении еще в 5 раз вовсе упало до 0,6 запросов в секунду (судя по логам, в связи с недостатком количества соединений к БД в пуле)
* В тестах 1 и 2, добавление кэширование позволило снизить среднее время задержки практически в 3 раза, а также увеличить число запросов/пропускную способность также в 3 раза
* В случае теста 3, добавление кэширования не дало результата, поскольку не хватает соединений к БД, запросы падают и кэш не пополняется
* Наилучший результат производительности был достигнут при увеличении количества соединений и потоков до 10, совместно с применением кэширования.
* Увеличение числа соединений к БД и вертикальное мастабирование среды исполнения позволило бы достичь лучших результатов при большем количестве HTTP соединений и потоков


## Лог исполнения
## Без кеширования
<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     6.85ms    3.07ms  42.59ms   89.56%
    Req/Sec   149.22     30.48   212.00     60.77%
  Latency Distribution
     50%    6.02ms
     75%    7.47ms
     90%   10.00ms
     99%   18.79ms
  8931 requests in 1.00m, 2.48MB read
Requests/sec:    148.64
Transfer/sec:     42.24KB

shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    69.01ms   20.20ms 194.30ms   80.71%
    Req/Sec    14.67      5.22    40.00     48.46%
  Latency Distribution
     50%   61.92ms
     75%   77.51ms
     90%   96.84ms
     99%  139.16ms
  8722 requests in 1.00m, 2.51MB read
Requests/sec:    145.17
Transfer/sec:     42.70KB

shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   171.04ms  136.08ms 356.78ms   47.22%
    Req/Sec     7.55      6.92    30.00     87.10%
  Latency Distribution
     50%  113.25ms
     75%  332.26ms
     90%  342.89ms
     99%  356.78ms
  36 requests in 1.00m, 10.48KB read
Requests/sec:      0.60
Transfer/sec:     178.54B
</pre>

## С кешированием
<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.91ms    2.99ms  74.08ms   95.60%
    Req/Sec   383.38     76.05   490.00     71.95%
  Latency Distribution
     50%    2.21ms
     75%    2.97ms
     90%    4.02ms
     99%   14.23ms
  22892 requests in 1.00m, 6.29MB read
Requests/sec:    381.52
Transfer/sec:    107.30KB

shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    19.59ms    7.40ms 115.74ms   89.55%
    Req/Sec    52.01     12.28   130.00     80.00%
  Latency Distribution
     50%   17.50ms
     75%   20.17ms
     90%   26.38ms
     99%   51.06ms
  31201 requests in 1.00m, 8.91MB read
Requests/sec:    519.16
Transfer/sec:    151.75KB

shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   255.51ms  175.36ms 453.96ms   55.00%
    Req/Sec     5.77      7.10    30.00     88.57%
  Latency Distribution
     50%  366.42ms
     75%  401.25ms
     90%  441.07ms
     99%  453.96ms
  40 requests in 1.00m, 11.64KB read
Requests/sec:      0.67
Transfer/sec:     198.40B
</pre>

# После увеличения числа соединений в пуле до 50

## Сводная таблица
| Result |Test 3|Test 3 (cache)|
|:-------|:------------|:------------|
| Duration (sec) |60|60|
| Threads |50|50|
| Connections |50|50|
| Avg Latency (ms) |322.25|127.15|
| Stdev Latency (ms) |81.52|46.59|
| Max Latency (ms) |755.58|755.88|
| +/- Stdev Latency (%) |70.28|89.55|
| Avg Req/Sec |3.02|8.78|
| Stdev Req/Sec |1.15|2.58|
| Max Req/Sec |10.00|20.00|
| +/- Stdev Req/Sec (%) |74.73|74.30|
| LD 50% (ms) |304.39|116.57|
| LD 75% (ms) |362.26|139.08|
| LD 90% (ms) |444.71|170.92|
| LD 99% (ms) |560.44|280.90|
| Requests in 1 min |9312|23951|
| Data in 1 min |2.65MB|6.83MB|
| Requests/sec |154.94|398.52|
| Transfer/sec |45.20KB|116.45KB|

## Без кэша
<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   322.25ms   81.52ms 755.58ms   70.28%
    Req/Sec     3.02      1.15    10.00     74.73%
  Latency Distribution
     50%  304.39ms
     75%  362.26ms
     90%  444.71ms
     99%  560.44ms
  9312 requests in 1.00m, 2.65MB read
Requests/sec:    154.94
Transfer/sec:     45.20KB
</pre>

## С кэшем
<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_06$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  50 threads and 50 connections  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   127.15ms   46.59ms 755.88ms   89.55%
    Req/Sec     8.78      2.58    20.00     74.30%
  Latency Distribution
     50%  116.57ms
     75%  139.08ms
     90%  170.92ms
     99%  280.90ms
  23951 requests in 1.00m, 6.83MB read
Requests/sec:    398.52
Transfer/sec:    116.45KB
</pre>