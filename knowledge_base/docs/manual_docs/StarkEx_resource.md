Directory structure:
└── starkware-libs-starkex-resources/
    ├── README.md
    ├── build.sh
    ├── CMakeLists.txt
    ├── LICENSE
    ├── presubmit.sh
    ├── tox.ini
    ├── .eslintrc.json
    ├── aerospike/
    │   ├── aerospike.conf
    │   └── CMakeLists.txt
    ├── committee/
    │   ├── README.md
    │   ├── build_committee_docker.sh
    │   ├── CMakeLists.txt
    │   ├── config.yml
    │   ├── docker-compose.yml
    │   ├── Dockerfile
    │   ├── integration_test.py
    │   ├── private_key.txt
    │   ├── setup.py
    │   ├── committee/
    │   │   ├── __init__.py
    │   │   ├── availability_gateway_client.py
    │   │   ├── batch_info.json
    │   │   ├── committee.py
    │   │   ├── committee_test.py
    │   │   ├── custom_validation.py
    │   │   └── dump_vaults_tree.py
    │   └── mock_availability_gateway/
    │       ├── README.md
    │       ├── CMakeLists.txt
    │       ├── config.yml
    │       ├── Dockerfile
    │       ├── setup.py
    │       └── mock_availability_gateway/
    │           ├── __init__.py
    │           ├── data.json
    │           ├── fetch_state_updates.py
    │           └── mock_availability_gateway.py
    ├── crypto/
    │   ├── CMakeLists.txt
    │   ├── setup.py
    │   └── starkware/
    │       ├── __init__.py
    │       └── crypto/
    │           ├── __init__.py
    │           └── signature/
    │               ├── __init__.py
    │               ├── asset.js
    │               ├── assets_precomputed.json
    │               ├── constant_points.json
    │               ├── fast_pedersen_hash.py
    │               ├── fast_pedersen_hash_test.py
    │               ├── key_derivation.js
    │               ├── keys_precomputed.json
    │               ├── math_utils.py
    │               ├── nothing_up_my_sleeve_gen.py
    │               ├── package.json
    │               ├── pedersen_params.json
    │               ├── rfc6979_signature_test_vector.json
    │               ├── settlement_example.json
    │               ├── signature.js
    │               ├── signature.py
    │               ├── signature_example.js
    │               ├── signature_test.py
    │               ├── signature_test_data.json
    │               ├── starkex_messages.py
    │               └── test/
    │                   ├── asset_test.js
    │                   ├── key_derivation_test.js
    │                   ├── signature_test.js
    │                   └── .eslintrc.json
    ├── stark_ex_objects/
    │   ├── README.md
    │   ├── CMakeLists.txt
    │   ├── setup.py
    │   └── starkware/
    │       ├── __init__.py
    │       ├── availability_claim.py
    │       ├── error_handling.py
    │       └── objects/
    │           ├── __init__.py
    │           ├── availability.py
    │           ├── fields.py
    │           └── state.py
    └── storage/
        ├── README.md
        ├── CMakeLists.txt
        ├── setup.py
        └── starkware/
            ├── __init__.py
            └── storage/
                ├── __init__.py
                ├── aerospike_lock.py
                ├── aerospike_storage_threadpool.py
                ├── batch_store.py
                ├── batch_store_test.py
                ├── dict_storage.py
                ├── imm_storage.py
                ├── redis_lock.py
                ├── redis_storage.py
                ├── s3_storage.py
                ├── storage.py
                ├── storage_test.py
                ├── test_utils.py
                └── merkle_tree/
                    ├── __init__.py
                    ├── merkle_tree.py
                    └── merkle_tree_test.py


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
# Stark Exchange Resources

This repo hold a collection of tools to support the Stark Exchange.
The Stark Exchange is a STARK-powered scalability engine for crypto exchanges.
It uses cryptographic proofs to attest to the validity of a batch of transactions (such as trades
and transfers) and updates a commitment to the state of the exchange on-chain.

The Stark Exchange allows exchanges to provide non-custodial trading at scale with high liquidity
and lower costs.

## Modules

1. [committee](committee/README.md) - Reference committee member service implementation
2. [crypto](crypto/README.md) - A cryptographic library for the Stark Exchange
3. [storage](storage/README.md) - A storage abstraction library
4. [stark_ex_objects](stark_ex_objects/README.md) - Various python objects used by the Stark
   Exchange

## Copyright

Copyright 2020 StarkWare Industries Ltd.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.starkware.co/open-source-license/

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions
and limitations under the License.



================================================
FILE: build.sh
================================================
#!/bin/bash
set -e

if [ $# -lt 1 ]
then
    FLAVOR="Release"
else
    FLAVOR=$1
fi

mkdir -p build/$FLAVOR
(cd build/$FLAVOR; cmake -DCMAKE_BUILD_TYPE=$FLAVOR ../..)
make -C build/$FLAVOR



================================================
FILE: CMakeLists.txt
================================================
cmake_minimum_required (VERSION 3.5)

macro(copy_files_target TARGET_NAME)
set(OUTPUT_FILES)
foreach(FILENAME ${ARGN})
  add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/${FILENAME}
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_CURRENT_SOURCE_DIR}/${FILENAME}
    ${CMAKE_CURRENT_BINARY_DIR}/${FILENAME}
    DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${FILENAME}
    COMMENT "Copying file ${FILENAME}"
  )
  set(OUTPUT_FILES ${OUTPUT_FILES} ${CMAKE_CURRENT_BINARY_DIR}/${FILENAME})
endforeach(FILENAME)

add_custom_target(${TARGET_NAME}
  ALL
  DEPENDS ${OUTPUT_FILES}
)
# Add to project virtual environment.

endmacro(copy_files_target)

# Note that PACKAGE_NAME must match the name in the package setup.py.
macro(python_package TARGET_NAME PACKAGE_NAME)
  copy_files_target(${TARGET_NAME}_copy_files ${ARGN})
  add_custom_command(
    OUTPUT ${PACKAGE_NAME}.egg-info/requires.txt
    COMMAND python3 setup.py egg_info
    DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/setup.py
    COMMENT "Generating egg_info for ${TARGET_NAME}"
  )

  add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}-0.1.zip
     # Delete the file so that will be able to check that it was actually created.
    COMMAND rm -f ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}-0.1.zip
    COMMAND python3.7 setup.py sdist --format=zip --dist-dir=${CMAKE_BINARY_DIR}/python_packages
    # Check that the file name passed to output is correct.
    COMMAND if test ! -f ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}-0.1.zip \; then ${CMAKE_COMMAND} -E cmake_echo_color --red "Bad package name: ${PACKAGE_NAME}." \; exit 1\; fi\;

    # If egg-info/requires.txt is missing create an empty one.
    COMMAND ${CMAKE_COMMAND} -E touch ${PACKAGE_NAME}.egg-info/requires.txt

    # Copy the egg-info/requires.txt.
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_CURRENT_BINARY_DIR}/${PACKAGE_NAME}.egg-info/requires.txt
    ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}.egg-info/requires.txt

    DEPENDS ${ARGN}
    COMMENT "Generating source distribution for ${TARGET_NAME}"
  )

  # The dependency makes sure that when this target is built, it also generates the corresponding source distribution .../python_packages/${PACKAGE_NAME}-0.1.zip, for every python package we have.
  add_custom_target(${TARGET_NAME} DEPENDS ${TARGET_NAME}_copy_files ${PACKAGE_NAME}.egg-info/requires.txt ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}-0.1.zip)
endmacro()

# This macro copies packages relevant to dockers into their respective folders on build
macro(python_dependency TARGET_NAME PACKAGE_NAME)
  add_custom_command(TARGET ${TARGET_NAME}
  COMMAND ${CMAKE_COMMAND} -E copy
  ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}-0.1.zip
  ${CMAKE_CURRENT_BINARY_DIR}/${PACKAGE_NAME}-0.1.zip
  # Copy the egg-info/requires.txt
  COMMAND ${CMAKE_COMMAND} -E copy
  ${CMAKE_BINARY_DIR}/python_packages/${PACKAGE_NAME}.egg-info/requires.txt
  ${CMAKE_CURRENT_BINARY_DIR}/${PACKAGE_NAME}.egg-info/requires.txt)
endmacro()

add_subdirectory(aerospike)
add_subdirectory(committee)
add_subdirectory(crypto)
add_subdirectory(stark_ex_objects)
add_subdirectory(storage)



================================================
FILE: LICENSE
================================================
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2020 StarkWare Industries Ltd.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.



================================================
FILE: presubmit.sh
================================================
#!/bin/bash
set -e

if [ $# -lt 1 ]
then
    FLAVOR="Release"
else
    FLAVOR=$1
fi

./build.sh $FLAVOR
tox -- --junitxml build/reports/$FLAVOR/pytest-starkware-public.xml

# Test JavaScript signature example.
cd crypto/starkware/crypto/signature
npm install
npm run lint
npm run test



================================================
FILE: tox.ini
================================================
[tox]
; By default tox assumes that it works on a python package (with setup.py) and installs it.
; Set skipsdist to True to skip this step.
skipsdist=True

; Virtual environment for services.
[testenv]
; Run in python3.7
basepython=python3.7
deps=
    Web3==5.2.2
    --editable={toxinidir}/committee
    --editable={toxinidir}/crypto
    --editable={toxinidir}/stark_ex_objects/
    --editable={toxinidir}/storage
    --no-cache-dir
    --force-reinstall
    --extra-index-url=https://test.pypi.org/simple/
    aerospike==4.0.0
    fastecdsa==1.7.2

    pytest-asyncio
passenv=
    USE_LOCAL_DOCKERS
commands=
    pytest {posargs}



================================================
FILE: .eslintrc.json
================================================
// Rules: https://eslint.org/docs/rules/
{
    "env": {
        "browser": true,
        "commonjs": true,
        "es6": true,
        "node": true
    },
    "extends": "eslint:recommended",
    "globals": {
        "BigInt": "readonly",
        "Atomics": "readonly",
        "SharedArrayBuffer": "readonly"
    },
    "parserOptions": {
        "ecmaVersion": 2018
    },
    "ignorePatterns": [
        "node_modules/"
    ],
    "rules": {
        "accessor-pairs": "error",
        "array-bracket-newline": [
            "error",
            "consistent"
        ],
        "array-bracket-spacing": [
            "error",
            "never"
        ],
        "array-callback-return": "error",
        "array-element-newline": [
            "error",
            "consistent"
        ],
        "arrow-body-style": [
            "error",
            "as-needed"
        ],
        "arrow-parens": [
            "error",
            "as-needed"
        ],
        "arrow-spacing": [
            "error",
            {
                "after": true,
                "before": true
            }
        ],
        "block-scoped-var": "error",
        "block-spacing": [
            "error",
            "always"
        ],
        "brace-style": [
            "error",
            "1tbs",
            {
                "allowSingleLine": false
            }
        ],
        "callback-return": "error",
        "camelcase": [
            "error",
            {
                "properties": "always"
            }
        ],
        "capitalized-comments": [
            "error",
            "always",
            {
                "ignoreInlineComments": true,
                "ignoreConsecutiveComments": true
            }
        ],
        "class-methods-use-this": "off",
        "comma-dangle": "error",
        "comma-spacing": [
            "error",
            {
                "after": true,
                "before": false
            }
        ],
        "comma-style": [
            "error",
            "last"
        ],
        "complexity": [
            "error",
            5
        ],
        "computed-property-spacing": [
            "error",
            "never"
        ],
        "consistent-return": [
            "error",
            {
                "treatUndefinedAsUnspecified": false
            }
        ],
        "consistent-this": "error",
        "curly": [
            "error",
            "all"
        ],
        "default-case": "error",
        "default-param-last": "error",
        "dot-location": [
            "error",
            "property"
        ],
        "dot-notation": [
            "error",
            {
                "allowKeywords": true
            }
        ],
        "eol-last": [
            "error",
            "always"
        ],
        "eqeqeq": [
            "error",
            "smart"
        ],
        "func-call-spacing": [
            "error",
            "never"
        ],
        "func-name-matching": "error",
        "func-names": [
            "error",
            "never",
            {
                "generators": "as-needed"
            }
        ],
        "func-style": [
            "error",
            "declaration"
        ],
        "function-call-argument-newline": [
            "error",
            "consistent"
        ],
        "function-paren-newline": [
            "error",
            "consistent"
        ],
        "generator-star-spacing": [
            "error",
            "after"
        ],
        "global-require": "off",
        "grouped-accessor-pairs": "error",
        "guard-for-in": "error",
        "handle-callback-err": "error",
        "id-blacklist": "error",
        "id-length": "off",
        "id-match": "error",
        "implicit-arrow-linebreak": [
            "error",
            "beside"
        ],
        "indent": [
            "error",
            4,
            {
                "SwitchCase": 1,
                "FunctionDeclaration": {
                    "body": 1,
                    "parameters": 2
                }
            }
        ],
        "indent-legacy": "off",
        "init-declarations": [
            "error",
            "always"
        ],
        "jsx-quotes": "error",
        "key-spacing": [
            "error",
            {
                "mode": "strict"
            }
        ],
        "keyword-spacing": [
            "error",
            {
                "after": true,
                "before": true
            }
        ],
        "line-comment-position": "off",
        "linebreak-style": [
            "error",
            "unix"
        ],
        "lines-around-comment": [
            "error",
            {
                "beforeBlockComment": true
            }
        ],
        "lines-around-directive": [
            "error",
            {
                "before": "never",
                "after": "always"
            }
        ],
        "lines-between-class-members": [
            "error",
            "always"
        ],
        "max-classes-per-file": "error",
        "max-depth": [
            "error",
            3
        ],
        "max-len": [
            "error",
            {
                "tabWidth": 4,
                "ignoreUrls": true,
                "code": 100
            }
        ],
        "max-lines": [
            "error",
            500
        ],
        "max-lines-per-function": [
            "error",
            {
                "max": 60,
                "IIFEs": true
            }
        ],
        "max-nested-callbacks": [
            "error",
            3
        ],
        "max-params": [
            "error",
            10
        ],
        "max-statements": "off",
        "max-statements-per-line": [
            "error",
            {
                "max": 1
            }
        ],
        "multiline-comment-style": "off",
        "multiline-ternary": [
            "error",
            "always-multiline"
        ],
        "new-cap": "error",
        "new-parens": "error",
        "newline-after-var": "off",
        "newline-before-return": "off",
        "newline-per-chained-call": "off",
        "no-alert": "error",
        "no-array-constructor": "error",
        "no-await-in-loop": "off",
        "no-bitwise": "off",
        "no-buffer-constructor": "error",
        "no-caller": "error",
        "no-catch-shadow": "error",
        "no-confusing-arrow": [
            "error",
            {
                "allowParens": true
            }
        ],
        "no-console": "off",
        "no-constructor-return": "error",
        "no-continue": "error",
        "no-div-regex": "error",
        "no-dupe-else-if": "error",
        "no-duplicate-imports": "error",
        "no-else-return": "error",
        "no-empty-function": "off",
        "no-eq-null": "error",
        "no-eval": "error",
        "no-extend-native": "error",
        "no-extra-bind": "error",
        "no-extra-label": "error",
        "no-extra-parens": "off",
        "no-floating-decimal": "error",
        "no-implicit-coercion": "error",
        "no-implicit-globals": "error",
        "no-implied-eval": "error",
        "no-import-assign": "error",
        "no-inline-comments": "off",
        "no-inner-declarations": [
            "error",
            "functions"
        ],
        "no-invalid-this": "error",
        "no-iterator": "error",
        "no-label-var": "error",
        "no-labels": "error",
        "no-lone-blocks": "error",
        "no-lonely-if": "error",
        "no-loop-func": "error",
        "no-magic-numbers": "off",
        "no-mixed-operators": [
            "error",
            {
                "groups": [
                    [
                        "&",
                        "|",
                        "^",
                        "~",
                        "<<",
                        ">>",
                        ">>>"
                    ],
                    [
                        "&&",
                        "||"
                    ]
                ]
            }
        ],
        "no-mixed-requires": "error",
        "no-multi-assign": "error",
        "no-multi-spaces": [
            "error",
            {
                "ignoreEOLComments": true
            }
        ],
        "no-multi-str": "error",
        "no-multiple-empty-lines": "error",
        "no-native-reassign": "error",
        "no-negated-condition": "off",
        "no-negated-in-lhs": "error",
        "no-nested-ternary": "off",
        "no-new": "error",
        "no-new-func": "error",
        "no-new-object": "error",
        "no-new-require": "error",
        "no-new-wrappers": "error",
        "no-octal-escape": "error",
        "no-param-reassign": "off",
        "no-path-concat": "off",
        "no-plusplus": "off",
        "no-process-env": "error",
        "no-process-exit": "error",
        "no-proto": "error",
        "no-restricted-globals": "error",
        "no-restricted-imports": "error",
        "no-restricted-modules": "error",
        "no-restricted-properties": "error",
        "no-restricted-syntax": "error",
        "no-return-assign": "error",
        "no-return-await": "off",
        "no-script-url": "error",
        "no-self-compare": "error",
        "no-sequences": "error",
        "no-setter-return": "error",
        "no-shadow": "error",
        "no-spaced-func": "error",
        "no-sync": "off",
        "no-tabs": "error",
        "no-template-curly-in-string": "error",
        "no-ternary": "off",
        "no-throw-literal": "error",
        "no-trailing-spaces": "error",
        "no-undef": "error",
        "no-undef-init": "off",
        "no-undefined": "off",
        "no-underscore-dangle": "error",
        "no-unmodified-loop-condition": "error",
        "no-unneeded-ternary": "error",
        "no-unused-expressions": "error",
        "no-use-before-define": [
            "error",
            {
                "variables": true,
                "functions": false,
                "classes": true
            }
        ],
        "no-useless-call": "error",
        "no-useless-computed-key": "error",
        "no-useless-concat": "error",
        "no-useless-constructor": "error",
        "no-useless-rename": "error",
        "no-useless-return": "error",
        "no-var": "error",
        "no-void": "error",
        "no-warning-comments": "warn",
        "no-whitespace-before-property": "error",
        "nonblock-statement-body-position": "error",
        "object-curly-newline": [
            "error",
            {
                "multiline": true,
                "consistent": true
            }
        ],
        "object-curly-spacing": [
            "error",
            "always",
            {
                "objectsInObjects": false
            }
        ],
        "object-shorthand": "error",
        "one-var": [
            "error",
            {
                "separateRequires": true
            }
        ],
        "one-var-declaration-per-line": "off",
        "operator-assignment": [
            "error",
            "always"
        ],
        "operator-linebreak": "error",
        "padded-blocks": [
            "error",
            "never"
        ],
        "padding-line-between-statements": "error",
        "prefer-arrow-callback": [
            "warn",
            {
                "allowNamedFunctions": true
            }
        ],
        "prefer-const": "error",
        "prefer-destructuring": [
            "error",
            {
                "object": true
            }
        ],
        "prefer-exponentiation-operator": "error",
        "prefer-named-capture-group": "off",
        "prefer-numeric-literals": "error",
        "prefer-object-spread": "error",
        "prefer-promise-reject-errors": "error",
        "prefer-reflect": "off",
        "prefer-regex-literals": "error",
        "prefer-rest-params": "error",
        "prefer-spread": "error",
        "prefer-template": "off",
        "quote-props": [
            "error",
            "as-needed"
        ],
        "quotes": [
            "error",
            "single"
        ],
        "radix": "off",
        "require-atomic-updates": "error",
        "require-await": "error",
        "require-unicode-regexp": "off",
        "rest-spread-spacing": [
            "error",
            "never"
        ],
        "semi": [
            "error",
            "always"
        ],
        "semi-spacing": [
            "error",
            {
                "after": true,
                "before": false
            }
        ],
        "semi-style": [
            "error",
            "last"
        ],
        "sort-imports": "error",
        "sort-keys": "off",
        "sort-vars": "off",
        "space-before-blocks": "error",
        "space-before-function-paren": [
            "error",
            "never"
        ],
        "space-in-parens": [
            "error",
            "never"
        ],
        "space-infix-ops": "error",
        "space-unary-ops": "error",
        "spaced-comment": [
            "error",
            "always",
            {
                "line": {
                    "exceptions": [
                        "/",
                        "-",
                        "="
                    ],
                    "markers": [
                        "/",
                        "!<"
                    ]
                },
                "block": {
                    "exceptions": [
                        "*#"
                    ],
                    "balanced": true
                }
            }
        ],
        "strict": "off",
        "switch-colon-spacing": "error",
        "symbol-description": "error",
        "template-curly-spacing": [
            "error",
            "never"
        ],
        "template-tag-spacing": "error",
        "unicode-bom": [
            "error",
            "never"
        ],
        "use-isnan": "error",
        "valid-jsdoc": "error",
        "vars-on-top": "off",
        "wrap-iife": [
            "error",
            "inside"
        ],
        "wrap-regex": "off",
        "yield-star-spacing": "error",
        "yoda": [
            "error",
            "never"
        ]
    }
}



================================================
FILE: aerospike/aerospike.conf
================================================
# Aerospike database configuration file.

# This stanza must come first.
service {
    user root
    group root
    # Number of nodes where the replica count is automatically reduced to 1.
    paxos-single-replica-limit 1
    pidfile /var/run/aerospike/asd.pid
    proto-fd-max 1024
}

logging {

    # Log file must be an absolute path.
    file /dev/null {
        context any info
    }

    # Send log messages to stdout
    console {
        context any info
    }
}

network {
    service {
        address any
        port 3000

        # Uncomment the following to set the `access-address` parameter to the
        # IP address of the Docker host. This will the allow the server to correctly
        # publish the address which applications and other nodes in the cluster to
        # use when addressing this node.
        # access-address <IPADDR>
    }

    heartbeat {

        address any
        # mesh is used for environments that do not support multicast
        mode mesh
        port 3002

        # use asinfo -v 'tip:host=<ADDR>;port=3002' to inform cluster of
        # other mesh nodes
        # mesh-seed-placeholder
        # mesh-seed-address-port aerospike-0.aerospike.as-test-1.svc.cluster.local 3002

        interval 150
        timeout 10
    }

    fabric {
        address any
        port 3001
    }

    info {
        address any
        port 3003
    }
}

namespace starkware {
    replication-factor 1
    memory-size 1G
    default-ttl 0

    storage-engine memory

    # To use file storage backing, comment out the line above and use the
    # following lines instead.
    # storage-engine device {
    #   file /opt/aerospike/data/${MY_POD_NAME}-${NAMESPACE}.dat
    #   filesize ${MEM_GB}G
    #   data-in-memory true # Store data in memory in addition to file.
    # }
}



================================================
FILE: aerospike/CMakeLists.txt
================================================
copy_files_target(stark_ex_aerospike
    aerospike.conf
)



================================================
FILE: committee/README.md
================================================
# Committee Service

**A service to validate the data availability for a Stark Exchange**

## Description
The Stark Exchange holds a state of accounts (called vaults) that are updated according to an
ordered series of transactions. It processes transactions in batches of varying sizes, based on size
and time criteria. Following each batch, a Merkle tree is computed over all vaults resulting in
a Merkle root representing the state following the batch which is eventually to be committed
on-chain. Since only the root is committed on-chain, some mechanism is required to guarantee data-availability in case the operator goes rogue.

The Stark Exchange relies on a committee to guarantee data-availability of the off-chain data.
Each committee member is responsible for keeping track of the data associated with
each root and signing an availability claim to attest to the data-availability.

The Stark Exchange operator provides the committee members access to an Availability Gateway.
The Availability Gateway allows the committee members to obtain information about new batches
and to submit signed availability claims.

A batch is uniquely identifiable by its batch_id.
The information about a new batch includes a reference batch_id and a list of (index, value) pairs
with the new values of the vaults that changed relative to the reference batch.
The service combines this information with the data from the reference batch, to compute the new
state and root.
Typically the reference batch is the immediate predecessor of the new batch. However, due to the
nature of the blockchain, it is possible that a batch created by the Stark Exchange is later
reverted and replaced by a different batch.

## Building the Committee Service
The reference committee service implementation can be compiled into a docker image
by running
```
./build.sh
```
and then running
```
docker build -f committee/Dockerfile build/Release
```

## Running the Committee Service
The docker image expects to find a `config.yaml` file in its root directory. This file should be
mounted to the docker at run time.

Service operators are expected to do the following:
The `config.yml` file should be edited to reflect the specific configuration of the Committee Service operator. In particular, this should include the following information:
- `PRIVATE_KEY_PATH` - where the private key for signing availability claims is mounted.
- `CERTIFICATES_PATH` - where the TLS certificates (`user.crt`, `user.key` and `server.crt`) for
  the Availability Gateway are mounted.
- `AVAILABILITY_GW_ENDPOINT` - The address of the Availability Gateway.

A committee member service operator is expected to run a database
and update the STORAGE section of the `config.yml` with the information required to connect to said
database. The reference implementation uses an Aerospike database.

## Publishing Committee Members Data
In the event that the Stark Exchange service malfunctions, becomes non-responsive or even malicious,
users eventually have the option to freeze it. Once frozen, a Committee member should publish the
vault data for the latest root that appears on the on-chain contract.
Exchange users can then use this data to exit the system even without the cooperation of the
Stark Exchange.
To extract this data from the database, a `dump_vaults_tree.py` script is provided herein.

## Security and Privacy Considerations
The Committee Service operator is expected to apply best practices with respect to ensuring the
security of the service which is critical to the operation of the Stark Exchange as well as
best practices for protecting the data it receives contained in the batch updates.

## Copyright
Copyright 2020 StarkWare Industries Ltd.

Licensed under the Apache License, Version 2.0 (the "License").
You may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.starkware.co/open-source-license/

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions
and limitations under the License.



================================================
FILE: committee/build_committee_docker.sh
================================================
#!/bin/bash
set -e

(cd build/Release; docker build -f committee/Dockerfile .)



================================================
FILE: committee/CMakeLists.txt
================================================
python_package(stark_ex_committee committee
    committee/__init__.py
    committee/availability_gateway_client.py
    committee/committee.py
    committee/custom_validation.py
    committee/dump_vaults_tree.py
    setup.py
)

# Copy Dockerfile.
copy_files_target(stark_ex_committee_docker
    Dockerfile
    config.yml
    private_key.txt
)

add_dependencies(stark_ex_committee_docker stark_ex_committee)
add_dependencies(stark_ex_committee_docker stark_ex_objects starkware_crypto starkware_storage)

python_dependency(stark_ex_committee_docker stark_ex_objects)
python_dependency(stark_ex_committee_docker starkware_crypto)
python_dependency(stark_ex_committee_docker starkware_storage)

add_subdirectory(mock_availability_gateway)


# Copy docker-compose.
copy_files_target(committee_test
    docker-compose.yml
)


add_dependencies(committee_test
    mock_availability_gateway_docker
    stark_ex_aerospike
    stark_ex_committee_docker
)



================================================
FILE: committee/config.yml
================================================
AVAILABILITY_GW_ENDPOINT:
  https://starkware-data-availability.com:443
VAULTS_MERKLE_HEIGHT:
  31
ORDERS_MERKLE_HEIGHT:
  63
POLLING_INTERVAL:
  1
VALIDATE_ORDERS:
  False
PRIVATE_KEY_PATH:
  /private_key.txt
# CERTIFICATES_PATH:
#   /certs

LOGGING:
  version: 1
  disable_existing_loggers: False
  formatters:
    plaintext:
      format: "[%(asctime)s] %(process)d %(levelname)s %(name)s:%(funcName)s:%(lineno)s - %(message)s"
  handlers:
    console:
      class: logging.StreamHandler
      level: DEBUG
      formatter: plaintext
      stream: ext://sys.stdout
  loggers:
    root:
      level: INFO
      handlers: [console]
    committee:
      level: DEBUG
      handlers: [console]

STORAGE:
  class: starkware.storage.aerospike_storage_threadpool.AerospikeLayeredStorage
  config:
    hosts:
      - committee-aerospike:3000
    namespace: starkware
    aero_set: starkware
    index_bits: 28



================================================
FILE: committee/docker-compose.yml
================================================
version: "3.3"
services:
  committee-aerospike:
    image: aerospike/aerospike-server:4.7.0.5
    command: ["--config-file","/etc/aerospike.conf"]
    hostname: aerospike
    ports:
      - "3000:3000"
    volumes:
      - ../aerospike/aerospike.conf:/etc/aerospike.conf:ro


  mock-availability-gateway:
    build:
      context: .
      dockerfile: mock_availability_gateway/Dockerfile
    ports:
      - "9414:9414"

  committee:
    build:
      context: ../
      dockerfile: committee/Dockerfile
    volumes:
      - ./config.yml:/config.yml:ro
      - ./private_key.txt:/private_key.txt:ro
    depends_on:
      - committee-aerospike
      - mock-availability-gateway
    environment:
      AVAILABILITY_GW_ENDPOINT: "http://mock-availability-gateway:9414"



================================================
FILE: committee/Dockerfile
================================================
FROM python:3.7
RUN apt update && apt -y install netcat python-dev libgmp3-dev && apt clean

# First install the dependencies.
COPY committee/committee.egg-info/requires.txt /app/committee/
RUN pip3 install -r /app/committee/requires.txt
RUN pip3 install web3

# Install python packages.
COPY committee/starkware_crypto-0.1.zip /app/starkware-crypto/
RUN pip3 install /app/starkware-crypto/starkware_crypto-0.1.zip
COPY committee/stark_ex_objects-0.1.zip /app/stark_ex_objects/
RUN pip3 install /app/stark_ex_objects/stark_ex_objects-0.1.zip
COPY committee/starkware_storage-0.1.zip /app/storage/
RUN pip3 install /app/storage/starkware_storage-0.1.zip

COPY committee /app/committee
RUN pip3 install /app/committee

CMD ["python3", "-u", "-m", "committee.committee"]



================================================
FILE: committee/integration_test.py
================================================
import asyncio
import csv
import logging
import os
import subprocess
import tempfile
import time

import requests
import yaml

from committee.dump_vaults_tree import dump_vaults_tree
from starkware.crypto.signature.fast_pedersen_hash import async_pedersen_hash_func
from starkware.objects.state import VaultStateFact
from starkware.storage.merkle_tree import MerkleTree
from starkware.storage.storage import Storage

logger = logging.getLogger(__name__)


async def dump_vaults_tree_test(storage_config):
    """
    The test dumps a vault tree with a specific root.
    After dumping all the data it goes over the dump and collects the information
    that is associated with a specific vault_id.
    It checks that the vault information is consistent with the hash of the corresponding leaf,
    and that the authentication path generated from the dumped data is the same
    as the authentication path generated using MerkleTree.get_authentication_path().
    """

    root = 0x0109bbc8b615885cafd7a2120e2f3c3218abde7b01a0abe5f772ab32dfe55861
    height = 31
    vault_id = 2136494259

    storage = await Storage.from_config(storage_config, logger=logger)
    tree = MerkleTree(root.to_bytes(32, 'big'), height, storage, async_pedersen_hash_func)

    nodes_file = tempfile.TemporaryFile(mode='r+')
    vaults_file = tempfile.TemporaryFile(mode='r+')
    await dump_vaults_tree(tree, nodes_file, vaults_file)

    vault_hash = None

    nodes_file.seek(0)
    reader = csv.reader(nodes_file, delimiter=',')

    index = vault_id + 2 ** height
    # Compute the indices of all the nodes in the authentication path.
    authentication_path_indices = [(index >> (height - 1 - depth)) ^ 1 for depth in range(height)]
    path = {}

    # Go over the csv file and collect the following hashes:
    # 1. vault_hash corresponding to vault_id
    # 2. hashes of nodes in the authentication path for the vault in 1.
    for row in reader:
        row_number = int(row[0])
        if row_number == index:
            vault_hash = row[1]
        if row_number in authentication_path_indices:
            path[row_number] = row[1]

    assert sorted(path.keys()) == authentication_path_indices

    vault_data = None

    vaults_file.seek(0)
    reader = csv.reader(vaults_file, delimiter=',')
    for row in reader:
        row_number = int(row[0])
        if row_number == index - 2**31:
            vault_data = VaultStateFact(int(row[1]), int(row[2]), int(row[3]))

    computed_vault_hash = (await vault_data._hash(async_pedersen_hash_func)).hex()
    assert computed_vault_hash == vault_hash,  f'{computed_vault_hash} != {vault_hash}'

    sorted_path = [root for index, root in sorted(path.items(), reverse=True)]

    # in the tree indexes are zero based.
    # while here the vaults start at offset 2**args.height.
    expected_path = [root.hex()
                     for root in await tree.get_authentication_path(index - 2 ** tree.height)]

    assert sorted_path == expected_path


def test_committee():
    """
    Tests the committee against a mock implementation of the availability verifier.
    """
    flavor = 'Release'
    build_path = os.path.join(os.path.dirname(__file__), f'../build/{flavor}')
    workdir = os.path.join(build_path, 'committee')
    report_dir = os.path.join(build_path, f'../reports/{flavor}')
    timeout = 60
    try:
        if os.environ.get('USE_LOCAL_DOCKERS') != '1':
            subprocess.check_call(['docker-compose', 'down'], cwd=workdir)
            subprocess.check_call(['docker-compose', 'build'], cwd=workdir)
            subprocess.check_call(['docker-compose', 'up', '-d'], cwd=workdir)
        start_time = time.time()
        n_batches_validated = 0
        while n_batches_validated < 3:
            time.sleep(1)
            if time.time() - start_time > timeout:
                raise TimeoutError
            try:
                resp = requests.request(
                    'GET',
                    'http://localhost:9414/availability_gateway/get_num_validated_batches')
            except requests.exceptions.ConnectionError:
                logger.info('Failed to query gateway.', exc_info=True)
                continue

            if resp.status_code != 200:
                logger.info(f'got code {resp.status_code}:, {resp.text}')
                continue

            n_batches_validated = int(resp.text)

        # Test dump_db flow after the db is initialized and before we bring it down.
        config = yaml.safe_load(open(os.path.join(workdir, 'config.yml'), 'r'))
        config['STORAGE']['config']['hosts'] = ['localhost:3000']
        asyncio.run(dump_vaults_tree_test(config['STORAGE']))

    finally:
        os.makedirs(report_dir, exist_ok=True)
        log_file = tempfile.NamedTemporaryFile(
            prefix='log_',
            suffix='.txt',
            delete=False,
            dir=report_dir)
        print(f'Writing docker logs into {os.path.abspath(log_file.name)}')
        subprocess.call(['docker-compose', 'logs', '--no-color'],
                        cwd=workdir, stdout=log_file)

        subprocess.call(['docker-compose', 'logs', 'mock_availability_gateway'], cwd=workdir)
        if os.environ.get('USE_LOCAL_DOCKERS') != '1':
            subprocess.call(['docker-compose', 'down'], cwd=workdir)



================================================
FILE: committee/private_key.txt
================================================
0xbfb1d570ddf495e378a1a85140e72d177a92637223fa540e05aaa061179f4290



================================================
FILE: committee/setup.py
================================================
from setuptools import find_packages, setup

setup(
    name='committee',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aerospike==4.0.0',
        'aioredis==1.2.0',
        'fastecdsa==1.7.2',
        'marshmallow-dataclass==7.1.0',
        'marshmallow==3.2.1',
        'PyYAML==5.1',
        'requests == 2.22.0',
    ]
)



================================================
FILE: committee/committee/__init__.py
================================================
[Empty file]


================================================
FILE: committee/committee/availability_gateway_client.py
================================================
import logging
from typing import Optional
from urllib.parse import urljoin

import requests

from starkware.objects.availability import BatchDataResponse, CommitteeSignature, StateUpdate

logger = logging.getLogger(__package__)


class BadRequest(Exception):
    def __init__(self, status_code, text):
        self.status_code = status_code
        self.text = text

    def __repr__(self):
        return f'HTTP error ocurred. Status: {str(self.status_code)}.' + \
            f' Text: {self.text}'


class AvailabilityGatewayClient:
    def __init__(self, gateway_url='http://localhost:9414/', requests_kwargs={}):
        self.gateway_url = gateway_url
        self.requests_kwargs = requests_kwargs

    def _send_request(self, send_method, uri, data=None):
        url = urljoin(self.gateway_url, uri)
        res = requests.request(send_method, url, data=data, **self.requests_kwargs)
        if res.status_code != 200:
            raise BadRequest(res.status_code, res.text)
        return res.text

    async def order_tree_height(self) -> int:
        uri = "/availability_gateway/order_tree_height"
        answer = self._send_request("GET", uri)
        return int(answer)

    async def get_batch_data(self, batch_id: int) -> Optional[StateUpdate]:
        uri = f'/availability_gateway/get_batch_data?batch_id={batch_id}'
        answer = self._send_request('GET', uri)

        return BatchDataResponse.Schema().loads(answer).update

    async def send_signature(self, batch_id: int, sig: str, member_key: str, claim_hash: str):
        encoded_signature = CommitteeSignature.Schema().dumps(CommitteeSignature(
            batch_id=batch_id, signature=sig, member_key=member_key, claim_hash=claim_hash))

        answer = self._send_request(
            'POST', f'/availability_gateway/approve_new_roots', data=encoded_signature)

        if answer != 'signature accepted':
            logger.error(f'unexpected response: {answer}')
            assert False, 'Signature was not accepted'

        logger.debug(f'Signature for batch {batch_id} was sent successfully')


================================================
FILE: committee/committee/batch_info.json
================================================
{
    "update": {
        "vault_root": "037912467b7b3cc02deec7b56829e3ae494b8d96f4e79d6ca7cc766c64d10806",
        "order_root": "000ab5b4ce84eb13d24d4dc89bc96ba10756a91cf180be92e015f7941d7e3b9d",
        "vaults": {
            "0": {
                "token": "0x0",
                "balance": "0",
                "stark_key": "0x0"
            },
            "2035282972": {
                "token": "0x2dc93a3c219fb2aa83f4eaa044b941853eaf43d86ef2dbc5b912783fcaf20c5",
                "balance": "950",
                "stark_key": "0x4e7cd30036f23c3bf1b7bd551b9c2e888590be1a6bdf24d3a44b6cebaf30b85"
            },
            "2116315985": {
                "token": "0x2dc93a3c219fb2aa83f4eaa044b941853eaf43d86ef2dbc5b912783fcaf20c5",
                "balance": "1050",
                "stark_key": "0x65be82eae31457f571757809e668c9d450a03fd96ae8b6c1c5c146ff17babfc"
            }
        },
        "orders": {
            "0": {
                "fulfilled_amount": "0"
            },
            "1": {
                "fulfilled_amount": "75"
            },
            "2": {
                "fulfilled_amount": "25"
            }
        },
        "prev_batch_id": -1
    }
}



================================================
FILE: committee/committee/committee.py
================================================
import asyncio
import concurrent
import logging
import logging.config
import os
import sys
from dataclasses import field
from typing import ClassVar, Type

import marshmallow
import yaml
from marshmallow_dataclass import dataclass
from web3 import eth

from starkware.availability_claim import hash_availability_claim
from starkware.crypto.signature.fast_pedersen_hash import pedersen_hash_func
from starkware.objects.availability import StateUpdate
from starkware.objects.fields import BytesAsHex
from starkware.objects.state import OrderStateFact, VaultStateFact
from starkware.storage.imm_storage import immediate_storage
from starkware.storage.merkle_tree import MerkleTree
from starkware.storage.storage import Storage

from .availability_gateway_client import AvailabilityGatewayClient, BadRequest
from .custom_validation import is_valid

logger = logging.getLogger(__package__)


@dataclass
class CommitteeBatchInfo():
    vaults_root: bytes = field(metadata={'marshmallow_field': BytesAsHex(required=True)})
    orders_root: bytes = field(metadata={'marshmallow_field': BytesAsHex(required=True)})
    sequence_number: int
    Schema: ClassVar[Type[marshmallow.Schema]] = marshmallow.Schema

    def serialize(self) -> bytes:
        return CommitteeBatchInfo.Schema().dumps(self).encode('ascii')

    @classmethod
    def deserialize(cls, data: bytes) -> 'CommitteeBatchInfo':
        return cls.Schema().loads(data.decode('ascii'))


class Committee:
    def __init__(self, config: dict, private_key: str, storage: Storage,
                 merkle_storage: Storage, hash_func,
                 availability_gateway: AvailabilityGatewayClient):
        self.storage = storage
        self.merkle_storage = merkle_storage
        self.hash_func = hash_func
        self.vaults_merkle_height = config['VAULTS_MERKLE_HEIGHT']
        self.orders_merkle_height = config['ORDERS_MERKLE_HEIGHT']

        self.availability_gateway = availability_gateway
        self.account = eth.Account.from_key(private_key)
        self.polling_interval = config['POLLING_INTERVAL']
        self.validate_orders = bool(config.get('VALIDATE_ORDERS', False))
        if self.validate_orders:
            logger.info('Full validation mode enabled: validating both vaults and orders.')
        else:
            logger.info('Validating only vault data-availability.')
        self.stopped = False

    def stop(self):
        self.stopped = True

    @staticmethod
    def next_batch_id_key() -> bytes:
        return 'committee_next_batch_id'.encode('ascii')

    @staticmethod
    def committee_batch_info_key(batch_id: int) -> bytes:
        return f'committee_batch_info:{batch_id}'.encode('ascii')

    async def compute_initial_batch_info(self):
        # Compute a CommitteeBatchInfo with empty Merkle trees and sequence_number == -1.
        initial_batch_id = -1
        async with immediate_storage(self.merkle_storage) as storage:
            vaults_tree, orders_tree = await asyncio.gather(
                MerkleTree.empty_tree(
                    self.vaults_merkle_height, storage, VaultStateFact.empty(),
                    self.hash_func),
                MerkleTree.empty_tree(
                    self.orders_merkle_height, storage, OrderStateFact(0), self.hash_func),
            )

            initial_batch_info = CommitteeBatchInfo(
                vaults_tree.root, orders_tree.root, sequence_number=-1).serialize()
        await self.storage.set_value(
            self.committee_batch_info_key(initial_batch_id), initial_batch_info)

    async def validate_data_availability(self, batch_id: int,
                                         state_update: StateUpdate, validate_orders: bool):
        """
        Given the state_update for a new batch, verify data availability by computing
        the roots for the new batch.

        The new roots are stored in storage along with the sequence number
        and a signed availability_claim is sent to the availability gateway.
        """

        prev_batch_info = await self.storage.get_value(
            Committee.committee_batch_info_key(state_update.prev_batch_id))
        assert prev_batch_info is not None, \
            f'Prev batch not found for batch_id {state_update.prev_batch_id}'

        logger.info(f'Processing batch {batch_id}')
        logger.info(f'Using batch {state_update.prev_batch_id} as reference')

        prev_batch_info = CommitteeBatchInfo.deserialize(prev_batch_info)

        # Task to compute the new vault root.
        async def compute_vault_root(storage):
            vault_tree = MerkleTree(prev_batch_info.vaults_root, self.vaults_merkle_height,
                                    storage, self.hash_func)
            vault_tree = await vault_tree.update(state_update.vaults.items())
            return vault_tree.root.hex()

        # Task to compute the new order root.
        async def compute_order_root(storage):
            order_tree = MerkleTree(prev_batch_info.orders_root, self.orders_merkle_height,
                                    storage, self.hash_func)
            order_tree = await order_tree.update(state_update.orders.items())
            return order_tree.root.hex()

        # Verify consistency of data with roots.
        async with immediate_storage(self.merkle_storage) as storage:
            if validate_orders:
                vault_root, order_root = await asyncio.gather(
                    compute_vault_root(storage), compute_order_root(storage))
                assert vault_root == state_update.vault_root, 'vault root mismatch'
                assert order_root == state_update.order_root, 'order root mismatch'
                logger.info(f'Verified vault root: 0x{state_update.vault_root}')
                logger.info(f'Verified order root: 0x{state_update.order_root}')
            else:
                vault_root = await compute_vault_root(storage)
                assert vault_root == state_update.vault_root, 'vault root mismatch'
                logger.info(f'Verified vault root: 0x{state_update.vault_root}')
                logger.info(f'Blindly signing order root: 0x{state_update.order_root}')

            batch_info = CommitteeBatchInfo(  # type: ignore
                bytes.fromhex(state_update.vault_root), bytes.fromhex(state_update.order_root),
                prev_batch_info.sequence_number + 1)

        await self.storage.set_value(
            self.committee_batch_info_key(batch_id), batch_info.serialize())

        # In StarkEx version 4.5, the height of the order tree has changed. For an old committee
        # (i.e. a committee from version 4.0 or below) to work with a version 4.5 backend, the order
        # tree height must be checked against the availability gateway, and possibly changed.
        # If the configured height doesn't match the height sent in response from the availability
        # gateway, assert that the order tree is not validated (self.validate_orders must be False
        # to swap order tree heights, otherwise the computed order root is incorrect anyway).
        # This patch doesn't affect the calculation of the order tree root, only the `trades_height`
        # used for signing the batch. Therefore, the patch relies on the committee trusting the
        # order root sent from the AvailabilityGateway (This means that it will only work if the
        # committee is not validating orders).
        # This patch will be deleted in the version 4.5 committee.
        logger.info("Trying to fetch trades height from the availability gateway")
        # If the API of order_tree_height exists in the Availability Gateway, use it. Otherwise,
        # use ORDERS_MERKLE_HEIGHT from the config (this can happen if the SE
        # Availability Gateway is using an old SE version which doesn't have the
        # order_tree_height API).
        trades_height = self.orders_merkle_height
        try:
            trades_height = await self.availability_gateway.order_tree_height()
            logger.info(
                f"Trades height received from the Availability Gateway is {trades_height}. The "
                f"trades height which is defined in the config is {self.orders_merkle_height}."
            )
            if self.orders_merkle_height != trades_height:
                assert not validate_orders, (
                    f"validate_orders is {validate_orders}, but configured trades height "
                    f"{self.orders_merkle_height} is not equal to response from the availability "
                    f"gateway ({trades_height}). This indicates that the root of the order "
                    f"tree was computed incorrectly and the claim will not be approved by the "
                    f"availability gateway, so there is no point in signing and sending the "
                    f"signature."
                )
        except BadRequest:
            pass

        logger.info(f'Signing batch with sequence number {batch_info.sequence_number}')

        availability_claim = hash_availability_claim(
            batch_info.vaults_root, self.vaults_merkle_height, batch_info.orders_root,
            trades_height, batch_info.sequence_number)
        signature = eth.Account._sign_hash(availability_claim, self.account.key).signature.hex()
        return signature, availability_claim.hex()

    async def run(self):
        next_batch_id = await self.storage.get_int(Committee.next_batch_id_key())
        if next_batch_id is None:
            await self.compute_initial_batch_info()
            next_batch_id = 0
            await self.storage.set_int(Committee.next_batch_id_key(), next_batch_id)

        while not self.stopped:
            try:
                availability_update = await self.availability_gateway.get_batch_data(next_batch_id)
                if availability_update is None:
                    logger.info(f'Waiting for batch {next_batch_id}')
                    await asyncio.sleep(self.polling_interval)
                    continue
                assert await is_valid(availability_update), 'Third party validation failed.'
                signature, availability_claim = await self.validate_data_availability(
                    next_batch_id, availability_update, self.validate_orders)
                await self.availability_gateway.send_signature(
                    next_batch_id, signature, self.account.address, availability_claim)
                next_batch_id += 1
                await self.storage.set_int(Committee.next_batch_id_key(), next_batch_id)
            except Exception:
                logger.error('Got an exception:', exc_info=True)
                await asyncio.sleep(self.polling_interval)


async def main():
    config = yaml.safe_load(open('/config.yml', 'r'))
    private_key_path = os.environ.get(
        'PRIVATE_KEY_PATH', config.get('PRIVATE_KEY_PATH', '/private_key.txt'))
    with open(private_key_path, 'r') as private_key_file:
        # Read private_key from file (remove '\n' from end of line).
        private_key = private_key_file.read().rstrip()
    logging.config.dictConfig(config.get('LOGGING', {}))
    storage = await Storage.from_config(config.get('STORAGE'), logger=logger)

    availability_gw_endpoint = os.environ.get(
        'AVAILABILITY_GW_ENDPOINT', config.get('AVAILABILITY_GW_ENDPOINT'))

    certificates_path = os.environ.get(
        'CERTIFICATES_PATH', config.get('CERTIFICATES_PATH'))

    requests_kwargs = {}
    if certificates_path is not None:
        requests_kwargs = {'cert': (os.path.join(certificates_path, 'user.crt'),
                                    os.path.join(certificates_path, 'user.key')),
                           'verify': os.path.join(certificates_path, 'server.crt')}

    availability_gateway = AvailabilityGatewayClient(
        availability_gw_endpoint, requests_kwargs=requests_kwargs)
    logger.info(f'Using {availability_gw_endpoint} as an availability gateway')

    workers = int(os.environ.get('HASH_WORKERS', os.cpu_count()))
    logger.info(f'Using {workers} hashing process')

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as pool:
        async def async_hash_func(x, y):
            return await asyncio.get_event_loop().run_in_executor(pool, pedersen_hash_func, x, y)
        committee = Committee(
            config=config,
            private_key=private_key,
            storage=storage,
            merkle_storage=storage,
            hash_func=async_hash_func, availability_gateway=availability_gateway)
        await committee.run()


if __name__ == '__main__':
    sys.exit(asyncio.run(main()))


================================================
FILE: committee/committee/committee_test.py
================================================
import json
import os

import pytest

from starkware.crypto.signature.fast_pedersen_hash import async_pedersen_hash_func
from starkware.objects.availability import BatchDataResponse
from starkware.storage.test_utils import MockStorage

from .committee import Committee


ORDER_TREE_HEIGHT = 63


class AvailabilityGatewayClientMock:
    def __init__(self):
        pass

    async def order_tree_height(self) -> int:
        return ORDER_TREE_HEIGHT


@pytest.fixture
def committee():
    config = {
        'VAULTS_MERKLE_HEIGHT': 31,
        'ORDERS_MERKLE_HEIGHT': ORDER_TREE_HEIGHT,
        'POLLING_INTERVAL': 1,
    }

    return Committee(
        config=config,
        private_key='0xbfb1d570ddf495e378a1a85140e72d177a92637223fa540e05aaa061179f4290',
        storage=MockStorage(),
        merkle_storage=MockStorage(),
        hash_func=async_pedersen_hash_func,
        availability_gateway=AvailabilityGatewayClientMock())


@pytest.fixture
def state_update():
    # batch_info.json is the batch availability data for batch-0 from end_to_end_test.
    # To generate this file:
    # - Run end_to_end_test.
    # - While the test is running, use curl to call get_batch_data for batch_id 0:
    #   curl localhost:9414/availability_gateway/get_batch_data?batch_id=0
    # - Save the response.
    batch_info_file = os.path.join(os.path.dirname(__file__), 'batch_info.json')
    with open(batch_info_file) as fp:
        batch_info = fp.read()
    state_update = BatchDataResponse.Schema().loads(batch_info).update
    return state_update


@pytest.fixture
def expected_signature():
    # The expected signature on the roots in the used config file.
    return '0xbfaa70666e1dcb21fe92014e4f0b8ff263a582b592855a7fd566d7f468aea0457' \
        '26663fbf723fc53ad33dbb949c72030fbd38bbed05ca53aebbe1b03043fe72e1b'


@pytest.mark.asyncio
async def test_initialization(committee):
    """
    Test committee initialization.
    """
    assert await committee.storage.get_value(committee.committee_batch_info_key(-1)) is None
    assert await committee.storage.get_int(Committee.next_batch_id_key()) is None
    await committee.compute_initial_batch_info()
    batch_info = json.loads(
        await committee.storage.get_value(committee.committee_batch_info_key(-1)))
    assert batch_info['sequence_number'] == -1
    assert batch_info['vaults_root'] == \
        '0075364111a7a336756626d19fc8ec8df6328a5e63681c68ffaa312f6bf98c5c'
    assert batch_info['orders_root'] == \
        '01bb0b0bdb803c733cf692a324a31e8e7749a9fdfb597d74e71c604795e659ed'


@pytest.mark.asyncio
@pytest.mark.parametrize('validate_orders', [True, False])
@pytest.mark.parametrize('valid_vault_root', [True, False])
@pytest.mark.parametrize('valid_order_root', [True, False])
async def test_validate_data_availability(committee, state_update, expected_signature,
                                          validate_orders, valid_vault_root, valid_order_root):
    """
    Test committee validate_data_availability().
    """
    await committee.compute_initial_batch_info()

    # Corrupt vault data if needed.
    if not valid_vault_root:
        state_update.vaults.popitem()

    # Corrupt order data if needed.
    if not valid_order_root:
        state_update.orders.popitem()

    if (not valid_vault_root) or (validate_orders and not valid_order_root):
        with pytest.raises(AssertionError, match='root mismatch'):
            await committee.validate_data_availability(0, state_update, validate_orders)

    else:
        signature, _ = await committee.validate_data_availability(0, state_update, validate_orders)
        assert signature == expected_signature



================================================
FILE: committee/committee/custom_validation.py
================================================
from starkware.objects.availability import StateUpdate


async def is_valid(state_update: StateUpdate) -> bool:
    """
    A hook for third parties to validate the state_update before signing the new root.
    """
    return True



================================================
FILE: committee/committee/dump_vaults_tree.py
================================================
import argparse
import asyncio
import csv
import sys
from typing import TextIO

import yaml

from starkware.crypto.signature.fast_pedersen_hash import async_pedersen_hash_func
from starkware.objects.state import VaultStateFact
from starkware.storage.merkle_tree import MerkleTree
from starkware.storage.storage import Storage


def parse_args():
    """
    Sets possible flags of arguments and parse the arguments accordingly
    Returns a dictionary with the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="""\
Dumps a vaults tree from the database.

The output is composed of two csv files.
A nodes file and a vaults file.
The structure of the nodes file is:
"index node_hash"
where index is the index of the node in a "binary tree in array represention",
i.e. 2**(node_layer) + node_index_in_layer.

The structure of the vaults file is:
"vault_id stark_key token_id balance"
""")
    parser.add_argument('--root', type=str, default=None,
                        help='Root of vaults Merkle tree')
    parser.add_argument('--height', type=int, default=31, help='Height of vaults Merkle Tree')
    parser.add_argument('--nodes_file', type=str,
                        help='Name of the output nodes csv file', required=True)
    parser.add_argument('--vaults_file', type=str,
                        help='Name of the output vaults csv file', required=True)
    parser.add_argument('--config_file', type=str, default=None,
                        help='path to config file with storage configuration')

    args = parser.parse_args()

    return args


async def dump_vaults_tree(tree: MerkleTree, nodes_file: TextIO, vaults_file: TextIO):
    """
    Dump 'tree' into the given output files.
    """
    empty_trees = await MerkleTree.empty_tree_roots(
        tree.height, VaultStateFact(0, 0, 0), tree.hash_func)

    nodes_writer = csv.writer(nodes_file, delimiter=',')
    vaults_writer = csv.writer(vaults_file, delimiter=',')

    # Traverse the tree in DFS manner,
    # obtaining data from leaves, and ignoring empty subtrees.
    async for index, node in tree.dfs(exclude_set=set(empty_trees)):
        data = node.root.hex()
        nodes_writer.writerow([index, data])

        if node.height == 0 and node.root != empty_trees[0]:
            data = await VaultStateFact.get(tree.storage, node.root)
            vault_id = index - 2 ** tree.height
            vaults_writer.writerow(
                [vault_id, data.stark_key, data.token, data.balance])


async def main():
    args = parse_args()

    if args.config_file:
        config = yaml.safe_load(open(args.config_file))
    else:
        # default configuration assuming port forwarding.
        config = yaml.safe_load("""\
STORAGE:
    class: starkware.storage.aerospike_storage_threadpool.AerospikeLayeredStorage
    config:
        hosts:
        - localhost:3000
        namespace: starkware
        aero_set: starkware
        index_bits: 28
    """)

    storage = await Storage.from_config(config['STORAGE'])

    root_as_int = int(args.root, 16)
    tree = MerkleTree(root_as_int.to_bytes(32, 'big'), args.height,
                      storage, async_pedersen_hash_func)

    with open(args.nodes_file, 'w') as nodes_file, open(args.vaults_file, 'w') as vaults_file:
        await dump_vaults_tree(tree, nodes_file, vaults_file)


if __name__ == '__main__':
    sys.exit(asyncio.run(main()))



================================================
FILE: committee/mock_availability_gateway/README.md
================================================
# Mock Availability Gateway Service

**A Mock of the Gateway Service Providing availability data for Committee members**



================================================
FILE: committee/mock_availability_gateway/CMakeLists.txt
================================================
python_package(mock_availability_gateway mock_availability_gateway
    mock_availability_gateway/__init__.py
    mock_availability_gateway/data.json
    mock_availability_gateway/mock_availability_gateway.py
    README.md
    setup.py
)

# Copy Dockerfile.
copy_files_target(mock_availability_gateway_docker
    config.yml
    Dockerfile
)

python_dependency(mock_availability_gateway_docker stark_ex_objects)
python_dependency(mock_availability_gateway_docker mock_availability_gateway)

add_dependencies(mock_availability_gateway_docker stark_ex_objects)
add_dependencies(mock_availability_gateway_docker mock_availability_gateway)



================================================
FILE: committee/mock_availability_gateway/config.yml
================================================
LOGGING:
  version: 1
  disable_existing_loggers: False
  formatters:
    plaintext:
      format: "[%(asctime)s] %(process)d %(levelname)s %(name)s:%(funcName)s:%(lineno)s - %(message)s"
  handlers:
    console:
      class: logging.StreamHandler
      level: DEBUG
      formatter: plaintext
      stream: ext://sys.stdout
  loggers:
    root:
      level: INFO
      handlers: [console]
    mock_availability_gateway:
      level: DEBUG
      handlers: [console]



================================================
FILE: committee/mock_availability_gateway/Dockerfile
================================================
FROM python:3.7
RUN apt update && apt -y install netcat && apt clean


# First install the dependencies.
COPY mock_availability_gateway/mock_availability_gateway.egg-info/requires.txt /app/mock_availability_gateway/
RUN pip3 install -r /app/mock_availability_gateway/requires.txt

COPY starkware_storage-0.1.zip /app/storage/
RUN pip3 install /app/storage/starkware_storage-0.1.zip
COPY mock_availability_gateway/stark_ex_objects-0.1.zip /app/stark_ex_objects/
RUN pip3 install /app/stark_ex_objects/stark_ex_objects-0.1.zip

COPY mock_availability_gateway/mock_availability_gateway-0.1.zip /app/mock_availability_gateway/
RUN pip3 install /app/mock_availability_gateway/mock_availability_gateway-0.1.zip

COPY mock_availability_gateway/config.yml /

CMD ["python3", "-u", "-m", "mock_availability_gateway.mock_availability_gateway"]



================================================
FILE: committee/mock_availability_gateway/setup.py
================================================
from os import path

from setuptools import find_packages, setup

# Reads the contents of your README file.
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mock_availability_gateway',
    version='0.1',
    author='StarkWare Industries',
    author_email='info@starkware.co',
    url='https://starkware.co',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.6.2',
        'PyYAML==5.1',
        'Web3==5.2.2',
    ],
    package_data={
        '': ['data.json']
    },
    long_description=long_description,
)



================================================
FILE: committee/mock_availability_gateway/mock_availability_gateway/__init__.py
================================================
[Empty file]


================================================
FILE: committee/mock_availability_gateway/mock_availability_gateway/data.json
================================================
[
    {
        "update": {
            "order_root": "01bb0b0bdb803c733cf692a324a31e8e7749a9fdfb597d74e71c604795e659ed",
            "prev_batch_id": -1,
            "vaults": {
                "0": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "163364768": {
                    "stark_key": "0x7fd933937901b2f45fde6352a19822cfc6f71ff5c0d6422adf40cb3c91d9abd",
                    "balance": "778816",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "174166142": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "189930935": {
                    "stark_key": "0x26912111620500e8d49b186c57f06ea25a61cbd9a405d8496f91d5787e13b4b",
                    "balance": "220709",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "437206568": {
                    "stark_key": "0x65d30058ad6ffab2df33bfd9a1dcef46edfc38508c8d1f156a6a5e933bc95dd",
                    "balance": "327803",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "441864402": {
                    "stark_key": "0x7cdbd3f7394ddaad523b4d99fd501aa4d99adc0da3a19cd420d33cc360d3b78",
                    "balance": "554549",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "501687328": {
                    "stark_key": "0x30bcad634bdd260016b2e039477376beb65ee1553295494fb4af7d10eca47e8",
                    "balance": "484856",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "514475460": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "549223251": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "575420282": {
                    "stark_key": "0x39d2ef87fd6ce47c505d350287bd0598a405fda9b2b9618a0313cf100b05aba",
                    "balance": "501805",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "586633181": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "836715273": {
                    "stark_key": "0x739076b8a77d1e9e962a5d12caae4002111a1dff7611d1f8d248d2a15aa05bc",
                    "balance": "474301",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "904585146": {
                    "stark_key": "0x519ffa9620c8fe513247b3a1587b970b1b2b1d8c0f420ab659142df16ef6b59",
                    "balance": "879860",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "941735225": {
                    "stark_key": "0x54fdb529da4050062844c15992f82694f0e94865e5dabb2a1c345e0d7f9247b",
                    "balance": "642784",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "950617251": {
                    "stark_key": "0x1f6bc061bb2229ae3dd113f306d3bcc0c4a59901cdfbd4df3a8c807dd1b8077",
                    "balance": "104877",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "973775219": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "983151349": {
                    "stark_key": "0x47e80f7aaa325757eb84bc94a22603e72a430af16a103542730a50b00d2411f",
                    "balance": "401177",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "1023248543": {
                    "stark_key": "0x72d58f00061fdd632acd6f59709f403529f48dd89c686bf33d566e0cbb5ae22",
                    "balance": "871691",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "1167284707": {
                    "stark_key": "0x41679198cb6321f526b1a5cfb70fc13d9e4bbbdac73ff6122eb650a4ab3fd1c",
                    "balance": "985869",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "1188486980": {
                    "stark_key": "0x61de80ba9f22ea84be191578a50f8f6f78be263de2e07056def365c59aedeca",
                    "balance": "817140",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "1228915337": {
                    "stark_key": "0x2a4aad530362806fc6670fba14f1f46291000aaa3656d271b1eede7ccc0daeb",
                    "balance": "137530",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "1347396059": {
                    "stark_key": "0x1a37e385b06c0e377fd196a522d2afbb7f30e526a060700617e5016b1ded505",
                    "balance": "263549",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "1536550913": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1654354424": {
                    "stark_key": "0xeb932098d133926e0be33628450b0246c4b0c1a5a75aa773d1af2725cf6d5d",
                    "balance": "618293",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "1664604506": {
                    "stark_key": "0x38f1a3581b64aca961afb65b862b326c4adc2c738147826d1391d66ab678314",
                    "balance": "891112",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "1789689921": {
                    "stark_key": "0x22dbeebdb406da3534535a5b44bb4151ce6be6d65470ec5385552fda532c869",
                    "balance": "98120",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "1807096546": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1914335570": {
                    "stark_key": "0x34aedc392f91014fb8d2be5d5617924073eadbc9c94257dbad5c082ad9496ed",
                    "balance": "239936",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "2127576341": {
                    "stark_key": "0x3a30942929f8c644a85f110fe6712f00c38e364d27ab1ac13ef0324d50c0a1a",
                    "balance": "324462",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "2136494259": {
                    "stark_key": "0x139e3b66720f8b5b9eed44f12e08f908c5cfd4926a8e19cd114cf5cfc4a4fd6",
                    "balance": "595993",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "2142119466": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                }
            },
            "orders": {
                "3065896435020512722": {
                    "fulfilled_amount": "0"
                },
                "4293697043586109717": {
                    "fulfilled_amount": "0"
                }
            },
            "vault_root": "0109bbc8b615885cafd7a2120e2f3c3218abde7b01a0abe5f772ab32dfe55861"
        }
    },
    {
        "update": {
            "order_root": "01bb0b0bdb803c733cf692a324a31e8e7749a9fdfb597d74e71c604795e659ed",
            "prev_batch_id": 0,
            "vaults": {
                "0": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "23336622": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "46140315": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "276040893": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "299239568": {
                    "stark_key": "0x412e1299a70e646b076cab5848c9fe1c04b6c04a2cf14cbd172119a76904b7d",
                    "balance": "285068",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "347544182": {
                    "stark_key": "0x3ee70f60fe5474d04c2e29af14b051a65c9a584b261f8d0749879524b4d9632",
                    "balance": "437053",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "401973587": {
                    "stark_key": "0x2535b8b6112e7f21c078806c122210a2326976f4476bc3d4e98b63287b4d4f6",
                    "balance": "949877",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "431343866": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "441024512": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "453191935": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "500382747": {
                    "stark_key": "0x1f6bc061bb2229ae3dd113f306d3bcc0c4a59901cdfbd4df3a8c807dd1b8077",
                    "balance": "687204",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "539389076": {
                    "stark_key": "0x4bf18bca57035cdb43f934118f28cce7d43609d78d63c3c42d90168aedcc1a7",
                    "balance": "984413",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "719980585": {
                    "stark_key": "0xd149f738c56e86078e3bd98a65331bda26df7e0f18c91f170ee56b5df00164",
                    "balance": "574384",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "785391346": {
                    "stark_key": "0x4db9898588720deb2b00a98fdeef4474b83f944bce466e71ff5204f126b67e8",
                    "balance": "403462",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "839508379": {
                    "stark_key": "0x577ff5622fec8336f1e02e39e867a81107527cca90b90962541db980b8953dd",
                    "balance": "803486",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "861088488": {
                    "stark_key": "0x17f753a4850703d0be93f167b15ed2094415bcb88cc4daf6e15743ab7e9e3dd",
                    "balance": "559939",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "926820487": {
                    "stark_key": "0x237fb724660d43c48c77b439501e5de3d02aeab2c904b327c4fe3649189bd31",
                    "balance": "651537",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "1275543963": {
                    "stark_key": "0x6e6fcb5b33abe14f15c7511e13fa4334f8ca18a464f08a1ae2a7ee86de9f760",
                    "balance": "359876",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "1500105667": {
                    "stark_key": "0x7720f939197edfb8d58aea4bb1f6d2a6543fd6203d258bf729cf137d988d658",
                    "balance": "48023",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "1527174464": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1548566155": {
                    "stark_key": "0x3b4b63c8aa167b379b8a16fba2bac1ecddcb4a9a761627e8996ddbedcda987d",
                    "balance": "399694",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "1583357861": {
                    "stark_key": "0x53c523080bd5b6b8a138aa9c558a5235247a6467aff423642ecc15c4c73a847",
                    "balance": "67159",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "1634414538": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1803793808": {
                    "stark_key": "0x6b54a9e274c84ad485e31ce1e4ee60b1653351594b35fe50218d70b87057325",
                    "balance": "455380",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "1824646357": {
                    "stark_key": "0x4a1ae3bb39a313a06c59fc8c666613588c2e998cec14190b6384bea9976725f",
                    "balance": "126001",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "1852075918": {
                    "stark_key": "0x83d0ac4bf8476b6afa4dc44e302faf2d7cfb0d8822604d639d03873d7ba4e7",
                    "balance": "147129",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "1998515754": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "2020839867": {
                    "stark_key": "0xe176e182ae592d7e719a045a55b56b0071c42a976ac5c17604ddff280c0e28",
                    "balance": "755985",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "2035521216": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "2100504300": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "2128718036": {
                    "stark_key": "0x15ee3e52e5355d8ac148d99f99c79d935b040977e972dd2d0d1d639859cad3a",
                    "balance": "77436",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                }
            },
            "orders": {
                "3065896435020512722": {
                    "fulfilled_amount": "0"
                },
                "4293697043586109717": {
                    "fulfilled_amount": "0"
                }
            },
            "vault_root": "0298df9f3babf341237de93fdad83825cc0c25dadddf7ca15bcc596ff55bdea0"
        }
    },
    {
        "update": {
            "order_root": "01bb0b0bdb803c733cf692a324a31e8e7749a9fdfb597d74e71c604795e659ed",
            "prev_batch_id": 1,
            "vaults": {
                "0": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "55463528": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "87556131": {
                    "stark_key": "0x3db8d94a5f392bf0aacc6ff3f8385dad7d89f6931854e6701bb8ffc3160150",
                    "balance": "1017186",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "154507097": {
                    "stark_key": "0x139e3b66720f8b5b9eed44f12e08f908c5cfd4926a8e19cd114cf5cfc4a4fd6",
                    "balance": "668969",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "465417770": {
                    "stark_key": "0x83b46cf9d44ae5e639e5691365c2b9f6d966530d70b42520eb3838ca4ad066",
                    "balance": "655168",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "474039420": {
                    "stark_key": "0x5e1b85857f9354020b4d99a9b38cfc1d6b3a4c2ca6f5b58832a01a58d5ce8bb",
                    "balance": "389528",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "729542194": {
                    "stark_key": "0x49c4d4e091c519970964e92edc6f63092626bb18f4d11c6456beb7e8442cfa4",
                    "balance": "923926",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "772966198": {
                    "stark_key": "0x3c533f226a75c105c05660a8f87d787a96c110309c01a9b55b12edf56b5d952",
                    "balance": "19275",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "849856347": {
                    "stark_key": "0x4fe0767647cf67b9b6d3f34f98d36c019becf99511ad35760f59b4bd068f402",
                    "balance": "831856",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "863243998": {
                    "stark_key": "0x5669b5a5cd3b5f81245598e36372b611b82efd8afe53c360fd1ff9be4332ae3",
                    "balance": "792883",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "931258958": {
                    "stark_key": "0x58b6699c3329f3f9bb039205830e17deacf3d0c3af19acc84eacf6c64b0c17b",
                    "balance": "567473",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "937243158": {
                    "stark_key": "0x7ef0d8ae039128778d97ad4949268b5d17b824db901cde80e7636ca36ba28e4",
                    "balance": "355447",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "997658268": {
                    "stark_key": "0x3ae3974bd34a3db83f7e50437246648d9c9a93d7df4ab0c618394099b57b4d7",
                    "balance": "691573",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "1016904168": {
                    "stark_key": "0x53feb21390a51001eaa298f1297bfc0d07f2bb3b64196d26c373a9b1ed1c873",
                    "balance": "886445",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "1045486264": {
                    "stark_key": "0x139971627f304f296861e79707e0c55d93636a77377ea23c5822cfe2971c5e0",
                    "balance": "503722",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "1234110914": {
                    "stark_key": "0x3b11156c78c315233bbaa368941ecfef7435bfebd22267c68e4d6f1e502f3b1",
                    "balance": "107347",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "1322449039": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1333354591": {
                    "stark_key": "0x7a3300534cb8a3a9a6290e8993e8be1f126144d13d01b0533df21da2a14644",
                    "balance": "906986",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "1336964013": {
                    "stark_key": "0x19e4657ba39888ea8d59c777782ed0ff07d0a82050eec910bb3e2199bd6d21e",
                    "balance": "124713",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "1445387365": {
                    "stark_key": "0x2a17b44c1e36da4d0587d88ff7bc5d00069efd74829793ec651dfc5d40287e3",
                    "balance": "24246",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "1456387094": {
                    "stark_key": "0x33618442e52aa32b5993bb3d606857579314c665bda7438308918bf69fc9cd3",
                    "balance": "531499",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "1503086760": {
                    "stark_key": "0x14121d041c83f19740f83a9a491766ad8a5bcb98d515f1fc9c4695e4dc99bb6",
                    "balance": "165271",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "1525771145": {
                    "stark_key": "0x6dd7ac0ec1c06d51abded1b2dc7cfd5f2d1296f2d5ca513f2a04ff1787ed18c",
                    "balance": "182469",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "1570940899": {
                    "stark_key": "0x638f11ed3598ed07952a306f3e7668d27dc9bed6f158021dfc5c0639184a734",
                    "balance": "438788",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "1664504721": {
                    "stark_key": "0x45e7029e9b5d891b64e8b0f3bdf7ac5b78d5febd61db9ba9a95eaa4c038dc05",
                    "balance": "705320",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "1685646035": {
                    "stark_key": "0x13e0f4a4191922ffac7174e10b8d1e409c24b7dc62d19d35855a9024e68acab",
                    "balance": "710058",
                    "token": "0x35220ed97e41f78be99e11002d64a30d74b9e2085ae0843deded0afc356ca73"
                },
                "1693049631": {
                    "stark_key": "0x17b066f15d57c9c8049591f62f7a724ff7562fb720c3a7098dea022b8315bb6",
                    "balance": "989041",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "1946053018": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1966632522": {
                    "stark_key": "0x5c9bd9f194783522e1338b3f15aefb2744e25beb460a8ca59969edd0e24c932",
                    "balance": "287540",
                    "token": "0x33cb0c9534932ef26d3fbde512ae8b94705b53f5a7d4693e1b76b29012f1f17"
                },
                "1977484140": {
                    "stark_key": "0x742ad63bdc41ffecdb27c220fc63fef0e19398814ea53358f228faf8b99f8e7",
                    "balance": "1652",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "1980501468": {
                    "stark_key": "0x3b4b63c8aa167b379b8a16fba2bac1ecddcb4a9a761627e8996ddbedcda987d",
                    "balance": "871546",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                }
            },
            "orders": {
                "3065896435020512722": {
                    "fulfilled_amount": "0"
                },
                "4293697043586109717": {
                    "fulfilled_amount": "0"
                }
            },
            "vault_root": "0212c156aeb123b90786e0d85f01775d5803378d21c6d0971bc74d4bec489671"
        }
    },
    {
        "update": {
            "order_root": "02a55f4db8f5cb217c3d58cc4b760827cd6d700f88bfc19d1091494e420ef91e",
            "prev_batch_id": 2,
            "vaults": {
                "64712": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "263212": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "795986": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "853267": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1404043": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "1576021": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "2573624": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "2764083": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "3860414": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "4236473": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "5625893": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "5805258": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "6198597": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "6206165": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "6363196": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "6877740": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "7109579": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "8991824": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "9509325": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "9854435": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "9912485": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "11261275": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "11746646": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "12580601": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "12689525": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "13500356": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "13772749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "15158190": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "16092842": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "16670893": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "17207162": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "17759016": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "18902773": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "19147836": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "19404519": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "21820530": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "23077749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "23143788": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "23336622": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "23867745": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "23909216": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "25180279": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "25961357": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "26122928": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "27076472": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "28309933": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "29523938": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "30556038": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "31292172": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "31378688": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "34554770": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "34662059": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "37151903": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "38004458": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "39394829": {
                    "stark_key": "0x387acd43fe2fb574ac3a9b462095423bddb75528c5e3bb39128285baddc9d5e",
                    "balance": "100037",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "39615585": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "41337292": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "41493763": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "42432857": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "42498147": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "42702973": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "42827413": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "43166655": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "43328292": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "45366089": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "46392174": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "46514661": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "46730080": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "48259777": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "49777926": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "50576456": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "50818413": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "51333624": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "51342201": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "52296506": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "53614866": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "53767549": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "55015862": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "55714689": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "57720431": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "57796565": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "58272763": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "58624310": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "59786231": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "60412914": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "60804751": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "60858668": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "61361387": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "63995233": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "65375371": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "65518916": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "66022059": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "66034560": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "67373926": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "67498296": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "68773688": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "68909654": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "69801006": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "69996829": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "69999703": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "70174979": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "70500348": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "70794744": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "74705117": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "74946014": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "75202345": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "75707047": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "75866949": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "75947473": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "76051234": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "76640509": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "76842691": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "78001236": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "78667002": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "78680494": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "80342955": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "81769444": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "81966790": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "85655216": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "86837217": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "86962817": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "87556131": {
                    "stark_key": "0x3db8d94a5f392bf0aacc6ff3f8385dad7d89f6931854e6701bb8ffc3160150",
                    "balance": "1017186",
                    "token": "0x74b79bd28af25020ee70c1c9edccff0807e3ff94e72f7b9e7e2ad24b28b93d"
                },
                "88823788": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "89051376": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "89067692": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "89261214": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "89529334": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "90644426": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "90874954": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "91309478": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "91664669": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "92373881": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "93298621": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "95612047": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "96223396": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "97761188": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "97965843": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "98032291": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "99400961": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "100253341": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "100577561": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "100977985": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "101276122": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "101481448": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "102237870": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "102726761": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "103537175": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "103924285": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "104692739": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "105284341": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "106086497": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "106625438": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "106701495": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "107343480": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "107810790": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "109779759": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "109816917": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "110187479": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "110246255": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "110636878": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "110772872": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "110787398": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "111181179": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "112151917": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "114941499": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "115477529": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "116075815": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "116850155": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "117121774": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "117933935": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "119473963": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "119652118": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "123412380": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "124180642": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "124248432": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "126276494": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "126594445": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "127046893": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "127277666": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "127380206": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "127389034": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "128186964": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "130091064": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "131751138": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "132358029": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "132823164": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "133187583": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "134651682": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "135856748": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "136062717": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "136283289": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "136370749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "136793743": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "137199520": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "138217342": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "138860376": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "140544806": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "141613813": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "141844520": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "141895774": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "141956812": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "142603365": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "142635468": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "144531284": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "144977875": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "145919144": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "145923612": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "146149591": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "148039977": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "148944703": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "149441837": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "151456938": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "152041705": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "152555008": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "153316490": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "153850830": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "154336649": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "154345607": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "154507097": {
                    "stark_key": "0x139e3b66720f8b5b9eed44f12e08f908c5cfd4926a8e19cd114cf5cfc4a4fd6",
                    "balance": "668969",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "154545733": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "154828223": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "155262113": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "155288194": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "155990943": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "156723549": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "157018535": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "157704911": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "158180652": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "158243158": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "160010102": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "160747497": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "160974434": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "161923906": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "161981899": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "162081977": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "162507567": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "163350417": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "163574907": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "164111164": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "166126985": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "166201383": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "166292912": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "166499242": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "169461682": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "170527794": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "170574591": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "172557763": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "172603458": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "173006570": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "173142440": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "173479334": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "173824166": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "173875208": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "174387217": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "174584344": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "175046376": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "175200476": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "175233259": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "176284769": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "177574821": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "178308758": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "179611881": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "179716295": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "179819157": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "179821191": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "181648045": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "181923341": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "182350384": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "182439294": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "182634806": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "182981703": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "183203141": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "183921540": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "185731812": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "187517109": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "187897931": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "188565690": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "189538181": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "189551500": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "191107217": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "191127671": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "191996933": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "193021675": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "193267325": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "193821589": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "195051511": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "195582295": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "197392123": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "197408932": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "198216069": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "198636522": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "198685175": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "199523891": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "200173358": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "201370164": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "202053169": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "202484581": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "202513191": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "202516165": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "203361652": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "203550655": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "204088285": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "204554369": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "204661552": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "204668836": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "205013380": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "205035169": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "205485991": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "205632377": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "205994523": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "206546046": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "206979537": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "207084227": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "207190203": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "208973824": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "210172697": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "210680302": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "210920086": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "211873638": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "212299133": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "212437176": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "212474110": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "212571555": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "213551939": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "213613982": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "213925730": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "214233393": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "215106646": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "215936144": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "217712752": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "219263731": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "219729875": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "221902756": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "222708166": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "222754262": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "223024255": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "224277123": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "224776101": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "226712710": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "229695820": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "231834546": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "232215649": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "232256396": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "233380710": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "233598548": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "233882150": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "235374628": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "236270360": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "236470561": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "236730607": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "237483253": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "238621488": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "240432064": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "240561260": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "241211143": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "241499910": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "242126697": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "244385772": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "244613418": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "244813927": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "248266408": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "249050349": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "249797353": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "250292656": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "250657920": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "251407407": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "251531560": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "251625026": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "252546858": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "252884879": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "253526174": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "253851426": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "254378047": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "255003510": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "255102813": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "255582111": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "256268095": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "256434584": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "257330256": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "257887188": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "257926920": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "259154188": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "259836703": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "260227425": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "261194125": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "261329492": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "261394295": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "261902500": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "261933098": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "262188911": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "263239963": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "263695393": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "264689951": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "265264792": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "266227787": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "266290113": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "266638799": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "267895078": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "268388348": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "269436476": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "272249627": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "273712649": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "276346421": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "276845299": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "278021465": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "278526360": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "279853068": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "281038389": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "282131689": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "283196422": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "285782238": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "287354585": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "287418183": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "289001749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "289840739": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "290037784": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "290463370": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "290516041": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "293034727": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "293414885": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "293415941": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "294393255": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "297362158": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "297896546": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "299239568": {
                    "stark_key": "0x412e1299a70e646b076cab5848c9fe1c04b6c04a2cf14cbd172119a76904b7d",
                    "balance": "285068",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "299742991": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "300186662": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "300884899": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "300927598": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "302125428": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "302306820": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "302592960": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "302769529": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "303185600": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "304821626": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "304900753": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "306119005": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "306456859": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "307099063": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "307703979": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "309337430": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "309496827": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "310257885": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "311565743": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "313360952": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "314266564": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "314502613": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "315793624": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "317899216": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "318485846": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "318500568": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "319081252": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "320563883": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "322095376": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "322302615": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "322685790": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "323234907": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "324878442": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "325394273": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "327867070": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "329128837": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "329711236": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "329820930": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "329933314": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "329978502": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "330288563": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "330288673": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "330969080": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "331557708": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "332226679": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "332315063": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "332361633": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "332361760": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "332545608": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "333472867": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "334201125": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "335274742": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "335276403": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "335577753": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "335849862": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "338741745": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "339078394": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "339120449": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "340310445": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "341011784": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "342062698": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "342980316": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "347897370": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "348315885": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "350837066": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "351662089": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "352097357": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "352110234": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "352201964": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "353856204": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "356200861": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "356699946": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "356743109": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "359590037": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "360855972": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "361164132": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "361868528": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "363031884": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "363411895": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "364555234": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "364589172": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "365320523": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "365663343": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "366538410": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "367718917": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "368494731": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "369250392": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "369907962": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "370191217": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "370206919": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "372581958": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "373873186": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "374546415": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "376023081": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "376224655": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "376965222": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "377272129": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "377303007": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "377894987": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "378340926": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "379156322": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "379879047": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "380454745": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "381889763": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "383328485": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "385104615": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "385413709": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "387147585": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "388357202": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "388928844": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "389352999": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "389909833": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "390248891": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "391903214": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "392270548": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "392560284": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "394311426": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "394596462": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "394840185": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "395089750": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "395604293": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "395881516": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "395883573": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "396518786": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "397012220": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "397178272": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "397616914": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "398056249": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "398585318": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "399077920": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "400514062": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "401973587": {
                    "stark_key": "0x2535b8b6112e7f21c078806c122210a2326976f4476bc3d4e98b63287b4d4f6",
                    "balance": "949877",
                    "token": "0x12c56da0548f83854cafd8eded2b8edb50bd61dda62090d3b63da427603c1cf"
                },
                "402435843": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "402531191": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "402748794": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "402969645": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "403619176": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "403770576": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "403980722": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "404258790": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "405679132": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "407463003": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "410504890": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "410505806": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "412476706": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "413492634": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "413572161": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "413677023": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "415496350": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "417178462": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "417834555": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "418938266": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "419250182": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "419615179": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "419860313": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "420658235": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "420847420": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "421008977": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "421833445": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "422070803": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "422800956": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "422934990": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "423720135": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "424415693": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "424460874": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "424579200": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "424709867": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "425227989": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "426267800": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "426601723": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "427052559": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "428176665": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "428850555": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "429427086": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "430423488": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "434224626": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "434977567": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "435472982": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "436987120": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "437206568": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "437754513": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "438187645": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "438358627": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "439938649": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "440324964": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "440404689": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "440665348": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "441864402": {
                    "stark_key": "0x7cdbd3f7394ddaad523b4d99fd501aa4d99adc0da3a19cd420d33cc360d3b78",
                    "balance": "554549",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "442238683": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "442362941": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "442501519": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "442515493": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "443616084": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "443983554": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "444544352": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "445016349": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "445274163": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "445545913": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "446793926": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "448158832": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "448161729": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "449292279": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "449678887": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "450426617": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "450627534": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "450949934": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "451566890": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "451780114": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "453413987": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "455325969": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "456179656": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "456507444": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "457306240": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "457740877": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "459905090": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "462448648": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "462601840": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "462865024": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "463261966": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "463599288": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "463872134": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "464181372": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "464568031": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "464626748": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "465626874": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "465703317": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "466006155": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "466317916": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "468092077": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "468130393": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "468359089": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "468385016": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "468644691": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "469104772": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "470170030": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "473792882": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "475020438": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "475775616": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "477044629": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "477500895": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "477580995": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "477960898": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "479082464": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "479559290": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "480964775": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "481895550": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "482341084": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "487692364": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "487693489": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "488535105": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "488978765": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "489154787": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "489395086": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "489683808": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "489813974": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "490563915": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "490757821": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "491669731": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "493755362": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "494409400": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "494498298": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "495013328": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "495570363": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "497024183": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "497676368": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "498016960": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "498790849": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "499542709": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "499603988": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "499724597": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "501592519": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "502184247": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "502270027": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "502410449": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "502471322": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "502658114": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "502769029": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "504034722": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "504357643": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "504864418": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "506119326": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "507422280": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "508415318": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "510810803": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "511932047": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "514207556": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "514502699": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "515140523": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "515191954": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "515347778": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "515550897": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "516673508": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "516752461": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "516994727": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "517061254": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "517863406": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "518305618": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "518855229": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "519343264": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "520275684": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "520277058": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "520385424": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "521445367": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "522313884": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "523771778": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "524030860": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "525126904": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "525699936": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "527301310": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "528717925": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "528952448": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "529792190": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "529844464": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "530632879": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "530636863": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "531242575": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "531906491": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "532260324": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "533085730": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "533955322": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "534069790": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "534873804": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "535900139": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "535965960": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "537601120": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "537716691": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "538859782": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "540559508": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "542261504": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "543331297": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "543457739": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "545520426": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "546191504": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "548096837": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "549201616": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "549223251": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "549304849": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "549365350": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "550390433": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "550722000": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "552618642": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "553740010": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "555727855": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "556549187": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "557137284": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "557385270": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "557524097": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "558008587": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "558284728": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "558308848": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "559825910": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "560212275": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "561518614": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "562071578": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "563402631": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "564672218": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "565100725": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "565141669": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "565778081": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "565987847": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "566731710": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "567682107": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "567714980": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "568059786": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "568526382": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "569144362": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "569515403": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "571332085": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "571973184": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "572026247": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "572199768": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "572707684": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "572855516": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "573187571": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "573304253": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "573805845": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "574443977": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "574478725": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "574510749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "575420282": {
                    "stark_key": "0x39d2ef87fd6ce47c505d350287bd0598a405fda9b2b9618a0313cf100b05aba",
                    "balance": "168109",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "576086454": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "577991288": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "578065130": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "578205759": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "578986563": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "579520198": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "579590935": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "580078265": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "580420723": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "580514796": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "581259379": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "582698677": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "584460776": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "588480400": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "588503566": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "590149986": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "592308445": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "593251749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "593499975": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "594886000": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "595131402": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "595388269": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "595420263": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "596372132": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "597274431": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "597308644": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "599385398": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "599528744": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "599715310": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "600760671": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "603978795": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "604603164": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "604944467": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "605558213": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "606028042": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "607065884": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "608164792": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "609126329": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "609135233": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "609547183": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "609918702": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "609989471": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "610980946": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "611054221": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "611258503": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "611635285": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "611670528": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "612007917": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "612437168": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "613215715": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "613564481": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "613698965": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "614456865": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "615085370": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "615735822": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "615932679": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "617940563": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "618339736": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "618665581": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "618797127": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "623028908": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "623800731": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "624378747": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "624388549": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "624533159": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "625270399": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "625650495": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "626406817": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "626411636": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "626892307": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "626912096": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "627095517": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "627591188": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "627929552": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "628437866": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "629043403": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "630424809": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "630601599": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "631198816": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "632549623": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "632798904": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "632824796": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "633014133": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "633557921": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "633853494": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "634521833": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "634852037": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "635845294": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "636049789": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "636201425": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "638865866": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "639647484": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "641474579": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "643308972": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "643526678": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "644810418": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "647618426": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "648128108": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "648532693": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "649952315": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "650281116": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "650956403": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "651149890": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "651398037": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "651862960": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "651884953": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "652548719": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "652741939": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "653470870": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "653875890": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "654055526": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "654345152": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "655460192": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "656043430": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "656101100": {
                    "stark_key": "0xbc18097dc1b91a2585eb37ae874094ef13b58c09501ff362e6352d448734d2",
                    "balance": "39351",
                    "token": "0x2fe8a91e5d0ce487daf331c6bb786d6908991ab2ad2ef1cbda95a6a00e33032"
                },
                "656130467": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "656498299": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "656687329": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "656985436": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "662754874": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "662945676": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "664220862": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "664385284": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "664404096": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "664510551": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "664882972": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "665340307": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "665673410": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "665841407": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "666983200": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "668317103": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "668576050": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "668698343": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "668798607": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "668934343": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "669394955": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "669618428": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "672448718": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "672830043": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "673974097": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "674215463": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "675689893": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "675852846": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "676035222": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "677133891": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "678156253": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "678895777": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "679091699": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "679348123": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "680721547": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "681304669": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "681477094": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "683497549": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "685268558": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "685534134": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "685601110": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "686389952": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "686609835": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "687316786": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "687824847": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "688514143": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "689037688": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "689418256": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "689734387": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "693226197": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "695726572": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "696132521": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "697305961": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "697971164": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "698299068": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "699796012": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "700915114": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "701310548": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "702332106": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "702466107": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "703348215": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "703832920": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "704965476": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "706184554": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "707948473": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "708242853": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "708527818": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "709716765": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "709782130": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "710415083": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "710434839": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "711661123": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "713374562": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "714835318": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "715130278": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "715456970": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "715947667": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "718726884": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "719229170": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "720503792": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "720963161": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "722384386": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "723026455": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "723938247": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "724277016": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "726103734": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "728648081": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "729605295": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "729963279": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "730321059": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "731806344": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "732605932": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "733575480": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "735332225": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "736328686": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "736578261": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "737735897": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "738393878": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "738570603": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "738920369": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "739243602": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "739744577": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "740436904": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "740531947": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "740864401": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "741459508": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "741733317": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "743000331": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "743066187": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "743171862": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "743585502": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "745266226": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "745636723": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "745961332": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "747926749": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "748311727": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "748317626": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "749498683": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "750561417": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "750703881": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "751426628": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "752178156": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "752447665": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "753451196": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "753880790": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "754703965": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "755002203": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "755496059": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "756919389": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "758384750": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "759494709": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "759594664": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "760205535": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "760289316": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "760526407": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "760760772": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "761159150": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "762263327": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "762740881": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "763121278": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "764128810": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "764807408": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "764897633": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "766627593": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "766923990": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "767906338": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "768430339": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "770333500": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "770462856": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "771567964": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "772071520": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "772734358": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "772783189": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "774573953": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "775284167": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "776717347": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "777413108": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "779717627": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "779723367": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "781120994": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "781650703": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "781835803": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "783405997": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "783790191": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "783946529": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "783951620": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "784861798": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "785703649": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "785822296": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "786779773": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "787708428": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "787870874": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "788405604": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "790061156": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "790427094": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "792680673": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "793205948": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "793976730": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "794008167": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "794147292": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "795977850": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "796180411": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "796945432": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "797454070": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "797776022": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "798758097": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "798785299": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "798932613": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "799333451": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "799533601": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "801958926": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "802375500": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "804571244": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "804616683": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "805331301": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "805658783": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "809094600": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "809123489": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "809256906": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "810547757": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "811035247": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "811863040": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "813079945": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "813249558": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "813423060": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "813615352": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "813620349": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "814801677": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "817752172": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "818506347": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "819796714": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "821716078": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "822263569": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "822367018": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "822981755": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "823143632": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "823580935": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "825099946": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "825131779": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "825722595": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "826275157": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "826325990": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "826931890": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "827343144": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "829345578": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "829463085": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "829906078": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "831266933": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "831272485": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "831330695": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "831435868": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "832421839": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "834114629": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "834260727": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "834488702": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "836463124": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "836715273": {
                    "stark_key": "0x739076b8a77d1e9e962a5d12caae4002111a1dff7611d1f8d248d2a15aa05bc",
                    "balance": "474301",
                    "token": "0x32e4cb5fa236658106a0bb0592413465132450e222420f53d0ee66ca4368247"
                },
                "837835455": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "839480604": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "840117446": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "840253977": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "840507638": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "841496179": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "842328590": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "843491920": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "844123648": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "844399275": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "845043243": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "845115380": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "845521679": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "845804508": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "845878071": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "846524073": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "847597266": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "848544761": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "848877747": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "849432492": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "849608214": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "850322810": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "851528746": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "853086937": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "854346036": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "854913015": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "855799640": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "856525797": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "856754259": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "858744608": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "858882793": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "858887706": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "859065939": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "860105315": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "861088488": {
                    "stark_key": "0x17f753a4850703d0be93f167b15ed2094415bcb88cc4daf6e15743ab7e9e3dd",
                    "balance": "559939",
                    "token": "0x2fe56aad895ecd27520db0d2b0169d77fba699d66a8c9b9a308b79bfaccf5b0"
                },
                "861161800": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "861278120": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "861575670": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "861793044": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "861889891": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "862374526": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "862715757": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "862983206": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "863885636": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "863978086": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "864401211": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "864412429": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "864713892": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "866469733": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "866595339": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "867031126": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "867646813": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "867701047": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "868084725": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "868242389": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "868360792": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "868419274": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "870841169": {
                    "stark_key": "0x551ad472486e1324f9dd97a2f171d34b499b698a91d4ada22a27ecbc2fdf1f6",
                    "balance": "102277",
                    "token": "0x17c23dccf1c7bfe2af9089a91d4b2349dd82aa3ecb5d44e7cbd2c88766b21d7"
                },
                "871845738": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "872264677": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "872523312": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
                },
                "874214407": {
                    "stark_key": "0x0",
                    "balance": "0",
                    "token": "0x0"
             