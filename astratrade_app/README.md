# AstraTrade App

AstraTrade is a cross-platform, gamified trading simulation app built with Flutter. It features a cyberpunk-themed UI, XP and leaderboard systems, and integration with Web3Auth and Starknet. The app is designed for both mobile and desktop, providing a fun and educational trading experience.

## Features
- Google OAuth login with Web3Auth wallet creation
- Cross-platform Flutter architecture (Android, iOS, Web, Desktop)
- Cyberpunk-themed Material Design 3 interface
- XP & Gamification: streak tracking, levels, and rewards
- Live leaderboard ranking by trading performance
- Planet/Ecosystem visual that evolves with user activity
- Gas-free experience via paymaster integration
- Mobile-optimized: smooth 60fps performance
- Comprehensive test suite

## Getting Started

### Prerequisites
- Flutter SDK (3.8.1 or later)
- Dart SDK
- Node.js (for some web features)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/trungkien1992/AstraTrade-Project.git
   cd AstraTrade-Project/astratrade_app
   ```
2. Install dependencies:
   ```bash
   flutter pub get
   ```
3. Run the app:
   - For mobile:
     ```bash
     flutter run
     ```
   - For web:
     ```bash
     flutter run -d chrome
     ```
   - For desktop:
     ```bash
     flutter run -d macos  # or windows, linux
     ```

### Configuration
- Update `lib/utils/constants.dart` for environment and branding settings.
- See `CONFIGURATION.md` for detailed setup (Web3Auth, API endpoints, etc).

## Project Structure
- `lib/` — Main Flutter app code
- `test/` — Widget and integration tests
- `android/`, `ios/`, `web/`, `macos/`, `linux/`, `windows/` — Platform-specific code

## Status
- **Current Version:** v1.0.0
- **Core features implemented:**
  - Web3Auth login
  - Gamification (XP, streaks, levels)
  - Leaderboard
  - Trading simulation
  - Paymaster integration
- **Planned:**
  - Real trading API integration
  - More advanced gamification and visuals

## License
MIT

---
For more details, see the in-app documentation or contact the project maintainer.