# 🚀 AstraTrade - Advanced Web3 Trading Platform

[![Flutter](https://img.shields.io/badge/Flutter-3.32.5-blue.svg)](https://flutter.dev/)
[![Dart](https://img.shields.io/badge/Dart-3.8.0-blue.svg)](https://dart.dev/)
[![Web3Auth](https://img.shields.io/badge/Web3Auth-6.2.0-green.svg)](https://web3auth.io/)
[![Starknet](https://img.shields.io/badge/Starknet-Ready-orange.svg)](https://starknet.io/)

AstraTrade is a cutting-edge Web3 trading platform that combines seamless social authentication with powerful blockchain technology. Built with Flutter for cross-platform compatibility and integrated with Starknet for efficient trading operations.

## 🌟 Features

### ✅ Implemented (v1.0.0)
- **🔐 Web3Auth Integration**: Seamless Google OAuth login with automatic wallet creation
- **🎨 Modern UI**: Cyberpunk-themed interface with Material Design 3
- **📱 Cross-Platform**: Native iOS, Android, Web, Desktop support
- **🔗 Starknet Ready**: Blockchain integration foundation with account management
- **🏗️ Clean Architecture**: Modular design with Riverpod state management
- **🧪 RAG System**: AI-powered knowledge base for development assistance

### 🚧 In Development
- **📊 Portfolio Analytics**: Real-time trading insights and performance metrics
- **💱 Advanced Trading**: Limit orders, stop-loss, and algorithmic trading
- **🔒 Enhanced Security**: Multi-factor authentication and hardware wallet support
- **📈 Market Data**: Live price feeds and technical analysis tools

## 🏗️ Architecture

```
astratrade_app/
├── 📁 lib/
│   ├── 🔌 api/                 # External API clients
│   ├── 📊 models/              # Data models with JSON serialization
│   ├── 🔄 providers/           # Riverpod state management
│   ├── 📺 screens/             # UI screens and pages
│   ├── ⚙️ services/            # Business logic and external integrations
│   ├── 🛠️ utils/               # Utility functions and constants
│   └── 🎨 widgets/             # Reusable UI components
├── 📁 knowledge_base/          # RAG system for AI assistance
└── 📁 platform/               # Platform-specific configurations
```

## 🚀 Quick Start

### Prerequisites

- **Flutter SDK**: 3.32.5 or higher
- **Dart SDK**: 3.8.0 or higher
- **iOS Development**: Xcode 14+ (for iOS builds)
- **Android Development**: Android Studio with API 26+ support

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-org/astratrade-project.git
   cd AstraTrade-Project/astratrade_app
   ```

2. **Install dependencies**
   ```bash
   flutter pub get
   dart run build_runner build
   ```

3. **Configure Web3Auth** (Required for authentication)
   ```bash
   # Get your client ID from https://dashboard.web3auth.io
   # Update lib/services/auth_service.dart:
   # Replace 'YOUR_WEB3AUTH_CLIENT_ID' with your actual client ID
   ```

4. **Run the application**
   ```bash
   flutter run
   ```

## ⚙️ Configuration

### Web3Auth Setup

1. **Create Web3Auth Account**
   - Visit [Web3Auth Dashboard](https://dashboard.web3auth.io)
   - Create a new project
   - Note your Client ID

2. **Configure Redirect URLs**
   
   **iOS (`ios/Runner/Info.plist`):**
   ```xml
   <key>CFBundleURLTypes</key>
   <array>
     <dict>
       <key>CFBundleURLName</key>
       <string>astratrade.auth</string>
       <key>CFBundleURLSchemes</key>
       <array>
         <string>astratrade</string>
       </array>
     </dict>
   </array>
   ```

   **Android (`android/app/src/main/AndroidManifest.xml`):**
   ```xml
   <activity
       android:name=".MainActivity"
       android:exported="true"
       android:launchMode="singleTop"
       android:theme="@style/LaunchTheme">
       <intent-filter android:autoVerify="true">
           <action android:name="android.intent.action.VIEW" />
           <category android:name="android.intent.category.DEFAULT" />
           <category android:name="android.intent.category.BROWSABLE" />
           <data android:scheme="astratrade" />
       </intent-filter>
   </activity>
   ```

3. **Update Configuration**
   ```dart
   // lib/services/auth_service.dart
   static const String _clientId = 'YOUR_ACTUAL_CLIENT_ID';
   ```

### RAG System (Optional Development Aid)

The project includes an AI-powered knowledge base for development assistance:

```bash
cd knowledge_base/backend
docker-compose up -d
# RAG system available at http://localhost:8000
```

## 🧪 Testing

```bash
# Run all tests
flutter test

# Run with coverage
flutter test --coverage

# Run specific test
flutter test test/widget_test.dart

# Analyze code quality
flutter analyze
```

## 📱 Platform-Specific Notes

### iOS
- **Minimum Version**: iOS 14.0+
- **Required**: Xcode 14.4+ for building
- **Setup**: Run `pod install` in the `ios/` directory

### Android
- **Minimum SDK**: API Level 26 (Android 8.0)
- **Target SDK**: API Level 34
- **Required**: Android Studio 2023.1.1+

### Web
- **Browser Support**: Chrome 90+, Firefox 88+, Safari 14+
- **PWA Ready**: Installable as progressive web app

## 🔐 Security Features

- **Social Authentication**: Secure OAuth with major providers
- **Non-Custodial Wallets**: Users control their private keys
- **Encrypted Storage**: Sensitive data protection at rest
- **Network Security**: HTTPS/TLS for all communications
- **Code Signing**: Verified application integrity

## 🛠️ Development

### Code Generation
```bash
# Generate JSON serialization code
dart run build_runner build

# Watch for changes
dart run build_runner watch
```

### State Management
AstraTrade uses **Riverpod** for state management:

```dart
// Reading state
final user = ref.watch(currentUserProvider);

// Updating state
await ref.read(authProvider.notifier).signInWithGoogle();
```

### Adding New Features

1. **Create Model** (`lib/models/`)
2. **Add Service** (`lib/services/`)
3. **Create Provider** (`lib/providers/`)
4. **Build UI** (`lib/screens/` & `lib/widgets/`)
5. **Write Tests** (`test/`)

## 📚 Knowledge Base Integration

AstraTrade includes a RAG (Retrieval-Augmented Generation) system for development assistance:

```bash
# Query the knowledge base
curl -X POST "http://localhost:8000/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "Web3Auth Flutter integration", "max_results": 3}'
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch** (`git checkout -b feature/amazing-feature`)
3. **Follow code style** (use `flutter analyze` and `dart format`)
4. **Write tests** for new functionality
5. **Commit changes** (`git commit -m 'Add amazing feature'`)
6. **Push to branch** (`git push origin feature/amazing-feature`)
7. **Open Pull Request**

### Code Style Guidelines

- **Dart/Flutter**: Follow [Effective Dart](https://dart.dev/guides/language/effective-dart)
- **Naming**: Use descriptive names for classes, methods, and variables
- **Documentation**: Add doc comments for public APIs
- **Testing**: Maintain 80%+ test coverage

## 📋 Project Roadmap

### Phase 1: Core Authentication ✅
- [x] Web3Auth integration
- [x] User onboarding flow
- [x] Starknet wallet creation
- [x] Basic UI framework

### Phase 2: Trading Infrastructure 🚧
- [ ] Market data integration
- [ ] Order management system
- [ ] Portfolio tracking
- [ ] Transaction history

### Phase 3: Advanced Features 📋
- [ ] Algorithmic trading
- [ ] Social trading features
- [ ] Advanced analytics
- [ ] Multi-chain support

### Phase 4: Enterprise Features 📋
- [ ] API for external developers
- [ ] White-label solutions
- [ ] Institutional features
- [ ] Advanced security

## 🔧 Troubleshooting

### Common Issues

**Build Errors:**
```bash
# Clean and rebuild
flutter clean
flutter pub get
dart run build_runner build --delete-conflicting-outputs
```

**Web3Auth Issues:**
- Verify client ID configuration
- Check redirect URL setup
- Ensure platform-specific configurations are correct

**Dependency Conflicts:**
```bash
# Update dependencies
flutter pub upgrade
flutter pub deps
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Flutter Team** for the amazing cross-platform framework
- **Web3Auth** for seamless Web3 authentication
- **Starknet** for efficient blockchain infrastructure
- **Riverpod** for excellent state management
- **Open Source Community** for countless helpful packages

## 📞 Support

- **Documentation**: [Project Wiki](https://github.com/your-org/astratrade-project/wiki)
- **Issues**: [GitHub Issues](https://github.com/your-org/astratrade-project/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/astratrade-project/discussions)
- **Email**: support@astratrade.io

---

<div align="center">

**Built with ❤️ by the AstraTrade Team**

[Website](https://astratrade.io) • [Documentation](https://docs.astratrade.io) • [Twitter](https://twitter.com/astratrade)

</div>