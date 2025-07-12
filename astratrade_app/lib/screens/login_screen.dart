import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:google_fonts/google_fonts.dart';

import '../providers/auth_provider.dart';
import '../utils/constants.dart';
import '../widgets/pulsating_button.dart';

class LoginScreen extends ConsumerStatefulWidget {
  const LoginScreen({super.key});

  @override
  ConsumerState<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends ConsumerState<LoginScreen>
    with WidgetsBindingObserver {
  bool _isLoading = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void dispose() {
    super.dispose();
    WidgetsBinding.instance.removeObserver(this);
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    // Handle user cancellation on Android for Web3Auth
    if (state == AppLifecycleState.resumed) {
      // Web3AuthFlutter.setCustomTabsClosed(); // Will be implemented with Web3Auth
    }
  }

  Future<void> _signInWithGoogle() async {
    setState(() {
      _isLoading = true;
    });

    try {
      await ref.read(authProvider.notifier).signInWithGoogle();
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Sign-in failed: ${e.toString()}'),
            backgroundColor: Colors.red,
          ),
        );
      }
    } finally {
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0A0A0A),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Spacer(flex: 2),
              
              // AstraTrade Logo with Animation
              Container(
                width: 150,
                height: 150,
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      Colors.purple.shade400,
                      Colors.blue.shade400,
                      Colors.cyan.shade300,
                    ],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(25),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.purple.withValues(alpha: 0.4),
                      blurRadius: 30,
                      spreadRadius: 8,
                    ),
                  ],
                ),
                child: const Icon(
                  Icons.currency_bitcoin,
                  size: 80,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 40),
              
              // App Name
              Text(
                AppConstants.appName,
                style: GoogleFonts.orbitron(
                  fontSize: 36,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                  letterSpacing: 3,
                ),
              ),
              const SizedBox(height: 12),
              
              // Tagline
              Text(
                AppConstants.appDescription,
                style: GoogleFonts.rajdhani(
                  fontSize: AppConstants.subtitleFontSize,
                  color: Colors.grey.shade400,
                  letterSpacing: 1.5,
                ),
              ),
              const SizedBox(height: 8),
              
              // Subtitle
              Text(
                AppConstants.appSubtitle,
                style: GoogleFonts.rajdhani(
                  fontSize: AppConstants.captionFontSize,
                  color: Colors.grey.shade500,
                  letterSpacing: 0.8,
                ),
                textAlign: TextAlign.center,
              ),
              
              const Spacer(flex: 2),
              
              // Sign in with Google Button
              SizedBox(
                width: double.infinity,
                height: 56,
                child: PulsatingButton(
                  text: _isLoading ? 'Connecting...' : 'Sign in with Google',
                  isLoading: _isLoading,
                  onPressed: _signInWithGoogle,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 24),
              
              // Additional info
              Text(
                'Your wallet is created automatically\nNo seed phrases required',
                style: GoogleFonts.rajdhani(
                  fontSize: 12,
                  color: Colors.grey.shade600,
                  height: 1.4,
                ),
                textAlign: TextAlign.center,
              ),
              
              const Spacer(),
            ],
          ),
        ),
      ),
    );
  }
}