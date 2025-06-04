import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  String message = 'Checking API...';

  @override
  void initState() {
    super.initState();
    checkApi();
  }

  Future<void> checkApi() async {
    try {
      final res = await http.get(Uri.parse(const String.fromEnvironment('API_URL', defaultValue: 'http://localhost:8000') + '/dar_reports/'));
      setState(() {
        message = res.statusCode == 200 ? 'API Connected' : 'API Error';
      });
    } catch (_) {
      setState(() { message = 'API Error'; });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GuardsPro',
      home: Scaffold(
        appBar: AppBar(title: const Text('GuardsPro')),
        body: Center(child: Text(message)),
      ),
    );
  }
}
