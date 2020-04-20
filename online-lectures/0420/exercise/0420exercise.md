# 4월 20일 exercise

### 1. flights 테이블 생성

```sqlite
$ sqlite3 practice.sqlite3
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite> .tables
sqlite> CREATE TABLE flights(
   ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
   ...> flight_num TEXT NOT NULL,
   ...> departure TEXT NOT NULL,
   ...> waypoint TEXT NOT NULL,
   ...> arrival TEXT NOT NULL, 
   ...> price INTEGER NOT NULL
   ...> );
```

### 2. 데이터 입력

```sqlite
sqlite> INSERT INTO flights (flight_num, departure, waypoint, arrival, price)
   ...> VALUES('RT9122','Madrid','Beijing','Incheon',200);
sqlite> INSERT INTO flights (flight_num, departure, waypoint, arrival, price)
   ...> VALUES('XZ0352','LA','Moscow','Incheon',800);
sqlite> INSERT INTO flights (flight_num, departure, waypoint, arrival, price)
   ...> VALUES('XQ0972','London','Beijing','Sydney',500);
```

### 3. 테이블 전체 데이터 조회

```sqlite
SELECT * FROM flights;
id | flight_num | departure | waypoint | arrival | price
1 | RT9122 | Madrid | Beijing | Incheon | 200
2 | XZ0352 | LA | Moscow | Incheon | 800
3 | SQ0972 | London | Beijing | Sydney | 500
```

### 4. 모든 waypoint 조회

```sqlite
sqlite> SELECT waypoint FROM flights;
waypoint
Beijing
Moscow
Beijing

--(중복 없이)
sqlite> SELECT DISTINCT waypoint FROM flights;               
waypoint
Beijing
Moscow
```

### 5. 항공권 가격 600미만인 항공편의 id와 flight_num 조회

```sqlite
sqlite> SELECT id, flight_num FROM flights WHERE price < 600;
id | flight_num
1 | RT9122
3 | SQ0972
```

### 6. 도착지가 Incheon이고 가격이 500 이상인 항공편의 departure 조회

```sqlite
sqlite> SELECT departure FROM flights WHERE arrival = 'Incheon' AND price >= 500;
departure
LA
```

### 7. 항공편의 숫자부분이 0으로 시작하고 2로 끝나면서, 경유지가 Beiging인 항공편들의 id와 flight_num 조회

```sqlite
sqlite> SELECT id, flight_num FROM flights
   ...> WHERE flight_num LIKE '%0%2' AND waypoint = 'Beijing';
id | flight_num
3 | SQ0972
```

### 8. SQ0972의 경유지를 Tokyo로  수정

```sqlite
sqlite> UPDATE flights
   ...> SET waypoint = 'Tokyo'
   ...> WHERE flight_num = 'SQ0972';
   
sqlite> SELECT * FROM flights;
id | flight_num | departure | waypoint | arrival | price
1 | RT9122 | Madrid | Beijing | Incheon | 200
2 | XZ0352 | LA | Moscow | Incheon | 800
3 | SQ0972 | London | Tokyo | Sydney | 500
```

### 9. RT9122를 테이블에서 삭제

```sqlite
sqlite> DELETE
   ...> FROM flights
   ...> WHERE flight_num = 'RT9122';
   
sqlite> SELECT * FROM flights;
id | flight_num | departure | waypoint | arrival | price
2 | XZ0352 | LA | Moscow | Incheon | 800
3 | SQ0972 | London | Tokyo | Sydney | 500
```

### 10. flights 테이블 삭제

```sqlite
sqlite> DROP TABLE flights;
sqlite> .table
sqlite> 
```