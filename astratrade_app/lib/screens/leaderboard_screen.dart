import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:google_fonts/google_fonts.dart';
import '../models/leaderboard.dart';
import '../providers/leaderboard_provider.dart';
import '../widgets/pulsating_button.dart';

class LeaderboardScreen extends ConsumerStatefulWidget {
  const LeaderboardScreen({super.key});

  @override
  ConsumerState<LeaderboardScreen> createState() => _LeaderboardScreenState();
}

class _LeaderboardScreenState extends ConsumerState<LeaderboardScreen>
    with TickerProviderStateMixin {
  late TabController _tabController;
  
  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
    
    // Load initial leaderboard data
    WidgetsBinding.instance.addPostFrameCallback((_) {
      ref.read(leaderboardProvider.notifier).loadLeaderboard(LeaderboardType.stellarShards);
    });
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final leaderboardState = ref.watch(leaderboardProvider);
    
    return Scaffold(
      backgroundColor: const Color(0xFF0A0A0A),
      appBar: AppBar(
        title: Text(
          'Cosmic Leaderboards',
          style: GoogleFonts.orbitron(
            fontWeight: FontWeight.bold,
            letterSpacing: 1.5,
          ),
        ),
        backgroundColor: Colors.transparent,
        elevation: 0,
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: () => ref.read(leaderboardProvider.notifier).refresh(),
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          onTap: _onTabChanged,
          tabs: const [
            Tab(text: 'Stellar Shards', icon: Icon(Icons.stars)),
            Tab(text: 'Lumina Flow', icon: Icon(Icons.auto_awesome)),
            Tab(text: 'Levels', icon: Icon(Icons.trending_up)),
            Tab(text: 'Win Streaks', icon: Icon(Icons.local_fire_department)),
          ],
          labelStyle: GoogleFonts.orbitron(fontSize: 12, fontWeight: FontWeight.w600),
          unselectedLabelStyle: GoogleFonts.orbitron(fontSize: 11),
        ),
      ),
      body: Column(
        children: [
          // Current User Quick Stats
          _buildCurrentUserStats(leaderboardState),
          
          // Leaderboard Content
          Expanded(
            child: TabBarView(
              controller: _tabController,
              children: [
                _buildLeaderboardList(leaderboardState, LeaderboardType.stellarShards),
                _buildLeaderboardList(leaderboardState, LeaderboardType.lumina),
                _buildLeaderboardList(leaderboardState, LeaderboardType.level),
                _buildLeaderboardList(leaderboardState, LeaderboardType.winStreak),
              ],
            ),
          ),
        ],
      ),
    );
  }

  void _onTabChanged(int index) {
    final types = [
      LeaderboardType.stellarShards,
      LeaderboardType.lumina,
      LeaderboardType.level,
      LeaderboardType.winStreak,
    ];
    
    ref.read(leaderboardProvider.notifier).switchLeaderboardType(types[index]);
  }

  Widget _buildCurrentUserStats(LeaderboardState state) {
    final currentUser = state.currentUserEntry;
    
    if (currentUser == null) {
      return Container(
        margin: const EdgeInsets.all(16),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.purple.shade900, Colors.blue.shade900],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.cyan.shade300, width: 1),
        ),
        child: const Center(
          child: Text(
            'Loading your cosmic status...',
            style: TextStyle(color: Colors.white70),
          ),
        ),
      );
    }

    return Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [
            Colors.purple.shade900.withOpacity(0.8),
            Colors.blue.shade900.withOpacity(0.8),
          ],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: currentUser.isVerifiedLuminaWeaver 
              ? Colors.yellow.shade300 
              : Colors.cyan.shade300,
          width: 2,
        ),
        boxShadow: [
          BoxShadow(
            color: (currentUser.isVerifiedLuminaWeaver 
                ? Colors.yellow.shade300 
                : Colors.cyan.shade300).withOpacity(0.3),
            blurRadius: 8,
            spreadRadius: 1,
          ),
        ],
      ),
      child: Column(
        children: [
          Row(
            children: [
              // Planet Icon
              Container(
                width: 50,
                height: 50,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  gradient: LinearGradient(
                    colors: [Colors.blue.shade400, Colors.purple.shade400],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                ),
                child: Center(
                  child: Text(
                    currentUser.planetIcon,
                    style: const TextStyle(fontSize: 24),
                  ),
                ),
              ),
              const SizedBox(width: 16),
              
              // User Info
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Text(
                          currentUser.username,
                          style: GoogleFonts.orbitron(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          ),
                        ),
                        if (currentUser.isVerifiedLuminaWeaver) ...[
                          const SizedBox(width: 8),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                            decoration: BoxDecoration(
                              gradient: LinearGradient(
                                colors: [Colors.yellow.shade400, Colors.orange.shade400],
                              ),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Text(
                              'Lumina Weaver',
                              style: GoogleFonts.orbitron(
                                fontSize: 10,
                                fontWeight: FontWeight.bold,
                                color: Colors.black,
                              ),
                            ),
                          ),
                        ],
                      ],
                    ),
                    const SizedBox(height: 4),
                    Text(
                      currentUser.cosmicTier,
                      style: GoogleFonts.orbitron(
                        fontSize: 14,
                        color: Colors.cyan.shade300,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),
              
              // Rank
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                decoration: BoxDecoration(
                  color: Colors.black.withOpacity(0.5),
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white.withOpacity(0.3)),
                ),
                child: Column(
                  children: [
                    Text(
                      '#${currentUser.rank}',
                      style: GoogleFonts.orbitron(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                    Text(
                      'RANK',
                      style: GoogleFonts.orbitron(
                        fontSize: 10,
                        color: Colors.white70,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
          
          const SizedBox(height: 16),
          
          // Stats Row
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              _buildStatItem('SS', currentUser.stellarShards.toString(), Colors.blue),
              _buildStatItem('LM', currentUser.lumina.toString(), Colors.yellow),
              _buildStatItem('LVL', currentUser.level.toString(), Colors.green),
              _buildStatItem('XP', currentUser.totalXP.toString(), Colors.purple),
              _buildStatItem('Streak', currentUser.winStreak.toString(), Colors.orange),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildStatItem(String label, String value, Color color) {
    return Column(
      children: [
        Text(
          value,
          style: GoogleFonts.orbitron(
            fontSize: 16,
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
        Text(
          label,
          style: GoogleFonts.orbitron(
            fontSize: 10,
            color: Colors.white70,
          ),
        ),
      ],
    );
  }

  Widget _buildLeaderboardList(LeaderboardState state, LeaderboardType type) {
    if (state.isLoading) {
      return const Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircularProgressIndicator(color: Colors.cyan),
            SizedBox(height: 16),
            Text(
              'Loading cosmic rankings...',
              style: TextStyle(color: Colors.white70),
            ),
          ],
        ),
      );
    }

    if (state.error != null) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Icon(Icons.error_outline, color: Colors.red, size: 48),
            const SizedBox(height: 16),
            Text(
              'Failed to load leaderboard',
              style: GoogleFonts.orbitron(color: Colors.white, fontSize: 16),
            ),
            const SizedBox(height: 8),
            Text(
              state.error!,
              style: const TextStyle(color: Colors.red, fontSize: 12),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 16),
            PulsatingButton(
              text: 'Retry',
              onPressed: () => ref.read(leaderboardProvider.notifier).refresh(),
            ),
          ],
        ),
      );
    }

    if (state.entries.isEmpty) {
      return const Center(
        child: Text(
          'No cosmic traders found',
          style: TextStyle(color: Colors.white70, fontSize: 16),
        ),
      );
    }

    // Filter entries for Lumina leaderboard (Pro Traders only)
    final filteredEntries = type == LeaderboardType.lumina
        ? state.entries.where((entry) => entry.isVerifiedLuminaWeaver).toList()
        : state.entries;

    return ListView.builder(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      itemCount: filteredEntries.length,
      itemBuilder: (context, index) {
        final entry = filteredEntries[index];
        return _buildLeaderboardEntry(entry, type, index);
      },
    );
  }

  Widget _buildLeaderboardEntry(LeaderboardEntry entry, LeaderboardType type, int listIndex) {
    final isCurrentUser = entry.isCurrentUser;
    final isTopThree = entry.rank <= 3;
    
    // Colors for top 3
    Color? rankColor;
    if (entry.rank == 1) {
      rankColor = Colors.yellow.shade400;
    } else if (entry.rank == 2) {
      rankColor = Colors.grey.shade300;
    } else if (entry.rank == 3) {
      rankColor = Colors.orange.shade400;
    }

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 4),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: isCurrentUser
              ? [Colors.purple.shade800.withOpacity(0.8), Colors.blue.shade800.withOpacity(0.8)]
              : isTopThree
                  ? [Colors.yellow.shade900.withOpacity(0.3), Colors.orange.shade900.withOpacity(0.3)]
                  : [Colors.grey.shade900.withOpacity(0.3), Colors.grey.shade800.withOpacity(0.3)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: isCurrentUser
              ? Colors.cyan.shade300
              : isTopThree
                  ? rankColor!
                  : Colors.white.withOpacity(0.1),
          width: isCurrentUser ? 2 : 1,
        ),
      ),
      child: Row(
        children: [
          // Rank
          Container(
            width: 40,
            height: 40,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: isTopThree ? rankColor : Colors.white.withOpacity(0.1),
            ),
            child: Center(
              child: Text(
                '#${entry.rank}',
                style: GoogleFonts.orbitron(
                  fontSize: 14,
                  fontWeight: FontWeight.bold,
                  color: isTopThree ? Colors.black : Colors.white,
                ),
              ),
            ),
          ),
          
          const SizedBox(width: 16),
          
          // Planet Icon
          Text(
            entry.planetIcon,
            style: const TextStyle(fontSize: 24),
          ),
          
          const SizedBox(width: 12),
          
          // User Info
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      entry.username,
                      style: GoogleFonts.orbitron(
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: isCurrentUser ? Colors.cyan.shade300 : Colors.white,
                      ),
                    ),
                    if (entry.isVerifiedLuminaWeaver) ...[
                      const SizedBox(width: 8),
                      Icon(
                        Icons.verified,
                        size: 16,
                        color: Colors.yellow.shade400,
                      ),
                    ],
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                  'Level ${entry.level} • ${entry.cosmicTier}',
                  style: GoogleFonts.orbitron(
                    fontSize: 12,
                    color: Colors.white70,
                  ),
                ),
              ],
            ),
          ),
          
          // Primary Stat (based on leaderboard type)
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.3),
              borderRadius: BorderRadius.circular(16),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                Text(
                  _getPrimaryStatValue(entry, type),
                  style: GoogleFonts.orbitron(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                    color: _getPrimaryStatColor(type),
                  ),
                ),
                Text(
                  _getPrimaryStatLabel(type),
                  style: GoogleFonts.orbitron(
                    fontSize: 10,
                    color: Colors.white70,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  String _getPrimaryStatValue(LeaderboardEntry entry, LeaderboardType type) {
    switch (type) {
      case LeaderboardType.stellarShards:
        return _formatNumber(entry.stellarShards);
      case LeaderboardType.lumina:
        return _formatNumber(entry.lumina);
      case LeaderboardType.level:
        return entry.level.toString();
      case LeaderboardType.winStreak:
        return entry.winStreak.toString();
    }
  }

  String _getPrimaryStatLabel(LeaderboardType type) {
    switch (type) {
      case LeaderboardType.stellarShards:
        return 'SS';
      case LeaderboardType.lumina:
        return 'LM';
      case LeaderboardType.level:
        return 'LVL';
      case LeaderboardType.winStreak:
        return 'STREAK';
    }
  }

  Color _getPrimaryStatColor(LeaderboardType type) {
    switch (type) {
      case LeaderboardType.stellarShards:
        return Colors.blue.shade300;
      case LeaderboardType.lumina:
        return Colors.yellow.shade300;
      case LeaderboardType.level:
        return Colors.green.shade300;
      case LeaderboardType.winStreak:
        return Colors.orange.shade300;
    }
  }

  String _formatNumber(int number) {
    if (number >= 1000000) {
      return '${(number / 1000000).toStringAsFixed(1)}M';
    } else if (number >= 1000) {
      return '${(number / 1000).toStringAsFixed(1)}K';
    } else {
      return number.toString();
    }
  }
}