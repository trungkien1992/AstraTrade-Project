import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:google_fonts/google_fonts.dart';

import '../providers/auth_provider.dart';
import '../providers/game_state_provider.dart';
import '../widgets/planet_view.dart';
import '../widgets/pulsating_button.dart';
import '../utils/constants.dart';
import '../api/rag_api_client.dart';
import '../services/game_service.dart';
import 'leaderboard_screen.dart';

class MainHubScreen extends ConsumerStatefulWidget {
  const MainHubScreen({super.key});

  @override
  ConsumerState<MainHubScreen> createState() => _MainHubScreenState();
}

class _MainHubScreenState extends ConsumerState<MainHubScreen> {
  final List<ForgeParticleEffect> _particleEffects = [];
  final GameService _gameService = GameService();
  
  // Pro Mode configuration
  bool _isConfiguringProMode = false;

  @override
  Widget build(BuildContext context) {
    final authState = ref.watch(authProvider);
    final user = authState.value;
    final gameState = ref.watch(gameStateProvider);
    final isTrading = ref.watch(isQuickTradingProvider);

    return Scaffold(
      backgroundColor: const Color(0xFF0A0A0A),
      appBar: AppBar(
        title: Text(
          '${AppConstants.appName} Hub',
          style: GoogleFonts.orbitron(
            fontWeight: FontWeight.bold,
            letterSpacing: 1.5,
          ),
        ),
        backgroundColor: Colors.transparent,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.leaderboard),
            onPressed: () => _showLeaderboards(context),
          ),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => _signOut(context, ref),
          ),
        ],
      ),
      body: user == null
          ? const Center(child: CircularProgressIndicator())
          : Stack(
              children: [
                SingleChildScrollView(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    children: [
                      // RAG Connection Status Banner
                      _buildRagStatusBanner(),
                      
                      // Game Stats Header
                      _buildGameStatsHeader(gameState),
                      const SizedBox(height: 24),

                      // Main Planet Display
                      _buildPlanetSection(gameState),
                      const SizedBox(height: 24),

                      // Pro Mode Toggle Section
                      _buildProModeToggle(),
                      const SizedBox(height: 16),
                      
                      // Quick Trade Section
                      _buildQuickTradeSection(gameState, isTrading),
                      const SizedBox(height: 24),

                      // Game Progress Section
                      _buildGameProgressSection(gameState),
                      const SizedBox(height: 24),

                      // Cosmic Genesis Grid (if unlocked)
                      if (gameState.hasGenesisIgnition)
                        _buildCosmicGenesisGrid(gameState),
                    ],
                  ),
                ),
                
                // Particle effects overlay
                ..._particleEffects,
              ],
            ),
    );
  }

  /// Game stats header showing TT, CP, XP and cosmic tier
  Widget _buildGameStatsHeader(GameState gameState) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            Colors.purple.shade800.withValues(alpha: 0.9),
            Colors.blue.shade800.withValues(alpha: 0.9),
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: _getPlanetHealthColor(gameState.planetHealth).withValues(alpha: 0.3),
          width: 2,
        ),
      ),
      child: Column(
        children: [
          // Cosmic Tier
          Text(
            gameState.cosmicTier.displayName,
            style: GoogleFonts.orbitron(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 16),
          
          // Stats Row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildStatColumn('Trade Tokens', '${gameState.stellarShards}', 'TT', Colors.cyan),
              _buildStatColumn('Cosmic Power', '${gameState.cosmicPower}', 'CP', Colors.purple),
              _buildStatColumn('Experience', '${gameState.experience}', 'XP', Colors.orange),
              if (gameState.hasGenesisIgnition)
                _buildStatColumn('Lumina', '${gameState.lumina}', 'LM', Colors.yellow),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildStatColumn(String label, String value, String suffix, Color color) {
    return Column(
      children: [
        Text(
          value,
          style: GoogleFonts.orbitron(
            fontSize: 20,
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
        Text(
          suffix,
          style: GoogleFonts.rajdhani(
            fontSize: 12,
            color: color.withValues(alpha: 0.8),
            fontWeight: FontWeight.w600,
          ),
        ),
        Text(
          label,
          style: GoogleFonts.rajdhani(
            fontSize: 10,
            color: Colors.grey.shade400,
          ),
        ),
      ],
    );
  }

  /// Main planet display with tap-to-forge functionality
  Widget _buildPlanetSection(GameState gameState) {
    return Column(
      children: [
        // Last trade message
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          decoration: BoxDecoration(
            color: Colors.black.withValues(alpha: 0.5),
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: _getPlanetHealthColor(gameState.planetHealth).withValues(alpha: 0.3),
            ),
          ),
          child: Text(
            gameState.lastTradeMessage,
            style: GoogleFonts.rajdhani(
              fontSize: 14,
              color: Colors.white,
              fontStyle: FontStyle.italic,
            ),
            textAlign: TextAlign.center,
          ),
        ),
        const SizedBox(height: 16),
        
        // Planet view
        PlanetView(
          health: gameState.planetHealth,
          size: 250,
          showQuantumCore: gameState.hasGenesisIgnition,
          onTap: () => _performManualForge(gameState),
        ),
        
        const SizedBox(height: 16),
        
        // Planet health indicator
        _buildPlanetHealthIndicator(gameState.planetHealth),
      ],
    );
  }

  Widget _buildPlanetHealthIndicator(PlanetHealth health) {
    String status;
    Color color;
    IconData icon;
    
    switch (health) {
      case PlanetHealth.flourishing:
        status = "Flourishing";
        color = Colors.green;
        icon = Icons.eco;
        break;
      case PlanetHealth.stable:
        status = "Stable";
        color = Colors.blue;
        icon = Icons.balance;
        break;
      case PlanetHealth.decaying:
        status = "Needs Attention";
        color = Colors.orange;
        icon = Icons.warning;
        break;
    }
    
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.2),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: color, width: 1),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 16, color: color),
          const SizedBox(width: 6),
          Text(
            'Planet: $status',
            style: GoogleFonts.rajdhani(
              fontSize: 12,
              color: color,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }

  /// Quick Trade section with pulsating button
  Widget _buildQuickTradeSection(GameState gameState, bool isTrading) {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            Colors.purple.shade900.withValues(alpha: 0.7),
            Colors.indigo.shade900.withValues(alpha: 0.7),
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: Colors.purple.withValues(alpha: 0.3),
          width: 2,
        ),
      ),
      child: Column(
        children: [
          Text(
            'Cosmic Forge',
            style: GoogleFonts.orbitron(
              fontSize: 20,
              fontWeight: FontWeight.bold,
              color: Colors.white,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            _gameService.isProModeEnabled
                ? 'Execute real trades with live market data'
                : 'Channel cosmic energies through strategic trading',
            style: GoogleFonts.rajdhani(
              fontSize: 14,
              color: Colors.grey.shade300,
            ),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 20),
          
          // Trade Button (changes based on Pro Mode)
          SizedBox(
            width: double.infinity,
            height: 60,
            child: PulsatingButton(
              text: isTrading 
                  ? 'Channeling Energy...' 
                  : _gameService.isProModeEnabled 
                      ? '💎 REAL TRADE' 
                      : '🌟 QUICK TRADE',
              isLoading: isTrading,
              onPressed: isTrading ? null : () => _performTrade(),
              color: _gameService.isProModeEnabled 
                  ? Colors.green.shade600 
                  : Colors.purple.shade600,
            ),
          ),
          
          const SizedBox(height: 16),
          
          // Trading stats
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              _buildTradeStatItem('Total Trades', '${gameState.totalTrades}'),
              _buildTradeStatItem('Win Streak', '${gameState.winStreak}'),
              if (gameState.hasGenesisIgnition)
                _buildTradeStatItem('Genesis Active', '✨'),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildTradeStatItem(String label, String value) {
    return Column(
      children: [
        Text(
          value,
          style: GoogleFonts.orbitron(
            fontSize: 16,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
        Text(
          label,
          style: GoogleFonts.rajdhani(
            fontSize: 10,
            color: Colors.grey.shade400,
          ),
        ),
      ],
    );
  }

  /// Game progress section showing upgrades and achievements
  Widget _buildGameProgressSection(GameState gameState) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Cosmic Expansion',
          style: GoogleFonts.orbitron(
            fontSize: 18,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
        const SizedBox(height: 16),
        
        // Astro-Forgers section
        Card(
          color: Colors.grey.shade900,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Astro-Forgers: ${gameState.astroForgers}',
                      style: GoogleFonts.orbitron(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    ElevatedButton(
                      onPressed: gameState.canAfford(stellarShardsCost: _calculateAstroForgerCost(gameState))
                          ? () => _purchaseAstroForger()
                          : null,
                      child: Text('Buy (${_calculateAstroForgerCost(gameState)} TT)'),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  'Automated stellar shard generation',
                  style: GoogleFonts.rajdhani(
                    fontSize: 12,
                    color: Colors.grey.shade400,
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }

  /// Cosmic Genesis Grid for Pro Traders
  Widget _buildCosmicGenesisGrid(GameState gameState) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Cosmic Genesis Grid',
          style: GoogleFonts.orbitron(
            fontSize: 18,
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
        const SizedBox(height: 16),
        
        Card(
          color: Colors.grey.shade900,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              children: [
                Text(
                  'Infuse Lumina to activate cosmic nodes',
                  style: GoogleFonts.rajdhani(
                    fontSize: 14,
                    color: Colors.grey.shade300,
                  ),
                ),
                const SizedBox(height: 16),
                
                // Sample nodes grid
                GridView.count(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  crossAxisCount: 3,
                  mainAxisSpacing: 8,
                  crossAxisSpacing: 8,
                  children: [
                    _buildCosmicNode('Graviton\nAmplifier', 'graviton_amplifier', gameState),
                    _buildCosmicNode('Chrono\nAccelerator', 'chrono_accelerator', gameState),
                    _buildCosmicNode('Bio-Synthesis\nNexus', 'bio_synthesis_nexus', gameState),
                  ],
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildCosmicNode(String name, String nodeType, GameState gameState) {
    final currentLevel = gameState.cosmicNodes[nodeType] ?? 0;
    final upgradeCost = _calculateNodeUpgradeCost(nodeType, currentLevel);
    final canAfford = gameState.canAfford(luminaCost: upgradeCost);
    
    return GestureDetector(
      onTap: canAfford ? () => _upgradeCosmicNode(nodeType) : null,
      child: Container(
        padding: const EdgeInsets.all(8),
        decoration: BoxDecoration(
          color: currentLevel > 0 
              ? Colors.purple.shade800.withValues(alpha: 0.5)
              : Colors.grey.shade800.withValues(alpha: 0.3),
          borderRadius: BorderRadius.circular(8),
          border: Border.all(
            color: currentLevel > 0 ? Colors.purple : Colors.grey,
            width: 1,
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              name,
              style: GoogleFonts.rajdhani(
                fontSize: 10,
                color: Colors.white,
                fontWeight: FontWeight.w600,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 4),
            Text(
              'Lv. $currentLevel',
              style: GoogleFonts.orbitron(
                fontSize: 12,
                color: currentLevel > 0 ? Colors.purple.shade300 : Colors.grey,
                fontWeight: FontWeight.bold,
              ),
            ),
            if (canAfford) ...[
              const SizedBox(height: 2),
              Text(
                '$upgradeCost LM',
                style: GoogleFonts.rajdhani(
                  fontSize: 8,
                  color: Colors.yellow.shade300,
                ),
              ),
            ],
          ],
        ),
      ),
    );
  }

  // Action methods for game interactions
  
  /// Perform trading operation (either simulation or real based on Pro Mode)
  Future<void> _performTrade() async {
    ref.read(isQuickTradingProvider.notifier).state = true;
    
    try {
      if (_gameService.isProModeEnabled) {
        // Pro Mode: Execute real trade
        await _performRealTrade();
      } else {
        // Simulation Mode: Execute RAG-powered simulation
        await ref.read(gameStateProvider.notifier).performQuickTrade();
      }
      
      // Show success feedback
      if (mounted) {
        final mode = _gameService.isProModeEnabled ? 'REAL' : 'SIMULATION';
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              '🚀 $mode Trade Successful! Check your cosmic progress.',
              style: GoogleFonts.rajdhani(fontSize: 14),
            ),
            backgroundColor: _gameService.isProModeEnabled 
                ? Colors.green.shade600 
                : Colors.purple.shade600,
            duration: const Duration(seconds: 2),
          ),
        );
      }
    } catch (e) {
      // Show detailed error feedback based on error type
      if (mounted) {
        String errorTitle;
        String errorMessage;
        Color backgroundColor;
        
        if (e.toString().contains('RAG') || e.toString().contains('Network')) {
          errorTitle = 'Cosmic Network Disruption';
          errorMessage = 'Live trading intelligence unavailable. Using simulation mode.';
          backgroundColor = Colors.orange.shade600;
        } else if (e.toString().contains('Pro Mode') || e.toString().contains('Extended')) {
          errorTitle = 'Pro Mode Error';
          errorMessage = 'Real trading system unavailable. Check credentials.';
          backgroundColor = Colors.red.shade700;
        } else {
          errorTitle = 'Cosmic Interference';
          errorMessage = e.toString();
          backgroundColor = Colors.red.shade600;
        }
        
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  errorTitle,
                  style: GoogleFonts.rajdhani(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  errorMessage.length > 80 
                      ? '${errorMessage.substring(0, 80)}...'
                      : errorMessage,
                  style: GoogleFonts.rajdhani(fontSize: 12),
                ),
              ],
            ),
            backgroundColor: backgroundColor,
            duration: const Duration(seconds: 4),
          ),
        );
      }
    } finally {
      if (mounted) {
        ref.read(isQuickTradingProvider.notifier).state = false;
      }
    }
  }
  
  /// Perform real trade using Extended Exchange API
  Future<void> _performRealTrade() async {
    try {
      final result = await _gameService.performRealTrade();
      
      // Update game state with real trade results
      ref.read(gameStateProvider.notifier).updateFromRealTrade(result);
      
    } catch (e) {
      // Let the calling method handle the error display
      rethrow;
    }
  }

  /// Perform manual stellar forge (planet tap)
  Future<void> _performManualForge(GameState gameState) async {
    await ref.read(gameStateProvider.notifier).performManualForge();
    
    // Add particle effect at tap location
    if (mounted) {
      late final ForgeParticleEffect particleEffect;
      particleEffect = ForgeParticleEffect(
        position: const Offset(200, 200), // Center of planet
        color: _getPlanetHealthColor(gameState.planetHealth),
        onComplete: () {
          if (mounted) {
            setState(() {
              _particleEffects.removeWhere((effect) => effect == particleEffect);
            });
          }
        },
      );
      
      setState(() {
        _particleEffects.add(particleEffect);
      });
    }
  }

  /// Purchase additional Astro-Forger
  void _purchaseAstroForger() {
    ref.read(gameStateProvider.notifier).purchaseAstroForger();
    
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          'New Astro-Forger acquired! Stellar Shard generation increased.',
          style: GoogleFonts.rajdhani(fontSize: 14),
        ),
        backgroundColor: Colors.cyan.shade600,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  /// Upgrade a Cosmic Genesis Node
  void _upgradeCosmicNode(String nodeType) {
    ref.read(gameStateProvider.notifier).upgradeCosmicNode(nodeType);
    
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          'Cosmic Node upgraded! Your planet grows stronger.',
          style: GoogleFonts.rajdhani(fontSize: 14),
        ),
        backgroundColor: Colors.purple.shade600,
        duration: const Duration(seconds: 2),
      ),
    );
  }

  // Helper methods
  
  /// Get color based on planet health
  Color _getPlanetHealthColor(PlanetHealth health) {
    switch (health) {
      case PlanetHealth.flourishing:
        return Colors.green;
      case PlanetHealth.stable:
        return Colors.blue;
      case PlanetHealth.decaying:
        return Colors.orange;
    }
  }

  /// Calculate cost for next Astro-Forger
  int _calculateAstroForgerCost(GameState gameState) {
    return 100 + (gameState.astroForgers * 50);
  }

  /// Calculate cost for upgrading a Cosmic Node
  int _calculateNodeUpgradeCost(String nodeType, int currentLevel) {
    return 10 + (currentLevel * 15);
  }

  /// Navigate to the Leaderboard Screen
  void _showLeaderboards(BuildContext context) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => const LeaderboardScreen(),
      ),
    );
  }

  /// Build RAG connection status banner
  Widget _buildRagStatusBanner() {
    return FutureBuilder<bool>(
      future: _checkRagConnection(),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.waiting) {
          return const SizedBox.shrink(); // Don't show while checking
        }
        
        final isConnected = snapshot.data ?? false;
        if (isConnected) {
          return const SizedBox.shrink(); // Don't show banner when connected
        }
        
        return Container(
          margin: const EdgeInsets.only(bottom: 16),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
          decoration: BoxDecoration(
            color: Colors.orange.shade800.withValues(alpha: 0.9),
            borderRadius: BorderRadius.circular(8),
            border: Border.all(color: Colors.orange.shade400),
          ),
          child: Row(
            children: [
              Icon(Icons.cloud_off, color: Colors.orange.shade200, size: 16),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  'Cosmic Intelligence Network offline - Using simulation mode',
                  style: GoogleFonts.rajdhani(
                    fontSize: 12,
                    color: Colors.white,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }
  
  /// Check RAG connection status
  Future<bool> _checkRagConnection() async {
    try {
      final ragClient = RagApiClient();
      final isConnected = await ragClient.healthCheck();
      ragClient.dispose();
      return isConnected;
    } catch (e) {
      return false;
    }
  }

  /// Build Pro Mode toggle section
  Widget _buildProModeToggle() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: _gameService.isProModeEnabled
              ? [
                  Colors.green.shade800.withValues(alpha: 0.9),
                  Colors.green.shade700.withValues(alpha: 0.9),
                ]
              : [
                  Colors.grey.shade800.withValues(alpha: 0.9),
                  Colors.grey.shade700.withValues(alpha: 0.9),
                ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: _gameService.isProModeEnabled 
              ? Colors.green.withValues(alpha: 0.5)
              : Colors.grey.withValues(alpha: 0.3),
          width: 2,
        ),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    _gameService.isProModeEnabled ? 'PRO MODE ACTIVE' : 'SIMULATION MODE',
                    style: GoogleFonts.orbitron(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: _gameService.isProModeEnabled ? Colors.green.shade200 : Colors.white,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    _gameService.isProModeEnabled
                        ? 'Real funds & live markets'
                        : 'Safe practice environment',
                    style: GoogleFonts.rajdhani(
                      fontSize: 12,
                      color: Colors.grey.shade300,
                    ),
                  ),
                ],
              ),
              Switch.adaptive(
                value: _gameService.isProModeEnabled,
                onChanged: (value) => _toggleProMode(value),
                activeColor: Colors.green.shade400,
                inactiveThumbColor: Colors.grey.shade400,
              ),
            ],
          ),
          
          // Pro Mode status indicators
          if (_gameService.isProModeEnabled) ...[
            const SizedBox(height: 12),
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: Colors.green.shade900.withValues(alpha: 0.5),
                borderRadius: BorderRadius.circular(8),
              ),
              child: Row(
                children: [
                  Icon(Icons.security, color: Colors.green.shade300, size: 16),
                  const SizedBox(width: 8),
                  Expanded(
                    child: Text(
                      'Connected to Extended Exchange testnet',
                      style: GoogleFonts.rajdhani(
                        fontSize: 11,
                        color: Colors.green.shade200,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ],
      ),
    );
  }
  
  /// Toggle Pro Mode on/off
  void _toggleProMode(bool enabled) {
    if (enabled) {
      _showProModeConfigDialog();
    } else {
      setState(() {
        _gameService.disableProMode();
      });
      
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            '🌟 Switched to Simulation Mode - Safe practice environment',
            style: GoogleFonts.rajdhani(fontSize: 14),
          ),
          backgroundColor: Colors.purple.shade600,
          duration: const Duration(seconds: 2),
        ),
      );
    }
  }
  
  /// Show Pro Mode configuration dialog
  void _showProModeConfigDialog() {
    final apiKeyController = TextEditingController();
    final privateKeyController = TextEditingController();
    
    // Demo credentials for testing
    apiKeyController.text = 'demo_api_key_testnet';
    privateKeyController.text = 'demo_private_key_for_testing_only';
    
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: Colors.grey.shade900,
        title: Text(
          '💎 Enable Pro Mode',
          style: GoogleFonts.orbitron(
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
        content: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'Enter your Extended Exchange credentials to enable real trading:',
                style: GoogleFonts.rajdhani(color: Colors.grey.shade300),
              ),
              const SizedBox(height: 16),
              
              // API Key input
              Text(
                'API Key:',
                style: GoogleFonts.rajdhani(
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 8),
              TextField(
                controller: apiKeyController,
                style: GoogleFonts.rajdhani(color: Colors.white),
                decoration: InputDecoration(
                  hintText: 'Your Extended Exchange API key',
                  hintStyle: GoogleFonts.rajdhani(color: Colors.grey.shade500),
                  border: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.grey.shade600),
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.grey.shade600),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              
              // Private Key input
              Text(
                'Private Key:',
                style: GoogleFonts.rajdhani(
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 8),
              TextField(
                controller: privateKeyController,
                obscureText: true,
                style: GoogleFonts.rajdhani(color: Colors.white),
                decoration: InputDecoration(
                  hintText: 'Your Starknet private key',
                  hintStyle: GoogleFonts.rajdhani(color: Colors.grey.shade500),
                  border: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.grey.shade600),
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderSide: BorderSide(color: Colors.grey.shade600),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              
              // Warning notice
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: Colors.orange.shade900.withValues(alpha: 0.3),
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: Colors.orange.shade600),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Icon(Icons.warning, color: Colors.orange.shade400, size: 16),
                        const SizedBox(width: 8),
                        Text(
                          'TESTNET ONLY',
                          style: GoogleFonts.orbitron(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            color: Colors.orange.shade400,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 4),
                    Text(
                      'This connects to Extended Exchange testnet with demo funds. Real funds are not at risk.',
                      style: GoogleFonts.rajdhani(
                        fontSize: 11,
                        color: Colors.orange.shade200,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text(
              'Cancel',
              style: GoogleFonts.rajdhani(color: Colors.grey),
            ),
          ),
          ElevatedButton(
            onPressed: () {
              final apiKey = apiKeyController.text.trim();
              final privateKey = privateKeyController.text.trim();
              
              if (apiKey.isNotEmpty && privateKey.isNotEmpty) {
                Navigator.of(context).pop();
                _enableProMode(apiKey, privateKey);
              } else {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(
                      'Please enter both API key and private key',
                      style: GoogleFonts.rajdhani(),
                    ),
                    backgroundColor: Colors.red.shade600,
                  ),
                );
              }
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.green.shade600,
            ),
            child: Text(
              'Enable Pro Mode',
              style: GoogleFonts.rajdhani(color: Colors.white),
            ),
          ),
        ],
      ),
    );
  }
  
  /// Enable Pro Mode with provided credentials
  void _enableProMode(String apiKey, String privateKey) async {
    try {
      setState(() {
        _isConfiguringProMode = true;
      });
      
      // Enable Pro Mode in game service
      _gameService.enableProMode(
        apiKey: apiKey,
        privateKey: privateKey,
      );
      
      // Test connectivity
      final isConnected = await _gameService.checkExtendedExchangeHealth();
      
      if (mounted) {
        setState(() {
          _isConfiguringProMode = false;
        });
        
        if (isConnected) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text(
                '💎 Pro Mode ACTIVATED! Connected to Extended Exchange testnet',
                style: GoogleFonts.rajdhani(fontSize: 14),
              ),
              backgroundColor: Colors.green.shade600,
              duration: const Duration(seconds: 3),
            ),
          );
        } else {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text(
                '⚠️ Pro Mode enabled but Extended Exchange unreachable. Check network.',
                style: GoogleFonts.rajdhani(fontSize: 14),
              ),
              backgroundColor: Colors.orange.shade600,
              duration: const Duration(seconds: 3),
            ),
          );
        }
      }
    } catch (e) {
      if (mounted) {
        setState(() {
          _isConfiguringProMode = false;
        });
        
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              'Failed to enable Pro Mode: ${e.toString()}',
              style: GoogleFonts.rajdhani(fontSize: 14),
            ),
            backgroundColor: Colors.red.shade600,
            duration: const Duration(seconds: 3),
          ),
        );
      }
    }
  }

  /// Sign out confirmation dialog
  void _signOut(BuildContext context, WidgetRef ref) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: Colors.grey.shade900,
        title: Text(
          'Leave Cosmic Journey?',
          style: GoogleFonts.orbitron(
            fontWeight: FontWeight.bold,
            color: Colors.white,
          ),
        ),
        content: Text(
          'Are you sure you want to sign out? Your cosmic progress will be saved.',
          style: GoogleFonts.rajdhani(color: Colors.grey.shade300),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text(
              'Stay',
              style: GoogleFonts.rajdhani(color: Colors.grey),
            ),
          ),
          TextButton(
            onPressed: () async {
              Navigator.of(context).pop();
              await ref.read(authProvider.notifier).signOut();
            },
            child: Text(
              'Sign Out',
              style: GoogleFonts.rajdhani(color: Colors.red),
            ),
          ),
        ],
      ),
    );
  }
}