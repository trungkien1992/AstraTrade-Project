import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:hive_flutter/hive_flutter.dart';

import 'screens/splash_screen.dart';
import 'screens/login_screen.dart';
import 'screens/main_hub_screen.dart';
import 'providers/auth_provider.dart';
import 'utils/constants.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Initialize Hive for local storage
  await Hive.initFlutter();
  
  runApp(
    const ProviderScope(
      child: AstraTradeApp(),
    ),
  );
}

class AstraTradeApp extends ConsumerWidget {
  const AstraTradeApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return MaterialApp(
      title: AppConstants.appName,
      debugShowCheckedModeBanner: false,
      theme: _buildTheme(),
      home: const AuthNavigator(),
    );
  }

  ThemeData _buildTheme() {
    return ThemeData(
      useMaterial3: true,
      brightness: Brightness.dark,
      colorScheme: ColorScheme.fromSeed(
        seedColor: Colors.purple,
        brightness: Brightness.dark,
      ),
      textTheme: GoogleFonts.rajdhaniTextTheme(
        ThemeData.dark().textTheme,
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: Colors.transparent,
        elevation: 0,
        titleTextStyle: GoogleFonts.orbitron(
          fontSize: 20,
          fontWeight: FontWeight.bold,
          color: Colors.white,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.purple.shade600,
          foregroundColor: Colors.white,
          elevation: 8,
          shadowColor: Colors.purple.withValues(alpha: 0.3),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
      cardTheme: CardThemeData(
        color: Colors.grey.shade900,
        elevation: 8,
        shadowColor: Colors.black.withValues(alpha: 0.3),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
        ),
      ),
    );
  }
}

/// Handles navigation based on authentication state
class AuthNavigator extends ConsumerStatefulWidget {
  const AuthNavigator({super.key});

  @override
  ConsumerState<AuthNavigator> createState() => _AuthNavigatorState();
}

class _AuthNavigatorState extends ConsumerState<AuthNavigator> {
  bool _showSplash = true;

  @override
  void initState() {
    super.initState();
    // Show splash screen for configured duration
    Future.delayed(const Duration(seconds: AppConstants.splashDurationSeconds), () {
      if (mounted) {
        setState(() {
          _showSplash = false;
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_showSplash) {
      return const SplashScreen();
    }

    final authState = ref.watch(authProvider);

    return authState.when(
      loading: () => const SplashScreen(), // Show splash while checking auth
      error: (error, stack) => const LoginScreen(), // Show login on error
      data: (user) {
        if (user != null) {
          return const MainHubScreen(); // User is authenticated
        } else {
          return const LoginScreen(); // User needs to authenticate
        }
      },
    );
  }
}
