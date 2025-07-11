Directory structure:
└── web3auth-web3auth-flutter-sdk/
    ├── README.md
    ├── analysis_options.yaml
    ├── CHANGELOG.md
    ├── LICENSE
    ├── pubspec.yaml
    ├── .metadata
    ├── .pubignore
    ├── android/
    │   ├── consumer_rules.pro
    │   ├── proguard-rules.pro
    │   ├── gradle/
    │   │   └── wrapper/
    │   │       └── gradle-wrapper.properties
    │   └── src/
    │       └── main/
    │           ├── AndroidManifest.xml
    │           └── kotlin/
    │               └── com/
    │                   └── web3auth/
    │                       └── flutter/
    │                           └── web3auth_flutter/
    │                               └── Web3AuthFlutterPlugin.kt
    ├── example/
    │   ├── README.md
    │   ├── analysis_options.yaml
    │   ├── pubspec.lock
    │   ├── pubspec.yaml
    │   ├── .metadata
    │   ├── android/
    │   │   ├── gradle.properties
    │   │   ├── app/
    │   │   │   └── src/
    │   │   │       ├── debug/
    │   │   │       │   └── AndroidManifest.xml
    │   │   │       ├── main/
    │   │   │       │   ├── AndroidManifest.xml
    │   │   │       │   ├── kotlin/
    │   │   │       │   │   └── com/
    │   │   │       │   │       └── openlogin/
    │   │   │       │   │           └── flutter/
    │   │   │       │   │               └── openlogin_flutter_example/
    │   │   │       │   │                   └── MainActivity.kt
    │   │   │       │   └── res/
    │   │   │       │       ├── drawable/
    │   │   │       │       │   └── launch_background.xml
    │   │   │       │       ├── drawable-v21/
    │   │   │       │       │   └── launch_background.xml
    │   │   │       │       ├── values/
    │   │   │       │       │   └── styles.xml
    │   │   │       │       └── values-night/
    │   │   │       │           └── styles.xml
    │   │   │       └── profile/
    │   │   │           └── AndroidManifest.xml
    │   │   └── gradle/
    │   │       └── wrapper/
    │   │           └── gradle-wrapper.properties
    │   ├── ios/
    │   │   ├── Podfile
    │   │   ├── Podfile.lock
    │   │   ├── Flutter/
    │   │   │   ├── AppFrameworkInfo.plist
    │   │   │   ├── Debug.xcconfig
    │   │   │   └── Release.xcconfig
    │   │   └── Runner/
    │   │       ├── AppDelegate.swift
    │   │       ├── Info.plist
    │   │       ├── Runner-Bridging-Header.h
    │   │       ├── Assets.xcassets/
    │   │       │   ├── AppIcon.appiconset/
    │   │       │   │   └── Contents.json
    │   │       │   └── LaunchImage.imageset/
    │   │       │       ├── README.md
    │   │       │       └── Contents.json
    │   │       └── Base.lproj/
    │   │           ├── LaunchScreen.storyboard
    │   │           └── Main.storyboard
    │   ├── lib/
    │   │   └── main.dart
    │   └── test/
    │       └── widget_test.dart
    ├── ios/
    │   ├── web3auth_flutter.podspec
    │   ├── Assets/
    │   │   └── .gitkeep
    │   └── Classes/
    │       ├── SwiftWeb3AuthFlutterPlugin.swift
    │       ├── Web3AuthFlutterPlugin.h
    │       └── Web3AuthFlutterPlugin.m
    ├── lib/
    │   ├── enums.dart
    │   ├── input.dart
    │   ├── output.dart
    │   └── web3auth_flutter.dart
    └── test/
        └── web3auth_flutter_test.dart


Files Content:

================================================
FILE: README.md
================================================
# Web3Auth Flutter SDK

Web3Auth is where passwordless auth meets non-custodial key infrastructure for Web3 apps and wallets. By aggregating OAuth (Google, Twitter, Discord) logins, different wallets and innovative Multi Party Computation (MPC) - Web3Auth provides a seamless login experience to every user on your application.

## 📖 Documentation

Checkout the official [Web3Auth Documentation](https://web3auth.io/docs) and [SDK Reference](https://web3auth.io/docs/sdk/pnp/flutter) to get started!

## 💡 Features

- Plug and Play, OAuth based Web3 Authentication Service
- Fully decentralized, non-custodial key infrastructure
- End to end Whitelabelable solution
- Threshold Cryptography based Key Reconstruction
- Multi Factor Authentication Setup & Recovery (Includes password, backup
  phrase, device factor editing/deletion etc)
- Support for WebAuthn & Passwordless Login
- Support for connecting to multiple wallets
- DApp Active Session Management

...and a lot more

## ⏪ Requirements

- For iOS, only iOS 14+ supported since we requires ASWebAuthenticationSession.
  - Xcode 11.4+ / 12.x
  - Swift 4.x / 5.x
  - For iOS build: `platform :ios` needs to be `14.0`. Check `ios/Podfile` in
    your Flutter project to change it.
- For Android, API version 26 or newer is supported.
  - For Android build: compileSdkVersion needs to be 34.
  - Check `android/app/build.gradle` in your Flutter project to change it.

## ⚡ Installation

Add `web3auth_flutter` as a dependency to your `pubspec.yaml` file.

```yml
dependencies:
  web3auth_flutter: ^6.1.2
```

or

```sh
flutter pub add web3auth_flutter
```

## 🌟 Configuration

Checkout [SDK Reference](https://web3auth.io/docs/sdk/pnp/flutter/install) to configure for Android and iOS
builds.

## 🩹 Example

Checkout the examples for your preferred blockchain and platform in our [examples](https://web3auth.io/docs/examples)

```dart
// Initialization
await Web3AuthFlutter.init(
  Web3AuthOptions(
    // Get your client it from dashboard.web3auth.io
    clientId: 'YOUR_WEB3AUTH_CLIENT_ID',
    network: Network.sapphire_devnet,
    // Your redirect url, check how to configure.
    // Android: https://web3auth.io/docs/sdk/pnp/flutter/install#android-configuration
    // iOS: https://web3auth.io/docs/sdk/pnp/flutter/install#ios-configuration
    redirectUrl: redirectUrl,
  ),
);

// Call initialize() function to get privKey and user information without relogging in
// user if a user has an active session. If no active session is present, the 
// function throws an error. 
await Web3AuthFlutter.initialize();

// Login
await Web3AuthFlutter.login(LoginParams(loginProvider: Provider.google));

// Logout
await Web3AuthFlutter.logout();
```

## Triggering UserCancellation on Android

On Android, if you want to trigger exception for user closing the browser tab, you have to use
`WidgetsBindingObserver` mixin with your your login screen.

```dart
class LoginScreen extends State<MyApp> with WidgetsBindingObserver {
 
  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
  }
  @override
  void dispose() {
    super.dispose();
    WidgetsBinding.instance.removeObserver(this);
  }
  @override
  void didChangeAppLifecycleState(final AppLifecycleState state) {
    // This is important to trigger the user cancellation on Android.
    if (state == AppLifecycleState.resumed) {
      Web3AuthFlutter.setCustomTabsClosed();
    }
  }
  
   @override
  Widget build(BuildContext context) { 
    // Your UI code
  }
  Future<void> _login() async {
    try {
      await Web3AuthFlutter.login(LoginParams(loginProvider: Provider.google));
    } on UserCancelledException {
        log("User cancelled.");
    } on UnKnownException {
        log("Unknown exception occurred");
    } catch (e) {
        log(e.toString());
    }
  }
}
```

## 🌐 Demo

Checkout the [Web3Auth Demo](https://demo-app.web3auth.io/) to see how Web3Auth can be used in an application.

Have a look at our [Web3Auth PnP Flutter Quick Start](https://web3auth.io/docs/quick-start?product=PNP&sdk=PNP_FLUTTER&framework=IOS&stepIndex=0) to help you quickly integrate a basic instance of Web3Auth Plug and Play in your Flutter app.

Further checkout the [example folder](https://github.com/Web3Auth/web3auth-flutter-sdk/tree/master/example) within this repository, which contains a sample app.

## 💬 Troubleshooting and Support

- Have a look at our [Community Portal](https://community.web3auth.io/) to see if anyone has any questions or issues you might be having. Feel free to create new topics and we'll help you out as soon as possible.
- Checkout our [Troubleshooting Documentation Page](https://web3auth.io/docs/troubleshooting) to know the common issues and solutions.
- For Priority Support, please have a look at our [Pricing Page](https://web3auth.io/pricing.html) for the plan that suits your needs.



================================================
FILE: analysis_options.yaml
================================================
include: package:flutter_lints/flutter.yaml

# Additional information about this file can be found at
# https://dart.dev/guides/language/analysis-options
linter:
  rules:
    constant_identifier_names: false
    non_constant_identifier_names: false



================================================
FILE: CHANGELOG.md
================================================
## 0.0.1

* Initial release with same API surface of the Android and iOS SDK.

## 0.0.2

* Add support for latest Android and iOS SDK API.

## 1.0.0

* Fd 749 rebranding to web3auth.
* white label data added. 
* feat: fix pubspec according to pub recommendation.
* chore: fix for pub check.
* fix: android deps on mfalevel.

## 1.0.2

* New UI and builds on iOS.
* Update README.md.
* Add id_token to ExtraLoginOptions.

## 1.0.3

* JWT login fixes.

## 1.1.0

* Update app manifest.xml to work with android sdk.
* version bump.
* Web3auth swift sdk update to 5.0.0.
* Bump web3auth android sdk.

## 1.1.1

* Added Web3Auth instance initialization check.

## 1.1.2

* Bump Web3Auth android sdk version.

## 1.2.0

* Bump android versions.

## 1.3.0

* Update version and added community portal link.
* Update README.md.
* bump web3Auth android sdk.
* Bump Web3Auth android sdk version.
* Resolved issues in case of weak/no network.

## 2.0.0

* Bump web3Auth android sdk.
* Feat/android fixes.
* Corekit flag added

## 2.0.1

* Update readme.
* Bump android sdk

## 2.0.2

* Bump web3auth-android-sdk.

## 2.0.3

* Bump android sdk.

## 3.0.0

* Sapphire network and openlogin v5 changes added for android.

## 3.0.1

* Add support for latest Android and iOS SDK API.


## 0.0.2

* Bump android version
* Bug fixes

## 3.1.0

* feat: add sessionTime in mfaSettings.
* Bump web3auth android sdk.
* Update openlogin version.


## 3.1.1

* Update android and ios versions.

## 3.1.2

* Fix typo for appName.
* Fix: typos.

## 3.1.3

* Fix sessionTime issue of always being default.

## 3.1.4

* Update README.
* Fix Android issues.

## 3.1.5

* Update iOS SDK.

## 3.1.6

* Update duration in setResultUrl.

## 3.1.7

* Interface documentation.

## 4.0.0

* Feat/message signing.
* Remove setResultUrl method.
* Update README.
* Add TextField for Email Passwordless in Demo.

## 5.0.0

* Add setCustomTabsClosed Method to handle UserCancellation exception.
* Feat/config api updates.

## 5.0.1

* Code refactored for User cancellation during login.

## 5.0.2

* Align useLogoLoader default value with Android and iOS SDK.

## 5.0.3

* Android sdk updated.

## 5.0.4

* Feat: bump android sdk deps.
* Feat: update library dependencies and update flutter sdk version.

## 6.0.0

* Update code documentation.
* Feat: auth-services v9 changes and wallet-services v3 changes added.

## 6.0.1

* Update auth-service version to v9 and wallet-service to v3.

## 6.1.0

* Update README.
* Swift pnp dependency updated

## 6.1.1

* Update sessionTime documentation.
* Feat: update pnp android sdk deps.

## 6.1.2

* Bump swift sdk and pubspec.yaml.

## 6.2.0

* Add manageMFA functionality.






================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2022 Torus Labs Private Limited

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



================================================
FILE: pubspec.yaml
================================================
name: web3auth_flutter
description: Flutter SDK for Torus Web3Auth (Web3Auth)
version: 6.2.0
homepage: https://web3auth.io
repository: https://github.com/Web3Auth/web3auth-flutter-sdk.git

environment:
  sdk: ">=2.15.1 <4.0.0"
  flutter: ">=2.5.0"

dependencies:
  flutter:
    sdk: flutter

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^4.0.0

# For information on the generic Dart part of this file, see the
# following page: https://dart.dev/tools/pub/pubspec

# The following section is specific to Flutter.
flutter:
  # This section identifies this Flutter project as a plugin project.
  # The 'pluginClass' and Android 'package' identifiers should not ordinarily
  # be modified. They are used by the tooling to maintain consistency when
  # adding or updating assets for this project.
  plugin:
    platforms:
      android:
        package: com.web3auth.flutter.web3auth_flutter
        pluginClass: Web3AuthFlutterPlugin
      ios:
        pluginClass: Web3AuthFlutterPlugin

  # To add assets to your plugin package, add an assets section, like this:
  # assets:
  #   - images/a_dot_burr.jpeg
  #   - images/a_dot_ham.jpeg
  #
  # For details regarding assets in packages, see
  # https://flutter.dev/assets-and-images/#from-packages
  #
  # An image asset can refer to one or more resolution-specific "variants", see
  # https://flutter.dev/assets-and-images/#resolution-aware.

  # To add custom fonts to your plugin package, add a fonts section here,
  # in this "flutter" section. Each entry in this list should have a
  # "family" key with the font family name, and a "fonts" key with a
  # list giving the asset and other descriptors for the font. For
  # example:
  # fonts:
  #   - family: Schyler
  #     fonts:
  #       - asset: fonts/Schyler-Regular.ttf
  #       - asset: fonts/Schyler-Italic.ttf
  #         style: italic
  #   - family: Trajan Pro
  #     fonts:
  #       - asset: fonts/TrajanPro.ttf
  #       - asset: fonts/TrajanPro_Bold.ttf
  #         weight: 700
  #
  # For details regarding fonts in packages, see
  # https://flutter.dev/custom-fonts/#from-packages



================================================
FILE: .metadata
================================================
# This file tracks properties of this Flutter project.
# Used by Flutter tool to assess capabilities and perform upgrades etc.
#
# This file should be version controlled and should not be manually edited.

version:
  revision: 77d935af4db863f6abd0b9c31c7e6df2a13de57b
  channel: stable

project_type: plugin



================================================
FILE: .pubignore
================================================
example/
customauth.iml
test/
.idea/
build/


================================================
FILE: android/consumer_rules.pro
================================================
# Keep Kotlin metadata
-keepclassmembers class ** {
    @kotlin.Metadata *;
}

# Keep public classes and members of your SDK
-keep class com.web3auth.** { *; }

# If using Gson (for JSON parsing)
-keep class com.google.gson.** { *; }
-keepattributes *Annotation*
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}

# Keep method names and constructor params
-keepattributes Signature, InnerClasses, EnclosingMethod, *Annotation*, SourceFile, LineNumberTable

# If you use coroutines or lambdas
-keep class kotlinx.coroutines.** { *; }
-dontwarn kotlinx.coroutines.**

# To avoid stripping methods like getError(), setCustomTabsClosed(), etc.
-keepclassmembers class ** {
    *** getError(...);
    void setCustomTabsClosed(...);
}

# Preserve Kotlin metadata and parameter names
-keepattributes *Annotation*, Signature, InnerClasses, EnclosingMethod
-keep class kotlin.Metadata { *; }
-keepclassmembers class ** {
    @kotlin.Metadata *;
}

# Optional: Keep your SDK class and its methods fully
-keep class com.web3auth.flutter.web3auth_flutter.Web3AuthFlutterPlugin {
    *;
}

-keepclassmembers class com.web3auth.core.Web3Auth {
    public static <methods>;
}

# Preserve the entire Kotlin object class (prevents it from being removed/renamed)
-keep class com.web3auth.core.types.Web3AuthError {
    *;
}



================================================
FILE: android/proguard-rules.pro
================================================
# Keep Kotlin metadata
-keepclassmembers class ** {
    @kotlin.Metadata *;
}

# Keep public classes and members of your SDK
-keep class com.web3auth.** { *; }

# If using Gson (for JSON parsing)
-keep class com.google.gson.** { *; }
-keepattributes *Annotation*
-keepclassmembers class * {
    @com.google.gson.annotations.SerializedName <fields>;
}

# Keep method names and constructor params
-keepattributes Signature, InnerClasses, EnclosingMethod, *Annotation*, SourceFile, LineNumberTable

# If you use coroutines or lambdas
-keep class kotlinx.coroutines.** { *; }
-dontwarn kotlinx.coroutines.**

# To avoid stripping methods like getError(), setCustomTabsClosed(), etc.
-keepclassmembers class ** {
    *** getError(...);
    void setCustomTabsClosed(...);
}

# Preserve Kotlin metadata and parameter names
-keepattributes *Annotation*, Signature, InnerClasses, EnclosingMethod
-keep class kotlin.Metadata { *; }
-keepclassmembers class ** {
    @kotlin.Metadata *;
}

# Optional: Keep your SDK class and its methods fully
-keep class com.web3auth.flutter.web3auth_flutter.Web3AuthFlutterPlugin {
    *;
}

-keepclassmembers class com.web3auth.core.Web3Auth {
    public static <methods>;
}

# Preserve the entire Kotlin object class (prevents it from being removed/renamed)
-keep class com.web3auth.core.types.Web3AuthError {
    *;
}



================================================
FILE: android/gradle/wrapper/gradle-wrapper.properties
================================================
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-7.4-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists



================================================
FILE: android/src/main/AndroidManifest.xml
================================================
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
  package="com.web3auth.flutter.web3auth_flutter">
</manifest>



================================================
FILE: android/src/main/kotlin/com/web3auth/flutter/web3auth_flutter/Web3AuthFlutterPlugin.kt
================================================
package com.web3auth.flutter.web3auth_flutter

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.net.Uri
import android.util.Log
import androidx.annotation.Keep
import androidx.annotation.NonNull
import com.google.gson.Gson
import com.google.gson.JsonArray
import com.google.gson.JsonElement
import com.google.gson.JsonPrimitive
import com.web3auth.core.Web3Auth
import com.web3auth.core.types.ChainConfig
import com.web3auth.core.types.ErrorCode
import com.web3auth.core.types.LoginParams
import com.web3auth.core.types.Web3AuthError
import com.web3auth.core.types.Web3AuthOptions
import com.web3auth.core.types.Web3AuthResponse
import io.flutter.embedding.engine.plugins.FlutterPlugin
import io.flutter.embedding.engine.plugins.activity.ActivityAware
import io.flutter.embedding.engine.plugins.activity.ActivityPluginBinding
import io.flutter.plugin.common.MethodCall
import io.flutter.plugin.common.MethodChannel
import io.flutter.plugin.common.MethodChannel.MethodCallHandler
import io.flutter.plugin.common.PluginRegistry
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import org.json.JSONObject

class Web3AuthFlutterPlugin : FlutterPlugin, ActivityAware, MethodCallHandler,
    PluginRegistry.NewIntentListener {
    private lateinit var channel: MethodChannel

    private var activity: Activity? = null
    private lateinit var context: Context
    private lateinit var web3auth: Web3Auth
    private var gson: Gson = Gson()

    override fun onAttachedToEngine(@NonNull binding: FlutterPlugin.FlutterPluginBinding) {
        channel = MethodChannel(binding.binaryMessenger, "web3auth_flutter")
        channel.setMethodCallHandler(this)
        context = binding.applicationContext
    }

    override fun onDetachedFromEngine(@NonNull binding: FlutterPlugin.FlutterPluginBinding) {
        channel.setMethodCallHandler(null)
    }

    override fun onAttachedToActivity(binding: ActivityPluginBinding) {
        activity = binding.activity
        binding.addOnNewIntentListener(this)
    }

    override fun onDetachedFromActivityForConfigChanges() {
        activity = null
    }

    override fun onReattachedToActivityForConfigChanges(binding: ActivityPluginBinding) {
        activity = binding.activity
    }

    override fun onDetachedFromActivity() {
        activity = null
    }

    override fun onNewIntent(intent: Intent): Boolean {
        if (this::web3auth.isInitialized) {
            web3auth.setResultUrl(intent.data)
        }
        return true
    }

    override fun onMethodCall(@NonNull call: MethodCall, @NonNull result: MethodChannel.Result) {
        CoroutineScope(Dispatchers.Default).launch {
            try {
                val response = runMethodCall(call)
                launch(Dispatchers.Main) { result.success(response) }
            } catch (e: NotImplementedError) {
                launch(Dispatchers.Main) { result.notImplemented() }
            } catch (e: Throwable) {
                launch(Dispatchers.Main) {
                    if(e.message == "User Cancelled") {
                        result.error("UserCancelledException", e.message, e.localizedMessage)
                    } else {
                        result.error("error", e.message, e.localizedMessage)
                    }
                }
            }
        }
    }

    private fun runMethodCall(@NonNull call: MethodCall): Any? {
        when (call.method) {
            "init" -> {
                val initArgs = call.arguments<String>() ?: return null
                val initParams = gson.fromJson(initArgs, Web3AuthOptions::class.java)
                // handle custom parameters which are gson excluded
                val obj = JSONObject(initArgs)
                if (obj.has("redirectUrl")) initParams.redirectUrl = Uri.parse(obj.get("redirectUrl") as String?)
                // Log.d(initParams.toString(), "#initParams")
                web3auth = Web3Auth(
                    initParams, activity!!
                )

                web3auth.setResultUrl(activity?.intent?.data)

                Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#init")
                return null
            }

            "login" -> {
                try {
                    val loginArgs = call.arguments<String>() ?: return null
                    val loginParams = gson.fromJson(loginArgs, LoginParams::class.java)
                    val obj = JSONObject(loginArgs)
                    if (obj.has("redirectUrl")) loginParams.redirectUrl = Uri.parse(obj.get("redirectUrl") as String?)
                    val loginCF = web3auth.login(loginParams)
                    // Log.d(loginParams.toString(), "#loginParams")
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#login")
                    val loginResult: Web3AuthResponse = loginCF.get()
                    return gson.toJson(loginResult)
                } catch (e: NotImplementedError) {
                    throw Error(e)
                } catch (e: Throwable) {
                    throw Error("User Cancelled")
                }
            }

            "logout" -> {
                try {
                    val logoutCF = web3auth.logout()
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#logout")
                    logoutCF.get()
                    return null
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "initialize" -> {
                try {
                    val initializeCF = web3auth.initialize()
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#initialize")
                    initializeCF.get()
                    return null
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "getPrivKey" -> {
                val privKey = web3auth.getPrivkey()
                Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#getPrivKey")
                return privKey
            }

            "getEd25519PrivKey" -> {
                val ed25519Key = web3auth.getEd25519PrivKey()
                Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#getEd25519PrivKey")
                return ed25519Key
            }

            "getUserInfo" -> {
                try {
                    val userInfoResult = web3auth.getUserInfo()
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#getUserInfo")
                    if (userInfoResult == null) {
                        throw Error(Web3AuthError.getError(ErrorCode.NOUSERFOUND))
                    }
                    return gson.toJson(userInfoResult)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "getWeb3AuthResponse" -> {
                try {
                    val web3AuthResult = web3auth.getWeb3AuthResponse()
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#getWeb3AuthResponse")
                    if (web3AuthResult == null) {
                        throw Error(Web3AuthError.getError(ErrorCode.NOUSERFOUND))
                    }
                    return gson.toJson(web3AuthResult)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "launchWalletServices" -> {
                try {
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#launchWalletServices")
                    val wsArgs = call.arguments<String>() ?: return null
                    val wsParams = gson.fromJson(wsArgs, WalletServicesJson::class.java)
                    Log.d(wsParams.toString(), "#wsParams")
                    val launchWalletCF = web3auth.launchWalletServices(
                        wsParams.chainConfig,
                        wsParams.path
                    )
                    launchWalletCF.get()
                    return null
                } catch (e: NotImplementedError) {
                    throw Error(e)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "enableMFA" -> {
                try {
                    val loginArgs = call.arguments<String>() ?: return null
                    val loginParams = gson.fromJson(loginArgs, LoginParams::class.java)
                    val obj = JSONObject(loginArgs)
                    if (obj.has("redirectUrl")) loginParams.redirectUrl =
                        Uri.parse(obj.get("redirectUrl") as String?)
                    val setupMfaCF = web3auth.enableMFA(loginParams)
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#enableMFA")
                    return setupMfaCF.get()
                } catch (e: NotImplementedError) {
                    throw Error(e)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "setCustomTabsClosed" -> {
                try {
                    if (Web3Auth.getCustomTabsClosed()) {
                        web3auth.setResultUrl(null)
                        Web3Auth.setCustomTabsClosed(false)
                    }
                    return null
                } catch (e: NotImplementedError) {
                    throw Error(e)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "request" -> {
                try {
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#signMessage")
                    val requestArgs = call.arguments<String>() ?: return null
                    val reqParams = gson.fromJson(requestArgs, RequestJson::class.java)
                    Log.d(reqParams.toString(), "#reqParams")
                    val requestCF = web3auth.request(
                        reqParams.chainConfig,
                        reqParams.method,
                        convertListToJsonArray(reqParams.requestParams) ,
                        reqParams.path,
                        reqParams.appState
                    )
                    return gson.toJson(requestCF.get())
                } catch (e: NotImplementedError) {
                    throw Error(e)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }

            "manageMFA" -> {
                try {
                    val loginArgs = call.arguments<String>() ?: return null
                    val loginParams = gson.fromJson(loginArgs, LoginParams::class.java)
                    val obj = JSONObject(loginArgs)
                    if (obj.has("redirectUrl")) loginParams.redirectUrl =
                        Uri.parse(obj.get("redirectUrl") as String?)
                    val setupMfaCF = web3auth.manageMFA(loginParams)
                    Log.d("${Web3AuthFlutterPlugin::class.qualifiedName}", "#enableMFA")
                    return setupMfaCF.get()
                } catch (e: NotImplementedError) {
                    throw Error(e)
                } catch (e: Throwable) {
                    throw Error(e)
                }
            }
        }
        throw NotImplementedError()
    }

    private fun convertListToJsonArray(list: List<Any?>): JsonArray {
        val jsonArray = JsonArray()
        val gson = Gson()

        list.forEach { item ->
            val jsonElement: JsonElement = when (item) {
                is Number -> JsonPrimitive(item)
                is String -> JsonPrimitive(item)
                is Boolean -> JsonPrimitive(item)
                is Map<*, *> -> gson.toJsonTree(item)
                is List<*> -> convertListToJsonArray(item)
                null -> JsonPrimitive("")
                else -> throw IllegalArgumentException("Unsupported type: ${item::class.java}")
            }
            jsonArray.add(jsonElement)
        }
        return jsonArray
    }
}
@Keep
data class WalletServicesJson(
    @Keep val chainConfig: ChainConfig,
    @Keep val path: String? = "wallet"
)

@Keep
data class RequestJson(
    @Keep val chainConfig: ChainConfig,
    @Keep val method: String,
    @Keep val requestParams: List<Any?>,
    @Keep val path: String? = "wallet/request",
    @Keep val appState: String? = null
)



================================================
FILE: example/README.md
================================================
# web3auth_flutter_example

Demonstrates how to use the web3auth_flutter plugin.

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://flutter.dev/docs/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://flutter.dev/docs/cookbook)

For help getting started with Flutter, view our
[online documentation](https://flutter.dev/docs), which offers tutorials,
samples, guidance on mobile development, and a full API reference.



================================================
FILE: example/analysis_options.yaml
================================================
# This file configures the analyzer, which statically analyzes Dart code to
# check for errors, warnings, and lints.
#
# The issues identified by the analyzer are surfaced in the UI of Dart-enabled
# IDEs (https://dart.dev/tools#ides-and-editors). The analyzer can also be
# invoked from the command line by running `flutter analyze`.

# The following line activates a set of recommended lints for Flutter apps,
# packages, and plugins designed to encourage good coding practices.
include: package:flutter_lints/flutter.yaml

linter:
  # The lint rules applied to this project can be customized in the
  # section below to disable rules from the `package:flutter_lints/flutter.yaml`
  # included above or to enable additional rules. A list of all available lints
  # and their documentation is published at
  # https://dart-lang.github.io/linter/lints/index.html.
  #
  # Instead of disabling a lint rule for the entire project in the
  # section below, it can also be suppressed for a single line of code
  # or a specific dart file by using the `// ignore: name_of_lint` and
  # `// ignore_for_file: name_of_lint` syntax on the line or in the file
  # producing the lint.
  rules:
    # avoid_print: false  # Uncomment to disable the `avoid_print` rule
    # prefer_single_quotes: true  # Uncomment to enable the `prefer_single_quotes` rule

# Additional information about this file can be found at
# https://dart.dev/guides/language/analysis-options



================================================
FILE: example/pubspec.lock
================================================
# Generated by pub
# See https://dart.dev/tools/pub/glossary#lockfile
packages:
  async:
    dependency: transitive
    description:
      name: async
      sha256: "947bfcf187f74dbc5e146c9eb9c0f10c9f8b30743e341481c1e2ed3ecc18c20c"
      url: "https://pub.dev"
    source: hosted
    version: "2.11.0"
  boolean_selector:
    dependency: transitive
    description:
      name: boolean_selector
      sha256: "6cfb5af12253eaf2b368f07bacc5a80d1301a071c73360d746b7f2e32d762c66"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.1"
  characters:
    dependency: transitive
    description:
      name: characters
      sha256: "04a925763edad70e8443c99234dc3328f442e811f1d8fd1a72f1c8ad0f69a605"
      url: "https://pub.dev"
    source: hosted
    version: "1.3.0"
  clock:
    dependency: transitive
    description:
      name: clock
      sha256: cb6d7f03e1de671e34607e909a7213e31d7752be4fb66a86d29fe1eb14bfb5cf
      url: "https://pub.dev"
    source: hosted
    version: "1.1.1"
  collection:
    dependency: transitive
    description:
      name: collection
      sha256: ee67cb0715911d28db6bf4af1026078bd6f0128b07a5f66fb2ed94ec6783c09a
      url: "https://pub.dev"
    source: hosted
    version: "1.18.0"
  convert:
    dependency: transitive
    description:
      name: convert
      sha256: "0f08b14755d163f6e2134cb58222dd25ea2a2ee8a195e53983d57c075324d592"
      url: "https://pub.dev"
    source: hosted
    version: "3.1.1"
  crypto:
    dependency: transitive
    description:
      name: crypto
      sha256: ff625774173754681d66daaf4a448684fb04b78f902da9cb3d308c19cc5e8bab
      url: "https://pub.dev"
    source: hosted
    version: "3.0.3"
  cupertino_icons:
    dependency: "direct main"
    description:
      name: cupertino_icons
      sha256: ba631d1c7f7bef6b729a622b7b752645a2d076dba9976925b8f25725a30e1ee6
      url: "https://pub.dev"
    source: hosted
    version: "1.0.8"
  eip1559:
    dependency: transitive
    description:
      name: eip1559
      sha256: c2b81ac85f3e0e71aaf558201dd9a4600f051ece7ebacd0c5d70065c9b458004
      url: "https://pub.dev"
    source: hosted
    version: "0.6.2"
  eip55:
    dependency: transitive
    description:
      name: eip55
      sha256: "213a9b86add87a5216328e8494b0ab836e401210c4d55eb5e521bd39e39169e1"
      url: "https://pub.dev"
    source: hosted
    version: "1.0.2"
  fake_async:
    dependency: transitive
    description:
      name: fake_async
      sha256: "511392330127add0b769b75a987850d136345d9227c6b94c96a04cf4a391bf78"
      url: "https://pub.dev"
    source: hosted
    version: "1.3.1"
  fixnum:
    dependency: transitive
    description:
      name: fixnum
      sha256: "25517a4deb0c03aa0f32fd12db525856438902d9c16536311e76cdc57b31d7d1"
      url: "https://pub.dev"
    source: hosted
    version: "1.1.0"
  flutter:
    dependency: "direct main"
    description: flutter
    source: sdk
    version: "0.0.0"
  flutter_lints:
    dependency: "direct dev"
    description:
      name: flutter_lints
      sha256: e2a421b7e59244faef694ba7b30562e489c2b489866e505074eb005cd7060db7
      url: "https://pub.dev"
    source: hosted
    version: "3.0.1"
  flutter_test:
    dependency: "direct dev"
    description: flutter
    source: sdk
    version: "0.0.0"
  http:
    dependency: transitive
    description:
      name: http
      sha256: a2bbf9d017fcced29139daa8ed2bba4ece450ab222871df93ca9eec6f80c34ba
      url: "https://pub.dev"
    source: hosted
    version: "1.2.0"
  http_parser:
    dependency: transitive
    description:
      name: http_parser
      sha256: "2aa08ce0341cc9b354a498388e30986515406668dbcc4f7c950c3e715496693b"
      url: "https://pub.dev"
    source: hosted
    version: "4.0.2"
  js:
    dependency: transitive
    description:
      name: js
      sha256: c1b2e9b5ea78c45e1a0788d29606ba27dc5f71f019f32ca5140f61ef071838cf
      url: "https://pub.dev"
    source: hosted
    version: "0.7.1"
  json_rpc_2:
    dependency: transitive
    description:
      name: json_rpc_2
      sha256: "5e469bffa23899edacb7b22787780068d650b106a21c76db3c49218ab7ca447e"
      url: "https://pub.dev"
    source: hosted
    version: "3.0.2"
  leak_tracker:
    dependency: transitive
    description:
      name: leak_tracker
      sha256: "3f87a60e8c63aecc975dda1ceedbc8f24de75f09e4856ea27daf8958f2f0ce05"
      url: "https://pub.dev"
    source: hosted
    version: "10.0.5"
  leak_tracker_flutter_testing:
    dependency: transitive
    description:
      name: leak_tracker_flutter_testing
      sha256: "932549fb305594d82d7183ecd9fa93463e9914e1b67cacc34bc40906594a1806"
      url: "https://pub.dev"
    source: hosted
    version: "3.0.5"
  leak_tracker_testing:
    dependency: transitive
    description:
      name: leak_tracker_testing
      sha256: "6ba465d5d76e67ddf503e1161d1f4a6bc42306f9d66ca1e8f079a47290fb06d3"
      url: "https://pub.dev"
    source: hosted
    version: "3.0.1"
  lints:
    dependency: transitive
    description:
      name: lints
      sha256: cbf8d4b858bb0134ef3ef87841abdf8d63bfc255c266b7bf6b39daa1085c4290
      url: "https://pub.dev"
    source: hosted
    version: "3.0.0"
  matcher:
    dependency: transitive
    description:
      name: matcher
      sha256: d2323aa2060500f906aa31a895b4030b6da3ebdcc5619d14ce1aada65cd161cb
      url: "https://pub.dev"
    source: hosted
    version: "0.12.16+1"
  material_color_utilities:
    dependency: transitive
    description:
      name: material_color_utilities
      sha256: f7142bb1154231d7ea5f96bc7bde4bda2a0945d2806bb11670e30b850d56bdec
      url: "https://pub.dev"
    source: hosted
    version: "0.11.1"
  meta:
    dependency: transitive
    description:
      name: meta
      sha256: bdb68674043280c3428e9ec998512fb681678676b3c54e773629ffe74419f8c7
      url: "https://pub.dev"
    source: hosted
    version: "1.15.0"
  path:
    dependency: transitive
    description:
      name: path
      sha256: "087ce49c3f0dc39180befefc60fdb4acd8f8620e5682fe2476afd0b3688bb4af"
      url: "https://pub.dev"
    source: hosted
    version: "1.9.0"
  pointycastle:
    dependency: transitive
    description:
      name: pointycastle
      sha256: "79fbafed02cfdbe85ef3fd06c7f4bc2cbcba0177e61b765264853d4253b21744"
      url: "https://pub.dev"
    source: hosted
    version: "3.9.0"
  sec:
    dependency: transitive
    description:
      name: sec
      sha256: "8bbd56df884502192a441b5f5d667265498f2f8728a282beccd9db79e215f379"
      url: "https://pub.dev"
    source: hosted
    version: "1.1.0"
  sky_engine:
    dependency: transitive
    description: flutter
    source: sdk
    version: "0.0.99"
  source_span:
    dependency: transitive
    description:
      name: source_span
      sha256: "53e943d4206a5e30df338fd4c6e7a077e02254531b138a15aec3bd143c1a8b3c"
      url: "https://pub.dev"
    source: hosted
    version: "1.10.0"
  sprintf:
    dependency: transitive
    description:
      name: sprintf
      sha256: "1fc9ffe69d4df602376b52949af107d8f5703b77cda567c4d7d86a0693120f23"
      url: "https://pub.dev"
    source: hosted
    version: "7.0.0"
  stack_trace:
    dependency: transitive
    description:
      name: stack_trace
      sha256: "73713990125a6d93122541237550ee3352a2d84baad52d375a4cad2eb9b7ce0b"
      url: "https://pub.dev"
    source: hosted
    version: "1.11.1"
  stream_channel:
    dependency: transitive
    description:
      name: stream_channel
      sha256: ba2aa5d8cc609d96bbb2899c28934f9e1af5cddbd60a827822ea467161eb54e7
      url: "https://pub.dev"
    source: hosted
    version: "2.1.2"
  stream_transform:
    dependency: transitive
    description:
      name: stream_transform
      sha256: "14a00e794c7c11aa145a170587321aedce29769c08d7f58b1d141da75e3b1c6f"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.0"
  string_scanner:
    dependency: transitive
    description:
      name: string_scanner
      sha256: "556692adab6cfa87322a115640c11f13cb77b3f076ddcc5d6ae3c20242bedcde"
      url: "https://pub.dev"
    source: hosted
    version: "1.2.0"
  term_glyph:
    dependency: transitive
    description:
      name: term_glyph
      sha256: a29248a84fbb7c79282b40b8c72a1209db169a2e0542bce341da992fe1bc7e84
      url: "https://pub.dev"
    source: hosted
    version: "1.2.1"
  test_api:
    dependency: transitive
    description:
      name: test_api
      sha256: "5b8a98dafc4d5c4c9c72d8b31ab2b23fc13422348d2997120294d3bac86b4ddb"
      url: "https://pub.dev"
    source: hosted
    version: "0.7.2"
  typed_data:
    dependency: transitive
    description:
      name: typed_data
      sha256: facc8d6582f16042dd49f2463ff1bd6e2c9ef9f3d5da3d9b087e244a7b564b3c
      url: "https://pub.dev"
    source: hosted
    version: "1.3.2"
  uuid:
    dependency: transitive
    description:
      name: uuid
      sha256: cd210a09f7c18cbe5a02511718e0334de6559871052c90a90c0cca46a4aa81c8
      url: "https://pub.dev"
    source: hosted
    version: "4.3.3"
  vector_math:
    dependency: transitive
    description:
      name: vector_math
      sha256: "80b3257d1492ce4d091729e3a67a60407d227c27241d6927be0130c98e741803"
      url: "https://pub.dev"
    source: hosted
    version: "2.1.4"
  vm_service:
    dependency: transitive
    description:
      name: vm_service
      sha256: "5c5f338a667b4c644744b661f309fb8080bb94b18a7e91ef1dbd343bed00ed6d"
      url: "https://pub.dev"
    source: hosted
    version: "14.2.5"
  wallet:
    dependency: transitive
    description:
      name: wallet
      sha256: "687fd89a16557649b26189e597792962f405797fc64113e8758eabc2c2605c32"
      url: "https://pub.dev"
    source: hosted
    version: "0.0.13"
  web:
    dependency: transitive
    description:
      name: web
      sha256: afe077240a270dcfd2aafe77602b4113645af95d0ad31128cc02bce5ac5d5152
      url: "https://pub.dev"
    source: hosted
    version: "0.3.0"
  web3auth_flutter:
    dependency: "direct main"
    description:
      path: ".."
      relative: true
    source: path
    version: "6.1.0"
  web3dart:
    dependency: "direct main"
    description:
      name: web3dart
      sha256: "885e5e8f0cc3c87c09f160a7fce6279226ca41316806f7ece2001959c62ecced"
      url: "https://pub.dev"
    source: hosted
    version: "2.7.3"
sdks:
  dart: ">=3.3.0 <4.0.0"
  flutter: ">=3.18.0-18.0.pre.54"



================================================
FILE: example/pubspec.yaml
================================================
name: web3auth_flutter_example
description: Demonstrates how to use the web3auth_flutter plugin.

# The following line prevents the package from being accidentally published to
# pub.dev using `flutter pub publish`. This is preferred for private packages.
publish_to: "none" # Remove this line if you wish to publish to pub.dev

environment:
  sdk: ">=2.15.1"

# Dependencies specify other packages that your package needs in order to work.
# To automatically upgrade your package dependencies to the latest versions
# consider running `flutter pub upgrade --major-versions`. Alternatively,
# dependencies can be manually updated by changing the version numbers below to
# the latest version available on pub.dev. To see which dependencies have newer
# versions available, run `flutter pub outdated`.
dependencies:
  flutter:
    sdk: flutter

  web3auth_flutter:
    # When depending on this package from a real application you should use:
    #   web3auth_flutter: ^x.y.z
    # See https://dart.dev/tools/pub/dependencies#version-constraints
    # The example app is bundled with the plugin so we use a path dependency on
    # the parent directory to use the current plugin's version.
    path: ../

  # The following adds the Cupertino Icons font to your application.
  # Use with the CupertinoIcons class for iOS style icons.
  cupertino_icons: ^1.0.8
  web3dart: ^2.7.3

dev_dependencies:
  flutter_test:
    sdk: flutter

  # The "flutter_lints" package below contains a set of recommended lints to
  # encourage good coding practices. The lint set provided by the package is
  # activated in the `analysis_options.yaml` file located at the root of your
  # package. See that file for information about deactivating specific lint
  # rules and activating additional ones.
  flutter_lints: ^3.0.0

# For information on the generic Dart part of this file, see the
# following page: https://dart.dev/tools/pub/pubspec

# The following section is specific to Flutter.
flutter:
  # The following line ensures that the Material Icons font is
  # included with your application, so that you can use the icons in
  # the material Icons class.
  uses-material-design: true

  # To add assets to your application, add an assets section, like this:
  # assets:
  #   - images/a_dot_burr.jpeg
  #   - images/a_dot_ham.jpeg

  # An image asset can refer to one or more resolution-specific "variants", see
  # https://flutter.dev/assets-and-images/#resolution-aware.

  # For details regarding adding assets from package dependencies, see
  # https://flutter.dev/assets-and-images/#from-packages

  # To add custom fonts to your application, add a fonts section here,
  # in this "flutter" section. Each entry in this list should have a
  # "family" key with the font family name, and a "fonts" key with a
  # list giving the asset and other descriptors for the font. For
  # example:
  # fonts:
  #   - family: Schyler
  #     fonts:
  #       - asset: fonts/Schyler-Regular.ttf
  #       - asset: fonts/Schyler-Italic.ttf
  #         style: italic
  #   - family: Trajan Pro
  #     fonts:
  #       - asset: fonts/TrajanPro.ttf
  #       - asset: fonts/TrajanPro_Bold.ttf
  #         weight: 700
  #
  # For details regarding fonts from package dependencies,
  # see https://flutter.dev/custom-fonts/#from-packages



================================================
FILE: example/.metadata
================================================
# This file tracks properties of this Flutter project.
# Used by Flutter tool to assess capabilities and perform upgrades etc.
#
# This file should be version controlled and should not be manually edited.

version:
  revision: "2663184aa79047d0a33a14a3b607954f8fdd8730"
  channel: "stable"

project_type: app

# Tracks metadata for the flutter migrate command
migration:
  platforms:
    - platform: root
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
    - platform: android
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
    - platform: ios
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
    - platform: linux
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
    - platform: macos
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
    - platform: web
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
    - platform: windows
      create_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730
      base_revision: 2663184aa79047d0a33a14a3b607954f8fdd8730

  # User provided section

  # List of Local paths (relative to this file) that should be
  # ignored by the migrate tool.
  #
  # Files that are not part of the templates will be ignored by default.
  unmanaged_files:
    - 'lib/main.dart'
    - 'ios/Runner.xcodeproj/project.pbxproj'



================================================
FILE: example/android/gradle.properties
================================================
## For more details on how to configure your build environment visit
# http://www.gradle.org/docs/current/userguide/build_environment.html
#
# Specifies the JVM arguments used for the daemon process.
# The setting is particularly useful for tweaking memory settings.
# Default value: -Xmx1024m -XX:MaxPermSize=256m
# org.gradle.jvmargs=-Xmx2048m -XX:MaxPermSize=512m -XX:+HeapDumpOnOutOfMemoryError -Dfile.encoding=UTF-8
#
# When configured, Gradle will run in incubating parallel mode.
# This option should only be used with decoupled projects. More details, visit
# http://www.gradle.org/docs/current/userguide/multi_project_builds.html#sec:decoupled_projects
# org.gradle.parallel=true
#Thu Feb 03 10:03:40 HKT 2022
org.gradle.jvmargs=-Xmx2048M -Dkotlin.daemon.jvm.options\="-Xmx2048M"
android.useAndroidX=true
android.enableJetifier=true



================================================
FILE: example/android/app/src/debug/AndroidManifest.xml
================================================
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.web3auth.flutter.web3auth_flutter_example">
    <!-- Flutter needs it to communicate with the running application
         to allow setting breakpoints, to provide hot reload, etc.
    -->
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest>



================================================
FILE: example/android/app/src/main/AndroidManifest.xml
================================================
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.web3auth.flutter.web3auth_flutter_example">
   <application
        android:label="web3auth_flutter_example"
        android:name="${applicationName}"
        tools:replace="android:name"
        android:icon="@mipmap/ic_launcher">
        <activity
            android:name="com.openlogin.flutter.openlogin_flutter_example.MainActivity"
            android:exported="true"
            android:launchMode="singleTop"
            android:theme="@style/LaunchTheme"
            android:configChanges="orientation|keyboardHidden|keyboard|screenSize|smallestScreenSize|locale|layoutDirection|fontScale|screenLayout|density|uiMode"
            android:hardwareAccelerated="true"
            android:windowSoftInputMode="adjustResize">
            <!-- Specifies an Android theme to apply to this Activity as soon as
                 the Android process has started. This theme is visible to the user
                 while the Flutter UI initializes. After that, this theme continues
                 to determine the Window background behind the Flutter UI. -->
            <meta-data
              android:name="io.flutter.embedding.android.NormalTheme"
              android:resource="@style/NormalTheme"
              />
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />

                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />

                <!-- Accept URIs: {YOUR_APP_PACKAGE_NAME}://* -->
                <data
                    android:scheme="torusapp"
                    android:host="org.torusresearch.flutter.web3authexample" />
            </intent-filter>
        </activity>
        <!-- Don't delete the meta-data below.
             This is used by the Flutter tool to generate GeneratedPluginRegistrant.java -->
        <meta-data
            android:name="flutterEmbedding"
            android:value="2" />
    </application>
</manifest>



================================================
FILE: example/android/app/src/main/kotlin/com/openlogin/flutter/openlogin_flutter_example/MainActivity.kt
================================================
package com.openlogin.flutter.openlogin_flutter_example

import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity() {
}



================================================
FILE: example/android/app/src/main/res/drawable/launch_background.xml
================================================
<?xml version="1.0" encoding="utf-8"?>
<!-- Modify this file to customize your launch splash screen -->
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@android:color/white" />

    <!-- You can insert your own image assets here -->
    <!-- <item>
        <bitmap
            android:gravity="center"
            android:src="@mipmap/launch_image" />
    </item> -->
</layer-list>



================================================
FILE: example/android/app/src/main/res/drawable-v21/launch_background.xml
================================================
<?xml version="1.0" encoding="utf-8"?>
<!-- Modify this file to customize your launch splash screen -->
<layer-list xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="?android:colorBackground" />

    <!-- You can insert your own image assets here -->
    <!-- <item>
        <bitmap
            android:gravity="center"
            android:src="@mipmap/launch_image" />
    </item> -->
</layer-list>



================================================
FILE: example/android/app/src/main/res/values/styles.xml
================================================
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Theme applied to the Android Window while the process is starting when the OS's Dark Mode setting is off -->
    <style name="LaunchTheme" parent="@android:style/Theme.Light.NoTitleBar">
        <!-- Show a splash screen on the activity. Automatically removed when
             Flutter draws its first frame -->
        <item name="android:windowBackground">@drawable/launch_background</item>
    </style>
    <!-- Theme applied to the Android Window as soon as the process has started.
         This theme determines the color of the Android Window while your
         Flutter UI initializes, as well as behind your Flutter UI while its
         running.

         This Theme is only used starting with V2 of Flutter's Android embedding. -->
    <style name="NormalTheme" parent="@android:style/Theme.Light.NoTitleBar">
        <item name="android:windowBackground">?android:colorBackground</item>
    </style>
</resources>



================================================
FILE: example/android/app/src/main/res/values-night/styles.xml
================================================
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Theme applied to the Android Window while the process is starting when the OS's Dark Mode setting is on -->
    <style name="LaunchTheme" parent="@android:style/Theme.Black.NoTitleBar">
        <!-- Show a splash screen on the activity. Automatically removed when
             Flutter draws its first frame -->
        <item name="android:windowBackground">@drawable/launch_background</item>
    </style>
    <!-- Theme applied to the Android Window as soon as the process has started.
         This theme determines the color of the Android Window while your
         Flutter UI initializes, as well as behind your Flutter UI while its
         running.

         This Theme is only used starting with V2 of Flutter's Android embedding. -->
    <style name="NormalTheme" parent="@android:style/Theme.Black.NoTitleBar">
        <item name="android:windowBackground">?android:colorBackground</item>
    </style>
</resources>



================================================
FILE: example/android/app/src/profile/AndroidManifest.xml
================================================
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.web3auth.flutter.web3auth_flutter_example">
    <!-- Flutter needs it to communicate with the running application
         to allow setting breakpoints, to provide hot reload, etc.
    -->
    <uses-permission android:name="android.permission.INTERNET"/>
</manifest>



================================================
FILE: example/android/gradle/wrapper/gradle-wrapper.properties
================================================
#Fri Jun 23 08:50:38 CEST 2017
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-7.4-all.zip



================================================
FILE: example/ios/Podfile
================================================
# Uncomment this line to define a global platform for your project
platform :ios, '14.0'

source 'https://github.com/CocoaPods/Specs.git'

# CocoaPods analytics sends network stats synchronously affecting flutter build latency.
ENV['COCOAPODS_DISABLE_STATS'] = 'true'

project 'Runner', {
  'Debug' => :debug,
  'Profile' => :release,
  'Release' => :release,
}

def flutter_root
  generated_xcode_build_settings_path = File.expand_path(File.join('..', 'Flutter', 'Generated.xcconfig'), __FILE__)
  unless File.exist?(generated_xcode_build_settings_path)
    raise "#{generated_xcode_build_settings_path} must exist. If you're running pod install manually, make sure flutter pub get is executed first"
  end

  File.foreach(generated_xcode_build_settings_path) do |line|
    matches = line.match(/FLUTTER_ROOT\=(.*)/)
    return matches[1].strip if matches
  end
  raise "FLUTTER_ROOT not found in #{generated_xcode_build_settings_path}. Try deleting Generated.xcconfig, then run flutter pub get"
end

require File.expand_path(File.join('packages', 'flutter_tools', 'bin', 'podhelper'), flutter_root)

flutter_ios_podfile_setup

target 'Runner' do
  use_frameworks!
  use_modular_headers!

  flutter_install_all_ios_pods File.dirname(File.realpath(__FILE__))
end

post_install do |installer|
  installer.pods_project.targets.each do |target|
    flutter_additional_ios_build_settings(target)
  end
end



================================================
FILE: example/ios/Podfile.lock
================================================
PODS:
  - BigInt (5.2.0)
  - curvelib.swift (2.0.0)
  - Flutter (1.0.0)
  - KeychainSwift (20.0.0)
  - TorusSessionManager (6.0.2):
    - curvelib.swift (~> 2.0.0)
    - KeychainSwift (~> 20.0.0)
  - Web3Auth (11.0.5):
    - BigInt (~> 5.2.0)
    - curvelib.swift (~> 2.0.0)
    - KeychainSwift (~> 20.0.0)
    - TorusSessionManager (~> 6.0.2)
  - web3auth_flutter (2.0.1):
    - Flutter
    - Web3Auth (~> 11.0.5)

DEPENDENCIES:
  - Flutter (from `Flutter`)
  - web3auth_flutter (from `.symlinks/plugins/web3auth_flutter/ios`)

SPEC REPOS:
  https://github.com/CocoaPods/Specs.git:
    - BigInt
    - curvelib.swift
    - KeychainSwift
    - TorusSessionManager
    - Web3Auth

EXTERNAL SOURCES:
  Flutter:
    :path: Flutter
  web3auth_flutter:
    :path: ".symlinks/plugins/web3auth_flutter/ios"

SPEC CHECKSUMS:
  BigInt: f668a80089607f521586bbe29513d708491ef2f7
  curvelib.swift: b9223e5cac801effed8a5fe8968e952b3fe427a5
  Flutter: e0871f40cf51350855a761d2e70bf5af5b9b5de7
  KeychainSwift: 0ce6a4d13f7228054d1a71bb1b500448fb2ab837
  TorusSessionManager: 3c47c2a4c4d6173a10006eb0af4b86317ee45ff8
  Web3Auth: cf501e2bccf63d7a9746c0e53eb98cf143841a5c
  web3auth_flutter: 79be94bbb719a1837c79e0c07e793abd64e11dd7

PODFILE CHECKSUM: 1d58595b82b880200a7ded05da9181d30ef8c1b7

COCOAPODS: 1.14.2



================================================
FILE: example/ios/Flutter/AppFrameworkInfo.plist
================================================
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>CFBundleDevelopmentRegion</key>
  <string>en</string>
  <key>CFBundleExecutable</key>
  <string>App</string>
  <key>CFBundleIdentifier</key>
  <string>io.flutter.flutter.app</string>
  <key>CFBundleInfoDictionaryVersion</key>
  <string>6.0</string>
  <key>CFBundleName</key>
  <string>App</string>
  <key>CFBundlePackageType</key>
  <string>FMWK</string>
  <key>CFBundleShortVersionString</key>
  <string>1.0</string>
  <key>CFBundleSignature</key>
  <string>????</string>
  <key>CFBundleVersion</key>
  <string>1.0</string>
  <key>MinimumOSVersion</key>
  <string>12.0</string>
</dict>
</plist>



================================================
FILE: example/ios/Flutter/Debug.xcconfig
================================================
#include? "Pods/Target Support Files/Pods-Runner/Pods-Runner.debug.xcconfig"
#include "Generated.xcconfig"



================================================
FILE: example/ios/Flutter/Release.xcconfig
================================================
#include? "Pods/Target Support Files/Pods-Runner/Pods-Runner.release.xcconfig"
#include "Generated.xcconfig"



================================================
FILE: example/ios/Runner/AppDelegate.swift
================================================
import Flutter
import UIKit

@main
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}



================================================
FILE: example/ios/Runner/Info.plist
================================================
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CADisableMinimumFrameDurationOnPhone</key>
	<true/>
	<key>CFBundleDevelopmentRegion</key>
	<string>$(DEVELOPMENT_LANGUAGE)</string>
	<key>CFBundleDisplayName</key>
	<string>Web3Auth Flutter</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIdentifier</key>
	<string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>web3auth_flutter_example</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>$(FLUTTER_BUILD_NAME)</string>
	<key>CFBundleSignature</key>
	<string>????</string>
	<key>CFBundleURLTypes</key>
	<array>
		<dict>
			<key>CFBundleTypeRole</key>
			<string>Editor</string>
			<key>CFBundleURLName</key>
			<string>org.torusresearch.flutter.web3authexample</string>
			<key>CFBundleURLSchemes</key>
			<array>
				<string>torusapp</string>
			</array>
		</dict>
	</array>
	<key>CFBundleVersion</key>
	<string>$(FLUTTER_BUILD_NUMBER)</string>
	<key>FlutterDeepLinkingEnabled</key>
	<true/>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>UIApplicationSupportsIndirectInputEvents</key>
	<true/>
	<key>UILaunchStoryboardName</key>
	<string>LaunchScreen</string>
	<key>UIMainStoryboardFile</key>
	<string>Main</string>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>UISupportedInterfaceOrientations~ipad</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationPortraitUpsideDown</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
	<key>UIViewControllerBasedStatusBarAppearance</key>
	<true/>
</dict>
</plist>



================================================
FILE: example/ios/Runner/Runner-Bridging-Header.h
================================================
#import "GeneratedPluginRegistrant.h"



================================================
FILE: example/ios/Runner/Assets.xcassets/AppIcon.appiconset/Contents.json
================================================
{
  "images" : [
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "Icon-App-20x20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "20x20",
      "idiom" : "iphone",
      "filename" : "Icon-App-20x20@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "iphone",
      "filename" : "Icon-App-29x29@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "Icon-App-40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "iphone",
      "filename" : "Icon-App-40x40@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "Icon-App-60x60@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "60x60",
      "idiom" : "iphone",
      "filename" : "Icon-App-60x60@3x.png",
      "scale" : "3x"
    },
    {
      "size" : "20x20",
      "idiom" : "ipad",
      "filename" : "Icon-App-20x20@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "20x20",
      "idiom" : "ipad",
      "filename" : "Icon-App-20x20@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "Icon-App-29x29@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "29x29",
      "idiom" : "ipad",
      "filename" : "Icon-App-29x29@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "Icon-App-40x40@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "40x40",
      "idiom" : "ipad",
      "filename" : "Icon-App-40x40@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "Icon-App-76x76@1x.png",
      "scale" : "1x"
    },
    {
      "size" : "76x76",
      "idiom" : "ipad",
      "filename" : "Icon-App-76x76@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "83.5x83.5",
      "idiom" : "ipad",
      "filename" : "Icon-App-83.5x83.5@2x.png",
      "scale" : "2x"
    },
    {
      "size" : "1024x1024",
      "idiom" : "ios-marketing",
      "filename" : "Icon-App-1024x1024@1x.png",
      "scale" : "1x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}



================================================
FILE: example/ios/Runner/Assets.xcassets/LaunchImage.imageset/README.md
================================================
# Launch Screen Assets

You can customize the launch screen with your own desired assets by replacing the image files in this directory.

You can also do it by opening your Flutter project's Xcode project with `open ios/Runner.xcworkspace`, selecting `Runner/Assets.xcassets` in the Project Navigator and dropping in the desired images.


================================================
FILE: example/ios/Runner/Assets.xcassets/LaunchImage.imageset/Contents.json
================================================
{
  "images" : [
    {
      "idiom" : "universal",
      "filename" : "LaunchImage.png",
      "scale" : "1x"
    },
    {
      "idiom" : "universal",
      "filename" : "LaunchImage@2x.png",
      "scale" : "2x"
    },
    {
      "idiom" : "universal",
      "filename" : "LaunchImage@3x.png",
      "scale" : "3x"
    }
  ],
  "info" : {
    "version" : 1,
    "author" : "xcode"
  }
}



================================================
FILE: example/ios/Runner/Base.lproj/LaunchScreen.storyboard
================================================
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="12121" systemVersion="16G29" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" launchScreen="YES" colorMatched="YES" initialViewController="01J-lp-oVM">
    <dependencies>
        <deployment identifier="iOS"/>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="12089"/>
    </dependencies>
    <scenes>
        <!--View Controller-->
        <scene sceneID="EHf-IW-A2E">
            <objects>
                <viewController id="01J-lp-oVM" sceneMemberID="viewController">
                    <layoutGuides>
                        <viewControllerLayoutGuide type="top" id="Ydg-fD-yQy"/>
                        <viewControllerLayoutGuide type="bottom" id="xbc-2k-c8Z"/>
                    </layoutGuides>
                    <view key="view" contentMode="scaleToFill" id="Ze5-6b-2t3">
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <subviews>
                            <imageView opaque="NO" clipsSubviews="YES" multipleTouchEnabled="YES" contentMode="center" image="LaunchImage" translatesAutoresizingMaskIntoConstraints="NO" id="YRO-k0-Ey4">
                            </imageView>
                        </subviews>
                        <color key="backgroundColor" red="1" green="1" blue="1" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
                        <constraints>
                            <constraint firstItem="YRO-k0-Ey4" firstAttribute="centerX" secondItem="Ze5-6b-2t3" secondAttribute="centerX" id="1a2-6s-vTC"/>
                            <constraint firstItem="YRO-k0-Ey4" firstAttribute="centerY" secondItem="Ze5-6b-2t3" secondAttribute="centerY" id="4X2-HB-R7a"/>
                        </constraints>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="iYj-Kq-Ea1" userLabel="First Responder" sceneMemberID="firstResponder"/>
            </objects>
            <point key="canvasLocation" x="53" y="375"/>
        </scene>
    </scenes>
    <resources>
        <image name="LaunchImage" width="168" height="185"/>
    </resources>
</document>



================================================
FILE: example/ios/Runner/Base.lproj/Main.storyboard
================================================
<?xml version="1.0" encoding="UTF-8"?>
<document type="com.apple.InterfaceBuilder3.CocoaTouch.Storyboard.XIB" version="3.0" toolsVersion="20037" targetRuntime="iOS.CocoaTouch" propertyAccessControl="none" useAutolayout="YES" useTraitCollections="YES" colorMatched="YES" initialViewController="BYZ-38-t0r">
    <device id="retina6_1" orientation="portrait" appearance="light"/>
    <dependencies>
        <deployment identifier="iOS"/>
        <plugIn identifier="com.apple.InterfaceBuilder.IBCocoaTouchPlugin" version="20020"/>
        <capability name="documents saved in the Xcode 8 format" minToolsVersion="8.0"/>
    </dependencies>
    <scenes>
        <!--Flutter View Controller-->
        <scene sceneID="tne-QT-ifu">
            <objects>
                <viewController id="BYZ-38-t0r" customClass="FlutterViewController" sceneMemberID="viewController">
                    <layoutGuides>
                        <viewControllerLayoutGuide type="top" id="y3c-jy-aDJ"/>
                        <viewControllerLayoutGuide type="bottom" id="wfy-db-euE"/>
                    </layoutGuides>
                    <view key="view" contentMode="scaleToFill" id="8bC-Xf-vdC">
                        <rect key="frame" x="0.0" y="0.0" width="414" height="896"/>
                        <autoresizingMask key="autoresizingMask" widthSizable="YES" heightSizable="YES"/>
                        <color key="backgroundColor" red="1" green="1" blue="1" alpha="1" colorSpace="custom" customColorSpace="sRGB"/>
                    </view>
                </viewController>
                <placeholder placeholderIdentifier="IBFirstResponder" id="dkx-z0-nzr" sceneMemberID="firstResponder"/>
            </objects>
            <point key="canvasLocation" x="-25" y="-30"/>
        </scene>
    </scenes>
</document>



================================================
FILE: example/lib/main.dart
================================================
import 'dart:async';
import 'dart:collection';
import 'dart:developer';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:web3auth_flutter/enums.dart';
import 'package:web3auth_flutter/input.dart';
import 'package:web3auth_flutter/output.dart';
import 'package:web3auth_flutter/web3auth_flutter.dart';
import 'package:web3dart/web3dart.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> with WidgetsBindingObserver {
  String _result = '';
  bool logoutVisible = false;
  late final TextEditingController textEditingController;

  @override
  void initState() {
    super.initState();
    initPlatformState();
    textEditingController = TextEditingController();
    WidgetsBinding.instance.addObserver(this);
  }

  @override
  void dispose() {
    super.dispose();
    WidgetsBinding.instance.removeObserver(this);
  }

  @override
  void didChangeAppLifecycleState(final AppLifecycleState state) {
    // This is important to trigger the user cancellation on Android.
    if (state == AppLifecycleState.resumed) {
      Web3AuthFlutter.setCustomTabsClosed();
    }
  }

  // Platform messages are asynchronous, so we initialize in an async method.
  Future<void> initPlatformState() async {
    HashMap themeMap = HashMap<String, String>();
    themeMap['primary'] = "#229954";

    Uri redirectUrl;
    if (Platform.isAndroid) {
      redirectUrl = Uri.parse('torusapp://org.torusresearch.flutter.web3authexample');
    } else if (Platform.isIOS) {
      redirectUrl =
          Uri.parse('com.web3auth.flutter.web3authflutterexample://auth');
    } else {
      throw UnKnownException('Unknown platform');
    }

    final loginConfig = HashMap<String, LoginConfigItem>();
    loginConfig['jwt'] = LoginConfigItem(
        verifier: "w3a-auth0-demo", // get it from web3auth dashboard
        typeOfLogin: TypeOfLogin.jwt,
        clientId: "hUVVf4SEsZT7syOiL0gLU9hFEtm2gQ6O" // auth0 client id
        );

    await Web3AuthFlutter.init(
      Web3AuthOptions(
        clientId:
            'BHgArYmWwSeq21czpcarYh0EVq2WWOzflX-NTK-tY1-1pauPzHKRRLgpABkmYiIV_og9jAvoIxQ8L3Smrwe04Lw',
        //sdkUrl: 'https://auth.mocaverse.xyz',
        //walletSdkUrl: 'https://lrc-mocaverse.web3auth.io',
        network: Network.sapphire_devnet,
        buildEnv: BuildEnv.production,
        redirectUrl: redirectUrl,
        whiteLabel: WhiteLabelData(
          mode: ThemeModes.dark,
          defaultLanguage: Language.en,
          appName: "Web3Auth Flutter App",
          theme: themeMap,
        ),
        loginConfig: loginConfig,
      ),
    );

    try {
      await Web3AuthFlutter.initialize();
    } catch (e) {
      print('Error during Web3Auth initialization: $e');
    }

    final String res = await Web3AuthFlutter.getPrivKey();
    log(res);
    if (res.isNotEmpty) {
      setState(() {
        logoutVisible = true;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Builder(
        builder: (context) {
          return Scaffold(
            appBar: AppBar(
              title: const Text('Web3Auth x Flutter Example'),
            ),
            body: SingleChildScrollView(
              child: Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Padding(
                      padding: EdgeInsets.all(8.0),
                    ),
                    Visibility(
                      visible: !logoutVisible,
                      child: Column(
                        children: [
                          const SizedBox(
                            height: 50,
                          ),
                          const Icon(
                            Icons.flutter_dash,
                            size: 80,
                            color: Color(0xFF1389fd),
                          ),
                          const SizedBox(
                            height: 40,
                          ),
                          const Text(
                            'Web3Auth',
                            style: TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: 36,
                                color: Color(0xFF0364ff)),
                          ),
                          const SizedBox(
                            height: 10,
                          ),
                          const Text(
                            'Welcome to Web3Auth x Flutter Demo',
                            style: TextStyle(fontSize: 14),
                          ),
                          const SizedBox(
                            height: 20,
                          ),
                          const Text(
                            'Login with',
                            style: TextStyle(fontSize: 12),
                          ),
                          const SizedBox(
                            height: 20,
                          ),
                          ElevatedButton(
                            onPressed: _login(_withGoogle),
                            child: const Text('Google'),
                          ),
                          ElevatedButton(
                            onPressed: _login(_withFacebook),
                            child: const Text('Facebook'),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(8.0),
                            child: TextField(
                              controller: textEditingController,
                              decoration: const InputDecoration(
                                border: OutlineInputBorder(),
                                hintText: "abc@xyz.com",
                              ),
                            ),
                          ),
                          ElevatedButton(
                            onPressed: _login(_withEmailPasswordless),
                            child: const Text('Email Passwordless'),
                          ),
                          ElevatedButton(
                            onPressed: _login(_withDiscord),
                            child: const Text('Discord'),
                          ),
                        ],
                      ),
                    ),
                    Visibility(
                      visible: logoutVisible,
                      child: Column(
                        children: [
                          ElevatedButton(
                            style: ElevatedButton.styleFrom(
                              backgroundColor: Colors.red[600],
                            ),
                            onPressed: _logout(),
                            child: const Text('Logout'),
                          ),
                          ElevatedButton(
                            onPressed: _privKey(_getPrivKey),
                            child: const Text('Get PrivKey'),
                          ),
                          ElevatedButton(
                            onPressed: _userInfo(_getUserInfo),
                            child: const Text('Get UserInfo'),
                          ),
                          ElevatedButton(
                            onPressed: _launchWalletServices(),
                            child: const Text('Launch Wallet Services'),
                          ),
                          ElevatedButton(
                            onPressed: _setupMFA(),
                            child: const Text('Setup MFA'),
                          ),
                          ElevatedButton(
                            onPressed: _manageMFA(),
                            child: const Text('Manage MFA'),
                          ),
                          ElevatedButton(
                            onPressed: _signMesssage(context),
                            child: const Text('Sign Message'),
                          ),
                        ],
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(_result),
                    )
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  VoidCallback _login(Future<Web3AuthResponse> Function() method) {
    return () async {
      try {
        final Web3AuthResponse _ = await method();
        setState(() {
          logoutVisible = true;
        });
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      } catch (e) {
        log(e.toString());
      }
    };
  }

  VoidCallback _logout() {
    return () async {
      try {
        await Web3AuthFlutter.logout();
        setState(() {
          _result = '';
          logoutVisible = false;
        });
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  VoidCallback _privKey(Future<String?> Function() method) {
    return () async {
      try {
        final String response = await Web3AuthFlutter.getPrivKey();
        setState(() {
          _result = response;
          logoutVisible = true;
        });
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  VoidCallback _userInfo(Future<TorusUserInfo> Function() method) {
    return () async {
      try {
        final TorusUserInfo response = await Web3AuthFlutter.getUserInfo();
        setState(() {
          _result = response.toString();
          logoutVisible = true;
        });
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  Future<Web3AuthResponse> _withGoogle() {
    return Web3AuthFlutter.login(
      LoginParams(loginProvider: Provider.google, mfaLevel: MFALevel.NONE),
    );
  }

  Future<Web3AuthResponse> _withFacebook() {
    return Web3AuthFlutter.login(LoginParams(loginProvider: Provider.facebook));
  }

  Future<Web3AuthResponse> _withEmailPasswordless() {
    return Web3AuthFlutter.login(
      LoginParams(
        loginProvider: Provider.email_passwordless,
        extraLoginOptions: ExtraLoginOptions(
          login_hint: textEditingController.text,
        ),
      ),
    );
  }

  Future<Web3AuthResponse> _withDiscord() {
    return Web3AuthFlutter.login(LoginParams(loginProvider: Provider.discord));
  }

  Future<String?> _getPrivKey() {
    return Web3AuthFlutter.getPrivKey();
  }

  Future<TorusUserInfo> _getUserInfo() {
    return Web3AuthFlutter.getUserInfo();
  }

  VoidCallback _launchWalletServices() {
    return () async {
      try {
        await Web3AuthFlutter.launchWalletServices(
          ChainConfig(
            chainId: "0x89",
            rpcTarget:
                "https://mainnet.infura.io/v3/daeee53504be4cd3a997d4f2718d33e0",
          ),
        );
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  VoidCallback _setupMFA() {
    return () async {
      try {
        await Web3AuthFlutter.enableMFA();
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  VoidCallback _manageMFA() {
    return () async {
      try {
        bool result = await Web3AuthFlutter.manageMFA();
        if (result) {
          log("MFA manage successfully done.");
        } else {
          log("Some error occured.");
        }
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  VoidCallback _signMesssage(BuildContext context) {
    return () async {
      try {
        String? privKey = await _getPrivKey();
        final credentials = EthPrivateKey.fromHex(privKey!);
        final address = credentials.address;
        List<dynamic> params = [];
        params.add("Hello, Web3Auth from Flutter!");
        params.add(address.hexEip55);
        params.add("Web3Auth");
        final signResponse = await Web3AuthFlutter.request(
          ChainConfig(chainId: "0x89", rpcTarget: "https://polygon-rpc.com/"),
          "personal_sign",
          params,
          appState: "web3auth",
        );
        if (context.mounted) {
          showAlertDialog(
            context,
            'Sign Result',
            signResponse.toString(),
          );
        }
      } on UserCancelledException {
        log("User cancelled.");
      } on UnKnownException {
        log("Unknown exception occurred");
      }
    };
  }

  void showAlertDialog(BuildContext context, String title, String content) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(title),
          content: Text(content),
          actions: <Widget>[
            TextButton(
              child: const Text('OK'),
              onPressed: () {
                Navigator.of(context).pop(); // Close the dialog
              },
            ),
          ],
        );
      },
    );
  }
}



================================================
FILE: example/test/widget_test.dart
================================================
// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility that Flutter provides. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:web3auth_flutter_example/main.dart';

void main() {
  testWidgets('Verify Platform version', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());

    // Verify that platform version is retrieved.
    expect(
      find.byWidgetPredicate(
        (Widget widget) =>
            widget is Text && widget.data!.startsWith('Running on:'),
      ),
      findsOneWidget,
    );
  });
}



================================================
FILE: ios/web3auth_flutter.podspec
================================================
#
# To learn more about a Podspec see http://guides.cocoapods.org/syntax/podspec.html.
# Run `pod lib lint web3auth_flutter.podspec` to validate before publishing.
#
Pod::Spec.new do |s|
  s.name             = 'web3auth_flutter'
  s.version          = '2.0.1'
  s.summary          = 'Flutter SDK for Torus Web3Auth'
  s.description      = <<-DESC
Flutter SDK for Torus Web3Auth (OpenLogin)
                       DESC
  s.homepage         = 'https://web3auth.io'
  s.license          = { :file => '../LICENSE' }
  s.author           = { 'Web3Auth' => 'hello@web3auth.io' }
  s.source           = { :path => '.' }
  s.source_files = 'Classes/**/*'
  s.dependency 'Flutter'
  s.dependency 'Web3Auth', '~> 11.1.0'
  s.platform = :ios, '14.0'

  # Flutter.framework does not contain a i386 slice.
  s.pod_target_xcconfig = { 'DEFINES_MODULE' => 'YES', 'EXCLUDED_ARCHS[sdk=iphonesimulator*]' => 'i386' }
  s.swift_version = '5.0'
end



================================================
FILE: ios/Assets/.gitkeep
================================================
[Empty file]


================================================
FILE: ios/Classes/SwiftWeb3AuthFlutterPlugin.swift
================================================
import Flutter
import UIKit
import Web3Auth

public class SwiftWeb3AuthFlutterPlugin: NSObject, FlutterPlugin {
    public static func register(with registrar: FlutterPluginRegistrar) {
        let channel = FlutterMethodChannel(name: "web3auth_flutter", binaryMessenger: registrar.messenger())
        let instance = SwiftWeb3AuthFlutterPlugin()
        registrar.addMethodCallDelegate(instance, channel: channel)
    }

    var web3auth: Web3Auth?
    public var state: Web3AuthState? {
        return web3auth?.state
    }
    var decoder = JSONDecoder()
    var encoder = JSONEncoder()

    public func handle(_ call: FlutterMethodCall, result: @escaping FlutterResult) {
        Task {
            // print(call, "calling args")
            guard let args = call.arguments as? String else {
                result(FlutterError(
                    code: "INVALID_ARGUMENTS",
                    message: "Invalid Flutter iOS plugin method arguments",
                    details: nil))
                return
            }
            guard let data = args.data(using: .utf8) else {
                result(FlutterError(
                    code: "INVALID_ARGUMENTS",
                    message: "Invalid Flutter iOS plugin init params",
                    details: nil))
                return
            }
            // print("call data", data)
            switch call.method {
            case "init":
                let initParams: W3AInitParams
                do {
                    initParams = try decoder.decode(W3AInitParams.self, from: data)
                    // print(initParams, "params")
                } catch {
                    // print(error)
                    result(FlutterError(
                        code: "INVALID_ARGUMENTS",
                        message: "Invalid Flutter decode init params",
                        details: data))
                    return
                }
                do {
                    let web3auth = try await Web3Auth(initParams)
                    self.web3auth = web3auth
                    result(nil)
                    return
                } catch {
                    result(FlutterError(
                        code: "InitFailedException",
                        message: "Web3Auth init failed",
                        details: error.localizedDescription))
                    return
                }
            case "login":
                guard let web3auth = web3auth
                else {
                    result(FlutterError(
                        code: "NotInitializedException",
                        message: "Web3Auth.init has to be called first",
                        details: nil))
                    return
                }
                let loginParams: W3ALoginParams
                do {
                    loginParams = try decoder.decode(W3ALoginParams.self, from: data)
                    //print("loginParams: \(loginParams)")
                } catch {
                    //print(error)
                    result(FlutterError(
                        code: "INVALID_ARGUMENTS",
                        message: "Invalid Login Params",
                        details: nil))
                    return
                }
                var resultMap: String = ""
                do {
                    let result = try await web3auth.login(loginParams)
                    let resultData = try encoder.encode(result)
                    resultMap = String(decoding: resultData, as: UTF8.self)
                } catch {
                    result(FlutterError(
                        code: "LoginFailedException",
                        message: "Web3Auth login flow failed",
                        details: error.localizedDescription
                    ))
                    return
                }
                result(resultMap)
                return
            case "logout":
                do {
                    try await web3auth?.logout()
                    result(nil)
                    return
                } catch {
                    result(FlutterError(
                        code: "LogoutFailedException",
                        message: "Web3Auth logout failed",
                        details: error.localizedDescription
                    ))
                    return
                }
            case "initialize":
                // There is no initialize function in swift
                result(nil)
                return
            case "getPrivKey":
                let privKey = web3auth?.getPrivkey()
                result(privKey)
                return
            case "getEd25519PrivKey":
                let getEd25519PrivKey = web3auth?.getEd25519PrivKey()
                result(getEd25519PrivKey)
                return
            case "launchWalletServices":
                let wsParams: WalletServicesParams
                do {
                    wsParams = try decoder.decode(WalletServicesParams.self, from: data)
                    print("chainConfig: \(wsParams.chainConfig)")
                } catch {
                    result(FlutterError(
                        code: "INVALID_ARGUMENTS",
                        message: "Invalid Wallet Services Params",
                        details: nil))
                        return
                }
                
                do {
                    try await web3auth?.launchWalletServices(chainConfig: wsParams.chainConfig, path: wsParams.path)
                    result(nil)
                    return
                } catch {
                     result(FlutterError(
                         code: "WalletServicesFailedFailedException",
                         message: "Web3Auth wallet services launch failed",
                         details: error.localizedDescription))
                     return
                }
            case "enableMFA":
                do {
                    let loginParams = try? decoder.decode(W3ALoginParams.self, from: data)

                    if let params = loginParams {
                        let enableMFAResult = try await web3auth?.enableMFA(params)
                        result(enableMFAResult)
                    } else {
                        let enableMFAResult = try await web3auth?.enableMFA()
                        result(enableMFAResult)
                    }
                    return
                } catch {
                    result(FlutterError(
                        code: "enableMFAFailedException",
                        message: "Web3Auth enableMFA failed",
                        details: error.localizedDescription))
                    return
                }
            case "manageMFA":
                do {
                    let loginParams = try? decoder.decode(W3ALoginParams.self, from: data)

                    if let params = loginParams {
                        let manageMFAResult = try await web3auth?.manageMFA(params)
                        result(manageMFAResult)
                    } else {
                        let manageMFAResult = try await web3auth?.manageMFA()
                        result(manageMFAResult)
                    }
                    return
                } catch {
                    result(FlutterError(
                        code: "manageMFAFailedException",
                        message: "Web3Auth manageMFA failed",
                        details: error.localizedDescription))
                    return
                }
            case "request":
                let reqParams: RequestJson
                    do {
                        reqParams = try decoder.decode(RequestJson.self, from: data)
                        } catch {
                        result(FlutterError(
                            code: "INVALID_ARGUMENTS",
                            message: "Invalid request Params",
                            details: error.localizedDescription))
                            return
                        }
                
                    do {
                        let signResponse = try await web3auth?.request(
                            chainConfig: reqParams.chainConfig,
                            method: reqParams.method,
                            requestParams: reqParams.requestParams,
                            path: reqParams.path,
                            appState: reqParams.appState
                        )
                        let signData = try encoder.encode(signResponse)
                        let resultMap = String(decoding: signData, as: UTF8.self)
                        result(resultMap)
                        return
                    } catch {
                        result(FlutterError(
                            code: "RequestFailedFailedException",
                            message: "Web3Auth request launch failed",
                            details: error.localizedDescription))
                        return
                    }
            case "getUserInfo":
                var resultMap: String = ""
                do {
                    let userInfo = try web3auth?.getUserInfo()
                    let resultData = try encoder.encode(userInfo)
                    resultMap = String(decoding: resultData, as: UTF8.self)
                } catch {
                    result(FlutterError(
                        code: "GetUserInfoFailedException",
                        message: "Web3Auth getUserInfo failed",
                        details: error.localizedDescription
                    ))
                    return
                }
                result(resultMap)
                return

            case "getWeb3AuthResponse":
                var resultMap: String = ""
                do {
                    let web3AuthResult = try web3auth?.getWeb3AuthResponse()
                    let resultData = try encoder.encode(web3AuthResult)
                    resultMap = String(decoding: resultData, as: UTF8.self)
                } catch {
                    result(FlutterError(
                        code: "GetWeb3AuthResponseFailedException",
                        message: "Web3Auth getUserInfo failed",
                        details: error.localizedDescription
                    ))
                    return
                }
                result(resultMap)
                return

            default:
                result(FlutterMethodNotImplemented)
            }
        }
    }
}

struct WalletServicesParams: Codable {
    let chainConfig: ChainConfig
    let path: String?
}

struct RequestJson: Codable {
    let chainConfig: ChainConfig
    let method: String
    let requestParams: [String]
    let path: String?
    let appState: String?
}



================================================
FILE: ios/Classes/Web3AuthFlutterPlugin.h
================================================
#import <Flutter/Flutter.h>

@interface Web3AuthFlutterPlugin : NSObject<FlutterPlugin>
@end



================================================
FILE: ios/Classes/Web3AuthFlutterPlugin.m
================================================
#import "Web3AuthFlutterPlugin.h"
#if __has_include(<web3auth_flutter/web3auth_flutter-Swift.h>)
#import <web3auth_flutter/web3auth_flutter-Swift.h>
#else
// Support project import fallback if the generated compatibility header
// is not copied when this plugin is created as a library.
// https://forums.swift.org/t/swift-static-libraries-dont-copy-generated-objective-c-header/19816
#import "web3auth_flutter-Swift.h"
#endif

@implementation Web3AuthFlutterPlugin
+ (void)registerWithRegistrar:(NSObject<FlutterPluginRegistrar>*)registrar {
  [SwiftWeb3AuthFlutterPlugin registerWithRegistrar:registrar];
}
@end



================================================
FILE: lib/enums.dart
================================================
enum Network { mainnet, testnet, cyan, aqua, sapphire_devnet, sapphire_mainnet }

enum BuildEnv { production, staging, testing }

enum ChainNamespace { eip155, solana }

enum Language { en, de, ja, ko, zh, es, fr, pt, nl , tr}

enum ThemeModes { light, dark, auto }

enum Provider {
  google,
  facebook,
  reddit,
  discord,
  twitch,
  github,
  apple,
  linkedin,
  twitter,
  line,
  kakao,
  email_passwordless,
  jwt,
  sms_passwordless,
  farcaster,
}

enum TypeOfLogin {
  google,
  facebook,
  reddit,
  discord,
  twitch,
  github,
  apple,
  kakao,
  linkedin,
  twitter,
  weibo,
  wechat,
  line,
  email_passwordless,
  email_password,
  jwt,
  sms_passwordless,
  farcaster,
}

enum Display {
  /// Displays the UI with a full page view.
  page,

  /// Displays the UI with a popup window.
  popup,

  /// Displays the UI in a way that leverages a touch interface.
  touch,

  /// Displays the UI with a "feature phone" type interface.
  wap,
}

enum MFALevel {
  /// Presents the MFA screen every third login.
  DEFAULT,
  /// Presents the MFA screen on every login, but user can skip it.
  OPTIONAL,
  /// Make it mandatory for users to set up MFA after login.
  MANDATORY,
  /// Skips the MFA setup screen.
  NONE,
}

extension MFALevelExtension on MFALevel {
  String get type {
    switch (this) {
      case MFALevel.DEFAULT:
        return "default";
      case MFALevel.OPTIONAL:
        return "optional";
      case MFALevel.MANDATORY:
        return "mandatory";
      case MFALevel.NONE:
        return "none";
      default:
        return "default";
    }
  }
}

enum Prompt {
  /// Do not prompt user for login or consent on re-authentication.
  none,

  /// Prompt user for re-authentication.
  login,

  /// Prompt user for consent before processing request.
  consent,

  /// Prompt user to select an account.
  select_account,
}

enum Curve { secp256k1, ed25519 }



================================================
FILE: lib/input.dart
================================================
import 'dart:collection';

import 'package:web3auth_flutter/enums.dart';
import 'package:web3auth_flutter/web3auth_flutter.dart';

class LoginParams {
  /// [loginProvider] sets the oAuth login method to be used. You can use any of the
  /// valid [Provider] from the supported list.
  final Provider loginProvider;

  /// Custom verifier logins can get a dapp share returned to them post successful login.
  /// This is useful if the dapps want to use this share to allow users to login seamlessly.
  final String? dappShare;

  /// [curve] will be used to determine the public key encoded in the jwt token which returned in
  /// `getUserInfo` function after user login.
  ///
  /// This parameter won't change format of private key returned by We3Auth. Private key returned
  /// by [Web3AuthFlutter.getPrivKey] is always secp256k1. To get the ed25519 key
  /// you can use [Web3AuthFlutter.getEd25519PrivKey] method.
  ///
  /// The default value is [Curve.secp256k1].
  final Curve? curve;

  /// [extraLoginOptions] can be used to set the OAuth login options for corresponding [loginProvider].
  ///
  /// For instance, you'll need to pass user's email address as `login_hint` for [Provider.email_passwordless].
  final ExtraLoginOptions? extraLoginOptions;

  /// Deeplinking for the application where user will be redirected after login.
  final Uri? redirectUrl;

  final String? appState;

  /// Customize the MFA screen shown to the user during OAuth authentication.
  final MFALevel? mfaLevel;
  final String? dappUrl;

  LoginParams(
      {required this.loginProvider,
      this.dappShare,
      this.curve = Curve.secp256k1,
      this.extraLoginOptions,
      this.redirectUrl,
      this.appState,
      this.mfaLevel,
      this.dappUrl});

  Map<String, dynamic> toJson() => {
        "loginProvider": loginProvider.name,
        "dappShare": dappShare,
        "curve": curve?.name,
        "extraLoginOptions": extraLoginOptions?.toJson(),
        "redirectUrl": redirectUrl?.toString(),
        "appState": appState,
        "mfaLevel": mfaLevel?.type,
        "dappUrl": dappUrl
      };
}

class LoginConfigItem {
  /// Custom verifier name given in the developer dashboard.
  final String verifier;

  /// The type of login for custom verifier.
  final TypeOfLogin typeOfLogin;

  /// Client id provided by your login provider used for custom verifier.
  final String clientId;

  /// Display name for the verifier. If null, the default name is used.
  final String? name;

  /// Description for the button. If provided, it renders as a full length button. else, icon button.
  final String? description;

  /// The field in JWT token which maps to verifier id. Please make sure you selected
  /// correct JWT verifier id in the developer dashboard.
  final String? verifierSubIdentifier;

  /// Logo to be shown on mouse hover.
  final String? logoHover;

  /// Light logo for the dark theme.
  final String? logoLight;

  /// Dark logo for the light theme.
  final String? logoDark;

  /// Show login button on the main list.
  final bool? mainOption;

  /// Whether to show the login button on Modal.
  final bool? showOnModal;

  /// Whether to show the login button on the Desktop.
  final bool? showOnDesktop;

  /// Whether to show the login button on Mobile.
  final bool? showOnMobile;

  LoginConfigItem({
    required this.verifier,
    required this.typeOfLogin,
    required this.clientId,
    this.name,
    this.description,
    this.verifierSubIdentifier,
    this.logoHover,
    this.logoLight,
    this.logoDark,
    this.mainOption,
    this.showOnModal,
    this.showOnDesktop,
    this.showOnMobile,
  });

  Map<String, dynamic> toJson() {
    return {
      'verifier': verifier,
      'typeOfLogin': typeOfLogin.name,
      'clientId': clientId,
      'name': name,
      'description': description,
      'verifierSubIdentifier': verifierSubIdentifier,
      'logoHover': logoHover,
      'logoLight': logoLight,
      'logoDark': logoDark,
      'mainOption': mainOption,
      'showOnModal': showOnModal,
      'showOnDesktop': showOnDesktop,
      'showOnMobile': showOnMobile
    };
  }
}

class ExtraLoginOptions {
  final Map? additionalParams;

  /// Your custom authentication domain. For example, if you are using Auth0,
  /// it can be example.au.auth0.com.
  final String? domain;

  /// Client id provided by your login provider used for custom verifier
  final String? client_id;

  /// The value used to account for clock skew in JWT expirations. The value is
  /// in the seconds, and ideally should no more than 60 seconds or 120 seconds at max.
  final String? leeway;

  /// The field in JWT token which maps to verifier id. Please make sure you selected
  /// correct JWT verifier id in the developer dashboard.
  final String? verifierIdField;

  /// Whether the verifier id field is case sensitive or not.
  final bool? isVerifierIdCaseSensitive;

  /// Allows developers the configure the display of UI. Checkout [Display] for more
  /// details.
  final Display? display;

  /// Prompt shown to the user during authentication process. Checkout [Prompt] for more
  /// details.
  final Prompt? prompt;

  /// Max time allowed without reauthentication. If the last time user authenticated
  /// is greater than this value, then user must reauthenticate.
  final String? max_age;

  /// The space separated list of language tags, ordered by preference. For instance
  /// `fr-CA fr en`.
  final String? ui_locales;

  /// [id_token_hint] denotes the previously issued ID token.
  final String? id_token_hint;

  final String? id_token;

  /// [login_hint] is used to send the user's email address during [Provider.email_passwordless].
  final String? login_hint;

  final String? acr_values;

  /// The default scope to be used on authentication requests. The defaultScope
  /// defined in the Auth0Client is included along with this scope.
  final String? scope;

  /// The audience, presented as the aud claim in the access token,
  /// defines the intended consumer of the token.
  final String? audience;

  /// The name of the connection configured for your application. If null, it will redirect to
  /// the Auth0 Login Page and show the Login Widget.
  final String? connection;

  final String? state;

  /// Defines which grant to execute for the authorization server.
  final String? response_type;
  final String? nonce;

  /// [redirectUrl] can be used to specify the default url, where your custom jwt verifier can redirect
  /// your browser to with the result. If you are using Auth0, it must be whitelisted in the Allowed
  /// Callback URLs in your Auth0's application.
  final String? redirect_uri;

  ExtraLoginOptions({
    this.additionalParams = const {},
    this.domain,
    this.client_id,
    this.leeway,
    this.verifierIdField,
    this.isVerifierIdCaseSensitive,
    this.display,
    this.prompt,
    this.max_age,
    this.ui_locales,
    this.id_token_hint,
    this.id_token,
    this.login_hint,
    this.acr_values,
    this.scope,
    this.audience,
    this.connection,
    this.state,
    this.response_type,
    this.nonce,
    this.redirect_uri,
  });

  Map<String, dynamic> toJson() => {
        "additionalParams": additionalParams,
        "domain": domain,
        "client_id": client_id,
        "leeway": leeway,
        "verifierIdField": verifierIdField,
        "isVerifierIdCaseSensitive": isVerifierIdCaseSensitive,
        "display": display?.name,
        "prompt": prompt?.name,
        "max_age": max_age,
        "ui_locales": ui_locales,
        "id_token_hint": id_token_hint,
        "id_token": id_token,
        "login_hint": login_hint,
        "acr_values": acr_values,
        "scope": scope,
        "audience": audience,
        "connection": connection,
        "state": state,
        "response_type": response_type,
        "nonce": nonce,
        "redirect_uri": redirect_uri,
      };
}

class WhiteLabelData {
  /// Display name for the app in the UI.
  final String? appName;

  /// App logo to be used in dark mode.
  final String? logoLight;

  /// App logo to be used in light mode.
  final String? logoDark;

  /// Language which will be used by Web3Auth, app will use browser language if not specified.
  ///
  /// Default language is [Language.en]. Checkout [Language] for supported languages.
  final Language? defaultLanguage;

  /// Theme mode for the login modal
  ///
  /// Default value is [ThemeModes.auto].
  final ThemeModes? mode;

  /// Used to customize the theme of the login modal.
  final HashMap? theme;

  /// Url to be used in the Modal
  final String? appUrl;

  /// Use logo loader.
  ///
  /// If [logoDark] and [logoLight] are null, the default Web3Auth logo
  /// will be used for the loader.
  final bool? useLogoLoader;

  WhiteLabelData({
    this.appName,
    this.logoLight,
    this.logoDark,
    this.defaultLanguage = Language.en,
    this.mode = ThemeModes.auto,
    this.theme,
    this.appUrl,
    this.useLogoLoader = false,
  });

  Map<String, dynamic> toJson() {
    return {
      'appName': appName,
      'logoLight': logoLight,
      'logoDark': logoDark,
      'defaultLanguage': defaultLanguage?.name,
      'mode': mode?.name,
      'theme': theme,
      'appUrl': appUrl,
      'useLogoLoader': useLogoLoader
    };
  }
}

class MfaSetting {
  /// Whether the factor is enabled or not.
  final bool enable;

  /// Priority of the factor over other factors.
  final int? priority;

  /// Whether the factor is mandaotry or not for prove
  /// the owenership.
  final bool? mandatory;

  MfaSetting({required this.enable, this.priority, this.mandatory});

  Map<String, dynamic> toJson() {
    return {'enable': enable, 'priority': priority, 'mandatory': mandatory};
  }
}

class MfaSettings {
  /// Define the settings for device share factor.
  final MfaSetting? deviceShareFactor;

  /// Define the settings for backup share factor.
  final MfaSetting? backUpShareFactor;

  /// Define the settings for social backup factor.
  final MfaSetting? socialBackupFactor;

  /// Define the settings for password factor.
  final MfaSetting? passwordFactor;
  final MfaSetting? passkeysFactor;
  final MfaSetting? authenticatorFactor;

  MfaSettings({
    this.deviceShareFactor,
    this.backUpShareFactor,
    this.socialBackupFactor,
    this.passwordFactor,
    this.passkeysFactor,
    this.authenticatorFactor,
  });

  Map<String, dynamic> toJson() {
    return {
      'deviceShareFactor': deviceShareFactor,
      'backUpShareFactor': backUpShareFactor,
      'socialBackupFactor': socialBackupFactor,
      'passwordFactor': passwordFactor,
      'passkeysFactor': passkeysFactor,
      'authenticatorFactor': authenticatorFactor
    };
  }
}

class ChainConfig {
  final ChainNamespace chainNamespace;
  final int? decimals;
  final String? blockExplorerUrl;
  final String chainId;
  final String? displayName;
  final String? logo;
  final String rpcTarget;
  final String? ticker;
  final String? tickerName;

  ChainConfig({
    this.chainNamespace = ChainNamespace.eip155,
    this.decimals = 18,
    this.blockExplorerUrl,
    required this.chainId,
    this.displayName,
    this.logo,
    required this.rpcTarget,
    this.ticker,
    this.tickerName,
  });

  Map<String, dynamic> toJson() {
    return {
      'chainNamespace': chainNamespace.name,
      'decimals': decimals,
      'blockExplorerUrl': blockExplorerUrl,
      'chainId': chainId,
      'displayName': displayName,
      'logo': logo,
      'rpcTarget': rpcTarget,
      'ticker': ticker,
      'tickerName': tickerName
    };
  }
}

class Web3AuthOptions {
  /// Client id for web3auth.
  ///
  /// You can obtain your client id from the web3auth [developer dashboard](https://dashboard.web3auth.io/).
  final String clientId;

  /// Web3Auth Network to use for the session & the issued idToken.
  ///
  /// User [Network.sapphire_mainnet] for production build.
  final Network network;

  /// [buildEnv] is used for internal testing purposes. This buildEnv
  /// signifies the enviroment for Web3Auth, and doesn't signifies
  /// the enviorment of the application.
  final BuildEnv? buildEnv;

  /// Define the desired Web3Auth service url.
  final String? sdkUrl;
  final String? walletSdkUrl;

  /// Deeplinking for the application where user will be redirected after login.
  /// Ideally, it should be bundleId and package name for iOS and Android respectively.
  ///
  /// While using redirectUrl, please make sure you have whitelisted it
  /// developer dashboard. Checkout [SDK reference](https://web3auth.io/docs/sdk/pnp/flutter/install#configuration-1) more details.
  final Uri? redirectUrl;

  /// WhiteLabel options for web3auth. It helps you define
  /// custom UI, branding, and translations for your brand app.
  ///
  /// Checkout [WhiteLabelData] for more details.
  final WhiteLabelData? whiteLabel;

  /// Login config for the custom verifiers.
  final HashMap<String, LoginConfigItem>? loginConfig;

  /// Use [useCoreKitKey] to get the core kit key.
  final bool? useCoreKitKey;

  final ChainNamespace? chainNamespace;

  /// Allows developers to configure the [MfaSettings] for authentication.
  ///
  /// Checkout [MFA SDK Reference](https://web3auth.io/docs/sdk/pnp/flutter/mfa) for more details.
  final MfaSettings? mfaSettings;

  /// [sessionTime] allows developers to configure the session management time.
  ///
  /// Session Time is in seconds, default is 86400 seconds which is 1 day. [sessionTime] can be max 30 days.
  final int? sessionTime;

  final ChainConfig? chainConfig;

  final Map<String, String>? originData;

  final String? dashboardUrl;

  Web3AuthOptions({
    required this.clientId,
    required this.network,
    this.buildEnv = BuildEnv.production,
    String? sdkUrl,
    String? walletSdkUrl,
    this.redirectUrl,
    this.whiteLabel,
    this.loginConfig,
    this.useCoreKitKey,
    this.chainNamespace = ChainNamespace.eip155,
    this.sessionTime = 30 * 86400,
    this.mfaSettings,
    this.originData,
    String? dashboardUrl,
  })  : chainConfig = null,
        sdkUrl = sdkUrl ?? getSdkUrl(buildEnv ?? BuildEnv.production),
        walletSdkUrl =
            walletSdkUrl ?? getWalletSdkUrl(buildEnv ?? BuildEnv.production),
        dashboardUrl =
            dashboardUrl ?? getDashboardUrl(buildEnv ?? BuildEnv.production);

  Map<String, dynamic> toJson() {
    return {
      'clientId': clientId,
      'network': network.name,
      'sdkUrl': sdkUrl,
      'walletSdkUrl': walletSdkUrl,
      'buildEnv': buildEnv?.name,
      'redirectUrl': redirectUrl.toString(),
      'whiteLabel': whiteLabel?.toJson(),
      'loginConfig': loginConfig,
      'useCoreKitKey': useCoreKitKey,
      'chainNamespace': chainNamespace?.name,
      'mfaSettings': mfaSettings,
      "sessionTime": sessionTime,
      "chainConfig": chainConfig?.toJson(),
      "originData": originData,
      "dashboardUrl": dashboardUrl,
    };
  }
}

class UserCancelledException implements Exception {}

class UnKnownException implements Exception {
  final String? message;

  UnKnownException(this.message);
}

String getSdkUrl(BuildEnv? buildEnv) {
  const String version = "v9";
  switch (buildEnv) {
    case BuildEnv.staging:
      return "https://staging-auth.web3auth.io/$version";
    case BuildEnv.testing:
      return "https://develop-auth.web3auth.io";
    case BuildEnv.production:
    default:
      return "https://auth.web3auth.io/$version";
  }
}

String getWalletSdkUrl(BuildEnv? buildEnv) {
  const String walletServicesVersion = "v4";
  switch (buildEnv) {
    case BuildEnv.staging:
      return "https://staging-wallet.web3auth.io/$walletServicesVersion";
    case BuildEnv.testing:
      return "https://develop-wallet.web3auth.io";
    case BuildEnv.production:
    default:
      return "https://wallet.web3auth.io/$walletServicesVersion";
  }
}

String getDashboardUrl(BuildEnv? buildEnv) {
  const String walletAccountConstant = "wallet/account";
  switch (buildEnv) {
    case BuildEnv.staging:
      return "https://staging-account.web3auth.io/$walletAccountConstant";
    case BuildEnv.testing:
      return "https://develop-account.web3auth.io/$walletAccountConstant";
    case BuildEnv.production:
    default:
      return "https://account.web3auth.io/$walletAccountConstant";
  }
}



================================================
FILE: lib/output.dart
================================================
import 'dart:core';

class Web3AuthResponse {
  /// secp256k1 private key compaitible with Ethereum ecosystem.
  final String? privKey;

  /// ed25519 private key compaitible with Solana ecosystem.
  final String? ed25519PrivKey;

  /// Current We3Auth sessionId.
  final String? sessionId;

  /// User's information based on the current session.
  final TorusUserInfo? userInfo;

  final String? error;

  /// secp256k1 core kit key.
  final String? coreKitKey;

  /// ed25519 core kit key.
  final String? coreKitEd25519PrivKey;
  final String? factorKey;
  final List<String>? signatures;
  final int? tssShareIndex;
  final String? tssPubKey;
  final String? tssShare;
  final int? tssNonce;
  final List<int>? nodeIndexes;
  final String? keyMode;

  Web3AuthResponse({
    this.privKey,
    this.userInfo,
    this.error,
    this.ed25519PrivKey,
    this.sessionId,
    this.coreKitKey,
    this.coreKitEd25519PrivKey,
    this.factorKey,
    this.signatures,
    this.tssShareIndex,
    this.tssPubKey,
    this.tssShare,
    this.tssNonce,
    this.nodeIndexes,
    this.keyMode
  });

  @override
  String toString() {
    return "{privKey=$privKey, userInfo = ${userInfo.toString()}, ed25519PrivKey=$ed25519PrivKey, coreKitKey=$coreKitKey, coreKitEd25519PrivKey=$coreKitEd25519PrivKey, sessionId=$sessionId, error=$error,"
        "factorKey=$factorKey, signatures=$signatures, tssShareIndex=$tssShareIndex, tssPubKey=$tssPubKey, tssShare=$tssShare, tssNonce=$tssNonce, nodeIndexes=$nodeIndexes, keyMode=$keyMode}";
  }

  Map<String, dynamic> toJson() {
    return {
      'privKey': privKey,
      'userInfo': userInfo?.toJson(),
      'ed25519PrivKey': ed25519PrivKey,
      'sessionId': sessionId,
      'error': error,
      'coreKitKey': coreKitKey,
      'coreKitEd25519PrivKey': coreKitEd25519PrivKey,
      'factorKey': factorKey,
      'signatures': signatures,
      'tssShareIndex': tssShareIndex,
      'tssPubKey': tssPubKey,
      'tssShare': tssShare,
      'tssNonce': tssNonce,
      'nodeIndexes': nodeIndexes,
      'keyMode': keyMode
    };
  }

  Web3AuthResponse.fromJson(Map<String, dynamic> json)
      : privKey = json['privKey'],
        userInfo = json['userInfo'] != null
            ? TorusUserInfo.fromJson(json['userInfo'])
            : null,
        ed25519PrivKey = json['ed25519PrivKey'],
        sessionId = json['sessionId'],
        coreKitKey = json['coreKitKey'],
        coreKitEd25519PrivKey = json['coreKitEd25519PrivKey'],
        error = json['error'],
        factorKey = json['factorKey'],
        signatures = json['signatures'] != null
            ? List<String>.from(json['signatures'])
            : null,
        tssShareIndex = json['tssShareIndex'],
        tssPubKey = json['tssPubKey'],
        tssShare = json['tssShare'],
        tssNonce = json['tssNonce'],
        nodeIndexes = json['nodeIndexes'] != null
            ? List<int>.from(json['nodeIndexes'])
            : null,
        keyMode = json['keyMode'];
}

class TorusUserInfo {
  /// Email of the connected user.
  final String? email;

  /// Name of the connected user.
  final String? name;

  /// Profile image of the connected user.
  final String? profileImage;

  /// Details of the verifier type.
  final String? verifier;

  /// Verified id for the custom verifiers.
  final String? verifierId;

  /// Type of login choosen by user, like google, facebook, etc.
  final String? typeOfLogin;

  /// Details of the aggregate verifier, if present.
  final String? aggregateVerifier;

  /// If you are using a Custom Verifier, you can get a dapp share after successful login.
  /// This share can act as a replacement to your user's device share.
  ///
  /// It is a 24 word seed phrase)
  final String? dappShare;

  /// JWT token issued by the Web3Auth.
  final String? idToken;

  /// JWT token issued by the OAuth provider.
  final String? oAuthIdToken;

  //// Access token issued by the OAuth provider.
  final String? oAuthAccessToken;

  /// Defines whether MFA is enabled or not.
  final bool? isMfaEnabled;

  const TorusUserInfo({
    this.email,
    this.name,
    this.profileImage,
    this.verifier,
    this.verifierId,
    this.typeOfLogin,
    this.aggregateVerifier,
    this.dappShare,
    this.idToken,
    this.oAuthIdToken,
    this.oAuthAccessToken,
    this.isMfaEnabled,
  });

  @override
  String toString() {
    return "{email=$email, name=$name, profileImage=$profileImage, verifier=$verifier,"
        "verifierId=$verifierId, typeOfLogin=$typeOfLogin, dappShare=$dappShare, idToken=$idToken, oAuthIdToken=$oAuthIdToken, oAuthAccessToken=$oAuthAccessToken, isMfaEnabled=$isMfaEnabled}";
  }

  Map<String, dynamic> toJson() {
    return {
      'email': email,
      'name': name,
      'profileImage': profileImage,
      'verifier': verifier,
      'verifierId': verifierId,
      'typeOfLogin': typeOfLogin,
      'aggregateVerifier': aggregateVerifier,
      'dappShare': dappShare,
      'idToken': idToken,
      'oAuthIdToken': oAuthIdToken,
      'oAuthAccessToken': oAuthAccessToken,
      'isMfaEnabled': isMfaEnabled
    };
  }

  TorusUserInfo.fromJson(Map<String, dynamic> json)
      : email = json['email'],
        name = json['name'],
        profileImage = json['profileImage'],
        verifier = json['verifier'],
        verifierId = json['verifierId'],
        typeOfLogin = json['typeOfLogin'],
        aggregateVerifier = json['aggregateVerifier'],
        dappShare = json['dappShare'],
        idToken = json['idToken'],
        oAuthIdToken = json['oAuthIdToken'],
        oAuthAccessToken = json['oAuthAccessToken'],
        isMfaEnabled = json['isMfaEnabled'];
}

class SignResponse {
  final bool success;
  final String? result;
  final String? error;

  SignResponse({
    required this.success,
    this.result,
    this.error,
  });

  @override
  String toString() {
    return "{success=$success, result = $result, error=$error}";
  }

  Map<String, dynamic> toJson() {
    return {
      'success': success,
      'result': result,
      'error': error
    };
  }

  SignResponse.fromJson(Map<String, dynamic> json)
      : success = json['success'],
        result = json['result'],
        error = json['error'];
}



================================================
FILE: lib/web3auth_flutter.dart
================================================
import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/services.dart';
import 'package:web3auth_flutter/input.dart';
import 'package:web3auth_flutter/output.dart';

class Web3AuthFlutter {
  static const MethodChannel _channel = MethodChannel('web3auth_flutter');

  /// [init] methods helps you setup [Web3AuthFlutter] SDK. You can add
  /// whitelabeling, redirect url, and set other parameters during init.
  ///
  /// Please checkout [Web3AuthOptions] for more details
  static Future<void> init(Web3AuthOptions initParams) async {
    Map<String, dynamic> initParamsJson = initParams.toJson();
    initParamsJson.removeWhere((key, value) => value == null);
    await _channel.invokeMethod('init', jsonEncode(initParamsJson));
  }

  /// [login] method will initiate login flow, opening the browser allowing
  /// users to authenticate themselves with preferred login provider.
  ///
  /// Use [loginParams] to change the login provider, curve, and other parameters.
  /// For more details, look into [LoginParams].
  static Future<Web3AuthResponse> login(LoginParams loginParams) async {
    try {
      Map<String, dynamic> loginParamsJson = loginParams.toJson();
      loginParamsJson.removeWhere((key, value) => value == null);
      final String loginResponse = await _channel.invokeMethod(
        'login',
        jsonEncode(loginParamsJson),
      );

      return Web3AuthResponse.fromJson(jsonDecode(loginResponse));
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  /// [logout] method will initiate the logout for current session.
  static Future<void> logout() async {
    try {
      await _channel.invokeMethod('logout', jsonEncode({}));
      return;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  /// Initializes the [Web3AuthFlutter] with session if present. 
  /// If no active session is present, the method will throw an error. 
  /// 
  /// You should use try and catch block to handle the error when no 
  /// active session is present.
  static Future<void> initialize() async {
    try {
      await _channel.invokeMethod('initialize', jsonEncode({}));
      return;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  /// Returns the secp256k1 EVM compaitible key if the user is successfully
  /// authenticated.
  ///
  /// If user is not authenticated, it'll return empty string.
  static Future<String> getPrivKey() async {
    try {
      final String privKey =
          await _channel.invokeMethod('getPrivKey', jsonEncode({}));
      return privKey;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  /// Returns the ed25519 Solana compaitible key if the user is successfully
  /// authenticated.
  ///
  /// If user is not authenticated, it'll return empty string.
  static Future<String> getEd25519PrivKey() async {
    try {
      final String getEd25519PrivKey =
          await _channel.invokeMethod('getEd25519PrivKey', jsonEncode({}));
      return getEd25519PrivKey;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  /// Returns the user information such as email address, name, session id, and etc.
  ///
  /// If user is not authenticated, it'll throw an error.
  static Future<TorusUserInfo> getUserInfo() async {
    try {
      final String torusUserInfo =
          await _channel.invokeMethod('getUserInfo', jsonEncode({}));
      return TorusUserInfo.fromJson(jsonDecode(torusUserInfo));
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }
  
  /// [setCustomTabsClosed] helps to trigger the [UserCancelledException] exception
  /// on Android.
  ///
  /// The Android SDK uses the custom tabs and from current implementation of chrome custom tab,
  /// it's not possible to add a listener directly to chrome custom tab close button and
  /// trigger login exceptions.
  ///
  /// If you want to trigger exception for user closing the browser tab, you have to use
  /// WidgetsBindingObserver mixin with your your login screen, and call the method during 
  /// [AppLifecycleState.resumed].
  static Future<void> setCustomTabsClosed() async {
    try {
      if (Platform.isAndroid) {
        await _channel.invokeMethod('setCustomTabsClosed');
      }
      return;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  static Exception _handlePlatformException(PlatformException e) {
    switch (e.code) {
      case "UserCancelledException":
        return UserCancelledException();
      case "NoAllowedBrowserFoundException":
        return UnKnownException(e.message);
      default:
        return e;
    }
  }

  static Future<void> launchWalletServices(
    ChainConfig chainConfig, {
    String path = "wallet",
  }) async {
    try {
      Map<String, dynamic> chainConfigJson = chainConfig.toJson();
      chainConfigJson.removeWhere((key, value) => value == null);

      Map<String, dynamic> walletServicesJson = {};
      walletServicesJson["chainConfig"] = chainConfigJson;
      walletServicesJson["path"] = path;

      await _channel.invokeMethod(
        'launchWalletServices',
        jsonEncode(walletServicesJson),
      );

      return;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }
 
  /// [enableMFA] method allows us trigger the MFA flow. If the MFA is already 
  /// enable, the method will throw an error.
  static Future<bool> enableMFA({LoginParams? loginParams}) async {
    try {
      bool isMFASetup = false;
      if (loginParams == null) {
        isMFASetup = await _channel.invokeMethod('enableMFA', jsonEncode({}));
        return isMFASetup;
      } else {
        Map<String, dynamic> loginParamsJson = loginParams.toJson();
        loginParamsJson.removeWhere((key, value) => value == null);
        isMFASetup = await _channel.invokeMethod(
          'enableMFA',
          jsonEncode(loginParamsJson),
        );
      }
      return isMFASetup;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  static Future<bool> manageMFA({LoginParams? loginParams}) async {
    try {
      bool isManageMFA = false;
      if (loginParams == null) {
        isManageMFA = await _channel.invokeMethod('manageMFA', jsonEncode({}));
        return isManageMFA;
      } else {
        Map<String, dynamic> loginParamsJson = loginParams.toJson();
        loginParamsJson.removeWhere((key, value) => value == null);
        isManageMFA = await _channel.invokeMethod(
          'manageMFA',
          jsonEncode(loginParamsJson),
        );
      }
      return isManageMFA;
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  static Future<SignResponse> request(
    ChainConfig chainConfig,
    String method,
    List<dynamic> requestParams, {
    String path = "wallet/request",
    String? appState,
  }) async {
    try {
      Map<String, dynamic> chainConfigJson = chainConfig.toJson();
      chainConfigJson.removeWhere((key, value) => value == null);

      List<String> modifiedRequestParams =
          requestParams.map((param) => jsonEncode(param)).toList();

      Map<String, dynamic> requestJson = {};
      requestJson["chainConfig"] = chainConfigJson;
      requestJson["method"] = method;
      requestJson["requestParams"] = modifiedRequestParams;
      requestJson["path"] = path;
      if (appState != null) {
        requestJson["appState"] = appState;
      }

      final response =
          await _channel.invokeMethod('request', jsonEncode(requestJson));

      if (response == "null") {
        return SignResponse(
          success: false,
          error: "Something went wrong. Unable to process the request.",
        );
      }

      return SignResponse.fromJson(jsonDecode(response));
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }

  static Future<Web3AuthResponse> getWeb3AuthResponse() async {
    try {
      final String web3AuthResponse = await _channel.invokeMethod(
        'getWeb3AuthResponse',
        jsonEncode({}),
      );
      return Web3AuthResponse.fromJson(jsonDecode(web3AuthResponse));
    } on PlatformException catch (e) {
      throw _handlePlatformException(e);
    }
  }
}



================================================
FILE: test/web3auth_flutter_test.dart
================================================
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  const MethodChannel channel = MethodChannel('web3auth_flutter');

  TestWidgetsFlutterBinding.ensureInitialized();

  setUp(() {
    channel.setMockMethodCallHandler((MethodCall methodCall) async {
      return '42';
    });
  });

  tearDown(() {
    channel.setMockMethodCallHandler(null);
  });
}


