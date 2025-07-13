# AstraTrade Project

This is the official repository for the AstraTrade app—a cross-platform, gamified trading simulation built with Flutter. This README provides the main documentation for the entire project.

## Project Overview
AstraTrade is a cyberpunk-themed trading simulation app featuring:
- Google OAuth login with Web3Auth wallet creation
- XP, streak, and leaderboard gamification
- Live trading simulation (with future real trading API integration)
- Paymaster integration for gas-free experience
- Mobile, web, and desktop support

## Getting Started

### Prerequisites
- Flutter SDK (3.8.1 or later)
- Dart SDK
- Node.js (for some web features)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/trungkien1992/AstraTrade-Project.git
   cd AstraTrade-Project
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
- See `astratrade_app/CONFIGURATION.md` for detailed setup (Web3Auth, API endpoints, etc).

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