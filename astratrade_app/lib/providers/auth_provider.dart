// Authentication state management using Riverpod

import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/user.dart';

// Authentication state
final authProvider = StateNotifierProvider<AuthNotifier, AsyncValue<User?>>((ref) {
  return AuthNotifier();
});

class AuthNotifier extends StateNotifier<AsyncValue<User?>> {
  AuthNotifier() : super(const AsyncValue.data(null));
  
  // TODO: Implement Web3Auth login
  // TODO: Implement Starknet wallet connection
  // TODO: Implement logout functionality
  // TODO: Implement session persistence
}