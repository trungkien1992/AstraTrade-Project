import 'package:flutter/material.dart';
import 'dart:math' as math;

/// Planet health states that affect the visual appearance
enum PlanetHealth {
  flourishing,  // Happy/thriving state - vibrant colors and effects
  stable,       // Normal state - balanced appearance
  decaying,     // Declining state - darker, less vibrant
}

/// PlanetView widget displays a dynamic 3D-style planet that changes based on health
class PlanetView extends StatefulWidget {
  final PlanetHealth health;
  final double size;
  final VoidCallback? onTap;
  final bool showQuantumCore;
  
  const PlanetView({
    super.key,
    required this.health,
    this.size = 200.0,
    this.onTap,
    this.showQuantumCore = false,
  });

  @override
  State<PlanetView> createState() => _PlanetViewState();
}

class _PlanetViewState extends State<PlanetView>
    with TickerProviderStateMixin {
  late AnimationController _rotationController;
  late AnimationController _pulseController;
  late AnimationController _coreController;
  
  @override
  void initState() {
    super.initState();
    
    // Rotation animation for the planet
    _rotationController = AnimationController(
      duration: const Duration(seconds: 20),
      vsync: this,
    )..repeat();
    
    // Pulse animation for health effects
    _pulseController = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    )..repeat(reverse: true);
    
    // Quantum core animation
    _coreController = AnimationController(
      duration: const Duration(seconds: 1),
      vsync: this,
    )..repeat(reverse: true);
  }

  @override
  void dispose() {
    _rotationController.dispose();
    _pulseController.dispose();
    _coreController.dispose();
    super.dispose();
  }

  Color _getPrimaryColor() {
    switch (widget.health) {
      case PlanetHealth.flourishing:
        return Colors.cyan.shade300;
      case PlanetHealth.stable:
        return Colors.blue.shade400;
      case PlanetHealth.decaying:
        return Colors.grey.shade600;
    }
  }

  Color _getSecondaryColor() {
    switch (widget.health) {
      case PlanetHealth.flourishing:
        return Colors.green.shade400;
      case PlanetHealth.stable:
        return Colors.purple.shade400;
      case PlanetHealth.decaying:
        return Colors.brown.shade400;
    }
  }

  List<Color> _getGradientColors() {
    switch (widget.health) {
      case PlanetHealth.flourishing:
        return [
          Colors.cyan.shade200,
          Colors.blue.shade300,
          Colors.green.shade400,
          Colors.teal.shade500,
        ];
      case PlanetHealth.stable:
        return [
          Colors.purple.shade300,
          Colors.blue.shade400,
          Colors.indigo.shade500,
          Colors.deepPurple.shade600,
        ];
      case PlanetHealth.decaying:
        return [
          Colors.grey.shade400,
          Colors.grey.shade600,
          Colors.brown.shade600,
          Colors.grey.shade800,
        ];
    }
  }

  double _getGlowIntensity() {
    switch (widget.health) {
      case PlanetHealth.flourishing:
        return 0.6;
      case PlanetHealth.stable:
        return 0.4;
      case PlanetHealth.decaying:
        return 0.1;
    }
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: widget.onTap,
      child: SizedBox(
        width: widget.size,
        height: widget.size,
        child: Stack(
          alignment: Alignment.center,
          children: [
            // Outer glow effect
            AnimatedBuilder(
              animation: _pulseController,
              builder: (context, child) {
                final glowScale = 1.0 + (_pulseController.value * 0.1);
                final glowOpacity = _getGlowIntensity() * (0.7 + _pulseController.value * 0.3);
                
                return Transform.scale(
                  scale: glowScale,
                  child: Container(
                    width: widget.size,
                    height: widget.size,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      boxShadow: [
                        BoxShadow(
                          color: _getPrimaryColor().withValues(alpha: glowOpacity),
                          blurRadius: 30,
                          spreadRadius: 15,
                        ),
                        BoxShadow(
                          color: _getSecondaryColor().withValues(alpha: glowOpacity * 0.5),
                          blurRadius: 50,
                          spreadRadius: 25,
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
            
            // Main planet body
            AnimatedBuilder(
              animation: _rotationController,
              builder: (context, child) {
                return Transform.rotate(
                  angle: _rotationController.value * 2 * math.pi,
                  child: Container(
                    width: widget.size * 0.8,
                    height: widget.size * 0.8,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      gradient: RadialGradient(
                        center: const Alignment(-0.3, -0.3),
                        radius: 0.8,
                        colors: _getGradientColors(),
                        stops: const [0.0, 0.3, 0.6, 1.0],
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withValues(alpha: 0.4),
                          blurRadius: 20,
                          offset: const Offset(5, 5),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
            
            // Surface details and texture
            Container(
              width: widget.size * 0.8,
              height: widget.size * 0.8,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: RadialGradient(
                  center: const Alignment(0.3, 0.3),
                  radius: 0.6,
                  colors: [
                    Colors.transparent,
                    Colors.black.withValues(alpha: 0.1),
                    Colors.black.withValues(alpha: 0.3),
                  ],
                ),
              ),
            ),
            
            // Atmospheric rings (for flourishing and stable states)
            if (widget.health != PlanetHealth.decaying)
              AnimatedBuilder(
                animation: _rotationController,
                builder: (context, child) {
                  return Transform.rotate(
                    angle: -_rotationController.value * 2 * math.pi * 0.5,
                    child: Container(
                      width: widget.size * 1.1,
                      height: widget.size * 0.2,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(widget.size),
                        gradient: LinearGradient(
                          colors: [
                            Colors.transparent,
                            _getPrimaryColor().withValues(alpha: 0.3),
                            Colors.transparent,
                          ],
                        ),
                      ),
                    ),
                  );
                },
              ),
            
            // Quantum Core (if enabled)
            if (widget.showQuantumCore)
              AnimatedBuilder(
                animation: _coreController,
                builder: (context, child) {
                  final coreScale = 0.3 + (_coreController.value * 0.1);
                  final coreOpacity = 0.8 + (_coreController.value * 0.2);
                  
                  return Transform.scale(
                    scale: coreScale,
                    child: Container(
                      width: widget.size * 0.3,
                      height: widget.size * 0.3,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        gradient: RadialGradient(
                          colors: [
                            Colors.white.withValues(alpha: coreOpacity),
                            _getPrimaryColor().withValues(alpha: coreOpacity * 0.8),
                            Colors.transparent,
                          ],
                        ),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.white.withValues(alpha: coreOpacity * 0.5),
                            blurRadius: 20,
                            spreadRadius: 5,
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            
            // Tap indicator
            if (widget.onTap != null)
              Positioned(
                bottom: widget.size * 0.1,
                child: AnimatedBuilder(
                  animation: _pulseController,
                  builder: (context, child) {
                    return Opacity(
                      opacity: 0.6 + (_pulseController.value * 0.4),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                        decoration: BoxDecoration(
                          color: Colors.black.withValues(alpha: 0.7),
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(
                            color: _getPrimaryColor().withValues(alpha: 0.5),
                            width: 1,
                          ),
                        ),
                        child: Text(
                          'TAP TO FORGE',
                          style: TextStyle(
                            color: _getPrimaryColor(),
                            fontSize: 10,
                            fontWeight: FontWeight.bold,
                            letterSpacing: 1,
                          ),
                        ),
                      ),
                    );
                  },
                ),
              ),
          ],
        ),
      ),
    );
  }
}

/// Particle effect widget for SS generation feedback
class ForgeParticleEffect extends StatefulWidget {
  final Offset position;
  final Color color;
  final VoidCallback onComplete;
  
  const ForgeParticleEffect({
    super.key,
    required this.position,
    required this.color,
    required this.onComplete,
  });

  @override
  State<ForgeParticleEffect> createState() => _ForgeParticleEffectState();
}

class _ForgeParticleEffectState extends State<ForgeParticleEffect>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late List<_Particle> _particles;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 1500),
      vsync: this,
    );
    
    _generateParticles();
    _controller.forward().then((_) => widget.onComplete());
  }

  void _generateParticles() {
    final random = math.Random();
    _particles = List.generate(8, (index) {
      final angle = (index / 8) * 2 * math.pi;
      final velocity = 50.0 + random.nextDouble() * 30;
      
      return _Particle(
        startX: widget.position.dx,
        startY: widget.position.dy,
        velocityX: math.cos(angle) * velocity,
        velocityY: math.sin(angle) * velocity,
        color: widget.color,
        size: 3.0 + random.nextDouble() * 3,
      );
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return CustomPaint(
          painter: _ParticlesPainter(_particles, _controller.value),
          size: const Size(300, 300),
        );
      },
    );
  }
}

class _Particle {
  final double startX;
  final double startY;
  final double velocityX;
  final double velocityY;
  final Color color;
  final double size;

  _Particle({
    required this.startX,
    required this.startY,
    required this.velocityX,
    required this.velocityY,
    required this.color,
    required this.size,
  });
}

class _ParticlesPainter extends CustomPainter {
  final List<_Particle> particles;
  final double progress;

  _ParticlesPainter(this.particles, this.progress);

  @override
  void paint(Canvas canvas, Size size) {
    for (final particle in particles) {
      final x = particle.startX + (particle.velocityX * progress);
      final y = particle.startY + (particle.velocityY * progress);
      final opacity = (1.0 - progress).clamp(0.0, 1.0);
      final particleSize = particle.size * (1.0 - progress * 0.5);

      final paint = Paint()
        ..color = particle.color.withValues(alpha: opacity)
        ..style = PaintingStyle.fill;

      canvas.drawCircle(Offset(x, y), particleSize, paint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}