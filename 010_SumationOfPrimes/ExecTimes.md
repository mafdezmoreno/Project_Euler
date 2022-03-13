# Ranking

1. Swift     623 ms
2. C++       660 ms
3. Dart     1057 ms
4. Python  31762 ms 


# Python

17
142913828922
31762.403250 ms

# Dart

```
➜  dart SumationOfPrimes.dart
17
142913828922
Executed in 4735 ms

➜  dart run  SumationOfPrimes.dart
17
142913828922
Executed in 4716 ms

➜  dart compile exe SumationOfPrimes.dart -o SumationOfPrimes_dart

➜ ./SumationOfPrimes_dart 
17
142913828922
Executed in 4282 ms
```

Using the native arm M1 version (2.15.0-268.18.beta) is much faster
```
dart-beta run SumationOfPrimes.dart
17
142913828922
Executed in 1057 ms
```

# C++

```
g++ SumationOfPrimes.cpp
./a.out                 
17
1179908154
2083ms
```

With optimizations
```
g++ -O2 SumationOfPrimes.cpp
./a.out                     
17
1179908154
660ms
```
# Swift

```
swift SumationOfPrimes.swift
17
142913828922
175126.649667 ms
```

With optimizations:
```
swift -O SumationOfPrimes.swift
17
142913828922
623.294125 ms
```
