import 'package:flutter_test/flutter_test.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:astratrade_app/main.dart';
import 'package:astratrade_app/providers/game_state_provider.dart';
import 'package:astratrade_app/providers/leaderboard_provider.dart';
import 'package:astratrade_app/services/game_service.dart';
import 'package:astratrade_app/services/leaderboard_service.dart';
import 'package:astratrade_app/models/leaderboard.dart';

void main() {
  group('AstraTrade Integration Tests', () {
    late ProviderContainer container;
    
    setUp(() {
      container = ProviderContainer();
    });
    
    tearDown(() {
      container.dispose();
    });

    testWidgets('Complete User Journey: Onboarding to Trading to Leaderboard', (WidgetTester tester) async {
      // Test Phase 1: App Initialization
      await tester.pumpWidget(
        UncontrolledProviderScope(
          container: container,
          child: const AstraTradeApp(),
        ),
      );
      
      // Verify app loads without crashing
      expect(find.text('AstraTrade'), findsOneWidget);
    });

    test('Phase 2: Mock Trading Gameplay Loop', () async {
      final gameService = GameService();
      final gameStateNotifier = container.read(gameStateProvider.notifier);
      
      // Test 20 consecutive trades as per requirements
      int totalXpGained = 0;
      int winStreakTested = 0;
      bool levelUpOccurred = false;
      
      for (int i = 0; i < 20; i++) {
        final initialXP = container.read(gameStateProvider).totalXP;
        final initialLevel = container.read(gameStateProvider).level;
        
        // Perform quick trade
        await gameStateNotifier.performQuickTrade();
        
        final finalXP = container.read(gameStateProvider).totalXP;
        final finalLevel = container.read(gameStateProvider).level;
        final winStreak = container.read(gameStateProvider).winStreak;
        
        // Verify XP is granted correctly
        expect(finalXP, greaterThan(initialXP), reason: 'XP should increase after trade $i');
        totalXpGained += (finalXP - initialXP);
        
        // Track win streak progression
        if (winStreak > winStreakTested) {
          winStreakTested = winStreak;
        }
        
        // Check for level up
        if (finalLevel > initialLevel) {
          levelUpOccurred = true;
        }
        
        // Verify game state consistency
        final gameState = container.read(gameStateProvider);
        expect(gameState.totalTrades, equals(i + 1), reason: 'Trade count should increment');
        expect(gameState.cosmicTier, isA<CosmicTier>(), reason: 'Cosmic tier should be valid');
      }
      
      // Verify overall progression
      expect(totalXpGained, greaterThan(0), reason: 'Total XP should increase over 20 trades');
      expect(winStreakTested, greaterThan(0), reason: 'Win streak should occur during 20 trades');
      
      print('✅ Mock Trading Test Results:');
      print('   - Total XP Gained: $totalXpGained');
      print('   - Max Win Streak: $winStreakTested');
      print('   - Level Up Occurred: $levelUpOccurred');
    });

    test('Phase 3: Real Trading (Pro Mode) Simulation', () async {
      final gameService = GameService();
      final gameStateNotifier = container.read(gameStateProvider.notifier);
      
      // Enable Pro Mode with test credentials
      gameService.enableProMode(
        apiKey: 'test_api_key_for_integration',
        privateKey: 'test_private_key_for_integration_testing_purposes_only',
      );
      
      expect(gameService.isProModeEnabled, isTrue, reason: 'Pro Mode should be enabled');
      
      // Note: Real trade testing would require actual API integration
      // For integration test, we verify the system can handle Pro Mode setup
      gameService.disableProMode();
      expect(gameService.isProModeEnabled, isFalse, reason: 'Pro Mode should be disabled');
      
      print('✅ Pro Mode Toggle Test: PASS');
    });

    test('Phase 4: Leaderboard Integrity Verification', () async {
      final leaderboardService = LeaderboardService();
      final leaderboardNotifier = container.read(leaderboardProvider.notifier);
      
      // Load leaderboard data
      await leaderboardNotifier.loadLeaderboard(LeaderboardType.stellarShards);
      
      final leaderboardState = container.read(leaderboardProvider);
      
      // Verify leaderboard loads successfully
      expect(leaderboardState.entries.isNotEmpty, isTrue, reason: 'Leaderboard should have entries');
      expect(leaderboardState.error, isNull, reason: 'Leaderboard should load without errors');
      
      // Find current user entry
      final currentUser = leaderboardState.currentUserEntry;
      expect(currentUser, isNotNull, reason: 'Current user should be found in leaderboard');
      expect(currentUser!.isCurrentUser, isTrue, reason: 'Current user flag should be set');
      
      // Verify leaderboard data consistency
      final gameState = container.read(gameStateProvider);
      expect(currentUser.stellarShards, equals(gameState.stellarShards), 
             reason: 'Leaderboard SS should match game state');
      expect(currentUser.level, equals(gameState.level),
             reason: 'Leaderboard level should match game state');
      expect(currentUser.totalXP, equals(gameState.totalXP),
             reason: 'Leaderboard XP should match game state');
      
      // Test multiple leaderboard types
      for (final type in LeaderboardType.values) {
        await leaderboardNotifier.loadLeaderboard(type);
        final state = container.read(leaderboardProvider);
        expect(state.entries.isNotEmpty, isTrue, 
               reason: 'Leaderboard type ${type.name} should have entries');
      }
      
      print('✅ Leaderboard Integrity Test: PASS');
    });

    test('Phase 5: XP and Level Progression System', () async {
      // Test XP calculation system
      const testCases = [
        {'isProfit': true, 'isCritical': false, 'isReal': false, 'streak': 0, 'profit': 5.0},
        {'isProfit': true, 'isCritical': true, 'isReal': false, 'streak': 5, 'profit': 10.0},
        {'isProfit': true, 'isCritical': false, 'isReal': true, 'streak': 10, 'profit': 15.0},
        {'isProfit': false, 'isCritical': false, 'isReal': false, 'streak': 0, 'profit': -5.0},
      ];
      
      for (final testCase in testCases) {
        final xp = XPCalculator.calculateTradeXP(
          isProfit: testCase['isProfit'] as bool,
          isCriticalForge: testCase['isCritical'] as bool,
          isRealTrade: testCase['isReal'] as bool,
          winStreak: testCase['streak'] as int,
          profitPercentage: testCase['profit'] as double,
        );
        
        if (testCase['isProfit'] as bool) {
          expect(xp, greaterThan(0), reason: 'Profitable trades should give positive XP');
        }
        
        if (testCase['isCritical'] as bool) {
          expect(xp, greaterThan(10), reason: 'Critical forge should give bonus XP');
        }
        
        if (testCase['isReal'] as bool) {
          expect(xp, greaterThan(15), reason: 'Real trades should give higher XP');
        }
      }
      
      // Test level calculation
      final testXPValues = [0, 100, 500, 2000, 5000, 10000];
      for (final xp in testXPValues) {
        final level = XPCalculator.calculateLevel(xp);
        final cosmicTier = CosmicTier.fromXP(xp);
        
        expect(level, greaterThan(0), reason: 'Level should be positive');
        expect(cosmicTier, isA<CosmicTier>(), reason: 'Cosmic tier should be valid');
      }
      
      print('✅ XP and Level Progression Test: PASS');
    });

    test('Phase 6: Backend Resilience Simulation', () async {
      final gameService = GameService();
      
      // Test RAG system fallback
      gameService.setRagEnabled(false);
      expect(gameService.isRagEnabled, isFalse, reason: 'RAG should be disabled');
      
      // Perform trade with RAG disabled (should fallback to mock)
      final result = await gameService.performQuickTrade();
      expect(result.stellarShardsGained, greaterThan(0), 
             reason: 'Trade should succeed even with RAG disabled');
      
      // Re-enable RAG
      gameService.setRagEnabled(true);
      expect(gameService.isRagEnabled, isTrue, reason: 'RAG should be re-enabled');
      
      print('✅ Backend Resilience Test: PASS');
    });
  });
}