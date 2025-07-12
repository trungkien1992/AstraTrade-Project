import 'dart:developer';
import 'dart:collection';
import 'package:web3auth_flutter/web3auth_flutter.dart';
import 'package:web3auth_flutter/enums.dart';
import 'package:web3auth_flutter/input.dart';
import 'package:web3auth_flutter/output.dart';

import '../models/user.dart';
import '../utils/constants.dart';
import 'starknet_service.dart';

class AuthService {
  static const String _clientId = AppConstants.web3AuthClientId;
  static const String _redirectUrl = AppConstants.web3AuthRedirectUrl;
  
  bool _isInitialized = false;
  final StarknetService _starknetService = StarknetService();

  Future<void> initialize() async {
    if (_isInitialized) return;

    try {
      await Web3AuthFlutter.init(
        Web3AuthOptions(
          clientId: _clientId,
          network: Network.sapphire_devnet, // Use testnet for development
          redirectUrl: Uri.parse(_redirectUrl),
          whiteLabel: WhiteLabelData(
            appName: AppConstants.appName,
            logoLight: "https://your-logo-url.com/logo-light.png", // TODO: Add actual logo URLs
            logoDark: "https://your-logo-url.com/logo-dark.png",
            defaultLanguage: Language.en,
            mode: ThemeModes.dark,
            theme: HashMap.from({
              "primary": "#7B2CBF", // Purple theme to match AstraTrade
            }),
          ),
        ),
      );
      
      _isInitialized = true;
      log('Web3Auth initialized successfully');
    } catch (e) {
      log('Web3Auth initialization failed: $e');
      rethrow;
    }
  }

  Future<User> signInWithGoogle() async {
    if (!_isInitialized) {
      await initialize();
    }

    try {
      // Attempt to initialize existing session first
      try {
        await Web3AuthFlutter.initialize();
        final privateKey = await Web3AuthFlutter.getPrivKey();
        if (privateKey.isNotEmpty) {
          final userInfo = await Web3AuthFlutter.getUserInfo();
          return await _createUserFromWeb3AuthInfo(userInfo, privateKey);
        }
      } catch (e) {
        log('No existing session found, proceeding with login');
      }

      // Perform fresh login
      await Web3AuthFlutter.login(
        LoginParams(
          loginProvider: Provider.google,
          extraLoginOptions: ExtraLoginOptions(
            domain: AppConstants.web3AuthDomain,
            prompt: Prompt.login,
          ),
        ),
      );

      final privateKey = await Web3AuthFlutter.getPrivKey();
      if (privateKey.isEmpty) {
        throw Exception('Failed to retrieve private key from Web3Auth');
      }

      final userInfo = await Web3AuthFlutter.getUserInfo();
      return await _createUserFromWeb3AuthInfo(userInfo, privateKey);
    } on UserCancelledException {
      throw Exception('User cancelled the login process');
    } on UnKnownException {
      throw Exception('Unknown error occurred during login');
    } catch (e) {
      log('Sign-in failed: $e');
      throw Exception('Sign-in failed: ${e.toString()}');
    }
  }

  Future<User> _createUserFromWeb3AuthInfo(TorusUserInfo userInfo, String privateKey) async {
    try {
      // Create Starknet account from private key
      final starknetAddress = await _starknetService.createAccountFromPrivateKey(privateKey);

      // Create User object
      final user = User(
        id: userInfo.verifierId ?? 'unknown',
        email: userInfo.email ?? 'unknown@email.com',
        name: userInfo.name ?? 'Unknown User',
        profilePicture: userInfo.profileImage,
        starknetAddress: starknetAddress,
        privateKey: privateKey, // TODO: Encrypt this in production
        createdAt: DateTime.now(),
        lastLoginAt: DateTime.now(),
      );

      log('User created successfully: ${user.toString()}');
      return user;
    } catch (e) {
      log('Failed to create user from Web3Auth info: $e');
      rethrow;
    }
  }

  Future<void> signOut() async {
    try {
      await Web3AuthFlutter.logout();
      log('User signed out successfully');
    } catch (e) {
      log('Sign-out failed: $e');
      throw Exception('Sign-out failed: ${e.toString()}');
    }
  }

  Future<bool> isUserLoggedIn() async {
    if (!_isInitialized) return false;
    
    try {
      await Web3AuthFlutter.initialize();
      final privateKey = await Web3AuthFlutter.getPrivKey();
      return privateKey.isNotEmpty;
    } catch (e) {
      return false;
    }
  }

  Future<String?> getPrivateKey() async {
    try {
      final response = await Web3AuthFlutter.getPrivKey();
      return response;
    } catch (e) {
      log('Failed to get private key: $e');
      return null;
    }
  }
}