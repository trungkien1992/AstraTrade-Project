// User model for AstraTrade application

class User {
  final String id;
  final String name;
  final String email;
  final String? walletAddress;
  final DateTime createdAt;
  
  const User({
    required this.id,
    required this.name,
    required this.email,
    this.walletAddress,
    required this.createdAt,
  });
  
  // TODO: Add fromJson and toJson methods
  // TODO: Add copyWith method for immutable updates
}