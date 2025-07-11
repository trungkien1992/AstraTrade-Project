Directory structure:
└── web3auth-web3auth-web/
    ├── README.md
    ├── babel.config.js
    ├── eslint.config.mjs
    ├── lerna.json
    ├── LICENSE
    ├── package.json
    ├── torus.config.js
    ├── tsconfig.json
    ├── webpack.config.js
    ├── .browserslistrc
    ├── .mocharc.json
    ├── .npmignore
    ├── .nvmrc
    ├── .prettierignore
    ├── .prettierrc.yaml
    ├── demo/
    │   ├── nextjs-ssr-app/
    │   │   ├── README.md
    │   │   ├── next-env.d.ts
    │   │   ├── next.config.js
    │   │   ├── package.json
    │   │   ├── tsconfig.json
    │   │   ├── .eslintrc.json
    │   │   ├── app/
    │   │   │   ├── globals.css
    │   │   │   ├── layout.tsx
    │   │   │   └── page.tsx
    │   │   └── components/
    │   │       ├── Main.tsx
    │   │       └── provider.tsx
    │   ├── react-app-no-modal/
    │   │   ├── README.md
    │   │   ├── config-overrides.js
    │   │   ├── package.json
    │   │   ├── tsconfig.json
    │   │   ├── public/
    │   │   │   ├── index.html
    │   │   │   ├── manifest.json
    │   │   │   └── robots.txt
    │   │   └── src/
    │   │       ├── App.css
    │   │       ├── App.test.tsx
    │   │       ├── App.tsx
    │   │       ├── index.css
    │   │       ├── index.tsx
    │   │       ├── react-app-env.d.ts
    │   │       ├── reportWebVitals.ts
    │   │       ├── setupTests.ts
    │   │       └── web3RPC.ts
    │   ├── vite-react-app-sfa/
    │   │   ├── README.md
    │   │   ├── eslint.config.mjs
    │   │   ├── index.html
    │   │   ├── package.json
    │   │   ├── tsconfig.json
    │   │   ├── vite-env.d.ts
    │   │   ├── vite.config.mts
    │   │   ├── public/
    │   │   │   ├── manifest.json
    │   │   │   └── robots.txt
    │   │   └── src/
    │   │       ├── App.css
    │   │       ├── App.tsx
    │   │       ├── config.ts
    │   │       ├── index.css
    │   │       ├── index.tsx
    │   │       ├── react-app-env.d.ts
    │   │       ├── components/
    │   │       │   └── Main.tsx
    │   │       └── styles/
    │   │           └── Home.module.css
    │   ├── vite-react-app-solana/
    │   │   ├── README.md
    │   │   ├── eslint.config.mjs
    │   │   ├── index.html
    │   │   ├── package.json
    │   │   ├── tsconfig.json
    │   │   ├── vite-env.d.ts
    │   │   ├── vite.config.mts
    │   │   ├── public/
    │   │   │   ├── manifest.json
    │   │   │   └── robots.txt
    │   │   └── src/
    │   │       ├── App.css
    │   │       ├── App.tsx
    │   │       ├── index.css
    │   │       ├── index.tsx
    │   │       ├── react-app-env.d.ts
    │   │       ├── components/
    │   │       │   └── Main.tsx
    │   │       └── styles/
    │   │           └── Home.module.css
    │   ├── vue-app-new/
    │   │   ├── README.md
    │   │   ├── index.html
    │   │   ├── package.json
    │   │   ├── postcss.config.js
    │   │   ├── tailwind.config.js
    │   │   ├── tsconfig.json
    │   │   ├── vercel.json
    │   │   ├── vite.config.mts
    │   │   ├── .env.sample
    │   │   ├── .eslintrc.mjs
    │   │   ├── .prettierrc.yaml
    │   │   └── src/
    │   │       ├── App.vue
    │   │       ├── config.ts
    │   │       ├── global.ts
    │   │       ├── main.ts
    │   │       ├── MainView.vue
    │   │       ├── style.css
    │   │       ├── vite-env.d.ts
    │   │       ├── components/
    │   │       │   ├── AppDashboard.vue
    │   │       │   ├── AppHeader.vue
    │   │       │   └── AppSettings.vue
    │   │       ├── icons/
    │   │       │   └── index.ts
    │   │       ├── plugins/
    │   │       │   └── iconPlugin.ts
    │   │       ├── services/
    │   │       │   ├── ethHandlers.ts
    │   │       │   ├── solHandlers.ts
    │   │       │   └── walletServiceHandlers.ts
    │   │       ├── store/
    │   │       │   └── form.ts
    │   │       ├── translations/
    │   │       │   ├── en.json
    │   │       │   └── vi.json
    │   │       └── utils/
    │   │           ├── chainconfig.ts
    │   │           ├── constants.ts
    │   │           └── solana.ts
    │   └── wagmi-react-app/
    │       ├── README.md
    │       ├── eslint.config.mjs
    │       ├── index.html
    │       ├── package.json
    │       ├── tsconfig.json
    │       ├── vite-env.d.ts
    │       ├── vite.config.mts
    │       ├── public/
    │       │   ├── manifest.json
    │       │   └── robots.txt
    │       └── src/
    │           ├── App.css
    │           ├── App.tsx
    │           ├── index.css
    │           ├── index.tsx
    │           ├── react-app-env.d.ts
    │           ├── components/
    │           │   └── Main.tsx
    │           └── styles/
    │               └── Home.module.css
    ├── locales/
    │   └── importLocales.mjs
    ├── packages/
    │   ├── modal/
    │   │   ├── README.md
    │   │   ├── babel.config.js
    │   │   ├── eslint.config.mjs
    │   │   ├── package.json
    │   │   ├── postcss.config.js
    │   │   ├── rollup.config.mjs
    │   │   ├── tailwind.config.js
    │   │   ├── torus.config.js
    │   │   ├── tsconfig.build.json
    │   │   ├── tsconfig.json
    │   │   ├── webpack.config.js
    │   │   └── src/
    │   │       ├── config.ts
    │   │       ├── index.ts
    │   │       ├── interface.ts
    │   │       ├── modalManager.ts
    │   │       ├── utils.ts
    │   │       ├── connectors/
    │   │       │   └── coinbase-connector/
    │   │       │       └── index.ts
    │   │       ├── providers/
    │   │       │   ├── ethereum-mpc-provider/
    │   │       │   │   └── index.ts
    │   │       │   └── xrpl-provider/
    │   │       │       └── index.ts
    │   │       ├── react/
    │   │       │   ├── index.ts
    │   │       │   ├── interfaces.ts
    │   │       │   ├── Web3AuthProvider.ts
    │   │       │   ├── context/
    │   │       │   │   ├── WalletServicesInnerContext.ts
    │   │       │   │   └── Web3AuthInnerContext.ts
    │   │       │   ├── hooks/
    │   │       │   │   ├── index.ts
    │   │       │   │   ├── useCheckout.ts
    │   │       │   │   ├── useEnableMFA.ts
    │   │       │   │   ├── useIdentityToken.ts
    │   │       │   │   ├── useManageMFA.ts
    │   │       │   │   ├── useSwap.ts
    │   │       │   │   ├── useSwitchChain.ts
    │   │       │   │   ├── useWalletConnectScanner.ts
    │   │       │   │   ├── useWalletServicesPlugin.ts
    │   │       │   │   ├── useWalletUI.ts
    │   │       │   │   ├── useWeb3Auth.ts
    │   │       │   │   ├── useWeb3AuthConnect.ts
    │   │       │   │   ├── useWeb3AuthDisconnect.ts
    │   │       │   │   ├── useWeb3AuthInner.ts
    │   │       │   │   └── useWeb3AuthUser.ts
    │   │       │   ├── solana/
    │   │       │   │   ├── index.ts
    │   │       │   │   └── hooks/
    │   │       │   │       ├── index.ts
    │   │       │   │       ├── useSignAndSendTransaction.ts
    │   │       │   │       ├── useSignMessage.ts
    │   │       │   │       ├── useSignTransaction.ts
    │   │       │   │       └── useSolanaWallet.ts
    │   │       │   └── wagmi/
    │   │       │       ├── constants.ts
    │   │       │       ├── index.ts
    │   │       │       ├── interface.ts
    │   │       │       └── provider.ts
    │   │       ├── ui/
    │   │       │   ├── config.ts
    │   │       │   ├── constants.ts
    │   │       │   ├── global.d.ts
    │   │       │   ├── index.ts
    │   │       │   ├── interfaces.ts
    │   │       │   ├── localeImport.ts
    │   │       │   ├── loginModal.tsx
    │   │       │   ├── utils.ts
    │   │       │   ├── .eslintrc.json
    │   │       │   ├── components/
    │   │       │   │   ├── BottomSheet/
    │   │       │   │   │   ├── BottomSheet.tsx
    │   │       │   │   │   ├── BottomSheet.type.ts
    │   │       │   │   │   └── index.ts
    │   │       │   │   ├── Button/
    │   │       │   │   │   ├── Button.tsx
    │   │       │   │   │   ├── Button.type.ts
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── ButtonSocial/
    │   │       │   │   │   │   ├── ButtonSocial.tsx
    │   │       │   │   │   │   ├── ButtonSocial.type.ts
    │   │       │   │   │   │   └── index.ts
    │   │       │   │   │   └── ButtonWallet/
    │   │       │   │   │       ├── ButtonWallet.tsx
    │   │       │   │   │       ├── ButtonWallet.type.ts
    │   │       │   │   │       └── index.ts
    │   │       │   │   ├── ConnectWallet/
    │   │       │   │   │   ├── ConnectWallet.tsx
    │   │       │   │   │   ├── ConnectWallet.type.ts
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── ConnectWalletChainFilter/
    │   │       │   │   │   │   ├── ConnectWalletChainFilter.tsx
    │   │       │   │   │   │   ├── ConnectWalletChainFilter.type.ts
    │   │       │   │   │   │   └── index.ts
    │   │       │   │   │   ├── ConnectWalletChainNamespaceSelect/
    │   │       │   │   │   │   ├── ConnectWalletChainNamespaceSelect.tsx
    │   │       │   │   │   │   ├── ConnectWalletChainNamespaceSelect.type.ts
    │   │       │   │   │   │   └── index.ts
    │   │       │   │   │   ├── ConnectWalletHeader/
    │   │       │   │   │   │   ├── ConnectWalletHeader.tsx
    │   │       │   │   │   │   ├── ConnectWalletHeader.type.ts
    │   │       │   │   │   │   └── index.ts
    │   │       │   │   │   ├── ConnectWalletList/
    │   │       │   │   │   │   ├── ConnectWalletList.tsx
    │   │       │   │   │   │   ├── ConnectWalletList.type.ts
    │   │       │   │   │   │   └── index.ts
    │   │       │   │   │   ├── ConnectWalletQrCode/
    │   │       │   │   │   │   ├── ConnectWalletQrCode.tsx
    │   │       │   │   │   │   ├── ConnectWalletQrCode.type.ts
    │   │       │   │   │   │   └── index.ts
    │   │       │   │   │   └── ConnectWalletSearch/
    │   │       │   │   │       ├── ConnectWalletSearch.tsx
    │   │       │   │   │       ├── ConnectWalletSearch.type.ts
    │   │       │   │   │       └── index.ts
    │   │       │   │   ├── Embed/
    │   │       │   │   │   ├── Embed.tsx
    │   │       │   │   │   ├── Embed.type.ts
    │   │       │   │   │   └── index.ts
    │   │       │   │   ├── Footer/
    │   │       │   │   │   ├── Footer.tsx
    │   │       │   │   │   ├── Footer.type.ts
    │   │       │   │   │   └── index.ts
    │   │       │   │   ├── Image/
    │   │       │   │   │   ├── Image.tsx
    │   │       │   │   │   ├── Image.type.ts
    │   │       │   │   │   └── index.ts
    │   │       │   │   ├── Loader/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── Loader.tsx
    │   │       │   │   │   └── Loader.type.ts
    │   │       │   │   ├── Login/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── Login.tsx
    │   │       │   │   │   ├── Login.type.ts
    │   │       │   │   │   ├── LoginOtp/
    │   │       │   │   │   │   ├── index.ts
    │   │       │   │   │   │   ├── LoginOtp.tsx
    │   │       │   │   │   │   └── LoginOtp.type.ts
    │   │       │   │   │   └── LoginPasswordLess/
    │   │       │   │   │       ├── index.ts
    │   │       │   │   │       ├── LoginPasswordLess.tsx
    │   │       │   │   │       └── LoginPasswordLess.type.ts
    │   │       │   │   ├── LoginHint/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── LoginHint.tsx
    │   │       │   │   │   └── LoginHint.type.ts
    │   │       │   │   ├── Modal/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── Modal.tsx
    │   │       │   │   │   └── Modal.type.ts
    │   │       │   │   ├── Otp/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── Otp.tsx
    │   │       │   │   │   └── Otp.type.ts
    │   │       │   │   ├── PulseLoader/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   └── PulseLoader.tsx
    │   │       │   │   ├── Root/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── Root.tsx
    │   │       │   │   │   └── Root.type.ts
    │   │       │   │   ├── SocialLoginList/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   ├── SocialLoginList.tsx
    │   │       │   │   │   └── SocialLoginList.type.ts
    │   │       │   │   ├── Toast/
    │   │       │   │   │   ├── index.ts
    │   │       │   │   │   └── Toast.tsx
    │   │       │   │   └── Widget/
    │   │       │   │       ├── index.ts
    │   │       │   │       ├── Widget.tsx
    │   │       │   │       └── Widget.type.ts
    │   │       │   ├── context/
    │   │       │   │   ├── AnalyticsContext.tsx
    │   │       │   │   ├── RootContext.tsx
    │   │       │   │   └── ThemeContext.tsx
    │   │       │   ├── css/
    │   │       │   │   └── index.css
    │   │       │   ├── handlers/
    │   │       │   │   ├── AbstractHandler.ts
    │   │       │   │   ├── EmailPasswordlessHandler.ts
    │   │       │   │   ├── factory.ts
    │   │       │   │   └── SmsPasswordlessHandler.ts
    │   │       │   ├── helper/
    │   │       │   │   └── countryData.ts
    │   │       │   ├── i18n/
    │   │       │   │   ├── dutch.json
    │   │       │   │   ├── english.json
    │   │       │   │   ├── french.json
    │   │       │   │   ├── german.json
    │   │       │   │   ├── index.ts
    │   │       │   │   ├── japanese.json
    │   │       │   │   ├── korean.json
    │   │       │   │   ├── mandarin.json
    │   │       │   │   ├── portuguese.json
    │   │       │   │   ├── spanish.json
    │   │       │   │   └── turkish.json
    │   │       │   ├── modal/
    │   │       │   │   └── index.html
    │   │       │   └── public/
    │   │       │       └── index.html
    │   │       └── vue/
    │   │           ├── index.ts
    │   │           ├── interfaces.ts
    │   │           ├── WalletServicesInnerProvider.ts
    │   │           ├── Web3AuthProvider.ts
    │   │           ├── composables/
    │   │           │   ├── index.ts
    │   │           │   ├── useCheckout.ts
    │   │           │   ├── useEnableMFA.ts
    │   │           │   ├── useIdentityToken.ts
    │   │           │   ├── useManageMFA.ts
    │   │           │   ├── useSwap.ts
    │   │           │   ├── useSwitchChain.ts
    │   │           │   ├── useWalletConnectScanner.ts
    │   │           │   ├── useWalletServicesPlugin.ts
    │   │           │   ├── useWalletUI.ts
    │   │           │   ├── useWeb3Auth.ts
    │   │           │   ├── useWeb3AuthConnect.ts
    │   │           │   ├── useWeb3AuthDisconnect.ts
    │   │           │   ├── useWeb3AuthInner.ts
    │   │           │   └── useWeb3AuthUser.ts
    │   │           ├── solana/
    │   │           │   ├── index.ts
    │   │           │   └── composables/
    │   │           │       ├── index.ts
    │   │           │       ├── useSignAndSendTransaction.ts
    │   │           │       ├── useSignMessage.ts
    │   │           │       ├── useSignTransaction.ts
    │   │           │       └── useSolanaWallet.ts
    │   │           └── wagmi/
    │   │               ├── constants.ts
    │   │               ├── index.ts
    │   │               ├── interface.ts
    │   │               └── provider.ts
    │   └── no-modal/
    │       ├── package.json
    │       ├── rollup.config.mjs
    │       ├── tsconfig.build.json
    │       ├── tsconfig.json
    │       ├── webpack.config.js
    │       └── src/
    │           ├── index.ts
    │           ├── noModal.ts
    │           ├── base/
    │           │   ├── analytics.ts
    │           │   ├── constants.ts
    │           │   ├── cookie.ts
    │           │   ├── deserialize.ts
    │           │   ├── index.ts
    │           │   ├── interfaces.ts
    │           │   ├── loglevel.ts
    │           │   ├── utils.ts
    │           │   ├── chain/
    │           │   │   └── IChainInterface.ts
    │           │   ├── composables/
    │           │   │   └── index.ts
    │           │   ├── connector/
    │           │   │   ├── baseConnector.ts
    │           │   │   ├── constants.ts
    │           │   │   ├── index.ts
    │           │   │   ├── interfaces.ts
    │           │   │   └── utils.ts
    │           │   ├── core/
    │           │   │   └── IWeb3Auth.ts
    │           │   ├── errors/
    │           │   │   └── index.ts
    │           │   ├── hooks/
    │           │   │   └── index.ts
    │           │   ├── plugin/
    │           │   │   ├── errors.ts
    │           │   │   ├── index.ts
    │           │   │   └── IPlugin.ts
    │           │   ├── provider/
    │           │   │   └── IProvider.ts
    │           │   └── wallet/
    │           │       └── index.ts
    │           ├── connectors/
    │           │   ├── index.ts
    │           │   ├── utils.ts
    │           │   ├── auth-connector/
    │           │   │   ├── authConnector.ts
    │           │   │   ├── index.ts
    │           │   │   └── interface.ts
    │           │   ├── base-evm-connector/
    │           │   │   ├── baseEvmConnector.ts
    │           │   │   └── index.ts
    │           │   ├── base-solana-connector/
    │           │   │   ├── baseSolanaConnector.ts
    │           │   │   └── index.ts
    │           │   ├── coinbase-connector/
    │           │   │   ├── coinbaseConnector.ts
    │           │   │   └── index.ts
    │           │   ├── injected-evm-connector/
    │           │   │   ├── index.ts
    │           │   │   └── injectedEvmConnector.ts
    │           │   ├── injected-solana-connector/
    │           │   │   ├── index.ts
    │           │   │   ├── utils.ts
    │           │   │   └── walletStandardConnector.ts
    │           │   ├── metamask-connector/
    │           │   │   ├── index.ts
    │           │   │   └── metamaskConnector.ts
    │           │   └── wallet-connect-v2-connector/
    │           │       ├── config.ts
    │           │       ├── index.ts
    │           │       ├── interface.ts
    │           │       ├── utils.ts
    │           │       ├── walletConnectV2Connector.ts
    │           │       ├── WalletConnectV2Provider.ts
    │           │       └── walletConnectV2Utils.ts
    │           ├── plugins/
    │           │   ├── index.ts
    │           │   ├── nft-checkout-plugin/
    │           │   │   ├── embed.ts
    │           │   │   ├── enums.ts
    │           │   │   ├── index.ts
    │           │   │   ├── plugin.ts
    │           │   │   └── utils.ts
    │           │   └── wallet-services-plugin/
    │           │       ├── index.ts
    │           │       └── plugin.ts
    │           ├── providers/
    │           │   ├── index.ts
    │           │   ├── account-abstraction-provider/
    │           │   │   ├── index.ts
    │           │   │   ├── providers/
    │           │   │   │   ├── AccountAbstractionProvider.ts
    │           │   │   │   ├── index.ts
    │           │   │   │   ├── utils.ts
    │           │   │   │   └── smartAccounts/
    │           │   │   │       └── index.ts
    │           │   │   └── rpc/
    │           │   │       ├── ethRpcMiddlewares.ts
    │           │   │       └── index.ts
    │           │   ├── base-provider/
    │           │   │   ├── baseProvider.ts
    │           │   │   ├── CommonJRPCProvider.ts
    │           │   │   ├── commonPrivateKeyProvider.ts
    │           │   │   ├── index.ts
    │           │   │   ├── interfaces.ts
    │           │   │   ├── jrpcClient.ts
    │           │   │   └── utils.ts
    │           │   ├── ethereum-mpc-provider/
    │           │   │   ├── index.ts
    │           │   │   ├── providers/
    │           │   │   │   ├── index.ts
    │           │   │   │   └── signingProviders/
    │           │   │   │       ├── EthereumSigningProvider.ts
    │           │   │   │       ├── index.ts
    │           │   │   │       └── signingUtils.ts
    │           │   │   └── rpc/
    │           │   │       ├── ethRpcMiddlewares.ts
    │           │   │       └── interfaces.ts
    │           │   ├── ethereum-provider/
    │           │   │   ├── index.ts
    │           │   │   ├── providers/
    │           │   │   │   ├── converter.ts
    │           │   │   │   ├── index.ts
    │           │   │   │   ├── utils.ts
    │           │   │   │   └── privateKeyProviders/
    │           │   │   │       ├── index.ts
    │           │   │   │       └── TransactionFormatter/
    │           │   │   │           ├── constants.ts
    │           │   │   │           ├── formatter.ts
    │           │   │   │           ├── index.ts
    │           │   │   │           ├── interfaces.ts
    │           │   │   │           └── utils.ts
    │           │   │   └── rpc/
    │           │   │       ├── ethRpcMiddlewares.ts
    │           │   │       ├── index.ts
    │           │   │       ├── interfaces.ts
    │           │   │       ├── jrpcClient.ts
    │           │   │       └── walletMidddleware.ts
    │           │   ├── solana-provider/
    │           │   │   ├── index.ts
    │           │   │   ├── interface.ts
    │           │   │   ├── solanaWallet.ts
    │           │   │   ├── providers/
    │           │   │   │   ├── index.ts
    │           │   │   │   └── injectedProviders/
    │           │   │   │       ├── index.ts
    │           │   │   │       ├── utils.ts
    │           │   │   │       ├── walletStandardProvider.ts
    │           │   │   │       └── base/
    │           │   │   │           ├── baseInjectedProvider.ts
    │           │   │   │           └── providerHandlers.ts
    │           │   │   └── rpc/
    │           │   │       ├── index.ts
    │           │   │       ├── interfaces.ts
    │           │   │       ├── JrpcClient.ts
    │           │   │       └── solanaRpcMiddlewares.ts
    │           │   └── xrpl-provider/
    │           │       ├── index.ts
    │           │       ├── providers/
    │           │       │   ├── index.ts
    │           │       │   └── privateKeyProviders/
    │           │       │       ├── constants.ts
    │           │       │       ├── index.ts
    │           │       │       ├── interface.ts
    │           │       │       ├── xrplPrivateKeyProvider.ts
    │           │       │       └── xrplWalletUtils.ts
    │           │       └── rpc/
    │           │           ├── JrpcClient.ts
    │           │           └── xrplRpcMiddlewares.ts
    │           ├── react/
    │           │   ├── index.ts
    │           │   ├── interfaces.ts
    │           │   ├── Web3AuthProvider.ts
    │           │   ├── context/
    │           │   │   ├── WalletServicesInnerContext.ts
    │           │   │   └── Web3AuthInnerContext.ts
    │           │   ├── hooks/
    │           │   │   ├── index.ts
    │           │   │   ├── useCheckout.ts
    │           │   │   ├── useEnableMFA.ts
    │           │   │   ├── useIdentityToken.ts
    │           │   │   ├── useManageMFA.ts
    │           │   │   ├── useSwap.ts
    │           │   │   ├── useSwitchChain.ts
    │           │   │   ├── useWalletConnectScanner.ts
    │           │   │   ├── useWalletServicesPlugin.ts
    │           │   │   ├── useWalletUI.ts
    │           │   │   ├── useWeb3Auth.ts
    │           │   │   ├── useWeb3AuthConnect.ts
    │           │   │   ├── useWeb3AuthDisconnect.ts
    │           │   │   ├── useWeb3AuthInner.ts
    │           │   │   └── useWeb3AuthUser.ts
    │           │   ├── solana/
    │           │   │   ├── index.ts
    │           │   │   └── hooks/
    │           │   │       ├── index.ts
    │           │   │       ├── useSignAndSendTransaction.ts
    │           │   │       ├── useSignMessage.ts
    │           │   │       ├── useSignTransaction.ts
    │           │   │       └── useSolanaWallet.ts
    │           │   └── wagmi/
    │           │       ├── constants.ts
    │           │       ├── index.ts
    │           │       ├── interface.ts
    │           │       └── provider.ts
    │           └── vue/
    │               ├── index.ts
    │               ├── interfaces.ts
    │               ├── WalletServicesInnerProvider.ts
    │               ├── Web3AuthProvider.ts
    │               ├── composables/
    │               │   ├── index.ts
    │               │   ├── useCheckout.ts
    │               │   ├── useEnableMFA.ts
    │               │   ├── useIdentityToken.ts
    │               │   ├── useManageMFA.ts
    │               │   ├── useSwap.ts
    │               │   ├── useSwitchChain.ts
    │               │   ├── useWalletConnectScanner.ts
    │               │   ├── useWalletServicesPlugin.ts
    │               │   ├── useWalletUI.ts
    │               │   ├── useWeb3Auth.ts
    │               │   ├── useWeb3AuthConnect.ts
    │               │   ├── useWeb3AuthDisconnect.ts
    │               │   ├── useWeb3AuthInner.ts
    │               │   └── useWeb3AuthUser.ts
    │               ├── context/
    │               │   ├── index.ts
    │               │   └── WalletServicesContext.ts
    │               ├── solana/
    │               │   ├── index.ts
    │               │   └── composables/
    │               │       ├── index.ts
    │               │       ├── useSignAndSendTransaction.ts
    │               │       ├── useSignMessage.ts
    │               │       ├── useSignTransaction.ts
    │               │       └── useSolanaWallet.ts
    │               └── wagmi/
    │                   ├── constants.ts
    │                   ├── index.ts
    │                   ├── interface.ts
    │                   └── provider.ts
    ├── scripts/
    │   ├── create-final-registry.js
    │   ├── create-web3-json.js
    │   ├── download-img.js
    │   ├── wallet-registry-updated.json
    │   ├── wallet-registry-wc.json
    │   ├── wallet-registry-web3auth-new.json
    │   ├── wallet-registry-web3auth-old.json
    │   ├── wallet-registry-web3auth-prod.json
    │   └── wallet-registry-web3auth.json
    ├── test/
    │   └── setup.mjs
    └── .github/
        ├── dependabot.yml
        ├── .stale.yml
        ├── ISSUE_TEMPLATE/
        │   ├── bug_report.md
        │   └── feature_request.md
        ├── PULL_REQUEST_TEMPLATE/
        │   ├── bug_fix.md
        │   └── feature.md
        └── workflows/
            └── ci.yml


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
# Web3Auth

[![lerna](https://img.shields.io/badge/maintained%20with-lerna-cc00ff.svg)](https://lerna.js.org/)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
![npm](https://img.shields.io/npm/dw/@web3auth/modal)

Web3Auth is where passwordless auth meets non-custodial key infrastructure for Web3 apps and wallets. By aggregating OAuth (Google, Twitter, Discord) logins, different wallets and innovative Multi Party Computation (MPC) - Web3Auth provides a seamless login experience to every user on your application.

## 📖 Documentation

Checkout the official [Web3Auth Documentation](https://web3auth.io/docs) and [SDK Reference](https://web3auth.io/docs/sdk/web/) to get started!

## 💡 Features

- Plug and Play, OAuth based Web3 Authentication Service
- Fully decentralized, non-custodial key infrastructure
- End to end Whitelabelable solution
- Threshold Cryptography based Key Reconstruction
- Multi Factor Authentication Setup & Recovery (Includes password, backup phrase, device factor editing/deletion etc)
- Support for Email and Mobile Passwordless Login
- Support for connecting to multiple wallets
- DApp Active Session Management

  ...and a lot more

## 🎯 Web3Auth Modal SDK

[Web3Auth Plug and Play Modal SDK `@web3auth/modal`](https://web3auth.io/docs/sdk/web/web3auth/) provides a simple and easy to use SDK that will give you a simple modular way of implementing Web3Auth directly within your application. You can use the pre-configured Web3Auth Modal UI and whitelabel it according to your needs.

## ⚡ Quick Start

### Installation

```shell
npm install --save @web3auth/modal
```

### Prerequisites

Before you start, make sure you have registered on the [Web3Auth Dashboard](https://dashboard.web3auth.io/) and have set up your project. Use the Client ID of the project to start your integration.

### React Integration

Web3Auth provides React Hooks for seamless integration with React applications.

#### 1. Create Configuration

```tsx
// web3authContext.tsx
import { type Web3AuthContextConfig } from "@web3auth/modal/react";
import { WEB3AUTH_NETWORK, type Web3AuthOptions } from "@web3auth/modal";

const web3AuthOptions: Web3AuthOptions = {
  clientId: "YOUR_CLIENT_ID", // Get your Client ID from Web3Auth Dashboard
  web3AuthNetwork: WEB3AUTH_NETWORK.SAPPHIRE_MAINNET, // or WEB3AUTH_NETWORK.SAPPHIRE_DEVNET
};

const web3AuthContextConfig: Web3AuthContextConfig = {
  web3AuthOptions,
};

export default web3AuthContextConfig;
```

#### 2. Setup Provider

```tsx
// main.tsx or index.tsx
import ReactDOM from "react-dom/client";
import { Web3AuthProvider } from "@web3auth/modal/react";
import web3AuthContextConfig from "./web3authContext";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <Web3AuthProvider config={web3AuthContextConfig}>
    <App />
  </Web3AuthProvider>
);
```

#### 3. Use Web3Auth Hooks

```tsx
// App.tsx
import { useWeb3AuthConnect } from "@web3auth/modal/react";

function ConnectButton() {
  const { connect, loading, isConnected, error } = useWeb3AuthConnect();

  return (
    <button onClick={() => connect()} disabled={loading || isConnected}>
      {loading ? "Connecting..." : isConnected ? "Connected" : "Connect"}
    </button>
    {error && <div>{error.message}</div>}
  );
}
```

### Vue Integration

Web3Auth provides Vue Composables for seamless integration with Vue applications.

#### 1. Create Configuration

```ts
// web3authContext.ts
import { type Web3AuthContextConfig } from "@web3auth/modal/vue";
import { WEB3AUTH_NETWORK, type Web3AuthOptions } from "@web3auth/modal";

const web3AuthOptions: Web3AuthOptions = {
  clientId: "YOUR_CLIENT_ID", // Get your Client ID from Web3Auth Dashboard
  web3AuthNetwork: WEB3AUTH_NETWORK.SAPPHIRE_MAINNET, // or WEB3AUTH_NETWORK.SAPPHIRE_DEVNET
};

const web3AuthContextConfig: Web3AuthContextConfig = {
  web3AuthOptions,
};

export default web3AuthContextConfig;
```

#### 2. Setup Provider

```html
<!-- App.vue -->
<script setup lang="ts">
import Home from "./Home.vue";
import { Web3AuthProvider } from "@web3auth/modal/vue";
import web3AuthContextConfig from "./web3authContext";
</script>

<template>
  <Web3AuthProvider :config="web3AuthContextConfig">
    <Home />
  </Web3AuthProvider>
</template>
```

#### 3. Use Web3Auth Composables

```html
<!-- Home.vue -->
<script setup lang="ts">
  import { useWeb3AuthConnect } from "@web3auth/modal/vue";

  const { connect, loading, isConnected, error } = useWeb3AuthConnect();
</script>

<template>
  <button @click="connect" :disabled="loading || isConnected">
    <span v-if="loading">Connecting...</span>
    <span v-else-if="isConnected">Connected</span>
    <span v-else>Connect</span>
  </button>
  <div v-if="error">{{ error.message }}</div>
</template>
```

### JavaScript Integration

For vanilla JavaScript or other frameworks, use the standard Web3Auth Modal SDK.

#### 1. Initialize Web3Auth

```javascript
import { Web3Auth, WEB3AUTH_NETWORK } from "@web3auth/modal";

const web3auth = new Web3Auth({
  clientId: "YOUR_CLIENT_ID", // Get your Client ID from Web3Auth Dashboard
  web3AuthNetwork: WEB3AUTH_NETWORK.SAPPHIRE_MAINNET, // or WEB3AUTH_NETWORK.SAPPHIRE_DEVNET
});

// Initialize the SDK
await web3auth.init();
```

#### 2. Login User

```javascript
// Login
await web3auth.connect();

// Get user info
const user = await web3auth.getUserInfo();

// Logout
await web3auth.logout();
```

## 🔧 Advanced Configuration

The Web3Auth Modal SDK offers a rich set of advanced configuration options:

- **Smart Accounts**: Configure account abstraction parameters
- **Custom Authentication**: Define authentication methods
- **Whitelabeling & UI Customization**: Personalize the modal's appearance
- **Multi-Factor Authentication (MFA)**: Set up and manage MFA
- **Wallet Services**: Integrate additional wallet services

## ⏪ Requirements

- All packages require a peer dependency of `@babel/runtime`
- Node 18+

## 🧳 Bundling

This module is distributed in 4 formats

- `esm` build `dist/package.esm.js` in es6 format
- `commonjs` build `dist/package.cjs.js` in es5 format
- `umd` build `dist/package.umd.min.js` in es5 format without polyfilling corejs minified

By default, the appropriate format is used for your specified usecase
You can use a different format (if you know what you're doing) by referencing the correct file

The cjs build is not polyfilled with core-js.
It is upto the user to polyfill based on the browserlist they target

### Directly in Browser

CDN's serve the non-core-js polyfilled version by default. You can use a different

Please replace package and version with the appropriate package name

#### `jsdeliver`

```js
<script src="https://cdn.jsdelivr.net/npm/@web3auth/PACKAGE@VERSION"></script>
```

#### `unpkg`

```js
<script src="https://unpkg.com/@web3auth/PACKAGE@VERSION"></script>
```

## 🩹 Examples

Check out the examples for your preferred blockchain and platform on our [examples page](https://web3auth.io/docs/examples).

## 🌐 Demo

Checkout the [Web3Auth Demo](https://demo.web3auth.io) to see how Web3Auth can be used in your application.

For more detailed examples, visit our [Web3Auth Examples repository](https://github.com/Web3Auth/web3auth-examples/). This repository contains a comprehensive collection of sample projects to help you get started with your Web3Auth integration.

## 💬 Troubleshooting and Support

- Have a look at our [Community Portal](https://community.web3auth.io/) to see if anyone has any questions or issues you might be having. Feel free to create new topics and we'll help you out as soon as possible.
- Checkout our [Troubleshooting Documentation Page](https://web3auth.io/docs/troubleshooting) to know the common issues and solutions.
- For Priority Support, please have a look at our [Pricing Page](https://web3auth.io/pricing.html) for the plan that suits your needs.




================================================
FILE: babel.config.js
================================================
module.exports = require("@toruslabs/config/babel.config");



================================================
FILE: eslint.config.mjs
================================================
import toruslabsTypescript from "@toruslabs/eslint-config-typescript";

export default [
  ...toruslabsTypescript,
  {
    files: ["packages/no-modal/src/react/wagmi/**.ts", "packages/no-modal/src/vue/wagmi/**.ts"],
    rules: {
      "import/no-extraneous-dependencies": "off",
    },
  },
];



================================================
FILE: lerna.json
================================================
{
  "version": "10.0.5",
  "npmClient": "npm"
}



================================================
FILE: LICENSE
================================================
Copyright Torus Labs Private Limited 2023. All rights reserved.

You acknowledge and agree that Torus Labs Private Limited (Web3Auth) (or Web3Auth's licensors) own all legal rights, titles and interests in and to the work, software, application, source code, documentation and any other documents in this repository (collectively, the “Program”), including any intellectual property rights which subsist in the Program (whether those rights happen to be registered or not, and wherever in the world those rights may exist), whether in source code or any other form.

Subject to the limited license below, you may not (and you may not permit anyone else to) distribute, publish, copy, modify, merge, combine with another program, create derivative works of, reverse engineer, decompile or otherwise attempt to extract the source code of, the Program or any part thereof, except that you may contribute to this repository.

You are granted a non-exclusive, non-transferable, non-sublicensable license to distribute, publish, copy, modify, merge, combine with another program or create derivative works of the Program (such resulting program, collectively, the “Resulting Program”) solely for Non-Commercial Use as long as you:

1.  give prominent notice (“Notice”) with each copy of the Resulting Program that the Program is used in the Resulting Program and that the Program is the copyright of Web3Auth; and
2.  subject the Resulting Program and any distribution, publication, copy, modification, merger therewith, combination with another program or derivative works thereof to the same Notice requirement and Non-Commercial Use restriction set forth herein.

“Non-Commercial Use” means each use as described in clauses (1)-(3) below, as reasonably determined by Web3Auth in its sole discretion:

1.  personal use for research, personal study, private entertainment, hobby projects or amateur pursuits, in each case without any anticipated commercial application;
2.  use by any charitable organization, educational institution, public research organization, public safety or health organization, environmental protection organization or government institution; or
3.  the number of monthly active users of the Resulting Program across all versions thereof and platforms globally do not exceed 1,000 at any time.

You will not use any trade mark, service mark, trade name, logo of Web3Auth or any other company or organization in a way that is likely or intended to cause confusion about the owner or authorized user of such marks, names or logos.

If you have any questions, comments or interest in pursuing any other use cases, please reach out to us at hello@tor.us.



================================================
FILE: package.json
================================================
{
  "author": "Torus Labs",
  "bugs": {
    "url": "https://github.com/Web3Auth/Web3Auth/issues"
  },
  "description": "Monorepo for web3 auth packages",
  "devDependencies": {
    "@babel/register": "^7.27.1",
    "@rollup/plugin-node-resolve": "^16.0.1",
    "@toruslabs/config": "^3.1.0",
    "@toruslabs/eslint-config-typescript": "^4.1.4",
    "@toruslabs/torus-scripts": "^7.1.6",
    "@types/chai": "^5.2.2",
    "@types/mocha": "^10.0.10",
    "@types/node": "^22",
    "chai": "^5.2.0",
    "cross-env": "^7.0.3",
    "dotenv": "^16.5.0",
    "eslint": "^9.29.0",
    "eslint-import-resolver-typescript": "^4.4.3",
    "husky": "^9.1.7",
    "lerna": "^8.2.2",
    "lint-staged": "^16.1.2",
    "mocha": "^11.7.0",
    "prettier": "^3.5.3",
    "rimraf": "^6.0.1",
    "ts-node": "^10.9.2",
    "ts-patch": "^3.3.0",
    "tsconfig-paths": "^4.2.0",
    "tsconfig-paths-webpack-plugin": "^4.2.0",
    "typescript": "~5.8.3",
    "typescript-transform-paths": "^3.5.5"
  },
  "engines": {
    "node": ">=20.x",
    "npm": ">=9.x"
  },
  "homepage": "https://github.com/Web3Auth/Web3Auth#readme",
  "keywords": [
    "aggregator",
    "authentication",
    "blockchain",
    "ethereum",
    "key management",
    "login",
    "solana",
    "wallet",
    "web3"
  ],
  "license": "ISC",
  "lint-staged": {
    "*": "lerna run --concurrency 1 --stream --since HEAD --exclude-dependents pre-commit -- "
  },
  "name": "web3auth",
  "optionalDependencies": {
    "@nx/nx-linux-x64-gnu": "^21.2.0",
    "@rollup/rollup-linux-x64-gnu": "^4.43.0"
  },
  "private": true,
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Web3Auth/Web3Auth.git"
  },
  "scripts": {
    "build": "cross-env FORCE_COLOR=1 lerna run --stream build",
    "clean": "lerna clean --yes && lerna exec -- rimraf package-lock.json .rollup.cache/ tsconfig.build.tsbuildinfo yarn.lock dist/ .rts2_cache_{cjs,esm}/ web3auth-*.tgz .eslintcache",
    "dev": "lerna run dev --parallel",
    "just:publish:lerna": "lerna publish",
    "lint": "cross-env FORCE_COLOR=1 lerna run lint --parallel",
    "locale": "node locales/importLocales.mjs",
    "pack:lerna": "lerna exec 'npm pack'",
    "pre-commit": "lerna run pre-commit",
    "prepare": "husky",
    "publish:lerna": "npm run clean && npm install && lerna publish",
    "test": "cross-env FORCE_COLOR=1 lerna run test --parallel",
    "test-debugger": "cross-env FORCE_COLOR=1 lerna run test-debugger --parallel"
  },
  "workspaces": [
    "packages/no-modal",
    "packages/modal"
  ],
  "overrides": {
    "ox": "0.6.9",
    "react": "19.1.0",
    "react-dom": "19.1.0"
  }
}



================================================
FILE: torus.config.js
================================================
module.exports = require("@toruslabs/config/torus.config");



================================================
FILE: tsconfig.json
================================================
{
  "extends": "@toruslabs/config/tsconfig.default.json",
  "compilerOptions": {
    "paths": {
      "@web3auth/modal": ["./packages/modal"],
      "@web3auth/no-modal": ["./packages/no-modal"]
    }
  }
}



================================================
FILE: webpack.config.js
================================================
const TsconfigPathsPlugin = require("tsconfig-paths-webpack-plugin");

function generateWebpackConfig({ alias, module = {}, pkgBaseConfig = {}, plugins = [] }) {
  const baseConfig = {
    ...pkgBaseConfig,
    resolve: {
      plugins: [new TsconfigPathsPlugin()],
      alias: {
        "bn.js": require.resolve("bn.js"),
        tweetnacl: require.resolve("@toruslabs/tweetnacl-js"),
        ...alias,
      },
    },
  };

  const config = { baseConfig };
  config.umdConfig = {
    module,
    plugins,
  };

  return config;
}

module.exports = generateWebpackConfig;



================================================
FILE: .browserslistrc
================================================
supports bigint
not dead


================================================
FILE: .mocharc.json
================================================
{
  "loader": "ts-node/esm/transpile-only",
  "extension": ["ts", "js"],
  "require": ["../../test/setup.mjs"],
  "timeout": 0,
  "exit": true
}



================================================
FILE: .npmignore
================================================
# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
lerna-debug.log*

# Diagnostic reports (https://nodejs.org/api/report.html)
report.[0-9]*.[0-9]*.[0-9]*.[0-9]*.json

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage
*.lcov

# nyc test coverage
.nyc_output

# Grunt intermediate storage (https://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (https://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# TypeScript v1 declaration files
typings/

# TypeScript cache
*.tsbuildinfo

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Microbundle cache
.rpt2_cache/
.rts2_cache_cjs/
.rts2_cache_es/
.rts2_cache_umd/

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variables file
.env
.env.test

# parcel-bundler cache (https://parceljs.org/)
.cache

# Next.js build output
.next

# Nuxt.js build / generate output
.nuxt

# Gatsby files
.cache/
# Comment in the public line in if your project uses Gatsby and *not* Next.js
# https://nextjs.org/blog/next-9-1#public-directory-support
# public

# Serverless directories
.serverless/

# FuseBox cache
.fusebox/

# DynamoDB Local files
.dynamodb/

# TernJS port file
.tern-port


examples/
ssl/
src/
scripts/
.eslintrc.json
.eslintignore
.prettierignore
.prettierrc.yaml
.babelrc


================================================
FILE: .nvmrc
================================================
>=18.x


================================================
FILE: .prettierignore
================================================
# See https://help.github.com/ignore-files/ for more about ignoring files.

# dependencies
/node_modules

# testing
/coverage

#production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*
/packages/*/types


================================================
FILE: .prettierrc.yaml
================================================
# .prettierrc or .prettierrc.yaml
printWidth: 150
singleQuote: false
semi: true
trailingComma: es5



================================================
FILE: demo/nextjs-ssr-app/README.md
================================================
# Web3Auth (`@web3auth/modal`) x EVM x Next.js

[![Web3Auth](https://img.shields.io/badge/Web3Auth-SDK-blue)](https://web3auth.io/docs/sdk/pnp/web/modal)
[![Web3Auth](https://img.shields.io/badge/Web3Auth-Community-cyan)](https://community.web3auth.io)

[Join our Community Portal](https://community.web3auth.io/) to get support and stay up to date with the latest news and updates.

This example demonstrates how to use Web3Auth with EVM in Next.js

## How to Use

### One-Click Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FWeb3Auth%2Fweb3auth-pnp-examples%2Ftree%2Fmain%2Fweb-modal-sdk%2Fquick-starts%2Fnextjs-modal-quick-start&project-name=w3a-nextjs-modal&repository-name=w3a-nextjs-modal)

### Download Manually

```bash
npx degit Web3Auth/web3auth-pnp-examples/web-no-modal-sdk/quick-starts/nextjs-no-modal-quick-start w3a-example
```

Install & Run:

```bash
cd w3a-example
npm install
npm run dev
# or
cd w3a-example
yarn
yarn dev
```

## Important Links

- [Website](https://web3auth.io)
- [Docs](https://web3auth.io/docs)
- [Guides](https://web3auth.io/docs/guides)
- [SDK / API References](https://web3auth.io/docs/sdk)
- [Pricing](https://web3auth.io/pricing.html)
- [Community Portal](https://community.web3auth.io)



================================================
FILE: demo/nextjs-ssr-app/next-env.d.ts
================================================
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/basic-features/typescript for more information.



================================================
FILE: demo/nextjs-ssr-app/next.config.js
================================================
const path = require('path')

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  webpack: (config) => {
    config.resolve.alias = {
      ...(config.resolve.alias || {}),
      wagmi: path.resolve(__dirname, 'node_modules/wagmi'),
    };
    return config;
  },
}
  
module.exports = nextConfig



================================================
FILE: demo/nextjs-ssr-app/package.json
================================================
{
  "name": "nextjs-ssr-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@tanstack/react-query": "^5.80.7",
    "@web3auth/modal": "../../packages/modal",
    "next": "14.1.0",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "wagmi": "^2.15.6"
  },
  "devDependencies": {
    "@types/elliptic": "^6.4.18",
    "@types/node": "20.4.1",
    "@types/react": "19.1.8",
    "@types/react-dom": "19.1.6",
    "@wagmi/core": "^2.17.3",
    "eslint": "8.44.0",
    "eslint-config-next": "13.4.9",
    "typescript": "5.1.6"
  }
}



================================================
FILE: demo/nextjs-ssr-app/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}



================================================
FILE: demo/nextjs-ssr-app/.eslintrc.json
================================================
{
  "extends": "next/core-web-vitals",
  "ignorePatterns": ["*.config.js"]
}



================================================
FILE: demo/nextjs-ssr-app/app/globals.css
================================================
.container {
  width: 60%;
  margin: auto;
  padding: 0 2rem;
}

.main {
  min-height: 100vh;
  padding: 4rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  line-height: 1.15;
  font-size: 3rem;
  text-align: center;
  margin: 50px;
}

.title a {
  color: #0070f3;
  text-decoration: none;
}

.console {
  max-width: 100%;
}

.code {
  background: #fafafa;
  border-radius: 5px;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace;
  overflow-wrap: break-word;
}

.grid {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.setting {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 20px;
  margin: 30px 0;
  background: #f4f5f7;
  border: 1px solid #ebecf0;
  border-radius: 5px;
}

.card {
  margin: 0.5rem;
  padding: 0.7rem;
  text-align: center;
  color: #0070f3;
  text-decoration: none;
  border: 1px solid #0070f3;
  border-radius: 10px;
  transition: color 0.15s ease, border-color 0.15s ease;
  width: 100%;
}

.card:hover,
.card:focus,
.card:active {
  cursor: pointer;
  background-color: #fafafa;
}

.row {
  display: flex;
  margin-bottom: 0.5rem;
  width: 100%;
}
.label {
  flex-basis: 45%;
  padding-right: 10px;
  display: flex;
  align-items: center;
  justify-content: right;
  font-weight: bold;
}

.select {
  flex-basis: 30%;
  text-align: left;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  border-radius: 8px;
}

.footer {
  display: flex;
  flex: 1;
  padding: 2rem 0;
  border-top: 1px solid #eaeaea;
  justify-content: center;
  align-items: center;
  margin-top: 10rem;
}

.footer a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.logo {
  height: 1.5rem;
  margin-left: 0.5rem;
}

/* @media (max-width: 1200px) {
  .container {
    width: 100%;
  }
} */



================================================
FILE: demo/nextjs-ssr-app/app/layout.tsx
================================================
import "./globals.css";

import { Inter } from "next/font/google";

import Provider from "@/components/provider";
import { cookieToWeb3AuthState } from "@web3auth/modal";
import { headers } from "next/headers";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Web3Auth NextJS Quick Start",
  description: "Web3Auth NextJS Quick Start",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const web3authInitialState = cookieToWeb3AuthState((headers()).get('cookie'))
  console.log("web3authInitialState", web3authInitialState)
  return (
    <html lang="en">
      <body className={inter.className}>
        <Provider web3authInitialState={web3authInitialState}>{children}</Provider>
      </body>
    </html>
  );
}



================================================
FILE: demo/nextjs-ssr-app/app/page.tsx
================================================
"use client";

import Main from "@/components/Main";

export default function Home() {
  return <Main />
}



================================================
FILE: demo/nextjs-ssr-app/components/Main.tsx
================================================
"use client";

import {
  useCheckout,
  useEnableMFA,
  useIdentityToken,
  useManageMFA,
  useWalletConnectScanner,
  useWalletUI,
  useWeb3Auth,
  useWeb3AuthConnect,
  useWeb3AuthDisconnect,
  useWeb3AuthUser,
} from "@web3auth/modal/react";
import { useAccount, useBalance, useChainId, useSignMessage, useSignTypedData, useSwitchChain } from "wagmi";

const Main = () => {
  const { provider, isConnected } = useWeb3Auth();
  const { chains, switchChain } = useSwitchChain();
  const chainId = useChainId();
  const { loading: connecting, connect, error: connectingError, connectorName } = useWeb3AuthConnect();
  const { disconnect } = useWeb3AuthDisconnect();
  const { signMessageAsync, data: signedMessageData } = useSignMessage();
  const { address, isConnected: isWagmiConnected } = useAccount();
  const { userInfo, isMFAEnabled } = useWeb3AuthUser();
  const { data: balance } = useBalance({ address });
  const { signTypedData, data: signedTypedDataData } = useSignTypedData();
  const { enableMFA, loading: isEnableMFALoading, error: enableMFAError } = useEnableMFA();
  const { manageMFA, loading: isManageMFALoading, error: manageMFAError } = useManageMFA();
  const { showCheckout, loading: isCheckoutLoading, error: checkoutError } = useCheckout();
  const { showWalletConnectScanner, loading: isWalletConnectScannerLoading, error: walletConnectScannerError } = useWalletConnectScanner();
  const { showWalletUI, loading: isWalletUILoading, error: walletUIError } = useWalletUI();
  const { token, loading: isUserTokenLoading, error: userTokenError, getIdentityToken } = useIdentityToken();

  console.log("isConnected", isConnected, balance);

  const loggedInView = (
    <>
      <div className="container">
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          {/* <p>Account Address: {address}</p> */}
          {/* <p>Account Balance: {balance?.value}</p> */}
          <p>MFA Enabled: {isMFAEnabled ? "Yes" : "No"}</p>
        </div>

        {/* User Info */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>User Info</p>
          <textarea disabled rows={5} value={JSON.stringify(userInfo, null, 2)} style={{ width: "100%" }} />
        </div>

        {/* User Token */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>User Token</p>
          {token && <textarea disabled rows={5} value={token} style={{ width: "100%" }} />}
          {!token && (
            <>
              {isUserTokenLoading ? (
                <p>Authenticating...</p>
              ) : (
                <button onClick={() => getIdentityToken()} className="card">
                  Authenticate User
                </button>
              )}
            </>
          )}
          {userTokenError && <p>Error: {userTokenError.message}</p>}
        </div>

        {/* MFA */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>MFA</p>
          {isMFAEnabled ? (
            <>
              {isManageMFALoading ? (
                <p>Managing MFA...</p>
              ) : (
                <button onClick={() => manageMFA()} className="card">
                  Manage MFA
                </button>
              )}
              {manageMFAError && <p>Error: {manageMFAError.message}</p>}
            </>
          ) : (
            <>
              {isEnableMFALoading ? (
                <p>Enabling MFA...</p>
              ) : (
                <button onClick={() => enableMFA()} className="card">
                  Enable MFA
                </button>
              )}
              {enableMFAError && <p>Error: {enableMFAError.message}</p>}
            </>
          )}
        </div>

        {/* Checkout */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Checkout</p>
          {isCheckoutLoading ? (
            <p>Checking out...</p>
          ) : (
            <button onClick={() => showCheckout()} className="card">
              Checkout
            </button>
          )}
          {checkoutError && <p>Error: {checkoutError.message}</p>}
        </div>

        {/* Wallet Connect Scanner */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Wallet Connect Scanner</p>
          {isWalletConnectScannerLoading ? (
            <p>Scanning...</p>
          ) : (
            <button onClick={() => showWalletConnectScanner()} className="card">
              Scan
            </button>
          )}
          {walletConnectScannerError && <p>Error: {walletConnectScannerError.message}</p>}
        </div>

        {/* Wallet UI */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Wallet UI</p>
          {isWalletUILoading ? (
            <p>Loading...</p>
          ) : (
            <button onClick={() => showWalletUI()} className="card">
              Wallet UI
            </button>
          )}
          {walletUIError && <p>Error: {walletUIError.message}</p>}
        </div>

        {/* Provider Actions */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Provider Actions</p>
          {/* Sign Message */}
          <button onClick={() => signMessageAsync({ message: "Hello, world!" })} className="card">
            Sign Message
          </button>
          {signedMessageData && <textarea disabled rows={5} value={signedMessageData} style={{ width: "100%" }} />}

          {/* Sign Typed Data */}
          <button
            onClick={() =>
              signTypedData({
                types: {
                  Person: [
                    { name: "name", type: "string" },
                    { name: "wallet", type: "address" },
                  ],
                  Mail: [
                    { name: "from", type: "Person" },
                    { name: "to", type: "Person" },
                    { name: "contents", type: "string" },
                  ],
                },
                primaryType: "Mail",
                message: {
                  from: {
                    name: "Cow",
                    wallet: "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826",
                  },
                  to: {
                    name: "Bob",
                    wallet: "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB",
                  },
                  contents: "Hello, Bob!",
                },
              })
            }
            className="card"
          >
            Sign Typed Data
          </button>
          {signedTypedDataData && <textarea disabled rows={5} value={signedTypedDataData} style={{ width: "100%" }} />}
        </div>

        {/* Switch Chain */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Switch Chain</p>
          {chains.map((chain) => (
            <button
              key={chain.id}
              disabled={chain.id === chainId}
              onClick={() => switchChain({ chainId: chain.id })}
              style={{ opacity: chain.id === chainId ? 0.5 : 1 }}
              className="card"
            >
              {chain.name}
            </button>
          ))}
        </div>

        {/* Disconnect */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Logout</p>
          <button onClick={() => disconnect()} className="card">
            Disconnect
          </button>
        </div>
      </div>
    </>
  );

  const unloggedInView = (
    <>
      {connecting ? (
        <p>Connecting to {connectorName}...</p>
      ) : (
        <button onClick={() => connect()} className="card">
          Login
        </button>
      )}
      {connectingError && <p>Error: {connectingError.message}</p>}
    </>
  );

  return (
    <div className="grid">
      <p>Web3Auth: {isConnected ? "Connected" : "Disconnected"}</p>
      <p>Wagmi: {isWagmiConnected ? "Connected" : "Disconnected"}</p>
      {provider ? loggedInView : unloggedInView}
    </div>
  );
};

export default Main;



================================================
FILE: demo/nextjs-ssr-app/components/provider.tsx
================================================
"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { IWeb3AuthState } from "@web3auth/modal";
import { type Web3AuthContextConfig } from "@web3auth/modal/react";
import { Web3AuthProvider } from "@web3auth/modal/react";
import { WagmiProvider } from "@web3auth/modal/react/wagmi";

const queryClient = new QueryClient();
const clientId = "BMjGyXu-SceWBNiPxfQK6qRlnVOzYLX5YNgI8yrgd1F9_pfAWyMUWfyt2Yr45CYlOs92cJh0C02M2hJonVb_zC0";

const web3authConfig: Web3AuthContextConfig = {
  web3AuthOptions: {
    enableLogging: true,
    web3AuthNetwork: "sapphire_devnet",
    clientId: clientId,
    ssr: true,
  },
};

export default function Provider({
  children,
  web3authInitialState,
}: {
  children: React.ReactNode;
  web3authInitialState: IWeb3AuthState | undefined;
}) {
  return (
    <Web3AuthProvider config={web3authConfig} initialState={web3authInitialState}>
      <QueryClientProvider client={queryClient}>
        <WagmiProvider>{children}</WagmiProvider>
      </QueryClientProvider>
    </Web3AuthProvider>
  );
}



================================================
FILE: demo/react-app-no-modal/README.md
================================================
# Web3Auth x React Demo Application

## Questions

Ask us on our
[Github Discussion Board](https://github.com/orgs/Web3Auth/discussions) or reach
out to our [Discord](https://discord.gg/web3auth).

## Important Links

- [Website](https://web3auth.io)
- [Docs](https://web3auth.io/docs)
- [Guides](https://web3auth.io/docs/guides)
- [SDK / API References](https://web3auth.io/docs/sdk)
- [Pricing](https://web3auth.io/pricing.html)
- [Github Discussion Board](https://github.com/orgs/Web3Auth/discussions)

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests)
for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best
performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about
[deployment](https://create-react-app.dev/docs/deployment) for
more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can
`eject` at any time. This command will remove the single build dependency from
your project.

Instead, it will copy all the configuration files and the transitive
dependencies (webpack, Babel, ESLint, etc) right into your project so you have
full control over them. All of the commands except `eject` will still work, but
they will point to the copied scripts so you can tweak them. At this point
you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for
small and middle deployments, and you shouldn’t feel obligated to use this
feature. However we understand that this tool wouldn’t be useful if you couldn’t
customize it when you are ready for it.



================================================
FILE: demo/react-app-no-modal/config-overrides.js
================================================
const webpack = require("webpack");

module.exports = function override(config) {
  const fallback = config.resolve.fallback || {};
  Object.assign(fallback, {
    crypto: false,
    stream: false,
    assert: false,
    http: false,
    https: false,
    os: false,
    url: false,
    zlib: false,
  });
  config.resolve.fallback = fallback;
  config.plugins = (config.plugins || []).concat([
    new webpack.ProvidePlugin({
      process: "process/browser",
      Buffer: ["buffer", "Buffer"],
    }),
  ]);
  config.ignoreWarnings = [/Failed to parse source map/];
  config.module.rules.push({
    test: /\.(js|mjs|jsx)$/,
    enforce: "pre",
    loader: require.resolve("source-map-loader"),
    resolve: {
      fullySpecified: false,
    },
  });
  return config;
};



================================================
FILE: demo/react-app-no-modal/package.json
================================================
{
  "name": "react-evm-no-modal-example",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@web3auth/no-modal": "file:../../packages/no-modal",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "web-vitals": "^3.3.2",
    "web3": "^1.10.0"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      "supports bigint",
      "not dead"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@testing-library/jest-dom": "^5.16.5",
    "@testing-library/react": "^13.4.0",
    "@testing-library/user-event": "^14.4.3",
    "@types/jest": "^29.5.2",
    "@types/node": "^18.11.18",
    "@types/react": "^18.2.8",
    "@types/react-dom": "^18.2.4",
    "assert": "^2.0.0",
    "buffer": "^6.0.3",
    "crypto-browserify": "^3.12.0",
    "https-browserify": "^1.0.0",
    "os-browserify": "^0.3.0",
    "process": "^0.11.10",
    "react-app-rewired": "^2.2.1",
    "react-scripts": "5.0.1",
    "stream-browserify": "^3.0.0",
    "stream-http": "^3.2.0",
    "typescript": "^4.9.4",
    "url": "^0.11.0"
  },
  "scripts": {
    "start": "react-app-rewired start",
    "build": "react-app-rewired build",
    "test": "react-app-rewired test",
    "eject": "react-scripts eject",
    "lint": "react-scripts lint"
  }
}



================================================
FILE: demo/react-app-no-modal/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "es5",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": [
    "src"
  ]
}



================================================
FILE: demo/react-app-no-modal/public/index.html
================================================
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>



================================================
FILE: demo/react-app-no-modal/public/manifest.json
================================================
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}



================================================
FILE: demo/react-app-no-modal/public/robots.txt
================================================
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:



================================================
FILE: demo/react-app-no-modal/src/App.css
================================================
.container {
	width: 60%;
	margin: auto;
	padding: 0 2rem;
}

.main {
	min-height: 100vh;
	padding: 4rem 0;
	flex: 1;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}

.title {
	line-height: 1.15;
	font-size: 3rem;
	text-align: center;
	margin: 50px;
}

.title a {
	color: #0070f3;
	text-decoration: none;
}

.grid {
	display: flex;
	align-items: center;
	flex-direction: column;
}

.card {
	margin: 0.5rem;
	padding: 0.7rem;
	text-align: center;
	color: #0070f3;
	background-color: #fafafa;
	text-decoration: none;
	border: 1px solid #0070f3;
	border-radius: 10px;
	transition: color 0.15s ease, border-color 0.15s ease;
	width: 100%;
}

.card:hover,
.card:focus,
.card:active {
	cursor: pointer;
	background-color: #f1f1f1;
}

.footer {
	display: flex;
	flex: 1;
	padding: 2rem 0;
	border-top: 1px solid #eaeaea;
	justify-content: center;
	align-items: center;
	margin-top: 10rem;
}

.footer a {
	display: flex;
	justify-content: center;
	align-items: center;
	flex-grow: 1;
}

.logo {
	height: 1.5rem;
	margin-left: 0.5rem;
}

@media (max-width: 1200px) {
	.container {
		width: 100%;
	}
}

.flex-container {
	display: flex;
	flex-flow: row wrap;
}

.flex-container > div {
	width: 100px;
	margin: 10px;
	text-align: center;
	line-height: 75px;
	font-size: 30px;
}

#console {
	width: 100%;
	height: 100%;
	overflow: auto;
	word-wrap: break-word;
	font-size: 16px;
	font-family: monospace;
}



================================================
FILE: demo/react-app-no-modal/src/App.test.tsx
================================================
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});



================================================
FILE: demo/react-app-no-modal/src/App.tsx
================================================
import "./App.css";

import { SafeEventEmitterProvider, WALLET_CONNECTORS } from "@web3auth/modal";
import { Web3AuthNoModal } from "@web3auth/no-modal";
import { useEffect, useState } from "react";

import RPC from "./web3RPC"; // for using web3.js

const clientId = "BEglQSgt4cUWcj6SKRdu5QkOXTsePmMcusG5EAoyjyOYKlVRjIF1iCNnMOTfpzCiunHRrMui8TIwQPXdkQ8Yxuk"; // get from https://dashboard.web3auth.io

function App() {
  const [web3auth, setWeb3auth] = useState<Web3AuthNoModal | null>(null);
  const [provider, setProvider] = useState<SafeEventEmitterProvider | null>(null);

  useEffect(() => {
    const init = async () => {
      try {
        const web3auth = new Web3AuthNoModal({
          clientId,
          web3AuthNetwork: "sapphire_mainnet",
          authBuildEnv: "testing",
        });

        setWeb3auth(web3auth);

        await web3auth.init();
        if (web3auth.connectedConnectorName && web3auth.provider) {
          setProvider(web3auth.provider);
        }
      } catch (error) {
        console.error(error);
      }
    };

    init();
  }, []);

  const login = async () => {
    if (!web3auth) {
      uiConsole("web3auth not initialized yet");
      return;
    }
    const web3authProvider = await web3auth.connectTo(WALLET_CONNECTORS.AUTH, { authConnection: "google" });
    setProvider(web3authProvider);
  };

  const getIdentityToken = async () => {
    if (!web3auth) {
      uiConsole("web3auth not initialized yet");
      return;
    }
    const idToken = await web3auth.getIdentityToken();
    uiConsole(idToken);
  };

  const getUserInfo = async () => {
    if (!web3auth) {
      uiConsole("web3auth not initialized yet");
      return;
    }
    const user = await web3auth.getUserInfo();
    uiConsole(user);
  };

  const logout = async () => {
    if (!web3auth) {
      uiConsole("web3auth not initialized yet");
      return;
    }
    await web3auth.logout();
    setProvider(null);
  };

  const getChainId = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    const rpc = new RPC(provider);
    const chainId = await rpc.getChainId();
    uiConsole(chainId);
  };

  const switchChain = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    await web3auth?.switchChain({ chainId: "0x5" });
    uiConsole("Chain Switched");
  };

  const getAccounts = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    const rpc = new RPC(provider);
    const address = await rpc.getAccounts();
    uiConsole(address);
  };

  const getBalance = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    const rpc = new RPC(provider);
    const balance = await rpc.getBalance();
    uiConsole(balance);
  };

  const sendTransaction = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    const rpc = new RPC(provider);
    const receipt = await rpc.sendTransaction();
    uiConsole(receipt);
  };

  const signMessage = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    const rpc = new RPC(provider);
    const signedMessage = await rpc.signMessage();
    uiConsole(signedMessage);
  };

  const getPrivateKey = async () => {
    if (!provider) {
      uiConsole("provider not initialized yet");
      return;
    }
    const rpc = new RPC(provider);
    const privateKey = await rpc.getPrivateKey();
    uiConsole(privateKey);
  };

  function uiConsole(...args: any[]): void {
    const el = document.querySelector("#console>p");
    if (el) {
      el.innerHTML = JSON.stringify(args || {}, (key, value) => (typeof value === "bigint" ? value.toString() : value), 2);
    }
  }

  const loggedInView = (
    <>
      <div className="flex-container">
        <div>
          <button onClick={getUserInfo} className="card">
            Get User Info
          </button>
        </div>
        <div>
          <button onClick={getIdentityToken} className="card">
            Get ID Token
          </button>
        </div>
        <div>
          <button onClick={getChainId} className="card">
            Get Chain ID
          </button>
        </div>
        <div>
          <button onClick={switchChain} className="card">
            Switch Chain
          </button>
        </div>
        <div>
          <button onClick={getAccounts} className="card">
            Get Accounts
          </button>
        </div>
        <div>
          <button onClick={getBalance} className="card">
            Get Balance
          </button>
        </div>
        <div>
          <button onClick={signMessage} className="card">
            Sign Message
          </button>
        </div>
        <div>
          <button onClick={sendTransaction} className="card">
            Send Transaction
          </button>
        </div>
        <div>
          <button onClick={getPrivateKey} className="card">
            Get Private Key
          </button>
        </div>
        <div>
          <button onClick={logout} className="card">
            Log Out
          </button>
        </div>
      </div>
      <div id="console" style={{ whiteSpace: "pre-line" }}>
        <p style={{ whiteSpace: "pre-line" }}>Logged in Successfully!</p>
      </div>
    </>
  );

  const unloggedInView = (
    <button onClick={login} className="card">
      Login
    </button>
  );

  return (
    <div className="container">
      <h1 className="title">
        <a target="_blank" href="http://web3auth.io/" rel="noreferrer">
          Web3Auth{" "}
        </a>
        & ReactJS Example
      </h1>

      <div className="grid">{provider ? loggedInView : unloggedInView}</div>

      <footer className="footer">
        <a
          href="https://github.com/Web3Auth/examples/tree/master/web-no-modal-sdk/evm/react-evm-no-modal-example"
          target="_blank"
          rel="noopener noreferrer"
        >
          Source code
        </a>
      </footer>
    </div>
  );
}

export default App;



================================================
FILE: demo/react-app-no-modal/src/index.css
================================================
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}



================================================
FILE: demo/react-app-no-modal/src/index.tsx
================================================
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();



================================================
FILE: demo/react-app-no-modal/src/react-app-env.d.ts
================================================
/// <reference types="react-scripts" />



================================================
FILE: demo/react-app-no-modal/src/reportWebVitals.ts
================================================
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;



================================================
FILE: demo/react-app-no-modal/src/setupTests.ts
================================================
// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';



================================================
FILE: demo/react-app-no-modal/src/web3RPC.ts
================================================
import type { SafeEventEmitterProvider } from "@web3auth/no-modal";
import Web3 from "web3";

export default class EthereumRpc {
  private provider: SafeEventEmitterProvider;

  constructor(provider: SafeEventEmitterProvider) {
    this.provider = provider;
  }

  async getChainId(): Promise<string> {
    try {
      const web3 = new Web3(this.provider as any);

      // Get the connected Chain's ID
      const chainId = await web3.eth.getChainId();

      return chainId.toString();
    } catch (error) {
      return error as string;
    }
  }

  async getAccounts(): Promise<any> {
    try {
      const web3 = new Web3(this.provider as any);

      // Get user's Ethereum public address
      const address = (await web3.eth.getAccounts())[0];

      return address;
    } catch (error) {
      return error;
    }
  }

  async getBalance(): Promise<string> {
    try {
      const web3 = new Web3(this.provider as any);

      // Get user's Ethereum public address
      const address = (await web3.eth.getAccounts())[0];

      // Get user's balance in ether
      const balance = web3.utils.fromWei(
        await web3.eth.getBalance(address) // Balance is in wei
      );

      return balance;
    } catch (error) {
      return error as string;
    }
  }

  async sendTransaction(): Promise<any> {
    try {
      const web3 = new Web3(this.provider as any);

      // Get user's Ethereum public address
      const fromAddress = (await web3.eth.getAccounts())[0];

      const destination = fromAddress;

      const amount = web3.utils.toWei("0.001"); // Convert 1 ether to wei

      // Submit transaction to the blockchain and wait for it to be mined
      const receipt = await web3.eth.sendTransaction({
        from: fromAddress,
        to: destination,
        value: amount,
        maxPriorityFeePerGas: "5000000000", // Max priority fee per gas
        maxFeePerGas: "6000000000000", // Max fee per gas
      });

      return receipt;
    } catch (error) {
      return error as string;
    }
  }

  async signMessage() {
    try {
      const web3 = new Web3(this.provider as any);

      // Get user's Ethereum public address
      const fromAddress = (await web3.eth.getAccounts())[0];

      const originalMessage = "YOUR_MESSAGE";

      // Sign the message
      const signedMessage = await web3.eth.personal.sign(
        originalMessage,
        fromAddress,
        "test password!" // configure your own password here.
      );

      return signedMessage;
    } catch (error) {
      return error as string;
    }
  }

  async getPrivateKey(): Promise<any> {
    try {
      const privateKey = await this.provider.request({
        method: "eth_private_key",
      });

      return privateKey;
    } catch (error) {
      return error as string;
    }
  }
}


================================================
FILE: demo/vite-react-app-sfa/README.md
================================================
# Web3Auth x React Demo App

## Quickstart

To use this demo app, you'll first have to build the Web3Auth packages.

### Build the `Web3Auth` packages

```bash
git clone https://github.com/Web3Auth/web3auth-web.git
cd web3auth-web
npm install
npm run bootstrap && npm run build
```

### Start the demo app

> Inside `web3auth-web` directory.

```bash
cd demo/react-app
npm install
npm run start
# localhost:3000
```



================================================
FILE: demo/vite-react-app-sfa/eslint.config.mjs
================================================
import toruslabsReact from "@toruslabs/eslint-config-react";

export default [
  ...toruslabsReact,
  {
    ignores: ["*.config.mjs", "*.config.mts"],
  },
];



================================================
FILE: demo/vite-react-app-sfa/index.html
================================================
<!--
  Migrate from react-app to vite by following this guide
  https://www.freecodecamp.org/news/how-to-migrate-from-create-react-app-to-vite/
-->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Web site created using create-react-app" />
    <link rel="apple-touch-icon" href="/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="/manifest.json" />
    <script type="module">
      import { Buffer } from "buffer";
      import process from "process";
      // window.global ||= window;
      window.Buffer = Buffer;
      window.process = process;
    </script>
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
    <script type="module" src="/src/index.tsx"></script>
  </body>
</html>



================================================
FILE: demo/vite-react-app-sfa/package.json
================================================
{
  "name": "react-app-sfa",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@react-oauth/google": "^0.12.1",
    "@tanstack/react-query": "^5.74.11",
    "@web3auth/auth": "^10.2.3",
    "@web3auth/no-modal": "file:../../packages/no-modal",
    "@web3auth/sign-in-with-ethereum": "^4.2.2",
    "ethers": "^6.13.4",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "wagmi": "^2.15.1"
  },
  "scripts": {
    "start": "vite",
    "build": "tsc && vite build",
    "lint": "eslint --fix 'src/**/*.ts' 'src/**/*.tsx'",
    "preview": "vite preview"
  },
  "browserslist": {
    "production": [
      "supports bigint",
      "not dead"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@toruslabs/eslint-config-react": "^3.4.4",
    "@types/node": "^22.10.1",
    "@types/react": "^19.1.2",
    "@types/react-dom": "^19.1.2",
    "@vitejs/plugin-react": "^4.3.4",
    "buffer": "^6.0.3",
    "eslint": "^8.57.1",
    "process": "^0.11.10",
    "typescript": "^5.2.2",
    "vite": "^6.0.11",
    "vite-tsconfig-paths": "^5.1.3",
    "webpack-bundle-analyzer": "^4.10.2"
  }
}



================================================
FILE: demo/vite-react-app-sfa/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "types": ["vite/client"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}



================================================
FILE: demo/vite-react-app-sfa/vite-env.d.ts
================================================
/// <reference types="vite/client" />


================================================
FILE: demo/vite-react-app-sfa/vite.config.mts
================================================
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { resolve } from "node:path";

export default defineConfig({
  plugins: [react()],
  server: {
    // this ensures that the browser opens upon server start
    open: true,
    // this sets a default port to 3000
    port: 3000,
  },
  resolve: {
    alias: {
      wagmi: resolve("./node_modules/wagmi"),
    }
  }
});



================================================
FILE: demo/vite-react-app-sfa/public/manifest.json
================================================
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}



================================================
FILE: demo/vite-react-app-sfa/public/robots.txt
================================================
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:



================================================
FILE: demo/vite-react-app-sfa/src/App.css
================================================
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}



================================================
FILE: demo/vite-react-app-sfa/src/App.tsx
================================================
import "./App.css";
import styles from "./styles/Home.module.css";
import Main from "./components/Main";
import { GoogleOAuthProvider } from "@react-oauth/google";
import { GOOGLE_CLIENT_ID } from "./config";

function App() {
  return (
    <div className={styles.container}>
      <GoogleOAuthProvider clientId={GOOGLE_CLIENT_ID}>
        <Main />
      </GoogleOAuthProvider>
    </div>
  );
}

export default App;



================================================
FILE: demo/vite-react-app-sfa/src/config.ts
================================================
export const GOOGLE_CLIENT_ID = "519228911939-cri01h55lsjbsia1k7ll6qpalrus75ps.apps.googleusercontent.com";


================================================
FILE: demo/vite-react-app-sfa/src/index.css
================================================
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}



================================================
FILE: demo/vite-react-app-sfa/src/index.tsx
================================================
import "./index.css";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { type Web3AuthContextConfig, Web3AuthProvider } from "@web3auth/no-modal/react";
import { WagmiProvider } from "@web3auth/no-modal/react/wagmi";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./App";

const container = document.getElementById("root") as HTMLElement;
const root = createRoot(container);

const clientId = "BPi5PB_UiIZ-cPz1GtV5i1I2iOSOHuimiXBI0e-Oe_u6X3oVAbCiAZOTEBtTXw4tsluTITPqA8zMsfxIKMjiqNQ";
const queryClient = new QueryClient();

const web3authConfig: Web3AuthContextConfig = {
  web3AuthOptions: {
    enableLogging: true,
    web3AuthNetwork: "sapphire_mainnet",
    clientId: clientId,
    authBuildEnv: "testing",
  },
};

root.render(
  <StrictMode>
    <Web3AuthProvider config={web3authConfig}>
      <QueryClientProvider client={queryClient}>
        <WagmiProvider>
          <App />
        </WagmiProvider>
      </QueryClientProvider>
    </Web3AuthProvider>
  </StrictMode>
);



================================================
FILE: demo/vite-react-app-sfa/src/react-app-env.d.ts
================================================
/// <reference types="react-scripts" />



================================================
FILE: demo/vite-react-app-sfa/src/components/Main.tsx
================================================
import { CredentialResponse, GoogleLogin } from "@react-oauth/google";
import { WALLET_CONNECTORS } from "@web3auth/no-modal";
import { useWeb3Auth, useWeb3AuthConnect, useWeb3AuthDisconnect } from "@web3auth/no-modal/react";
import { useAccount, useSignMessage } from "wagmi";

import styles from "../styles/Home.module.css";

const Main = () => {
  const { provider, isConnected } = useWeb3Auth();
  const { connect, loading: connecting, error: connectingError, connectorName } = useWeb3AuthConnect();
  const { disconnect } = useWeb3AuthDisconnect();
  const { isConnected: isWagmiConnected } = useAccount();
  const { signMessageAsync, data: signedMessageData } = useSignMessage();

  const loggedInView = (
    <>
      <div style={{ marginTop: "16px", marginBottom: "16px" }}>
        <p>Provider Actions</p>
        {/* Sign Message */}
        <button onClick={() => signMessageAsync({ message: "Hello, world!" })} className={styles.card}>
          Sign Message
        </button>
        {signedMessageData && <textarea disabled rows={5} value={signedMessageData} style={{ width: "100%" }} />}
      </div>

      <button onClick={() => disconnect()} className={styles.card}>
        Log Out
      </button>

      <div className={styles.console} id="console">
        <p className={styles.code}></p>
      </div>
    </>
  );

  const onGoogleLogin = async (response: CredentialResponse) => {
    console.log(response);
    const idToken = response.credential;
    if (!idToken) {
      console.error("No idToken present");
      return;
    }

    await connect(WALLET_CONNECTORS.AUTH, {
      authConnection: "custom",
      authConnectionId: "w3a-sfa-web-google",
      idToken: idToken,
      extraLoginOptions: {
        userIdField: "email",
        isUserIdCaseSensitive: false,
      },
    });
  };

  const unloggedInView = (
    <>
      {connecting ? (
        <p>Connecting...</p>
      ) : (
        <div className="flex justify-center mb-2">
          <GoogleLogin
            logo_alignment="left"
            locale="en"
            auto_select={false}
            text="continue_with"
            onSuccess={onGoogleLogin}
            size="large"
            shape="pill"
            width={window.innerWidth < 640 ? "276px" : "332px"}
          />
        </div>
      )}
      {connectingError && <p>Error: {connectingError.message}</p>}
    </>
  );

  return (
    <div className={styles.grid}>
      <p>Web3Auth: {isConnected ? "Connected" : "Disconnected"}</p>
      <p>Wagmi: {isWagmiConnected ? "Connected" : "Disconnected"}</p>
      {provider ? loggedInView : unloggedInView}
    </div>
  );
};

export default Main;



================================================
FILE: demo/vite-react-app-sfa/src/styles/Home.module.css
================================================
.container {
  width: 60%;
  margin: auto;
  padding: 0 2rem;
}

.main {
  min-height: 100vh;
  padding: 4rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  line-height: 1.15;
  font-size: 3rem;
  text-align: center;
  margin: 50px;
}

.title a {
  color: #0070f3;
  text-decoration: none;
}

.console {
  max-width: 100%;
}

.code {
  background: #fafafa;
  border-radius: 5px;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace;
  overflow-wrap: break-word;
}

.grid {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.setting {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 20px;
  margin: 30px 0;
  background: #f4f5f7;
  border: 1px solid #ebecf0;
  border-radius: 5px;
}

.card {
  margin: 0.5rem;
  padding: 0.7rem;
  text-align: center;
  color: #0070f3;
  text-decoration: none;
  border: 1px solid #0070f3;
  border-radius: 10px;
  transition: color 0.15s ease, border-color 0.15s ease;
  width: 100%;
}

.card:hover,
.card:focus,
.card:active {
  cursor: pointer;
  background-color: #fafafa;
}

.row {
  display: flex;
  margin-bottom: 0.5rem;
  width: 100%;
}
.label {
  flex-basis: 45%;
  padding-right: 10px;
  display: flex;
  align-items: center;
  justify-content: right;
  font-weight: bold;
}

.select {
  flex-basis: 30%;
  text-align: left;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  border-radius: 8px;
}

.footer {
  display: flex;
  flex: 1;
  padding: 2rem 0;
  border-top: 1px solid #eaeaea;
  justify-content: center;
  align-items: center;
  margin-top: 10rem;
}

.footer a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.logo {
  height: 1.5rem;
  margin-left: 0.5rem;
}

/* @media (max-width: 1200px) {
  .container {
    width: 100%;
  }
} */



================================================
FILE: demo/vite-react-app-solana/README.md
================================================
# Web3Auth x React Demo App

## Quickstart

To use this demo app, you'll first have to build the Web3Auth packages.

### Build the `Web3Auth` packages

```bash
git clone https://github.com/Web3Auth/web3auth-web.git
cd web3auth-web
npm install
npm run bootstrap && npm run build
```

### Start the demo app

> Inside `web3auth-web` directory.

```bash
cd demo/react-app
npm install
npm run start
# localhost:3000
```



================================================
FILE: demo/vite-react-app-solana/eslint.config.mjs
================================================
import toruslabsReact from "@toruslabs/eslint-config-react";

export default [
  ...toruslabsReact,
  {
    ignores: ["*.config.mjs", "*.config.mts"],
  },
];



================================================
FILE: demo/vite-react-app-solana/index.html
================================================
<!--
  Migrate from react-app to vite by following this guide
  https://www.freecodecamp.org/news/how-to-migrate-from-create-react-app-to-vite/
-->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Web site created using create-react-app" />
    <link rel="apple-touch-icon" href="/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="/manifest.json" />
    <script type="module">
      import { Buffer } from "buffer";
      import process from "process";
      // window.global ||= window;
      window.Buffer = Buffer;
      window.process = process;
    </script>
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
    <script type="module" src="/src/index.tsx"></script>
  </body>
</html>



================================================
FILE: demo/vite-react-app-solana/package.json
================================================
{
  "name": "react-test",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@web3auth/modal": "file:../../packages/modal",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "scripts": {
    "start": "vite",
    "build": "tsc && vite build",
    "lint": "eslint --fix 'src/**/*.ts' 'src/**/*.tsx'",
    "preview": "vite preview"
  },
  "browserslist": {
    "production": [
      "supports bigint",
      "not dead"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@toruslabs/eslint-config-react": "^4.1.4",
    "@types/node": "^22.10.1",
    "@vitejs/plugin-react": "^4.3.4",
    "buffer": "^6.0.3",
    "process": "^0.11.10",
    "typescript": "^5.2.2",
    "vite": "^6.0.11",
    "vite-tsconfig-paths": "^5.1.3",
    "webpack-bundle-analyzer": "^4.10.2"
  }
}



================================================
FILE: demo/vite-react-app-solana/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "types": ["vite/client"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}



================================================
FILE: demo/vite-react-app-solana/vite-env.d.ts
================================================
/// <reference types="vite/client" />


================================================
FILE: demo/vite-react-app-solana/vite.config.mts
================================================
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    // this ensures that the browser opens upon server start
    open: true,
    // this sets a default port to 3000
    port: 3000,
  },
});



================================================
FILE: demo/vite-react-app-solana/public/manifest.json
================================================
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}



================================================
FILE: demo/vite-react-app-solana/public/robots.txt
================================================
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:



================================================
FILE: demo/vite-react-app-solana/src/App.css
================================================
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}



================================================
FILE: demo/vite-react-app-solana/src/App.tsx
================================================
import "./App.css";

import Main from "./components/Main";
import styles from "./styles/Home.module.css";

function App() {
  return (
    <div className={styles.container}>
      <Main />
    </div>
  );
}

export default App;



================================================
FILE: demo/vite-react-app-solana/src/index.css
================================================
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}



================================================
FILE: demo/vite-react-app-solana/src/index.tsx
================================================
import "./index.css";

import { type Web3AuthContextConfig, Web3AuthProvider } from "@web3auth/modal/react";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./App";

const container = document.getElementById("root") as HTMLElement;
const root = createRoot(container);

const clientId = "BIkhKhVq14WkcoGDNkOpaVB3vhBDANPzD0oVQzCmnoCz83z2WrKwtiROqA6J9d6UZdX4hifg9z1hI3fuQMfwMc8";

const web3authConfig: Web3AuthContextConfig = {
  web3AuthOptions: {
    enableLogging: true,
    web3AuthNetwork: "sapphire_devnet",
    clientId: clientId,
    authBuildEnv: "testing",
  },
};

root.render(
  <StrictMode>
    <Web3AuthProvider config={web3authConfig}>
      <App />
    </Web3AuthProvider>
  </StrictMode>
);



================================================
FILE: demo/vite-react-app-solana/src/react-app-env.d.ts
================================================
/// <reference types="react-scripts" />



================================================
FILE: demo/vite-react-app-solana/src/components/Main.tsx
================================================
import { useWeb3Auth, useWeb3AuthConnect, useWeb3AuthDisconnect } from "@web3auth/modal/react";
import { useSignMessage } from "@web3auth/modal/react/solana";

import styles from "../styles/Home.module.css";

const Main = () => {
  const { provider, isInitialized } = useWeb3Auth();
  const { connect } = useWeb3AuthConnect();
  const { disconnect } = useWeb3AuthDisconnect();
  const { data: signedMessageData, signMessage } = useSignMessage();

  const loggedInView = (
    <>
      <div style={{ marginTop: "16px", marginBottom: "16px" }}>
        <p>Provider Actions</p>
        {/* Sign Message */}
        <button onClick={() => signMessage("Hello, world!")} className={styles.card}>
          Sign Message
        </button>
        {signedMessageData && <textarea disabled rows={5} value={signedMessageData} style={{ width: "100%" }} />}
      </div>

      <button onClick={() => disconnect()} className={styles.card}>
        Log Out
      </button>

      <div className={styles.console} id="console">
        <p className={styles.code}></p>
      </div>
    </>
  );

  const unloggedInView = (
    <>
      {isInitialized ? (
        <button onClick={() => connect()} className={styles.card}>
          Login
        </button>
      ) : (
        <p>Loading Web3Auth...</p>
      )}
    </>
  );

  return <div className={styles.grid}>{provider ? loggedInView : unloggedInView}</div>;
};

export default Main;



================================================
FILE: demo/vite-react-app-solana/src/styles/Home.module.css
================================================
.container {
  width: 60%;
  margin: auto;
  padding: 0 2rem;
}

.main {
  min-height: 100vh;
  padding: 4rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  line-height: 1.15;
  font-size: 3rem;
  text-align: center;
  margin: 50px;
}

.title a {
  color: #0070f3;
  text-decoration: none;
}

.console {
  max-width: 100%;
}

.code {
  background: #fafafa;
  border-radius: 5px;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace;
  overflow-wrap: break-word;
}

.grid {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.setting {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 20px;
  margin: 30px 0;
  background: #f4f5f7;
  border: 1px solid #ebecf0;
  border-radius: 5px;
}

.card {
  margin: 0.5rem;
  padding: 0.7rem;
  text-align: center;
  color: #0070f3;
  text-decoration: none;
  border: 1px solid #0070f3;
  border-radius: 10px;
  transition: color 0.15s ease, border-color 0.15s ease;
  width: 100%;
}

.card:hover,
.card:focus,
.card:active {
  cursor: pointer;
  background-color: #fafafa;
}

.row {
  display: flex;
  margin-bottom: 0.5rem;
  width: 100%;
}
.label {
  flex-basis: 45%;
  padding-right: 10px;
  display: flex;
  align-items: center;
  justify-content: right;
  font-weight: bold;
}

.select {
  flex-basis: 30%;
  text-align: left;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  border-radius: 8px;
}

.footer {
  display: flex;
  flex: 1;
  padding: 2rem 0;
  border-top: 1px solid #eaeaea;
  justify-content: center;
  align-items: center;
  margin-top: 10rem;
}

.footer a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.logo {
  height: 1.5rem;
  margin-left: 0.5rem;
}

/* @media (max-width: 1200px) {
  .container {
    width: 100%;
  }
} */



================================================
FILE: demo/vue-app-new/README.md
================================================
# Web3Auth x Vue Demo App

## Quickstart

To use this demo app, you'll first have to build the Web3Auth packages.

### Build the `Web3Auth` packages

```bash
git clone https://github.com/Web3Auth/web3auth-web.git
cd web3auth-web
npm install
npm run bootstrap && npm run build
```

### Start the demo app

> Inside `web3auth-web` directory.

```bash
cd demo/vue-app
npm install
npm run dev
# localhost:8080
```



================================================
FILE: demo/vue-app-new/index.html
================================================
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Web3Auth demo</title>
  </head>
  <body>
    <noscript>
      <strong>We're sorry but this app doesn't work properly without JavaScript enabled. Please enable it to continue.</strong>
    </noscript>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
</html>



================================================
FILE: demo/vue-app-new/package.json
================================================
{
  "name": "vue-app-new",
  "private": true,
  "version": "0.0.0",
  "scripts": {
    "type-check": "vue-tsc --noEmit -p tsconfig.json",
    "dev": "vite",
    "serve": "vite preview",
    "build": "npm run type-check && vite build",
    "lint": "eslint --cache --fix"
  },
  "dependencies": {
    "@solana/web3.js": "^1.98.2",
    "@tanstack/vue-query": "^5.80.7",
    "@toruslabs/base-controllers": "^8.6.0",
    "@toruslabs/bs58": "^1.0.0",
    "@toruslabs/ethereum-controllers": "^8.6.0",
    "@toruslabs/solana-controllers": "^8.6.0",
    "@toruslabs/tweetnacl-js": "^1.0.4",
    "@toruslabs/vue-components": "^8.0.8",
    "@toruslabs/vue-icons": "^8.0.2",
    "@wagmi/vue": "^0.1.22",
    "@web3auth/auth": "^10.5.0",
    "@web3auth/modal": "file:../../packages/modal",
    "@web3auth/no-modal": "file:../../packages/no-modal",
    "@web3auth/sign-in-with-ethereum": "^5.0.0",
    "@web3auth/ws-embed": "^5.0.17",
    "ethers": "^6.14.4",
    "petite-vue-i18n": "^11.1.6",
    "vue": "^3.5.17"
  },
  "devDependencies": {
    "@toruslabs/eslint-config-vue": "^4.1.5",
    "@vitejs/plugin-vue": "^5.2.4",
    "autoprefixer": "^10.4.21",
    "eslint": "^9.29.0",
    "globals": "^16.2.0",
    "postcss": "^8.5.6",
    "prettier": "^3.5.3",
    "stream-browserify": "^3.0.0",
    "tailwindcss": "^3.4.13",
    "typescript": "^5.8.3",
    "vite": "^6.3.5",
    "vue-tsc": "^2.2.10"
  },
  "overrides": {
    "ox": "0.6.9"
  },
  "optionalDependencies": {
    "@esbuild/linux-x64": "0.25.4"
  },
  "lint-staged": {
    "!(*d).{js,ts}": [
      "eslint --cache --fix",
      "prettier --write"
    ],
    "*.{json, md}": [
      "prettier --write"
    ]
  }
}



================================================
FILE: demo/vue-app-new/postcss.config.js
================================================
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};



================================================
FILE: demo/vue-app-new/tailwind.config.js
================================================
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}


================================================
FILE: demo/vue-app-new/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "esnext",
    "module": "ESNext",
    "strict": true,
    "jsx": "preserve",
    "importHelpers": true,
    "moduleResolution": "bundler",
    "experimentalDecorators": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "resolveJsonModule": true,
    "sourceMap": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },
    "lib": ["esnext", "dom", "dom.iterable", "scripthost"]
  },
  "include": ["src"],
  "exclude": ["node_modules"]
}



================================================
FILE: demo/vue-app-new/vercel.json
================================================
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}



================================================
FILE: demo/vue-app-new/vite.config.mts
================================================
import { resolve } from "node:path";

import vue from "@vitejs/plugin-vue";
import { defineConfig, loadEnv } from "vite";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const { VITE_APP_INFURA_PROJECT_KEY, VITE_APP_SOLANA_MAINNET_RPC, VITE_APP_SOLANA_TESTNET_RPC, VITE_APP_SOLANA_DEVNET_RPC } = loadEnv(
    mode,
    process.cwd()
  );

  return {
    mode,
    server: {
      port: 8080,
    },
    plugins: [vue()],
    resolve: {
      alias: {
        "@": "/src",
        "@wagmi/vue": resolve("./node_modules/@wagmi/vue"),
      },
    },
    define: {
      global: "globalThis",
      "process.env.NODE_ENV": JSON.stringify(process.env.NODE_ENV),
      "process.env.VITE_APP_INFURA_PROJECT_KEY": JSON.stringify(VITE_APP_INFURA_PROJECT_KEY),
      "process.env.VITE_APP_SOLANA_MAINNET_RPC": JSON.stringify(VITE_APP_SOLANA_MAINNET_RPC),
      "process.env.VITE_APP_SOLANA_TESTNET_RPC": JSON.stringify(VITE_APP_SOLANA_TESTNET_RPC),
      "process.env.VITE_APP_SOLANA_DEVNET_RPC": JSON.stringify(VITE_APP_SOLANA_DEVNET_RPC),
    },
  };
});



================================================
FILE: demo/vue-app-new/.env.sample
================================================
VITE_APP_PIMLICO_API_KEY=""
VITE_APP_SOLANA_MAINNET_RPC=""
VITE_APP_SOLANA_DEVNET_RPC=""
VITE_APP_SOLANA_TESTNET_RPC=""



================================================
FILE: demo/vue-app-new/.eslintrc.mjs
================================================
import toruslabsVue from "@toruslabs/eslint-config-vue";

export default [
  ...toruslabsVue,
  {
    ignores: ["*.config.mjs", "*.config.mts"],
  },
];



================================================
FILE: demo/vue-app-new/.prettierrc.yaml
================================================
# .prettierrc or .prettierrc.yaml
printWidth: 150
singleQuote: false
semi: true
htmlWhitespaceSensitivity: ignore
trailingComma: es5



================================================
FILE: demo/vue-app-new/src/App.vue
================================================
<script setup lang="ts">
import Main from "./MainView.vue";
</script>

<template>
  <Main />
</template>



================================================
FILE: demo/vue-app-new/src/config.ts
================================================
import { AUTH_CONNECTION, AUTH_CONNECTION_TYPE, LANGUAGE_TYPE, LANGUAGES, WhiteLabelData } from "@web3auth/auth";
import {
  CHAIN_NAMESPACES,
  ChainNamespaceType,
  CONFIRMATION_STRATEGY,
  type CONFIRMATION_STRATEGY_TYPE,
  LoginMethodConfig,
  ModalConfig,
  SignTypedDataMessageV4,
  WEB3AUTH_NETWORK,
  WEB3AUTH_NETWORK_TYPE,
  type WidgetType,
} from "@web3auth/modal";

export const networkOptions = Object.values(WEB3AUTH_NETWORK).map((x) => ({ name: x, value: x }));

export const chainNamespaceOptions = Object.values(CHAIN_NAMESPACES).map((x) => ({ name: x, value: x }));

export const chainConfigs: Record<ChainNamespaceType, string[]> = {
  [CHAIN_NAMESPACES.EIP155]: ["0x1", "0xaa36a7", "0x2105", "0x61", "0x13882"],
  [CHAIN_NAMESPACES.SOLANA]: ["0x65", "0x67"],
  [CHAIN_NAMESPACES.CASPER]: [],
  [CHAIN_NAMESPACES.XRPL]: [],
  [CHAIN_NAMESPACES.OTHER]: [],
};

export const clientIds: Record<WEB3AUTH_NETWORK_TYPE, string> = {
  [WEB3AUTH_NETWORK.MAINNET]: "BJRZ6qdDTbj6Vd5YXvV994TYCqY42-PxldCetmvGTUdoq6pkCqdpuC1DIehz76zuYdaq1RJkXGHuDraHRhCQHvA",
  [WEB3AUTH_NETWORK.TESTNET]: "BHr_dKcxC0ecKn_2dZQmQeNdjPgWykMkcodEHkVvPMo71qzOV6SgtoN8KCvFdLN7bf34JOm89vWQMLFmSfIo84A",
  [WEB3AUTH_NETWORK.AQUA]: "BM34K7ZqV3QwbDt0lvJFCdr4DxS9gyn7XZ2wZUaaf0Ddr71nLjPCNNYtXuGWxxc4i7ivYdgQzFqKlIot4IWrWCE",
  [WEB3AUTH_NETWORK.CYAN]: "BEglQSgt4cUWcj6SKRdu5QkOXTsePmMcusG5EAoyjyOYKlVRjIF1iCNnMOTfpzCiunHRrMui8TIwQPXdkQ8Yxuk",
  [WEB3AUTH_NETWORK.SAPPHIRE_DEVNET]: "BHgArYmWwSeq21czpcarYh0EVq2WWOzflX-NTK-tY1-1pauPzHKRRLgpABkmYiIV_og9jAvoIxQ8L3Smrwe04Lw",
  [WEB3AUTH_NETWORK.SAPPHIRE_MAINNET]: "BPi5PB_UiIZ-cPz1GtV5i1I2iOSOHuimiXBI0e-Oe_u6X3oVAbCiAZOTEBtTXw4tsluTITPqA8zMsfxIKMjiqNQ",
  [WEB3AUTH_NETWORK.CELESTE]: "openlogin",
};

export const initWhiteLabel: WhiteLabelData = {
  appName: "HelloDemo",
  appUrl: window.location.origin,
  logoDark: "https://images.web3auth.io/example-hello.svg", // dark logo for light background
  logoLight: "https://images.web3auth.io/example-hello-light.svg", // light logo for dark background
  mode: "auto",
  defaultLanguage: "en",
  theme: {
    primary: "#5DF0EB",
    onPrimary: "black",
  },
};

export const loginProviderOptions = Object.values(AUTH_CONNECTION)
  .filter((x) => x !== "custom" && x !== "authenticator" && x !== "passkeys")
  .map((x) => ({ name: x.replaceAll("_", " "), value: x }));

export const languageOptions: { name: string; value: LANGUAGE_TYPE }[] = [
  { name: "English", value: LANGUAGES.en },
  { name: "German", value: LANGUAGES.de },
  { name: "Japanese", value: LANGUAGES.ja },
  { name: "Korean", value: LANGUAGES.ko },
  { name: "Mandarin", value: LANGUAGES.zh },
  { name: "Spanish", value: LANGUAGES.es },
  { name: "French", value: LANGUAGES.fr },
  { name: "Portuguese", value: LANGUAGES.pt },
  { name: "Dutch", value: LANGUAGES.nl },
  { name: "Turkish", value: LANGUAGES.tr },
];

export const defaultLoginMethod: Record<AUTH_CONNECTION_TYPE, ModalConfig> = loginProviderOptions.reduce(
  (acc, curr) => ({
    ...acc,
    [curr.value]: {
      name: `${curr.name} login`,
      description: "",
      logoHover: "",
      logoLight: "",
      logoDark: "",
      mainOption: false,
      showOnModal: true,
      label: "",
    } as LoginMethodConfig[AUTH_CONNECTION_TYPE],
  }),
  {} as Record<AUTH_CONNECTION_TYPE, ModalConfig>
);

export type SmartAccountType = "biconomy" | "safe" | "nexus" | "kernel" | "trust" | "metamask";

export const SmartAccountOptions: { name: string; value: SmartAccountType }[] = [
  { name: "Biconomy", value: "biconomy" },
  { name: "Safe", value: "safe" },
  { name: "Nexus", value: "nexus" },
  { name: "Kernel", value: "kernel" },
  { name: "Trust", value: "trust" },
  { name: "Metamask", value: "metamask" },
  // { name: "Light", value: "light" },
  // { name: "Simple", value: "simple" },
];

export const getDefaultBundlerUrl = (chainId: string): string => {
  return `https://api.pimlico.io/v2/${Number(chainId)}/rpc?apikey=${import.meta.env.VITE_APP_PIMLICO_API_KEY}`;
};

export type FormData = {
  // authMode: string;
  network: WEB3AUTH_NETWORK_TYPE;
  chainNamespaces: ChainNamespaceType[];
  chains: string[];
  defaultChainId?: string;
  whiteLabel: {
    enable: boolean;
    config: WhiteLabelData;
  };
  connectors: string[];
  loginProviders: AUTH_CONNECTION_TYPE[];
  showWalletDiscovery: boolean;
  multiInjectedProviderDiscovery: boolean;
  loginMethods: LoginMethodConfig;
  walletPlugin: {
    enable: boolean;
    confirmationStrategy: Exclude<CONFIRMATION_STRATEGY_TYPE, "popup">;
  };
  nftCheckoutPlugin: {
    enable: boolean;
  };
  useAccountAbstractionProvider: boolean;
  useAAWithExternalWallet?: boolean;
  smartAccountType?: SmartAccountType;
  smartAccountChains: string[];
  smartAccountChainsConfig: Record<string, { bundlerUrl: string; paymasterUrl: string }>;
  widget?: WidgetType;
  targetId?: string;
};

export const getV4TypedData = (chainId: string): SignTypedDataMessageV4 => ({
  types: {
    // EIP712Domain: [
    //   {
    //     name: "name",
    //     type: "string",
    //   },
    //   {
    //     name: "version",
    //     type: "string",
    //   },
    //   {
    //     name: "chainId",
    //     type: "uint256",
    //   },
    //   {
    //     name: "verifyingContract",
    //     type: "address",
    //   },
    // ],
    Person: [
      { name: "name", type: "string" },
      { name: "wallet", type: "address" },
    ],
    Mail: [
      { name: "from", type: "Person" },
      { name: "to", type: "Person" },
      { name: "contents", type: "string" },
    ],
  },
  domain: {
    name: "Ether Mail",
    version: "1",
    chainId: Number(chainId),
    verifyingContract: "0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC",
  },
  message: {
    from: {
      name: "Cow",
      wallet: "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826",
    },
    to: {
      name: "Bob",
      wallet: "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB",
    },
    contents: "Hello, Bob!",
  },
});

export const confirmationStrategyOptions: { name: string; value: string }[] = [
  { name: "Modal", value: CONFIRMATION_STRATEGY.MODAL },
  { name: "Auto Approve", value: CONFIRMATION_STRATEGY.AUTO_APPROVE },
  { name: "Default", value: CONFIRMATION_STRATEGY.DEFAULT },
];

export const NFT_CHECKOUT_CONTRACT_ID = {
  FREE_MINT: "b5b4de3f-0212-11ef-a08f-0242ac190003",
  PAID_MINT: "d1145a8b-98ae-44e0-ab63-2c9c8371caff",
};

export const NFT_CHECKOUT_CLIENT_ID = "BHgArYmWwSeq21czpcarYh0EVq2WWOzflX-NTK-tY1-1pauPzHKRRLgpABkmYiIV_og9jAvoIxQ8L3Smrwe04Lw";



================================================
FILE: demo/vue-app-new/src/global.ts
================================================
import { Buffer } from "buffer";
import process from "process";
// window.global ||= window;

window.Buffer = Buffer;
window.process = process;



================================================
FILE: demo/vue-app-new/src/main.ts
================================================
import "./global";
import "./style.css";

import { VueQueryPlugin } from "@tanstack/vue-query";
import { createI18n, PathValue } from "petite-vue-i18n";
import { createApp } from "vue";

import App from "./App.vue";
import createIcons from "./plugins/iconPlugin";
import en from "./translations/en.json";
import vi from "./translations/vi.json";

const i18n = createI18n({
  locale: "en", // set locale
  fallbackLocale: "en",
  messages: { vi, en },
  legacy: false,
  messageResolver: (obj: unknown, path: string): PathValue | null => {
    const keys = path.split(".");
    const value = keys.reduce((acc, key) => {
      if (acc && typeof acc === "object" && key in acc) {
        return (acc as Record<string, unknown>)[key];
      }
      return null;
    }, obj);
    return value as PathValue;
  },
  fallbacker: (_: string, fallbackLocale: string): string => {
    return fallbackLocale;
  },
});

const app = createApp(App);

app.use(createIcons);
app.use(i18n);
app.use(VueQueryPlugin);
app.mount("#app");



================================================
FILE: demo/vue-app-new/src/MainView.vue
================================================
<script setup lang="ts">
import {
  authConnector,
  CHAIN_NAMESPACES,
  type ConnectorFn,
  type CustomChainConfig,
  nftCheckoutPlugin,
  type PluginFn,
  storageAvailable,
  type UIConfig,
  WALLET_CONNECTORS,
  walletServicesPlugin,
  type AccountAbstractionMultiChainConfig,
  type Web3AuthOptions,
  type ConnectorsModalConfig,
  type LoginMethodConfig,
} from "@web3auth/modal";

import { type Web3AuthContextConfig, Web3AuthProvider } from "@web3auth/modal/vue";
import { WagmiProvider } from "@web3auth/modal/vue/wagmi";
import { coinbaseConnector } from "@web3auth/no-modal/connectors/coinbase-connector";
import { computed, onBeforeMount, ref, watch } from "vue";

import { type AUTH_CONNECTION_TYPE, BUILD_ENV } from "@web3auth/auth";
import AppDashboard from "./components/AppDashboard.vue";
import AppHeader from "./components/AppHeader.vue";
import AppSettings from "./components/AppSettings.vue";
import { clientIds, NFT_CHECKOUT_CLIENT_ID } from "./config";
import { formDataStore } from "./store/form";
import { getChainConfig } from "./utils/chainconfig";
import { SmartAccountType } from "@toruslabs/ethereum-controllers";

const formData = formDataStore;

const externalConnectors = ref<ConnectorFn[]>([]);

const showAAProviderSettings = computed(() => formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155));

// Options for reinitializing the web3Auth object
const options = computed((): Web3AuthOptions => {
  const { config: whiteLabel, enable: enabledWhiteLabel } = formData.whiteLabel;

  // Account Abstraction
  const { useAccountAbstractionProvider } = formData;
  let accountAbstractionConfig: Web3AuthOptions["accountAbstractionConfig"];
  if (showAAProviderSettings.value && useAccountAbstractionProvider) {
    const chains: AccountAbstractionMultiChainConfig["chains"] = [];
    Object.entries(formData.smartAccountChainsConfig).forEach(([chainId, { bundlerUrl, paymasterUrl }]) => {
      if (formData.chains.includes(chainId)) {
        chains.push({
          chainId,
          bundlerConfig: { url: bundlerUrl },
          paymasterConfig: paymasterUrl ? { url: paymasterUrl } : undefined,
          smartAccountConfig: undefined,
        });
      }
    });
    accountAbstractionConfig = {
      smartAccountType: formData.smartAccountType as SmartAccountType,
      chains,
    };
  }

  // Wallet services settings
  let walletServicesConfig: Web3AuthOptions["walletServicesConfig"] = {
    // walletUrls: {
    //   production: {
    //     url: "http://localhost:4050",
    //   },
    // },
  };
  if (formData.walletPlugin.enable) {
    const { confirmationStrategy } = formData.walletPlugin;
    walletServicesConfig = {
      ...walletServicesConfig,
      whiteLabel: { showWidgetButton: true },
      confirmationStrategy,
    };
  }

  // Plugins
  const plugins: PluginFn[] = [];
  if (formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155) || formData.chainNamespaces.includes(CHAIN_NAMESPACES.SOLANA)) {
    if (formData.nftCheckoutPlugin.enable && formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155)) {
      plugins.push(nftCheckoutPlugin({ clientId: NFT_CHECKOUT_CLIENT_ID }));
    }
    if (formData.walletPlugin.enable) {
      plugins.push(walletServicesPlugin());
    }
  }

  // Chains
  const chains: CustomChainConfig[] = [];
  for (const namespace of formData.chainNamespaces) {
    for (const chainId of formData.chains) {
      const chain = getChainConfig(namespace, chainId, clientIds[formData.network]);
      if (!chain) continue;
      // we need to validate chain id as legacy Solana chainIds 0x1, 0x2, 0x3 are not valid anymore
      if (chain.chainId !== chainId) continue;
      if (namespace === CHAIN_NAMESPACES.SOLANA) {
        if (chainId === "0x65") {
          chain.rpcTarget = import.meta.env.VITE_APP_SOLANA_MAINNET_RPC || chain.rpcTarget;
        } else if (chainId === "0x66") {
          chain.rpcTarget = import.meta.env.VITE_APP_SOLANA_TESTNET_RPC || chain.rpcTarget;
        } else if (chainId === "0x67") {
          chain.rpcTarget = import.meta.env.VITE_APP_SOLANA_DEVNET_RPC || chain.rpcTarget;
        }
      }
      chains.push(chain);
    }
  }

  const { widget, targetId } = formData;
  const uiConfig: Web3AuthOptions["uiConfig"] = enabledWhiteLabel
    ? { ...whiteLabel, widgetType: widget, targetId }
    : { widgetType: widget, targetId };
  const authConnectorInstance = authConnector({ connectorSettings: {} });

  return {
    clientId: clientIds[formData.network],
    web3AuthNetwork: formData.network,
    uiConfig: uiConfig as UIConfig,
    accountAbstractionConfig,
    useAAWithExternalWallet: formData.useAAWithExternalWallet,
    // TODO: Add more options
    // enableLogging?: boolean;
    // storageType?: "session" | "local";
    // sessionTime?: number;
    // useSFAKey?: boolean;
    chains,
    defaultChainId: formData.defaultChainId,
    enableLogging: true,
    authBuildEnv: BUILD_ENV.PRODUCTION, // Custom build env
    connectors: [...externalConnectors.value, authConnectorInstance],
    plugins,
    multiInjectedProviderDiscovery: formData.multiInjectedProviderDiscovery,
    walletServicesConfig,
    modalConfig: {
      connectors: modalParams.value,
      hideWalletDiscovery: !formData.showWalletDiscovery,
    },
  };
});

const loginMethodsConfig = computed(() => {
  const customConfig = {
    email_passwordless: {
      authConnectionId: `w3a-custom-email-${formData.network.replace("_", "-")}`,
    },
    sms_passwordless: {
      authConnectionId: `w3a-custom-sms-${formData.network.replace("_", "-")}`,
    },
  };
  if (formData.loginProviders.length === 0) return customConfig;

  // only show login methods that are configured
  const config = formData.loginProviders.reduce((acc, provider) => {
    acc[provider] = formData.loginMethods[provider];
    return acc;
  }, {} as LoginMethodConfig);

  if (config.email_passwordless) {
    config.email_passwordless.authConnectionId = `w3a-custom-email-${formData.network.replace("_", "-")}`;
  }
  if (config.sms_passwordless) {
    config.sms_passwordless.authConnectionId = `w3a-custom-sms-${formData.network.replace("_", "-")}`;
  }

  const loginMethods: LoginMethodConfig = JSON.parse(JSON.stringify(config));
  return loginMethods;
});

const modalParams = computed(() => {
  const modalConfig = {
    [WALLET_CONNECTORS.AUTH]: {
      label: "auth",
      loginMethods: loginMethodsConfig.value,
    },
  } as ConnectorsModalConfig["connectors"];
  return modalConfig;
});

const getExternalAdapterByName = (name: string): ConnectorFn[] => {
  switch (name) {
    case "coinbase":
      return [coinbaseConnector()];
    default:
      return [];
  }
};

onBeforeMount(() => {
  if (storageAvailable("sessionStorage")) {
    const storedValue = sessionStorage.getItem("state");
    try {
      if (storedValue) {
        const json = JSON.parse(storedValue);
        formData.connectors = json.connectors;
        formData.chains = json.chains;
        formData.chainNamespaces = json.chainNamespaces;
        formData.loginProviders = json.loginProviders;
        formData.showWalletDiscovery = json.showWalletDiscovery;
        formData.multiInjectedProviderDiscovery = json.multiInjectedProviderDiscovery;
        formData.network = json.network;
        formData.whiteLabel = json.whiteLabel;
        formData.walletPlugin = json.walletPlugin;
        formData.nftCheckoutPlugin = json.nftCheckoutPlugin || {};
        formData.useAccountAbstractionProvider = json.useAccountAbstractionProvider;
        formData.smartAccountType = json.smartAccountType;
        formData.smartAccountChains = json.smartAccountChains || [];
        formData.smartAccountChainsConfig = json.smartAccountChainsConfig || {};
        formData.defaultChainId = json.defaultChainId;
      }
    } catch (error) {}
  }
});

watch(formData, () => {
  if (storageAvailable("sessionStorage")) sessionStorage.setItem("state", JSON.stringify(formData));
});

// Every time the form data changes, reinitialize the web3Auth object
watch(
  () => formData.connectors,
  async () => {
    let connectors: ConnectorFn[] = [];
    for (let i = 0; i <= formData.connectors.length; i += 1) {
      connectors = connectors.concat(getExternalAdapterByName(formData.connectors[i]));
    }
    externalConnectors.value = connectors;
  }
);

const configs = computed<Web3AuthContextConfig>(() => {
  return {
    web3AuthOptions: options.value,
  };
});
</script>

<template>
  <Web3AuthProvider :config="configs">
    <WagmiProvider>
      <AppHeader />
      <div class="flex flex-col items-center justify-center">
        <main class="relative flex flex-col lg:h-[calc(100dvh_-_110px)]">
          <AppSettings />
          <AppDashboard :chains="options.chains || []" />
        </main>
      </div>
    </WagmiProvider>
  </Web3AuthProvider>
</template>



================================================
FILE: demo/vue-app-new/src/style.css
================================================
@tailwind base;
@tailwind components;
@tailwind utilities;

body {
  @apply h-dvh min-h-dvh w-full flex flex-col;
}
 #app {
  @apply h-full w-full;
 }



================================================
FILE: demo/vue-app-new/src/vite-env.d.ts
================================================
/// <reference types="vite/client" />



================================================
FILE: demo/vue-app-new/src/components/AppDashboard.vue
================================================
<script setup lang="ts">
import { Button, Card } from "@toruslabs/vue-components";
import { CHAIN_NAMESPACES, IProvider, log, WALLET_CONNECTORS, WALLET_PLUGINS } from "@web3auth/modal";
import {
  useCheckout,
  useEnableMFA,
  useIdentityToken,
  useManageMFA,
  useWalletConnectScanner,
  useWalletUI,
  useWeb3Auth,
  useWeb3AuthUser,
  useSwitchChain as useWeb3AuthSwitchChain,
} from "@web3auth/modal/vue";
import { type CustomChainConfig, type NFTCheckoutPluginType } from "@web3auth/no-modal";
import { useI18n } from "petite-vue-i18n";

import { useSignAndSendTransaction, useSignMessage as useSolanaSignMessage, useSignTransaction, useSolanaWallet } from "@web3auth/modal/vue/solana";
import { useAccount, useBalance, useChainId, useSignMessage, useSignTypedData, useSwitchChain as useWagmiSwitchChain } from "@wagmi/vue";

import { LAMPORTS_PER_SOL, PublicKey, SystemProgram, Transaction } from "@solana/web3.js";
import { ProviderConfig } from "@toruslabs/base-controllers";
import { SUPPORTED_NETWORKS } from "@toruslabs/ethereum-controllers";
import { computed, ref, watch } from "vue";
import { NFT_CHECKOUT_CONTRACT_ID } from "../config";
import { getPrivateKey, sendEth, sendEthWithSmartAccount, signTransaction as signEthTransaction } from "../services/ethHandlers";
import { getBalance as getSolBalance, getPrivateKey as getSolPrivateKey, signAllTransactions } from "../services/solHandlers";
import { formDataStore } from "../store/form";
import { SOLANA_SUPPORTED_NETWORKS } from "../utils/constants";

const supportedNetworks = { ...SUPPORTED_NETWORKS, ...SOLANA_SUPPORTED_NETWORKS } as Record<string, ProviderConfig>;

const { t } = useI18n({ useScope: "global" });

const formData = formDataStore;

const props = defineProps<{
  chains: CustomChainConfig[];
}>();

const { isConnected, provider, web3Auth, isMFAEnabled } = useWeb3Auth();
const { userInfo, loading: userInfoLoading } = useWeb3AuthUser();
const { enableMFA } = useEnableMFA();
const { manageMFA } = useManageMFA();
const { switchChainAsync } = useWagmiSwitchChain();
const { switchChain } = useWeb3AuthSwitchChain();
const { showWalletUI, loading: showWalletUILoading } = useWalletUI();
const { showWalletConnectScanner, loading: showWalletConnectScannerLoading } = useWalletConnectScanner();
const { showCheckout, loading: showCheckoutLoading } = useCheckout();
const { getIdentityToken, loading: getIdentityTokenLoading } = useIdentityToken();
const { status, address } = useAccount();
const { signTypedDataAsync } = useSignTypedData();
const { signMessageAsync } = useSignMessage();
const wagmiChainId = useChainId();
const balance = useBalance({
  address: address,
});

const { accounts: solanaAccounts, connection } = useSolanaWallet();
const { signMessage: signSolanaMessage } = useSolanaSignMessage();
const { signTransaction: signSolTransaction } = useSignTransaction();
const { signAndSendTransaction } = useSignAndSendTransaction();

const currentChainId = ref<string | undefined>(web3Auth.value?.currentChain?.chainId);
const currentChainConfig = computed(() => supportedNetworks[currentChainId.value as keyof typeof supportedNetworks]);
const currentChainNamespace = computed(() => currentChainConfig.value?.chainNamespace);

const chainChangedListener = (chainId: string) => {
  currentChainId.value = chainId;
};

watch(
  isConnected,
  (newIsConnected, _, onCleanup) => {
    if (!newIsConnected || !provider.value) return;
    currentChainId.value = web3Auth.value?.currentChain?.chainId;
    provider.value.on("chainChanged", chainChangedListener);
    onCleanup(() => {
      provider.value?.off("chainChanged", chainChangedListener);
    });
  },
  {
    immediate: true,
  }
);

const isDisplay = (name: "dashboard" | "ethServices" | "solServices" | "walletServices" | "nftCheckoutServices"): boolean => {
  const chainNamespace = currentChainNamespace.value;
  switch (name) {
    case "dashboard":
      return isConnected.value;

    case "ethServices":
      return chainNamespace === CHAIN_NAMESPACES.EIP155;

    case "solServices":
      return chainNamespace === CHAIN_NAMESPACES.SOLANA;

    case "walletServices":
      return (
        (chainNamespace === CHAIN_NAMESPACES.EIP155 || chainNamespace === CHAIN_NAMESPACES.SOLANA) &&
        web3Auth.value?.connectedConnectorName === WALLET_CONNECTORS.AUTH
      );

    case "nftCheckoutServices":
      return chainNamespace === CHAIN_NAMESPACES.EIP155 && formData.nftCheckoutPlugin.enable;

    default: {
      return false;
    }
  }
};

const clearConsole = () => {
  const el = document.querySelector("#console>pre");
  const h1 = document.querySelector("#console>h1");
  const consoleBtn = document.querySelector<HTMLElement>("#console>div.clear-console-btn");
  if (h1) {
    h1.innerHTML = "";
  }
  if (el) {
    el.innerHTML = "";
  }
  if (consoleBtn) {
    consoleBtn.style.display = "none";
  }
};

const printToConsole = (...args: unknown[]) => {
  const el = document.querySelector("#console>pre");
  const h1 = document.querySelector("#console>h1");
  const consoleBtn = document.querySelector<HTMLElement>("#console>div.clear-console-btn");
  if (h1) {
    h1.innerHTML = args[0] as string;
  }
  if (el) {
    el.innerHTML = JSON.stringify(args[1] || {}, null, 2);
  }
  if (consoleBtn) {
    consoleBtn.style.display = "block";
  }
};

watch(
  status,
  (newStatus) => {
    console.log("wagmi status", newStatus);
  },
  { immediate: true }
);

// NFT Checkout
const showPaidMintNFTCheckout = async () => {
  const nftCheckoutPlugin = web3Auth.value?.getPlugin(WALLET_PLUGINS.NFT_CHECKOUT) as NFTCheckoutPluginType;
  nftCheckoutPlugin.show({ contractId: NFT_CHECKOUT_CONTRACT_ID.PAID_MINT });
};
const showFreeMintNFTCheckout = async () => {
  const nftCheckoutPlugin = web3Auth.value?.getPlugin(WALLET_PLUGINS.NFT_CHECKOUT) as NFTCheckoutPluginType;
  nftCheckoutPlugin.show({ contractId: NFT_CHECKOUT_CONTRACT_ID.FREE_MINT });
};

// Ethereum Provider
const onGetUserInfo = async () => {
  printToConsole("User Info", userInfo.value);
};

const ongetIdentityToken = async () => {
  const idToken = await getIdentityToken();
  printToConsole("id token", idToken);
};

const onSendEth = async () => {
  await sendEth(provider.value as IProvider, printToConsole);
};

const onSignEthMessage = async () => {
  const result = await signMessageAsync({
    message: "Hello, Bob!",
  });
  printToConsole("result", result);
};

const onGetAccounts = async () => {
  printToConsole("account", address.value);
};

const onGetPrivateKey = async () => {
  await getPrivateKey(provider.value as IProvider, printToConsole);
};

const getConnectedChainId = async () => {
  printToConsole("chainId", wagmiChainId.value);
};

const onGetBalance = async () => {
  const data = await balance.refetch();
  printToConsole("balance", data.data?.value.toString());
};

const onSignEthTransaction = async () => {
  await signEthTransaction(provider.value as IProvider, printToConsole);
};

const onSignTypedData_v4 = async () => {
  const result = await signTypedDataAsync({
    types: {
      Person: [
        { name: "name", type: "string" },
        { name: "wallet", type: "address" },
      ],
      Mail: [
        { name: "from", type: "Person" },
        { name: "to", type: "Person" },
        { name: "contents", type: "string" },
      ],
    },
    primaryType: "Mail",
    message: {
      from: {
        name: "Cow",
        wallet: "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826",
      },
      to: {
        name: "Bob",
        wallet: "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB",
      },
      contents: "Hello, Bob!",
    },
  });
  printToConsole("result", result);
};

const onSignPersonalMsg = async () => {
  const result = await signMessageAsync({
    message: "Hello, Bob!",
  });
  printToConsole("result", result);
};

const isSmartAccount = computed(() => {
  return web3Auth.value?.accountAbstractionProvider?.smartAccount && web3Auth.value?.accountAbstractionProvider?.bundlerClient;
});

const onSendAATx = async () => {
  await sendEthWithSmartAccount(web3Auth.value, printToConsole);
};

// Solana
const onGetSolPrivateKey = async () => {
  await getSolPrivateKey(provider.value as IProvider, printToConsole);
};

const onSignAndSendTransaction = async () => {
  if (!solanaAccounts.value) throw new Error("No account connected");
  if (!connection.value) throw new Error("No connection");
  const block = await connection.value?.getLatestBlockhash("finalized");
  const pubKey = solanaAccounts.value[0];

  const transactionInstruction = SystemProgram.transfer({
    fromPubkey: new PublicKey(pubKey),
    toPubkey: new PublicKey(pubKey),
    lamports: 0.01 * LAMPORTS_PER_SOL,
  });

  const transaction = new Transaction({
    blockhash: block.blockhash,
    lastValidBlockHeight: block.lastValidBlockHeight,
    feePayer: new PublicKey(pubKey),
  }).add(transactionInstruction);

  const data = await signAndSendTransaction(transaction);
  printToConsole("result", data);
};

const onSignSolTransaction = async () => {
  if (!solanaAccounts.value) throw new Error("No account connected");
  if (!connection.value) throw new Error("No connection");
  const block = await connection.value?.getLatestBlockhash("finalized");
  const pubKey = solanaAccounts.value[0];

  const transactionInstruction = SystemProgram.transfer({
    fromPubkey: new PublicKey(pubKey),
    toPubkey: new PublicKey(pubKey),
    lamports: 0.01 * LAMPORTS_PER_SOL,
  });

  const transaction = new Transaction({
    blockhash: block.blockhash,
    lastValidBlockHeight: block.lastValidBlockHeight,
    feePayer: new PublicKey(pubKey),
  }).add(transactionInstruction);

  const result = await signSolTransaction(transaction);
  printToConsole("result", result);
};

const onSignSolMessage = async () => {
  const result = await signSolanaMessage("Hello, Bob!");
  printToConsole("result", result);
};

const onGetSolBalance = async () => {
  await getSolBalance(provider.value as IProvider, printToConsole);
};

const onSignAllTransactions = async () => {
  await signAllTransactions(provider.value as IProvider, printToConsole);
};

// Common
const canSwitchChain = computed(() => {
  const currentNamespace = currentChainNamespace.value;
  const newChain = props.chains.find((x) => x.chainNamespace === currentNamespace && x.chainId !== currentChainId.value);
  return Boolean(newChain);
});

const canSwitchChainNamespace = computed(() => {
  const currentNamespace = currentChainNamespace.value;
  if (currentNamespace !== CHAIN_NAMESPACES.EIP155 && currentNamespace !== CHAIN_NAMESPACES.SOLANA) return false;

  const newNamespace = currentNamespace === CHAIN_NAMESPACES.EIP155 ? CHAIN_NAMESPACES.SOLANA : CHAIN_NAMESPACES.EIP155;
  const newChain = props.chains.find((x) => x.chainNamespace === newNamespace);
  return Boolean(newChain);
});

const onSwitchChain = async () => {
  log.info("switching chain");
  try {
    const { chainId } = provider.value as IProvider;
    if (chainId !== currentChainId.value) throw new Error("chainId does not match current chainId");

    const currentNamespace = currentChainNamespace.value;
    const newChain = props.chains.find((x) => x.chainNamespace === currentNamespace && x.chainId !== chainId);
    if (!newChain) throw new Error(`Please configure at least 2 chains for ${currentNamespace} in the config`);
    const data = await switchChainAsync({ chainId: Number(newChain.chainId) });
    printToConsole("switchedChain", { chainId: data.id });
  } catch (error) {
    printToConsole("switchedChain error", error);
  }
};

const onSwitchChainNamespace = async () => {
  log.info("switching chain namespace");
  try {
    const chainNamespace = currentChainNamespace.value;
    if (chainNamespace !== CHAIN_NAMESPACES.EIP155 && chainNamespace !== CHAIN_NAMESPACES.SOLANA)
      throw new Error("switching to differnt chainNamespaces is not supported for current chainNamespace");
    const newChainNamespace = chainNamespace === CHAIN_NAMESPACES.EIP155 ? CHAIN_NAMESPACES.SOLANA : CHAIN_NAMESPACES.EIP155;
    const supportedChains = props.chains || [];
    const newChain = supportedChains.find((chain) => chain.chainNamespace === newChainNamespace);

    if (!newChain) throw new Error(`chain namespace ${newChainNamespace} not supported, please configure this chain namespace in the config`);
    await switchChain({ chainId: newChain.chainId });
    printToConsole("switchedChainNamespace", { chainId: newChain.chainId, chainNamespace: newChainNamespace });
  } catch (error) {
    printToConsole("switchedChainNamespace error", error);
  }
};
</script>

<template>
  <div v-if="isDisplay('dashboard')" class="w-full h-full px-10">
    <div class="grid h-full grid-cols-1 md:grid-cols-4 lg:grid-cols-6">
      <Card class="px-4 py-4 grid col-span-1 lg:col-span-2 h-full !rounded-3xl md:!rounded-r-none !shadow-none">
        <div class="mb-2">
          <Button block size="xs" pill variant="tertiary" data-testid="btnClearConsole" @click="clearConsole">
            {{ $t("app.buttons.btnClearConsole") }}
          </Button>
        </div>
        <div class="mb-2">
          <Button :loading="userInfoLoading" block size="xs" pill @click="onGetUserInfo">
            {{ $t("app.buttons.btnGetUserInfo") }}
          </Button>

          <Button
            class="my-2"
            block
            size="xs"
            pill
            @click="
              () => {
                if (isMFAEnabled) {
                  manageMFA();
                } else {
                  enableMFA();
                }
              }
            "
          >
            {{ isMFAEnabled ? "Manage MFA" : "Enable MFA" }}
          </Button>
        </div>
        <!-- Wallet Services -->
        <Card v-if="isDisplay('walletServices')" class="!h-auto lg:!h-[calc(100dvh_-_240px)] gap-4 px-4 py-4 mb-2" :shadow="false">
          <div class="mb-2 text-xl font-bold leading-tight text-left">Wallet Service</div>
          <Button :loading="showWalletUILoading" block size="xs" pill class="mb-2" @click="() => showWalletUI()">
            {{ $t("app.buttons.btnShowWalletUI") }}
          </Button>
          <Button :loading="showWalletConnectScannerLoading" block size="xs" pill class="mb-2" @click="() => showWalletConnectScanner()">
            {{ $t("app.buttons.btnShowWalletConnectScanner") }}
          </Button>
          <Button :loading="showCheckoutLoading" block size="xs" pill class="mb-2" @click="() => showCheckout()">
            {{ $t("app.buttons.btnShowCheckout") }}
          </Button>
          <!-- <Button v-if="isDisplay('ethServices')" block size="xs" pill class="mb-2" @click="onWalletSignPersonalMessage">
            {{ t("app.buttons.btnSignPersonalMsg") }}
          </Button>
          <Button v-if="isDisplay('ethServices')" block size="xs" pill class="mb-2" @click="onWalletSignTypedData_v4">
            {{ t("app.buttons.btnSignTypedData_v4") }}
          </Button>
          <Button v-if="isDisplay('ethServices')" block size="xs" pill class="mb-2" @click="onWalletSendEth">{{ t("app.buttons.btnSendEth") }}</Button>

          <Button v-if="isDisplay('solServices')" block size="xs" pill class="mb-2" @click="onWalletSignSolanaMessage">
            {{ t("app.buttons.btnSignMessage") }}
          </Button>
          <Button v-if="isDisplay('solServices')" block size="xs" pill class="mb-2" @click="onWalletSignSolanaVersionedTransaction">
            {{ t("app.buttons.btnSignTransaction") }}
          </Button> -->
        </Card>

        <!-- NFT Checkout -->
        <Card v-if="isDisplay('nftCheckoutServices')" class="!h-auto lg:!h-[calc(100dvh_-_240px)] gap-4 px-4 py-4 mb-2" :shadow="false">
          <div class="mb-2 text-xl font-bold leading-tight text-left">NFT Checkout Service</div>
          <Button block size="xs" pill class="mb-2" @click="showFreeMintNFTCheckout">
            {{ $t("app.buttons.btnShowFreeMintNFTCheckout") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="showPaidMintNFTCheckout">
            {{ $t("app.buttons.btnShowPaidMintNFTCheckout") }}
          </Button>
        </Card>

        <!-- EVM -->
        <Card v-if="isDisplay('ethServices')" class="px-4 py-4 gap-4 !h-auto lg:!h-[calc(100dvh_-_240px)]" :shadow="false">
          <div class="mb-2 text-xl font-bold leading-tight text-left">Sample Transaction</div>
          <Button block size="xs" pill class="mb-2" @click="onGetAccounts">
            {{ t("app.buttons.btnGetAccounts") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onGetPrivateKey">
            {{ t("app.buttons.btnGetPrivateKey") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onGetBalance">
            {{ t("app.buttons.btnGetBalance") }}
          </Button>
          <Button v-if="canSwitchChain" block size="xs" pill class="mb-2" @click="onSwitchChain">{{ t("app.buttons.btnSwitchChain") }}</Button>
          <Button v-if="canSwitchChainNamespace" block size="xs" pill class="mb-2" @click="onSwitchChainNamespace">
            {{ t("app.buttons.btnSwitchChainNamespace") }} to Solana
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onSendEth">{{ t("app.buttons.btnSendEth") }}</Button>
          <Button v-if="isSmartAccount" block size="xs" pill class="mb-2" @click="onSendAATx">{{ t("app.buttons.btnSendAATx") }}</Button>
          <Button block size="xs" pill class="mb-2" @click="onSignEthTransaction">
            {{ t("app.buttons.btnSignTransaction") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onSignEthMessage">{{ t("app.buttons.btnSignEthMessage") }}</Button>
          <Button block size="xs" pill class="mb-2" @click="getConnectedChainId">
            {{ t("app.buttons.btnGetConnectedChainId") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onSignTypedData_v4">
            {{ t("app.buttons.btnSignTypedData_v4") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onSignPersonalMsg">
            {{ t("app.buttons.btnSignPersonalMsg") }}
          </Button>
          <Button :loading="getIdentityTokenLoading" block size="xs" pill class="mb-2" @click="ongetIdentityToken">Get id token</Button>
        </Card>

        <!-- SOLANA -->
        <Card v-if="isDisplay('solServices')" class="h-auto gap-4 px-4 py-4 mb-2" :shadow="false">
          <div class="mb-2 text-xl font-bold leading-tight text-left">Sample Transaction</div>
          <Button block size="xs" pill class="mb-2" @click="onGetSolPrivateKey">{{ t("app.buttons.btnGetPrivateKey") }}</Button>
          <Button v-if="canSwitchChain" block size="xs" pill class="mb-2" @click="onSwitchChain">{{ t("app.buttons.btnSwitchChain") }}</Button>
          <Button v-if="canSwitchChainNamespace" block size="xs" pill class="mb-2" @click="onSwitchChainNamespace">
            {{ t("app.buttons.btnSwitchChainNamespace") }} to EVM
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onGetSolBalance">{{ t("app.buttons.btnGetBalance") }}</Button>
          <Button block size="xs" pill class="mb-2" @click="onSignSolMessage">{{ t("app.buttons.btnSignMessage") }}</Button>
          <Button block size="xs" pill class="mb-2" @click="onSignAndSendTransaction">
            {{ t("app.buttons.btnSignAndSendTransaction") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onSignSolTransaction">
            {{ t("app.buttons.btnSignTransaction") }}
          </Button>
          <Button block size="xs" pill class="mb-2" @click="onSignAllTransactions">
            {{ t("app.buttons.btnSignAllTransactions") }}
          </Button>
          <Button :loading="getIdentityTokenLoading" block size="xs" pill class="mb-2" @click="ongetIdentityToken">Get id token</Button>
        </Card>
      </Card>
      <Card
        id="console"
        class="px-4 py-4 col-span-1 md:col-span-3 lg:col-span-4 overflow-y-auto h-full !rounded-3xl md:!rounded-l-none md:!border-l-0 !shadow-none"
      >
        <pre class="max-h-screen overflow-x-auto overflow-y-auto text-base font-normal leading-6 text-black break-words whitespace-pre-line"></pre>
      </Card>
    </div>
  </div>
</template>



================================================
FILE: demo/vue-app-new/src/components/AppHeader.vue
================================================
<script setup lang="ts">
import { Button } from "@toruslabs/vue-components";
import { useWeb3Auth, useWeb3AuthDisconnect } from "@web3auth/modal/vue";
import { useI18n } from "petite-vue-i18n";
import { watch } from "vue";

const { log } = console;
const { t } = useI18n({ useScope: "global" });

const { status, isConnected } = useWeb3Auth();
const { disconnect } = useWeb3AuthDisconnect();

const isDisplay = (name: string): boolean => {
  switch (name) {
    case "btnLogout":
      return isConnected.value;

    case "appHeading":
      return isConnected.value;

    default: {
      return false;
    }
  }
};

watch(status, () => {
  log("status :::::::::::::::::::::::::::", status.value);
});
</script>

<template>
  <nav class="bg-white sticky w-full z-20 top-0 start-0 border-gray-200 dark:border-gray-600">
    <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <a href="#" class="flex items-center space-x-3 rtl:space-x-reverse">
        <img :src="`/web3auth.svg`" class="h-8" alt="W3A Logo" />
      </a>
      <div class="flex md:order-2 space-x-3 md:space-x-0 rtl:space-x-reverse">
        <Button v-if="isDisplay('btnLogout')" block size="xs" pill variant="tertiary" @click="() => disconnect()">
          {{ t("app.btnLogout") }}
        </Button>
        <Button v-else block size="xs" pill variant="secondary" @click="() => {}">
          {{ t("app.documentation") }}
        </Button>
      </div>
      <div id="navbar-sticky" class="items-center justify-between w-full md:flex md:w-auto md:order-1 text-center">
        <div v-if="isDisplay('appHeading')" class="max-sm:w-full max-sm:mt-4">
          <h1 class="leading-tight text-2xl sm:text-3xl font-bold">{{ $t("app.title") }}</h1>
          <p class="leading-tight text-lg sm:text-xl">{{ $t("app.description") }}</p>
        </div>
      </div>
    </div>
  </nav>
</template>



================================================
FILE: demo/vue-app-new/src/components/AppSettings.vue
================================================
<script setup lang="ts">
import { Button, Card, Select, Tab, Tabs, Tag, TextField, Toggle } from "@toruslabs/vue-components";
import { CHAIN_NAMESPACES, ChainNamespaceType, CONNECTOR_STATUS, log } from "@web3auth/modal";
import { useWeb3Auth, useWeb3AuthConnect } from "@web3auth/modal/vue";
import { computed, InputHTMLAttributes, ref } from "vue";
import {
  chainConfigs,
  chainNamespaceOptions,
  clientIds,
  confirmationStrategyOptions,
  getDefaultBundlerUrl,
  languageOptions,
  loginProviderOptions,
  networkOptions,
  SmartAccountOptions,
} from "../config";
import { formDataStore } from "../store/form";
import { getChainConfig } from "../utils/chainconfig";

const formData = formDataStore;

const { status, isConnected, isInitialized } = useWeb3Auth();
const { connect } = useWeb3AuthConnect();

const chainOptions = computed(() => {
  const allChains: { name: string; value: string }[] = [];
  formData.chainNamespaces.forEach((namespace: ChainNamespaceType) => {
    const chainsForNamespace = chainConfigs[namespace].map((chainId) => {
      const chainConfig = getChainConfig(namespace, chainId, clientIds[formData.network]);
      if (!chainConfig) {
        throw new Error(`Chain config not found for chainId: ${chainId}`);
      }
      return {
        name: `${chainId} ${chainConfig.displayName}`,
        value: chainId,
      };
    });
    allChains.push(...chainsForNamespace);
  });
  return allChains;
});

const defaultChainOptions = computed(() => {
  return formData.chains.map((chain) => ({ name: chain, value: chain }));
});

const aaSupportedChains = computed(() => {
  return formData.chains
    .map((chainId) => {
      return getChainConfig(CHAIN_NAMESPACES.EIP155, chainId, clientIds[formData.network]);
    })
    .filter((chainConfig) => chainConfig)
    .map((chainConfig) => ({ name: `${chainConfig!.chainId} ${chainConfig!.displayName}`, value: chainConfig!.chainId }));
});

const connectorOptions = computed(() =>
  formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155) ? [{ name: "coinbase-connector", value: "coinbase" }] : []
);

const isDisplay = (_name: string): boolean => {
  return !isConnected.value;
};

const isDisabled = (name: string): boolean => {
  switch (name) {
    case "whiteLabelSettings":
      return !formData.whiteLabel.enable;

    case "walletServicePlugin":
      return !formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155) && !formData.chainNamespaces.includes(CHAIN_NAMESPACES.SOLANA);

    case "nftCheckoutPlugin":
      return !formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155);

    case "btnConnect":
      return !isInitialized.value;

    case "smartAccountType":
    case "smartAccountChains":
    case "bundlerUrl":
    case "paymasterUrl":
    case "useAAWithExternalWallet":
      return !formData.useAccountAbstractionProvider;

    case "accountAbstraction":
      return !formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155);

    default: {
      return false;
    }
  }
};

const activeTab = ref(0);
const onTabChange = (index: number) => {
  activeTab.value = index;
};
const isActiveTab = (index: number) => activeTab.value === index;

const onChainNamespaceChange = (value: string[]) => {
  log.info("onChainNamespaceChange", value);
  formData.chains = value.map((namespace) => chainConfigs[namespace as ChainNamespaceType][0]);
  onChainChange(formData.chains);
  formData.connectors = [];
};

const onChainChange = (chainIds: string[]) => {
  log.info("onChainChange", chainIds);
  // update default chain Id if not found in the new chains
  if (formData.defaultChainId && chainIds.includes(formData.defaultChainId)) {
    formData.defaultChainId = chainIds[0];
  }
  // update smart account chains if not found in the new chains
  formData.smartAccountChains = formData.smartAccountChains.filter((chain) => chainIds.includes(chain));
};

const onSmartAccountChainChange = (chainIds: string[]) => {
  log.info("onSmartAccountChainChange", chainIds);
  formData.smartAccountChainsConfig = {};
  for (const chainId of chainIds) {
    if (!formData.smartAccountChainsConfig[chainId]) {
      formData.smartAccountChainsConfig[chainId] = {
        bundlerUrl: getDefaultBundlerUrl(chainId),
        paymasterUrl: "",
      };
    }
  }
};
</script>

<template>
  <div class="flex !flex-col sm:!flex-row items-center justify-center gap-6 px-10 py-4">
    <div v-if="isDisplay('form')">
      <Card
        class="h-auto p-4 sm:p-8 col-span-8 sm:col-span-6 lg:col-span-4 max-sm:!shadow-none max-sm:!border-0 !w-full [@media(min-width:900px)]:!min-w-[700px] [@media(min-width:1200px)]:!min-w-[800px] [@media(min-width:1500px)]:!w-[800px]"
      >
        <div class="text-2xl font-bold leading-tight text-center sm:text-3xl">{{ $t("app.greeting") }}</div>
        <div class="my-4 font-extrabold leading-tight text-center flex items-center justify-center gap-2">
          <Select
            v-model="formData.widget"
            data-testid="selectWidget"
            :aria-label="$t('app.widget.title')"
            :placeholder="$t('app.widget.title')"
            matchParentsWidth
            :options="[
              { name: $t('app.widget.embed'), value: 'embed' },
              { name: $t('app.widget.modal'), value: 'modal' },
            ]"
            :classes="{
              container: '!w-[120px]',
            }"
          />
          <Tag v-bind="{ minWidth: 'inherit' }" :class="['uppercase', { '!bg-blue-400 text-white': status === CONNECTOR_STATUS.READY }]">
            {{ status }}
          </Tag>
          &nbsp;
          <Tag v-bind="{ minWidth: 'inherit' }" :class="['uppercase', { '!bg-blue-400 text-white': isInitialized }]">
            {{ isInitialized ? "INITIALIZED" : "NOT_INITIALIZE_YET" }}
          </Tag>
        </div>
        <Tabs class="mb-4">
          <Tab variant="underline" :active="isActiveTab(0)" @click="onTabChange(0)">General</Tab>
          <Tab variant="underline" :active="isActiveTab(1)" @click="onTabChange(1)">WhiteLabel</Tab>
          <Tab variant="underline" :active="isActiveTab(2)" @click="onTabChange(2)">Login Provider</Tab>
          <Tab
            v-if="formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155) || formData.chainNamespaces.includes(CHAIN_NAMESPACES.SOLANA)"
            variant="underline"
            :active="isActiveTab(3)"
            @click="onTabChange(3)"
          >
            Wallet Plugin
          </Tab>
          <Tab v-if="formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155)" variant="underline" :active="isActiveTab(4)" @click="onTabChange(4)">
            NFT Checkout Plugin
          </Tab>
          <Tab v-if="formData.chainNamespaces.includes(CHAIN_NAMESPACES.EIP155)" variant="underline" :active="isActiveTab(5)" @click="onTabChange(5)">
            Account Abstraction Provider
          </Tab>
        </Tabs>
        <Card v-if="isActiveTab(0)" class="grid grid-cols-1 gap-2 px-4 py-4" :shadow="false">
          <Select
            v-model="formData.network"
            data-testid="selectNetwork"
            :label="$t('app.network')"
            :aria-label="$t('app.network')"
            :placeholder="$t('app.network')"
            :options="networkOptions"
            matchParentsWidth
          />
          <Select
            v-model="formData.chainNamespaces"
            data-testid="selectChainNamespace"
            :label="$t('app.chainNamespaces')"
            :aria-label="$t('app.chainNamespaces')"
            :placeholder="$t('app.chainNamespaces')"
            :options="chainNamespaceOptions"
            :multiple="true"
            matchParentsWidth
            @update:model-value="onChainNamespaceChange"
          />
          <Select
            v-model="formData.chains"
            data-testid="selectChain"
            :label="$t('app.chains')"
            :aria-label="$t('app.chains')"
            :placeholder="$t('app.chains')"
            :multiple="true"
            matchParentsWidth
            :options="chainOptions"
            @update:model-value="onChainChange"
          />
          <Select
            v-model="formData.defaultChainId"
            data-testid="selectDefaultChainId"
            :label="$t('app.defaultChainId')"
            :aria-label="$t('app.defaultChainId')"
            :placeholder="$t('app.defaultChainId')"
            matchParentsWidth
            :options="defaultChainOptions"
          />
          <Select
            v-model="formData.connectors"
            data-testid="selectConnectors"
            :label="$t('app.connectors')"
            :aria-label="$t('app.connectors')"
            :placeholder="$t('app.connectors')"
            :options="connectorOptions"
            multiple
            matchParentsWidth
            :show-check-box="true"
          />
          <Toggle
            v-model="formData.showWalletDiscovery"
            data-testid="showWalletDiscovery"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.showWalletDiscovery')"
            :label-enabled="$t('app.showWalletDiscovery')"
            class="mb-2"
          />
          <Toggle
            v-model="formData.multiInjectedProviderDiscovery"
            data-testid="multiInjectedProviderDiscovery"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.multiInjectedProviderDiscovery')"
            :label-enabled="$t('app.multiInjectedProviderDiscovery')"
            class="mb-2"
          />
        </Card>
        <Card v-if="isActiveTab(1)" class="grid grid-cols-1 gap-2 px-4 py-4 sm:grid-cols-2" :shadow="false">
          <Toggle
            v-model="formData.whiteLabel.enable"
            data-testid="whitelabel"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.whiteLabel.title')"
            :label-enabled="$t('app.whiteLabel.title')"
            class="mb-2"
          />
          <Toggle
            id="useLogoLoader"
            v-model="formData.whiteLabel.config.useLogoLoader"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.whiteLabel.useLogoLoader')"
            :label-enabled="$t('app.whiteLabel.useLogoLoader')"
            :disabled="isDisabled('whiteLabelSettings')"
          />
          <TextField
            v-model="formData.whiteLabel.config.appName"
            :label="$t('app.whiteLabel.appName')"
            :aria-label="$t('app.whiteLabel.appName')"
            :placeholder="$t('app.whiteLabel.appName')"
            :disabled="isDisabled('whiteLabelSettings')"
          />
          <Select
            v-model="formData.whiteLabel.config.defaultLanguage"
            :label="$t('app.whiteLabel.defaultLanguage')"
            :aria-label="$t('app.whiteLabel.defaultLanguage')"
            :placeholder="$t('app.whiteLabel.defaultLanguage')"
            :options="languageOptions"
            matchParentsWidth
            :disabled="isDisabled('whiteLabelSettings')"
          />
          <TextField
            v-model="formData.whiteLabel.config.appUrl"
            :label="$t('app.whiteLabel.appUrl')"
            :aria-label="$t('app.whiteLabel.appUrl')"
            :placeholder="$t('app.whiteLabel.appUrl')"
            :disabled="isDisabled('whiteLabelSettings')"
            class="col-span-2"
          />
          <TextField
            v-model="formData.whiteLabel.config.logoLight"
            :label="$t('app.whiteLabel.logoLight')"
            :aria-label="$t('app.whiteLabel.logoLight')"
            :placeholder="$t('app.whiteLabel.logoLight')"
            :disabled="isDisabled('whiteLabelSettings')"
          />
          <TextField
            v-model="formData.whiteLabel.config.logoDark"
            :label="$t('app.whiteLabel.logoDark')"
            :aria-label="$t('app.whiteLabel.logoDark')"
            :placeholder="$t('app.whiteLabel.logoDark')"
            :disabled="isDisabled('whiteLabelSettings')"
          />

          <TextField
            :model-value="formData.whiteLabel.config.theme?.primary"
            :label="$t('app.whiteLabel.primaryColor')"
            :aria-label="$t('app.whiteLabel.primaryColor')"
            :placeholder="$t('app.whiteLabel.primaryColor')"
            :disabled="isDisabled('whiteLabelSettings')"
          >
            <template #endIconSlot>
              <input
                id="primary-color-picker"
                class="color-picker"
                type="color"
                :value="formData.whiteLabel.config.theme?.primary"
                @input="
                  (e) => {
                    const color = (e.target as InputHTMLAttributes).value;
                    formData.whiteLabel.config.theme = { ...formData.whiteLabel.config.theme, primary: color };
                  }
                "
              />
            </template>
          </TextField>
          <TextField
            :model-value="formData.whiteLabel.config.theme?.onPrimary"
            :label="$t('app.whiteLabel.onPrimaryColor')"
            :aria-label="$t('app.whiteLabel.onPrimaryColor')"
            :placeholder="$t('app.whiteLabel.onPrimaryColor')"
            :disabled="isDisabled('whiteLabelSettings')"
          >
            <template #endIconSlot>
              <input
                id="primary-color-picker"
                class="color-picker"
                type="color"
                :value="formData.whiteLabel.config.theme?.onPrimary"
                @input="
                  (e) => {
                    const color = (e.target as InputHTMLAttributes).value;
                    formData.whiteLabel.config.theme = { ...formData.whiteLabel.config.theme, onPrimary: color };
                  }
                "
              />
            </template>
          </TextField>
        </Card>
        <Card v-if="isActiveTab(2)" class="grid grid-cols-1 gap-2 px-4 py-4" :shadow="false">
          <Select
            v-model="formData.loginProviders"
            data-testid="selectLoginProviders"
            :label="$t('app.loginProviders')"
            :aria-label="$t('app.loginProviders')"
            :placeholder="$t('app.loginProviders')"
            :options="loginProviderOptions"
            multiple
            matchParentsWidth
            class=""
          />
          <Card v-for="p in formData.loginProviders" :key="p" :shadow="false" class="grid grid-cols-1 gap-2 px-4 py-4 sm:grid-cols-3">
            <div class="font-bold leading-tight text-left">{{ p }}</div>
            <Toggle
              v-model="formData.loginMethods[p]!.mainOption"
              :show-label="true"
              :size="'small'"
              :label-disabled="$t('app.loginMethod.mainOption')"
              :label-enabled="$t('app.loginMethod.mainOption')"
            />
            <Toggle
              v-model="formData.loginMethods[p]!.showOnModal"
              :show-label="true"
              :size="'small'"
              :label-disabled="$t('app.loginMethod.showOnModal')"
              :label-enabled="$t('app.loginMethod.showOnModal')"
            />
            <TextField
              v-model="formData.loginMethods[p]!.name"
              :label="$t('app.loginMethod.name')"
              :aria-label="$t('app.loginMethod.name')"
              :placeholder="$t('app.loginMethod.name')"
            />
            <TextField
              v-model="formData.loginMethods[p]!.description"
              :label="$t('app.loginMethod.description')"
              :aria-label="$t('app.loginMethod.description')"
              :placeholder="$t('app.loginMethod.description')"
              class="sm:col-span-2"
            />
            <TextField
              v-model="formData.loginMethods[p]!.logoHover"
              :label="$t('app.loginMethod.logoHover')"
              :aria-label="$t('app.loginMethod.logoHover')"
              :placeholder="$t('app.loginMethod.logoHover')"
            />
            <TextField
              v-model="formData.loginMethods[p]!.logoLight"
              :label="$t('app.loginMethod.logoLight')"
              :aria-label="$t('app.loginMethod.logoLight')"
              :placeholder="$t('app.loginMethod.logoLight')"
            />
            <TextField
              v-model="formData.loginMethods[p]!.logoDark"
              :label="$t('app.loginMethod.logoDark')"
              :aria-label="$t('app.loginMethod.logoDark')"
              :placeholder="$t('app.loginMethod.logoDark')"
            />
          </Card>
        </Card>
        <Card v-if="isActiveTab(3)" class="grid grid-cols-1 gap-2 px-4 py-4" :shadow="false">
          <Toggle
            v-model="formData.walletPlugin.enable"
            :disabled="isDisabled('walletServicePlugin')"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.walletPlugin.title')"
            :label-enabled="$t('app.walletPlugin.title')"
            class="mb-2"
          />
          <Select
            v-model="formData.walletPlugin.confirmationStrategy"
            data-testid="selectConfirmationStrategy"
            :label="$t('app.walletPlugin.confirmationStrategy')"
            :aria-label="$t('app.walletPlugin.confirmationStrategy')"
            :placeholder="$t('app.walletPlugin.confirmationStrategy')"
            :options="confirmationStrategyOptions"
            matchParentsWidth
            class=""
          />
        </Card>
        <Card v-if="isActiveTab(4)" class="grid grid-cols-1 gap-2 px-4 py-4" :shadow="false">
          <Toggle
            v-model="formData.nftCheckoutPlugin.enable"
            :disabled="isDisabled('nftCheckoutPlugin')"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.nftCheckoutPlugin.title')"
            :label-enabled="$t('app.nftCheckoutPlugin.title')"
            class="mb-2"
          />
        </Card>
        <Card v-if="isActiveTab(5)" class="grid grid-cols-1 gap-2 px-4 py-4" :shadow="false">
          <Toggle
            v-model="formData.useAccountAbstractionProvider"
            data-testid="accountAbstractionProvider"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.accountAbstractionProvider.title')"
            :label-enabled="$t('app.accountAbstractionProvider.title')"
            class="my-2"
          />
          <Toggle
            v-model="formData.useAAWithExternalWallet"
            data-testid="useAAWithExternalWallet"
            :show-label="true"
            :size="'small'"
            :label-disabled="$t('app.accountAbstractionProvider.useAAWithExternalWallet')"
            :label-enabled="$t('app.accountAbstractionProvider.useAAWithExternalWallet')"
            class="my-2"
            :disabled="isDisabled('useAAWithExternalWallet')"
          />
          <Select
            v-model="formData.smartAccountType"
            data-testid="smartAccountType"
            :label="$t('app.accountAbstractionProvider.smartAccountType')"
            :aria-label="$t('app.accountAbstractionProvider.smartAccountType')"
            :placeholder="$t('app.accountAbstractionProvider.smartAccountType')"
            :options="SmartAccountOptions"
            :disabled="isDisabled('smartAccountType')"
            matchParentsWidth
          />
          <Select
            v-model="formData.smartAccountChains"
            data-testid="selectSmartAccountChains"
            :label="$t('app.chains')"
            :aria-label="$t('app.chains')"
            :placeholder="$t('app.chains')"
            :options="aaSupportedChains"
            multiple
            matchParentsWidth
            :disabled="isDisabled('smartAccountChains')"
            @update:model-value="onSmartAccountChainChange"
          />
          <Card v-for="c in formData.smartAccountChains" :key="c" :shadow="false" class="gap-2 px-4 py-4">
            <div class="font-bold leading-tight text-left sm:col-span-2">{{ c }}</div>
            <TextField
              class="mt-3"
              v-model="formData.smartAccountChainsConfig[c].bundlerUrl"
              :label="$t('app.accountAbstractionProvider.bundlerUrl')"
              :aria-label="$t('app.accountAbstractionProvider.bundlerUrl')"
              :placeholder="$t('app.accountAbstractionProvider.bundlerUrl')"
              :disabled="isDisabled('bundlerUrl')"
            />
            <TextField
              class="mt-3"
              v-model="formData.smartAccountChainsConfig[c].paymasterUrl"
              :label="$t('app.accountAbstractionProvider.paymasterUrl')"
              :aria-label="$t('app.accountAbstractionProvider.paymasterUrl')"
              :placeholder="$t('app.accountAbstractionProvider.paymasterUrl')"
              :disabled="isDisabled('paymasterUrl')"
            />
          </Card>
        </Card>
        <div class="flex justify-center mt-5">
          <Button
            v-if="formData.widget === 'modal'"
            :class="['w-full !h-auto group py-3 rounded-full flex items-center justify-center']"
            data-testid="loginButton"
            type="button"
            block
            size="md"
            pill
            :disabled="isDisabled('btnConnect')"
            @click="connect"
          >
            Connect
          </Button>
        </div>
        <div class="px-0 mt-4 mb-5 text-sm font-normal text-app-gray-900 dark:text-app-gray-200">
          Reach out to us at
          <a class="underline text-app-primary-600 dark:text-app-primary-500" href="mailto:hello@tor.us">hello@tor.us</a>
          or
          <a class="underline text-app-primary-600 dark:text-app-primary-500" href="https://t.me/torusdev">telegram group</a>
          .
        </div>
      </Card>
    </div>
    <div
      v-if="formData.widget === 'embed'"
      id="w3a-parent-test-container"
      class="flex flex-col items-center justify-center mt-10 xs:mt-0 !w-full [@media(min-width:375px)]:!max-w-[500px]"
    ></div>
  </div>
</template>



================================================
FILE: demo/vue-app-new/src/icons/index.ts
================================================
import type { IconSets } from "@toruslabs/vue-components";

export default {
  ArrowRightIcon: () => import("@toruslabs/vue-icons/arrows/ArrowRightIcon"),
  AdjustmentsIcon: () => import("@toruslabs/vue-icons/others/AdjustmentsIcon"),
  MobileIcon: () => import("@toruslabs/vue-icons/gadgets/MobileIcon"),
  DesktopIcon: () => import("@toruslabs/vue-icons/gadgets/DesktopIcon"),
  CheckCircleSolidIcon: () => import("@toruslabs/vue-icons/notifications/CheckCircleSolidIcon"),
  EyeOffSolidIcon: () => import("@toruslabs/vue-icons/security/EyeOffSolidIcon"),
  EyeSolidIcon: () => import("@toruslabs/vue-icons/security/EyeSolidIcon"),
  InformationCircleSolidIcon: () => import("@toruslabs/vue-icons/security/InformationCircleSolidIcon"),
  LockClosedIcon: () => import("@toruslabs/vue-icons/security/LockClosedIcon"),
  TrashIcon: () => import("@toruslabs/vue-icons/others/TrashIcon"),
  TrashSolidIcon: () => import("@toruslabs/vue-icons/others/TrashSolidIcon"),
  ExclamationCircleSolidIcon: () => import("@toruslabs/vue-icons/notifications/ExclamationCircleSolidIcon"),
  XIcon: () => import("@toruslabs/vue-icons/notifications/XIcon"),
  XSolidIcon: () => import("@toruslabs/vue-icons/notifications/XSolidIcon"),
  UploadIcon: () => import("@toruslabs/vue-icons/mail/UploadIcon"),
  ColorSwatchIcon: () => import("@toruslabs/vue-icons/file/ColorSwatchIcon"),
  DocumentDuplicateIcon: () => import("@toruslabs/vue-icons/file/DocumentDuplicateIcon"),
  PhoneIcon: () => import("@toruslabs/vue-icons/call/PhoneIcon"),
  ArrowCircleLeftIcon: () => import("@toruslabs/vue-icons/arrows/ArrowCircleLeftIcon"),
  ChevronDownSolidIcon: () => import("@toruslabs/vue-icons/arrows/ChevronDownSolidIcon"),
  ChevronUpSolidIcon: () => import("@toruslabs/vue-icons/arrows/ChevronUpSolidIcon"),
  CloudIcon: () => import("@toruslabs/vue-icons/software/CloudIcon"),
  DownloadIcon: () => import("@toruslabs/vue-icons/software/DownloadIcon"),
  UserCircleIcon: () => import("@toruslabs/vue-icons/users/UserCircleIcon"),
  MailIcon: () => import("@toruslabs/vue-icons/mail/MailIcon"),
  InformationCircleIcon: () => import("@toruslabs/vue-icons/security/InformationCircleIcon"),
  XCircleSolidIcon: () => import("@toruslabs/vue-icons/notifications/XCircleSolidIcon"),
  IdentificationIcon: () => import("@toruslabs/vue-icons/security/IdentificationIcon"),
  KeySolidIcon: () => import("@toruslabs/vue-icons/security/KeySolidIcon"),
} as unknown as IconSets;



================================================
FILE: demo/vue-app-new/src/plugins/iconPlugin.ts
================================================
import { createIcons } from "@toruslabs/vue-components";

import Icons from "../icons";

export default createIcons(Icons);



================================================
FILE: demo/vue-app-new/src/services/ethHandlers.ts
================================================
import { IProvider, log, type Web3Auth } from "@web3auth/modal";
import { verifyMessage as eipVerifyMessage } from "@web3auth/sign-in-with-ethereum";
import { EVM_METHOD_TYPES } from "@web3auth/ws-embed";
import { BrowserProvider, parseEther, Transaction } from "ethers";

import { getV4TypedData } from "../config";
import { formDataStore } from "../store/form";

export const sendEth = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const txRes = await signer.sendTransaction({
      from: account,
      to: account,
      value: parseEther("0.01"),
    });
    // check for big int before logging to not break the stringify
    uiConsole("txRes", txRes.toJSON());
  } catch (error) {
    log.info("error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

export const sendEthWithSmartAccount = async (web3Auth: Web3Auth | null, uiConsole: (name: string, value: unknown) => void) => {
  const { smartAccount, bundlerClient } = web3Auth?.accountAbstractionProvider || {};
  if (!smartAccount || !bundlerClient) {
    throw new Error("Smart account or bundler client not found");
  }

  try {
    const hash = await bundlerClient.sendUserOperation({
      account: smartAccount,
      calls: [
        {
          to: smartAccount.address,
          value: parseEther("0.00001"),
        },
      ],
    });

    const { success, userOpHash, reason, receipt } = await bundlerClient.waitForUserOperationReceipt({ hash });
    uiConsole("result", { userOpHash, txHash: receipt.transactionHash, txStatus: receipt.status, userOpSuccess: success, userOpReason: reason });
  } catch (error) {
    log.error("error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

export const signEthMessage = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const fromAddress = account;
    log.info("fromAddress", fromAddress);

    const message = "Some string";
    const sig = await ethProvider.send(EVM_METHOD_TYPES.ETH_SIGN, [fromAddress, message]);
    uiConsole("eth sign", sig);
  } catch (error) {
    log.error("error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

export const getAccounts = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void): Promise<string[] | undefined> => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    uiConsole("accounts", account);
    return [account];
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
    return [];
  }
};

export const getPrivateKey = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void): Promise<string | undefined> => {
  try {
    const privateKey = (await provider.request({
      method: EVM_METHOD_TYPES.ETH_PRIVATE_KEY,
      params: [],
    })) as string;
    uiConsole("privateKey", { privateKey });
    return privateKey;
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
    return undefined;
  }
};

export const getChainId = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void): Promise<string | undefined> => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const req = ethProvider.getRpcRequest({ method: "chainId" });
    const res = await provider.request(req!);
    log.info("res", res);
    const { chainId } = provider;
    uiConsole("chainId", chainId.toString());
    return chainId.toString();
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
    return undefined;
  }
};

export const getBalance = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const balance = await ethProvider.getBalance(account);
    uiConsole("balance", balance.toString());
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

export const signTransaction = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    // only supported with social logins (openlogin adapter)
    const serializedTx = await signer.signTransaction({
      from: account,
      to: account,
      value: parseEther("0.01"),
    });
    if (formDataStore.useAccountAbstractionProvider) {
      // serialized user operation can't be parsed like transaction
      uiConsole("serialized user operation", serializedTx);
    } else {
      const tx = Transaction.from(serializedTx);
      // check for big int before logging to not break the stringify
      uiConsole("txRes", tx.toJSON());
    }
  } catch (error) {
    log.info("error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

export const signPersonalMessage = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const from = account;

    const originalMessage = "Example `personal_sign` messages";

    // Sign the message
    const signedMessage = await signer.signMessage(originalMessage);

    const valid = await eipVerifyMessage({
      provider: ethProvider,
      message: originalMessage,
      signature: signedMessage,
      signer: from,
    });

    uiConsole(`Success`, { signedMessage, verify: valid });
  } catch (error) {
    log.error("Error", error);
    uiConsole("Error", error instanceof Error ? error.message : error);
  }
};

export const signTypedMessage = async (provider: IProvider, uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const from = account;
    const typedData = getV4TypedData(provider.chainId);

    const signedMessage = await signer.signTypedData(typedData.domain, typedData.types, typedData.message);

    const valid = await eipVerifyMessage({
      provider: ethProvider,
      typedData,
      signature: signedMessage,
      signer: from,
    });

    uiConsole(`Success`, { signedMessage, verify: valid });
  } catch (error) {
    log.error("Error", error);
    uiConsole("Error", error instanceof Error ? error.message : error);
  }
};



================================================
FILE: demo/vue-app-new/src/services/solHandlers.ts
================================================
/* eslint-disable @typescript-eslint/no-explicit-any */
import { Connection, LAMPORTS_PER_SOL, PublicKey, SystemProgram, Transaction } from "@solana/web3.js";
import { CustomChainConfig, IProvider, log, SolanaWallet, TransactionOrVersionedTransaction } from "@web3auth/modal";
import { SOLANA_METHOD_TYPES } from "@web3auth/ws-embed";

export const getConnection = async (provider: IProvider): Promise<Connection> => {
  const solanaWallet = new SolanaWallet(provider);

  const connectionConfig = await solanaWallet.request<never, CustomChainConfig>({ method: "solana_provider_config" });
  const conn = new Connection(connectionConfig.rpcTarget);
  return conn;
};

function getNewTx(publicKeys: any, blockhash: any) {
  const inst = SystemProgram.transfer({
    fromPubkey: new PublicKey(publicKeys[0]),
    toPubkey: new PublicKey(publicKeys[0]),
    lamports: 0.1 * LAMPORTS_PER_SOL,
  });
  return new Transaction({ recentBlockhash: blockhash, feePayer: new PublicKey(publicKeys![0]) }).add(inst);
}

export const getAccounts = async (provider: IProvider, uiConsole: any): Promise<string[] | undefined> => {
  try {
    const solWeb3 = new SolanaWallet(provider);
    const acc = await solWeb3.requestAccounts();
    uiConsole("accounts", acc);
    return acc;
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error);
    return [];
  }
};

export const getPrivateKey = async (provider: IProvider, uiConsole: any): Promise<string | undefined> => {
  try {
    const privateKey = (await provider.request({
      method: SOLANA_METHOD_TYPES.SOLANA_PRIVATE_KEY,
      params: [],
    })) as string;
    uiConsole("privateKey", { privateKey });
    return privateKey;
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
    return undefined;
  }
};

export const getBalance = async (provider: IProvider, uiConsole: any): Promise<void> => {
  try {
    const conn = await getConnection(provider);
    const solanaWallet = new SolanaWallet(provider);
    const accounts = await solanaWallet.requestAccounts();
    const balance = await conn.getBalance(new PublicKey(accounts[0]));
    uiConsole("balance", { balance });
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error);
  }
};

export const signAndSendTransaction = async (provider: IProvider, uiConsole: any) => {
  try {
    const conn = await getConnection(provider);
    const solWeb3 = new SolanaWallet(provider);
    const pubKey = await solWeb3.requestAccounts();

    const block = await conn.getLatestBlockhash("finalized");
    const transactionInstruction = SystemProgram.transfer({
      fromPubkey: new PublicKey(pubKey[0]),
      toPubkey: new PublicKey(pubKey[0]),
      lamports: 0.01 * LAMPORTS_PER_SOL,
    });

    const transaction = new Transaction({
      blockhash: block.blockhash,
      lastValidBlockHeight: block.lastValidBlockHeight,
      feePayer: new PublicKey(pubKey[0]),
    }).add(transactionInstruction);

    const signature = await solWeb3.signAndSendTransaction(transaction as unknown as TransactionOrVersionedTransaction);
    uiConsole("signature", { signature });
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error);
  }
};

export const signTransaction = async (provider: IProvider, uiConsole: any) => {
  try {
    const conn = await getConnection(provider);
    const solWeb3 = new SolanaWallet(provider);
    const pubKey = await solWeb3.requestAccounts();
    log.info("pubKey", pubKey);

    const transactionInstruction = SystemProgram.transfer({
      fromPubkey: new PublicKey(pubKey[0]),
      toPubkey: new PublicKey(pubKey[0]),
      lamports: 0 * LAMPORTS_PER_SOL,
    });

    const block = await conn.getLatestBlockhash("finalized");
    const transaction = new Transaction({
      blockhash: block.blockhash,
      lastValidBlockHeight: block.lastValidBlockHeight,
      feePayer: new PublicKey(pubKey[0]),
    }).add(transactionInstruction);

    const signature = await solWeb3.signTransaction(transaction);
    log.info("signedTx", signature);
    uiConsole("signature", { signature });
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error);
  }
};

export const signMessage = async (provider: IProvider, uiConsole: any) => {
  try {
    const solWeb3 = new SolanaWallet(provider);
    const pubKey = await solWeb3.requestAccounts();
    log.info("pubKey", pubKey);

    const msg = "Test Signing Message";
    const signature = await solWeb3.signMessage(msg, pubKey[0]);
    uiConsole("solana signed message", { signature });
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error);
  }
};

export const signAllTransactions = async (provider: IProvider, uiConsole: any) => {
  try {
    const conn = await getConnection(provider);
    const solWeb3 = new SolanaWallet(provider);
    const publicKeys = await solWeb3.requestAccounts();
    const { blockhash } = await conn.getLatestBlockhash("finalized");
    log.info("blockhash", blockhash);

    const signedTransactions = await solWeb3.signAllTransactions([
      getNewTx(publicKeys, blockhash) as unknown as TransactionOrVersionedTransaction,
      getNewTx(publicKeys, blockhash) as unknown as TransactionOrVersionedTransaction,
      getNewTx(publicKeys, blockhash) as unknown as TransactionOrVersionedTransaction,
    ]);
    log.info("signedTransactions", signedTransactions);
    uiConsole("signed transactions", { signedTransactions });
  } catch (error) {
    log.error("Error", error);
    uiConsole("error", error);
  }
};



================================================
FILE: demo/vue-app-new/src/services/walletServiceHandlers.ts
================================================
import { Connection, PublicKey } from "@solana/web3.js";
import { bs58 } from "@toruslabs/bs58";
import { sign } from "@toruslabs/tweetnacl-js";
import { log, type WalletServicesPluginType } from "@web3auth/modal";
import { verifyMessage as eipVerifyMessage } from "@web3auth/sign-in-with-ethereum";
import { SOLANA_METHOD_TYPES as SOL_METHOD_TYPES } from "@web3auth/ws-embed";
import { BrowserProvider, parseEther } from "ethers";

import { getV4TypedData } from "../config";
import { generateSolTransferInstruction, generateVersionedTransaction } from "../utils/solana";

// EVM
export const walletSignPersonalMessage = async (
  provider: WalletServicesPluginType["provider"],
  uiConsole: (name: string, value: unknown) => void
) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const from = account;

    const originalMessage = "Example `personal_sign` messages";

    // Sign the message
    const signedMessage = await signer.signMessage(originalMessage);

    const valid = await eipVerifyMessage({
      provider: ethProvider,
      message: originalMessage,
      signature: signedMessage,
      signer: from,
    });

    uiConsole(`Success`, { signedMessage, verify: valid });
  } catch (error) {
    log.error("Error", error);
    uiConsole("Error", error instanceof Error ? error.message : error);
  }
};

export const walletSignTypedMessage = async (provider: WalletServicesPluginType["provider"], uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const from = account;
    const typedData = getV4TypedData(provider.chainId);

    const signedMessage = await signer.signTypedData(typedData.domain, typedData.types, typedData.message);

    const valid = await eipVerifyMessage({
      provider: ethProvider,
      typedData,
      signature: signedMessage,
      signer: from,
    });

    uiConsole(`Success`, { signedMessage, verify: valid });
  } catch (error) {
    log.error("Error", error);
    uiConsole("Error", error instanceof Error ? error.message : error);
  }
};

export const walletSendEth = async (provider: WalletServicesPluginType["provider"], uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const signer = await ethProvider.getSigner();
    const account = await signer.getAddress();
    const txRes = await signer.sendTransaction({
      from: account,
      to: account,
      value: parseEther("0.01"),
    });
    // check for big int before logging to not break the stringify
    uiConsole("txRes", txRes.toJSON());
  } catch (error) {
    log.info("error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

export const walletSignTransaction = async (provider: WalletServicesPluginType["provider"], uiConsole: (name: string, value: unknown) => void) => {
  try {
    const ethProvider = new BrowserProvider(provider);
    const accounts = await provider.request({ method: "eth_accounts" });
    const smartAccountAddress = accounts[0];
    const signer = await ethProvider.getSigner(smartAccountAddress);
    const account = await signer.getAddress();
    // only supported with social logins (openlogin adapter)
    const serializedTx = await signer.signTransaction({
      from: account,
      to: account,
      value: parseEther("0.01"),
    });

    uiConsole("serialized user operation", serializedTx);
  } catch (error) {
    log.info("error", error);
    uiConsole("error", error instanceof Error ? error.message : error);
  }
};

// Solana
export const walletSignSolanaMessage = async (provider: WalletServicesPluginType["provider"], uiConsole: (name: string, value: unknown) => void) => {
  try {
    const message = "Test Signing Message";
    const accounts = await provider.request({ method: SOL_METHOD_TYPES.GET_ACCOUNTS });
    const account = accounts[0];

    const signature = (await provider.request({
      method: SOL_METHOD_TYPES.SIGN_MESSAGE,
      params: { data: message, from: account },
    })) as string;
    sign.detached.verify(Buffer.from(message, "utf8"), bs58.decode(signature), new PublicKey(account).toBytes());
    uiConsole("Success", { signature });
  } catch (e) {
    uiConsole("Error signing message", (e as Error).message);
  }
};

export const walletSignSolanaVersionedTransaction = async (
  provider: WalletServicesPluginType["provider"],
  connection: Connection,
  uiConsole: (name: string, value?: unknown) => void
) => {
  uiConsole("Signing Versioned Transaction");
  try {
    const accounts = await provider.request({ method: SOL_METHOD_TYPES.GET_ACCOUNTS });
    const account = accounts[0];

    const instruction = await generateSolTransferInstruction(account, account, 0);
    const transaction = await generateVersionedTransaction(connection, account, [instruction]);
    const signature = (await provider.request({
      method: SOL_METHOD_TYPES.SIGN_TRANSACTION,
      params: { message: Buffer.from(transaction.serialize()).toString("base64") },
    })) as string;
    uiConsole("Success", { signature });
  } catch (e) {
    uiConsole("Error", (e as Error).message);
  }
};



================================================
FILE: demo/vue-app-new/src/store/form.ts
================================================
import { WEB3AUTH_NETWORK } from "@web3auth/auth";
import { CHAIN_NAMESPACES, WIDGET_TYPE } from "@web3auth/modal";
import { reactive } from "vue";

import { chainConfigs, defaultLoginMethod, FormData, initWhiteLabel } from "../config";

export const formDataStore = reactive<FormData>({
  // authMode: "",
  connectors: [],
  network: process.env.NODE_ENV === "production" ? WEB3AUTH_NETWORK.SAPPHIRE_MAINNET : WEB3AUTH_NETWORK.SAPPHIRE_DEVNET,
  chainNamespaces: [CHAIN_NAMESPACES.EIP155, CHAIN_NAMESPACES.SOLANA],
  chains: [chainConfigs[CHAIN_NAMESPACES.EIP155][0], chainConfigs[CHAIN_NAMESPACES.SOLANA][0]],
  defaultChainId: undefined,
  whiteLabel: {
    enable: false,
    config: initWhiteLabel,
  },
  loginProviders: [],
  showWalletDiscovery: true,
  multiInjectedProviderDiscovery: true,
  loginMethods: defaultLoginMethod,
  walletPlugin: {
    enable: false,
    confirmationStrategy: "modal",
  },
  nftCheckoutPlugin: {
    enable: false,
  },
  useAccountAbstractionProvider: false,
  useAAWithExternalWallet: true,
  smartAccountType: "metamask", // default smart account type to safe
  smartAccountChains: [],
  smartAccountChainsConfig: {},
  widget: WIDGET_TYPE.MODAL,
  targetId: "w3a-parent-test-container",
});



================================================
FILE: demo/vue-app-new/src/translations/en.json
================================================
{
  "app": {
    "title": "Web3Auth Web Vue Demo",
    "description": "This is a demo of Web3Auth in a Vue.js app.",
    "btnLogout": "Logout",
    "documentation": "Documentation",
    "network": "Network",
    "chains": "Chains",
    "defaultChainId": "Default Chain ID",
    "loginProviders": "Login provider",
    "connectors": "Connectors",
    "showWalletDiscovery": "Show Wallet Discovery",
    "multiInjectedProviderDiscovery": "Multi Injected Provider Discovery",
    "greeting": "Let's configure Web3Auth!",
    "enableWalletServicePlugin": "Enable Wallet Service Plugin",
    "walletPlugin": {
      "title": "Wallet Service Plugin",
      "logoLight": "Logo Light",
      "logoDark": "Logo Dark",
      "confirmationStrategy": "Confirmation Strategy"
    },
    "nftCheckoutPlugin": {
      "title": "NFT Checkout Plugin"
    },
    "accountAbstractionProvider": {
      "title": "Account Abstraction Provider",
      "smartAccountType": "Smart Account Type",
      "bundlerUrl": "Bundler Url",
      "paymasterUrl": "Paymaster Url",
      "useAAWithExternalWallet": "Use Account Abstraction Provider with external wallet"
    },
    "whiteLabel": {
      "title": "Enable White Label",
      "appName": "App Name",
      "appUrl": "App URL",
      "defaultLanguage": "Default Language",
      "logoLight": "Light Logo",
      "logoDark": "Dark Logo",
      "useLogoLoader": "Use Logo Loader",
      "primaryColor": "Primary Color",
      "onPrimaryColor": "On Primary Color"
    },
    "loginMethod": {
      "name": "Name",
      "description": "Description",
      "logoHover": "Logo Hover",
      "logoLight": "Logo Light",
      "logoDark": "Logo Dark",
      "mainOption": "Main Option",
      "showOnModal": "Show on Modal"
    },
    "adapter": {
      "sessionTime": "Session Time"
    },
    "chainNamespaces": "Chain namespaces",
    "w3aStatus": "Web3Auth status ::::: {status}",
    "isConnected": "Is connected ::::: {isConnected}",
    "isInitialized": "Is initialized ::::: {isInitialized}",
    "buttons": {
      "btnClearConsole": "Clear Console",
      "btnGetUserInfo": "Get User Info",
      "btnGetAccounts": "Get Accounts",
      "btnGetPrivateKey": "Get Private Key",
      "btnGetBalance": "Get Balance",
      "btnSendEth": "Send ETH",
      "btnSendAATx": "Send ETH with Smart Account",
      "btnSignEthMessage": "Sign ETH Message",
      "btnGetConnectedChainId": "Get Connected Chain ID",
      "btnAddChain": "Add Chain",
      "btnSwitchChain": "Switch Chain",
      "btnSwitchChainNamespace": "Switch Chain Namespace",
      "btnSignAndSendTransaction": "Sign and Send Transaction",
      "btnSignTransaction": "Sign Transaction",
      "btnSignMessage": "Sign Message",
      "btnSignAllTransactions": "Sign All Transactions",
      "btnShowWalletUI": "Show Wallet UI",
      "btnShowCheckout": "Show Checkout",
      "btnShowWalletConnectScanner": "Show WalletConnect Scanner",
      "btnSignTypedData_v4": "Sign Typed Data v4",
      "btnSignPersonalMsg": "Sign Personal Message",
      "btnShowFreeMintNFTCheckout": "Show Free Mint NFT",
      "btnShowPaidMintNFTCheckout": "Show Paid Mint NFT"
    },
    "widget": {
      "title": "Widget",
      "embed": "Embed",
      "modal": "Modal"
    }
  }
}



================================================
FILE: demo/vue-app-new/src/translations/vi.json
================================================
{}


================================================
FILE: demo/vue-app-new/src/utils/chainconfig.ts
================================================
import { CHAIN_NAMESPACES, ChainNamespaceType, CustomChainConfig, WalletInitializationError } from "@web3auth/modal";

const INFURA_PROXY_URL = "https://api.web3auth.io/infura-service/v1";

const getDefaultNetworkId = (chainNamespace: ChainNamespaceType): number => {
  if (chainNamespace === CHAIN_NAMESPACES.EIP155) {
    return 1;
  }
  if (chainNamespace === CHAIN_NAMESPACES.SOLANA) {
    return 1;
  }
  if (chainNamespace === CHAIN_NAMESPACES.XRPL) {
    return 1;
  }
  throw WalletInitializationError.invalidParams(`Chain namespace ${chainNamespace} is not supported`);
};
// TODO: remove this function and get this from dashboard instead
export const getEvmChainConfig = (chainId: number, web3AuthClientId: string = ""): CustomChainConfig | null => {
  const chainNamespace = CHAIN_NAMESPACES.EIP155;
  const infuraRpcTarget = `${INFURA_PROXY_URL}/${chainId}/${web3AuthClientId}`;
  if (chainId === 1) {
    return {
      logo: "https://images.toruswallet.io/eth.svg",
      chainNamespace,
      chainId: "0x1",
      rpcTarget: infuraRpcTarget,
      displayName: "Ethereum Mainnet",
      blockExplorerUrl: "https://etherscan.io/",
      ticker: "ETH",
      tickerName: "Ethereum",
      decimals: 18,
    };
  }
  if (chainId === 10) {
    return {
      chainNamespace: CHAIN_NAMESPACES.EIP155,
      decimals: 18,
      blockExplorerUrl: "https://optimistic.etherscan.io",
      chainId: "0xa",
      displayName: "Optimism",
      logo: "optimism.svg",
      rpcTarget: infuraRpcTarget,
      ticker: "ETH",
      tickerName: "Ethereum",
    };
  }
  if (chainId === 8453) {
    return {
      chainNamespace: CHAIN_NAMESPACES.EIP155,
      decimals: 18,
      blockExplorerUrl: "https://basescan.org",
      chainId: "0x2105",
      displayName: "Base",
      logo: "base.svg",
      rpcTarget: infuraRpcTarget,
      ticker: "ETH",
      tickerName: "Ethereum",
    };
  }
  if (chainId === 42161) {
    return {
      chainNamespace: CHAIN_NAMESPACES.EIP155,
      decimals: 18,
      blockExplorerUrl: "https://arbiscan.io",
      chainId: "0xa4b1",
      displayName: "Arbitrum One",
      logo: "arbitrum.svg",
      rpcTarget: infuraRpcTarget,
      ticker: "ETH",
      tickerName: "Ethereum",
    };
  }
  if (chainId === 59144) {
    return {
      chainNamespace: CHAIN_NAMESPACES.EIP155,
      decimals: 18,
      blockExplorerUrl: "https://lineascan.build",
      chainId: "0xe708",
      logo: "https://images.toruswallet.io/eth.svg",
      rpcTarget: infuraRpcTarget,
      ticker: "ETH",
      tickerName: "Ethereum",
      displayName: "Linea",
    };
  }
  if (chainId === 11155111) {
    return {
      logo: "https://images.toruswallet.io/eth.svg",
      chainNamespace,
      chainId: "0xaa36a7",
      rpcTarget: infuraRpcTarget,
      displayName: "Sepolia Testnet",
      blockExplorerUrl: "https://sepolia.etherscan.io/",
      ticker: "ETH",
      tickerName: "Ethereum",
      decimals: 18,
    };
  }
  if (chainId === 137) {
    return {
      logo: "https://images.toruswallet.io/polygon.svg",
      chainNamespace,
      chainId: "0x89",
      rpcTarget: infuraRpcTarget,
      displayName: "Polygon Mainnet",
      blockExplorerUrl: "https://polygonscan.com",
      ticker: "POL",
      tickerName: "Polygon Ecosystem Token",
    };
  }
  if (chainId === 80002) {
    return {
      logo: "https://images.toruswallet.io/polygon.svg",
      chainNamespace,
      chainId: "0x13882",
      rpcTarget: infuraRpcTarget,
      displayName: "Polygon Amoy Testnet",
      blockExplorerUrl: "https://www.oklink.com/amoy",
      ticker: "POL",
      tickerName: "Polygon Ecosystem Token",
      decimals: 18,
    };
  }
  if (chainId === 56) {
    return {
      logo: "https://images.toruswallet.io/bnb.png",
      chainNamespace,
      chainId: "0x38",
      rpcTarget: infuraRpcTarget,
      displayName: "Binance SmartChain Mainnet",
      blockExplorerUrl: "https://bscscan.com",
      ticker: "BNB",
      tickerName: "Binance SmartChain",
      decimals: 18,
    };
  }
  if (chainId === 97) {
    return {
      logo: "https://images.toruswallet.io/bnb.png",
      chainNamespace,
      chainId: "0x61",
      rpcTarget: infuraRpcTarget,
      displayName: "Binance SmartChain Testnet",
      blockExplorerUrl: "https://testnet.bscscan.com",
      ticker: "BNB",
      tickerName: "Binance SmartChain",
      decimals: 18,
    };
  }
  if (chainId === 25) {
    return {
      logo: "https://images.toruswallet.io/cro.svg",
      chainNamespace,
      chainId: "0x19",
      rpcTarget: "https://rpc.cronos.org",
      displayName: "Cronos Mainnet",
      blockExplorerUrl: "https://cronoscan.com/",
      ticker: "CRO",
      tickerName: "Cronos",
    };
  }
  if (chainId === 338) {
    return {
      logo: "https://images.toruswallet.io/cro.svg",
      chainNamespace,
      chainId: "0x152",
      rpcTarget: "https://rpc-t3.cronos.org/",
      displayName: "Cronos Testnet",
      blockExplorerUrl: "https://cronoscan.com/",
      ticker: "CRO",
      tickerName: "Cronos",
      decimals: 18,
    };
  }
  if (chainId === 8217) {
    return {
      logo: "https://images.toruswallet.io/klay.svg",
      chainNamespace,
      chainId: "0x2019",
      rpcTarget: "https://public-node-api.klaytnapi.com/v1/cypress",
      displayName: "Klaytn Mainnet",
      blockExplorerUrl: "https://scope.klaytn.com",
      ticker: "KLAY",
      tickerName: "Klaytn",
      decimals: 18,
    };
  }
  if (chainId === 1946) {
    return {
      chainNamespace: CHAIN_NAMESPACES.EIP155,
      chainId: "0x79a",
      rpcTarget: "https://rpc.minato.soneium.org",
      displayName: "Soneium Minato Testnet",
      blockExplorerUrl: "https://explorer-testnet.soneium.org",
      ticker: "ETH",
      tickerName: "ETH",
      logo: "https://iili.io/2i5xce2.png",
    };
  }
  if (chainId === 1868) {
    return {
      chainNamespace: CHAIN_NAMESPACES.EIP155,
      chainId: "0x74c",
      rpcTarget: "https://rpc.soneium.org",
      displayName: "Soneium Mainnet",
      blockExplorerUrl: "https://soneium.blockscout.com",
      ticker: "ETH",
      tickerName: "ETH",
      logo: "https://iili.io/2i5xce2.png",
    };
  }

  return null;
};

export const getSolanaChainConfig = (chainId: number): CustomChainConfig | null => {
  const chainNamespace = CHAIN_NAMESPACES.SOLANA;
  // support both cross chain id and base solana chain id from 1
  if (chainId === 101 || chainId === 1) {
    return {
      logo: "https://images.toruswallet.io/sol.svg",
      chainNamespace,
      chainId: "0x65",
      rpcTarget: "https://api.mainnet-beta.solana.com",
      displayName: "Solana Mainnet",
      blockExplorerUrl: "https://explorer.solana.com",
      ticker: "SOL",
      tickerName: "Solana",
      decimals: 9,
    };
  } else if (chainId === 102 || chainId === 2) {
    return {
      logo: "https://images.toruswallet.io/sol.svg",
      chainNamespace,
      chainId: "0x66",
      rpcTarget: "https://api.testnet.solana.com",
      displayName: "Solana Testnet",
      blockExplorerUrl: "https://explorer.solana.com?cluster=testnet",
      ticker: "SOL",
      tickerName: "Solana",
      decimals: 9,
    };
  } else if (chainId === 103 || chainId === 3) {
    return {
      logo: "https://images.toruswallet.io/sol.svg",
      chainNamespace,
      chainId: "0x67",
      rpcTarget: "https://api.devnet.solana.com",
      displayName: "Solana Devnet",
      blockExplorerUrl: "https://explorer.solana.com?cluster=devnet",
      ticker: "SOL",
      tickerName: "Solana",
      decimals: 9,
    };
  }

  return null;
};

export const getXrplChainConfig = (chainId: number): CustomChainConfig | null => {
  const chainNamespace = CHAIN_NAMESPACES.XRPL;
  if (chainId === 1) {
    return {
      chainNamespace,
      decimals: 15,
      chainId: "0x1",
      logo: "https://images.toruswallet.io/XRP.svg",
      rpcTarget: "https://ripple-node.tor.us",
      wsTarget: "wss://s2.ripple.com",
      ticker: "XRP",
      tickerName: "XRPL",
      displayName: "xrpl mainnet",
      blockExplorerUrl: "https://livenet.xrpl.org",
    };
  }
  if (chainId === 2) {
    return {
      chainNamespace,
      decimals: 15,
      chainId: "0x2",
      logo: "https://images.toruswallet.io/XRP.svg",
      rpcTarget: "https://testnet-ripple-node.tor.us",
      wsTarget: "wss://s.altnet.rippletest.net",
      ticker: "XRP",
      tickerName: "XRPL",
      displayName: "xrpl testnet",
      blockExplorerUrl: "https://testnet.xrpl.org",
      isTestnet: true,
    };
  }
  if (chainId === 3) {
    return {
      chainNamespace,
      decimals: 15,
      chainId: "0x3",
      logo: "https://images.toruswallet.io/XRP.svg",
      rpcTarget: "https://devnet-ripple-node.tor.us",
      wsTarget: "wss://s.devnet.rippletest.net/",
      ticker: "XRP",
      tickerName: "XRPL",
      displayName: "xrpl devnet",
      blockExplorerUrl: "https://devnet.xrpl.org",
      isTestnet: true,
    };
  }

  return null;
};

export const getChainConfig = (
  chainNamespace: ChainNamespaceType,
  chainId?: number | string,
  web3AuthClientId?: string
): CustomChainConfig | null => {
  if (chainNamespace === CHAIN_NAMESPACES.OTHER) return null;

  const finalChainId = chainId ? (typeof chainId === "number" ? chainId : parseInt(chainId, 16)) : getDefaultNetworkId(chainNamespace);
  if (chainNamespace === CHAIN_NAMESPACES.EIP155) {
    return getEvmChainConfig(finalChainId, web3AuthClientId);
  } else if (chainNamespace === CHAIN_NAMESPACES.SOLANA) {
    return getSolanaChainConfig(finalChainId);
  }
  if (chainNamespace === CHAIN_NAMESPACES.XRPL) {
    return getXrplChainConfig(finalChainId);
  }
  return null;
};



================================================
FILE: demo/vue-app-new/src/utils/constants.ts
================================================
import { CHAIN_NAMESPACES, ProviderConfig } from "@toruslabs/base-controllers";
import { SOLANA_CHAIN_IDS as CHAIN_IDS } from "@web3auth/ws-embed";

export const EXPLORER = "https://explorer.solana.com";

const MAINNET_RPC = import.meta.env.VITE_APP_SOLANA_MAINNET_RPC;
const TESTNET_RPC = import.meta.env.VITE_APP_SOLANA_TESTNET_RPC;
const DEVNET_RPC = import.meta.env.VITE_APP_SOLANA_DEVNET_RPC;

function rpcUrlToWsUrl(rpcUrl: string) {
  if (!rpcUrl) throw new Error("Please configure https endpoint for solana rpc");
  return rpcUrl.replace("https://", "wss://");
}

export const SOLANA_SUPPORTED_NETWORKS = {
  [CHAIN_IDS.SOLANA_MAINNET]: {
    chainNamespace: CHAIN_NAMESPACES.SOLANA,
    decimals: 9,
    blockExplorerUrl: EXPLORER,
    chainId: CHAIN_IDS.SOLANA_MAINNET,
    displayName: "Solana Mainnet",
    logo: "solana.svg",
    rpcTarget: MAINNET_RPC,
    wsTarget: rpcUrlToWsUrl(MAINNET_RPC as string),
    ticker: "SOL",
    tickerName: "Solana Token",
  } as ProviderConfig,
  [CHAIN_IDS.SOLANA_TESTNET]: {
    chainNamespace: CHAIN_NAMESPACES.SOLANA,
    decimals: 9,
    blockExplorerUrl: EXPLORER,
    chainId: CHAIN_IDS.SOLANA_TESTNET,
    displayName: "Solana Testnet",
    logo: "solana.svg",
    rpcTarget: TESTNET_RPC,
    wsTarget: rpcUrlToWsUrl(TESTNET_RPC as string),
    ticker: "SOL",
    tickerName: "Solana Token",
    isTestnet: true,
  } as ProviderConfig,
  [CHAIN_IDS.SOLANA_DEVNET]: {
    chainNamespace: CHAIN_NAMESPACES.SOLANA,
    decimals: 9,
    blockExplorerUrl: EXPLORER,
    chainId: CHAIN_IDS.SOLANA_DEVNET,
    displayName: "Solana Devnet",
    logo: "solana.svg",
    rpcTarget: DEVNET_RPC,
    wsTarget: rpcUrlToWsUrl(DEVNET_RPC as string),
    ticker: "SOL",
    tickerName: "Solana Token",
    isTestnet: true,
  } as ProviderConfig,
} as const;



================================================
FILE: demo/vue-app-new/src/utils/solana.ts
================================================
import {
  Connection,
  LAMPORTS_PER_SOL,
  PublicKey,
  SystemProgram,
  Transaction,
  TransactionInstruction,
  TransactionMessage,
  VersionedTransaction,
} from "@solana/web3.js";

export async function generateSolTransferInstruction(sender: string, receiver: string, amount: number) {
  return SystemProgram.transfer({
    fromPubkey: new PublicKey(sender),
    toPubkey: new PublicKey(receiver),
    lamports: amount * LAMPORTS_PER_SOL,
  });
}

export async function generateLegacyTransaction(connection: Connection | null, sender: string, instructions: TransactionInstruction[]) {
  if (!connection) throw new Error("Connection not found");
  const latestBlockhash = await connection.getLatestBlockhash("finalized");
  const transaction = new Transaction({
    blockhash: latestBlockhash.blockhash,
    lastValidBlockHeight: latestBlockhash.lastValidBlockHeight,
    feePayer: new PublicKey(sender),
  }).add(...instructions);
  return transaction;
}

export async function generateVersionedTransaction(connection: Connection | null, sender: string, instructions: TransactionInstruction[]) {
  if (!connection) throw new Error("Connection not found");
  const latestBlockhash = await connection.getLatestBlockhash("finalized");
  // create v0 compatible message
  const messageV0 = new TransactionMessage({
    payerKey: new PublicKey(sender),
    instructions,
    recentBlockhash: latestBlockhash.blockhash,
  }).compileToV0Message();
  const transactionV0 = new VersionedTransaction(messageV0);
  return transactionV0;
}



================================================
FILE: demo/wagmi-react-app/README.md
================================================
# Web3Auth x React Demo App

## Quickstart

To use this demo app, you'll first have to build the Web3Auth packages.

### Build the `Web3Auth` packages

```bash
git clone https://github.com/Web3Auth/web3auth-web.git
cd web3auth-web
npm install
npm run build
```

### Start the demo app

> Inside `web3auth-web` directory.

```bash
cd demo/wagmi-react-app
npm install
npm start
# localhost:3000
```



================================================
FILE: demo/wagmi-react-app/eslint.config.mjs
================================================
import toruslabsReact from "@toruslabs/eslint-config-react";

export default [
  ...toruslabsReact,
  {
    ignores: ["*.config.mjs", "*.config.mts"],
  },
];



================================================
FILE: demo/wagmi-react-app/index.html
================================================
<!--
  Migrate from react-app to vite by following this guide
  https://www.freecodecamp.org/news/how-to-migrate-from-create-react-app-to-vite/
-->
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="Web site created using create-react-app" />
    <link rel="apple-touch-icon" href="/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="/manifest.json" />
    <script type="module">
      window.global = globalThis;
      import { Buffer } from "buffer";
      import process from "process";
      // window.global ||= window;
      window.Buffer = Buffer;
      window.process = process;
    </script>
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
    <script type="module" src="/src/index.tsx"></script>
  </body>
</html>



================================================
FILE: demo/wagmi-react-app/package.json
================================================
{
  "name": "wagmi-react-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@tanstack/react-query": "^5.74.7",
    "@web3auth/modal": "file:../../packages/modal",
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "viem": "^2.28.1",
    "wagmi": "^2.15.0"
  },
  "scripts": {
    "start": "vite",
    "build": "tsc && vite build",
    "lint": "eslint --fix 'src/**/*.ts' 'src/**/*.tsx'",
    "preview": "vite preview"
  },
  "browserslist": {
    "production": [
      "supports bigint",
      "not dead"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "@toruslabs/eslint-config-react": "^4.1.4",
    "@types/node": "^22.15.3",
    "@types/react": "^19.1.2",
    "@types/react-dom": "^19.1.2",
    "@vitejs/plugin-react": "^4.4.1",
    "buffer": "^6.0.3",
    "process": "^0.11.10",
    "typescript": "^5.8.3",
    "vite": "^6.3.3",
    "vite-tsconfig-paths": "^5.1.4",
    "webpack-bundle-analyzer": "^4.10.2"
  }
}



================================================
FILE: demo/wagmi-react-app/tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ESNext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "types": ["vite/client"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}



================================================
FILE: demo/wagmi-react-app/vite-env.d.ts
================================================
/// <reference types="vite/client" />


================================================
FILE: demo/wagmi-react-app/vite.config.mts
================================================
import react from "@vitejs/plugin-react";
import { resolve } from "node:path";
import { defineConfig } from "vite";

export default defineConfig({
  plugins: [react()],
  server: {
    // this ensures that the browser opens upon server start
    open: true,
    // this sets a default port to 3000
    port: 3000,
  },
  resolve: {
    alias: {
      wagmi: resolve("./node_modules/wagmi"),
    },
  },
});



================================================
FILE: demo/wagmi-react-app/public/manifest.json
================================================
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}



================================================
FILE: demo/wagmi-react-app/public/robots.txt
================================================
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:



================================================
FILE: demo/wagmi-react-app/src/App.css
================================================
.App {
  text-align: center;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
    animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}



================================================
FILE: demo/wagmi-react-app/src/App.tsx
================================================
import "./App.css";

import Main from "./components/Main";
import styles from "./styles/Home.module.css";

function App() {
  return (
    <div className={styles.container}>
      <Main />
    </div>
  );
}

export default App;



================================================
FILE: demo/wagmi-react-app/src/index.css
================================================
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}



================================================
FILE: demo/wagmi-react-app/src/index.tsx
================================================
import "./index.css";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { type Web3AuthContextConfig, Web3AuthProvider } from "@web3auth/modal/react";
import { WagmiProvider } from "@web3auth/modal/react/wagmi";
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

import App from "./App";

const queryClient = new QueryClient();
const clientId = "BNJiiG6wVmiMMzApYoCbfD2xU0xxh3cp-t94tgKdwWEuf8Z5DOufWs4SnYiTqdqdA6-pTReQkaiI6z-y9rHxTIM";

const web3authConfig: Web3AuthContextConfig = {
  web3AuthOptions: {
    enableLogging: true,
    web3AuthNetwork: "sapphire_devnet",
    clientId: clientId,
  },
};

const container = document.getElementById("root") as HTMLElement;
const root = createRoot(container);

root.render(
  <StrictMode>
    <Web3AuthProvider config={web3authConfig}>
      <QueryClientProvider client={queryClient}>
        <WagmiProvider>
          <App />
        </WagmiProvider>
      </QueryClientProvider>
    </Web3AuthProvider>
  </StrictMode>
);



================================================
FILE: demo/wagmi-react-app/src/react-app-env.d.ts
================================================
/// <reference types="react-scripts" />



================================================
FILE: demo/wagmi-react-app/src/components/Main.tsx
================================================
import {
  useCheckout,
  useEnableMFA,
  useIdentityToken,
  useManageMFA,
  useWalletConnectScanner,
  useWalletUI,
  useWeb3Auth,
  useWeb3AuthConnect,
  useWeb3AuthDisconnect,
  useWeb3AuthUser,
} from "@web3auth/modal/react";
import { useAccount, useBalance, useChainId, useSignMessage, useSignTypedData, useSwitchChain } from "wagmi";

import styles from "../styles/Home.module.css";

const Main = () => {
  const { provider, isConnected } = useWeb3Auth();
  const { loading: connecting, connect, error: connectingError, connectorName, connectTo } = useWeb3AuthConnect();
  const { disconnect } = useWeb3AuthDisconnect();
  const { signMessageAsync, data: signedMessageData } = useSignMessage();
  const { address, isConnected: isWagmiConnected } = useAccount();
  const { userInfo, isMFAEnabled } = useWeb3AuthUser();
  const { data: balance } = useBalance({ address });
  const { signTypedData, data: signedTypedDataData } = useSignTypedData();
  const { enableMFA, loading: isEnableMFALoading, error: enableMFAError } = useEnableMFA();
  const { manageMFA, loading: isManageMFALoading, error: manageMFAError } = useManageMFA();
  const { showCheckout, loading: isCheckoutLoading, error: checkoutError } = useCheckout();
  const { showWalletConnectScanner, loading: isWalletConnectScannerLoading, error: walletConnectScannerError } = useWalletConnectScanner();
  const { showWalletUI, loading: isWalletUILoading, error: walletUIError } = useWalletUI();
  const { token, loading: isUserTokenLoading, error: userTokenError, getIdentityToken } = useIdentityToken();
  const { switchChainAsync, chains } = useSwitchChain();
  const chainId = useChainId();

  const loggedInView = (
    <>
      <div className={styles.container}>
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Account Address: {address}</p>
          <p>Account Balance: {balance?.value}</p>
          <p>MFA Enabled: {isMFAEnabled ? "Yes" : "No"}</p>
          <p>ConnectedChain ID: {chainId}</p>
        </div>

        {/* User Info */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>User Info</p>
          <textarea disabled rows={5} value={JSON.stringify(userInfo, null, 2)} style={{ width: "100%" }} />
        </div>

        {/* User Token */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>User Token</p>
          {token && <textarea disabled rows={5} value={token} style={{ width: "100%" }} />}
          {!token && (
            <>
              {isUserTokenLoading ? (
                <p>Authenticating...</p>
              ) : (
                <button onClick={() => getIdentityToken()} className={styles.card}>
                  Authenticate User
                </button>
              )}
            </>
          )}
          {userTokenError && <p>Error: {userTokenError.message}</p>}
        </div>

        {/* MFA */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>MFA</p>
          {isMFAEnabled ? (
            <>
              {isManageMFALoading ? (
                <p>Managing MFA...</p>
              ) : (
                <button onClick={() => manageMFA()} className={styles.card}>
                  Manage MFA
                </button>
              )}
              {manageMFAError && <p>Error: {manageMFAError.message}</p>}
            </>
          ) : (
            <>
              {isEnableMFALoading ? (
                <p>Enabling MFA...</p>
              ) : (
                <button onClick={() => enableMFA()} className={styles.card}>
                  Enable MFA
                </button>
              )}
              {enableMFAError && <p>Error: {enableMFAError.message}</p>}
            </>
          )}
        </div>

        {/* Checkout */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Checkout</p>
          {isCheckoutLoading ? (
            <p>Checking out...</p>
          ) : (
            <button onClick={() => showCheckout()} className={styles.card}>
              Checkout
            </button>
          )}
          {checkoutError && <p>Error: {checkoutError.message}</p>}
        </div>

        {/* Wallet Connect Scanner */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Wallet Connect Scanner</p>
          {isWalletConnectScannerLoading ? (
            <p>Scanning...</p>
          ) : (
            <button onClick={() => showWalletConnectScanner()} className={styles.card}>
              Scan
            </button>
          )}
          {walletConnectScannerError && <p>Error: {walletConnectScannerError.message}</p>}
        </div>

        {/* Wallet UI */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Wallet UI</p>
          {isWalletUILoading ? (
            <p>Loading...</p>
          ) : (
            <button onClick={() => showWalletUI()} className={styles.card}>
              Wallet UI
            </button>
          )}
          {walletUIError && <p>Error: {walletUIError.message}</p>}
        </div>

        {/* Provider Actions */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Provider Actions</p>
          {/* Sign Message */}
          <button onClick={() => signMessageAsync({ message: "Hello, world!" })} className={styles.card}>
            Sign Message
          </button>
          {signedMessageData && <textarea disabled rows={5} value={signedMessageData} style={{ width: "100%" }} />}

          {/* Sign Typed Data */}
          <button
            onClick={() =>
              signTypedData({
                types: {
                  Person: [
                    { name: "name", type: "string" },
                    { name: "wallet", type: "address" },
                  ],
                  Mail: [
                    { name: "from", type: "Person" },
                    { name: "to", type: "Person" },
                    { name: "contents", type: "string" },
                  ],
                },
                primaryType: "Mail",
                message: {
                  from: {
                    name: "Cow",
                    wallet: "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826",
                  },
                  to: {
                    name: "Bob",
                    wallet: "0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB",
                  },
                  contents: "Hello, Bob!",
                },
              })
            }
            className={styles.card}
          >
            Sign Typed Data
          </button>
          {signedTypedDataData && <textarea disabled rows={5} value={signedTypedDataData} style={{ width: "100%" }} />}
        </div>

        {/* Chain Actions */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Switch Chain</p>
          {chains.map((chain) => (
            <button
              key={chain.id}
              onClick={async () => switchChainAsync({ chainId: chain.id })}
              className={styles.card}
              disabled={chainId === chain.id}
              style={{ opacity: chainId === chain.id ? 0.5 : 1 }}
            >
              Switch to {chain.name}
            </button>
          ))}
        </div>

        {/* Disconnect */}
        <div style={{ marginTop: "16px", marginBottom: "16px" }}>
          <p>Logout</p>
          <button onClick={() => disconnect()} className={styles.card}>
            Disconnect
          </button>
        </div>
      </div>
    </>
  );

  const unloggedInView = (
    <>
      {connecting ? (
        <p>Connecting to {connectorName}...</p>
      ) : (
        <>
          <button onClick={() => connect()} className={styles.card}>
            Login with Modal
          </button>
          <button onClick={() => connectTo("auth", { authConnection: "facebook" })} className={styles.card}>
            Login with Facebook
          </button>
        </>
      )}
      {connectingError && <p>Error: {connectingError.message}</p>}
    </>
  );

  return (
    <div className={styles.grid}>
      <p>Web3Auth: {isConnected ? "Connected" : "Disconnected"}</p>
      <p>Wagmi: {isWagmiConnected ? "Connected" : "Disconnected"}</p>
      {provider || isWagmiConnected ? loggedInView : unloggedInView}
    </div>
  );
};

export default Main;



================================================
FILE: demo/wagmi-react-app/src/styles/Home.module.css
================================================
.container {
  width: 60%;
  margin: auto;
  padding: 0 2rem;
}

.main {
  min-height: 100vh;
  padding: 4rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  line-height: 1.15;
  font-size: 3rem;
  text-align: center;
  margin: 50px;
}

.title a {
  color: #0070f3;
  text-decoration: none;
}

.console {
  max-width: 100%;
}

.code {
  background: #fafafa;
  border-radius: 5px;
  padding: 0.75rem;
  font-size: 1.1rem;
  font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace;
  overflow-wrap: break-word;
}

.grid {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.setting {
  display: flex;
  align-items: center;
  flex-direction: column;
  padding: 20px;
  margin: 30px 0;
  background: #f4f5f7;
  border: 1px solid #ebecf0;
  border-radius: 5px;
}

.card {
  margin: 0.5rem;
  padding: 0.7rem;
  text-align: center;
  color: #0070f3;
  text-decoration: none;
  border: 1px solid #0070f3;
  border-radius: 10px;
  transition: color 0.15s ease, border-color 0.15s ease;
  width: 100%;
}

.card:hover,
.card:focus,
.card:active {
  cursor: pointer;
  background-color: #fafafa;
}

.row {
  display: flex;
  margin-bottom: 0.5rem;
  width: 100%;
}
.label {
  flex-basis: 45%;
  padding-right: 10px;
  display: flex;
  align-items: center;
  justify-content: right;
  font-weight: bold;
}

.select {
  flex-basis: 30%;
  text-align: left;
  padding: 0.3rem 0.8rem;
  font-size: 1rem;
  border-radius: 8px;
}

.footer {
  display: flex;
  flex: 1;
  padding: 2rem 0;
  border-top: 1px solid #eaeaea;
  justify-content: center;
  align-items: center;
  margin-top: 10rem;
}

.footer a {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-grow: 1;
}

.logo {
  height: 1.5rem;
  margin-left: 0.5rem;
}

/* @media (max-width: 1200px) {
  .container {
    width: 100%;
  }
} */



================================================
FILE: locales/importLocales.mjs
================================================
/* eslint-disable promise/always-return */

import fs from "fs";
import path from "path";

const args = process.argv.slice(2);
const branch = args[0] || "main";
const repoUrl = `https://raw.githubusercontent.com/Web3Auth/web3auth-locales/${branch}/Web3Auth-locale`;
const localeGroups = ["locale-common"];
const promises = [];
const locales = {};

localeGroups.forEach((group) => {
  const urlFetch = `${repoUrl}/${group}.json`;
  promises.push(fetch(urlFetch).then((res) => res.json()));
});

function processRecords(items) {
  Object.keys(items).forEach((groupKey) => {
    Object.keys(items[groupKey]).forEach((wordKey) => {
      Object.keys(items[groupKey][wordKey]).forEach((localeKey) => {
        if (!locales[localeKey]) locales[localeKey] = {};
        if (!locales[localeKey][groupKey]) locales[localeKey][groupKey] = {};
        locales[localeKey][groupKey][wordKey] = items[groupKey][wordKey][localeKey];
      });
    });
  });
}

Promise.all(promises)
  .then((results) => {
    results.forEach((set) => {
      processRecords(set);
    });

    // Create json files
    const folder = "./packages/modal/src/ui/i18n/";
    const folderPath = path.resolve(folder);
    if (!fs.existsSync(folderPath)) {
      fs.mkdirSync(folderPath);
    }

    const keys = Object.keys(locales);
    for (const localeKey of keys) {
      if (Object.prototype.hasOwnProperty.call(locales, localeKey)) {
        const filePath = path.resolve(`${folder}${localeKey}.json`);
        fs.writeFile(filePath, JSON.stringify(locales[localeKey], null, 2), { flag: "w" }, (error) => {
          if (error) throw error;
        });
      }
    }
  })
  .catch((error) => {
    // eslint-disable-next-line no-console
    console.error(error);
  });



================================================
FILE: packages/modal/README.md
================================================
# Web3Auth Plug and Play Modal

[![npm version](https://img.shields.io/npm/v/@web3auth/modal?label=%22%22)](https://www.npmjs.com/package/@web3auth/modal/v/latest)
[![minzip](https://img.shields.io/bundlephobia/minzip/@web3auth/modal?label=%22%22)](https://bundlephobia.com/result?p=@web3auth/modal@latest)

> Web3Auth is where passwordless auth meets non-custodial key infrastructure for Web3 apps and wallets. By aggregating OAuth (Google, Twitter, Discord) logins, different wallets and innovative Multi Party Computation (MPC) - Web3Auth provides a seamless login experience to every user on your application.

This package provides main class for using default Web3Auth Modal. The package includes all of our packages and gives you a simple way of implementing Web3Auth within your interface. Additionally, it is a child class of [`@web3auth/no-modal`](https://web3auth.io/docs/sdk/web/no-modal/) package. Hence, you can still call all the functions available in the [`@web3auth/no-modal`](https://web3auth.io/docs/sdk/web/no-modal/) package.

## 📖 Documentation

Checkout the official [Web3Auth Documentation](https://web3auth.io/docs/sdk/web/web3auth/) to get started.

## 💡 Features

- Plug and Play, OAuth based Web3 Authentication Service
- Fully decentralized, non-custodial key infrastructure
- End to end Whitelabelable solution
- Threshold Cryptography based Key Reconstruction
- Multi Factor Authentication Setup & Recovery (Includes password, backup phrase, device factor editing/deletion etc)
- Support for WebAuthn & Passwordless Login
- Support for connecting to multiple wallets
- DApp Active Session Management

...and a lot more

## 🔗 Installation

```shell
npm install --save @web3auth/modal
```

## ⚡ Quick Start

### Get your Client ID from Web3Auth Dashboard

Hop on to the [Web3Auth Dashboard](https://dashboard.web3auth.io/) and create a new project. Use the Client ID of the project to start your integration.

![Web3Auth Dashboard](https://github-production-user-asset-6210df.s3.amazonaws.com/6962565/272779464-043f6383-e671-4aa5-80fb-ec87c569e5ab.png)

### Initialize Web3Auth for your preferred blockchain

Web3Auth needs to initialise as soon as your app loads up to enable the user to log in. Preferably done within a constructor, initialisation is the step where you can pass on all the configurations for Web3Auth you want. A simple integration for Ethereum blockchain will look like this:

```js
import { Web3Auth } from "web3auth";

//Initialize within your constructor
const web3auth = new Web3Auth({
  clientId: "", // Get your Client ID from Web3Auth Dashboard
  chainConfig: {
    chainNamespace: "eip155",
    chainId: "0x1",
  },
});

await web3auth.init();
```

### Login your User

Once you're done initialising, just create a button that triggers to open the login modal for the user on their request. Logging in is as easy as:

```js
await web3auth.connect();
```

## 🩹 Examples

Check out the examples for your preferred blockchain and platform on our [examples page](https://web3auth.io/docs/examples).

## 🌐 Demo

Checkout the [Web3Auth Demo](https://demo.web3auth.io) to see how Web3Auth can be used in your application.

## 💬 Troubleshooting and Support

- Have a look at our [Community Portal](https://community.web3auth.io/) to see if anyone has any questions or issues you might be having. Feel free to reate new topics and we'll help you out as soon as possible.
- Checkout our [Troubleshooting Documentation Page](https://web3auth.io/docs/troubleshooting) to know the common issues and solutions.
- For Priority Support, please have a look at our [Pricing Page](https://web3auth.io/pricing.html) for the plan that suits your needs.



================================================
FILE: packages/modal/babel.config.js
================================================
module.exports = {
  presets: [["@babel/preset-react", { runtime: "automatic" }]],
};



================================================
FILE: packages/modal/eslint.config.mjs
================================================
import toruslabsReact from "@toruslabs/eslint-config-react";

export default [
  ...toruslabsReact,
  {
    ignores: ["./rollup.config.mjs"],
  },
  {
    files: ["./src/react/wagmi/**.ts", "./src/vue/wagmi/**.ts"],
    rules: {
      "import/no-extraneous-dependencies": "off",
    },
  },
  {
    files: ["./src/vue/**/*.ts"],
    rules: {
      "react-hooks/rules-of-hooks": "off",
    },
  },
];



================================================
FILE: packages/modal/package.json
================================================
{
  "name": "@web3auth/modal",
  "version": "10.0.5",
  "description": "Multi chain wallet aggregator for web3Auth",
  "keywords": [
    "web3Auth/ui",
    "web3Auth",
    "multichainWallet",
    "blockchain",
    "ethereum",
    "solana"
  ],
  "main": "dist/lib.cjs/packages/modal/src/index.js",
  "module": "dist/lib.esm/packages/modal/src/index.js",
  "unpkg": "dist/modal.umd.min.js",
  "jsdelivr": "dist/modal.umd.min.js",
  "types": "dist/lib.cjs/types/index.d.ts",
  "author": "Torus Labs",
  "bugs": {
    "url": "https://github.com/Web3Auth/Web3Auth/issues"
  },
  "files": [
    "dist"
  ],
  "scripts": {
    "test": "mocha --config ../../.mocharc.json test/**.ts",
    "test-debugger": "mocha --config ../../.mocharc.json --inspect-brk test/**.ts",
    "dev": "torus-scripts start",
    "build": "torus-scripts build",
    "lint": "eslint --fix 'src/**/*.ts'",
    "prepack": "npm run build",
    "pre-commit": "lint-staged --cwd ."
  },
  "peerDependenciesMeta": {
    "@coinbase/wallet-sdk": {
      "optional": true
    },
    "viem": {
      "optional": true
    },
    "vue": {
      "optional": true
    }
  },
  "peerDependencies": {
    "@babel/runtime": "^7.x",
    "@coinbase/wallet-sdk": "^4.3.x",
    "@solana/web3.js": ">=1.98",
    "react": ">=18",
    "react-dom": ">=18",
    "viem": ">=2.23",
    "vue": ">=3.x"
  },
  "devDependencies": {
    "@babel/preset-react": "^7.27.1",
    "@coinbase/wallet-sdk": "^4.3.4",
    "@mertasan/tailwindcss-variables": "^2.7.0",
    "@rollup/plugin-json": "^6.1.0",
    "@rollup/plugin-replace": "^6.0.2",
    "@rollup/plugin-url": "^8.0.2",
    "@solana/web3.js": "^1.98.2",
    "@svgr/rollup": "^8.1.0",
    "@svgr/webpack": "^8.1.0",
    "@toruslabs/eslint-config-react": "^4.1.4",
    "@toruslabs/eslint-config-vue": "^4.1.5",
    "@toruslabs/isomorphic-style-loader": "^5.4.0",
    "@toruslabs/vue-components": "^8.0.8",
    "@types/react": "^19.1.8",
    "@types/react-dom": "^19.1.6",
    "@wagmi/core": "^2.17.3",
    "@wagmi/vue": "^0.1.22",
    "autoprefixer": "^10.4.21",
    "css-loader": "^7.1.2",
    "live-server": "^1.2.2",
    "postcss": "^8.5.6",
    "postcss-loader": "^8.1.1",
    "postcss-prefix-selector": "^2.1.1",
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "rollup-plugin-postcss": "^4.0.2",
    "rollup-preserve-directives": "^1.1.3",
    "style-loader": "^4.0.0",
    "tailwindcss": "^3.4.17",
    "url-loader": "^4.1.1",
    "viem": "^2.31.3",
    "vue": "^3.5.17",
    "wagmi": "^2.15.6"
  },
  "dependencies": {
    "@hcaptcha/react-hcaptcha": "^1.12.0",
    "@toruslabs/base-controllers": "^8.6.0",
    "@toruslabs/http-helpers": "^8.1.1",
    "@web3auth/auth": "^10.5.0",
    "@web3auth/no-modal": "^10.0.5",
    "bowser": "^2.11.0",
    "classnames": "^2.5.1",
    "clsx": "^2.1.1",
    "color": "^5.0.0",
    "copy-to-clipboard": "^3.3.3",
    "deepmerge": "^4.3.1",
    "i18next": "^25.2.1",
    "react-i18next": "^15.5.3",
    "react-qrcode-logo": "^3.0.0",
    "tailwind-merge": "^3.3.1"
  },
  "exports": {
    ".": {
      "import": "./dist/lib.esm/packages/modal/src/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/index.js",
      "types": "./dist/lib.cjs/types/index.d.ts"
    },
    "./react": {
      "import": "./dist/lib.esm/packages/modal/src/react/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/react/index.js",
      "types": "./dist/lib.cjs/types/react/index.d.ts"
    },
    "./react/wagmi": {
      "import": "./dist/lib.esm/packages/modal/src/react/wagmi/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/react/wagmi/index.js",
      "types": "./dist/lib.cjs/types/react/wagmi/index.d.ts"
    },
    "./react/solana": {
      "import": "./dist/lib.esm/packages/modal/src/react/solana/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/react/solana/index.js",
      "types": "./dist/lib.cjs/types/react/solana/index.d.ts"
    },
    "./vue": {
      "import": "./dist/lib.esm/packages/modal/src/vue/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/vue/index.js",
      "types": "./dist/lib.cjs/types/vue/index.d.ts"
    },
    "./vue/solana": {
      "import": "./dist/lib.esm/packages/modal/src/vue/solana/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/vue/solana/index.js",
      "types": "./dist/lib.cjs/types/vue/solana/index.d.ts"
    },
    "./vue/wagmi": {
      "import": "./dist/lib.esm/packages/modal/src/vue/wagmi/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/vue/wagmi/index.js",
      "types": "./dist/lib.cjs/types/vue/wagmi/index.d.ts"
    },
    "./connectors/coinbase-connector": {
      "import": "./dist/lib.esm/packages/modal/src/connectors/coinbase-connector/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/connectors/coinbase-connector/index.js",
      "types": "./dist/lib.cjs/types/connectors/coinbase-connector/index.d.ts"
    },
    "./providers/xrpl-provider": {
      "import": "./dist/lib.esm/packages/modal/src/providers/xrpl-provider/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/providers/xrpl-provider/index.js",
      "types": "./dist/lib.cjs/types/providers/xrpl-provider/index.d.ts"
    },
    "./providers/ethereum-mpc-provider": {
      "import": "./dist/lib.esm/packages/modal/src/providers/ethereum-mpc-provider/index.js",
      "require": "./dist/lib.cjs/packages/modal/src/providers/ethereum-mpc-provider/index.js",
      "types": "./dist/lib.cjs/types/providers/ethereum-mpc-provider/index.d.ts"
    }
  },
  "typesVersions": {
    "*": {
      "react": [
        "./dist/lib.cjs/types/react/index.d.ts"
      ],
      "react/wagmi": [
        "./dist/lib.cjs/types/react/wagmi/index.d.ts"
      ],
      "react/solana": [
        "./dist/lib.cjs/types/react/solana/index.d.ts"
      ],
      "vue": [
        "./dist/lib.cjs/types/vue/index.d.ts"
      ],
      "vue/solana": [
        "./dist/lib.cjs/types/vue/solana/index.d.ts"
      ],
      "vue/wagmi": [
        "./dist/lib.cjs/types/vue/wagmi/index.d.ts"
      ],
      "connectors/coinbase-connector": [
        "./dist/lib.cjs/types/connectors/coinbase-connector/index.d.ts"
      ],
      "providers/xrpl-provider": [
        "./dist/lib.cjs/types/providers/xrpl-provider/index.d.ts"
      ],
      "providers/ethereum-mpc-provider": [
        "./dist/lib.cjs/types/providers/ethereum-mpc-provider/index.d.ts"
      ]
    }
  },
  "engines": {
    "node": ">=20.x",
    "npm": ">=9.x"
  },
  "lint-staged": {
    "!(*d).ts": [
      "eslint --cache --fix",
      "prettier --write"
    ]
  },
  "publishConfig": {
    "access": "public"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Web3Auth/Web3Auth.git"
  },
  "gitHead": "6c62ee11818e12b77eca33a78ee896e46549ac16"
}



================================================
FILE: packages/modal/postcss.config.js
================================================
const prefix = ".w3a-parent-container";

module.exports = {
  plugins: {
    tailwindcss: {},
    "postcss-prefix-selector": {
      prefix,
      transform(_, selector, prefixedSelector) {
        // if selector is already the prefix just return it
        // e.g. in the case of css vars that we put under prefix
        if (selector === prefix) {
          return selector;
        }
        return prefixedSelector;
      },
    },
  },
};



================================================
FILE: packages/modal/rollup.config.mjs
================================================
/* eslint-disable import/no-extraneous-dependencies */
import json from "@rollup/plugin-json";
import replace from "@rollup/plugin-replace";
import url from "@rollup/plugin-url";
import svgr from "@svgr/rollup";
import { readJSONFile } from "@toruslabs/torus-scripts/helpers/utils.js";
import path from "path";
import postcss from "rollup-plugin-postcss";
import preserveDirectives from 'rollup-preserve-directives'

const pkg = await readJSONFile(path.resolve("./package.json"));
const allDeps = [...Object.keys(pkg.dependencies || {}), ...Object.keys(pkg.peerDependencies || {}), "wagmi", "@wagmi/vue", "@wagmi/core"];

// TODO: use ssr module for cjs build

export const baseConfig = {
  input: [
    "./src/index.ts",
    "./src/react/index.ts",
    "./src/vue/index.ts",
    "./src/react/wagmi/index.ts",
    "./src/react/solana/index.ts",
    "./src/vue/solana/index.ts",
    "./src/vue/wagmi/index.ts",

    // re-exports from no-modal sdk.
    "./src/connectors/coinbase-connector/index.ts",
    "./src/providers/xrpl-provider/index.ts",
    "./src/providers/ethereum-mpc-provider/index.ts",
  ],
  plugins: [
    replace({
      "process.env.WEB3AUTH_VERSION": `"${pkg.version}"`,
      preventAssignment: true,
    }),
    postcss({
      config: {
        path: path.resolve("./postcss.config.js"),
      },
      extensions: [".css"],
      minimize: true,
    }),
    url(),
    svgr(),
    json(),
    preserveDirectives(),
  ],
  external: [...allDeps, ...allDeps.map((x) => new RegExp(`^${x}/`)), /@babel\/runtime/],
};



================================================
FILE: packages/modal/tailwind.config.js
================================================
const web3AuthBasePreset = require("@toruslabs/vue-components/web3auth-base-preset");

/** @type {import('tailwindcss').Config} */
module.exports = {
  presets: [web3AuthBasePreset],
  prefix: "w3a--",
  darkMode: "class",
  content: ["./src/**/*.{html,js,ts,tsx,jsx}"],
  theme: {
    extend: {
      colors: {
        app: {
          primary: {
            950: "#2D4874",
          },
        },
      },
      boxShadow: {
        modal: "0px 4px 16px rgba(0, 0, 0, 0.08)",
        autofill: "0 0 0 30px #f9fafb inset !important",
        autofillDark: "0 0 0 30px #374151 inset !important",
        light: "0px 2px 8px 2px #E5E7EB",
        dark: "0px 2px 8px 2px #111928",
      },
      backgroundImage: {
        select: `url('data:image/svg + xml;charset=utf-8,%3Csvgxmlns="http://www.w3.org/2000/svg"fill="none"viewBox="002020"%3E%3Cpathstroke="%236B7280"stroke-linecap="round"stroke-linejoin="round"stroke-width="1.5"d="m68444-4"/%3E%3C/svg%3E')`,
        // TODO: import via design system
        "gradient-conic": "conic-gradient(transparent, var(--tw-gradient-to))",
      },
    },
    variables: {
      // place the variables under w3a-parent-container instead of the default (:root)
      // since it may conflict with css vars of dApps integrating us
      ".w3a-parent-container": {
        ...web3AuthBasePreset.theme.variables,
      },
    },
  },
  plugins: [require("@mertasan/tailwindcss-variables")],
};



================================================
FILE: packages/modal/torus.config.js
================================================
module.exports = {
  esm: false,
};



================================================
FILE: packages/modal/tsconfig.build.json
================================================
{
  "extends": "./tsconfig.json",
  "include": ["src"],
  "compilerOptions": {
    "outDir": "dist",
    "declarationDir": "./dist/types",
  }
}



================================================
FILE: packages/modal/tsconfig.json
================================================
{
  "extends": "../../tsconfig.json",
  "include": ["src"],
  "compilerOptions": {
    "resolveJsonModule": true,
    "jsx": "react-jsx"
  }
}



================================================
FILE: packages/modal/webpack.config.js
================================================
const path = require("path");
const { EnvironmentPlugin } = require("webpack");
const generateWebpackConfig = require("../../webpack.config");

const pkg = require("./package.json");

const currentPath = path.resolve(".");

const ssrModule = {
  rules: [
    {
      test: /\.css$/,
      use: [
        "@toruslabs/isomorphic-style-loader",
        {
          loader: "css-loader",
        },
        {
          loader: "postcss-loader",
          options: {
            postcssOptions: {
              plugins: {
                tailwindcss: {},
                autoprefixer: {},
              },
            },
          },
        },
      ],
    },
    {
      test: /\.svg$/,
      exclude: /node_modules/,
      use: ["@svgr/webpack", "url-loader"],
    },
  ],
};

const config = generateWebpackConfig({
  currentPath,
  pkg,
  alias: {},
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: [
          { loader: "style-loader", options: {} },
          { loader: "css-loader", options: {} },
          {
            loader: "postcss-loader",
            options: {
              postcssOptions: {
                plugins: {
                  tailwindcss: {},
                  autoprefixer: {},
                },
              },
            },
          },
        ],
      },
      {
        test: /\.svg$/,
        exclude: /node_modules/,
        use: ["@svgr/webpack", "url-loader"],
      },
    ],
  },
  plugins: [new EnvironmentPlugin({ WEB3AUTH_VERSION: pkg.version })],
  ssrModule,
});

module.exports = config;



================================================
FILE: packages/modal/src/config.ts
================================================
import { EVM_CONNECTORS, type WALLET_CONNECTOR_TYPE } from "@web3auth/no-modal";

import { ConnectorsModalConfig, ModalConfig } from "./interface";

export const version = process.env.WEB3AUTH_VERSION;

export const defaultConnectorsModalConfig: ConnectorsModalConfig = {
  hideWalletDiscovery: false,
  connectors: {
    [EVM_CONNECTORS.AUTH]: {
      label: "Auth",
      showOnModal: true,
    },
  } as Record<WALLET_CONNECTOR_TYPE, ModalConfig>,
};

export const walletRegistryUrl = "https://assets.web3auth.io/v1/wallet-registry.json";



================================================
FILE: packages/modal/src/index.ts
================================================
export * from "./config";
export * from "./interface";
export * from "./modalManager";
export * from "@web3auth/no-modal";



================================================
FILE: packages/modal/src/interface.ts
================================================
import type { BaseConnectorConfig, IProvider, IWeb3Auth, LoginMethodConfig, WALLET_CONNECTOR_TYPE } from "@web3auth/no-modal";

export interface ModalConfig extends Omit<BaseConnectorConfig, "isInjected" | "chainNamespaces"> {
  loginMethods?: LoginMethodConfig;
}

export interface ConnectorsModalConfig {
  connectors?: Partial<Record<WALLET_CONNECTOR_TYPE, ModalConfig>>;
  hideWalletDiscovery?: boolean;
}
export interface IWeb3AuthModal extends IWeb3Auth {
  connect(): Promise<IProvider | null>;
}



================================================
FILE: packages/modal/src/modalManager.ts
================================================
import { AuthConnectionConfigItem, serializeError } from "@web3auth/auth";
import {
  ANALYTICS_EVENTS,
  ANALYTICS_SDK_TYPE,
  type AUTH_CONNECTION_TYPE,
  type AuthConnectorType,
  type AuthLoginParams,
  type BaseConnectorConfig,
  type ChainNamespaceType,
  cloneDeep,
  CONNECTOR_CATEGORY,
  CONNECTOR_EVENTS,
  CONNECTOR_NAMES,
  CONNECTOR_NAMESPACES,
  CONNECTOR_STATUS,
  fetchProjectConfig,
  fetchWalletRegistry,
  getErrorAnalyticsProperties,
  type IConnector,
  type IProvider,
  type IWeb3AuthCoreOptions,
  IWeb3AuthState,
  log,
  LOGIN_MODE,
  type LoginMethodConfig,
  type ProjectConfig,
  sdkVersion,
  type WALLET_CONNECTOR_TYPE,
  WALLET_CONNECTORS,
  WalletInitializationError,
  type WalletRegistry,
  Web3AuthNoModal,
  withAbort,
} from "@web3auth/no-modal";
import deepmerge from "deepmerge";

import { defaultConnectorsModalConfig, walletRegistryUrl } from "./config";
import { type ConnectorsModalConfig, type IWeb3AuthModal, type ModalConfig } from "./interface";
import { AUTH_PROVIDERS, AUTH_PROVIDERS_NAMES, capitalizeFirstLetter, getUserLanguage, LOGIN_MODAL_EVENTS, LoginModal, type UIConfig } from "./ui";

export interface Web3AuthOptions extends IWeb3AuthCoreOptions {
  /**
   * Config for configuring modal ui display properties
   */
  uiConfig?: Omit<UIConfig, "connectorListener">;

  /**
   * Config for configuring modal ui display properties
   */
  modalConfig?: ConnectorsModalConfig;
}

export class Web3Auth extends Web3AuthNoModal implements IWeb3AuthModal {
  public loginModal: LoginModal;

  readonly options: Web3AuthOptions;

  private modalConfig: ConnectorsModalConfig = cloneDeep(defaultConnectorsModalConfig);

  constructor(options: Web3AuthOptions, initialState?: IWeb3AuthState) {
    super(options, initialState);
    this.options = { ...options };

    if (!this.options.uiConfig) this.options.uiConfig = {};
    if (this.options.modalConfig) this.modalConfig = this.options.modalConfig;

    log.info("modalConfig", this.modalConfig);
  }

  public async init(options?: { signal?: AbortSignal }): Promise<void> {
    // init analytics
    const startTime = Date.now();
    this.analytics.init();
    this.analytics.identify(this.options.clientId, {
      web3auth_client_id: this.options.clientId,
      web3auth_network: this.options.web3AuthNetwork,
    });
    this.analytics.setGlobalProperties({
      dapp_url: window.location.origin,
      sdk_name: ANALYTICS_SDK_TYPE.WEB_MODAL,
      sdk_version: sdkVersion,
      // Required for organization analytics
      web3auth_client_id: this.options.clientId,
      web3auth_network: this.options.web3AuthNetwork,
    });
    let trackData: Record<string, unknown> = {};

    try {
      const { signal } = options || {};

      super.checkInitRequirements();
      // get project config and wallet registry
      const { projectConfig, walletRegistry } = await this.getProjectAndWalletConfig();

      // init config
      this.initUIConfig(projectConfig);
      super.initAccountAbstractionConfig(projectConfig);
      super.initChainsConfig(projectConfig);
      super.initCachedConnectorAndChainId();
      super.initWalletServicesConfig(projectConfig);
      this.analytics.setGlobalProperties({ team_id: projectConfig.teamId });
      trackData = this.getInitializationTrackData();

      // init login modal
      const { filteredWalletRegistry, disabledExternalWallets } = this.filterWalletRegistry(walletRegistry, projectConfig);
      this.loginModal = new LoginModal(
        {
          ...this.options.uiConfig,
          connectorListener: this,
          web3authClientId: this.options.clientId,
          web3authNetwork: this.options.web3AuthNetwork,
          authBuildEnv: this.options.authBuildEnv,
          chainNamespaces: this.getChainNamespaces(),
          walletRegistry: filteredWalletRegistry,
          analytics: this.analytics,
        },
        {
          onInitExternalWallets: this.onInitExternalWallets,
          onSocialLogin: this.onSocialLogin,
          onExternalWalletLogin: this.onExternalWalletLogin,
          onModalVisibility: this.onModalVisibility,
        }
      );
      await withAbort(() => this.loginModal.initModal(), signal);

      // setup common JRPC provider
      await withAbort(() => this.setupCommonJRPCProvider(), signal);

      // initialize connectors
      this.on(CONNECTOR_EVENTS.CONNECTORS_UPDATED, ({ connectors: newConnectors }) => {
        const onAbortHandler = () => {
          log.debug("init aborted");
          if (this.connectors?.length > 0) {
            super.cleanup();
          }
        };
        withAbort(() => this.initConnectors({ connectors: newConnectors, projectConfig, disabledExternalWallets }), signal, onAbortHandler);
      });

      await withAbort(() => super.loadConnectors({ projectConfig, modalMode: true }), signal);

      // initialize plugins
      await withAbort(() => super.initPlugins(), signal);

      // track completion event
      const authConnector = this.getConnector(WALLET_CONNECTORS.AUTH) as AuthConnectorType;
      trackData = {
        ...trackData,
        connectors: this.connectors.map((connector) => connector.name),
        plugins: Object.keys(this.plugins),
        auth_ux_mode: authConnector?.authInstance?.options?.uxMode || this.coreOptions.uiConfig?.uxMode,
      };
      this.analytics.track(ANALYTICS_EVENTS.SDK_INITIALIZATION_COMPLETED, {
        ...trackData,
        duration: Date.now() - startTime,
      });
    } catch (error) {
      if (error instanceof DOMException && error.name === "AbortError") return;

      // track failure event
      this.analytics.track(ANALYTICS_EVENTS.SDK_INITIALIZATION_FAILED, {
        ...trackData,
        ...getErrorAnalyticsProperties(error),
        duration: Date.now() - startTime,
      });
      log.error("Failed to initialize modal", error);
      throw error;
    }
  }

  public async connect(): Promise<IProvider | null> {
    if (!this.loginModal) throw WalletInitializationError.notReady("Login modal is not initialized");
    // if already connected return provider
    if (this.connectedConnectorName && this.status === CONNECTOR_STATUS.CONNECTED && this.provider) return this.provider;
    this.loginModal.open();
    return new Promise((resolve, reject) => {
      // remove all listeners when promise is resolved or rejected.
      // this is to prevent memory leaks if user clicks connect button multiple times.
      const handleConnected = () => {
        this.removeListener(CONNECTOR_EVENTS.ERRORED, handleError);
        this.removeListener(LOGIN_MODAL_EVENTS.MODAL_VISIBILITY, handleVisibility);
        return resolve(this.provider);
      };

      const handleError = (err: unknown) => {
        this.removeListener(CONNECTOR_EVENTS.CONNECTED, handleConnected);
        this.removeListener(LOGIN_MODAL_EVENTS.MODAL_VISIBILITY, handleVisibility);
        return reject(err);
      };

      const handleVisibility = (visibility: boolean) => {
        // modal is closed but user is not connected to any wallet.
        if (!visibility && this.status !== CONNECTOR_STATUS.CONNECTED) {
          this.removeListener(CONNECTOR_EVENTS.CONNECTED, handleConnected);
          this.removeListener(CONNECTOR_EVENTS.ERRORED, handleError);
          return reject(new Error("User closed the modal"));
        }
      };

      this.once(CONNECTOR_EVENTS.CONNECTED, handleConnected);
      this.once(CONNECTOR_EVENTS.ERRORED, handleError);
      this.once(LOGIN_MODAL_EVENTS.MODAL_VISIBILITY, handleVisibility);
    });
  }

  protected initUIConfig(projectConfig: ProjectConfig) {
    super.initUIConfig(projectConfig);
    this.options.uiConfig = deepmerge(cloneDeep(projectConfig.whitelabel || {}), this.options.uiConfig || {});
    if (!this.options.uiConfig.defaultLanguage) this.options.uiConfig.defaultLanguage = getUserLanguage(this.options.uiConfig.defaultLanguage);
    if (!this.options.uiConfig.mode) this.options.uiConfig.mode = "light";
    this.options.uiConfig = deepmerge(projectConfig.loginModal || {}, this.options.uiConfig, {
      arrayMerge: (_, sourceArray) => sourceArray,
    });

    // merge login methods order from project config and user config, with user config taking precedence
    const defaultAuthConnections = projectConfig.embeddedWalletAuth.filter((x) => x.isDefault).map((x) => x.authConnection);
    const mergedAuthConnections = [...(this.options.uiConfig.loginMethodsOrder || []), ...defaultAuthConnections];
    const loginMethodsOrder = [];
    const authConnectionSet = new Set();
    for (const authConnection of mergedAuthConnections) {
      if (authConnectionSet.has(authConnection)) continue;
      authConnectionSet.add(authConnection);
      loginMethodsOrder.push(authConnection);
    }
    this.options.uiConfig.loginMethodsOrder = loginMethodsOrder;
  }

  protected getInitializationTrackData(): Record<string, unknown> {
    return {
      ...super.getInitializationTrackData(),
      modal_hide_wallet_discovery: this.modalConfig?.hideWalletDiscovery,
      modal_connectors: Object.keys(this.modalConfig?.connectors || {}),
      modal_auth_connector_login_methods: Object.keys(this.modalConfig?.connectors?.[WALLET_CONNECTORS.AUTH]?.loginMethods || {}),
      // UI config
      ui_login_methods_order: this.options.uiConfig?.loginMethodsOrder,
      ui_modal_z_index: this.options.uiConfig?.modalZIndex,
      ui_display_errors_on_modal: this.options.uiConfig?.displayErrorsOnModal,
      ui_login_grid_col: this.options.uiConfig?.loginGridCol,
      ui_primary_button: this.options.uiConfig?.primaryButton,
      ui_modal_widget_type: this.options.uiConfig?.widgetType,
      ui_modal_target_id_used: Boolean(this.options.uiConfig?.targetId),
      ui_modal_logo_alignment: this.options.uiConfig?.logoAlignment,
      ui_modal_border_radius_type: this.options.uiConfig?.borderRadiusType,
      ui_modal_button_radius_type: this.options.uiConfig?.buttonRadiusType,
      ui_modal_sign_in_methods: this.options.uiConfig?.signInMethods,
      ui_modal_add_previous_login_hint: this.options.uiConfig?.addPreviousLoginHint,
      ui_modal_display_installed_external_wallets: this.options.uiConfig?.displayInstalledExternalWallets,
      ui_modal_display_external_wallets_count: this.options.uiConfig?.displayExternalWalletsCount,
    };
  }

  private filterWalletRegistry(
    walletRegistry: WalletRegistry,
    projectConfig: ProjectConfig
  ): { disabledExternalWallets: Set<string>; filteredWalletRegistry: WalletRegistry } {
    const { disableAllRecommendedWallets, disableAllOtherWallets, disabledWallets } = projectConfig.externalWalletAuth || {};

    // add disabled wallets to set
    const disabledExternalWallets = new Set(disabledWallets || []);
    if (disableAllRecommendedWallets) {
      Object.keys(walletRegistry.default).forEach((wallet) => disabledExternalWallets.add(wallet));
    }
    if (disableAllOtherWallets) {
      Object.keys(walletRegistry.others).forEach((wallet) => disabledExternalWallets.add(wallet));
    }
    // always show MetaMask, force enable it
    disabledExternalWallets.delete(WALLET_CONNECTORS.METAMASK);

    // remove wallets that are disabled in project config from wallet registry
    const filteredWalletRegistry = cloneDeep(walletRegistry);
    disabledExternalWallets.forEach((wallet) => {
      delete filteredWalletRegistry.default[wallet];
      delete filteredWalletRegistry.others[wallet];
    });
    return { disabledExternalWallets, filteredWalletRegistry };
  }

  private async getProjectAndWalletConfig() {
    const [projectConfigResult, walletRegistryResult] = await Promise.allSettled([
      fetchProjectConfig({
        clientId: this.options.clientId,
        web3AuthNetwork: this.options.web3AuthNetwork,
        aaProvider: this.options.accountAbstractionConfig?.smartAccountType,
        authBuildEnv: this.options.authBuildEnv,
      }),
      fetchWalletRegistry(walletRegistryUrl),
    ]);

    // handle project config result
    if (projectConfigResult.status === "rejected") {
      const error = await serializeError(projectConfigResult.reason);
      log.error("Failed to fetch project configurations", error);
      throw WalletInitializationError.notReady("failed to fetch project configurations", error);
    }
    const projectConfig = projectConfigResult.value;

    // handle wallet registry result
    let walletRegistry: WalletRegistry = { others: {}, default: {} };
    const isExternalWalletEnabled = Boolean(projectConfig.externalWalletAuth);
    if (isExternalWalletEnabled && !this.modalConfig?.hideWalletDiscovery) {
      if (walletRegistryResult.status === "fulfilled") {
        walletRegistry = walletRegistryResult.value;
      } else {
        log.error("Failed to fetch wallet registry", walletRegistryResult.reason);
      }
    }
    return { projectConfig, walletRegistry };
  }

  private async initConnectors({
    connectors,
    projectConfig,
    disabledExternalWallets,
  }: {
    connectors: IConnector<unknown>[];
    projectConfig: ProjectConfig;
    disabledExternalWallets: Set<string>;
  }) {
    // filter connectors based on config
    const filteredConnectorNames = await this.filterConnectors({ projectConfig, disabledExternalWallets });

    // initialize connectors based on availability
    const { hasInAppConnectors, hasExternalConnectors } = await this.checkConnectorAvailability(filteredConnectorNames);
    const filteredConnectors = connectors.filter((x) => filteredConnectorNames.includes(x.name as WALLET_CONNECTOR_TYPE));
    if (hasInAppConnectors) {
      await this.initInAppAndCachedConnectors(filteredConnectors);
    }
    if (hasExternalConnectors) {
      if (hasInAppConnectors) {
        // show connect button if both in-app and external wallets are available
        this.loginModal.initExternalWalletContainer();
        // initialize installed external wallets (except WC), don't mark external wallets as fully initialized
        this.initExternalConnectors(
          filteredConnectors.filter((x) => x.type === CONNECTOR_CATEGORY.EXTERNAL && x.name !== WALLET_CONNECTORS.WALLET_CONNECT_V2),
          { externalWalletsInitialized: false, showExternalWalletsOnly: false, externalWalletsVisibility: false }
        );
      } else {
        // if no in app wallet is available then initialize all external wallets in modal
        await this.initExternalConnectors(
          filteredConnectors.filter((x) => x.type === CONNECTOR_CATEGORY.EXTERNAL),
          { externalWalletsInitialized: true, showExternalWalletsOnly: true, externalWalletsVisibility: true }
        );
      }
    }

    // emit ready event if connector is ready
    if (this.status === CONNECTOR_STATUS.NOT_READY) {
      this.status = CONNECTOR_STATUS.READY;
      this.emit(CONNECTOR_EVENTS.READY);
    }
  }

  private async filterConnectors({
    projectConfig,
    disabledExternalWallets,
  }: {
    projectConfig: ProjectConfig;
    disabledExternalWallets: Set<string>;
  }): Promise<WALLET_CONNECTOR_TYPE[]> {
    // Auth connector config: populate this with the default config for auth connectors.
    const loginMethods: LoginMethodConfig = {};
    const embedWalletConfigMap: Map<string, AuthConnectionConfigItem & { isDefault?: boolean }> = new Map();
    for (const authConnectionConfig of projectConfig.embeddedWalletAuth || []) {
      const { isDefault, authConnection, groupedAuthConnectionId, authConnectionId } = authConnectionConfig;
      if (isDefault) {
        loginMethods[authConnection] = {
          name: AUTH_PROVIDERS_NAMES[authConnection],
          authConnection: authConnection as AUTH_CONNECTION_TYPE,
          authConnectionId: authConnectionId,
          groupedAuthConnectionId: groupedAuthConnectionId,
          extraLoginOptions: authConnectionConfig.jwtParameters,
          isDefault: true,
          showOnModal: true,
        };
      }
      embedWalletConfigMap.set(groupedAuthConnectionId || authConnectionId, authConnectionConfig);
    }

    const dashboardConnectorConfig = {
      [WALLET_CONNECTORS.AUTH]: { label: WALLET_CONNECTORS.AUTH, loginMethods },
    } as Record<WALLET_CONNECTOR_TYPE, ModalConfig>;

    // populate the user config data with the dashboard config.
    if (this.modalConfig?.connectors?.[WALLET_CONNECTORS.AUTH]) {
      if (!this.modalConfig.connectors[WALLET_CONNECTORS.AUTH].loginMethods) this.modalConfig.connectors[WALLET_CONNECTORS.AUTH].loginMethods = {};
    }

    const authProviders = new Set(AUTH_PROVIDERS);
    Object.keys(this.modalConfig.connectors[WALLET_CONNECTORS.AUTH].loginMethods).forEach((key) => {
      const userConfig = this.modalConfig.connectors[WALLET_CONNECTORS.AUTH].loginMethods[key as AUTH_CONNECTION_TYPE];
      const { authConnectionId, groupedAuthConnectionId } = userConfig;
      if (!authProviders.has(key as AUTH_CONNECTION_TYPE)) {
        throw WalletInitializationError.invalidParams(`Invalid auth connection: ${key}`);
      }

      // only throw error if one of them is defined in the config.
      if (groupedAuthConnectionId || authConnectionId) {
        if (!embedWalletConfigMap.has(groupedAuthConnectionId || authConnectionId))
          throw WalletInitializationError.invalidParams(
            `Invalid auth connection config, authConnection: ${key}. Missing AuthConnectionConfig from the dashboard.`
          );

        const configFromDashboard = embedWalletConfigMap.get(groupedAuthConnectionId || authConnectionId);
        this.modalConfig.connectors[WALLET_CONNECTORS.AUTH].loginMethods[key as AUTH_CONNECTION_TYPE] = {
          authConnection: configFromDashboard.authConnection,
          authConnectionId: configFromDashboard.authConnectionId,
          groupedAuthConnectionId: configFromDashboard.groupedAuthConnectionId,
          isDefault: configFromDashboard.isDefault || false,
          extraLoginOptions: {
            ...configFromDashboard.jwtParameters,
            ...userConfig.extraLoginOptions,
          },
        };
      }
    });

    this.modalConfig.connectors = deepmerge(dashboardConnectorConfig, cloneDeep(this.modalConfig.connectors || {}));

    // merge default connectors with the custom configured connectors.
    const allConnectorNames = [
      ...new Set([...Object.keys(this.modalConfig.connectors || {}), ...this.connectors.map((connector) => connector.name)]),
    ] as WALLET_CONNECTOR_TYPE[];

    const connectorNames = allConnectorNames.map((connectorName: WALLET_CONNECTOR_TYPE) => {
      // start with the default config of connector.
      const defaultConnectorConfig = {
        label: CONNECTOR_NAMES[connectorName] || connectorName.split("-").map(capitalizeFirstLetter).join(" "),
        showOnModal: true,
      };

      this.modalConfig.connectors[connectorName] = {
        ...defaultConnectorConfig,
        ...(this.modalConfig?.connectors?.[connectorName] || {}),
      };

      // check if connector is configured/added by user and exist in connectors map.
      const connector = this.getConnector(connectorName);
      log.debug("connector config", connectorName, this.modalConfig.connectors?.[connectorName]?.showOnModal, connector);

      // check if connector is configured/added by user and exist in connectors map.
      const connectorConfig = this.modalConfig.connectors?.[connectorName];
      if (!connector) {
        if (connectorConfig.showOnModal) throw WalletInitializationError.invalidParams(`Connector ${connectorName} is not configured`);
        return;
      }

      // skip connector if it is hidden by user
      if (!connectorConfig.showOnModal) return;

      // skip external connector if external wallets are disabled except for MetaMask
      const isExternalWalletEnabled = Boolean(projectConfig.externalWalletAuth);
      if (connector.type === CONNECTOR_CATEGORY.EXTERNAL && connector.name !== WALLET_CONNECTORS.METAMASK) {
        if (!isExternalWalletEnabled) return;
        if (disabledExternalWallets.has(connectorName)) return;
      }

      // skip WC connector if external wallets are disabled or hideWalletDiscovery is true
      if (connectorName === WALLET_CONNECTORS.WALLET_CONNECT_V2) {
        if (!isExternalWalletEnabled) return;
        if (this.modalConfig?.hideWalletDiscovery) return;
      }

      this.modalConfig.connectors[connectorName] = connectorConfig;
      return connectorName;
    });
    // const connectorNames = await Promise.all(connectorConfigurationPromises);
    return connectorNames.filter((name) => name !== undefined);
  }

  private async checkConnectorAvailability(
    connectorNames: WALLET_CONNECTOR_TYPE[]
  ): Promise<{ hasInAppConnectors: boolean; hasExternalConnectors: boolean }> {
    // currently all default in app and external wallets can be hidden or shown based on config.
    // check if in app connectors are available
    const hasInAppConnectors = this.connectors.some((connector) => {
      if (connector.type !== CONNECTOR_CATEGORY.IN_APP) return false;
      if (this.modalConfig.connectors?.[connector.name as WALLET_CONNECTOR_TYPE]?.showOnModal !== true) return false;
      if (!this.modalConfig.connectors?.[connector.name as WALLET_CONNECTOR_TYPE]?.loginMethods) return true;
      if (Object.values(this.modalConfig.connectors[connector.name as WALLET_CONNECTOR_TYPE].loginMethods).some((method) => method.showOnModal))
        return true;
      return false;
    });
    log.debug(hasInAppConnectors, this.connectors, connectorNames, "hasInAppWallets");

    // check if external connectors are available
    const hasExternalConnectors = connectorNames.some((connectorName) => {
      if (connectorName === WALLET_CONNECTORS.WALLET_CONNECT_V2) return true;
      return (
        this.getConnector(connectorName)?.type === CONNECTOR_CATEGORY.EXTERNAL &&
        this.modalConfig.connectors?.[connectorName as WALLET_CONNECTOR_TYPE]?.showOnModal
      );
    });
    return { hasInAppConnectors, hasExternalConnectors };
  }

  private async initInAppAndCachedConnectors(connectors: IConnector<unknown>[]) {
    await Promise.all(
      connectors.map(async (connector) => {
        const connectorName = connector.name as WALLET_CONNECTOR_TYPE;
        try {
          // skip if connector is already initialized
          if (connector.status !== CONNECTOR_STATUS.NOT_READY) return;

          // only initialize a external connectors here if it is a cached connector.
          if (this.cachedConnector !== connectorName && connector.type === CONNECTOR_CATEGORY.EXTERNAL) return;

          // in-app wallets or cached wallet (being connected or already connected) are initialized first.
          // if connector is configured then only initialize in app or cached connector.
          // external wallets are initialized on INIT_EXTERNAL_WALLET event.
          this.subscribeToConnectorEvents(connector);
          const initialChain = this.getInitialChainIdForConnector(connector);
          const autoConnect = super.checkIfAutoConnect(connector);
          await connector.init({ autoConnect, chainId: initialChain.chainId });

          // note: not adding cachedWallet to modal if it is external wallet.
          // adding it later if no in-app wallets are available.
          if (connector.type === CONNECTOR_CATEGORY.IN_APP) {
            log.info("connectorInitResults", connectorName);
            const loginMethods = this.modalConfig.connectors[connectorName]?.loginMethods || {};
            this.loginModal.addSocialLogins(connectorName, loginMethods, this.options.uiConfig?.loginMethodsOrder || AUTH_PROVIDERS, {
              ...this.options.uiConfig,
              loginGridCol: this.options.uiConfig?.loginGridCol || 3,
              primaryButton: this.options.uiConfig?.primaryButton || "socialLogin",
            });
          }
        } catch (error) {
          log.error(error, "error while initializing connector ", connectorName);
        }
      })
    );
  }

  private async initExternalConnectors(
    externalConnectors: IConnector<unknown>[],
    options: { externalWalletsInitialized: boolean; showExternalWalletsOnly?: boolean; externalWalletsVisibility?: boolean }
  ): Promise<void> {
    const connectorsConfig: Record<string, BaseConnectorConfig> = {};
    const connectorChainNamespaceMap: Record<string, Set<ChainNamespaceType>> = {};

    // we do it like this because we don't want one slow connector to delay the load of the entire external wallet section.
    externalConnectors.forEach(async (connector) => {
      const connectorName = connector.name as WALLET_CONNECTOR_TYPE;
      log.debug("init external wallet", this.cachedConnector, connectorName, connector.status);

      // a wallet can support multiple chain namespaces e.g. Phantom has EvmInjected connector and WalletStandard connector.
      if (!connectorChainNamespaceMap[connectorName]) connectorChainNamespaceMap[connectorName] = new Set();
      if (connector.connectorNamespace === CONNECTOR_NAMESPACES.MULTICHAIN) {
        this.getChainNamespaces().forEach((x) => connectorChainNamespaceMap[connectorName].add(x));
      } else {
        connectorChainNamespaceMap[connectorName].add(connector.connectorNamespace as ChainNamespaceType);
      }

      // initialize connectors
      // skip initializing cached connector here as it is already being initialized in initModal before.
      if (connector.status === CONNECTOR_STATUS.NOT_READY && this.cachedConnector !== connectorName) {
        try {
          this.subscribeToConnectorEvents(connector);
          const initialChain = this.getInitialChainIdForConnector(connector);
          await connector.init({ autoConnect: this.cachedConnector === connectorName, chainId: initialChain.chainId });
        } catch (error) {
          log.error(error, "error while initializing connector", connectorName);
        }
      }

      // update connector config
      if (([CONNECTOR_STATUS.NOT_READY, CONNECTOR_STATUS.READY, CONNECTOR_STATUS.CONNECTING] as string[]).includes(connector.status)) {
        const connectorModalConfig = this.modalConfig.connectors[connectorName];
        connectorsConfig[connectorName] = {
          ...connectorModalConfig,
          isInjected: connector.isInjected,
          icon: connector.icon,
          chainNamespaces: Array.from(connectorChainNamespaceMap[connectorName]),
        };
        this.loginModal.addWalletLogins(connectorsConfig, {
          showExternalWalletsOnly: !!options.showExternalWalletsOnly,
          externalWalletsVisibility: !!options.externalWalletsVisibility,
          externalWalletsInitialized: !!options.externalWalletsInitialized,
        });
      }
    });
  }

  private onInitExternalWallets = async (params: { externalWalletsInitialized: boolean }): Promise<void> => {
    if (params.externalWalletsInitialized) return;
    // initialize WC connector only as other external wallets are initialized in initModal
    await this.initExternalConnectors(
      this.connectors.filter((x) => x.name === WALLET_CONNECTORS.WALLET_CONNECT_V2),
      { externalWalletsInitialized: true, externalWalletsVisibility: true }
    );
  };

  private onSocialLogin = async (params: { connector: WALLET_CONNECTOR_TYPE; loginParams: AuthLoginParams }): Promise<void> => {
    try {
      await this.connectTo(WALLET_CONNECTORS.AUTH, params.loginParams, LOGIN_MODE.MODAL);
    } catch (error) {
      log.error(`Error while connecting to connector: ${params.connector}`, error);
    }
  };

  private onExternalWalletLogin = async (params: {
    connector: WALLET_CONNECTOR_TYPE | string;
    loginParams: { chainNamespace: ChainNamespaceType };
  }): Promise<void> => {
    try {
      const connector = this.getConnector(params.connector as WALLET_CONNECTOR_TYPE, params.loginParams?.chainNamespace);
      // auto-connect WalletConnect and non-injected MetaMask in background to generate QR code URI without interfering with user's selected connection
      const shouldStartConnectionInBackground =
        connector.name === WALLET_CONNECTORS.WALLET_CONNECT_V2 || (connector.name === WALLET_CONNECTORS.METAMASK && !connector.isInjected);
      if (shouldStartConnectionInBackground) {
        const initialChain = this.getInitialChainIdForConnector(connector);
        await connector.connect({ chainId: initialChain.chainId });
      } else {
        await this.connectTo(params.connector as WALLET_CONNECTOR_TYPE, params.loginParams, LOGIN_MODE.MODAL);
      }
    } catch (error) {
      log.error(`Error while connecting to connector: ${params.connector}`, error);
    }
  };

  private onModalVisibility = async (visibility: boolean): Promise<void> => {
    log.debug("is login modal visible", visibility);
    this.emit(LOGIN_MODAL_EVENTS.MODAL_VISIBILITY, visibility);

    // handle WC session refresh
    const wcConnector = this.getConnector(WALLET_CONNECTORS.WALLET_CONNECT_V2);
    if (wcConnector) {
      const walletConnectStatus = wcConnector?.status;
      log.debug("trying refreshing wc session", visibility, walletConnectStatus);
      if (visibility && (walletConnectStatus === CONNECTOR_STATUS.READY || walletConnectStatus === CONNECTOR_STATUS.CONNECTING)) {
        log.debug("refreshing wc session");

        // refreshing session for wallet connect whenever modal is opened.
        try {
          const initialChain = this.getInitialChainIdForConnector(wcConnector);
          wcConnector.connect({ chainId: initialChain.chainId });
        } catch (error) {
          log.error(`Error while disconnecting to wallet connect in core`, error);
        }
      }
      if (
        !visibility &&
        this.status === CONNECTOR_STATUS.CONNECTED &&
        (walletConnectStatus === CONNECTOR_STATUS.READY || walletConnectStatus === CONNECTOR_STATUS.CONNECTING)
      ) {
        log.debug("this stops wc connector from trying to reconnect once proposal expires");
        wcConnector.status = CONNECTOR_STATUS.READY;
      }
    }

    // handle MM session refresh if MM is not injected
    const metamaskConnector = this.getConnector(WALLET_CONNECTORS.METAMASK);
    if (metamaskConnector && !metamaskConnector.isInjected) {
      const status = metamaskConnector?.status;
      log.debug("trying refreshing MM session", visibility, status);
      if (visibility && (status === CONNECTOR_STATUS.READY || status === CONNECTOR_STATUS.CONNECTING)) {
        log.debug("refreshing MM session");

        // refreshing session for MM whenever modal is opened.
        try {
          const initialChain = this.getInitialChainIdForConnector(metamaskConnector);
          metamaskConnector.connect({ chainId: initialChain.chainId });
        } catch (error) {
          log.error(`Error while connecting to MM`, error);
        }
      }
      if (
        !visibility &&
        this.status === CONNECTOR_STATUS.CONNECTED &&
        (status === CONNECTOR_STATUS.READY || status === CONNECTOR_STATUS.CONNECTING)
      ) {
        log.debug("this stops MM connector from trying to reconnect once proposal expires");
        metamaskConnector.status = CONNECTOR_STATUS.READY;
      }
    }
  };

  private getChainNamespaces = (): ChainNamespaceType[] => {
    return [...new Set(this.coreOptions.chains?.map((x) => x.chainNamespace) || [])];
  };
}



================================================
FILE: packages/modal/src/utils.ts
================================================
import { type UIConfig } from "./ui";

export const getLoginModalAnalyticsProperties = (uiConfig?: UIConfig) => {
  return {
    ui_modal_login_methods_order: uiConfig?.loginMethodsOrder,
    ui_modal_z_index: uiConfig?.modalZIndex,
    ui_modal_display_errors_on_modal: uiConfig?.displayErrorsOnModal,
    ui_modal_login_grid_col: uiConfig?.loginGridCol,
    ui_modal_primary_button: uiConfig?.primaryButton,
    ui_modal_widget_type: uiConfig?.widgetType,
    ui_modal_target_id_used: Boolean(uiConfig?.targetId),
    ui_modal_logo_alignment: uiConfig?.logoAlignment,
    ui_modal_border_radius_type: uiConfig?.borderRadiusType,
    ui_modal_button_radius_type: uiConfig?.buttonRadiusType,
    ui_modal_sign_in_methods: uiConfig?.signInMethods,
    ui_modal_add_previous_login_hint: uiConfig?.addPreviousLoginHint,
    ui_modal_display_installed_external_wallets: uiConfig?.displayInstalledExternalWallets,
    ui_modal_display_external_wallets_count: uiConfig?.displayExternalWalletsCount,
  };
};



================================================
FILE: packages/modal/src/connectors/coinbase-connector/index.ts
================================================
export * from "@web3auth/no-modal/connectors/coinbase-connector";



================================================
FILE: packages/modal/src/providers/ethereum-mpc-provider/index.ts
================================================
export * from "@web3auth/no-modal/providers/ethereum-mpc-provider";



================================================
FILE: packages/modal/src/providers/xrpl-provider/index.ts
================================================
export * from "@web3auth/no-modal/providers/xrpl-provider";



================================================
FILE: packages/modal/src/react/index.ts
================================================
export * from "./hooks";
export * from "./interfaces";
export * from "./Web3AuthProvider";



================================================
FILE: packages/modal/src/react/interfaces.ts
================================================
import type { IBaseWeb3AuthHookContext, IWeb3AuthState, WalletServicesPluginType } from "@web3auth/no-modal";

import type { Web3Auth, Web3AuthOptions } from "../modalManager";

export type Web3AuthContextConfig = {
  web3AuthOptions: Web3AuthOptions;
};

export interface Web3AuthProviderProps {
  config: Web3AuthContextConfig;
  initialState?: IWeb3AuthState;
}

export interface IWeb3AuthInnerContext extends IBaseWeb3AuthHookContext {
  web3Auth: Web3Auth | null;
}
export interface IWalletServicesContext {
  ready: boolean;
  connecting: boolean;
  plugin: WalletServicesPluginType | null;
}

export type IWeb3AuthContext = IWeb3AuthInnerContext;



================================================
FILE: packages/modal/src/react/Web3AuthProvider.ts
================================================
import { createElement, PropsWithChildren } from "react";

import { WalletServicesContextProvider } from "./context/WalletServicesInnerContext";
import { Web3AuthInnerContext, Web3AuthInnerProvider } from "./context/Web3AuthInnerContext";
import { Web3AuthProviderProps } from "./interfaces";

export function Web3AuthProvider({ config, initialState, children }: PropsWithChildren<Web3AuthProviderProps>) {
  const pluginChild = createElement(WalletServicesContextProvider, { context: Web3AuthInnerContext }, children);
  return createElement(Web3AuthInnerProvider, { config, initialState }, pluginChild);
}



================================================
FILE: packages/modal/src/react/context/WalletServicesInnerContext.ts
================================================
import { CONNECTOR_STATUS, EVM_PLUGINS, PLUGIN_EVENTS } from "@web3auth/no-modal";
import { type WalletServicesPluginType } from "@web3auth/no-modal";
import { Context, createContext, createElement, PropsWithChildren, useContext, useEffect, useMemo, useState } from "react";

import { IWalletServicesContext, IWeb3AuthInnerContext } from "../interfaces";

export const WalletServicesContext = createContext<IWalletServicesContext>(null);

export function WalletServicesContextProvider({ children, context }: PropsWithChildren<{ context: Context<IWeb3AuthInnerContext> }>) {
  const web3AuthContext = useContext(context);
  const { getPlugin, isInitialized, isConnected } = web3AuthContext;

  const [ready, setReady] = useState<boolean>(false);
  const [connecting, setConnecting] = useState<boolean>(false);
  const [walletServicesPlugin, setWalletServicesPlugin] = useState<WalletServicesPluginType>(null);

  useEffect(() => {
    if (isInitialized) {
      const plugin = getPlugin(EVM_PLUGINS.WALLET_SERVICES) as WalletServicesPluginType;
      setWalletServicesPlugin(plugin);
    }
  }, [isInitialized, getPlugin]);

  useEffect(() => {
    if (isConnected) {
      const plugin = getPlugin(EVM_PLUGINS.WALLET_SERVICES) as WalletServicesPluginType;
      setWalletServicesPlugin(plugin);
      // when rehydrating, the connectedListener may be registered after the connected event is emitted, we need to check the status here
      if (plugin?.status === CONNECTOR_STATUS.CONNECTED) setReady(true);
    }
  }, [isConnected, getPlugin, walletServicesPlugin]);

  useEffect(() => {
    const connectedListener = () => {
      setReady(true);
      setConnecting(false);
    };

    const disconnectedListener = () => {
      setReady(false);
      setConnecting(false);
    };

    const connectingListener = () => {
      setConnecting(true);
    };

    if (walletServicesPlugin) {
      walletServicesPlugin.on(PLUGIN_EVENTS.CONNECTED, connectedListener);
      walletServicesPlugin.on(PLUGIN_EVENTS.DISCONNECTED, disconnectedListener);
      walletServicesPlugin.on(PLUGIN_EVENTS.CONNECTING, connectingListener);
    }

    return () => {
      if (walletServicesPlugin) {
        walletServicesPlugin.off(PLUGIN_EVENTS.CONNECTED, connectedListener);
        walletServicesPlugin.off(PLUGIN_EVENTS.DISCONNECTED, disconnectedListener);
        walletServicesPlugin.off(PLUGIN_EVENTS.CONNECTING, connectingListener);
      }
    };
  }, [walletServicesPlugin]);

  const value = useMemo(() => {
    return {
      plugin: walletServicesPlugin,
      ready,
      connecting,
    };
  }, [walletServicesPlugin, ready, connecting]);

  return createElement(WalletServicesContext.Provider, { value }, children);
}



================================================
FILE: packages/modal/src/react/context/Web3AuthInnerContext.ts
================================================
import {
  ANALYTICS_INTEGRATION_TYPE,
  type CONNECTED_EVENT_DATA,
  CONNECTOR_EVENTS,
  CONNECTOR_STATUS,
  type CONNECTOR_STATUS_TYPE,
  type IProvider,
  WalletInitializationError,
} from "@web3auth/no-modal";
import { createContext, createElement, PropsWithChildren, useCallback, useEffect, useMemo, useState } from "react";

import { Web3Auth } from "../../modalManager";
import { IWeb3AuthInnerContext, Web3AuthProviderProps } from "../interfaces";

export const Web3AuthInnerContext = createContext<IWeb3AuthInnerContext>(null);

export function Web3AuthInnerProvider(params: PropsWithChildren<Web3AuthProviderProps>) {
  const { children, config, initialState } = params;
  const { web3AuthOptions } = config;

  const [isInitializing, setIsInitializing] = useState<boolean>(false);
  const [initError, setInitError] = useState<Error | null>(null);
  const [provider, setProvider] = useState<IProvider | null>(null);
  const [isInitialized, setIsInitialized] = useState<boolean>(false);
  const [isMFAEnabled, setIsMFAEnabled] = useState<boolean>(false);

  const web3Auth = useMemo(() => {
    setProvider(null);

    return new Web3Auth(web3AuthOptions, initialState);
  }, [web3AuthOptions, initialState]);

  const [isConnected, setIsConnected] = useState<boolean>(web3Auth.status === CONNECTOR_STATUS.CONNECTED);
  const [status, setStatus] = useState<CONNECTOR_STATUS_TYPE | null>(web3Auth.status);

  const getPlugin = useCallback(
    (name: string) => {
      if (!web3Auth) throw WalletInitializationError.notReady();
      return web3Auth.getPlugin(name);
    },
    [web3Auth]
  );

  useEffect(() => {
    const controller = new AbortController();
    async function init() {
      try {
        setInitError(null);
        setIsInitializing(true);
        web3Auth.setAnalyticsProperties({ integration_type: ANALYTICS_INTEGRATION_TYPE.REACT_HOOKS });
        await web3Auth.init({ signal: controller.signal });
      } catch (error) {
        setInitError(error as Error);
      } finally {
        setIsInitializing(false);
      }
    }

    if (web3Auth) init();

    return () => {
      controller.abort();
    };
  }, [web3Auth, config]);

  useEffect(() => {
    const notReadyListener = () => setStatus(web3Auth.status);
    const readyListener = () => {
      setStatus(web3Auth.status);
      setIsInitialized(true);
    };
    const connectedListener = (data: CONNECTED_EVENT_DATA) => {
      setStatus(web3Auth.status);
      // we do this because of rehydration issues. status connected is fired first but web3auth sdk is not ready yet.
      if (web3Auth.status === CONNECTOR_STATUS.CONNECTED) {
        setIsInitialized(true);
        setIsConnected(true);
        setProvider(data.provider);
      }
    };
    const disconnectedListener = () => {
      setStatus(web3Auth.status);
      setIsConnected(false);
      setProvider(null);
    };
    const connectingListener = () => {
      setStatus(web3Auth.status);
    };
    const errorListener = () => {
      setStatus(web3Auth.status);
    };

    const rehydrationErrorListener = () => {
      setStatus(web3Auth.status);
      setIsConnected(false);
      setProvider(null);
    };

    const mfaEnabledListener = (isMFAEnabled: boolean) => {
      if (typeof isMFAEnabled === "boolean") setIsMFAEnabled(isMFAEnabled);
    };

    if (web3Auth) {
      // web3Auth is initialized here.
      setStatus(web3Auth.status);
      web3Auth.on(CONNECTOR_EVENTS.NOT_READY, notReadyListener);
      web3Auth.on(CONNECTOR_EVENTS.READY, readyListener);
      web3Auth.on(CONNECTOR_EVENTS.CONNECTED, connectedListener);
      web3Auth.on(CONNECTOR_EVENTS.DISCONNECTED, disconnectedListener);
      web3Auth.on(CONNECTOR_EVENTS.CONNECTING, connectingListener);
      web3Auth.on(CONNECTOR_EVENTS.ERRORED, errorListener);
      web3Auth.on(CONNECTOR_EVENTS.REHYDRATION_ERROR, rehydrationErrorListener);
      web3Auth.on(CONNECTOR_EVENTS.MFA_ENABLED, mfaEnabledListener);
    }

    return () => {
      if (web3Auth) {
        web3Auth.off(CONNECTOR_EVENTS.NOT_READY, notReadyListener);
        web3Auth.off(CONNECTOR_EVENTS.READY, readyListener);
        web3Auth.off(CONNECTOR_EVENTS.CONNECTED, connectedListener);
        web3Auth.off(CONNECTOR_EVENTS.DISCONNECTED, disconnectedListener);
        web3Auth.off(CONNECTOR_EVENTS.CONNECTING, connectingListener);
        web3Auth.off(CONNECTOR_EVENTS.ERRORED, errorListener);
        web3Auth.off(CONNECTOR_EVENTS.REHYDRATION_ERROR, rehydrationErrorListener);
        web3Auth.off(CONNECTOR_EVENTS.MFA_ENABLED, mfaEnabledListener);

        web3Auth.cleanup();
      }
    };
  }, [web3Auth]);

  const value = useMemo(() => {
    return {
      web3Auth,
      isConnected,
      isInitialized,
      provider,
      status,
      isInitializing,
      initError,
      isMFAEnabled,
      getPlugin,
      setIsMFAEnabled,
    };
  }, [web3Auth, isConnected, isMFAEnabled, setIsMFAEnabled, isInitialized, provider, status, getPlugin, isInitializing, initError]);

  return createElement(Web3AuthInnerContext.Provider, { value }, children);
}



================================================
FILE: packages/modal/src/react/hooks/index.ts
================================================
export * from "./useCheckout";
export * from "./useEnableMFA";
export * from "./useIdentityToken";
export * from "./useManageMFA";
export * from "./useSwap";
export * from "./useSwitchChain";
export * from "./useWalletConnectScanner";
export * from "./useWalletServicesPlugin";
export * from "./useWalletUI";
export * from "./useWeb3Auth";
export * from "./useWeb3AuthConnect";
export * from "./useWeb3AuthDisconnect";
export * from "./useWeb3AuthUser";



================================================
FILE: packages/modal/src/react/hooks/useCheckout.ts
================================================
import { BaseEmbedControllerState } from "@toruslabs/base-controllers";
import { WalletServicesPluginError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWalletServicesPlugin } from "./useWalletServicesPlugin";

export interface IUseCheckout {
  loading: boolean;
  error: Web3AuthError | null;
  showCheckout: (showCheckoutParams?: BaseEmbedControllerState["showCheckout"]) => Promise<void>;
}

export const useCheckout = (): IUseCheckout => {
  const { plugin, ready } = useWalletServicesPlugin();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const showCheckout = useCallback(
    async (showCheckoutParams?: BaseEmbedControllerState["showCheckout"]) => {
      setLoading(true);
      setError(null);
      try {
        if (!plugin) throw WalletServicesPluginError.notInitialized();
        if (!ready) throw WalletServicesPluginError.walletPluginNotConnected();

        await plugin.showCheckout(showCheckoutParams);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [plugin, ready]
  );

  return { loading, error, showCheckout };
};



================================================
FILE: packages/modal/src/react/hooks/useEnableMFA.ts
================================================
import { Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWeb3AuthInner } from "./useWeb3AuthInner";

export interface IUseEnableMFA {
  loading: boolean;
  error: Web3AuthError | null;
  enableMFA<T>(params?: T): Promise<void>;
}

export const useEnableMFA = (): IUseEnableMFA => {
  const { web3Auth } = useWeb3AuthInner();

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const enableMFA = useCallback(
    async <T>(params: T) => {
      setLoading(true);
      setError(null);
      try {
        await web3Auth.enableMFA(params);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [web3Auth]
  );

  return { loading, error, enableMFA };
};



================================================
FILE: packages/modal/src/react/hooks/useIdentityToken.ts
================================================
import { Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useEffect, useState } from "react";

import { useWeb3AuthInner } from "./useWeb3AuthInner";

export interface IUseIdentityToken {
  loading: boolean;
  error: Web3AuthError | null;
  token: string | null;
  getIdentityToken: () => Promise<string | null>;
}

export const useIdentityToken = () => {
  const { web3Auth, isConnected } = useWeb3AuthInner();

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);
  const [token, setToken] = useState<string | null>(null);

  const getIdentityToken = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const userAuthInfo = await web3Auth.getIdentityToken();
      if (userAuthInfo?.idToken) {
        setToken(userAuthInfo.idToken);
      }
      return userAuthInfo?.idToken;
    } catch (error) {
      setError(error as Web3AuthError);
    } finally {
      setLoading(false);
    }
  }, [web3Auth]);

  useEffect(() => {
    if (!isConnected && token) {
      setToken(null);
    }
  }, [isConnected, token]);

  return { loading, error, token, getIdentityToken };
};



================================================
FILE: packages/modal/src/react/hooks/useManageMFA.ts
================================================
import { Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWeb3AuthInner } from "./useWeb3AuthInner";

export interface IUseManageMFA {
  loading: boolean;
  error: Web3AuthError | null;
  manageMFA<T>(params?: T): Promise<void>;
}

export const useManageMFA = (): IUseManageMFA => {
  const { web3Auth } = useWeb3AuthInner();

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const manageMFA = useCallback(
    async <T>(params: T) => {
      setLoading(true);
      setError(null);
      try {
        await web3Auth.manageMFA(params);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [web3Auth]
  );

  return { loading, error, manageMFA };
};



================================================
FILE: packages/modal/src/react/hooks/useSwap.ts
================================================
import { BaseEmbedControllerState } from "@toruslabs/base-controllers";
import { WalletServicesPluginError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWalletServicesPlugin } from "./useWalletServicesPlugin";

export interface IUseSwap {
  loading: boolean;
  error: Web3AuthError | null;
  showSwap: (showSwapParams?: BaseEmbedControllerState["showSwap"]) => Promise<void>;
}

export const useSwap = (): IUseSwap => {
  const { plugin, ready } = useWalletServicesPlugin();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const showSwap = useCallback(
    async (showSwapParams?: BaseEmbedControllerState["showSwap"]) => {
      setLoading(true);
      setError(null);
      try {
        if (!plugin) throw WalletServicesPluginError.notInitialized();
        if (!ready) throw WalletServicesPluginError.walletPluginNotConnected();

        await plugin.showSwap(showSwapParams);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [plugin, ready]
  );

  return { loading, error, showSwap };
};



================================================
FILE: packages/modal/src/react/hooks/useSwitchChain.ts
================================================
import { Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWeb3AuthInner } from "../hooks/useWeb3AuthInner";

export interface IUseSwitchChain {
  loading: boolean;
  error: Web3AuthError | null;
  switchChain: (chainId: string) => Promise<void>;
}

export const useSwitchChain = (): IUseSwitchChain => {
  const { web3Auth } = useWeb3AuthInner();

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const switchChain = useCallback(
    async (chainId: string) => {
      setLoading(true);
      setError(null);
      try {
        await web3Auth.switchChain({ chainId });
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [web3Auth]
  );

  return { loading, error, switchChain };
};



================================================
FILE: packages/modal/src/react/hooks/useWalletConnectScanner.ts
================================================
import { BaseEmbedControllerState } from "@toruslabs/base-controllers";
import { WalletServicesPluginError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWalletServicesPlugin } from "./useWalletServicesPlugin";

export interface IUseWalletConnectScanner {
  loading: boolean;
  error: Web3AuthError | null;
  showWalletConnectScanner: (showWalletConnectScannerParams?: BaseEmbedControllerState["showWalletConnect"]) => Promise<void>;
}

export const useWalletConnectScanner = (): IUseWalletConnectScanner => {
  const { plugin, ready } = useWalletServicesPlugin();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const showWalletConnectScanner = useCallback(
    async (showWalletConnectScannerParams?: BaseEmbedControllerState["showWalletConnect"]) => {
      setLoading(true);
      setError(null);
      try {
        if (!plugin) throw WalletServicesPluginError.notInitialized();
        if (!ready) throw WalletServicesPluginError.walletPluginNotConnected();

        await plugin.showWalletConnectScanner(showWalletConnectScannerParams);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [plugin, ready]
  );

  return { loading, error, showWalletConnectScanner };
};



================================================
FILE: packages/modal/src/react/hooks/useWalletServicesPlugin.ts
================================================
import { WalletInitializationError } from "@web3auth/no-modal";
import { useContext } from "react";

import { WalletServicesContext } from "../context/WalletServicesInnerContext";
import { IWalletServicesContext } from "../interfaces";

export const useWalletServicesPlugin = (): IWalletServicesContext => {
  const context = useContext(WalletServicesContext);
  if (!context) throw WalletInitializationError.fromCode(1000, "usage of useWalletServicesPlugin not wrapped in `WalletServicesContextProvider`.");
  return context;
};



================================================
FILE: packages/modal/src/react/hooks/useWalletUI.ts
================================================
import { BaseEmbedControllerState } from "@toruslabs/base-controllers";
import { WalletServicesPluginError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWalletServicesPlugin } from "./useWalletServicesPlugin";

export interface IUseWalletUI {
  loading: boolean;
  error: Web3AuthError | null;
  showWalletUI: (showWalletUiParams?: BaseEmbedControllerState["showWalletUi"]) => Promise<void>;
}

export const useWalletUI = (): IUseWalletUI => {
  const { plugin, ready } = useWalletServicesPlugin();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const showWalletUI = useCallback(
    async (showWalletUiParams?: BaseEmbedControllerState["showWalletUi"]) => {
      setLoading(true);
      setError(null);
      try {
        if (!plugin) throw WalletServicesPluginError.notInitialized();
        if (!ready) throw WalletServicesPluginError.walletPluginNotConnected();

        await plugin.showWalletUi(showWalletUiParams);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [plugin, ready]
  );

  return { loading, error, showWalletUI };
};



================================================
FILE: packages/modal/src/react/hooks/useWeb3Auth.ts
================================================
import { IWeb3AuthInnerContext } from "../interfaces";
import { useWeb3AuthInner } from "./useWeb3AuthInner";

export type IUseWeb3Auth = Omit<IWeb3AuthInnerContext, "isMFAEnabled" | "setIsMFAEnabled">;

export const useWeb3Auth = (): IUseWeb3Auth => {
  const { initError, isConnected, isInitialized, isInitializing, provider, status, web3Auth, getPlugin } = useWeb3AuthInner();
  return {
    initError,
    isConnected,
    isInitialized,
    isInitializing,
    provider,
    status,
    web3Auth,
    getPlugin,
  };
};



================================================
FILE: packages/modal/src/react/hooks/useWeb3AuthConnect.ts
================================================
import type { IProvider, LoginParamMap, WALLET_CONNECTOR_TYPE, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useEffect, useState } from "react";

import { useWeb3AuthInner } from "../hooks/useWeb3AuthInner";

export interface IUseWeb3AuthConnect {
  isConnected: boolean;
  loading: boolean;
  error: Web3AuthError | null;
  connectorName: WALLET_CONNECTOR_TYPE | null;
  connect(): Promise<IProvider | null>;
  connectTo<T extends WALLET_CONNECTOR_TYPE>(connector: T, params?: LoginParamMap[T]): Promise<IProvider | null>;
}

export const useWeb3AuthConnect = (): IUseWeb3AuthConnect => {
  const { web3Auth, isConnected } = useWeb3AuthInner();

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);
  const [connectorName, setConnectorName] = useState<WALLET_CONNECTOR_TYPE | null>(null);

  useEffect(() => {
    if (!web3Auth) return;
    if (!isConnected && connectorName) {
      setConnectorName(null);
    }
    if (isConnected && !connectorName) {
      setConnectorName(web3Auth.connectedConnectorName);
    }
  }, [isConnected, connectorName, web3Auth]);

  const connect = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const provider = await web3Auth.connect();
      if (provider) {
        setConnectorName(web3Auth.connectedConnectorName);
      }
      return provider;
    } catch (error) {
      setError(error as Web3AuthError);
    } finally {
      setLoading(false);
    }
  }, [web3Auth]);

  const connectTo = useCallback(
    async <T extends WALLET_CONNECTOR_TYPE>(connector: T, params?: LoginParamMap[T]) => {
      setLoading(true);
      setError(null);
      try {
        const provider = await web3Auth.connectTo(connector, params);
        if (provider) {
          setConnectorName(web3Auth.connectedConnectorName);
        }
        return provider;
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [web3Auth]
  );

  return {
    isConnected,
    loading,
    error,
    connectorName,
    connect,
    connectTo,
  };
};



================================================
FILE: packages/modal/src/react/hooks/useWeb3AuthDisconnect.ts
================================================
import { Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useWeb3AuthInner } from "./useWeb3AuthInner";

export interface IUseWeb3AuthDisconnect {
  loading: boolean;
  error: Web3AuthError | null;
  disconnect(options?: { cleanup: boolean }): Promise<void>;
}

export const useWeb3AuthDisconnect = (): IUseWeb3AuthDisconnect => {
  const { web3Auth } = useWeb3AuthInner();

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const disconnect = useCallback(
    async (options?: { cleanup: boolean }) => {
      setLoading(true);
      setError(null);
      try {
        await web3Auth.logout(options);
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [web3Auth]
  );

  return { loading, error, disconnect };
};



================================================
FILE: packages/modal/src/react/hooks/useWeb3AuthInner.ts
================================================
import { WalletInitializationError } from "@web3auth/no-modal";
import { useContext } from "react";

import { Web3AuthInnerContext } from "../context/Web3AuthInnerContext";
import { IWeb3AuthInnerContext } from "../interfaces";

export const useWeb3AuthInner = (): IWeb3AuthInnerContext => {
  const context = useContext(Web3AuthInnerContext);
  if (!context) {
    throw WalletInitializationError.fromCode(1000, "usage of useWeb3Auth not wrapped in `Web3AuthContextProvider`.");
  }
  return context;
};



================================================
FILE: packages/modal/src/react/hooks/useWeb3AuthUser.ts
================================================
import { type UserInfo, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useEffect, useState } from "react";

import { useWeb3AuthInner } from "./useWeb3AuthInner";

export interface IUseWeb3AuthUser {
  loading: boolean;
  error: Web3AuthError | null;
  userInfo: Partial<UserInfo> | null;
  isMFAEnabled: boolean;
  getUserInfo: () => Promise<Partial<UserInfo> | null>;
}

export const useWeb3AuthUser = (): IUseWeb3AuthUser => {
  const { web3Auth, isConnected, isMFAEnabled, setIsMFAEnabled } = useWeb3AuthInner();

  const [userInfo, setUserInfo] = useState<Partial<UserInfo> | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);

  const getUserInfo = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const userInfo = await web3Auth.getUserInfo();
      setUserInfo(userInfo);
      return userInfo;
    } catch (error) {
      setError(error as Web3AuthError);
    } finally {
      setLoading(false);
    }
  }, [web3Auth]);

  useEffect(() => {
    const saveUserInfo = async () => {
      const userInfo = await getUserInfo();
      setUserInfo(userInfo);
      setIsMFAEnabled(userInfo?.isMfaEnabled || false);
    };

    if (isConnected && !userInfo) saveUserInfo();

    if (!isConnected && userInfo) {
      setUserInfo(null);
      setIsMFAEnabled(false);
    }
  }, [isConnected, userInfo, getUserInfo, setIsMFAEnabled]);

  return { loading, error, userInfo, isMFAEnabled, getUserInfo };
};



================================================
FILE: packages/modal/src/react/solana/index.ts
================================================
export * from "./hooks";



================================================
FILE: packages/modal/src/react/solana/hooks/index.ts
================================================
export * from "./useSignAndSendTransaction";
export * from "./useSignMessage";
export * from "./useSignTransaction";
export * from "./useSolanaWallet";



================================================
FILE: packages/modal/src/react/solana/hooks/useSignAndSendTransaction.ts
================================================
import { TransactionOrVersionedTransaction, WalletInitializationError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useSolanaWallet } from "./useSolanaWallet";

export type IUseSignAndSendTransaction = {
  loading: boolean;
  error: Web3AuthError | null;
  data: string | null;
  signAndSendTransaction: (transaction: TransactionOrVersionedTransaction) => Promise<string>;
};

export const useSignAndSendTransaction = (): IUseSignAndSendTransaction => {
  const { solanaWallet } = useSolanaWallet();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);
  const [data, setData] = useState<string | null>(null);

  const signAndSendTransaction = useCallback(
    async (transaction: TransactionOrVersionedTransaction) => {
      setLoading(true);
      setError(null);
      try {
        if (!solanaWallet) throw WalletInitializationError.notReady();
        const signature = await solanaWallet.signAndSendTransaction(transaction);
        setData(signature);
        return signature;
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [solanaWallet]
  );

  return { loading, error, data, signAndSendTransaction };
};



================================================
FILE: packages/modal/src/react/solana/hooks/useSignMessage.ts
================================================
import { WalletInitializationError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useSolanaWallet } from "./useSolanaWallet";

export type IUseSignMessage = {
  loading: boolean;
  error: Web3AuthError | null;
  data: string | null;
  signMessage: (message: string) => Promise<string>;
};

export const useSignMessage = (): IUseSignMessage => {
  const { solanaWallet, accounts } = useSolanaWallet();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);
  const [data, setData] = useState<string | null>(null);

  const signMessage = useCallback(
    async (message: string, from?: string) => {
      setLoading(true);
      setError(null);
      try {
        if (!solanaWallet) throw WalletInitializationError.notReady();
        const signature = await solanaWallet.signMessage(message, from ?? accounts?.[0]);
        setData(signature);
        return signature;
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [solanaWallet, accounts]
  );

  return { loading, error, data, signMessage };
};



================================================
FILE: packages/modal/src/react/solana/hooks/useSignTransaction.ts
================================================
import { type TransactionOrVersionedTransaction, WalletInitializationError, Web3AuthError } from "@web3auth/no-modal";
import { useCallback, useState } from "react";

import { useSolanaWallet } from "./useSolanaWallet";

export type IUseSignTransaction = {
  loading: boolean;
  error: Web3AuthError | null;
  data: string | null;
  signTransaction: (transaction: TransactionOrVersionedTransaction) => Promise<string>;
};

export const useSignTransaction = () => {
  const { solanaWallet } = useSolanaWallet();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Web3AuthError | null>(null);
  const [data, setData] = useState<string | null>(null);

  const signTransaction = useCallback(
    async (transaction: TransactionOrVersionedTransaction) => {
      setLoading(true);
      setError(null);
      try {
        if (!solanaWallet) throw WalletInitializationError.notReady();
        const signedTransaction = await solanaWallet.signTransaction(transaction);
        setData(signedTransaction);
        return signedTransaction;
      } catch (error) {
        setError(error as Web3AuthError);
      } finally {
        setLoading(false);
      }
    },
    [solanaWallet]
  );

  return {
    loading,
    error,
    data,
    signTransaction,
  };
};



================================================
FILE: packages/modal/src/react/solana/hooks/useSolanaWallet.ts
================================================
import { Connection } from "@solana/web3.js";
import { CHAIN_NAMESPACES, SolanaWallet } from "@web3auth/no-modal";
import { useEffect, useMemo, useState } from "react";

import { useWeb3Auth } from "../../hooks/useWeb3Auth";

export type IUseSolanaWallet = {
  accounts: string[] | null;
  solanaWallet: SolanaWallet | null;
  connection: Connection | null;
};

export 