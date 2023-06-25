import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home:Scaffold(
      body: SafeArea(
        child:  WebView(
        initialUrl:"https://orchid-ai.uc.r.appspot.com/",
        javascriptMode: JavascriptMode.unrestricted),
    ),
    ),
  ));
}

