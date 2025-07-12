import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'dart:developer';

import '../models/user.dart';
import '../services/auth_service.dart';

class AuthNotifier extends StateNotifier<AsyncValue<User?>> {
  AuthNotifier() : super(const AsyncValue.data(null)) {
    _checkExistingSession();
  }

  final AuthService _authService = AuthService();

  /// Check if user has an existing session on app startup
  Future<void> _checkExistingSession() async {
    try {
      state = const AsyncValue.loading();
      
      await _authService.initialize();
      final isLoggedIn = await _authService.isUserLoggedIn();
      
      if (isLoggedIn) {
        // User has existing session, recreate User object
        final user = await _authService.signInWithGoogle(); // This will use existing session
        state = AsyncValue.data(user);
        log('Existing session restored for user: ${user.email}');
      } else {
        state = const AsyncValue.data(null);
        log('No existing session found');
      }
    } catch (e) {
      log('Error checking existing session: $e');
      state = const AsyncValue.data(null);
    }
  }

  /// Sign in with Google using Web3Auth
  Future<void> signInWithGoogle() async {
    try {
      state = const AsyncValue.loading();
      
      final user = await _authService.signInWithGoogle();
      state = AsyncValue.data(user);
      
      log('User signed in successfully: ${user.email}');
    } catch (e) {
      log('Sign-in failed: $e');
      state = AsyncValue.error(e, StackTrace.current);
      rethrow;
    }
  }

  /// Sign out the current user
  Future<void> signOut() async {
    try {
      await _authService.signOut();
      state = const AsyncValue.data(null);
      log('User signed out successfully');
    } catch (e) {
      log('Sign-out failed: $e');
      rethrow;
    }
  }

  /// Get the current user (null if not authenticated)
  User? get currentUser {
    return state.value;
  }

  /// Check if user is currently authenticated
  bool get isAuthenticated {
    return state.value != null;
  }

  /// Check if authentication is in progress
  bool get isLoading {
    return state.isLoading;
  }

  /// Get authentication error if any
  Object? get error {
    return state.hasError ? state.error : null;
  }

  /// Refresh user session
  Future<void> refreshSession() async {
    await _checkExistingSession();
  }
}

final authProvider = StateNotifierProvider<AuthNotifier, AsyncValue<User?>>((ref) {
  return AuthNotifier();
});

/// Convenience provider to get current user
final currentUserProvider = Provider<User?>((ref) {
  return ref.watch(authProvider).value;
});

/// Convenience provider to check if user is authenticated
final isAuthenticatedProvider = Provider<bool>((ref) {
  return ref.watch(authProvider).value != null;
});