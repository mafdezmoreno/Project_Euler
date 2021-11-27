// To install dart:
//  brew tap dart-lang/dart
//  brew install dart

// To run a dart file:
//    dart hellodart.dart

// To compile to native file:
////    dart2native hellodart.dart -o hellodart //OLD
//   dart compile exe hellodart.dart -o hellodart //Yes, exe also for macos

// To run compiled file:
//   ./hellodart

// To compile and run at the same time
//  dart run hellodart.dart

// To compile to aot-snapshot
// dart compile aot-snapshot hellodart.dart
// dartaotruntime hellodart

main() {
  print('Hello Dart developers');
}
