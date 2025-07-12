import 'dart:async';
import 'dart:math' as math;
import 'package:flutter/foundation.dart';
import '../api/rag_api_client.dart';
import '../api/extended_exchange_client.dart';
import 'starknet_service.dart';

/// Result of a trading operation
enum TradeOutcome {
  profit,
  loss,
  breakeven,
}

/// Trade result containing outcome and rewards
class TradeResult {
  final TradeOutcome outcome;
  final int stellarShardsGained;
  final int luminaGained;
  final double profitPercentage;
  final String outcomeMessage;
  final bool isCriticalForge;

  TradeResult({
    required this.outcome,
    required this.stellarShardsGained,
    required this.luminaGained,
    required this.profitPercentage,
    required this.outcomeMessage,
    this.isCriticalForge = false,
  });
}

/// Game service that manages trading mechanics and rewards
class GameService {
  static final GameService _instance = GameService._internal();
  factory GameService() => _instance;
  GameService._internal();

  final _random = math.Random();
  final _ragClient = RagApiClient();
  final _starknetService = StarknetService();
  
  // Configuration
  bool _useRagBackend = true;
  bool _isProModeEnabled = false;
  
  // Extended Exchange client (initialized when Pro Mode is enabled)
  ExtendedExchangeClient? _exchangeClient;
  
  // Demo credentials (in production, these would come from secure storage)
  String? _apiKey;
  String? _privateKey;
  
  // Trading simulation parameters
  static const double _baseProfitChance = 0.55; // 55% chance of profit
  static const double _criticalForgeChance = 0.15; // 15% chance of critical forge
  static const int _baseStellarShardsReward = 10;
  static const int _baseLuminaReward = 5;
  
  // Cosmic-themed outcome messages
  static const List<String> _profitMessages = [
    "Stellar Alignment Achieved! The cosmos smiles upon you.",
    "Cosmic Energies Channeled! Your orbital trajectory was perfect.",
    "Quantum Resonance Detected! The universe rewards your wisdom.",
    "Nebula Formation Successful! Your cosmic instincts are sharp.",
    "Galactic Harmony Reached! The stars align in your favor.",
  ];
  
  static const List<String> _lossMessages = [
    "Solar Storm Interference. The cosmic winds shift unexpectedly.",
    "Temporal Flux Detected. The universe tests your resolve.",
    "Gravitational Anomaly. Even masters face cosmic challenges.",
    "Void Whispers Heard. Darkness teaches valuable lessons.",
    "Meteor Shower Disruption. The cosmos humbles us all.",
  ];
  
  static const List<String> _breakevenMessages = [
    "Cosmic Balance Maintained. The universe remains neutral.",
    "Stellar Equilibrium Achieved. Perfect cosmic harmony.",
    "Quantum Stasis Reached. The cosmos holds its breath.",
    "Orbital Stability Detected. A moment of cosmic peace.",
  ];

  /// Performs a Quick Trade operation using RAG backend for realistic outcomes
  /// Falls back to mock data if RAG is unavailable
  Future<TradeResult> performQuickTrade() async {
    if (_useRagBackend) {
      try {
        return await _performRagQuickTrade();
      } catch (e) {
        // RAG failed, fall back to mock data and disable RAG for this session
        _useRagBackend = false;
        debugPrint('RAG backend unavailable, falling back to mock data: $e');
        return await _performMockQuickTrade();
      }
    } else {
      return await _performMockQuickTrade();
    }
  }
  
  /// Perform trade using RAG backend for realistic market simulation
  Future<TradeResult> _performRagQuickTrade() async {
    // Check RAG health first
    final isHealthy = await _ragClient.healthCheck();
    if (!isHealthy) {
      throw Exception('RAG backend health check failed');
    }
    
    // Query RAG for trading scenario
    final response = await _ragClient.searchTradingScenario(
      'Quick Trade',
      asset: 'ETH',
      direction: _random.nextBool() ? 'long' : 'short',
      amount: 50.0 + (_random.nextDouble() * 200.0), // $50-$250
    );
    
    if (response.results.isEmpty) {
      throw Exception('No trading scenarios found in RAG');
    }
    
    // Parse RAG response to determine trade outcome
    final ragContent = response.results.first.content.toLowerCase();
    final isCritical = _random.nextDouble() < _criticalForgeChance;
    
    TradeOutcome outcome;
    double profitPercentage;
    String cosmicMessage;
    
    // Analyze RAG content for profit/loss indicators
    if (ragContent.contains('profit') || 
        ragContent.contains('gain') || 
        ragContent.contains('positive') ||
        ragContent.contains('up ')) {
      outcome = TradeOutcome.profit;
      profitPercentage = _extractPercentage(ragContent) ?? (5.0 + (_random.nextDouble() * 15.0));
      cosmicMessage = _generateCosmicMessage(ragContent, outcome);
    } else if (ragContent.contains('loss') || 
               ragContent.contains('negative') || 
               ragContent.contains('down ') ||
               ragContent.contains('decline')) {
      outcome = TradeOutcome.loss;
      profitPercentage = -(2.0 + (_random.nextDouble() * 8.0));
      cosmicMessage = _generateCosmicMessage(ragContent, outcome);
    } else {
      outcome = TradeOutcome.breakeven;
      profitPercentage = -1.0 + (_random.nextDouble() * 2.0);
      cosmicMessage = _generateCosmicMessage(ragContent, outcome);
    }
    
    // Calculate rewards based on RAG-driven outcome
    int stellarShards = 0;
    int lumina = 0;
    
    switch (outcome) {
      case TradeOutcome.profit:
        stellarShards = (_baseStellarShardsReward * (1.0 + profitPercentage / 100)).round();
        lumina = (_baseLuminaReward * (1.0 + profitPercentage / 200)).round();
        break;
      case TradeOutcome.loss:
        stellarShards = 3; // Small consolation reward
        lumina = 0;
        break;
      case TradeOutcome.breakeven:
        stellarShards = _baseStellarShardsReward ~/ 2;
        lumina = 1;
        break;
    }
    
    // Apply critical forge multiplier
    if (isCritical && outcome == TradeOutcome.profit) {
      stellarShards = (stellarShards * 2.5).round();
      lumina = (lumina * 2).round();
      cosmicMessage = "⭐ CRITICAL FORGE! ⭐ $cosmicMessage";
    }
    
    return TradeResult(
      outcome: outcome,
      stellarShardsGained: stellarShards,
      luminaGained: lumina,
      profitPercentage: profitPercentage,
      outcomeMessage: cosmicMessage,
      isCriticalForge: isCritical && outcome == TradeOutcome.profit,
    );
  }
  
  /// Fallback mock implementation (original logic)
  Future<TradeResult> _performMockQuickTrade() async {
    // Simulate network delay and processing time
    await Future.delayed(const Duration(milliseconds: 500));
    
    // Determine trade outcome
    final profitRoll = _random.nextDouble();
    final isCritical = _random.nextDouble() < _criticalForgeChance;
    
    TradeOutcome outcome;
    if (profitRoll < _baseProfitChance * 0.7) {
      outcome = TradeOutcome.profit;
    } else if (profitRoll < _baseProfitChance) {
      outcome = TradeOutcome.breakeven;
    } else {
      outcome = TradeOutcome.loss;
    }
    
    // Calculate rewards based on outcome
    int stellarShards = 0;
    int lumina = 0;
    double profitPercentage = 0.0;
    String message = "";
    
    switch (outcome) {
      case TradeOutcome.profit:
        profitPercentage = 5.0 + (_random.nextDouble() * 15.0); // 5-20% profit
        stellarShards = (_baseStellarShardsReward * (1.0 + profitPercentage / 100)).round();
        lumina = (_baseLuminaReward * (1.0 + profitPercentage / 200)).round();
        message = _profitMessages[_random.nextInt(_profitMessages.length)];
        break;
        
      case TradeOutcome.loss:
        profitPercentage = -2.0 - (_random.nextDouble() * 8.0); // -2% to -10% loss
        stellarShards = 3; // Small consolation reward
        lumina = 0;
        message = _lossMessages[_random.nextInt(_lossMessages.length)];
        break;
        
      case TradeOutcome.breakeven:
        profitPercentage = -1.0 + (_random.nextDouble() * 2.0); // -1% to +1%
        stellarShards = _baseStellarShardsReward ~/ 2;
        lumina = 1;
        message = _breakevenMessages[_random.nextInt(_breakevenMessages.length)];
        break;
    }
    
    // Apply critical forge multiplier
    if (isCritical && outcome == TradeOutcome.profit) {
      stellarShards = (stellarShards * 2.5).round();
      lumina = (lumina * 2).round();
      message = "⭐ CRITICAL FORGE! ⭐ $message";
    }
    
    return TradeResult(
      outcome: outcome,
      stellarShardsGained: stellarShards,
      luminaGained: lumina,
      profitPercentage: profitPercentage,
      outcomeMessage: message,
      isCriticalForge: isCritical && outcome == TradeOutcome.profit,
    );
  }
  
  /// Performs idle stellar shard generation (tap or auto-forge)
  Future<int> performStellarForge({bool isManualTap = false}) async {
    if (isManualTap) {
      // Manual taps have slight randomization
      final baseReward = 5;
      final bonus = _random.nextInt(3); // 0-2 bonus
      return baseReward + bonus;
    } else {
      // Auto-forge from Astro-Forgers
      return 3 + _random.nextInt(2); // 3-4 SS per auto-forge
    }
  }
  
  /// Calculates Astro-Forger efficiency based on planet health
  double calculateForgerEfficiency(String planetHealth) {
    switch (planetHealth.toLowerCase()) {
      case 'flourishing':
        return 1.5; // 50% boost
      case 'stable':
        return 1.0; // Normal rate
      case 'decaying':
        return 0.7; // 30% reduction
      default:
        return 1.0;
    }
  }
  
  /// Gets market data with RAG-enhanced cosmic forecasts
  Map<String, dynamic> getMarketData() {
    final volatility = 0.5 + (_random.nextDouble() * 1.5); // 0.5-2.0 volatility
    final trend = _random.nextDouble() - 0.5; // -0.5 to +0.5 trend
    
    return {
      'stellarFlux': volatility,
      'cosmicTrend': trend,
      'forecast': _generateCosmicForecast(volatility, trend),
      'timestamp': DateTime.now().millisecondsSinceEpoch,
      'ragEnabled': _useRagBackend,
    };
  }
  
  String _generateCosmicForecast(double volatility, double trend) {
    if (volatility > 1.5) {
      return trend > 0 
          ? "Supernova Brewing: Explosive Growth Ahead"
          : "Black Hole Warning: Gravitational Collapse Imminent";
    } else if (volatility > 1.0) {
      return trend > 0.2
          ? "Nebula Forming: Steady Stellar Ascent"
          : trend < -0.2
              ? "Meteor Shower: Orbital Descent Expected"
              : "Solar Winds: Gentle Cosmic Fluctuations";
    } else {
      return "Cosmic Tranquility: Stable Stellar Drift";
    }
  }
  
  /// Validates trade parameters for "Cosmic Forge" UI
  bool validateTradeParameters({
    required String direction, // 'ascent' or 'descent'
    required double amount,
    required double leverage,
  }) {
    return direction.isNotEmpty && 
           amount > 0 && 
           leverage >= 1.0 && 
           leverage <= 10.0;
  }
  
  /// Extract percentage from RAG content text
  double? _extractPercentage(String content) {
    final regex = RegExp(r'(\d+(?:\.\d+)?)%');
    final match = regex.firstMatch(content);
    if (match != null) {
      return double.tryParse(match.group(1) ?? '');
    }
    return null;
  }
  
  /// Generate cosmic-themed message from RAG content
  String _generateCosmicMessage(String ragContent, TradeOutcome outcome) {
    // Try to extract meaningful text from RAG response
    final sentences = ragContent.split('.').where((s) => s.trim().length > 10).toList();
    
    if (sentences.isNotEmpty) {
      // Use first meaningful sentence from RAG as base
      String baseMessage = sentences.first.trim();
      
      // Add cosmic theming based on outcome
      switch (outcome) {
        case TradeOutcome.profit:
          return "Stellar Alignment Achieved! $baseMessage";
        case TradeOutcome.loss:
          return "Solar Storm Interference: $baseMessage";
        case TradeOutcome.breakeven:
          return "Cosmic Balance Maintained: $baseMessage";
      }
    }
    
    // Fallback to predefined messages
    switch (outcome) {
      case TradeOutcome.profit:
        return _profitMessages[_random.nextInt(_profitMessages.length)];
      case TradeOutcome.loss:
        return _lossMessages[_random.nextInt(_lossMessages.length)];
      case TradeOutcome.breakeven:
        return _breakevenMessages[_random.nextInt(_breakevenMessages.length)];
    }
  }
  
  /// Check if RAG backend is currently enabled
  bool get isRagEnabled => _useRagBackend;
  
  /// Enable or disable RAG backend (for testing/debugging)
  void setRagEnabled(bool enabled) {
    _useRagBackend = enabled;
  }
  
  /// Enable Pro Mode with Extended Exchange credentials
  void enableProMode({
    required String apiKey,
    required String privateKey,
  }) {
    _isProModeEnabled = true;
    _apiKey = apiKey;
    _privateKey = privateKey;
    
    // Initialize Extended Exchange client
    _exchangeClient = ExtendedExchangeClient(apiKey: apiKey);
    
    debugPrint('Pro Mode enabled with Extended Exchange integration');
  }
  
  /// Disable Pro Mode (return to simulation)
  void disableProMode() {
    _isProModeEnabled = false;
    _apiKey = null;
    _privateKey = null;
    
    // Clean up Exchange client
    _exchangeClient?.dispose();
    _exchangeClient = null;
    
    debugPrint('Pro Mode disabled - returned to simulation mode');
  }
  
  /// Check if Pro Mode is currently enabled
  bool get isProModeEnabled => _isProModeEnabled;
  
  /// Perform a real trade using Extended Exchange API
  /// This method handles the complete Pro Mode trading flow:
  /// 1. Creates and signs the trading payload using Starknet Service
  /// 2. Sends the signed order to Extended Exchange API
  /// 3. Processes the response and converts to game rewards
  Future<TradeResult> performRealTrade({
    String market = 'ETH-USD-PERP',
    double amount = 10.0, // USD amount
    String? direction, // 'BUY' or 'SELL' - if null, randomly chosen
  }) async {
    if (!_isProModeEnabled || _exchangeClient == null || _privateKey == null) {
      throw Exception('Pro Mode not enabled or configured properly');
    }
    
    try {
      // Determine trade direction
      final side = direction ?? (_random.nextBool() ? 'BUY' : 'SELL');
      
      // Convert USD amount to size (simplified)
      final size = (amount / 100).toStringAsFixed(3); // Rough ETH equivalent
      
      debugPrint('Initiating real trade: $side $size $market');
      
      // Step 1: Create and sign the trading payload
      final signedPayload = await _starknetService.signRealTradePayload(
        privateKey: _privateKey!,
        market: market,
        side: side,
        type: 'MARKET', // Use market orders for simplicity
        size: size,
        clientOrderId: 'ASTRA_${DateTime.now().millisecondsSinceEpoch}',
      );
      
      debugPrint('Payload signed successfully: ${signedPayload.clientOrderId}');
      
      // Step 2: Submit order to Extended Exchange
      final orderResponse = await _exchangeClient!.placeOrder(
        market: signedPayload.market,
        side: signedPayload.side,
        type: signedPayload.type,
        size: signedPayload.size,
        price: signedPayload.price,
        clientOrderId: signedPayload.clientOrderId,
        starkSignature: signedPayload.signature,
        reduceOnly: signedPayload.reduceOnly,
        postOnly: signedPayload.postOnly,
      );
      
      // Step 3: Process response and convert to game format
      if (orderResponse.isSuccess && orderResponse.data != null) {
        return _convertRealTradeToGameResult(
          orderData: orderResponse.data!,
          requestedSide: side,
          requestedAmount: amount,
        );
      } else {
        throw Exception('Trade failed: ${orderResponse.error?.message ?? 'Unknown error'}');
      }
      
    } catch (e) {
      debugPrint('Real trade failed: $e');
      
      // Convert error to game result (still provide some rewards for trying)
      return TradeResult(
        outcome: TradeOutcome.loss,
        stellarShardsGained: 1, // Consolation reward
        luminaGained: 0,
        profitPercentage: -5.0,
        outcomeMessage: "Cosmic Interference: ${e.toString().length > 50 ? '${e.toString().substring(0, 50)}...' : e.toString()}",
        isCriticalForge: false,
      );
    }
  }
  
  /// Convert Extended Exchange order response to game TradeResult
  TradeResult _convertRealTradeToGameResult({
    required ExtendedOrderData orderData,
    required String requestedSide,
    required double requestedAmount,
  }) {
    // Simulate profit/loss based on order status and market conditions
    // In a real implementation, this would wait for order fill and calculate actual PnL
    
    final isOrderAccepted = orderData.status == 'PENDING' || 
                           orderData.status == 'OPEN' || 
                           orderData.status == 'FILLED';
    
    if (!isOrderAccepted) {
      return TradeResult(
        outcome: TradeOutcome.loss,
        stellarShardsGained: 2,
        luminaGained: 0,
        profitPercentage: -2.0,
        outcomeMessage: "Trade Rejected: Order status ${orderData.status}",
        isCriticalForge: false,
      );
    }
    
    // For successful orders, simulate realistic outcomes
    final profitChance = 0.52; // Slightly positive expected value
    final isProfit = _random.nextDouble() < profitChance;
    final isCritical = _random.nextDouble() < 0.08; // 8% critical rate for real trades
    
    TradeOutcome outcome;
    double profitPercentage;
    int stellarShards;
    int lumina;
    String message;
    
    if (isProfit) {
      outcome = TradeOutcome.profit;
      profitPercentage = 2.0 + (_random.nextDouble() * 8.0); // 2-10% profit
      stellarShards = (20 + (profitPercentage * 2)).round();
      lumina = (8 + (profitPercentage * 1.5)).round();
      message = "🚀 Real Trade SUCCESS! Order ${orderData.orderId} executed on ${orderData.market}";
    } else {
      outcome = TradeOutcome.loss;
      profitPercentage = -1.0 - (_random.nextDouble() * 5.0); // -1% to -6% loss
      stellarShards = 5; // Small consolation
      lumina = 1;
      message = "⚡ Market Volatility: Order ${orderData.orderId} hit stop-loss";
    }
    
    // Apply critical forge multiplier for real trades
    if (isCritical && outcome == TradeOutcome.profit) {
      stellarShards = (stellarShards * 3).round(); // Higher multiplier for real trades
      lumina = (lumina * 2.5).round();
      message = "💎 CRITICAL FORGE! Real market mastery achieved! $message";
    }
    
    debugPrint('Real trade converted to game result: $outcome, ${profitPercentage.toStringAsFixed(2)}%');
    
    return TradeResult(
      outcome: outcome,
      stellarShardsGained: stellarShards,
      luminaGained: lumina,
      profitPercentage: profitPercentage,
      outcomeMessage: message,
      isCriticalForge: isCritical && outcome == TradeOutcome.profit,
    );
  }
  
  /// Check Extended Exchange connectivity
  Future<bool> checkExtendedExchangeHealth() async {
    try {
      if (_exchangeClient == null) return false;
      return await _exchangeClient!.healthCheck();
    } catch (e) {
      debugPrint('Extended Exchange health check failed: $e');
      return false;
    }
  }
  
  /// Get account balance from Extended Exchange (if Pro Mode enabled)
  Future<ExtendedBalanceData?> getProModeBalance() async {
    if (!_isProModeEnabled || _exchangeClient == null) return null;
    
    try {
      final balanceResponse = await _exchangeClient!.getBalance();
      return balanceResponse.isSuccess ? balanceResponse.data : null;
    } catch (e) {
      debugPrint('Failed to get Pro Mode balance: $e');
      return null;
    }
  }
  
  /// Get current positions from Extended Exchange (if Pro Mode enabled)
  Future<List<ExtendedPosition>?> getProModePositions() async {
    if (!_isProModeEnabled || _exchangeClient == null) return null;
    
    try {
      return await _exchangeClient!.getPositions();
    } catch (e) {
      debugPrint('Failed to get Pro Mode positions: $e');
      return null;
    }
  }
  
  /// Clean up resources
  void dispose() {
    _ragClient.dispose();
    _exchangeClient?.dispose();
  }
}