import 'dart:async';
import 'dart:math' as math;
import 'package:flutter/foundation.dart';
import '../models/leaderboard.dart';

/// Service for managing leaderboard data and rankings
class LeaderboardService {
  static final LeaderboardService _instance = LeaderboardService._internal();
  factory LeaderboardService() => _instance;
  LeaderboardService._internal();

  final _random = math.Random();
  
  // Mock current user ID (in production, this would come from auth service)
  static const String currentUserId = 'current_user_123';
  
  // Cache for leaderboard data
  List<LeaderboardEntry>? _cachedStellarShardsLeaderboard;
  List<LeaderboardEntry>? _cachedLuminaLeaderboard;
  DateTime? _lastCacheUpdate;
  
  // Cache duration (5 minutes)
  static const Duration cacheExpirationDuration = Duration(minutes: 5);

  /// Get leaderboard data for the specified type
  Future<List<LeaderboardEntry>> getLeaderboardData(LeaderboardType type) async {
    // Simulate network delay
    await Future.delayed(Duration(milliseconds: 300 + _random.nextInt(700)));
    
    switch (type) {
      case LeaderboardType.stellarShards:
        return _getStellarShardsLeaderboard();
      case LeaderboardType.lumina:
        return _getLuminaLeaderboard();
      case LeaderboardType.level:
        return _getLevelLeaderboard();
      case LeaderboardType.winStreak:
        return _getWinStreakLeaderboard();
    }
  }

  /// Get current user's ranking for a specific leaderboard type
  Future<LeaderboardEntry?> getCurrentUserRanking(LeaderboardType type) async {
    final leaderboard = await getLeaderboardData(type);
    return leaderboard.firstWhere(
      (entry) => entry.isCurrentUser,
      orElse: () => throw StateError('Current user not found in leaderboard'),
    );
  }

  /// Get top players for the specified type (limit results)
  Future<List<LeaderboardEntry>> getTopPlayers(LeaderboardType type, {int limit = 10}) async {
    final leaderboard = await getLeaderboardData(type);
    return leaderboard.take(limit).toList();
  }

  /// Get players around current user's rank
  Future<List<LeaderboardEntry>> getPlayersAroundUser(LeaderboardType type, {int range = 5}) async {
    final leaderboard = await getLeaderboardData(type);
    final currentUser = leaderboard.firstWhere((entry) => entry.isCurrentUser);
    
    final startIndex = math.max(0, currentUser.rank - 1 - range);
    final endIndex = math.min(leaderboard.length, currentUser.rank + range);
    
    return leaderboard.sublist(startIndex, endIndex);
  }

  /// Update current user's stats (for real-time updates)
  void updateCurrentUserStats({
    required int stellarShards,
    required int lumina,
    required int totalXP,
    required int winStreak,
    required int totalTrades,
    required double winRate,
  }) {
    // In a real app, this would update the backend
    // For now, we'll just invalidate the cache
    _invalidateCache();
    
    debugPrint('Updated current user stats: SS=$stellarShards, LM=$lumina, XP=$totalXP');
  }

  /// Invalidate cached data to force refresh
  void _invalidateCache() {
    _cachedStellarShardsLeaderboard = null;
    _cachedLuminaLeaderboard = null;
    _lastCacheUpdate = null;
  }

  /// Check if cache is still valid
  bool _isCacheValid() {
    if (_lastCacheUpdate == null) return false;
    return DateTime.now().difference(_lastCacheUpdate!) < cacheExpirationDuration;
  }

  /// Generate Stellar Shards leaderboard (Trade Token Leaderboard)
  List<LeaderboardEntry> _getStellarShardsLeaderboard() {
    if (_cachedStellarShardsLeaderboard != null && _isCacheValid()) {
      return _cachedStellarShardsLeaderboard!;
    }

    final entries = <LeaderboardEntry>[];
    
    // Generate mock leaderboard data
    final mockUsers = _generateMockUsers();
    
    // Add current user with moderate stats (around middle of pack)
    final currentUserEntry = LeaderboardEntry(
      userId: currentUserId,
      username: 'CosmicTrader',
      avatarUrl: 'https://api.dicebear.com/7.x/avataaars/svg?seed=cosmic',
      rank: 0, // Will be calculated after sorting
      stellarShards: 1250,
      lumina: 45,
      level: XPCalculator.calculateLevel(750),
      totalXP: 750,
      cosmicTier: CosmicTier.fromXP(750).displayName,
      isVerifiedLuminaWeaver: true,
      isCurrentUser: true,
      planetIcon: '🌍',
      winStreak: 8,
      totalTrades: 45,
      winRate: 0.67,
      lastActive: DateTime.now().subtract(Duration(minutes: 5)),
    );
    
    entries.add(currentUserEntry);
    entries.addAll(mockUsers);
    
    // Sort by Stellar Shards (descending)
    entries.sort((a, b) => b.stellarShards.compareTo(a.stellarShards));
    
    // Assign ranks
    for (int i = 0; i < entries.length; i++) {
      entries[i] = entries[i].copyWith(rank: i + 1);
    }
    
    _cachedStellarShardsLeaderboard = entries;
    _lastCacheUpdate = DateTime.now();
    
    return entries;
  }

  /// Generate Lumina leaderboard (Pro Traders only)
  List<LeaderboardEntry> _getLuminaLeaderboard() {
    if (_cachedLuminaLeaderboard != null && _isCacheValid()) {
      return _cachedLuminaLeaderboard!;
    }

    final stellarLeaderboard = _getStellarShardsLeaderboard();
    
    // Filter to only verified Lumina Weavers (Pro Traders)
    final proTraders = stellarLeaderboard
        .where((entry) => entry.isVerifiedLuminaWeaver)
        .toList();
    
    // Sort by Lumina (descending)
    proTraders.sort((a, b) => b.lumina.compareTo(a.lumina));
    
    // Reassign ranks for Lumina leaderboard
    for (int i = 0; i < proTraders.length; i++) {
      proTraders[i] = proTraders[i].copyWith(rank: i + 1);
    }
    
    _cachedLuminaLeaderboard = proTraders;
    return proTraders;
  }

  /// Generate level-based leaderboard
  List<LeaderboardEntry> _getLevelLeaderboard() {
    final stellarLeaderboard = _getStellarShardsLeaderboard();
    
    // Sort by level (descending), then by XP
    stellarLeaderboard.sort((a, b) {
      final levelComparison = b.level.compareTo(a.level);
      if (levelComparison != 0) return levelComparison;
      return b.totalXP.compareTo(a.totalXP);
    });
    
    // Reassign ranks
    for (int i = 0; i < stellarLeaderboard.length; i++) {
      stellarLeaderboard[i] = stellarLeaderboard[i].copyWith(rank: i + 1);
    }
    
    return stellarLeaderboard;
  }

  /// Generate win streak leaderboard
  List<LeaderboardEntry> _getWinStreakLeaderboard() {
    final stellarLeaderboard = _getStellarShardsLeaderboard();
    
    // Sort by win streak (descending), then by win rate
    stellarLeaderboard.sort((a, b) {
      final streakComparison = b.winStreak.compareTo(a.winStreak);
      if (streakComparison != 0) return streakComparison;
      return b.winRate.compareTo(a.winRate);
    });
    
    // Reassign ranks
    for (int i = 0; i < stellarLeaderboard.length; i++) {
      stellarLeaderboard[i] = stellarLeaderboard[i].copyWith(rank: i + 1);
    }
    
    return stellarLeaderboard;
  }

  /// Generate mock user data for leaderboard
  List<LeaderboardEntry> _generateMockUsers() {
    final mockUsernames = [
      'NebulaKnight', 'StardustSage', 'GalaxyGuru', 'CosmicCrusader',
      'VoidVoyager', 'StellarSorcerer', 'OrbitOracle', 'QuantumQuest',
      'CelestialChief', 'AstroAce', 'MeteorMaster', 'PlanetPioneer',
      'SolarSultan', 'LunarLegend', 'SupernovaStar', 'CometCommander',
      'AsteroidAdept', 'BlackHoleBaron', 'WormholeWizard', 'SpaceShaman',
      'GravityGuru', 'TimeWarden', 'DimensionDuke', 'UniverseUltimate',
      'InfinityImp', 'EternityElite', 'ZenithZealot', 'ApexAstronaut',
      'SummitSage', 'PeakPilot', 'EliteExplorer', 'ProPioneer'
    ];

    final planetIcons = ['🌍', '🌎', '🌏', '🪐', '🌕', '🌑', '☄️', '⭐', '🌟', '✨'];
    
    final entries = <LeaderboardEntry>[];
    
    for (int i = 0; i < mockUsernames.length; i++) {
      final username = mockUsernames[i];
      
      // Generate realistic but varied stats
      final baseXP = 2000 - (i * 50) + _random.nextInt(200);
      final stellarShards = 2500 - (i * 75) + _random.nextInt(300);
      final lumina = i < 15 ? 80 - (i * 4) + _random.nextInt(20) : 0; // Only top players have Lumina
      final winStreak = math.max(0, 15 - i + _random.nextInt(10));
      final totalTrades = 20 + _random.nextInt(100);
      final winRate = (0.45 + (0.4 * (1 - i / mockUsernames.length)) + _random.nextDouble() * 0.1).clamp(0.0, 1.0);
      
      final isProTrader = lumina > 0;
      
      entries.add(LeaderboardEntry(
        userId: 'user_$i',
        username: username,
        avatarUrl: 'https://api.dicebear.com/7.x/avataaars/svg?seed=$username',
        rank: 0, // Will be assigned later
        stellarShards: stellarShards,
        lumina: lumina,
        level: XPCalculator.calculateLevel(baseXP),
        totalXP: baseXP,
        cosmicTier: CosmicTier.fromXP(baseXP).displayName,
        isVerifiedLuminaWeaver: isProTrader,
        isCurrentUser: false,
        planetIcon: planetIcons[_random.nextInt(planetIcons.length)],
        winStreak: winStreak,
        totalTrades: totalTrades,
        winRate: winRate,
        lastActive: DateTime.now().subtract(Duration(
          minutes: _random.nextInt(60 * 24), // Last active within 24 hours
        )),
      ));
    }
    
    return entries;
  }

  /// Simulate real-time leaderboard updates (for demo purposes)
  Stream<List<LeaderboardEntry>> getLeaderboardStream(LeaderboardType type) {
    return Stream.periodic(
      Duration(seconds: 30), // Update every 30 seconds
      (_) => getLeaderboardData(type),
    ).asyncMap((future) => future);
  }

  /// Get leaderboard statistics
  Future<Map<String, dynamic>> getLeaderboardStats(LeaderboardType type) async {
    final leaderboard = await getLeaderboardData(type);
    
    int totalPlayers = leaderboard.length;
    int proTraders = leaderboard.where((e) => e.isVerifiedLuminaWeaver).length;
    
    double avgLevel = leaderboard.map((e) => e.level).reduce((a, b) => a + b) / totalPlayers;
    int totalStellarShards = leaderboard.map((e) => e.stellarShards).reduce((a, b) => a + b);
    int totalLumina = leaderboard.map((e) => e.lumina).reduce((a, b) => a + b);
    
    return {
      'totalPlayers': totalPlayers,
      'proTraders': proTraders,
      'averageLevel': avgLevel.round(),
      'totalStellarShards': totalStellarShards,
      'totalLumina': totalLumina,
      'topPlayerSS': leaderboard.first.stellarShards,
      'topPlayerLumina': leaderboard.where((e) => e.lumina > 0).isNotEmpty 
          ? leaderboard.where((e) => e.lumina > 0).first.lumina 
          : 0,
    };
  }

  /// Clean up resources
  void dispose() {
    _invalidateCache();
  }
}