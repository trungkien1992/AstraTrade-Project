AstraTrade: Game Specifications 
This document provides detailed technical specifications for implementing AstraTrade, a gamified perpetuals trading application. It adheres to the "Cosmic Catalyst" design philosophy (v4.0), emphasizing radical abstraction of blockchain and trading complexities into an addictive, visually rewarding cosmic growth experience.
1. Core Game Mechanics
1.1. Orbital Forging (Free-to-Play Layer)
Currency: Stellar Shards (SS) - The primary, abundant in-game currency.
Generation Methods:
Manual Tap: User taps on the central planet/Quantum Core. Each tap triggers a "Forge Cycle" generating a base amount of SS.
Automated (Astro-Forgers): Bots (Astro-Forgers) are purchased and upgraded with SS. Each Astro-Forger automatically performs "Forge Cycles" at a defined interval, generating SS over time.
Efficiency Calculation: SS generation rate per Astro-Forger is determined by its base level, specific type, active "planet health" buffs, and any active "Cosmic Genesis Node" multipliers.
Visual & Auditory Feedback Loop (The "Astro-Forging Beat"):
Visual: On every SS generation (manual tap or automated cycle), emit a vibrant, customizable particle burst from the point of origin (planet tap location or Astro-Forger). The color and intensity of the burst should scale with the amount of SS generated (e.g., larger, brighter burst for "Crit Forges").
Auditory: Play a distinct, harmonious "chime" sound effect for each SS generation. A unique, deeper, and more resonant chime should play for "Crit Forges."
Planet Growth Visuals: Accumulation of SS should visibly contribute to minor, incremental, organic changes on the planet's surface (e.g., new flora sprouting, small, intricate structures appearing, atmospheric density visibly increasing). These changes are cosmetic but provide a sense of continuous progression.
Spending SS: SS is used to:
Purchase new Astro-Forgers (unlocks new automation tiers).
Upgrade existing Astro-Forgers (increases their SS generation rate and unlocks new visual tiers for the Astro-Forger model).
Unlock and expand "Terraforming Blocks" (new landmasses/biomes on the planet, expanding the visual canvas).
Purchase "Cosmic Flora & Fauna" (cosmetic elements that also provide minor, passive SS generation buffs or visual flair).
Upgrade "Basic Core Upgrades" (incremental, flat percentage boosts to overall SS generation, "Crit Chance," and "Foraging Speed").
1.2. Quantum Harvesting (Pro Trader Layer)
Currency: Lumina (LM) - The premium, highly coveted progression resource.
Generation: LM is exclusively "harvested" from real-money trades executed via the "Cosmic Forge" UI.
Formula: LM_generated = Base_LM * f(Trade_PnL_Ratio, Trade_Volume, Consecutive_Win_Streak, Quantum_Harvest_Efficiency_Multiplier).
A positive PnL ratio, higher volume, and longer consecutive win streaks significantly increase LM generation.
Even losing trades (negative PnL) will generate a small, fixed amount of "Stardust Fragments" (see 4.1) and contribute to "Shield Dust" (see 4.2), ensuring a form of reward even without LM.
Visual Feedback:
Harvest Animation: Upon successful LM generation, a captivating animation of glowing Lumina particles visually flows from the "Cosmic Forge" UI (trading interface) directly into the Quantum Core at the center of the player's planet.
"Quantum Harvest Efficiency Gauge": A dynamic, pulsating energy bar or radial gauge within the "Cosmic Forge" UI that visually fills up in real-time during a trade's outcome, indicating the efficiency of the current trade in generating LM. A full gauge signifies maximum LM harvest.
2. Player Journey & Progression
2.1. Stage 0: Frictionless Onboarding – The First Glimmer
Login Flow: Implement social login (Google/Apple OAuth) as the sole entry point.
Backend Wallet Creation (Transparent): Upon successful social login, trigger a backend process to create a secure smart contract wallet (Starknet Account Abstraction). This entire process must be completely transparent and hidden from the user. No wallet addresses, seed phrases, or gas fees are ever explicitly mentioned or shown.
Initial Planet Selection: User is presented with a visually appealing carousel of "Cosmic Seeds" (planet archetypes: e.g., "Verdant," "Volcanic," "Crystalline"). This choice is initially cosmetic but influences early biome aesthetics.
2.2. Stage 1: The Cosmic Gardener – Nurturing the Seed
Default State: All new users begin in this F2P state, with access only to the "Orbital Forging" mechanics.
UI Elements: The main screen prominently displays their chosen planet. A dormant "Quantum Core" at the planet's center pulses faintly, a visual mystery. A "Lumina Flow Leaderboard" (read-only initially) shimmers on a separate tab, subtly introducing the concept of a higher tier of power and elite status.
"Cosmic Hints" (Soft Education): Implement a system for subtle, non-intrusive in-game hints. These could be animated "Cosmic wisps" that occasionally float across the screen with short, thematic text overlays (e.g., "The Quantum Core sleeps, awaiting Lumina to awaken its true power...", "The most vibrant planets have harnessed Lumina's energy..."). These hints are designed to pique curiosity without overwhelming.
2.3. Stage 2: Genesis Ignition – The First Spark of Lumina
This is the pivotal, celebrated initiation into the Pro Trader layer.
Trigger: The "Cosmic Genesis" Quest becomes available (e.g., after reaching a certain cumulative SS threshold, time played, or specific Astro-Forger upgrade). A prominent, glowing quest icon appears.
"Lumina Conduit" (On-Ramp):
Integrate a secure fiat-to-crypto on-ramp solution SDK (e.g., Banxa, Ramp, MoonPay).
The UI for this process must be highly stylized as a "Lumina Conduit" – a visually engaging, animated interface where players "channel" external energy (fiat currency) into their account. The focus is on the flow of energy into the game's ecosystem, not a financial transaction.
Handle the purchase of a small, pre-defined amount of crypto (e.g., USDC) directly within the app's themed UI.
"First Harvest" Guided Trade:
After funding, the player is presented with a simplified, visually guided "First Harvest" scenario.
Abstraction: Trading parameters are abstracted into cosmic terms (e.g., "Detecting Stellar Flux," "Optimizing Orbital Trajectory").
Simplified Choice: User makes a simple "direction" choice: "Orbital Ascent" (long) or "Gravitational Descent" (short) via intuitive visual buttons. Minimal other parameters are exposed initially.
Simulated PnL (Pre-Trade): Briefly display a tiny, simulated PnL (abstracted as "Stellar Gain/Loss") before the real trade executes, to familiarize the user with the concept of market movement without real risk.
Execution: The system handles the underlying real trade execution on a perpetuals exchange (via backend integration).
Permanent Cosmic Awakening ("Genesis Metamorphosis"):
Upon successful execution of this very first real-money trade, the player's planet undergoes a dramatic, full-screen, unskippable animation. This could involve rings of energy coalescing around the planet, new celestial bodies appearing in orbit, or the Quantum Core erupting with brilliant light.
This is a permanent, irreversible visual upgrade – a clear, superior, and visible indicator of their "Pro" status.
"Lumina Cascade" Bonus: Immediately following the metamorphosis, grant a substantial, one-time Lumina bonus. This bonus is visually delivered as a spectacular cascade of glowing particles pouring directly into the Quantum Core. This allows the player to instantly unlock their first "Cosmic Genesis Node" or a powerful "Lumina Infusion" to feel its immediate impact.
2.4. Stage 3: The Lumina Weaver – Orchestrating the Cosmos
After "Genesis Ignition," the player accesses a new, powerful dimension of the game where real trades directly influence their cosmic destiny.
The Quantum Core & "Cosmic Genesis" Grid:
The Quantum Core, now active and glowing, becomes the central interactive element.
A grid-based UI (the "Cosmic Genesis Grid") appears on the planet's surface, radiating from the Core. This grid contains empty "Cosmic Genesis Nodes."
LM is spent to activate and upgrade these nodes. Each node has a unique visual representation (e.g., a "Graviton Amplifier," "Chrono-Accelerator," "Bio-Synthesis Nexus"), implying its function through cosmic metaphors.
Cosmic Genesis Node Effects (Specific & Impactful): Each activated/upgraded Genesis Node provides a specific, highly impactful multiplier or passive effect on the idle game's "Orbital Forging" mechanics, rather than a generic multiplier.
Example Effects:
"Graviton Amplifier Level 1": Multiplies SS generation from Astro-Forgers in specific biomes by X%.
"Chrono-Accelerator Level 1": Reduces upgrade timers for F2P elements (Astro-Forgers, Terraforming) by Y%.
"Bio-Synthesis Nexus Level 1": Boosts SS generation from "Cosmic Flora & Fauna" by Z%.
"Dimensional Shifter Level 1": Grants a small chance for bonus SS drops from any source.
Dynamic Visual Feedback: As Lumina is infused into nodes, energy visibly flows from the Quantum Core, illuminating pathways and structures on the grid, creating a sense of powerful, directed growth and strategic investment.
Strategic LM Infusion: Pro Traders gain the strategic choice of how to "infuse" their harvested Lumina:
Core Overclocking: Increases the base global SS multiplier from the Quantum Core.
Resonance Amplifiers: Unlocks new visual effects and powerful temporary boosts for "Resonance Spikes" (see 3.2).
Planetary Schema Expansion: Unlocks entirely new, Pro-exclusive building plots or biomes on your planet. These are visually distinct, often more complex, and offer unique, high-tier SS generation methods or advanced cosmetic options.
The "Catalyst Flow" – Integrated Dual Gameplay: The player is now simultaneously engaged in:
The Idle Game (Orbital Forging): Continuously generates Stellar Shards at a hyper-accelerated rate, dynamically shaped by their Lumina investments, to expand their planet's physical domain.
The Pro Game (Quantum Harvesting): Strategically placing real trades to harvest Lumina. This Lumina is then used to activate and level up "Cosmic Genesis Nodes," infuse "Resonance Amplifiers," and expand their "Planetary Schema," creating a powerful, self-reinforcing feedback loop that makes their idle game exponentially more powerful and visually spectacular.
3. Abstraction Layer Details (Critical for User Experience)
3.1. Market Data Abstraction ("Stellar Flux")
Visual Representation: Real-time market data (e.g., BTC/USDC price movements) are abstracted into visually compelling, dynamic "Stellar Flux" graphs. These are not traditional candlesticks but rather undulating energy waves, shimmering nebulae, or fluctuating gravitational fields. The visual intensity and pattern should intuitively convey volatility and trend.
Trading Direction: User choices are abstracted to "Orbital Ascent" (long position) or "Gravitational Descent" (short position), represented by clear, thematic visual buttons.
"Cosmic Forecasts": Integrate an LLM (specifically gemini-2.0-flash) to generate simplified, thematic "forecasts" based on real market sentiment or technical indicators.
LLM Prompt: "Analyze current market sentiment for [asset pair, e.g., BTC/USDC] and provide a short, cosmic-themed forecast (e.g., 'Nebula Forming: Volatility Ahead', 'Stellar Drift: Steady Ascent', 'Solar Flare Imminent: Sharp Drop Expected'). Do not use financial jargon, numbers, or specific trading advice. Focus purely on a metaphorical cosmic prediction."
Display: Display these forecasts as short, animated text snippets or subtle visual cues (e.g., a small nebula appearing on the "Stellar Flux" graph).
3.2. PnL & Volume Abstraction ("Lumina Harvest Efficiency")
Lumina Harvest Efficiency Gauge: For each real trade, a dynamic visual gauge (e.g., a pulsating energy bar or radial fill) is displayed. It fills up to indicate the efficiency of the current trade in generating Lumina. A full gauge signifies maximum LM generation (profitable trade with high volume/streak). A partially filled or empty gauge indicates lower/zero LM generation.
Loss Aversion Mitigation:
No Explicit "Loss": The term "loss" is never explicitly shown. Instead, a losing trade results in "Lumina Harvest Efficiency: Low" or "Lumina Harvest Efficiency: Zero." The focus is always on what was gained (even if minimal, like Stardust Fragments or Shield Dust), not what was lost.
Stardust Fragments: Even losing trades contribute a small, fixed amount of "Stardust Fragments" (visualized as tiny, shimmering particles) towards the Stardust Lottery.
"Cosmic Resonance Spikes": Successful real trades don't just grant LM; they trigger temporary "Resonance Spikes" from your Quantum Core. These are visually stunning energy waves that visibly channel across your planet, activating "Supercharged Nodes" or temporarily boosting specific resource generation zones (see 2.4).
3.3. Blockchain Abstraction
Zero Blockchain Terminology: Absolutely no terms like "wallet," "gas fees," "chain," "transaction hash," "smart contract," "dApp," "minting," "staking," etc., are ever exposed to the user.
"Cosmic Vault" / "Lumina Reservoir": The user's account balance (fiat/crypto) is displayed as their "Cosmic Vault" or "Lumina Reservoir," using cosmic iconography and animations.
"Cosmic Friction": Gas fees are entirely abstracted away and subsidized by the game. If an unavoidable, negligible fee occurs, it's represented as a brief, ethereal shimmer or a subtle "Cosmic Friction" visual effect during a process, with no numerical value displayed.
Seamless Integration: The backend handles all wallet creation, key management (secure enclave), and transaction signing via Starknet Account Abstraction without any user interaction or awareness.
Integrated On-Ramp: As specified in 2.3, the "Lumina Conduit" is a fully integrated, in-app experience.
4. Direct Rewards & Risk Mitigation
4.1. Stardust Lottery
Mechanism: Every real trade (win or lose) grants one "Stardust Ticket." Additionally, all trades (including losing ones) contribute a small, fixed amount of "Stardust Fragments" that accumulate towards bonus tickets.
Lottery Draw: A weekly automated lottery draw occurs at a fixed time. Winners are announced via in-game notifications and a dedicated "Cosmic News" feed.
Prizes: Large LM pools, exclusive limited-edition NFTs (cosmetic only, no gameplay advantage), and unique planetary cosmetic elements.
4.2. Shield Generation ("Shield Dust")
Generation: Real trading activity (win or lose) passively generates "Shield Dust." The rate of generation increases with trading volume.
Consumption & Effect: "Shield Dust" is automatically consumed when a mock trade (in the idle game) would result in a negative effect (e.g., a bot's SS generation temporarily dipping, a "planet decay" event).
Visuals: When consumed, an animated "Shield Aura" visually envelops the affected Astro-Forger or biome, absorbing the "negative energy" and preventing any detrimental impact on the idle game. A calming sound effect accompanies the shield activation. This provides a tangible sense of protection and reduces the perceived punishment of idle game losses.
4.3. Pro-Exclusive "Quantum Anomalies"
Trigger: Rare, procedurally generated events triggered by significant cumulative LM earnings or specific real-trading milestones (e.g., completing a high-volume trade, achieving a long streak).
Manifestation: Visually distinct, temporary cosmic phenomena appear near the player's planet (e.g., a swirling wormhole, an unstable energy field, a rogue celestial body).
Interaction: Interacting with Anomalies involves unique, gamified micro-quests or challenges:
Trading Challenges: "Sustain a 5-trade winning streak during this anomaly to stabilize it."
Strategic Decisions: Choosing a path within the anomaly that has different risk/reward outcomes.
Mini-Games: Simple, quick mini-games that, if completed successfully, yield rewards.
Rewards: Massive SS bonuses, rare cosmetic drops, small bonus LM rewards, or exclusive "Anomaly Fragments" that can be combined for unique items.
Risk/Reward: Some anomalies might present a slight, temporary risk (e.g., a brief reduction in SS generation if the challenge is failed), but with proportionally greater rewards for success. The risk is always framed in game terms, not financial terms.
5. Advanced Social & Prestige Systems
5.1. Dual Leaderboards
Trade Token Leaderboard: Ranks all players (F2P and Pro) based on accumulated SS earnings, showcasing idle game mastery.
Lumina Flow Leaderboard: The ultimate "Pro" leaderboard, ranking players by total LM harvested. This is the true measure of trading prowess and cosmic influence.
UI: Clear, visually distinct leaderboards with smooth scrolling. Each entry features the player's chosen avatar/name, their current mini-planet icon, and their "Verified Lumina Weaver" flair if applicable.
5.2. "Verified Lumina Weaver" Flair & Visual Cues
Activation: Automatically applied to a player's profile and planet upon successful "Genesis Ignition."
Visuals: A distinct, permanent visual flair (e.g., a shimmering, animated cosmic aura around their planet, a special animated badge by their name) visible across all social features and leaderboards, immediately signifying their elevated status.
5.3. Interactive "Trading Constellations" (Guilds)
Formation: Players can form or join "Trading Constellations" (guilds/alliances).
Galactic Map Visualization: Member planets visually cluster together on a dynamic, zoomable galactic map. The constellation grows larger, brighter, and more elaborate (e.g., forming nebulae, connecting via light-speed lanes) based on the collective LM earnings and achievements of its members.
Inter-Constellation Challenges: Weekly or monthly "Cosmic Market Challenges" encourage friendly competition between constellations. Guilds compete to achieve specific collective trading objectives (e.g., highest collective "Stellar Gain" in a specific "Stellar Flux" type, most consistent trading volume over a period) for shared LM bonuses, unique temporary constellation-wide visual effects, and exclusive cosmetic rewards for all members.
5.4. "Pro Trader Broadcasts" & "Market Pulse"
"Market Pulse Insights": Top-ranked "Lumina Weavers" (e.g., top 100 on the Lumina Flow Leaderboard) are given the option to periodically share short, text-based "Market Pulse Insights."
Content: Observations on "Stellar Flux" trends or strategic approaches (must be non-financial advice, system-moderated for appropriate content).
Display: A dedicated in-game feed where players can view, "like," and "react" to these insights, fostering community discussion.
"Pro Trader Spotlight": A visually appealing rotating feature on the main screen showcasing a top-ranked player's unique planet, LM progress, and a brief, pre-approved bio or "cosmic philosophy" on trading, inspiring the broader player base.
6. The Long Game: Cosmic Ascension & NFT Utility
6.1. Cosmic Ascension Tiers
Progression: Beyond accumulating LM, Pro Traders ascend through Cosmic Ascension Tiers (e.g., "Nebula Novice," "Stellar Strategist," "Galaxy Grandmaster," "Universal Sovereign"). Tiers are unlocked by reaching significant cumulative LM milestones and completing specific real-trading achievements (e.g., "Achieve X total Stellar Gain," "Maintain Z streak across 3 months," "Participate in Y Quantum Anomalies").
Tier Rewards: Each ascension tier unlocks progressively grander rewards:
Exclusive Planet Customization: New, visually distinct and undeniably prestigious options (e.g., orbiting moons, advanced space stations, cosmic weather patterns, unique planetary rings).
Elite Astro-Forgers: Unique Astro-Forger models with special abilities (e.g., a "Market Oracle Bot" that provides subtle, non-financial "hints" in the idle game, or a "Volatility Harvester Bot" that thrives during specific "Stellar Flux" conditions).
Enhanced Stardust Lottery payouts and improved odds.
Access to exclusive social hubs or private channels within the game, fostering an elite community.
6.2. NFT Utility
Exclusive Minting Whitelist: Only Pro Trader wallets (identified by their underlying smart contract wallet) are whitelisted for minting the most prestigious cosmetic NFTs. These NFTs are verifiable on-chain and serve as ultimate status symbols.
"Artifact NFTs": Introduce rare "Artifact NFTs" that, when held in the user's wallet, grant minor, non-game-breaking passive benefits in the idle game (e.g., "+1% Astro-Forger efficiency," "-0.5% upgrade costs," "grants a slight boost to crit chance"). These are carefully balanced to be non-pay-to-win, acting as subtle advantages that reward long-term engagement and collection.
"Event NFTs": Limited-edition NFTs issued for participating in specific in-game events, achieving challenging trading milestones, or excelling in Constellation Challenges. These offer both prestige and potential future utility in new game modes or collaborations.
7. Technical Considerations for AI Coders
This section details the specific technologies and implementation considerations, differentiating between native mobile (Flutter) and web (React) where necessary.
Frontend Frameworks:
Native Mobile (iOS & Android): Flutter
Rationale: Chosen for its ability to build natively compiled, high-performance, and visually rich applications from a single codebase. Its expressive UI toolkit and strong support for custom animations make it ideal.
State Management: Provider, Riverpod, or Bloc for robust and scalable state management.
UI/UX: Leverage Flutter's custom painting capabilities and widget composition for bespoke cosmic aesthetics and animations.
Styling:
Native Mobile (Flutter): Custom Thematic Styling. Flutter's powerful widget system and custom painting (CustomPainter) will be leveraged to create bespoke, highly animated, and thematically consistent UI components. This ensures the unique cosmic aesthetic is delivered natively without reliance on external CSS frameworks. Focus on Material Design principles adapted to the cosmic theme.
Web (React): Tailwind CSS. Utilized extensively for rapid UI development and consistent design system implementation, ensuring full responsiveness.
3D Graphics:
Native Mobile (Flutter): Explore flutter_3d_controller for simpler 3D elements (e.g., orbiting Astro-Forgers). For the complex, high-performance planet rendering and particle systems, consider direct integration with native graphics APIs (OpenGL ES / Metal) via Flutter plugins (e.g., flutter_gl or custom FFI bindings to a C++ rendering engine). This ensures optimal performance and visual fidelity.
Web (React): three.js. Powerful library for creating and rendering complex 3D scenes directly in the browser. Optimize three.js scenes for mobile GPUs (LOD, instancing, careful polygon budgeting).
Audio:
Native Mobile (Flutter): audioplayers or just_audio packages. For robust audio playback, low-latency sound effects, and dynamic background music. Implement a system for layering music tracks based on player progress and "Stellar Flux" conditions.
Web (React): Tone.js. For advanced control over audio synthesis, effects, and dynamic background music, leveraging the Web Audio API.
Backend Integration (APIs): Seamless communication with:
Starknet Account Abstraction: Implement SDK/API calls for transparent wallet creation, key management (secure enclave integration), and transaction signing.
Perpetuals Exchange API: Connect to a chosen perpetuals exchange (e.g., dYdX, GMX) for real-time market data ("Stellar Flux") and trade execution ("Quantum Harvesting"). All API calls must be abstracted.
Fiat On-Ramp SDK/API: Integrate selected on-ramp provider (e.g., Banxa, Ramp, MoonPay) SDK for the "Lumina Conduit" functionality.
LLM Integration: gemini-2.0-flash for "Cosmic Forecasts" (as detailed in 3.1) and potentially other dynamic text generation for in-game events or narrative elements.
Firestore: Utilize Firestore for all game state persistence, player progress, social data, and leaderboards.
Security Rules: Implement strict Firestore security rules (public/private data as per previous instructions).
Real-time Updates: Utilize onSnapshot() listeners for real-time UI updates across all relevant game elements (e.g., SS/LM counters, leaderboard changes, planet state).
Error Handling: Implement robust try/catch blocks and user-friendly, in-game error messages (no alert() or confirm() dialogs). Use custom modal UI for critical information.
Performance Optimization:
Optimize animations, particle systems, and data fetching to ensure a smooth, fluid experience across all platforms, especially on mobile.
Minimize Cumulative Layout Shifts (CLS) in web and ensure smooth frame rates in Flutter.
Implement lazy loading for assets to reduce initial load times.
Security: Prioritize secure coding practices, especially for all financial interactions and API key management. Ensure all sensitive data is handled securely on the backend.
User Experience (UX) Principles:
Intuitive Design: All UI elements must be self-explanatory and visually appealing, relying on cosmic metaphors rather than explicit instructions.
Immediate Feedback: Provide instant and clear visual, auditory, and haptic (where supported) feedback for every user action.
Clear Progress Indicators: Use animated progress bars, fill animations, and clear numerical displays for all growth metrics (SS, LM, upgrade progress).
Responsive Layouts: Ensure optimal viewing and interaction on all devices and orientations.

