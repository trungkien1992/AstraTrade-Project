Directory structure:
└── chipi-pay-chipi-sdk/
    ├── README.MD
    ├── package.json
    ├── tsconfig.json
    ├── tsup.config.ts
    ├── .npmignore
    ├── docs/
    │   ├── README.md
    │   ├── development.mdx
    │   ├── docs.json
    │   ├── introduction.mdx
    │   ├── quickstart.mdx
    │   ├── api-reference/
    │   │   ├── introduction.mdx
    │   │   ├── openapi.json
    │   │   └── endpoint/
    │   │       ├── create.mdx
    │   │       ├── delete.mdx
    │   │       └── get.mdx
    │   ├── essentials/
    │   │   ├── code.mdx
    │   │   ├── images.mdx
    │   │   ├── markdown.mdx
    │   │   ├── navigation.mdx
    │   │   ├── reusable-snippets.mdx
    │   │   └── settings.mdx
    │   └── snippets/
    │       └── snippet-intro.mdx
    └── src/
        ├── index.ts
        ├── types.ts
        ├── core/
        │   ├── backend-url.ts
        │   ├── chipi-sdk.ts
        │   ├── create-argent-wallet.ts
        │   ├── index.ts
        │   ├── send-transaction-with-paymaster.ts
        │   ├── types.ts
        │   └── lib/
        │       ├── encryption.ts
        │       └── index.ts
        └── react/
            ├── index.ts
            ├── types.ts
            ├── context/
            │   ├── chipi-provider.tsx
            │   └── index.ts
            └── hooks/
                ├── index.ts
                ├── use-approve.ts
                ├── use-call-any-contract.ts
                ├── use-create-wallet.ts
                ├── use-stake-vesu-usdc.ts
                ├── use-transfer.ts
                └── use-withdraw-vesu-usdc.ts


Files Content:

================================================
FILE: README.MD
================================================
# Chipi SDK

Chipi SDK is the easiest way to integrate USDC staking and withdrawal functionality into your React/Next.js application. Add secure wallet management, token staking, and withdrawals to your application in minutes. All transactions are sponsored thanks to Avnu's paymaster.

## Prerequisites

- React 18 or later
- Node.js >=18.17.0 or later
- A Chipi account. [Create your account for free](https://dashboard.chipipay.com)

## Installation

The fastest way to get started with Chipi SDK is by following our [Quickstart Guide](https://docs.chipipay.com/gasless/quickstart).

```bash
npm install @chipi-pay/chipi-sdk
# or
yarn add @chipi-pay/chipi-sdk
```

## Usage

For detailed information, guides, and examples visit our [documentation](https://docs.chipipay.com).

## Support

You can get in touch with us in any of the following ways:

- Join our [Telegram community](https://t.me/chipi_pay)
- Visit our [YouTube channel](https://www.youtube.com/@chipipay) for tutorials
- Email us at support@chipi.com

## Contributing

We're open to all community contributions! If you'd like to contribute in any way, please read our contribution guidelines and code of conduct.

## Security

@chipi-pay/chipi-sdk follows best practices for security, but 100% security cannot be assured.

@chipi-pay/chipi-sdk is provided "as is" without any warranty. Use at your own risk.

For more information and to report security issues, please refer to our [security documentation](https://docs.chipipay.com).


================================================
FILE: package.json
================================================
{
  "name": "@chipi-pay/chipi-sdk",
  "version": "3.2.2",
  "description": "SDK to create wallets and make gasless transactions",
  "main": "./dist/index.js",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "import": "./dist/index.mjs",
      "require": "./dist/index.js",
      "types": "./dist/index.d.ts"
    },
    "./react": {
      "import": "./dist/react/index.mjs",
      "require": "./dist/react/index.js",
      "types": "./dist/react/index.d.ts"
    }
  },
  "files": [
    "dist",
    "README.md"
  ],
  "scripts": {
    "build": "tsup",
    "dev": "tsup --watch",
    "typecheck": "tsc --noEmit"
  },
  "peerDependencies": {
    "@tanstack/react-query": ">=4.0.0",
    "react": ">=16.8.0",
    "starknet": ">=6.23.1"
  },
  "devDependencies": {
    "@types/crypto-js": "^4.2.2",
    "@types/node": "^22.15.15",
    "@types/react": "^18.2.0",
    "react": "^18.2.0",
    "tsup": "^8.3.6",
    "typescript": "^5.7.3"
  },
  "dependencies": {
    "@avnu/gasless-sdk": "^0.1.6",
    "@clerk/express": "^1.5.0",
    "crypto-js": "^4.2.0",
    "starknet": ">=6.23.1"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/chipi-pay/chipi-sdk"
  },
  "bugs": {
    "url": "https://github.com/chipi-pay/chipi-sdk/issues"
  },
  "homepage": "https://github.com/chipi-pay/chipi-sdk#readme"
}



================================================
FILE: tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "declaration": true,
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "jsx": "react-jsx"

  },
  "include": ["src", "src/index.ts"],
  "exclude": ["node_modules", "dist"]
} 


================================================
FILE: tsup.config.ts
================================================
// tsup.config.ts
import { defineConfig } from 'tsup';

export default defineConfig({
  entry: ['src/index.ts', 'src/react/index.ts'],
  format: ['cjs', 'esm'],  // Outputs both CommonJS and ES Modules
  dts: true,               // Generates TypeScript declaration files
  splitting: true,         // Enables code splitting
  sourcemap: true,        // Generates source maps for debugging
  clean: true,            // Cleans dist folder before build
  external: ['react', '@tanstack/react-query', 'starknet'],
  treeshake: true,        // Removes unused code
});


================================================
FILE: .npmignore
================================================
src
tsconfig.json
.gitignore
node_modules 


================================================
FILE: docs/README.md
================================================
# Mintlify Starter Kit

Click on `Use this template` to copy the Mintlify starter kit. The starter kit contains examples including

- Guide pages
- Navigation
- Customizations
- API Reference pages
- Use of popular components

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where docs.json is)

```
mintlify dev
```

### Publishing Changes

Install our Github App to auto propagate changes from your repo to your deployment. Changes will be deployed to production automatically after pushing to the default branch. Find the link to install on your dashboard. 

#### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`



================================================
FILE: docs/development.mdx
================================================
---
title: 'Development'
description: 'Preview changes locally to update your docs'
---

<Info>
  **Prerequisite**: Please install Node.js (version 19 or higher) before proceeding. <br />
  Please upgrade to ```docs.json``` before proceeding and delete the legacy ```mint.json``` file.
</Info>

Follow these steps to install and run Mintlify on your operating system:

**Step 1**: Install Mintlify:

<CodeGroup>

  ```bash npm
  npm i -g mintlify
  ```

```bash yarn
yarn global add mintlify
```

</CodeGroup>

**Step 2**: Navigate to the docs directory (where the `docs.json` file is located) and execute the following command:

```bash
mintlify dev
```

A local preview of your documentation will be available at `http://localhost:3000`.

### Custom Ports

By default, Mintlify uses port 3000. You can customize the port Mintlify runs on by using the `--port` flag. To run Mintlify on port 3333, for instance, use this command:

```bash
mintlify dev --port 3333
```

If you attempt to run Mintlify on a port that's already in use, it will use the next available port:

```md
Port 3000 is already in use. Trying 3001 instead.
```

## Mintlify Versions

Please note that each CLI release is associated with a specific version of Mintlify. If your local website doesn't align with the production version, please update the CLI:

<CodeGroup>

```bash npm
npm i -g mintlify@latest
```

```bash yarn
yarn global upgrade mintlify
```

</CodeGroup>

## Validating Links

The CLI can assist with validating reference links made in your documentation. To identify any broken links, use the following command:

```bash
mintlify broken-links
```

## Deployment

<Tip>
  Unlimited editors available under the [Pro
  Plan](https://mintlify.com/pricing) and above.
</Tip>

If the deployment is successful, you should see the following:

<Frame>
  <img src="/images/checks-passed.png" style={{ borderRadius: '0.5rem' }} />
</Frame>

## Code Formatting

We suggest using extensions on your IDE to recognize and format MDX. If you're a VSCode user, consider the [MDX VSCode extension](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx) for syntax highlighting, and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) for code formatting.

## Troubleshooting

<AccordionGroup>
  <Accordion title='Error: Could not load the "sharp" module using the darwin-arm64 runtime'>

    This may be due to an outdated version of node. Try the following:
    1. Remove the currently-installed version of mintlify: `npm remove -g mintlify`
    2. Upgrade to Node v19 or higher.
    3. Reinstall mintlify: `npm install -g mintlify`
  </Accordion>

  <Accordion title="Issue: Encountering an unknown error">
  
    Solution: Go to the root of your device and delete the \~/.mintlify folder. Afterwards, run `mintlify dev` again.
  </Accordion>
</AccordionGroup>

Curious about what changed in the CLI version? [Check out the CLI changelog.](https://www.npmjs.com/package/mintlify?activeTab=versions)



================================================
FILE: docs/docs.json
================================================
{
  "$schema": "https://mintlify.com/docs.json",
  "theme": "mint",
  "name": "Mint Starter Kit",
  "colors": {
    "primary": "#16A34A",
    "light": "#07C983",
    "dark": "#15803D"
  },
  "favicon": "/favicon.svg",
  "navigation": {
    "tabs": [
      {
        "tab": "Guides",
        "groups": [
          {
            "group": "Get Started",
            "pages": [
              "introduction",
              "quickstart",
              "development"
            ]
          },
          {
            "group": "Essentials",
            "pages": [
              "essentials/markdown",
              "essentials/code",
              "essentials/images",
              "essentials/settings",
              "essentials/navigation",
              "essentials/reusable-snippets"
            ]
          }
        ]
      },
      {
        "tab": "API Reference",
        "groups": [
          {
            "group": "API Documentation",
            "pages": [
              "api-reference/introduction"
            ]
          },
          {
            "group": "Endpoint Examples",
            "pages": [
              "api-reference/endpoint/get",
              "api-reference/endpoint/create",
              "api-reference/endpoint/delete"
            ]
          }
        ]
      }
    ],
    "global": {
      "anchors": [
        {
          "anchor": "Documentation",
          "href": "https://mintlify.com/docs",
          "icon": "book-open-cover"
        },
        {
          "anchor": "Community",
          "href": "https://mintlify.com/community",
          "icon": "slack"
        },
        {
          "anchor": "Blog",
          "href": "https://mintlify.com/blog",
          "icon": "newspaper"
        }
      ]
    }
  },
  "logo": {
    "light": "/logo/light.svg",
    "dark": "/logo/dark.svg"
  },
  "navbar": {
    "links": [
      {
        "label": "Support",
        "href": "mailto:hi@mintlify.com"
      }
    ],
    "primary": {
      "type": "button",
      "label": "Dashboard",
      "href": "https://dashboard.mintlify.com"
    }
  },
  "footer": {
    "socials": {
      "x": "https://x.com/hicihpipay",
      "github": "https://github.com/chipipay"
    }
  }
}


================================================
FILE: docs/introduction.mdx
================================================
---
title: Introduction
description: "Welcome to the home of your new documentation"
---

<img
  className="block dark:hidden"
  src="/images/hero-light.png"
  alt="Hero Light"
/>
<img
  className="hidden dark:block"
  src="/images/hero-dark.png"
  alt="Hero Dark"
/>

## Setting up

The first step to world-class documentation is setting up your editing environments.

<CardGroup cols={2}>
  <Card
    title="Edit Your Docs"
    icon="pen-to-square"
    href="https://mintlify.com/docs/quickstart"
  >
    Get your docs set up locally for easy development
  </Card>
  <Card
    title="Preview Changes"
    icon="image"
    href="https://mintlify.com/docs/development"
  >
    Preview your changes before you push to make sure they're perfect
  </Card>
</CardGroup>

## Make it yours

Update your docs to your brand and add valuable content for the best user conversion.

<CardGroup cols={2}>
  <Card
    title="Customize Style"
    icon="palette"
    href="https://mintlify.com/docs/settings/global"
  >
    Customize your docs to your company's colors and brands
  </Card>
  <Card
    title="Reference APIs"
    icon="code"
    href="https://mintlify.com/docs/api-playground/openapi"
  >
    Automatically generate endpoints from an OpenAPI spec
  </Card>
  <Card
    title="Add Components"
    icon="screwdriver-wrench"
    href="https://mintlify.com/docs/content/components/accordions"
  >
    Build interactive features and designs to guide your users
  </Card>
  <Card
    title="Get Inspiration"
    icon="stars"
    href="https://mintlify.com/customers"
  >
    Check out our showcase of our favorite documentation
  </Card>
</CardGroup>



================================================
FILE: docs/quickstart.mdx
================================================
---
title: 'Quickstart'
description: 'Start building awesome documentation in under 5 minutes'
---

## Setup your development

Learn how to update your docs locally for Starknet.

### Edit and preview

<AccordionGroup>
  <Accordion icon="github" title="Clone your docs locally">
    During the onboarding process, we created a repository on your Github with
    your docs content. You can find this repository on our
    [dashboard](https://dashboard.mintlify.com). To clone the repository
    locally, follow these
    [instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    in your terminal.
  </Accordion>
  <Accordion icon="rectangle-terminal" title="Preview changes">
    Previewing helps you make sure your changes look as intended. We built a
    command line interface to render these changes locally. 
    1. Install the
    [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the
    documentation changes locally with this command: ``` npm i -g mintlify ```
    2. Run the following command at the root of your documentation (where
    `docs.json` is): ``` mintlify dev ```
    <Note>
      If you’re currently using the legacy ```mint.json``` configuration file, please update the Mintlify CLI:


      ```npm i -g mintlify@latest```
      And run the new upgrade command in your docs repository:

      ```mintlify upgrade```
      You should now be using the new ```docs.json``` configuration file. Feel free to delete the ```mint.json``` file from your repository.
    </Note>
  </Accordion>
</AccordionGroup>

### Deploy your changes

<AccordionGroup>

<Accordion icon="message-bot" title="Install our Github app">
  Our Github app automatically deploys your changes to your docs site, so you
  don't need to manage deployments yourself. You can find the link to install on
  your [dashboard](https://dashboard.mintlify.com). Once the bot has been
  successfully installed, there should be a check mark next to the commit hash
  of the repo.
</Accordion>
<Accordion icon="rocket" title="Push your changes">
  [Commit and push your changes to
  Git](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository#about-git-push)
  for your changes to update in your docs site. If you push and don't see that
  the Github app successfully deployed your changes, you can also manually
  update your docs through our [dashboard](https://dashboard.mintlify.com).
</Accordion>

</AccordionGroup>

## Update your docs

Add content directly in your files with MDX syntax and React components. You can use any of our components, or even build your own.

<CardGroup>

<Card title="Add Content With MDX" icon="file" href="/essentials/markdown">
  Add content to your docs with MDX syntax.
</Card>

<Card
  title="Add Code Blocks"
  icon="square-code"
  href="/essentials/code"
>
  Add code directly to your docs with syntax highlighting.
</Card>

<Card
  title="Add Images"
  icon="image"
  href="/essentials/images"
>
  Add images to your docs to make them more engaging.
</Card>

<Card
  title="Add Custom Components"
  icon="puzzle-piece"
  href="/essentials/reusable-snippets"
>
  Add templates to your docs to make them more reusable.
</Card>

</CardGroup>



================================================
FILE: docs/api-reference/introduction.mdx
================================================
---
title: 'Introduction'
description: 'Example section for showcasing API endpoints'
---

<Note>
  If you're not looking to build API reference documentation, you can delete
  this section by removing the api-reference folder.
</Note>

## Welcome

There are two ways to build API documentation: [OpenAPI](https://mintlify.com/docs/api-playground/openapi/setup) and [MDX components](https://mintlify.com/docs/api-playground/mdx/configuration). For the starter kit, we are using the following OpenAPI specification.

<Card
  title="Plant Store Endpoints"
  icon="leaf"
  href="https://github.com/mintlify/starter/blob/main/api-reference/openapi.json"
>
  View the OpenAPI specification file
</Card>

## Authentication

All API endpoints are authenticated using Bearer tokens and picked up from the specification file.

```json
"security": [
  {
    "bearerAuth": []
  }
]
```



================================================
FILE: docs/api-reference/openapi.json
================================================
{
  "openapi": "3.0.1",
  "info": {
    "title": "OpenAPI Plant Store",
    "description": "A sample API that uses a plant store as an example to demonstrate features in the OpenAPI specification",
    "license": {
      "name": "MIT"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "http://sandbox.mintlify.com"
    }
  ],
  "security": [
    {
      "bearerAuth": []
    }
  ],
  "paths": {
    "/plants": {
      "get": {
        "description": "Returns all plants from the system that the user has access to",
        "parameters": [
          {
            "name": "limit",
            "in": "query",
            "description": "The maximum number of results to return",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Plant response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Plant"
                  }
                }
              }
            }
          },
          "400": {
            "description": "Unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      },
      "post": {
        "description": "Creates a new plant in the store",
        "requestBody": {
          "description": "Plant to add to the store",
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/NewPlant"
              }
            }
          },
          "required": true
        },
        "responses": {
          "200": {
            "description": "plant response",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Plant"
                }
              }
            }
          },
          "400": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    },
    "/plants/{id}": {
      "delete": {
        "description": "Deletes a single plant based on the ID supplied",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of plant to delete",
            "required": true,
            "schema": {
              "type": "integer",
              "format": "int64"
            }
          }
        ],
        "responses": {
          "204": {
            "description": "Plant deleted",
            "content": {}
          },
          "400": {
            "description": "unexpected error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "Plant": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "name": {
            "description": "The name of the plant",
            "type": "string"
          },
          "tag": {
            "description": "Tag to specify the type",
            "type": "string"
          }
        }
      },
      "NewPlant": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Plant"
          },
          {
            "required": [
              "id"
            ],
            "type": "object",
            "properties": {
              "id": {
                "description": "Identification number of the plant",
                "type": "integer",
                "format": "int64"
              }
            }
          }
        ]
      },
      "Error": {
        "required": [
          "error",
          "message"
        ],
        "type": "object",
        "properties": {
          "error": {
            "type": "integer",
            "format": "int32"
          },
          "message": {
            "type": "string"
          }
        }
      }
    },
    "securitySchemes": {
      "bearerAuth": {
        "type": "http",
        "scheme": "bearer"
      }
    }
  }
}


================================================
FILE: docs/api-reference/endpoint/create.mdx
================================================
---
title: 'Create Plant'
openapi: 'POST /plants'
---



================================================
FILE: docs/api-reference/endpoint/delete.mdx
================================================
---
title: 'Delete Plant'
openapi: 'DELETE /plants/{id}'
---



================================================
FILE: docs/api-reference/endpoint/get.mdx
================================================
---
title: 'Get Plants'
openapi: 'GET /plants'
---



================================================
FILE: docs/essentials/code.mdx
================================================
---
title: 'Code Blocks'
description: 'Display inline code and code blocks'
icon: 'code'
---

## Basic

### Inline Code

To denote a `word` or `phrase` as code, enclose it in backticks (`).

```
To denote a `word` or `phrase` as code, enclose it in backticks (`).
```

### Code Block

Use [fenced code blocks](https://www.markdownguide.org/extended-syntax/#fenced-code-blocks) by enclosing code in three backticks and follow the leading ticks with the programming language of your snippet to get syntax highlighting. Optionally, you can also write the name of your code after the programming language.

```java HelloWorld.java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

````md
```java HelloWorld.java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```
````



================================================
FILE: docs/essentials/images.mdx
================================================
---
title: 'Images and Embeds'
description: 'Add image, video, and other HTML elements'
icon: 'image'
---

<img
  style={{ borderRadius: '0.5rem' }}
  src="https://mintlify-assets.b-cdn.net/bigbend.jpg"
/>

## Image

### Using Markdown

The [markdown syntax](https://www.markdownguide.org/basic-syntax/#images) lets you add images using the following code

```md
![title](/path/image.jpg)
```

Note that the image file size must be less than 5MB. Otherwise, we recommend hosting on a service like [Cloudinary](https://cloudinary.com/) or [S3](https://aws.amazon.com/s3/). You can then use that URL and embed.

### Using Embeds

To get more customizability with images, you can also use [embeds](/writing-content/embed) to add images

```html
<img height="200" src="/path/image.jpg" />
```

## Embeds and HTML elements

<iframe
  width="560"
  height="315"
  src="https://www.youtube.com/embed/4KzFe50RQkQ"
  title="YouTube video player"
  frameBorder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowFullScreen
  style={{ width: '100%', borderRadius: '0.5rem' }}
></iframe>

<br />

<Tip>

Mintlify supports [HTML tags in Markdown](https://www.markdownguide.org/basic-syntax/#html). This is helpful if you prefer HTML tags to Markdown syntax, and lets you create documentation with infinite flexibility.

</Tip>

### iFrames

Loads another HTML page within the document. Most commonly used for embedding videos.

```html
<iframe src="https://www.youtube.com/embed/4KzFe50RQkQ"> </iframe>
```



================================================
FILE: docs/essentials/markdown.mdx
================================================
---
title: 'Markdown Syntax'
description: 'Text, title, and styling in standard markdown'
icon: 'text-size'
---

## Titles

Best used for section headers.

```md
## Titles
```

### Subtitles

Best use to subsection headers.

```md
### Subtitles
```

<Tip>

Each **title** and **subtitle** creates an anchor and also shows up on the table of contents on the right.

</Tip>

## Text Formatting

We support most markdown formatting. Simply add `**`, `_`, or `~` around text to format it.

| Style         | How to write it   | Result          |
| ------------- | ----------------- | --------------- |
| Bold          | `**bold**`        | **bold**        |
| Italic        | `_italic_`        | _italic_        |
| Strikethrough | `~strikethrough~` | ~strikethrough~ |

You can combine these. For example, write `**_bold and italic_**` to get **_bold and italic_** text.

You need to use HTML to write superscript and subscript text. That is, add `<sup>` or `<sub>` around your text.

| Text Size   | How to write it          | Result                 |
| ----------- | ------------------------ | ---------------------- |
| Superscript | `<sup>superscript</sup>` | <sup>superscript</sup> |
| Subscript   | `<sub>subscript</sub>`   | <sub>subscript</sub>   |

## Linking to Pages

You can add a link by wrapping text in `[]()`. You would write `[link to google](https://google.com)` to [link to google](https://google.com).

Links to pages in your docs need to be root-relative. Basically, you should include the entire folder path. For example, `[link to text](/writing-content/text)` links to the page "Text" in our components section.

Relative links like `[link to text](../text)` will open slower because we cannot optimize them as easily.

## Blockquotes

### Singleline

To create a blockquote, add a `>` in front of a paragraph.

> Dorothy followed her through many of the beautiful rooms in her castle.

```md
> Dorothy followed her through many of the beautiful rooms in her castle.
```

### Multiline

> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

```md
> Dorothy followed her through many of the beautiful rooms in her castle.
>
> The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.
```

### LaTeX

Mintlify supports [LaTeX](https://www.latex-project.org) through the Latex component.

<Latex>8 x (vk x H1 - H2) = (0,1)</Latex>

```md
<Latex>8 x (vk x H1 - H2) = (0,1)</Latex>
```



================================================
FILE: docs/essentials/navigation.mdx
================================================
---
title: 'Navigation'
description: 'The navigation field in docs.json defines the pages that go in the navigation menu'
icon: 'map'
---

The navigation menu is the list of links on every website.

You will likely update `docs.json` every time you add a new page. Pages do not show up automatically.

## Navigation syntax

Our navigation syntax is recursive which means you can make nested navigation groups. You don't need to include `.mdx` in page names.

<CodeGroup>

```json Regular Navigation
"navigation": {
  "tabs": [
    {
      "tab": "Docs",
      "groups": [
        {
          "group": "Getting Started",
          "pages": ["quickstart"]
        }
      ]
    }
  ]
}
```

```json Nested Navigation
"navigation": {
  "tabs": [
    {
      "tab": "Docs",
      "groups": [
        {
          "group": "Getting Started",
          "pages": [
            "quickstart",
            {
              "group": "Nested Reference Pages",
              "pages": ["nested-reference-page"]
            }
          ]
        }
      ]
    }
  ]
}
```

</CodeGroup>

## Folders

Simply put your MDX files in folders and update the paths in `docs.json`.

For example, to have a page at `https://yoursite.com/your-folder/your-page` you would make a folder called `your-folder` containing an MDX file called `your-page.mdx`.

<Warning>

You cannot use `api` for the name of a folder unless you nest it inside another folder. Mintlify uses Next.js which reserves the top-level `api` folder for internal server calls. A folder name such as `api-reference` would be accepted.

</Warning>

```json Navigation With Folder
"navigation": {
  "tabs": [
    {
      "tab": "Docs",
      "groups": [
        {
          "group": "Group Name",
          "pages": ["your-folder/your-page"]
        }
      ]
    }
  ]
}
```

## Hidden Pages

MDX files not included in `docs.json` will not show up in the sidebar but are accessible through the search bar and by linking directly to them.



================================================
FILE: docs/essentials/reusable-snippets.mdx
================================================
---
title: Reusable Snippets
description: Reusable, custom snippets to keep content in sync
icon: 'recycle'
---

import SnippetIntro from '/snippets/snippet-intro.mdx';

<SnippetIntro />

## Creating a custom snippet

**Pre-condition**: You must create your snippet file in the `snippets` directory.

<Note>
  Any page in the `snippets` directory will be treated as a snippet and will not
  be rendered into a standalone page. If you want to create a standalone page
  from the snippet, import the snippet into another file and call it as a
  component.
</Note>

### Default export

1. Add content to your snippet file that you want to re-use across multiple
   locations. Optionally, you can add variables that can be filled in via props
   when you import the snippet.

```mdx snippets/my-snippet.mdx
Hello world! This is my content I want to reuse across pages. My keyword of the
day is {word}.
```

<Warning>
  The content that you want to reuse must be inside the `snippets` directory in
  order for the import to work.
</Warning>

2. Import the snippet into your destination file.

```mdx destination-file.mdx
---
title: My title
description: My Description
---

import MySnippet from '/snippets/path/to/my-snippet.mdx';

## Header

Lorem impsum dolor sit amet.

<MySnippet word="bananas" />
```

### Reusable variables

1. Export a variable from your snippet file:

```mdx snippets/path/to/custom-variables.mdx
export const myName = 'my name';

export const myObject = { fruit: 'strawberries' };
```

2. Import the snippet from your destination file and use the variable:

```mdx destination-file.mdx
---
title: My title
description: My Description
---

import { myName, myObject } from '/snippets/path/to/custom-variables.mdx';

Hello, my name is {myName} and I like {myObject.fruit}.
```

### Reusable components

1. Inside your snippet file, create a component that takes in props by exporting
   your component in the form of an arrow function.

```mdx snippets/custom-component.mdx
export const MyComponent = ({ title }) => (
  <div>
    <h1>{title}</h1>
    <p>... snippet content ...</p>
  </div>
);
```

<Warning>
  MDX does not compile inside the body of an arrow function. Stick to HTML
  syntax when you can or use a default export if you need to use MDX.
</Warning>

2. Import the snippet into your destination file and pass in the props

```mdx destination-file.mdx
---
title: My title
description: My Description
---

import { MyComponent } from '/snippets/custom-component.mdx';

Lorem ipsum dolor sit amet.

<MyComponent title={'Custom title'} />
```



================================================
FILE: docs/essentials/settings.mdx
================================================
---
title: 'Global Settings'
description: 'Mintlify gives you complete control over the look and feel of your documentation using the docs.json file'
icon: 'gear'
---

Every Mintlify site needs a `docs.json` file with the core configuration settings. Learn more about the [properties](#properties) below.

## Properties

<ResponseField name="name" type="string" required>
Name of your project. Used for the global title.

Example: `mintlify`

</ResponseField>

<ResponseField name="navigation" type="Navigation[]" required>
  An array of groups with all the pages within that group
  <Expandable title="Navigation">
    <ResponseField name="group" type="string">
    The name of the group.

    Example: `Settings`

    </ResponseField>
    <ResponseField name="pages" type="string[]">
    The relative paths to the markdown files that will serve as pages.

    Example: `["customization", "page"]`

    </ResponseField>

  </Expandable>
</ResponseField>

<ResponseField name="logo" type="string or object">
  Path to logo image or object with path to "light" and "dark" mode logo images
  <Expandable title="Logo">
    <ResponseField name="light" type="string">
      Path to the logo in light mode
    </ResponseField>
    <ResponseField name="dark" type="string">
      Path to the logo in dark mode
    </ResponseField>
    <ResponseField name="href" type="string" default="/">
      Where clicking on the logo links you to
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="favicon" type="string">
  Path to the favicon image
</ResponseField>

<ResponseField name="colors" type="Colors">
  Hex color codes for your global theme
  <Expandable title="Colors">
    <ResponseField name="primary" type="string" required>
      The primary color. Used for most often for highlighted content, section
      headers, accents, in light mode
    </ResponseField>
    <ResponseField name="light" type="string">
      The primary color for dark mode. Used for most often for highlighted
      content, section headers, accents, in dark mode
    </ResponseField>
    <ResponseField name="dark" type="string">
      The primary color for important buttons
    </ResponseField>
    <ResponseField name="background" type="object">
      The color of the background in both light and dark mode
      <Expandable title="Object">
        <ResponseField name="light" type="string" required>
          The hex color code of the background in light mode
        </ResponseField>
        <ResponseField name="dark" type="string" required>
          The hex color code of the background in dark mode
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="topbarLinks" type="TopbarLink[]">
  Array of `name`s and `url`s of links you want to include in the topbar
  <Expandable title="TopbarLink">
    <ResponseField name="name" type="string">
    The name of the button.

    Example: `Contact us`
    </ResponseField>
    <ResponseField name="url" type="string">
    The url once you click on the button. Example: `https://mintlify.com/docs`
    </ResponseField>

  </Expandable>
</ResponseField>

<ResponseField name="topbarCtaButton" type="Call to Action">
  <Expandable title="Topbar Call to Action">
    <ResponseField name="type" type={'"link" or "github"'} default="link">
    Link shows a button. GitHub shows the repo information at the url provided including the number of GitHub stars.
    </ResponseField>
    <ResponseField name="url" type="string">
    If `link`: What the button links to.
    
    If `github`: Link to the repository to load GitHub information from.
    </ResponseField>
    <ResponseField name="name" type="string">
    Text inside the button. Only required if `type` is a `link`.
    </ResponseField>

  </Expandable>
</ResponseField>

<ResponseField name="versions" type="string[]">
  Array of version names. Only use this if you want to show different versions
  of docs with a dropdown in the navigation bar.
</ResponseField>

<ResponseField name="anchors" type="Anchor[]">
  An array of the anchors, includes the `icon`, `color`, and `url`.
  <Expandable title="Anchor">
    <ResponseField name="icon" type="string">
    The [Font Awesome](https://fontawesome.com/search?q=heart) icon used to feature the anchor.

    Example: `comments`
    </ResponseField>
    <ResponseField name="name" type="string">
    The name of the anchor label.

    Example: `Community`
    </ResponseField>
    <ResponseField name="url" type="string">
      The start of the URL that marks what pages go in the anchor. Generally, this is the name of the folder you put your pages in.
    </ResponseField>
    <ResponseField name="color" type="string">
      The hex color of the anchor icon background. Can also be a gradient if you pass an object with the properties `from` and `to` that are each a hex color.
    </ResponseField>
    <ResponseField name="version" type="string">
      Used if you want to hide an anchor until the correct docs version is selected.
    </ResponseField>
    <ResponseField name="isDefaultHidden" type="boolean" default="false">
      Pass `true` if you want to hide the anchor until you directly link someone to docs inside it.
    </ResponseField>
    <ResponseField name="iconType" default="duotone" type="string">
      One of: "brands", "duotone", "light", "sharp-solid", "solid", or "thin"
    </ResponseField>

  </Expandable>
</ResponseField>

<ResponseField name="topAnchor" type="Object">
  Override the default configurations for the top-most anchor.
  <Expandable title="Object">
    <ResponseField name="name" default="Documentation" type="string">
      The name of the top-most anchor
    </ResponseField>
    <ResponseField name="icon" default="book-open" type="string">
      Font Awesome icon.
    </ResponseField>
    <ResponseField name="iconType" default="duotone" type="string">
      One of: "brands", "duotone", "light", "sharp-solid", "solid", or "thin"
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="tabs" type="Tabs[]">
  An array of navigational tabs.
  <Expandable title="Tabs">
    <ResponseField name="name" type="string">
      The name of the tab label.
    </ResponseField>
    <ResponseField name="url" type="string">
      The start of the URL that marks what pages go in the tab. Generally, this
      is the name of the folder you put your pages in.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="api" type="API">
  Configuration for API settings. Learn more about API pages at [API Components](/api-playground/demo).
  <Expandable title="API">
    <ResponseField name="baseUrl" type="string">
      The base url for all API endpoints. If `baseUrl` is an array, it will enable for multiple base url
      options that the user can toggle.
    </ResponseField>

    <ResponseField name="auth" type="Auth">
      <Expandable title="Auth">
        <ResponseField name="method" type='"bearer" | "basic" | "key"'>
          The authentication strategy used for all API endpoints.
        </ResponseField>
        <ResponseField name="name" type="string">
        The name of the authentication parameter used in the API playground.

        If method is `basic`, the format should be `[usernameName]:[passwordName]`
        </ResponseField>
        <ResponseField name="inputPrefix" type="string">
        The default value that's designed to be a prefix for the authentication input field.

        E.g. If an `inputPrefix` of `AuthKey` would inherit the default input result of the authentication field as `AuthKey`.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="playground" type="Playground">
      Configurations for the API playground

      <Expandable title="Playground">
        <ResponseField name="mode" default="show" type='"show" | "simple" | "hide"'>
          Whether the playground is showing, hidden, or only displaying the endpoint with no added user interactivity `simple`

          Learn more at the [playground guides](/api-playground/demo)
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="maintainOrder" type="boolean">
      Enabling this flag ensures that key ordering in OpenAPI pages matches the key ordering defined in the OpenAPI file.

      <Warning>This behavior will soon be enabled by default, at which point this field will be deprecated.</Warning>
    </ResponseField>

  </Expandable>
</ResponseField>

<ResponseField name="openapi" type="string | string[]">
  A string or an array of strings of URL(s) or relative path(s) pointing to your
  OpenAPI file.
  
  Examples:
  <CodeGroup>
    ```json Absolute
    "openapi": "https://example.com/openapi.json"
    ```
    ```json Relative
    "openapi": "/openapi.json"
    ```
    ```json Multiple
    "openapi": ["https://example.com/openapi1.json", "/openapi2.json", "/openapi3.json"]
    ```
  </CodeGroup>

</ResponseField>

<ResponseField name="footerSocials" type="FooterSocials">
  An object of social media accounts where the key:property pair represents the social media platform and the account url.
  
  Example: 
  ```json
  {
    "x": "https://x.com/mintlify",
    "website": "https://mintlify.com"
  }
  ```
  <Expandable title="FooterSocials">
    <ResponseField name="[key]" type="string">
    One of the following values `website`, `facebook`, `x`, `discord`, `slack`, `github`, `linkedin`, `instagram`, `hacker-news`
    
    Example: `x`
    </ResponseField>
    <ResponseField name="property" type="string">
    The URL to the social platform.
    
    Example: `https://x.com/mintlify`
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="feedback" type="Feedback">
  Configurations to enable feedback buttons

  <Expandable title="Feedback">
    <ResponseField name="suggestEdit" type="boolean" default="false">
    Enables a button to allow users to suggest edits via pull requests
    </ResponseField>
    <ResponseField name="raiseIssue" type="boolean" default="false">
    Enables a button to allow users to raise an issue about the documentation
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="modeToggle" type="ModeToggle">
  Customize the dark mode toggle.
  <Expandable title="ModeToggle">
    <ResponseField name="default" type={'"light" or "dark"'}>
      Set if you always want to show light or dark mode for new users. When not
      set, we default to the same mode as the user's operating system.
    </ResponseField>
    <ResponseField name="isHidden" type="boolean" default="false">
      Set to true to hide the dark/light mode toggle. You can combine `isHidden` with `default` to force your docs to only use light or dark mode. For example:
      
      <CodeGroup>
      ```json Only Dark Mode
      "modeToggle": {
        "default": "dark",
        "isHidden": true
      }
      ```

      ```json Only Light Mode
      "modeToggle": {
        "default": "light",
        "isHidden": true
      }
      ```
      </CodeGroup>

    </ResponseField>

  </Expandable>
</ResponseField>

<ResponseField name="backgroundImage" type="string">
  A background image to be displayed behind every page. See example with
  [Infisical](https://infisical.com/docs) and [FRPC](https://frpc.io).
</ResponseField>



================================================
FILE: docs/snippets/snippet-intro.mdx
================================================
One of the core principles of software development is DRY (Don't Repeat
Yourself). This is a principle that apply to documentation as
well. If you find yourself repeating the same content in multiple places, you
should consider creating a custom snippet to keep your content in sync.



================================================
FILE: src/index.ts
================================================
// Core exports
export * from './core';

// React exports
export * from './react';


================================================
FILE: src/types.ts
================================================
import { Call } from "starknet";

export interface ChipiSDKConfig {
  apiKey: string;
  rpcUrl: string;
  argentClassHash: string;
  contractAddress: string;
  contractEntryPoint?: string;
}

export interface WalletData {
  publicKey: string;
  encryptedPrivateKey: string;
}

// Tipos específicos para diferentes transacciones
export interface TransferParams {
  recipient: string;
  amount: string | number;
  decimals?: number;
}

export interface IncrementParams {
  // No requiere parámetros adicionales
}

// Union type para todos los tipos de transacciones
export type TransactionParams = {
  type: 'transfer' | 'approve';
  params: TransferParams;
} | {
  type: 'wildcard';
  params: IncrementParams;
};

export interface SimpleTransactionInput {
  pin: string;
  wallet: WalletData;
  contractAddress: string;
  calls: Call[];
}

export interface TransactionInput {
  pin: string;
  wallet: WalletData;
  calls: Call[];
}

export interface TransactionResult {
  success: boolean;
  accountAddress: string;
  encryptedPrivateKey: string;
  txHash: string;
} 


================================================
FILE: src/core/backend-url.ts
================================================
export const BACKEND_URL = "https://api.chipipay.com/v1";


================================================
FILE: src/core/chipi-sdk.ts
================================================
import { cairo, type Call, type Uint256 } from "starknet";
import {
  executePaymasterTransaction,
  ExecuteTransactionParams,
} from "./send-transaction-with-paymaster";
import type {
  ApproveParams,
  CallAnyContractParams,
  ChipiSDKConfig,
  CreateWalletParams,
  StakeVesuUsdcParams,
  TransferParams,
  WithdrawVesuUsdcParams,
} from "./types";
import { createArgentWallet } from "./create-argent-wallet";
import { CreateWalletResponse } from "./types";

export class ChipiSDK {
  private apiPublicKey: string;
  private readonly nodeUrl = "https://starknet-mainnet.public.blastapi.io/rpc/v0_7";

  constructor(config: ChipiSDKConfig) {
    this.apiPublicKey = config.apiPublicKey;
    
    // Bind all methods to preserve this context
    this.executeTransaction = this.executeTransaction.bind(this);
    this.transfer = this.transfer.bind(this);
    this.approve = this.approve.bind(this);
    this.stakeVesuUsdc = this.stakeVesuUsdc.bind(this);
    this.withdrawVesuUsdc = this.withdrawVesuUsdc.bind(this);
    this.callAnyContract = this.callAnyContract.bind(this);
    this.createWallet = this.createWallet.bind(this);
  }

  private formatAmount(amount: string | number, decimals: number = 18): string {
    const amountStr = amount.toString();
    // Si es un número entero, multiplicar por 10^decimals
    if (!amountStr.includes('.')) {
      const amountBN = BigInt(amountStr) * BigInt(10) ** BigInt(decimals);
      console.log('Formatted integer amount:', amountBN.toString());
      return amountBN.toString();
    }

    // Si tiene decimales, manejamos como antes
    const [integerPart, decimalPart = ''] = amountStr.split('.');
    const paddedDecimal = decimalPart.padEnd(decimals, '0').slice(0, decimals);
    const amountBN = BigInt(integerPart + paddedDecimal);
    
    return amountBN.toString();
  }

  async executeTransaction(input: Omit<ExecuteTransactionParams, 'apiPublicKey'>): Promise<string> {
    return executePaymasterTransaction({
      ...input,
      apiPublicKey: this.apiPublicKey,
    });
  }

  async transfer(params: Omit<TransferParams, 'apiPublicKey'>): Promise<string> {
    const { encryptKey, wallet, contractAddress, recipient, amount, decimals, bearerToken } = params;
    const formattedAmount = this.formatAmount(amount, decimals);
    
    return this.executeTransaction({
      encryptKey,
      wallet,
      bearerToken,
      calls: [
        {
          contractAddress,
          entrypoint: "transfer",
          calldata: [
            recipient,
            formattedAmount,
            "0x0",
          ],
        },
      ],
    });
  }

  async approve(params: Omit<ApproveParams, 'apiPublicKey'>): Promise<string> {
    const { encryptKey, wallet, contractAddress, spender, amount, decimals, bearerToken } = params;
    return this.executeTransaction({
      encryptKey,
      wallet,
      bearerToken,
      calls: [
        {
          contractAddress,
          entrypoint: "approve",
          calldata: [
            spender,
            this.formatAmount(amount, decimals),
            "0x0",
          ],
        },
      ],
    });
  }

  async stakeVesuUsdc(params: Omit<StakeVesuUsdcParams, 'apiPublicKey'>): Promise<string> {
    const { encryptKey, wallet, amount, receiverWallet, bearerToken } = params;
    const formattedAmount = this.formatAmount(amount, 6);
    
    return this.executeTransaction({
      encryptKey,
      wallet,
      bearerToken,
      calls: [
        {
          contractAddress:"0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
          entrypoint: "approve",
          calldata: [
            "0x017f19582c61479f2fe0b6606300e975c0a8f439102f43eeecc1d0e9b3d84350",
            formattedAmount,
            "0x0",
          ],
        },
        {
          contractAddress:"0x017f19582c61479f2fe0b6606300e975c0a8f439102f43eeecc1d0e9b3d84350",
          entrypoint: "deposit",
          calldata: [
            formattedAmount,
            "0x0",
            receiverWallet,
          ],
        },
      ],
    });
  }

  async withdrawVesuUsdc(params: Omit<WithdrawVesuUsdcParams, 'apiPublicKey'>): Promise<string> {
    const { encryptKey, wallet, amount, recipient, bearerToken } = params;
    const formattedAmount = this.formatAmount(amount, 6);
    
    return this.executeTransaction({
      encryptKey,
      wallet,
      bearerToken,
      calls: [
        {
          contractAddress: "0x017f19582c61479f2fe0b6606300e975c0a8f439102f43eeecc1d0e9b3d84350",
          entrypoint: "withdraw",
          calldata: [
            formattedAmount,
            recipient,
            "0x0",
          ],
        },
      ],
    });
  }

  async callAnyContract(params: Omit<CallAnyContractParams, 'apiPublicKey'>): Promise<string> {
    const { encryptKey, wallet, contractAddress, calls, bearerToken } = params;
    return this.executeTransaction({
      encryptKey,
      wallet,
      bearerToken,
      calls,
    });
  }

  async createWallet(params: Omit<CreateWalletParams, 'apiPublicKey' | 'nodeUrl'>): Promise<CreateWalletResponse> {
    const { encryptKey, bearerToken } = params;
    return createArgentWallet({
      encryptKey: encryptKey,
      apiPublicKey: this.apiPublicKey,
      bearerToken,
      nodeUrl: this.nodeUrl,
    });
  }
}

// Export types
// export type { ChipiSDKConfig, WalletData, TransactionResult };


================================================
FILE: src/core/create-argent-wallet.ts
================================================
import type { DeploymentData } from "@avnu/gasless-sdk";
import {
  Account,
  CairoCustomEnum,
  CairoOption,
  CairoOptionVariant,
  CallData,
  ec,
  hash,
  num,
  RpcProvider,
  stark,
} from "starknet";
import { encryptPrivateKey } from "./lib/encryption";
import { CreateWalletParams, CreateWalletResponse, WalletData } from "./types";
import { BACKEND_URL } from "./backend-url";


export const createArgentWallet = async (
   params: CreateWalletParams
): Promise<CreateWalletResponse> => {

  // console.log("create wallet Params: ", params);
  try {
    const { encryptKey, apiPublicKey, bearerToken, nodeUrl } = params;
   
    const provider = new RpcProvider({ nodeUrl: nodeUrl });
    // Generating the private key with Stark Curve
    const privateKeyAX = stark.randomAddress();
    const starkKeyPubAX = ec.starkCurve.getStarkKey(privateKeyAX);

    // Using Argent X Account v0.4.0 class hash
    const accountClassHash = "0x036078334509b514626504edc9fb252328d1a240e4e948bef8d0c08dff45927f" //params.argentClassHash;
  
    // Calculate future address of the ArgentX account
    const axSigner = new CairoCustomEnum({
      Starknet: { pubkey: starkKeyPubAX },
    });
    // Set the dApp Guardian address
    const axGuardian = new CairoOption<unknown>(CairoOptionVariant.None);

    const AXConstructorCallData = CallData.compile({
      owner: axSigner,
      guardian: axGuardian,
    });

    const publicKey = hash.calculateContractAddressFromHash(
      starkKeyPubAX,
      accountClassHash,
      AXConstructorCallData,
      0
    );
    // console.log("Contract address: ", contractAddress);
   
    // Initiating Account
    const account = new Account(provider, publicKey, privateKeyAX);
    // console.log("Account ", { ...account });

    // Backend Call API to create the wallet
    console.log("apiPublicKey", apiPublicKey);
    const typeDataResponse = await fetch(`${BACKEND_URL}/chipi-wallets/prepare-creation`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${bearerToken}`,
        'x-api-key': apiPublicKey,
      },
      body: JSON.stringify({
        publicKey,
      }),
    });
    const { typeData, accountClassHash: accountClassHashResponse } = await typeDataResponse.json();

    // console.log("Type data: ", typeData);
    // Sign the message
    const userSignature = await account.signMessage(typeData);

    // console.log("User signature: ", userSignature);
    const deploymentData: DeploymentData = {
      class_hash: accountClassHashResponse,
      salt: starkKeyPubAX,
      unique: `${num.toHex(0)}`,
      calldata: AXConstructorCallData.map((value) => num.toHex(value)),
    };

    // console.log("Deployment data: ------ ", deploymentData);
    const encryptedPrivateKey = encryptPrivateKey(privateKeyAX, encryptKey);
    // console.log("Encrypted private key: ", encryptedPrivateKey);

    // Llamar a la API para guardar la wallet en dashboard
    const executeTransactionResponse = await fetch(`${BACKEND_URL}/chipi-wallets`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${bearerToken}`,
        'x-api-key': apiPublicKey,
      },
      body: JSON.stringify({
        apiPublicKey,
        publicKey,
        userSignature: {
          r: (userSignature as any).r.toString(),
          s: (userSignature as any).s.toString(),
          recovery: (userSignature as any).recovery
        },
        typeData,
        encryptedPrivateKey,
        deploymentData: {
          ...deploymentData,
          salt: `${deploymentData.salt}`,
          calldata: deploymentData.calldata.map(data => `${data}`),
        }
      }),
    });
    const executeTransaction = await executeTransactionResponse.json();
    console.log("Execute transaction: ", executeTransaction);

    if (executeTransaction.success) {
    return {
      success: true,
      txHash: executeTransaction.txHash,
      wallet: {
        publicKey: executeTransaction.walletPublicKey,
        encryptedPrivateKey: encryptedPrivateKey,
      } as WalletData,
      };
    } else {
      return {
        success: false,
        txHash: "",
        wallet: {
          publicKey: "",
          encryptedPrivateKey: "",
        } as WalletData,
      };
    }
  } catch (error: unknown) {
    console.error("Error detallado:", error);

    if (error instanceof Error && error.message.includes("SSL")) {
      throw new Error(
        "Error de conexión SSL. Intenta usando NODE_TLS_REJECT_UNAUTHORIZED=0 o verifica la URL del RPC"
      );
    }

    throw new Error(
      `Error creating Argent wallet: ${
        error instanceof Error ? error.message : "Unknown error"
      }`
    );
  }
};



================================================
FILE: src/core/index.ts
================================================
// src/core/index.ts
export { ChipiSDK } from './chipi-sdk';
export { createArgentWallet } from './create-argent-wallet';
export { executePaymasterTransaction } from './send-transaction-with-paymaster';
export { BACKEND_URL } from './backend-url';
export * from './types';


================================================
FILE: src/core/send-transaction-with-paymaster.ts
================================================
import { Account, Call, RpcProvider } from "starknet";
import { decryptPrivateKey } from "./lib/encryption";
import { BACKEND_URL } from "./backend-url";

export interface ExecuteTransactionParams {
  apiPublicKey: string;
  encryptKey: string;
  bearerToken: string;
  wallet: {
    publicKey: string;
    encryptedPrivateKey: string;
  }; //ClerkWallet;
  calls: Call[];
}

export const executePaymasterTransaction = async (
  params: ExecuteTransactionParams
): Promise<string> => {
  try {
    const { encryptKey, wallet, calls, apiPublicKey, bearerToken } = params;

    // Fetch the encrypted private key from clerk public metadata
    const privateKeyDecrypted = decryptPrivateKey(
      wallet.encryptedPrivateKey,
      encryptKey
    );

    if (!privateKeyDecrypted) {
      throw new Error("Failed to decrypt private key");
    }

    const provider = new RpcProvider({
      nodeUrl: "https://cloud.argent-api.com/v1/starknet/mainnet/rpc/v0.7",
    });

    const account = new Account(
      provider,
      wallet.publicKey,
      privateKeyDecrypted
    );

    // Build the type data
    const typeDataResponse = await fetch(`${BACKEND_URL}/transactions/prepare-typed-data`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${bearerToken}`,
        'X-API-Key': apiPublicKey,
      },
      body: JSON.stringify({
        publicKey: wallet.publicKey,
        calls: calls,
        accountClassHash: "0x036078334509b514626504edc9fb252328d1a240e4e948bef8d0c08dff45927f"
      }),
    });

    if (!typeDataResponse.ok) {
      const errorText = await typeDataResponse.text();
      throw new Error(`Error en la API: ${errorText}`);
    }

    const typeData = await typeDataResponse.json();

    // Sign the message
    const userSignature = await account.signMessage(typeData);
    //console.log("User signature: ", userSignature);


   
    // Execute the transaction
    const executeTransaction = await fetch(`${BACKEND_URL}/transactions/execute-sponsored-transaction`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${bearerToken}`,
        'X-API-Key': apiPublicKey,
      },
      body: JSON.stringify({
        publicKey: wallet.publicKey,
        typeData: typeData,
        userSignature: {
          r: (userSignature as any).r.toString(),
          s: (userSignature as any).s.toString(),
          recovery: (userSignature as any).recovery
        }
      }),
    });

    if (!executeTransaction.ok) {
      const errorText = await executeTransaction.text();
      throw new Error(`Error en la API de ejecución: ${errorText}`);
    }

    const result = await executeTransaction.json();
    // console.log('Resultado de la transacción:', result);
    
    if (!result.transactionHash) {
      throw new Error('La respuesta no contiene el hash de la transacción');
    }

    return result.transactionHash;
  } catch (error) {
    console.error("Error sending transaction with paymaster", error);
    throw error;
  }
};



================================================
FILE: src/core/types.ts
================================================
import { Call } from "starknet";
export interface ChipiSDKConfig {
  apiPublicKey: string;
}

export interface WalletData {
  publicKey: string;
  encryptedPrivateKey: string;
}

export interface TransferParams {
  encryptKey: string;
  wallet: WalletData;
  contractAddress: string;
  recipient: string;
  amount: string | number;
  decimals?: number;
  bearerToken: string;
}

export interface ApproveParams {
  encryptKey: string;
  wallet: WalletData;
  contractAddress: string;
  spender: string;
  amount: string | number;
  decimals?: number;
  bearerToken: string;
}

export interface StakeVesuUsdcParams {
  encryptKey: string;
  wallet: WalletData;
  amount: string | number;
  receiverWallet: string;
  bearerToken: string;
}

export interface WithdrawVesuUsdcParams {
  encryptKey: string;
  wallet: WalletData;
  recipient: string;
  amount: string | number;
  bearerToken: string;
}

export interface CallAnyContractParams {
  encryptKey: string;
  wallet: WalletData;
  contractAddress: string;
  calls: Call[];
  bearerToken: string;
}

export interface ExecuteTransactionParams {
  encryptKey: string;
  wallet: WalletData;
  contractAddress: string;
  calls: Call[];
  bearerToken: string;
}

export interface CreateWalletParams {
  encryptKey: string;
  apiPublicKey: string;
  bearerToken: string;
  nodeUrl: string;
}

export interface CreateWalletResponse {
  success: boolean;
  wallet: WalletData;
  txHash: string;
}

export interface IncrementParams {}
export type TransactionParams =
  | {
      type: "transfer" | "approve";
      params: TransferParams;
    }
  | {
      type: "wildcard";
      params: IncrementParams;
    };
export interface SimpleTransactionInput {
  pin: string;
  wallet: WalletData;
  contractAddress: string;
  calls: Call[];
}
export interface TransactionInput {
  pin: string;
  wallet: WalletData;
  calls: Call[];
}
export interface TransactionResult {
  success: boolean;
  accountAddress: string;
  encryptedPrivateKey: string;
  txHash: string;
}



================================================
FILE: src/core/lib/encryption.ts
================================================
import CryptoJS from "crypto-js";

export const encryptPrivateKey = (
  privateKey: string,
  password: string,
): string => {
  if (!privateKey || !password) {
    throw new Error("Private key and password are required");
  }

  return CryptoJS.AES.encrypt(privateKey, password).toString();
};

export const decryptPrivateKey = (
  encryptedPrivateKey: string,
  password: string,
): string | null => {
  if (!encryptedPrivateKey || !password) {
    console.error("Encrypted private key and password are required");
    return null;
  }

  try {
    const bytes = CryptoJS.AES.decrypt(encryptedPrivateKey, password);
    const decrypted = bytes.toString(CryptoJS.enc.Utf8);

    // Check if the decrypted string is empty
    if (!decrypted) {
      return null;
    }

    return decrypted;
  } catch (error) {
    console.error("Decryption failed:", error);
    return null;
  }
};



================================================
FILE: src/core/lib/index.ts
================================================
// src/core/lib/index.ts
export { encryptPrivateKey, decryptPrivateKey } from './encryption';


================================================
FILE: src/react/index.ts
================================================
// src/react/index.ts
export { ChipiProvider, useChipiContext } from './context/chipi-provider';
export * from './hooks';
export type { ChipiProviderProps } from './types';


================================================
FILE: src/react/types.ts
================================================
import type { ChipiSDKConfig, WalletData } from '../core/types';

export interface ChipiProviderProps {
  children: React.ReactNode;
  config: ChipiSDKConfig;
}

export interface StorageAdapter {
  saveWallet: (wallet: WalletData) => Promise<void>;
  getWallet?: (address: string) => Promise<WalletData | null>;
}


================================================
FILE: src/react/context/chipi-provider.tsx
================================================
import { createContext, useContext, useMemo } from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ChipiSDK } from "../../core/chipi-sdk";

export interface ChipiSDKConfig {
  apiPublicKey: string;
}

interface ChipiContextValue {
  config: ChipiSDKConfig;
  chipiSDK: ChipiSDK;
}

const ChipiContext = createContext<ChipiContextValue | null>(null);
const queryClient = new QueryClient();

export function ChipiProvider({
  children,
  config,
}: {
  children: React.ReactNode;
  config: ChipiSDKConfig;
}) {
  if (!config.apiPublicKey) {
    throw new Error("Chipi SDK apiPublicKey is required");
  }

  const chipiSDK = useMemo(() => {
    console.log("Creating new ChipiSDK instance with apiPublicKey:", config.apiPublicKey);
    return new ChipiSDK({
      apiPublicKey: config.apiPublicKey,
    });
  }, [config.apiPublicKey]);

  const contextValue = useMemo(() => ({
    config,
    chipiSDK,
  }), [config, chipiSDK]);

  return (
    <QueryClientProvider client={queryClient}>
      <ChipiContext.Provider value={contextValue}>
        {children}
      </ChipiContext.Provider>
    </QueryClientProvider>
  );
}

export function useChipiContext() {
  const context = useContext(ChipiContext);
  if (!context) {
    throw new Error("useChipiContext must be used within a ChipiProvider");
  }
  return context;
}



================================================
FILE: src/react/context/index.ts
================================================
export { 
    ChipiProvider,
    useChipiContext,
  } from './chipi-provider';


================================================
FILE: src/react/hooks/index.ts
================================================
// src/react/hooks/index.ts
export { useCreateWallet } from './use-create-wallet';
export { useTransfer } from './use-transfer';
export { useApprove } from './use-approve';
export { useStakeVesuUsdc } from './use-stake-vesu-usdc';
export { useWithdrawVesuUsdc } from './use-withdraw-vesu-usdc';
export { useCallAnyContract } from './use-call-any-contract';




================================================
FILE: src/react/hooks/use-approve.ts
================================================
import { useMutation } from "@tanstack/react-query";
import { useChipiContext } from "../context";
import { ApproveParams } from "../../core";

export function useApprove() {
  const { chipiSDK } = useChipiContext();

  const mutation = useMutation<
    string,
    Error,
    Omit<ApproveParams, "apiPublicKey">
  >({
    mutationFn: chipiSDK.approve,
  });

  return {
    approve: mutation.mutate,
    approveAsync: mutation.mutateAsync,
    approveData: mutation.data,
    isLoading: mutation.isPending,
    isError: mutation.isError,
  };
}



================================================
FILE: src/react/hooks/use-call-any-contract.ts
================================================
import { useMutation } from "@tanstack/react-query";
import { useChipiContext } from "../context";
import { CallAnyContractParams } from "../../core";

export function useCallAnyContract() {
  const { chipiSDK } = useChipiContext();

  const mutation = useMutation<
    string,
    Error,
    Omit<CallAnyContractParams, "apiPublicKey">
  >({
    mutationFn: chipiSDK.callAnyContract,
  });

  return {
    callAnyContract: mutation.mutate,
    callAnyContractAsync: mutation.mutateAsync,
    callAnyContractData: mutation.data,
    isLoading: mutation.isPending,
    isError: mutation.isError,
  };
}



================================================
FILE: src/react/hooks/use-create-wallet.ts
================================================
import { useMutation } from "@tanstack/react-query";
import { useChipiContext } from "../context";
import {  CreateWalletParams, CreateWalletResponse } from "../../core";


export function useCreateWallet() {
  const { chipiSDK } = useChipiContext();

  const mutation = useMutation<CreateWalletResponse, Error, Omit<CreateWalletParams, 'apiPublicKey' | 'nodeUrl'>>({
    mutationFn: chipiSDK.createWallet,
  });

  return {
    createWallet: mutation.mutate,
    createWalletAsync: mutation.mutateAsync,
    createWalletResponse: mutation.data,
    isLoading: mutation.isPending,
    isError: mutation.isError,
  };
}


================================================
FILE: src/react/hooks/use-stake-vesu-usdc.ts
================================================
import { useMutation } from "@tanstack/react-query";
import { useChipiContext } from "../context";
import { StakeVesuUsdcParams } from "../../core";




export function useStakeVesuUsdc() {
  const { chipiSDK } = useChipiContext();

  const mutation = useMutation<string, Error, Omit<StakeVesuUsdcParams, 'apiPublicKey'>>({
    mutationFn: chipiSDK.stakeVesuUsdc,
  });

  return {
    stake: mutation.mutate,
    stakeAsync: mutation.mutateAsync,
    stakeData: mutation.data,
    isLoading: mutation.isPending,
    isError: mutation.isError,
  };
}


================================================
FILE: src/react/hooks/use-transfer.ts
================================================
import { useMutation } from "@tanstack/react-query";
import { useChipiContext } from "../context";
import { TransferParams } from "../../core";




export function useTransfer() {
  const { chipiSDK } = useChipiContext();

  const mutation = useMutation<string, Error, Omit<TransferParams, 'apiPublicKey'>>({
    mutationFn: chipiSDK.transfer,
  });

  return {
    transfer: mutation.mutate,
    transferAsync: mutation.mutateAsync,
    transferData: mutation.data,
    isLoading: mutation.isPending,
    isError: mutation.isError,
  };
}


================================================
FILE: src/react/hooks/use-withdraw-vesu-usdc.ts
================================================
import { useMutation } from "@tanstack/react-query";
import { useChipiContext } from "../context";
import { WithdrawVesuUsdcParams } from "../../core";




export function useWithdrawVesuUsdc() {
  const { chipiSDK } = useChipiContext();

  const mutation = useMutation<string, Error, Omit<WithdrawVesuUsdcParams, 'apiPublicKey'>>({
    mutationFn: chipiSDK.withdrawVesuUsdc,
  });

  return {
    withdraw: mutation.mutate,
    withdrawAsync: mutation.mutateAsync,
    withdrawData: mutation.data,
    isLoading: mutation.isPending,
    isError: mutation.isError,
  };
}

