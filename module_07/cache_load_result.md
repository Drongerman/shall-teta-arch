# Результат нагрузочного тестирования сервиса /author/

## Среда выполнения
* CPU: 11th Gen Intel(R) Core(TM) i7-1165G7 @ 2.80GHz 2.80 GHz
* RAM: 32,0 ГБ


## Сводная таблица
| Result |Test 1 Maria|Test 1 Mongo|Test 1 Maria (cache)|Test 1 Mongo (cache)|Test 2 Maria|Test 2 Mongo|Test 2 Maria (cache)|Test 2 Mongo (cache)|Test 3 Maria|Test 3 Mongo|Test 3 Maria (cache)|Test 3 Mongo (cache)|
|:-------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|:------------|
| Duration (sec) |60|60|60|60|60|60|60|60|60|60|60|60|
| Threads |1|1|1|1|10|10|10|10|50|50|50|50|
| Connections |1|1|1|1|10|10|10|10|50|50|50|50|
| Avg Latency (ms)      |6.85|3.07|2.91|2.23|69.01|18.93|19.59|13.17|322.25|106.14|127.15|60.27|
| Stdev Latency (ms)    |3.07|1.55|2.99|1.87|20.20|6.06|7.40|6.27|81.52|42.38|46.59|24.83|
| Max Latency (ms)      |42.59|30.44|74.08|29.86|194.30|67.21|115.74|73.28|755.58|522.95|755.88|470.95|
| +/- Stdev Latency (%) |89.56|94.09|95.60|93.74|80.71|80.62|89.55|80.81|70.28|79.36|89.55|86.69|
| Avg Req/Sec           |149.22|336.30|383.38|500.38|14.67|53.11|52.01|77.89|3.02|10.32|8.78|16.99|
| Stdev Req/Sec         |30.48|49.79|76.05|93.58|5.22|10.60|12.28|22.05|1.15|4.20|2.58|5.80|
| Max Req/Sec           |212.00|420.00|490.00|640.00|40.00|80.00|130.00|141.00|10.00|49.00|20.00|70.00|
| +/- Stdev Req/Sec (%) |60.77|67.67|71.95|67.83|48.46|67.63|80.00|56.84|74.73|70.15|74.30|59.89|
| LD 50% (ms)           |6.02|2.66|2.21|1.68|61.92|17.42|17.50|11.57|304.39|94.38|116.57|54.31|
| LD 75% (ms)           |7.47|3.32|2.97|2.17|77.51|20.81|20.17|15.80|362.26|127.15|139.08|68.06|
| LD 90% (ms)           |18.79|4.10 |4.02|3.20|96.84|26.43|26.38|20.31|444.71|161.76|170.92|86.15|
| LD 99% (ms)           |18.79|10.26|14.23|11.32|136.16|41.81|51.06|34.17|560.44|247.89|280.90|132.77|
| Requests in 1 min     |8931|20116|22893|29917|8722|31874|31201|46646|9312|28573|23951|50609|
| Data in 1 min         |2.48 Mb|5.70MB|6.29 Mb|8.47MB|2.51 Mb|9.00MB|8.91 Mb|13.21MB|2.65MB|8.08MB|6.83MB|14.31MB|
| Requests/sec          |148.64|334.83|381.52|497.98|145.17|530.36|519.16|776.27|154.94|475.42|398.52|842.09|
| Transfer/sec          |42.24 Kb|97.11KB|107.30 Kb|144.44KB|42.70 Kb|153.31KB|151.75 Kb|225.15KB|45.20KB|137.75KB|116.45KB|243.74KB|

**Выводы:**
* Переход на MongoDB повысил скорость работы системы в 2-3 раза (задержки снизились, количество обработанных запросов выросло). 
* Даже без использования дополнительного кэширования, MongoDB дал те же результаты, как MariaDB + Redis кэш
* Рекомендуется использовать MongoDB для данной задачи


## Лог исполнения на MongoDB
## Без кеширования
<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_07$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8081/
ning 1m test @ http://localhost:8081/Running 1m test @ http://localhost:8081/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     3.07ms    1.55ms  30.44ms   94.09%
    Req/Sec   336.30     49.79   420.00     67.67%
  Latency Distribution
     50%    2.66ms
     75%    3.32ms
     90%    4.10ms
     99%   10.26ms
  20116 requests in 1.00m, 5.70MB read
Requests/sec:    334.83
Transfer/sec:     97.11KB
</pre>

<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_07$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8081/
Running 1m test @ http://localhost:8081/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    18.93ms    6.06ms  67.21ms   80.62%
    Req/Sec    53.11     10.60    80.00     67.63%
  Latency Distribution
     50%   17.42ms
     75%   20.81ms
     90%   26.43ms
     99%   41.81ms
  31874 requests in 1.00m, 9.00MB read
Requests/sec:    530.36
Transfer/sec:    153.31KB
</pre>

<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_07$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8081/
unning 1m test @ http://localhost:8081/Running 1m test @ http://localhost:8081/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   106.14ms   42.38ms 522.95ms   79.36%
    Req/Sec    10.32      4.20    49.00     70.15%
  Latency Distribution
     50%   94.38ms
     75%  127.15ms
     90%  161.76ms
     99%  247.89ms
  28573 requests in 1.00m, 8.08MB read
Requests/sec:    475.42
Transfer/sec:    137.75KB
</pre>

## С кешированием

<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_07$ wrk -d 60 -t 1 -c 1 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  1 threads and 1 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     2.23ms    1.87ms  29.86ms   93.74%
    Req/Sec   500.38     93.58   640.00     67.83%
  Latency Distribution
     50%    1.68ms
     75%    2.17ms
     90%    3.20ms
     99%   11.32ms
  29917 requests in 1.00m, 8.47MB read
Requests/sec:    497.98
Transfer/sec:    144.44KB
</pre>

<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_07$ wrk -d 60 -t 10 -c 10 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.17ms    6.27ms  73.28ms   80.81%
    Req/Sec    77.89     22.05   141.00     56.84%
  Latency Distribution
     50%   11.57ms
     75%   15.80ms
     90%   20.31ms
     99%   34.17ms
  46646 requests in 1.00m, 13.21MB read
Requests/sec:    776.27
Transfer/sec:    225.15KB
</pre>

<pre>
shall@0411NBB01479NWV:/mnt/c/Users/asshalunov/Documents/GitHub/shall-teta-arch/module_07$ wrk -d 60 -t 50 -c 50 --latency -s ./get.lua http://localhost:8082/
Running 1m test @ http://localhost:8082/
  50 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    60.27ms   24.83ms 470.95ms   86.69%
    Req/Sec    16.99      5.80    70.00     59.89%
  Latency Distribution
     50%   54.31ms
     75%   68.06ms
     90%   86.15ms
     99%  132.77ms
  50609 requests in 1.00m, 14.31MB read
Requests/sec:    842.09
Transfer/sec:    243.74KB
</pre>

## Лог исполнения на MariaDB
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