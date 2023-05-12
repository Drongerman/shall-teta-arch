## 1. Aggregation:
Пример 1: Подсчет общего количества документов в коллекции:
<pre>
db.collection.aggregate([
  { $count: "totalDocuments" }
])
</pre>

Пример 2: Группировка документов по определенному полю и подсчет количества документов в каждой группе:
<pre>
db.collection.aggregate([
  { $group: { _id: "$field", count: { $sum: 1 } } }
])
</pre>

Пример 3: Вычисление среднего, максимального или минимального значения поля в коллекции:
<pre>
db.collection.aggregate([
  { $group: { _id: null, avg: { $avg: "$field" }, max: { $max: "$field" }, min: { $min: "$field" } } }
</pre>

## 2. Text search:
Пример 1: Поиск документов, содержащих определенное ключевое слово или фразу:
<pre>
db.collection.find({ $text: { $search: "keyword" } })
</pre>
Пример 2: Фильтрация документов по определенному текстовому полю:
<pre>
db.collection.find({ field: { $regex: /pattern/ } })
</pre>
Пример 3: Поиск документов, содержащих определенную комбинацию ключевых слов или фраз:
<pre>
db.collection.find({ $text: { $search: "keyword1 keyword2" } })
</pre>

## 3. MapReduce:
Пример 1: Подсчет общего количества документов в коллекции:
<pre>
db.collection.mapReduce(
  function() { emit("totalDocuments", 1); },
  function(key, values) { return Array.sum(values); },
  { out: "totalDocuments" }
)
</pre>
Пример 2: Группировка документов по определенному полю и подсчет количества документов в каждой группе:
<pre>
db.collection.mapReduce(
  function() { emit(this.field, 1); },
  function(key, values) { return Array.sum(values); },
  { out: "groupedDocuments" }
)
</pre>
Пример 3: Вычисление среднего, максимального или минимального значения поля в коллекции:
<pre>
db.collection.mapReduce(
  function() { emit(null, { count: 1, sum: this.field }); },
  function(key, values) {
    var result = { count: 0, sum: 0 };
    values.forEach(function(value) {
      result.count += value.count;
      result.sum += value.sum;
    });
    return result;
  },
  { out: "stats" }
)
</pre>

## 4. Geospatial queries:
Пример 1: Поиск документов, находящихся в определенном радиусе от заданной точки:
<pre>
db.collection.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [longitude, latitude]
      },
      $maxDistance: radius
    }
  }
})
</pre>
Пример 2: Поиск документов, находящихся внутри определенной географической области:
<pre>
db.collection.find({
  location: {
    $geoWithin: {
      $geometry: {
        type: "Polygon",
        coordinates: [[
          [longitude1, latitude1],
          [longitude2, latitude2],
          [longitude3, latitude3],
          [longitude4, latitude4],
          [longitude1, latitude1]
        ]]
      }
    }
  }
})
</pre>
Пример 3: Поиск документов, которые находятся на определенном расстоянии от заданной точки:
<pre>
db.collection.find({
  location: {
    $near: {
      $geometry: {
        type: "Point",
        coordinates: [longitude, latitude]
      },
      $minDistance: distance,
      $maxDistance: distance
    }
  }
})
</pre>

## 5. Transactions:
Пример 1: Атомарное обновление нескольких документов в одной транзакции:
<pre>
session.startTransaction();
try {
  db.collection1.updateMany({ field: value1 }, { $set: { field: newValue1 } });
  db.collection2.updateMany({ field: value2 }, { $set: { field: newValue2 } });
  session.commitTransaction();
} catch (error) {
  session.abortTransaction();
}
</pre>
Пример 2: Атомарное добавление нескольких документов в одной транзакции:
<pre>
session.startTransaction();
try {
  db.collection1.insertMany([{ field1: value1 }, { field1: value2 }]);
  db.collection2.insertMany([{ field2: value3 }, { field2: value4 }]);
  session.commitTransaction();
} catch (error) {
  session.abortTransaction();
}
</pre>
Пример 3: Отмена транзакции в случае возникновения ошибки:
<pre>
session.startTransaction();
try {
  // выполнение операций
  session.commitTransaction();
} catch (error) {
  session.abortTransaction();
}
</pre>