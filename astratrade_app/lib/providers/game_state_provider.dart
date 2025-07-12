import 'package:flutter/foundation.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../services/game_service.dart';
import '../widgets/planet_view.dart';
import '../api/rag_api_client.dart';
import '../models/leaderboard.dart';
import '../services/leaderboard_service.dart';

/// Player game state data model
class GameState {
  final int stellarShards;
  final int lumina;
  final int experience;
  final int totalXP;
  final int level;
  final PlanetHealth planetHealth;
  final int astroForgers;
  final bool hasGenesisIgnition;
  final String lastTradeMessage;
  final DateTime lastActivity;
  final Map<String, int> cosmicNodes;
  final int totalTrades;
  final int winStreak;
  final double winRate;
  final CosmicTier cosmicTier;

  const GameState({
    this.stellarShards = 50,
    this.lumina = 0,
    this.experience = 0,
    this.totalXP = 0,
    this.level = 1,
    this.planetHealth = PlanetHealth.stable,
    this.astroForgers = 1,
    this.hasGenesisIgnition = false,
    this.lastTradeMessage = "Welcome to the Cosmic Trading Journey!",
    required this.lastActivity,
    this.cosmicNodes = const {},
    this.totalTrades = 0,
    this.winStreak = 0,
    this.winRate = 0.0,
    this.cosmicTier = CosmicTier.stellarSeedling,
  });

  GameState copyWith({
    int? stellarShards,
    int? lumina,
    int? experience,
    int? totalXP,
    int? level,
    PlanetHealth? planetHealth,
    int? astroForgers,
    bool? hasGenesisIgnition,
    String? lastTradeMessage,
    DateTime? lastActivity,
    Map<String, int>? cosmicNodes,
    int? totalTrades,
    int? winStreak,
    double? winRate,
    CosmicTier? cosmicTier,
  }) {
    return GameState(
      stellarShards: stellarShards ?? this.stellarShards,
      lumina: lumina ?? this.lumina,
      experience: experience ?? this.experience,
      totalXP: totalXP ?? this.totalXP,
      level: level ?? this.level,
      planetHealth: planetHealth ?? this.planetHealth,
      astroForgers: astroForgers ?? this.astroForgers,
      hasGenesisIgnition: hasGenesisIgnition ?? this.hasGenesisIgnition,
      lastTradeMessage: lastTradeMessage ?? this.lastTradeMessage,
      lastActivity: lastActivity ?? this.lastActivity,
      cosmicNodes: cosmicNodes ?? this.cosmicNodes,
      totalTrades: totalTrades ?? this.totalTrades,
      winStreak: winStreak ?? this.winStreak,
      winRate: winRate ?? this.winRate,
      cosmicTier: cosmicTier ?? this.cosmicTier,
    );
  }

  /// Calculate player's cosmic power (CP) based on various factors
  int get cosmicPower {
    int basePower = stellarShards ~/ 10;
    int luminaPower = lumina * 50;
    int experiencePower = experience ~/ 5;
    int forgerPower = astroForgers * 25;
    int nodePower = cosmicNodes.values.fold(0, (sum, level) => sum + (level * 100));
    
    return basePower + luminaPower + experiencePower + forgerPower + nodePower;
  }

  /// Get player's cosmic tier display name based on their power level
  String get cosmicTierDisplayName {
    return cosmicTier.displayName;
  }

  /// Check if player can afford an upgrade
  bool canAfford({int? stellarShardsCost, int? luminaCost}) {
    if (stellarShardsCost != null && stellarShards < stellarShardsCost) {
      return false;
    }
    if (luminaCost != null && lumina < luminaCost) {
      return false;
    }
    return true;
  }
}

/// Game state notifier that manages all game state changes
class GameStateNotifier extends StateNotifier<GameState> {
  GameStateNotifier() : super(GameState(lastActivity: DateTime.now())) {
    _startAutoForging();
    _checkRagConnection();
  }

  final GameService _gameService = GameService();
  final LeaderboardService _leaderboardService = LeaderboardService();
  
  /// Check RAG backend connection status
  Future<void> _checkRagConnection() async {
    try {
      final ragClient = RagApiClient();
      await ragClient.healthCheck();
      ragClient.dispose();
    } catch (e) {
      // RAG connection failed, will fall back to mock data
      // In production, this would be logged to a proper logging service
      debugPrint('RAG connection check failed: $e');
    }
  }

  /// Perform a Quick Trade operation with enhanced error handling and XP system
  Future<void> performQuickTrade() async {
    try {
      final result = await _gameService.performQuickTrade();
      
      // Calculate XP gained based on trade result
      final xpGained = XPCalculator.calculateTradeXP(
        isProfit: result.outcome == TradeOutcome.profit,
        isCriticalForge: result.isCriticalForge,
        isRealTrade: false, // This is simulation trade
        winStreak: state.winStreak,
        profitPercentage: result.profitPercentage,
      );
      
      // Update state based on trade result
      final newStellarShards = state.stellarShards + result.stellarShardsGained;
      final newLumina = state.lumina + result.luminaGained;
      final newExperience = state.experience + (result.isCriticalForge ? 20 : 10);
      final newTotalXP = state.totalXP + xpGained;
      final newTotalTrades = state.totalTrades + 1;
      
      // Update win streak
      int newWinStreak = state.winStreak;
      if (result.outcome == TradeOutcome.profit) {
        newWinStreak += 1;
      } else if (result.outcome == TradeOutcome.loss) {
        newWinStreak = 0;
      }
      
      // Calculate new level and cosmic tier
      final newLevel = XPCalculator.calculateLevel(newTotalXP);
      final newCosmicTier = CosmicTier.fromXP(newTotalXP);
      
      // Calculate win rate
      final profitableTrades = result.outcome == TradeOutcome.profit ? 1 : 0;
      final newWinRate = newTotalTrades > 0 
          ? ((state.winRate * state.totalTrades) + profitableTrades) / newTotalTrades
          : 0.0;
      
      // Check for level up
      final didLevelUp = newLevel > state.level;
      final didTierUp = newCosmicTier != state.cosmicTier;
      
      // Determine new planet health based on recent performance
      PlanetHealth newPlanetHealth = _calculatePlanetHealth(
        result.outcome,
        newWinStreak,
        newTotalTrades,
      );
      
      // Build level up message if applicable
      String finalMessage = result.outcomeMessage;
      if (didLevelUp) {
        finalMessage += "\n🎉 LEVEL UP! You've reached Level $newLevel!";
      }
      if (didTierUp) {
        finalMessage += "\n✨ COSMIC ASCENSION! You are now ${newCosmicTier.displayName}!";
      }
      if (xpGained > 0) {
        finalMessage += "\n+$xpGained XP gained!";
      }
      
      state = state.copyWith(
        stellarShards: newStellarShards,
        lumina: newLumina,
        experience: newExperience,
        totalXP: newTotalXP,
        level: newLevel,
        cosmicTier: newCosmicTier,
        planetHealth: newPlanetHealth,
        lastTradeMessage: finalMessage,
        lastActivity: DateTime.now(),
        totalTrades: newTotalTrades,
        winStreak: newWinStreak,
        winRate: newWinRate,
      );
      
      // Update leaderboard with new stats
      _leaderboardService.updateCurrentUserStats(
        stellarShards: newStellarShards,
        lumina: newLumina,
        totalXP: newTotalXP,
        winStreak: newWinStreak,
        totalTrades: newTotalTrades,
        winRate: newWinRate,
      );
      
      // Trigger Genesis Ignition if this is the first profitable trade
      if (!state.hasGenesisIgnition && result.outcome == TradeOutcome.profit) {
        _triggerGenesisIgnition();
      }
      
    } catch (e) {
      // Handle trade error with detailed messaging
      String errorMessage;
      if (e is RagApiException) {
        errorMessage = "Cosmic Network Disruption: ${e.message}";
      } else {
        errorMessage = "Cosmic Interference Detected: ${e.toString()}";
      }
      
      state = state.copyWith(
        lastTradeMessage: errorMessage,
        lastActivity: DateTime.now(),
      );
      
      // Re-throw for UI handling
      rethrow;
    }
  }

  /// Perform manual stellar forge (planet tap)
  Future<void> performManualForge() async {
    final reward = await _gameService.performStellarForge(isManualTap: true);
    final efficiency = _gameService.calculateForgerEfficiency(state.planetHealth.name);
    final finalReward = (reward * efficiency).round();
    
    state = state.copyWith(
      stellarShards: state.stellarShards + finalReward,
      experience: state.experience + 2,
      lastActivity: DateTime.now(),
    );
  }

  /// Purchase additional Astro-Forger
  void purchaseAstroForger() {
    final cost = _calculateAstroForgerCost();
    if (state.canAfford(stellarShardsCost: cost)) {
      state = state.copyWith(
        stellarShards: state.stellarShards - cost,
        astroForgers: state.astroForgers + 1,
        lastActivity: DateTime.now(),
      );
    }
  }

  /// Activate/upgrade a Cosmic Genesis Node
  void upgradeCosmicNode(String nodeType) {
    final cost = _calculateNodeUpgradeCost(nodeType);
    if (state.canAfford(luminaCost: cost)) {
      final currentLevel = state.cosmicNodes[nodeType] ?? 0;
      final newNodes = Map<String, int>.from(state.cosmicNodes);
      newNodes[nodeType] = currentLevel + 1;
      
      state = state.copyWith(
        lumina: state.lumina - cost,
        cosmicNodes: newNodes,
        lastActivity: DateTime.now(),
      );
    }
  }

  /// Trigger Genesis Ignition (Pro Trader activation)
  void _triggerGenesisIgnition() {
    state = state.copyWith(
      hasGenesisIgnition: true,
      lumina: state.lumina + 25, // Lumina Cascade bonus
      lastTradeMessage: "🌟 GENESIS IGNITION ACHIEVED! Welcome to Pro Trading! 🌟",
      planetHealth: PlanetHealth.flourishing,
    );
  }

  /// Calculate planet health based on recent trading performance
  PlanetHealth _calculatePlanetHealth(
    TradeOutcome lastOutcome,
    int winStreak,
    int totalTrades,
  ) {
    // Calculate success rate if we have enough trades
    if (totalTrades >= 5) {
      if (winStreak >= 3) {
        return PlanetHealth.flourishing;
      } else if (winStreak >= 1 || lastOutcome != TradeOutcome.loss) {
        return PlanetHealth.stable;
      } else {
        return PlanetHealth.decaying;
      }
    }
    
    // For early trades, be more forgiving
    if (lastOutcome == TradeOutcome.profit) {
      return PlanetHealth.flourishing;
    } else if (lastOutcome == TradeOutcome.breakeven) {
      return PlanetHealth.stable;
    } else {
      return state.planetHealth; // Don't penalize immediately
    }
  }

  /// Calculate cost for next Astro-Forger
  int _calculateAstroForgerCost() {
    return 100 + (state.astroForgers * 50);
  }

  /// Calculate cost for upgrading a Cosmic Node
  int _calculateNodeUpgradeCost(String nodeType) {
    final currentLevel = state.cosmicNodes[nodeType] ?? 0;
    return 10 + (currentLevel * 15);
  }

  /// Start auto-forging from Astro-Forgers
  void _startAutoForging() {
    // This would typically use a timer in a real implementation
    // For now, we'll simulate periodic auto-forging
    Future.delayed(const Duration(seconds: 30), () {
      if (mounted && state.astroForgers > 0) {
        _performAutoForge();
        _startAutoForging(); // Continue the cycle
      }
    });
  }

  /// Perform automatic stellar forge from Astro-Forgers
  Future<void> _performAutoForge() async {
    if (state.astroForgers <= 0) return;
    
    final baseReward = await _gameService.performStellarForge(isManualTap: false);
    final efficiency = _gameService.calculateForgerEfficiency(state.planetHealth.name);
    final totalReward = (baseReward * state.astroForgers * efficiency).round();
    
    state = state.copyWith(
      stellarShards: state.stellarShards + totalReward,
      experience: state.experience + 1,
      lastActivity: DateTime.now(),
    );
  }

  /// Update game state from real trade result with enhanced XP system
  void updateFromRealTrade(TradeResult result) {
    // Calculate XP gained for real trade (higher rewards)
    final xpGained = XPCalculator.calculateTradeXP(
      isProfit: result.outcome == TradeOutcome.profit,
      isCriticalForge: result.isCriticalForge,
      isRealTrade: true, // Real trade gets higher XP
      winStreak: state.winStreak,
      profitPercentage: result.profitPercentage,
    );
    
    // Update state based on real trade result
    final newStellarShards = state.stellarShards + result.stellarShardsGained;
    final newLumina = state.lumina + result.luminaGained;
    final newExperience = state.experience + (result.isCriticalForge ? 30 : 15); // Higher XP for real trades
    final newTotalXP = state.totalXP + xpGained;
    final newTotalTrades = state.totalTrades + 1;
    
    // Update win streak
    int newWinStreak = state.winStreak;
    if (result.outcome == TradeOutcome.profit) {
      newWinStreak += 1;
    } else if (result.outcome == TradeOutcome.loss) {
      newWinStreak = 0;
    }
    
    // Calculate new level and cosmic tier
    final newLevel = XPCalculator.calculateLevel(newTotalXP);
    final newCosmicTier = CosmicTier.fromXP(newTotalXP);
    
    // Calculate win rate
    final profitableTrades = result.outcome == TradeOutcome.profit ? 1 : 0;
    final newWinRate = newTotalTrades > 0 
        ? ((state.winRate * state.totalTrades) + profitableTrades) / newTotalTrades
        : 0.0;
    
    // Check for level up
    final didLevelUp = newLevel > state.level;
    final didTierUp = newCosmicTier != state.cosmicTier;
    
    // Determine new planet health based on real trade performance
    PlanetHealth newPlanetHealth = _calculatePlanetHealth(
      result.outcome,
      newWinStreak,
      newTotalTrades,
    );
    
    // Build enhanced message for real trades
    String finalMessage = "🚀 REAL TRADE: ${result.outcomeMessage}";
    if (didLevelUp) {
      finalMessage += "\n🎉 LEVEL UP! You've reached Level $newLevel!";
    }
    if (didTierUp) {
      finalMessage += "\n✨ COSMIC ASCENSION! You are now ${newCosmicTier.displayName}!";
    }
    if (xpGained > 0) {
      finalMessage += "\n+$xpGained XP gained! (Real Trade Bonus)";
    }
    
    state = state.copyWith(
      stellarShards: newStellarShards,
      lumina: newLumina,
      experience: newExperience,
      totalXP: newTotalXP,
      level: newLevel,
      cosmicTier: newCosmicTier,
      planetHealth: newPlanetHealth,
      lastTradeMessage: finalMessage,
      lastActivity: DateTime.now(),
      totalTrades: newTotalTrades,
      winStreak: newWinStreak,
      winRate: newWinRate,
    );
    
    // Update leaderboard with new stats
    _leaderboardService.updateCurrentUserStats(
      stellarShards: newStellarShards,
      lumina: newLumina,
      totalXP: newTotalXP,
      winStreak: newWinStreak,
      totalTrades: newTotalTrades,
      winRate: newWinRate,
    );
    
    // Trigger Genesis Ignition if this is the first profitable real trade
    if (!state.hasGenesisIgnition && result.outcome == TradeOutcome.profit) {
      _triggerGenesisIgnition();
    }
  }
  
  /// Reset game state (for testing or new game)
  void resetGameState() {
    state = GameState(lastActivity: DateTime.now());
  }

  /// Get market data for UI display
  Map<String, dynamic> getMarketData() {
    return _gameService.getMarketData();
  }
}

/// Provider for the game state
final gameStateProvider = StateNotifierProvider<GameStateNotifier, GameState>(
  (ref) => GameStateNotifier(),
);

/// Provider for market data (updates periodically)
final marketDataProvider = StreamProvider<Map<String, dynamic>>((ref) {
  return Stream.periodic(
    const Duration(seconds: 5),
    (_) => ref.read(gameStateProvider.notifier).getMarketData(),
  );
});

/// Provider for checking if player is in "Quick Trade" loading state
final isQuickTradingProvider = StateProvider<bool>((ref) => false);

/// Provider for RAG backend connection status
final ragConnectionStatusProvider = StateProvider<RagConnectionStatus>((ref) => RagConnectionStatus.unknown);

/// RAG connection status enum
enum RagConnectionStatus {
  unknown,
  connected,
  disconnected,
  connecting,
  error,
}