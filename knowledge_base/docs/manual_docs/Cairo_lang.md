Directory structure:
└── cairo-book-cairo-book/
    ├── README.md
    ├── _typos.toml
    ├── book.toml
    ├── cairo-documentation-style-guide.md
    ├── CLAUDE.md
    ├── LANGUAGES
    ├── LICENSE
    ├── llms-full.txt
    ├── llms.txt
    ├── pyproject.toml
    ├── Scarb.toml
    ├── summary.md
    ├── translations.sh
    ├── uv.lock
    ├── .all-contributorsrc
    ├── .python-version
    ├── .tool-versions
    ├── docs/
    │   └── CONTRIBUTING.md
    ├── listings/
    │   ├── appendix/
    │   │   ├── listing_01_clone/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_copy/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_03_debug/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_04_implpartialeq/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_05_partialeq/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_06_serialize/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_07_default/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── listing_07_deserialize/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch01-getting-started/
    │   │   ├── no_listing_01_hello_world/
    │   │   │   ├── initial_Scarb.toml
    │   │   │   ├── output_build.txt
    │   │   │   ├── output_run.txt
    │   │   │   ├── Scarb.toml
    │   │   │   ├── snfoundry.toml
    │   │   │   └── src/
    │   │   │       ├── hello_world.cairo
    │   │   │       └── lib.cairo
    │   │   ├── prime_prover/
    │   │   │   ├── output.txt
    │   │   │   ├── output_prove.txt
    │   │   │   ├── output_verify.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── prime_prover2/
    │   │       ├── output.txt
    │   │       ├── output_verify.txt
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch02-common-programming-concepts/
    │   │   ├── no_listing_00_consts/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_variables_are_immutable/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_adding_mut/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_shadowing/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_shadowing_different_type/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_mut_cant_change_type/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_data_types/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_integer_types/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_08_numeric_operations/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_09_boolean_type/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_10_short_string_type/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_11_into/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_12_tuple_type/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_13_tuple_destructuration/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_14_tuple_types/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_15_functions/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_16_single_param/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_17_multiple_params/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_18_named_parameters/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_19_statement/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_20_statements_dont_return_values/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_21_blocks_are_expressions/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_22_function_return_values/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_23_function_return_values_2/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_24_function_return_invalid/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_25_comments/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_26_comments/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_27_if/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_28_bis_if_not_bool/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_29_ter_if_not_equal_zero/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_30_else_if/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_31_if_let/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_32_infinite_loop/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_33_loop_break/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_34_loop_continue/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_35_loop_return_values/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_36_while_loop/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_37_item_doc_comments/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_38_mod_doc_comments/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_39_tryinto/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_40_fixed_size_arr_type/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_41_fixed_size_arr_months/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_42_fixed_size_arr_accessing_elements/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_44_fixed_size_arr_accessing_elements_span/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_45_iter_loop_while/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_46_iter_loop_for/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_47_for_range/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_const_fn/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_loop_recursion/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           ├── lib.cairo
    │   │           └── examples/
    │   │               ├── loop_example.cairo
    │   │               └── recursion_example.cairo
    │   ├── ch03-common-collections/
    │   │   ├── no_listing_01_array_new_append/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_array_pop_front/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_array_get/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_array_at/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_array_macro/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_array_with_enums/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_08_array_span/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_09_intro/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_10_intro_rewrite/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_11_entries/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_12_custom_methods/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_13_dict_of_complex/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_14_dict_of_array_insert/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_15_dict_of_array_attempt_get/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_16_dict_of_array/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch04-understanding-ownership/
    │   │   ├── listing_01_variable_and_scope/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_moving_return_values/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_03_returning_many_values/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_04_attempt_modifying_snapshot/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_05_mutable_reference/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_array/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_pass_array_by_value/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_copy_trait/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_no_drop_derive_fails/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_drop_derive_compiles/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_no_destruct_compile_fails/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_destruct_compiles/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_08_array_clone/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_09_snapshots/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_10_desnap/
    │   │       ├── Scarb.lock
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch05-using-structs-to-structure-related-data/
    │   │   ├── listing_01_user_struct/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_mut_struct/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_03_no_struct/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_04_w_tuples/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_05_w_structs/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_update_syntax/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_without_update_syntax/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_define_methods/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_gen_trait/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_references/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_some_params/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_class_methods/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_multiple_traits/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_into/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_08_tryinto/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch06-enums-and-pattern-matching/
    │   │   ├── no_listing_01_enum_example/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_enum_with_values_example/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_enum_message/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_enum_option/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_match_example/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_match_arms_block/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_match_pattern_bind/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_08_match_option/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_09_missing_match_arm/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_10_match_catch_all/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_11_match_or/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_12_match_tuple/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_13_match_integers/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_14_if_let_match_one/
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_15_if_let/
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_16_if_let_coiner_match/
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_17_if_let_coiner/
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_18_while_let/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch07-managing-cairo-projects-with-packages-crates-and-modules/
    │   │   ├── listing_01_basic_nested_modules/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_paths/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_03_pub_keyword/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_04_pub_compiles/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_05_super/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_06_use/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_07_use_and_scope/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_08_unidiomatic_use/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_09_idiomatic_import/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_as_keyword/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_11_multiple_items/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_12_pub_use/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_13_front_extraction/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_14_front_definition/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_lib/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_02_garden/
    │   │       ├── Scarb.lock
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch08-generic-types-and-traits/
    │   │   ├── listing_08_01_extracting_function_01/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_08_01_extracting_function_02/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_08_01_extracting_function_03/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_default_impl/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_impl_aliases/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_missing_tdrop/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_with_tdrop/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_missing_tcopy/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_with_tcopy/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_with_anonymous_impl/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_derive_generics/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_drop_explicit/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_08_two_generics/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_09_option/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_10_result/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_11_generic_methods/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_12_constrained_generics/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_13_not_compiling/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_14_compiling/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_14_simple_trait/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_15_traits/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_16_generate_trait/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_17_generic_traits/
    │   │   │   ├── Scarb.lock
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_18_negative_impl/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_19_associated_items_constraints/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_20_type_equal/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       ├── lib.cairo
    │   │   │       ├── safe_default.cairo
    │   │   │       └── state_machine.cairo
    │   │   └── no_listing_default_impl_self_call/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch09-error-handling/
    │   │   ├── listing_09_01/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_09_02/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_panic/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_with_felt252/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_panic_macro/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_nopanic/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_nopanic_wrong/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_panic_with/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_result_enum/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_08_result_trait/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_09_result_example/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch10-testing-cairo-programs/
    │   │   ├── listing_10_01/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_02/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_03/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_04/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       ├── add_two.cairo
    │   │   │       ├── lib.cairo
    │   │   │       └── wrong_add_two.cairo
    │   │   ├── listing_10_05/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_06/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_07/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_08/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_wrong_can_hold_impl/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_custom_messages/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_03_wrong_new_impl/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_04_new_bug/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_05_ignore_tests/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_assert/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_06_test_gas/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_07_benchmark_gas/
    │   │   │   └── output.txt
    │   │   ├── no_listing_09_integration_test/
    │   │   │   ├── output.txt
    │   │   │   ├── output_integration.txt
    │   │   │   ├── Scarb.toml
    │   │   │   ├── src/
    │   │   │   │   └── lib.cairo
    │   │   │   └── tests/
    │   │   │       └── integration_tests.cairo
    │   │   ├── no_listing_10_assert_eq_ne_macro/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_11_test_private_function/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_12_submodules/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   ├── src/
    │   │   │   │   └── lib.cairo
    │   │   │   └── tests/
    │   │   │       ├── common.cairo
    │   │   │       └── integration_tests.cairo
    │   │   └── no_listing_13_single_integration_crate/
    │   │       ├── output.txt
    │   │       ├── Scarb.toml
    │   │       ├── src/
    │   │       │   └── lib.cairo
    │   │       └── tests/
    │   │           ├── common.cairo
    │   │           ├── integration_tests.cairo
    │   │           └── lib.cairo
    │   ├── ch100-introduction-to-smart-contracts/
    │   │   ├── listing_01_simple_contract/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── listing_02_wrong_impl/
    │   │       ├── output.txt
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch101-building-starknet-smart-contracts/
    │   │   ├── listing_01_reference_contract/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_storage_mapping/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_events_example/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_nested_storage_mapping/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_simple_storage/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_starknet_types/
    │   │   │   ├── Scarb.toml
    │   │   │   ├── snfoundry.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_storage_node/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_storage_vecs/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_abi_per_item_attribute/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_03_explicit_internal_fn/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch102-starknet-cross-contract-interactions/
    │   │   ├── listing_01_simple_erc20_interface/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_expanded_ierc20_dispatcher/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_03_contract_dispatcher/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_04_expanded_ierc20_library/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_05_library_dispatcher/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_06_syscalls/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_07_library_syscall/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── listing_safe_dispatcher/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch103-building-advanced-starknet-smart-contracts/
    │   │   ├── listing_01_storage_packing/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_02_ownable_component/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       ├── component.cairo
    │   │   │       ├── contract.cairo
    │   │   │       └── lib.cairo
    │   │   ├── listing_03_component_dep/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       ├── contract.cairo
    │   │   │       ├── counter.cairo
    │   │   │       ├── lib.cairo
    │   │   │       └── owner.cairo
    │   │   ├── listing_04_test_component/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       ├── counter.cairo
    │   │   │       ├── lib.cairo
    │   │   │       ├── tests_deployed.cairo
    │   │   │       └── tests_direct.cairo
    │   │   ├── listing_05_vote_contract/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_06_dice_game_vrf/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_06_upgrade_with_syscall/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_07_oz_upgrade/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_08_price_feed/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_09_basic_erc20/
    │   │   │   ├── Scarb.toml
    │   │   │   ├── snfoundry.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_10_mintable_burnable_erc20/
    │   │   │   ├── Scarb.toml
    │   │   │   ├── snfoundry.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── listing_11_pausable_erc20/
    │   │   │   ├── Scarb.toml
    │   │   │   ├── snfoundry.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_01_embeddable/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   ├── no_listing_02_embeddable_as_output/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_03_L1_L2_messaging/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch104-starknet-smart-contracts-security/
    │   │   ├── listing_02_pizza_factory_snfoundry/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       ├── lib.cairo
    │   │   │       ├── pizza.cairo
    │   │   │       └── tests/
    │   │   │           └── foundry_test.cairo
    │   │   ├── no_listing_01_assert_balance/
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── no_listing_02_simple_access_control/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   ├── ch11-functional-features/
    │   │   ├── listing_closure_different_types/
    │   │   │   ├── output.txt
    │   │   │   ├── Scarb.toml
    │   │   │   └── src/
    │   │   │       └── lib.cairo
    │   │   └── listing_closure_type/
    │   │       ├── Scarb.toml
    │   │       └── src/
    │   │           └── lib.cairo
    │   └── ch12-advanced-features/
    │       ├── listing_01_array_collection/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_02_inlining/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       ├── inlining.sierra
    │       │       └── lib.cairo
    │       ├── listing_03_inlining_example/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       ├── inlining.sierra
    │       │       └── lib.cairo
    │       ├── listing_04_basic_box/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_05_box/
    │       │   ├── box_memory.json
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_09_deref_coercion/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_10_arithmetic_circuits/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_10_associated_types/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_11_associated_consts/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_12_associated_impls/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_closures/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── listing_recursive_types/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       ├── display.cairo
    │       │       └── lib.cairo
    │       ├── listing_recursive_types_wrong/
    │       │   ├── output.txt
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_01_potions/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_03_hash_trait/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_04_hash_pedersen/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_04_hash_poseidon/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_05_advanced_hash/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_06_format_macro/
    │       │   ├── output.txt
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_07_write_macro/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_08_print_macro/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_09_deref_example/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_09_deref_fn_arg/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_09_deref_mut_example/
    │       │   ├── output.txt
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_09_display_trait_with_format/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_10_display_trait_with_write/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_12_dict_struct_member/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_13_cust_struct_vect/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_14_cust_struct_stack/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_15_procedural_macro/
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.cairo
    │       ├── no_listing_16_procedural_macro_expression/
    │       │   ├── Cargo.toml
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.rs
    │       ├── no_listing_17_procedural_macro_derive/
    │       │   ├── Cargo.toml
    │       │   ├── Scarb.toml
    │       │   └── src/
    │       │       └── lib.rs
    │       └── no_listing_18_procedural_macro_attribute/
    │           ├── Cargo.toml
    │           ├── Scarb.toml
    │           └── src/
    │               └── lib.rs
    ├── quizzes/
    │   ├── ch01-01-installation.toml
    │   ├── ch01-02-hello-world.toml
    │   ├── ch02-01-variables-and-mutability.toml
    │   ├── ch02-02-data-types.toml
    │   ├── ch02-03-functions.toml
    │   ├── ch02-04-comments.toml
    │   ├── ch02-05-control-flow.toml
    │   ├── ch03-01-arrays.toml
    │   ├── ch03-02-dictionaries.toml
    │   ├── ch04-01-what-is-ownership.toml
    │   ├── ch04-02-references-and-snapshots.toml
    │   ├── ch05-01-defining-and-instantiating-structs.toml
    │   ├── ch05-02-an-example-program-using-structs.toml
    │   ├── ch05-03-method-syntax.toml
    │   ├── ch06-01-enums.toml
    │   ├── ch06-02-match.toml
    │   ├── ch06-03-concise-control-flow-with-if-let-and-while-let.toml
    │   ├── ch07-01-packages-crates.toml
    │   ├── ch07-02-defining-modules-to-control-scope.toml
    │   ├── ch07-03-paths-in-module-tree-1.toml
    │   ├── ch07-03-paths-in-module-tree-2.toml
    │   ├── ch07-04-bringing-paths-into-scope.toml
    │   ├── ch07-05-separate-modules.toml
    │   ├── ch08-01-generic-data-types.toml
    │   ├── ch08-02-traits.toml
    │   ├── ch09-01-unrecoverable-errors-with-panic.toml
    │   ├── ch09-02-error-handling-result.toml
    │   ├── ch10-01-how_to_write_tests.toml
    │   ├── ch10-02-testing-organization.toml
    │   ├── ch12-01-custom-structs.toml
    │   ├── ch12-02-smart_pointers.toml
    │   └── ch12-03-operator-overloading.toml
    ├── runner_crate/
    │   └── Scarb.toml
    ├── scripts/
    │   ├── README.md
    │   ├── combine-markdown.sh
    │   ├── display_build_diff.sh
    │   ├── dspy-summarizer.py
    │   ├── handle_targets.py
    │   ├── package.json
    │   ├── tsconfig.json
    │   ├── update-meta-descriptions.ts
    │   └── src/
    │       ├── index.ts
    │       ├── prompt.ts
    │       ├── reorder-listings.ts
    │       ├── search-rename-listing.ts
    │       └── utils.ts
    ├── src/
    │   ├── appendix-00.md
    │   ├── appendix-000.md
    │   ├── appendix-01-keywords.md
    │   ├── appendix-02-operators-and-symbols.md
    │   ├── appendix-03-derivable-traits.md
    │   ├── appendix-04-cairo-prelude.md
    │   ├── appendix-05-common-error-messages.md
    │   ├── appendix-06-useful-development-tools.md
    │   ├── appendix-08-system-calls.md
    │   ├── appendix-09-sierra.md
    │   ├── ch00-00-introduction.md
    │   ├── ch00-01-foreword.md
    │   ├── ch01-00-getting-started.md
    │   ├── ch01-01-installation.md
    │   ├── ch01-02-hello-world.md
    │   ├── ch01-03-proving-a-prime-number.md
    │   ├── ch02-00-common-programming-concepts.md
    │   ├── ch02-01-variables-and-mutability.md
    │   ├── ch02-02-data-types.md
    │   ├── ch02-03-functions.md
    │   ├── ch02-04-comments.md
    │   ├── ch02-05-control-flow.md
    │   ├── ch03-00-common-collections.md
    │   ├── ch03-01-arrays.md
    │   ├── ch03-02-dictionaries.md
    │   ├── ch04-00-understanding-ownership.md
    │   ├── ch04-01-what-is-ownership.md
    │   ├── ch04-02-references-and-snapshots.md
    │   ├── ch05-00-using-structs-to-structure-related-data.md
    │   ├── ch05-01-defining-and-instantiating-structs.md
    │   ├── ch05-02-an-example-program-using-structs.md
    │   ├── ch05-03-method-syntax.md
    │   ├── ch06-00-enums-and-pattern-matching.md
    │   ├── ch06-01-enums.md
    │   ├── ch06-02-the-match-control-flow-construct.md
    │   ├── ch06-03-concise-control-flow-with-if-let-and-while-let.md
    │   ├── ch07-00-managing-cairo-projects-with-packages-crates-and-modules.md
    │   ├── ch07-01-packages-and-crates.md
    │   ├── ch07-02-defining-modules-to-control-scope.md
    │   ├── ch07-03-paths-for-referring-to-an-item-in-the-module-tree.md
    │   ├── ch07-04-bringing-paths-into-scope-with-the-use-keyword.md
    │   ├── ch07-05-separating-modules-into-different-files.md
    │   ├── ch08-00-generic-types-and-traits.md
    │   ├── ch08-01-generic-data-types.md
    │   ├── ch08-02-traits-in-cairo.md
    │   ├── ch09-00-error-handling.md
    │   ├── ch09-01-unrecoverable-errors-with-panic.md
    │   ├── ch09-02-recoverable-errors.md
    │   ├── ch10-00-testing-cairo-programs.md
    │   ├── ch10-01-how-to-write-tests.md
    │   ├── ch10-02-test-organization.md
    │   ├── ch100-00-introduction-to-smart-contracts.md
    │   ├── ch100-01-contracts-classes-and-instances.md
    │   ├── ch101-00-building-starknet-smart-contracts.md
    │   ├── ch101-01-00-contract-storage.md
    │   ├── ch101-01-01-storage-mappings.md
    │   ├── ch101-01-02-storage-vecs.md
    │   ├── ch101-01-starknet-types.md
    │   ├── ch101-02-contract-functions.md
    │   ├── ch101-03-contract-events.md
    │   ├── ch102-00-starknet-contract-interactions.md
    │   ├── ch102-01-contract-class-abi.md
    │   ├── ch102-02-interacting-with-another-contract.md
    │   ├── ch102-03-executing-code-from-another-class.md
    │   ├── ch102-04-serialization-of-cairo-types.md
    │   ├── ch103-00-building-advanced-starknet-smart-contracts.md
    │   ├── ch103-01-optimizing-storage-costs.md
    │   ├── ch103-02-00-composability-and-components.md
    │   ├── ch103-02-01-under-the-hood.md
    │   ├── ch103-02-02-component-dependencies.md
    │   ├── ch103-02-03-testing-components.md
    │   ├── ch103-03-upgradeability.md
    │   ├── ch103-04-L1-L2-messaging.md
    │   ├── ch103-05-01-price-feeds.md
    │   ├── ch103-05-02-randomness.md
    │   ├── ch103-05-oracle-interactions.md
    │   ├── ch103-06-00-other-examples.md
    │   ├── ch103-06-01-deploying-and-interacting-with-a-voting-contract.md
    │   ├── ch103-06-02-working-with-erc20-token.md
    │   ├── ch104-00-starknet-smart-contracts-security.md
    │   ├── ch104-01-general-recommendations.md
    │   ├── ch104-02-testing-smart-contracts.md
    │   ├── ch104-03-static-analysis-tools.md
    │   ├── ch11-00-functional-features.md
    │   ├── ch11-01-closures.md
    │   ├── ch12-00-advanced-features.md
    │   ├── ch12-01-custom-data-structures.md
    │   ├── ch12-02-smart-pointers.md
    │   ├── ch12-03-operator-overloading.md
    │   ├── ch12-04-hash.md
    │   ├── ch12-05-macros.md
    │   ├── ch12-06-inlining-in-cairo.md
    │   ├── ch12-07-gas-optimisation.md
    │   ├── ch12-08-printing.md
    │   ├── ch12-09-deref-coercion.md
    │   ├── ch12-10-arithmetic-circuits.md
    │   ├── ch12-10-associated-items.md
    │   ├── ch12-10-procedural-macros.md
    │   ├── ch200-introduction.md
    │   ├── ch201-architecture.md
    │   ├── ch202-00-memory.md
    │   ├── ch202-01-non-deterministic-read-only-memory.md
    │   ├── ch202-02-segments.md
    │   ├── ch203-00-execution-model.md
    │   ├── ch204-00-builtins.md
    │   ├── ch204-01-how-builtins-work.md
    │   ├── ch204-02-00-output.md
    │   ├── ch204-02-01-pedersen.md
    │   ├── ch204-02-02-range-check.md
    │   ├── ch204-02-03-ecdsa.md
    │   ├── ch204-02-04-bitwise.md
    │   ├── ch204-02-05-ec-op.md
    │   ├── ch204-02-06-keccak.md
    │   ├── ch204-02-07-poseidon.md
    │   ├── ch204-02-08-mod-builtin.md
    │   ├── ch204-02-08-range-check-96.md
    │   ├── ch204-02-09-add-mod.md
    │   ├── ch204-02-10-mul-mod.md
    │   ├── ch204-02-11-segment-arena.md
    │   ├── ch204-02-12-gas.md
    │   ├── ch204-02-13-system.md
    │   ├── ch204-02-builtins-list.md
    │   ├── ch205-00-hints.md
    │   ├── ch206-00-runner.md
    │   ├── ecdsa-full.excalidraw
    │   ├── ecdsa-invalid-hash.excalidraw
    │   ├── ecdsa-invalid-key.excalidraw
    │   ├── ecdsa-segment.excalidraw
    │   ├── ecop-invalid-inputs.excalidraw
    │   ├── ecop-segment.excalidraw
    │   ├── keccak-segment.excalidraw
    │   ├── mermaid-storage-model.txt
    │   ├── range-check-builtin.excalidraw
    │   ├── segment-arena.excalidraw
    │   ├── SUMMARY.md
    │   └── title-page.md
    ├── theme/
    │   ├── book.js
    │   ├── chat.js
    │   ├── highlight.css
    │   ├── highlight.js
    │   ├── index.hbs
    │   ├── css/
    │   │   ├── chat.css
    │   │   ├── chrome.css
    │   │   ├── general.css
    │   │   ├── last-changed.css
    │   │   ├── print.css
    │   │   └── variables.css
    │   ├── fonts/
    │   │   ├── fonts.css
    │   │   ├── OPEN-SANS-LICENCE.txt
    │   │   ├── open-sans-v17-all-charsets-300.woff2
    │   │   ├── open-sans-v17-all-charsets-300italic.woff2
    │   │   ├── open-sans-v17-all-charsets-600.woff2
    │   │   ├── open-sans-v17-all-charsets-600italic.woff2
    │   │   ├── open-sans-v17-all-charsets-700.woff2
    │   │   ├── open-sans-v17-all-charsets-700italic.woff2
    │   │   ├── open-sans-v17-all-charsets-800.woff2
    │   │   ├── open-sans-v17-all-charsets-800italic.woff2
    │   │   ├── open-sans-v17-all-charsets-italic.woff2
    │   │   ├── open-sans-v17-all-charsets-regular.woff2
    │   │   ├── SOURCE-CODE-PRO-LICENSE.txt
    │   │   └── source-code-pro-v11-all-charsets-500.woff2
    │   ├── js/
    │   │   └── index.mjs
    │   └── wasm-cairo/
    │       └── worker.cjs
    ├── .github/
    │   └── workflows/
    │       ├── ci.yml
    │       ├── link-check.yml
    │       ├── mdbook.yml
    │       ├── release.yml
    │       └── install-mdbook/
    │           └── action.yml
    └── .trunk/
        ├── trunk.yaml
        └── configs/
            ├── svgo.config.js
            ├── .markdownlint.yaml
            ├── .rustfmt.toml
            ├── .shellcheckrc
            └── .yamllint.yaml


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
FILE: README.md
================================================
<div align="center">
<!-- Remember: Keep a span between the HTML tag and the markdown tag.  -->

  <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-42-orange.svg?style=flat-square)](#contributors)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

  <h1>The Cairo Programming Language Book</h1>
  <h3> Alexandria </h3>
  <img src="assets/alexandria.jpg" height="400" width="400">
</div>

## Description

This repository contains the source of "The Cairo Programming Language" book, a comprehensive documentation of the Cairo 1 programming language. This documentation is your go-to resource for mastering Cairo, created and maintained by the Starknet community. You can read the book [online](https://book.cairo-lang.org/).

<div align="center">
  <h3> Created by builders, for builders 📜</h3>
</div>

## Contribute

### Setup

1. Rust related packages:
   - Install toolchain providing `cargo` using [rustup](https://rustup.rs/).
   - Install [mdBook](https://rust-lang.github.io/mdBook/guide/installation.html) and the required extensions:
   ```
   cargo install mdbook mdbook-i18n-helpers mdbook-last-changed
   ```
2. Host machine packages:

   - Install [gettext](https://www.gnu.org/software/gettext/) for translations, usually available with regular package manager: `sudo apt install gettext`.
   - Install [mdbook-quiz-cairo](https://github.com/cairo-book/mdbook-quiz-cairo?tab=readme-ov-file) following the instructions [here](https://github.com/cairo-book/mdbook-quiz-cairo?tab=readme-ov-file#installation) to be able to add interactive quizzes.

3. Clone this repository.

4. Install [mdbook-cairo](https://github.com/enitrat/mdbook-cairo) to process references and labels, and custom tags.

```bash
cargo install --git https://github.com/enitrat/mdbook-cairo
```

### Guidelines

Read the [CONTRIBUTING.md](./docs/CONTRIBUTING.md) file for more details on the style guide and guidelines for contributions to the book.

### Work locally

All the Markdown files **MUST** be edited in english. To work locally:

- Start a local server with `mdbook serve` and visit [localhost:3000](http://localhost:3000) to view the book.
  You can use the `--open` flag to open the browser automatically: `mdbook serve --open`.

- Make changes to the book and refresh the browser to see the changes.

- Open a PR with your changes.

### Verifying your Cairo Programs

The `cairo-listings` CLI tool is designed to wrap all Cairo and Starknet plugins for quickly verifying Cairo programs. You can verify that listings are correct with the `verify` argument, and generate the corresponding output with the `output` argument.
Install this tool with:

#### Setup

Firstly, you need to have `scarb` resolved in your path. See [here][installation] for more details.

To run the `cairo-listings` helper tool and verify Cairo programs, ensure that you are at the root of the repository (same directory of this `README.md` file).

Install the tool with:

```sh
cargo install --git https://github.com/enitrat/cairo-listings --locked
```

and then run:

```sh
cairo-listings verify
```

[installation]: ./src/ch01-01-installation.md

#### Usage

The tool scans for all `*.cairo` files in the specified directory and performs the following actions:

For a Starknet contract:

- `scarb build`
- If it has tests: `scarb test`

Cairo program:

- If it has a `main` function: `scarb execute --available-gas=200000000`
- Else, `scarb build`
- If it has tests: `scarb test`
- `scarb fmt -c`

To specify which tests to run, you can add a comment at the top of your file with the following format:

```cairo
// TAG: <tag1>
// TAGS: <tag1>, <tag2>
```

Here is a list of available tags:

- `does_not_compile`: don't run `scarb build`
- `does_not_run`: don't run `scarb execute --available-gas=200000000`
- `ignore_fmt`: don't run `scarb fmt`
- `tests_fail`: don't run `scarb test`

The mdbook-cairo is a mdbook preprocessor that only removes the `// TAG` lines in code blocks.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.starknet.id/"><img src="https://avatars.githubusercontent.com/u/78437165?v=4?s=100" width="100px;" alt="Fricoben"/><br /><sub><b>Fricoben</b></sub></a><br /><a href="#ideas-fricoben" title="Ideas, Planning, & Feedback">🤔</a> <a href="#fundingFinding-fricoben" title="Funding Finding">🔍</a> <a href="#projectManagement-fricoben" title="Project Management">📆</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/enitrat"><img src="https://avatars.githubusercontent.com/u/60658558?v=4?s=100" width="100px;" alt="Mathieu"/><br /><sub><b>Mathieu</b></sub></a><br /><a href="#ideas-enitrat" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=enitrat" title="Code">💻</a> <a href="#mentoring-enitrat" title="Mentoring">🧑‍🏫</a> <a href="https://github.com/cairo-book/cairo-book/pulls?q=is%3Apr+reviewed-by%3Aenitrat" title="Reviewed Pull Requests">👀</a> <a href="#projectManagement-enitrat" title="Project Management">📆</a> <a href="#maintenance-enitrat" title="Maintenance">🚧</a> <a href="#tool-enitrat" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Nadai2010"><img src="https://avatars.githubusercontent.com/u/112663528?v=4?s=100" width="100px;" alt="Nadai"/><br /><sub><b>Nadai</b></sub></a><br /><a href="#translation-Nadai2010" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/glihm"><img src="https://avatars.githubusercontent.com/u/7962849?v=4?s=100" width="100px;" alt="glihm"/><br /><sub><b>glihm</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=glihm" title="Code">💻</a> <a href="#tool-glihm" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.linkedin.com/in/clementwalter/"><img src="https://avatars.githubusercontent.com/u/18620296?v=4?s=100" width="100px;" alt="Clément Walter"/><br /><sub><b>Clément Walter</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/pulls?q=is%3Apr+reviewed-by%3AClementWalter" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/makluganteng"><img src="https://avatars.githubusercontent.com/u/74396818?v=4?s=100" width="100px;" alt="V.O.T"/><br /><sub><b>V.O.T</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=makluganteng" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rkdud007"><img src="https://avatars.githubusercontent.com/u/76558220?v=4?s=100" width="100px;" alt="Pia"/><br /><sub><b>Pia</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=rkdud007" title="Code">💻</a> <a href="#blog-rkdud007" title="Blogposts">📝</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cryptonerdcn"><img src="https://avatars.githubusercontent.com/u/97042744?v=4?s=100" width="100px;" alt="cryptonerdcn"/><br /><sub><b>cryptonerdcn</b></sub></a><br /><a href="#translation-cryptonerdcn" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MathiasTELITSINE"><img src="https://avatars.githubusercontent.com/u/95372106?v=4?s=100" width="100px;" alt="Argetlames"/><br /><sub><b>Argetlames</b></sub></a><br /><a href="#translation-MathiasTELITSINE" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://julio4.com"><img src="https://avatars.githubusercontent.com/u/30329843?v=4?s=100" width="100px;" alt="julio4"/><br /><sub><b>julio4</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=julio4" title="Code">💻</a> <a href="#tool-julio4" title="Tools">🔧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hgedia"><img src="https://avatars.githubusercontent.com/u/32969555?v=4?s=100" width="100px;" alt="Haresh Gedia"/><br /><sub><b>Haresh Gedia</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=hgedia" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://0xdarlington.disha.page"><img src="https://avatars.githubusercontent.com/u/75126961?v=4?s=100" width="100px;" alt="Darlington Nnam"/><br /><sub><b>Darlington Nnam</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=Darlington02" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/tiagofneto"><img src="https://avatars.githubusercontent.com/u/46165861?v=4?s=100" width="100px;" alt="Tiago Neto"/><br /><sub><b>Tiago Neto</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/pulls?q=is%3Apr+reviewed-by%3Atiagofneto" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/omahs"><img src="https://avatars.githubusercontent.com/u/73983677?v=4?s=100" width="100px;" alt="omahs"/><br /><sub><b>omahs</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=omahs" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://shramee.me"><img src="https://avatars.githubusercontent.com/u/11048263?v=4?s=100" width="100px;" alt="Shramee Srivastav"/><br /><sub><b>Shramee Srivastav</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=shramee" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dbejarano820"><img src="https://avatars.githubusercontent.com/u/58019353?v=4?s=100" width="100px;" alt="Daniel Bejarano"/><br /><sub><b>Daniel Bejarano</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=dbejarano820" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/TAdev0"><img src="https://avatars.githubusercontent.com/u/122918260?v=4?s=100" width="100px;" alt="Tristan"/><br /><sub><b>Tristan</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=TAdev0" title="Code">💻</a> <a href="#maintenance-TAdev0" title="Maintenance">🚧</a> <a href="https://github.com/cairo-book/cairo-book/pulls?q=is%3Apr+reviewed-by%3ATAdev0" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://okhaimie.com"><img src="https://avatars.githubusercontent.com/u/57156589?v=4?s=100" width="100px;" alt="okhai.stark ( Tony Stark )"/><br /><sub><b>okhai.stark ( Tony Stark )</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=okhaimie-dev" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Uniblake"><img src="https://avatars.githubusercontent.com/u/31915926?v=4?s=100" width="100px;" alt="shwang"/><br /><sub><b>shwang</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=Uniblake" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kwkr"><img src="https://avatars.githubusercontent.com/u/20127759?v=4?s=100" width="100px;" alt="kwkr"/><br /><sub><b>kwkr</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=kwkr" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ArnaudBD"><img src="https://avatars.githubusercontent.com/u/20355199?v=4?s=100" width="100px;" alt="ArnaudBD"/><br /><sub><b>ArnaudBD</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=ArnaudBD" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/JimmyFate"><img src="https://avatars.githubusercontent.com/u/158521482?v=4?s=100" width="100px;" alt="Jimmy Fate"/><br /><sub><b>Jimmy Fate</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=JimmyFate" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LeandroCarvajal"><img src="https://avatars.githubusercontent.com/u/99574021?v=4?s=100" width="100px;" alt="SimplementeCao"/><br /><sub><b>SimplementeCao</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=LeandroCarvajal" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LucasLvy"><img src="https://avatars.githubusercontent.com/u/70894690?v=4?s=100" width="100px;" alt="Lucas @ StarkWare"/><br /><sub><b>Lucas @ StarkWare</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=LucasLvy" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/remybar"><img src="https://avatars.githubusercontent.com/u/57539816?v=4?s=100" width="100px;" alt="Rémy Baranx"/><br /><sub><b>Rémy Baranx</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=remybar" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/stevencartavia"><img src="https://avatars.githubusercontent.com/u/112043913?v=4?s=100" width="100px;" alt="Steven Cordero"/><br /><sub><b>Steven Cordero</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=stevencartavia" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Symmaque"><img src="https://avatars.githubusercontent.com/u/50242998?v=4?s=100" width="100px;" alt="Symmaque"/><br /><sub><b>Symmaque</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=Symmaque" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=Symmaque" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/No-bodyq"><img src="https://avatars.githubusercontent.com/u/141028690?v=4?s=100" width="100px;" alt="Asher"/><br /><sub><b>Asher</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=No-bodyq" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://misicnenad.github.io"><img src="https://avatars.githubusercontent.com/u/19427053?v=4?s=100" width="100px;" alt="Nenad Misić"/><br /><sub><b>Nenad Misić</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=misicnenad" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=misicnenad" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/TeddyNotBear"><img src="https://avatars.githubusercontent.com/u/106410805?v=4?s=100" width="100px;" alt="Teddy Not Bear"/><br /><sub><b>Teddy Not Bear</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=TeddyNotBear" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://audithub.app"><img src="https://avatars.githubusercontent.com/u/71888134?v=4?s=100" width="100px;" alt="Malatrax"/><br /><sub><b>Malatrax</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=zmalatrax" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=zmalatrax" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://alankang.xyz"><img src="https://avatars.githubusercontent.com/u/55970530?v=4?s=100" width="100px;" alt="Beeyoung"/><br /><sub><b>Beeyoung</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=FriendlyLifeguard" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=FriendlyLifeguard" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/chachaleo"><img src="https://avatars.githubusercontent.com/u/49371958?v=4?s=100" width="100px;" alt="Charlotte"/><br /><sub><b>Charlotte</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=chachaleo" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=chachaleo" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/obatirou"><img src="https://avatars.githubusercontent.com/u/92337658?v=4?s=100" width="100px;" alt="Oba"/><br /><sub><b>Oba</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=obatirou" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/martinvibes"><img src="https://avatars.githubusercontent.com/u/127976766?v=4?s=100" width="100px;" alt="martin machiebe"/><br /><sub><b>martin machiebe</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=martinvibes" title="Documentation">📖</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Jeanmichel7"><img src="https://avatars.githubusercontent.com/u/59661788?v=4?s=100" width="100px;" alt="Jean-Michel"/><br /><sub><b>Jean-Michel</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=Jeanmichel7" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=Jeanmichel7" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/NueloSE"><img src="https://avatars.githubusercontent.com/u/124416278?v=4?s=100" width="100px;" alt="Emmanuel A Akalo"/><br /><sub><b>Emmanuel A Akalo</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=NueloSE" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=NueloSE" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/supreme2580"><img src="https://avatars.githubusercontent.com/u/100731397?v=4?s=100" width="100px;" alt="Supreme Labs"/><br /><sub><b>Supreme Labs</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=supreme2580" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=supreme2580" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blocksorcerer"><img src="https://avatars.githubusercontent.com/u/175638109?v=4?s=100" width="100px;" alt="blocksorcerer"/><br /><sub><b>blocksorcerer</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=blocksorcerer" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=blocksorcerer" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/quentin-abei"><img src="https://avatars.githubusercontent.com/u/98474907?v=4?s=100" width="100px;" alt="quentin-abei"/><br /><sub><b>quentin-abei</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=quentin-abei" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=quentin-abei" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.0xjarix.com/"><img src="https://avatars.githubusercontent.com/u/55955137?v=4?s=100" width="100px;" alt="0xjarix"/><br /><sub><b>0xjarix</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=0xjarix" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kkawula"><img src="https://avatars.githubusercontent.com/u/57270771?v=4?s=100" width="100px;" alt="kkawula"/><br /><sub><b>kkawula</b></sub></a><br /><a href="https://github.com/cairo-book/cairo-book/commits?author=kkawula" title="Documentation">📖</a> <a href="https://github.com/cairo-book/cairo-book/commits?author=kkawula" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->



================================================
FILE: _typos.toml
================================================
[default]
extend-ignore-identifiers-re = ["Groth16"]

[type.po]
extend-glob = ["*.po", "*.css", "*.js"]
check-file = false

[files]
extend-exclude = ["po/*.po", "listings/**/*.json", "**/*.excalidraw"]



================================================
FILE: book.toml
================================================
[book]
authors = ["Starknet community, with support from Starkware and Voyager"]
language = "en"
src = "src"
title = "The Cairo Programming Language"
description = "The Cairo Programming Language. A comprehensive documentation for Cairo, the smart contract language for Starknet."

[build]
extra-watch-dirs = ["po", "listings"]
create-missing = false

[preprocessor.cairo]
after = ["links"]

[preprocessor.gettext]
after = ["cairo"]

[preprocessor.quiz-cairo]
after = ["gettext"]

[output.html]
git-repository-url = "https://github.com/cairo-book/cairo-book.github.io"
edit-url-template = "https://github.com/cairo-book/cairo-book.github.io/edit/main/{path}"
playground.runnable = true
google-analytics = "G-0ZJLBV4KE2"
additional-css = ["theme/css/last-changed.css", "theme/css/chat.css"]
additional-js = [
  "theme/chat.js",
  "theme/js/index.mjs",
  "theme/wasm-cairo/pkg/wasm-cairo.js",
  "theme/wasm-cairo/pkg/wasm-cairo_bg.wasm",
  "theme/wasm-cairo/worker.cjs",
]
mathjax-support = true

# Redirects to avoid dead links
[output.html.redirect]
"/ch13-01-general-introduction-to-smart-contracts.html" = "/ch13-01-introduction-to-smart-contracts.html"
"/ch13-01-introduction-to-smart-contracts.html" = "/ch100-00-introduction-to-smart-contracts.html"
"/ch14-00-building-starknet-smart-contracts.html" = "/ch101-00-building-starknet-smart-contracts.html"
"/ch14-01-00-contract-storage.html" = "/ch101-01-00-contract-storage.html"
"/ch14-01-01-storage-mappings.html" = "/ch101-01-01-storage-mappings.html"
"/ch14-01-02-storage-vecs.html" = "/ch101-01-02-storage-vecs.html"
"/ch14-02-contract-functions.html" = "/ch101-02-contract-functions.html"
"/ch14-03-contract-events.html" = "/ch101-03-contract-events.html"
"/ch15-00-starknet-contract-interactions.html" = "/ch102-00-starknet-contract-interactions.html"
"/ch15-01-contract-class-abi.html" = "/ch102-01-contract-class-abi.html"
"/ch15-02-interacting-with-another-contract.html" = "/ch102-02-interacting-with-another-contract.html"
"/ch15-03-executing-code-from-another-class.html" = "/ch102-03-executing-code-from-another-class.html"
"/ch16-00-building-advanced-starknet-smart-contracts.html" = "/ch103-00-building-advanced-starknet-smart-contracts.html"
"/ch16-01-optimizing-storage-costs.html" = "/ch103-01-optimizing-storage-costs.html"
"/ch16-02-00-composability-and-components.html" = "/ch103-02-00-composability-and-components.html"
"/ch16-02-01-under-the-hood.html" = "/ch103-02-01-under-the-hood.html"
"/ch16-02-02-component-dependencies.html" = "/ch103-02-02-component-dependencies.html"
"/ch16-02-03-testing-components.html" = "/ch103-02-03-testing-components.html"
"/ch16-03-upgradeability.html" = "/ch103-03-upgradeability.html"
"/ch16-04-L1-L2-messaging.html" = "/ch103-04-L1-L2-messaging.html"
"/ch16-05-01-price-feeds.html" = "/ch103-05-01-price-feeds.html"
"/ch16-05-02-randomness.html" = "/ch103-05-02-randomness.html"
"/ch16-05-oracle-interactions.html" = "/ch103-05-oracle-interactions.html"
"/ch16-06-00-other-examples.html" = "/ch103-06-00-other-examples.html"
"/ch16-06-01-deploying-and-interacting-with-a-voting-contract.html" = "/ch103-06-01-deploying-and-interacting-with-a-voting-contract.html"
"/ch17-00-starknet-smart-contracts-security.html" = "/ch104-00-starknet-smart-contracts-security.html"
"/ch17-01-general-recommendations.html" = "/ch104-01-general-recommendations.html"
"/ch17-02-testing-smart-contracts.html" = "/ch104-02-testing-smart-contracts.html"
"/ch17-03-static-analysis-tools.html" = "/ch104-03-static-analysis-tools.html"
"/ch11-00-advanced-features.html" = "/ch12-00-advanced-features.html"
"/ch11-01-custom-data-structures.html" = "/ch12-01-custom-data-structures.html"
"/ch11-02-smart-pointers.html" = "/ch12-02-smart-pointers.html"
"/ch11-03-operator-overloading.html" = "/ch12-03-operator-overloading.html"
"/ch11-04-hash.html" = "/ch12-04-hash.html"
"/ch11-05-macros.html" = "/ch12-05-macros.html"
"/ch11-06-inlining-in-cairo.html" = "/ch12-06-inlining-in-cairo.html"
"/ch11-07-gas-optimisation.html" = "/ch12-07-gas-optimisation.html"
"/ch11-08-printing.html" = "/ch12-08-printing.html"
"/ch11-09-deref-coercion.html" = "/ch12-09-deref-coercion.html"
"/ch11-10-arithmetic-circuits.html" = "/ch12-10-arithmetic-circuits.html"
"/ch11-10-associated-items.html" = "/ch12-10-associated-items.html"
"/ch11-10-procedural-macros.html" = "/ch12-10-procedural-macros.html"

[output.html.code.hidelines]
cairo = "# "

[output.html.fold]
enable = true
level = 2

[output.markdown]



================================================
FILE: cairo-documentation-style-guide.md
================================================
<!-- omit in toc -->

# Cairo Documentation Style Guide

_Inspired by the [Rust Documentation Style Guide](https://github.com/esp-rs/book/blob/main/rust-doc-style-guide.md#rust-documentation-style-guide)_

As [The Rust RFC Book](https://rust-lang.github.io/rfcs/2436-style-guide.html#drawbacks) states:

> One can level some criticisms at having a style guide:
>
> - It is bureaucratic, gives developers more to worry about, and crushes creativity.
> - There are edge cases where the style rules make code look worse (e.g., around FFI).
>
> However, these are heavily out-weighed by the benefits.

The style guide is based on the best practices collected from the following books:

- [The Rust Programming Language](https://doc.rust-lang.org/book/foreword.html)
- [The Embedded Rust Book](https://docs.rust-embedded.org/book/intro/index.html)
- [The rustup book](https://rust-lang.github.io/rustup/installation/windows.html)
- [The Cargo Book](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html)
- [The rustc book](https://doc.rust-lang.org/nightly/rustc/targets/index.html)
- [The Rust on ESP Book](https://esp-rs.github.io/book/)

<!-- omit in toc -->

## Contents of This Style Guide

- [Heading Titles](#heading-titles)
  - [Capitalization](#capitalization)
- [Linking](#linking)
  - [Adding Links](#adding-links)
  - [Formatting](#formatting)
- [Lists](#lists)
  - [Types](#types)
  - [Formatting](#formatting-1)
- [Using `monospace`](#using-monospace)
  - [Monospace and Other Types of Formatting](#monospace-and-other-types-of-formatting)
- [Using _Italics_](#using-italics)
- [Mode of Narration](#mode-of-narration)
- [Terminology](#terminology)
  - [Recommended Terms](#recommended-terms)
- [Admonitions](#admonitions)
- [Appendix A: Existing Style Guides](#appendix-a-existing-style-guides)
  - [Documentation](#documentation)
  - [Code](#code)

## Heading Titles

The Cairo Book usually have heading titles based on nouns or gerunds:

> **Design Patterns** > **Using Structs to Structure Related Data**

### Capitalization

In heading titles, capitalize the first letter of every word **except for**:

- Articles (a, an, the); unless an article is the first word.

  > **Defining an Enum**

- Coordinating conjunctions (and, but, for, or, nor).

  > **Generic Types and Traits**

  > **Packages and Crates**

- Prepositions of _four_ letters or less, unless these prepositions are the first or last words. Prepositions of _five_ letters and above should be capitalized (Before, Through, Versus, Among, Under, Between, Without, etc.).

  > **Using Structs to Structure Related Data**

  > **Components: Under the Hood**

Do not capitalize names of functions, commands, packages, websites, etc.

> **What is `assert`**

> **Bringing Paths into Scope with the `use` Keyword**

See also, the [Using `monospace`](#using-monospace) section.

In hyphenated words, do not capitalize the parts following the hyphens.

> **Built-in Targets**

> **Allowed-by-default Lints**

## Linking

### Adding Links

To simplify link maintenance, follow the rules below:

- Use [link variables][stackoverflow-link-var] with variable names that give a clue on where the link leads.
- Define link variables right before the end of the section/subsection where they are used.

[stackoverflow-link-var]: https://stackoverflow.com/a/27784490/10308406

Example:

```md
[`scarb`][scarb-github] Scarb bundles the Cairo compiler and the Cairo language server together in an easy-to-install package so that you can start writing Cairo code right away.

[scarb-github]: https://github.com/software-mansion/scarb
```

### Formatting

The Cairo Book usually uses the following link formatting:

- Make intra-book links relative, so they work both online and locally.

- Do NOT turn long phrases into links.

  > ❌ See the [Cairo Reference’s section on constant evaluation](https://book.cairo-lang.org/ch02-01-variables-and-mutability.html) for more information on what operations can be used when declaring constants.

Also, consider the following:

- Do not provide a link to the same location repeatedly in the same or adjacent paragraphs without a good reason, especially using different link text.
- Do not use the same link text to refer to different locations.

  > `scarb` might have a section in a book and a github repo. In this case, see the [`scarb`](https://book.cairo-lang.org/ch01-01-installation.html) section and [`scarb` repo](https://github.com/software-mansion/scarb).

See also, the [Using `monospace`](#using-monospace) section.

## Lists

### Types

The following types of lists are usually used in documentation:

- **Bullet list** -- use it if the order of items is not important
- **Numbered list** -- use it if the order of items is important, such as when describing a process
  - **Procedure** -- special type of numbered list that gives steps to achieve some goal (to achieve this, do this); for an example of a procedure, see the [Usage](https://doc.rust-lang.org/nightly/rustc/profile-guided-optimization.html#usage) section in The rustc book.

### Formatting

The Cairo Book usually uses the following list formatting:

- Finish an introductory sentence with a dot.
- Capitalize the first letter of each bullet point.
- If a bullet point is a full sentence, you can end it with a full stop.
- If a list has at least one full stop, end all other list items with a full stop.

  > A crate is a subset of a package that is used in the actual Cairo compilation. This includes:
  >
  > - The package source code, identified by the package name and the crate root, which is the main entry point of the package.
  > - A subset of the package metadata that identifies crate-level settings of the Cairo compiler, for example, the edition field in the Scarb.toml file.

- For longer list items, consider using a summary word of phrase to make content [scannable](https://learn.microsoft.com/en-us/style-guide/scannable-content/).

  > If you run Windows on your host machine, make sure ...
  >
  > - **MSVC**: Recommended ABI, included in ...
  > - **GNU**: ABI used by the GCC toolchain ...

  - For an example using bold font, see the list in the [Modules Cheat Sheet](https://book.cairo-lang.org/ch07-02-defining-modules-to-control-scope.html#modules-cheat-sheet) section in The Cairo Programming Language book.
  - For an example using monospace font, see the [Appendix A](https://book.cairo-lang.org/appendix-01-keywords.html#strict-keywords) section in The Cairo Book.

## Using `monospace`

Use monospace font for the following items:

- Code snippets

  - Start the terminal commands with `$`
  - Output of previous commands should not start with `$`
  - Use `bash` syntax highlighting

- Cairo declarations: commands, functions, arguments, parameters, flags, variables
- In-line command line output

  > Writing a program that prints `Hello, world!`

- Data types: `u8`, `u128`, etc
- Names of crates, traits, libraries
- Command line tools, plugins, packages

### Monospace and Other Types of Formatting

Monospace font can also be used in:

- Links

  > [`ByteArray`](./src/ch02-02-data-types.md#byte-array-strings) is a string type provided by ...

- Headings

  > **Serializing with `Serde`**

- Important information, notes...

  > **Note: This program would not compile without a break condition. For the purpose of the example, we added a `break` statement that will never be reached, but satisfies the compiler.**

## Using _Italics_

- Introduce new terms

  > Enums, short for "enumerations," are a way to define a custom data type that consists of a fixed set of named values, called _variants_.

- Emphasize important concepts or words

  > we create an _instance_ of that struct by specifying concrete values for each of the fields

## Mode of Narration

- Use _the first person_ (we) when introducing a tutorial or explaining how things will be done. The reader will feel like being on the same team with the authors working side by side.

  > We have just created a file called lib.cairo, which contains a module declaration referencing another module named hello_world, as well as the file hello_world.cairo, containing the implementation details of the hello_world module.

- Use _the second person_ (you) when describing what the reader should do while installing software, following a tutorial or a procedure. However, in most cases you can use imperative mood as if giving orders to the readers. It makes instructions much shorter and clearer.

  > 1\. Create a new project using `scarb`
  >
  > `scarb new hello_world`
  >
  > 2\. Go into the _hello_world_ directory with the command cd hello_world
  >
  > `cd hello_world`

- Use _the third person_ (the user, it) when describing how things work from the perspective of hardware or software.

  > Cairo uses an immutable memory model, meaning that once a memory cell is written to, it can't be overwritten but only read from. To reflect this immutable memory model, variables in Cairo are immutable by default.

## Terminology

This chapter lists the terms that have inconsistencies in spelling, usage, etc.

If you spot other issues with terminology, please add the terms here in alphabetical order using the formatting as follows:

- _Recommended term_
  - Avoid: Add typical phrases in which this term is found
  - Use: Add recommended phrases
  - Note: Add more information if needed

### Recommended Terms

- _Scarb_
  - Note: always use uppercase _S_, unless referring to the command `scarb`
- _VS Code_
  - Use VS Code by default
  - Use only if necessary: Visual Studio Code

## Admonitions

Use the following formatting for notes and warnings:

- Note

  > ⚠️ **Note**: A note covering an important point or idea. Use sparingly or the readers will start ignoring them.

- Warning

  > 🚨 **Warning**: Use in critical circumstances only, e.g., for security risks or actions potentially harmful to users, etc.

In markdown:

```md
> ⚠️ **Note**: Write your note.
```

## Appendix A: Existing Style Guides

### Documentation

- [The Rust Programming Language Style Guide](https://github.com/rust-lang-ja/book-ja/blob/master-ja/style-guide.md)

### Code

- [Style Guidelines](https://doc.rust-lang.org/1.0.0/style/README.html)
- [The Rust RFC Book](https://rust-lang.github.io/rfcs/2436-style-guide.html) chapter _Style Guide_
- [Rust API Guidelines](https://rust-lang.github.io/api-guidelines/)
- [Rust Style Guide](https://riptutorial.com/rust/topic/4620/rust-style-guide) (riptutorial.com)
- [Rust Style Guide](https://github.com/rust-lang/rust/blob/master/src/doc/style-guide/src/principles.md) (github.com/rust-lang)



================================================
FILE: CLAUDE.md
================================================
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Prerequisites & Setup

Required tools:

- **mdBook**: `cargo install mdbook`
- **scarb**: v2.11.4 (via asdf: `asdf install`)
- **starknet-foundry**: v0.44.0 (via asdf)
- **mdbook-cairo**: Custom preprocessor (install via `cargo install --git https://github.com/enitrat/mdbook-cairo`)
- **cairo-listings**: Verification tool (install via `cargo install --git https://github.com/enitrat/cairo-listings --locked`)
- **typos-cli**: Spell checker (`cargo install typos-cli`)
- **bun** (optional): For helper scripts

## Build, Lint & Test Commands

- Build project: `mdbook build`
- Start local server: `mdbook serve [--open]`
- Format all code: `cairo-listings format`
- Generate all code outputs: `cairo-listings output`.
- Verify Cairo programs: `cairo-listings verify` - this will run `scarb build` and `scarb test` for all programs in the `listings` directory, so it can be quite long. If you want to verify a specific program, you can navigate to the directory and run `scarb` commands.
- Test individual Cairo programs: `scarb test [test_name]`
- Format Cairo code: `scarb fmt`
- Check formatting: `scarb fmt -c`
- Running a specific program: `scarb execute`
- Check for typos: `typos`

## Book Structure

The book is structured in the following way:

- `src/`: The main book content - this is where you should write the book. Don't write code examples here, use `listings/` for that, and then refer to the listing using mdbook's `{{#include <filename>}}` or `{{#rustdoc_include <filename>}}` (if referring to specific Anchor tags) macros.
- `listings/`: Code listings for the book. Each listing is a specific Scarb package. To create a new listing, navigate to the proper `listings/ch-name` and run `scarb new <listing-name>`. Create the package with the Starknet Foundry template. Instantly delete the created `package_name/.git` directory.
- `scripts/`: Helper scripts for the book.
- `book.toml`: The book configuration file.
- `SUMMARY.md`: The book summary file. Table of Content for the book. All pages of the book must be referenced there.
- `README.md`: The book README file.
- `quizzes/`: Quiz questions for the book. They can be embedded in the book using the `{{#quiz}}` macro.

## Code Style Guidelines

- **Naming**: Use `snake_case` for functions/variables, `PascalCase` for types/traits
- **Formatting**: All Cairo files must pass `cairo-listings format`
- **Imports**: Group imports by origin (core, external, internal)
- **Error Handling**: Use `Result` for recoverable errors, `panic!` for unrecoverable ones
- **Documentation**: Use doc comments (`///` for items, `//!` for modules)
- **Testing**: Place tests in a `#[cfg(test)]` module, use `#[test]` attribute
- **Code Organization**: Use ANCHOR/ANCHOR_END tags to mark sections for inclusion
- **TAG Comments**: Use TAG comments for special handling by the build tools
- **Traits**: Separate trait definitions from implementations
- **Storage**: Follow Starknet patterns for contract storage access

### TAG Comment System

- `// TAG: does_not_compile` - Code that intentionally doesn't compile
- `// TAG: does_not_run` - Code that compiles but doesn't run
- `// TAG: ignore_fmt` - Skip formatting for this file
- `// TAG: tests_fail` - Tests that are expected to fail

## Book Guidelines

- **Book Structure**:
  - The structure is defined in `SUMMARY.md`
  - The markdown files are located in `src` and there is a single nesting level.
  - The files are named like `ch01-getting-started.md`. Sub-chapters are named like `ch01-01-introduction.md`.
- **Code Blocks**:

  - All code blocks should have a language specified.
  - Example:

  ```cairo

  ```

  - The content of code blocks should be a {{#include <filename>}} macro, where filename is the path to the code to embed.
  - Example:

  ```md
  {{#include ../listings/ch01-getting-started/prime_prover/src/lib.cairo}}
  ```

- **Documentation style**:
  - Use the [Cairo Documentation Style Guide](./cairo-documentation-style-guide.md)
  - Follow markdown formatting rules
  - Always base the writing style on the existing book.

### Content Requirements

- Each concept must have runnable or illustrative code examples
- Use simple, clear language appropriate for beginners
- Include relevant diagrams when explaining complex concepts
- Provide exercises and quizzes for reader engagement
- Cross-reference related sections using mdBook's label/ref system

## Helper Scripts

Located in `scripts/` directory:

- Utility scripts for book maintenance
- Build automation tools
- Content validation scripts

## CI/CD Workflow

GitHub Actions automatically:

- Builds and tests the book on PRs
- Verifies all Cairo code examples compile
- Runs formatting checks
- Deploys to GitHub Pages on main branch merges
- Checks for spelling errors with typos

## mdBook Configuration

Key settings from `book.toml`:

- Output directory: `book/`
- Default theme with custom CSS/JS
- Multiple preprocessors for Cairo-specific features
- Internationalization support enabled

## Important Instruction Reminders

Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (\*.md) or README files. Only create documentation files if explicitly requested by the User.



================================================
FILE: LANGUAGES
================================================
es fr zh-cn id tr



================================================
FILE: LICENSE
================================================
MIT License

Copyright (c) 2023 cairo-book

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
FILE: llms-full.txt
================================================
# Introduction

## What is Cairo?

Cairo is a programming language designed to leverage the power of mathematical proofs for computational integrity. Just as C.S. Lewis defined integrity as "doing the right thing, even when no one is watching," Cairo enables programs to prove they've done the right computation, even when executed on untrusted machines.

The language is built on STARK technology, a modern evolution of PCP (Probabilistically Checkable Proofs) that transforms computational claims into constraint systems. While Cairo's ultimate purpose is to generate these mathematical proofs that can be verified efficiently and with absolute certainty.

## What Can You Do with It?

Cairo enables a paradigm shift in how we think about trusted computation. Its primary application today is Starknet, a Layer 2 scaling solution for Ethereum that addresses one of blockchain's fundamental challenges: scalability without sacrificing security.

In the traditional blockchain model, every participant must verify every computation. Starknet changes this by using Cairo's proof system: computations are executed off-chain by a prover who generates a STARK proof, which is then verified by an Ethereum smart contract. This verification requires significantly less computational power than re-executing the computations, enabling massive scalability while maintaining security.

However, Cairo's potential extends beyond blockchain. Any scenario where computational integrity needs to be verified efficiently can benefit from Cairo's verifiable computation capabilities.

## Who Is This Book For?

This book caters to three main audiences, each with their own learning path:

1. **General-Purpose Developers**: If you're interested in Cairo for its verifiable computation capabilities outside of blockchain, you'll want to focus on chapters 1-12. These chapters cover the core language features and programming concepts without diving deep into smart contract specifics.

2. **New Smart Contract Developers**: If you're new to both Cairo and smart contracts, we recommend reading the book front to back. This will give you a solid foundation in both the language fundamentals and smart contract development principles.

3. **Experienced Smart Contract Developers**: If you're already familiar with smart contract development in other languages, or Rust, you might want to follow this focused path:
   - Chapters 1-3 for Cairo basics
   - Chapter 8 for Cairo's trait and generics system
   - Skip to Chapter 15 for smart contract development
   - Reference other chapters as needed

Regardless of your background, this book assumes basic programming knowledge such as variables, functions, and common data structures. While prior experience with Rust can be helpful (as Cairo shares many similarities), it's not required.

## References

- Cairo CPU Architecture: <https://eprint.iacr.org/2021/1063>
- Cairo, Sierra and Casm: <https://medium.com/nethermind-eth/under-the-hood-of-cairo-1-0-exploring-sierra-7f32808421f5>
- State of non determinism: <https://twitter.com/PapiniShahar/status/1638203716535713798>
# Foreword

Zero-knowledge proofs have emerged as a transformative technology in the blockchain space, offering solutions for both privacy and scalability challenges. Among these, STARKs (Scalable Transparent ARguments of Knowledge) stand out as a particularly powerful innovation. Unlike traditional proof systems, STARKs rely solely on collision-resistant hash functions, making them post-quantum secure and eliminating the need for trusted setups.

However, writing general-purpose programs that can generate cryptographic proofs has historically been a significant challenge. Developers needed deep expertise in cryptography and complex mathematical concepts to create verifiable computations, making it impractical for mainstream adoption.

This is where Cairo comes in. As a general-purpose programming language designed specifically for creating provable programs, Cairo abstracts away the underlying cryptographic complexities while maintaining the full power of STARKs. Strongly inspired by Rust, Cairo has been built to help you create provable programs without requiring specific knowledge of its underlying architecture, allowing you to focus on the program logic itself.

Blockchain developers that want to deploy contracts on Starknet will use the Cairo programming language to code their smart contracts. This allows the Starknet OS to generate execution traces for transactions to be proved by a prover, which is then verified on Ethereum L1 prior to updating the state root of Starknet.

However, Cairo is not only for blockchain developers. As a general purpose programming language, it can be used for any computation that would benefit from being proved on one computer and verified on other machines. Powered by a Rust VM, and a next-generation prover, the execution and proof generation of Cairo programs is blazingly fast - making Cairo the best tool for building provable applications.

This book is designed for developers with a basic understanding of programming concepts. It is a friendly and approachable text intended to help you level up your knowledge of Cairo, but also help you develop your programming skills in general. So, dive in and get ready to learn all there is to know about Cairo!

## Acknowledgements

This book would not have been possible without the help of the Cairo community. We would like to thank every contributor for their contributions to this book!

We would like to thank the Rust community for the [Rust Book][doc rust], which has been a great source of inspiration for this book. Many examples and explanations have been adapted from the Rust Book to fit the Cairo programming language, as the two languages share many similarities.

[doc rust]: https://doc.rust-lang.org/book/
# Getting Started

Let’s start your Cairo journey! There’s a lot to learn, but every journey starts somewhere. In this chapter, we’ll discuss:

- Installing Scarb, which is Cairo's build toolchain and package manager, on Linux, macOS, and Windows.
- Installing Starknet Foundry, which is the default test runnner when creating a Cairo project.
- Writing a program that prints `Hello, world!`.
- Using basic Scarb commands to create a project and execute a program.

## Getting Help

If you have any questions about Starknet or Cairo, you can ask them in the [Starknet Discord server][discord]. The community is friendly and always willing to help.

[discord]: https://discord.gg/starknet-community

## Interacting with the Starknet AI Agent

Starknet proposes its own AI agent designed to assist with Cairo and Starknet-related questions. This AI agent is trained on the Cairo book and the Starknet documentation, using Retrieval-Augmented Generation (RAG) to efficiently retrieve information and provide accurate assistance.

You can find the Starknet Agent on the [Starknet Agent][agent gpt] website.

[agent gpt]: https://agent.starknet.id/
# Installation

The first step is to install Cairo. We'll download Cairo through [starkup][starkup], a command line tool for managing Cairo versions and associated tools. You'll need an internet connection for the download.

The following steps install the latest stable version of the Cairo compiler through a binary called [Scarb][scarb doc]. Scarb bundles the Cairo compiler and the Cairo language server together in an easy-to-install package so that you can start writing Cairo code right away.

Scarb is also Cairo's package manager and is heavily inspired by [Cargo][cargo doc], Rust's build system and package manager.

Scarb handles a lot of tasks for you, such as building your code (either pure Cairo or Starknet contracts), downloading the libraries your code depends on, building those libraries, and provides LSP support for the VSCode Cairo 1 extension.

As you write more complex Cairo programs, you might add dependencies, and if you start a project using Scarb, managing external code and dependencies will be a lot easier to do.

[Starknet Foundry][sn foundry] is a toolchain for Cairo programs and Starknet smart contract development. It supports many features, including writing and running tests with advanced features, deploying contracts, interacting with the Starknet network, and more.

Let's start by installing starkup, which will help us manage Cairo, Scarb, and Starknet Foundry.

[starkup]: https://github.com/software-mansion/starkup
[scarb doc]: https://docs.swmansion.com/scarb/docs
[cargo doc]: https://doc.rust-lang.org/cargo/
[sn foundry]: https://foundry-rs.github.io/starknet-foundry/index.html

## Installing `starkup` on Linux or MacOs

If you're using Linux or macOS, open a terminal and enter the following command:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.starkup.dev | sh
```

The command downloads a script and starts the installation of the starkup tool, which installs the latest stable version of Cairo and related toolings. You might be prompted for your password. If the install is successful, the following line will appear:

```bash
starkup: Installation complete.
```

After installation, starkup will automatically install the latest stable versions of Cairo, Scarb, and Starknet Foundry. You can verify the installations by running the following commands in a new terminal session:

```bash
$ scarb --version
scarb 2.11.4 (c0ef5ec6a 2025-04-09)
cairo: 2.11.4 (https://crates.io/crates/cairo-lang-compiler/2.11.4)
sierra: 1.7.0

$ snforge --version
snforge 0.39.0
```

We'll describe Starknet Foundry in more detail in [Chapter 10][writing tests] for Cairo programs testing and in [Chapter 18][testing with snfoundry] when discussing Starknet smart contract testing and security in the second part of the book.

[writing tests]: ./ch10-01-how-to-write-tests.md
[testing with snfoundry]: ./ch104-02-testing-smart-contracts.md#testing-smart-contracts-with-starknet-foundry

## Installing the VSCode Extension

Cairo has a VSCode extension that provides syntax highlighting, code completion, and other useful features. You can install it from the [VSCode Marketplace][vsc extension].
Once installed, go into the extension settings, and make sure to tick the `Enable Language Server` and `Enable Scarb` options.

[vsc extension]: https://marketplace.visualstudio.com/items?itemName=starkware.cairo1

<div class="quiz-placeholder" data-quiz-name="&quot;ch01-01-installation&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;id&quot;:&quot;1b7c7edd-8c2c-418b-ad80-c0b37b8ae215&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;Cairo's package manager and build system&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;a VS Code extension&quot;,&quot;the name of the VM that runs Cairo&quot;],&quot;prompt&quot;:&quot;What is Scarb?&quot;}}]}"></div>


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Hello, World

Now that you’ve installed Cairo through Scarb, it’s time to write your first Cairo program.
It’s traditional when learning a new language to write a little program that
prints the text `Hello, world!` to the screen, so we’ll do the same here!

> Note: This book assumes basic familiarity with the command line. Cairo makes
> no specific demands about your editing or tooling or where your code lives, so
> if you prefer to use an integrated development environment (IDE) instead of
> the command line, feel free to use your favorite IDE. The Cairo team has developed
> a VSCode extension for the Cairo language that you can use to get the features from
> the language server and code highlighting. See [Appendix F][devtools]
> for more details.

[devtools]: ./appendix-06-useful-development-tools.md

## Creating a Project Directory

You’ll start by making a directory to store your Cairo code. It doesn’t matter
to Cairo where your code lives, but for the exercises and projects in this book,
we suggest making a _cairo_projects_ directory in your home directory and keeping all
your projects there.

Open a terminal and enter the following commands to make a _cairo_projects_ directory.

For Linux, macOS, and PowerShell on Windows, enter this:

```shell
mkdir ~/cairo_projects
cd ~/cairo_projects
```

For Windows CMD, enter this:

```cmd
> mkdir "%USERPROFILE%\cairo_projects"
> cd /d "%USERPROFILE%\cairo_projects"
```

> Note: From now on, for each example shown in the book, we assume that
> you will be working from a Scarb project directory. If you are not using Scarb, and try to run the examples from a different directory, you might need to adjust the commands accordingly or create a Scarb project.

## Creating a Project with Scarb

Let’s create a new project using Scarb.

Navigate to your _cairo_projects_ directory (or wherever you decided to store your code). Then run the following:

```bash
scarb new hello_world
```

Scarb will ask you about the dependencies you want to add.
You will be given two options :

```text
? Which test runner do you want to set up? ›
❯ Starknet Foundry (default)
  Cairo Test
```

In general, we'll prefer using the first one `❯ Starknet Foundry (default)`.

This creates a new directory and project called _hello_world_. We’ve named our project _hello_world_, and Scarb creates its files in a directory of the same name.

Go into the _hello_world_ directory with the command `cd hello_world`. You’ll see that Scarb has generated three files and two directory for us: a _Scarb.toml_ file, a _src_ directory with a _lib.cairo_ file inside and a _tests_ directory containing a _test_contract.cairo_ file. For now, we can remove this _tests_ directory.

It has also initialized a new Git repository along with a `.gitignore` file

> Note: Git is a common version control system. You can stop using version control system by using the `--no-vcs` flag.
> Run `scarb new --help` to see the available options.

Open _Scarb.toml_ in your text editor of choice. It should look similar to the code in Listing 1-1.

<span class="filename">Filename: Scarb.toml</span>

```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2024_07"

# See more keys and their definitions at https://docs.swmansion.com/scarb/docs/reference/manifest.html

[dependencies]
starknet = "2.11.4"

[dev-dependencies]
snforge_std = "0.39.0"
assert_macros = "2.11.4"

[[target.starknet-contract]]
sierra = true

[scripts]
test = "snforge test"

# ...
```

<span class="caption">Listing 1-1: Contents of _Scarb.toml_ generated by `scarb new`</span>

This file is in the [TOML][toml doc] (Tom’s Obvious, Minimal Language) format, which is Scarb’s configuration format.

The first line, `[package]`, is a section heading that indicates that the following statements are configuring a package. As we add more information to this file, we’ll add other sections.

The next three lines set the configuration information Scarb needs to compile your program: the name of the package and the version of Scarb to use, and the edition of the prelude to use. The prelude is the collection of the most commonly used items that are automatically imported into every Cairo program. You can learn more about the prelude in [Appendix D][prelude].

The `[dependencies]` section, is the start of a section for you to list any of your project’s dependencies. In Cairo, packages of code are referred to as crates. We won’t need any other crates for this project.

The `[dev-dependencies]` section is about dependencies that are required for development, but are not needed for the actual production build of the project. `snforge_std` and `assert_macros` are two examples of such dependencies. If you want to test your project without using Starknet Foundry, you can use `cairo_test`.

The `[[target.starknet-contract]]` section allows to build Starknet smart contracts. We can remove it for now.

The `[script]` section allows to define custom scripts. By default, there is one script for running tests using `snforge` with the `scarb test` command. We can also remove it for now.

Starknet Foundry also have more options, check out [Starknet Foundry documentation](https://foundry-rs.github.io/starknet-foundry/appendix/scarb-toml.html) for more information.

By default, using Starknet Foundry adds the `starknet` dependency and the `[[target.starknet-contract]]` section, so that you can build contracts for Starknet out of the box. We will start with only Cairo programs, so you can edit your _Scarb.toml_ file to the following:

<span class="filename">Filename: Scarb.toml</span>

```toml
[package]
name = "hello_world"
version = "0.1.0"
edition = "2024_07"

[dependencies]
```

<span class="caption">Listing 1-2: Contents of modified _Scarb.toml_</span>

The other file created by Scarb is _src/lib.cairo_, let's delete all the content and put in the following content, we will explain the reason later.

```cairo,noplayground
mod hello_world;
```

Then create a new file called _src/hello_world.cairo_ and put the following code in it:

<span class="filename">Filename: src/hello_world.cairo</span>

```cairo
fn main() {
    println!("Hello, World!");
}
```

We have just created a file called _lib.cairo_, which contains a module declaration referencing another module named `hello_world`, as well as the file _hello_world.cairo_, containing the implementation details of the `hello_world` module.

Scarb requires your source files to be located within the _src_ directory.

The top-level project directory is reserved for _README_ files, license information, configuration files, and any other non-code-related content.
Scarb ensures a designated location for all project components, maintaining a structured organization.

If you started a project that doesn’t use Scarb, you can convert it to a project that does use Scarb. Move the project code into the _src_ directory and create an appropriate _Scarb.toml_ file. You can also use `scarb init` command to generate the _src_ folder and the _Scarb.toml_ it contains.

```txt
├── Scarb.toml
├── src
│   ├── lib.cairo
│   └── hello_world.cairo
```

<span class="caption"> A sample Scarb project structure</span>

[toml doc]: https://toml.io/
[prelude]: ./appendix-04-cairo-prelude.md
[starknet package]: https://docs.swmansion.com/scarb/docs/extensions/starknet/starknet-package.html

## Building a Scarb Project

From your _hello_world_ directory, build your project by entering the following command:

```bash
$ scarb build
   Compiling hello_world v0.1.0 (listings/ch01-getting-started/no_listing_01_hello_world/Scarb.toml)
    Finished `dev` profile target(s) in 8 seconds

```

This command creates a `hello_world.sierra.json` file in _target/dev_, let's ignore the `sierra` file for now.

If you have installed Cairo correctly, you should be able to run the `main` function of your program with the `scarb execute` command and see the following output:

```shell
$ scarb execute
   Compiling hello_world v0.1.0 (listings/ch01-getting-started/no_listing_01_hello_world/Scarb.toml)
    Finished `dev` profile target(s) in 15 seconds
     Running hello_world
Hello, World!
Run completed successfully, returning []

```


Regardless of your operating system, the string `Hello, world!` should be printed to
the terminal.

If `Hello, world!` did print, congratulations! You’ve officially written a Cairo
program. That makes you a Cairo programmer — welcome!

## Anatomy of a Cairo Program

Let’s review this “Hello, world!” program in detail. Here’s the first piece of
the puzzle:

```cairo,noplayground
fn main() {

}
```

These lines define a function named `main`. The `main` function is special: it
is always the first code that runs in every executable Cairo program. Here, the
first line declares a function named `main` that has no parameters and returns
nothing. If there were parameters, they would go inside the parentheses `()`.

The function body is wrapped in `{}`. Cairo requires curly brackets around all
function bodies. It’s good style to place the opening curly bracket on the same
line as the function declaration, adding one space in between.

> Note: If you want to stick to a standard style across Cairo projects, you can
> use the automatic formatter tool available with `scarb fmt` to format your code in a
> particular style (more on `scarb fmt` in
> [Appendix F][devtools]). The Cairo team has included this tool
> with the standard Cairo distribution, as `cairo-run` is, so it should already be
> installed on your computer!

The body of the `main` function holds the following code:

```cairo,noplayground
    println!("Hello, World!");
```

This line does all the work in this little program: it prints text to the
screen. There are four important details to notice here.

First, Cairo style is to indent with four spaces, not a tab.

Second, `println!` calls a Cairo macro. If it had called a function instead, it would be entered as `println` (without the `!`).
We’ll discuss Cairo macros in more detail in the ["Macros"][macros] chapter. For now, you just need to know that using a `!` means that you’re calling a macro instead of a normal function and that macros don’t always follow the same rules as functions.

Third, you see the `"Hello, world!"` string. We pass this string as an argument to `println!`, and the string is printed to the screen.

Fourth, we end the line with a semicolon (`;`), which indicates that this
expression is over and the next one is ready to begin. Most lines of Cairo code
end with a semicolon.

[devtools]: ./appendix-06-useful-development-tools.md
[macros]: ./ch12-05-macros.md

<div class="quiz-placeholder" data-quiz-name="&quot;ch01-02-hello-world&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;id&quot;:&quot;aac32d9f-b5a4-4946-81f2-eb6bcfc090ed&quot;,&quot;type&quot;:&quot;ShortAnswer&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;main&quot;},&quot;prompt&quot;:{&quot;prompt&quot;:&quot;What is the name of the initial function that a Cairo program runs?&quot;}},{&quot;context&quot;:&quot;`scarb execute` will first compile and then run your code.&quot;,&quot;id&quot;:&quot;a89b37cf-aa75-4fc7-b433-3b57d273ce1d&quot;,&quot;type&quot;:&quot;ShortAnswer&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;scarb execute&quot;},&quot;prompt&quot;:{&quot;prompt&quot;:&quot;Which command will run the code in your project?&quot;}}]}"></div>

# Summary

Let’s recap what we’ve learned so far about Scarb:

- We can install one or multiple Scarb versions, either the latest stable or a specific one, using asdf.
- We can create a project using `scarb new`.
- We can build a project using `scarb build` to generate the compiled Sierra code.
- We can execute a Cairo program using the `scarb execute` command.

An additional advantage of using Scarb is that the commands are the same no matter which operating system you’re working on. So, at this point, we’ll no longer provide specific instructions for Linux and macOS versus Windows.

You’re already off to a great start on your Cairo journey! This is a great time to build a more substantial program to get used to reading and writing Cairo code.


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Proving That A Number Is Prime

Let’s dive into Cairo by working through a hands-on project together! This section introduces you to key Cairo concepts and the process of generating zero-knowledge proofs locally, a powerful feature enabled by Cairo in combination with the [Stwo prover][stwo]. You’ll learn about functions, control flow, executable targets, Scarb workflows, and how to prove a statement — all while practicing the fundamentals of Cairo programming. In later chapters, we’ll explore these ideas in more depth.

For this project, we’ll implement a classic mathematical problem suited for zero-knowledge proofs: proving that a number is prime. This is the ideal project to introduce you to the concept of zero-knowledge proofs in Cairo, because while _finding_ prime numbers is a complex task, _proving_ that a number is prime is straightforward.

Here’s how it works: the program will take an input number from the user and check whether it’s prime using a trial division algorithm. Then, we’ll use Scarb to execute the program and generate a proof that the primality check was performed correctly, so that anyone can verify your proof to trust that you found a prime number. The user will input a number, and we’ll output whether it’s prime, followed by generating and verifying a proof.

## Setting Up a New Project

To get started, ensure you have Scarb 2.11.4 or later installed (see [Installation][installation] for details). We’ll use Scarb to create and manage our Cairo project.

Open a terminal in your projects directory and create a new Scarb project:

```bash
scarb new prime_prover
cd prime_prover
```

The scarb new command creates a new directory called `prime_prover` with a basic project structure. Let’s examine the generated Scarb.toml file:

<span class="filename">Filename: Scarb.toml</span>

```toml
[package]
name = "prime_prover"
version = "0.1.0"
edition = "2024_07"

[dependencies]

[dev-dependencies]
cairo_test = "2.11.4"
```

This is a minimal manifest file for a Cairo project. However, since we want to create an executable program that we can prove, we need to modify it. Update Scarb.toml to define an executable target and include the `cairo_execute` plugin:

<span class="filename">Filename: Scarb.toml</span>

```toml
[package]
name = "prime_prover"
version = "0.1.0"
edition = "2024_07"

[[target.executable]]

[cairo]
enable-gas = false

[cairo]
enable-gas = false

[dependencies]
cairo_execute = "2.11.4"
```

Here’s what we’ve added:

- `[[target.executable]]` specifies that this package compiles to a Cairo executable (not a library or Starknet contract).
- `[cairo] enable-gas = false` disables gas tracking, which is required for executable targets since gas is specific to Starknet contracts.
  `[dependencies] cairo_execute = "2.11.4"` adds the plugin needed to execute and prove our program.

Now, check the generated `src/lib.cairo`, which is a simple placeholder. Since we’re building an executable, we’ll replace this with a function annotated with `#[executable]` to define our entry point.

## Writing the Prime-Checking Logic

Let’s write a program to check if a number is prime. A number is prime if it’s greater than 1 and divisible only by 1 and itself. We’ll implement a simple trial division algorithm and mark it as executable. Replace the contents of `src/lib.cairo` with the following:

<span class="filename">Filename: src/lib.cairo</span>

```cairo
/// Checks if a number is prime
///
/// # Arguments
///
/// * `n` - The number to check
///
/// # Returns
///
/// * `true` if the number is prime
/// * `false` if the number is not prime
fn is_prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    let mut i = 3;
    let mut is_prime = true;
    loop {
        if i * i > n {
            break;
        }
        if n % i == 0 {
            is_prime = false;
            break;
        }
        i += 2;
    }
    is_prime
}

// Executable entry point
#[executable]
fn main(input: u32) -> bool {
    is_prime(input)
}
```

Let’s break this down:

The `is_prime` function:

- Takes a `u32` input (an unsigned 32-bit integer) and returns a `bool`.
- Checks edge cases: numbers ≤ 1 are not prime, 2 is prime, even numbers > 2 are not prime.
- Uses a loop to test odd divisors up to the square root of `n`. If no divisors are found, the number is prime.

The `main` function:

- Marked with `#[executable]`, indicating it’s the entry point for our program.
- Takes a u32 input from the user and returns a bool indicating whether it’s prime.
- Calls is_prime to perform the check.

This is a straightforward implementation, but it’s perfect for demonstrating proving in Cairo.

## Executing the Program

Now let’s run the program with Scarb to test it. Use the scarb execute command and provide an input number as an argument:

```bash
scarb execute -p prime_prover --print-program-output --arguments 17
```

- `-p prime_prover` specifies the package name (matches Scarb.toml).
- `--print-program-output` displays the result.
- `--arguments 17` passes the number 17 as input.

You should see output like this:

```bash
$ scarb execute -p prime_prover --print-program-output --arguments 17
   Compiling prime_prover v0.1.0 (listings/ch01-getting-started/prime_prover/Scarb.toml)
    Finished `dev` profile target(s) in 2 seconds
   Executing prime_prover
Program output:
0
1
Saving output to: target/execute/prime_prover/execution2

```

The output represents whether the program executed successfully and the result of the program. Here, `0` indicates success (no panic), and `1` represents true (17 is prime). Try a few more numbers:

```bash
$ scarb execute -p prime_prover --print-program-output --arguments 4
[0, 0]  # 4 is not prime
$ scarb execute -p prime_prover --print-program-output --arguments 23
[0, 1]  # 23 is prime
```

The execution creates a folder under `./target/execute/prime_prover/execution1/` containing files like `air_public_input.json`, `air_private_input.json`, `trace.bin`, and `memory.bin`. These are the artifacts needed for proving.

## Generating a Zero-Knowledge Proof

Now for the exciting part: proving that the primality check was computed correctly without revealing the input! Cairo 2.10 integrates the Stwo prover via Scarb, allowing us to generate a proof directly. Run:

```bash
$ scarb prove --execution-id 1
     Proving prime_prover
warn: soundness of proof is not yet guaranteed by Stwo, use at your own risk
Saving proof to: target/execute/prime_prover/execution1/proof/proof.json

```

`--execution_id 1` points to the first execution (from the `execution1` folder).

This command generates a `proof.json` file in `./target/execute/prime_prover/execution1/proof/`. The proof demonstrates that the program executed correctly for some input, producing a true or false output.

## Verifying the Proof

To ensure the proof is valid, verify it with:

```bash
$ scarb verify --execution-id 1
   Verifying prime_prover
    Verified proof successfully

```

If successful, you’ll see a confirmation message. This verifies that the computation (primality check) was performed correctly, aligning with the public inputs, without needing to re-run the program.

## Improving the Program: Handling Input Errors

Currently, our program assumes the input is a valid `u32`. What if we want to handle larger numbers or invalid inputs? Cairo’s `u32` has a maximum value of `2^32 - 1 (4,294,967,295)`, and inputs must be provided as integers. Let’s modify the program to use `u128` and add a basic check. Update `src/lib.cairo`:

<span class="filename">Filename: src/lib.cairo</span>

```cairo
/// Checks if a number is prime
///
/// # Arguments
///
/// * `n` - The number to check
///
/// # Returns
///
/// * `true` if the number is prime
/// * `false` if the number is not prime
fn is_prime(n: u128) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }
    let mut i = 3;
    let mut is_prime = true;
    loop {
        if i * i > n {
            break;
        }
        if n % i == 0 {
            is_prime = false;
            break;
        }
        i += 2;
    }
    is_prime
}

#[executable]
fn main(input: u128) -> bool {
    if input > 1000000 { // Arbitrary limit for demo purposes
        panic!("Input too large, must be <= 1,000,000");
    }
    is_prime(input)
}
```

Changed `u32` to `u128` for a larger range (up to `2^128 - 1`).
Added a check to panic if the input exceeds 1,000,000 (for simplicity; adjust as needed).
Test it:

```bash
$ scarb execute -p prime_prover --print-program-output --arguments 1000001
   Compiling prime_prover v0.1.0 (listings/ch01-getting-started/prime_prover2/Scarb.toml)
    Finished `dev` profile target(s) in 2 seconds
   Executing prime_prover
Program output:
1
Saving output to: target/execute/prime_prover/execution2
error: Panicked with "Input too large, must be <= 1,000,000".

```

If we pass a number greater than 1,000,000, the program will panic - and thus, no proof can be generated. As such, it's not possible to verify a proof for a panicked execution.

## Summary

Congratulations! You’ve built a Cairo program to check primality, executed it with Scarb, and generated and verified a zero-knowledge proof using the Stwo prover. This project introduced you to:

- Defining executable targets in Scarb.toml.
- Writing functions and control flow in Cairo.
- Using `scarb execute` to run programs and generate execution traces.
- Proving and verifying computations with `scarb prove` and `scarb verify`.

In the next chapters, you’ll dive deeper into Cairo’s syntax (Chapter 2), ownership (Chapter 4), and other features. For now, experiment with different inputs or modify the primality check — can you optimize it further?

[installation]: ./ch01-01-installation.md
[stwo]: https://github.com/starkware-libs/stwo
# Common Programming Concepts

This chapter covers concepts that appear in almost every programming language and how they work in Cairo. Many programming languages have much in common at their core. None of the concepts presented in this chapter are unique to Cairo, but we’ll discuss them in the context of Cairo and explain the conventions around using these concepts.

Specifically, you’ll learn about variables, basic types, functions, comments, and control flow. These foundations will be in every Cairo program, and learning them early will give you a strong core to start from.
# Variables and Mutability

Cairo uses an immutable memory model, meaning that once a memory cell is written to,
it can't be overwritten but only read from. To reflect this immutable memory model,
variables in Cairo are immutable by default.
However, the language abstracts this model and gives you the option to make your
variables mutable. Let’s explore how and why Cairo enforces immutability, and how
you can make your variables mutable.

When a variable is immutable, once a value is bound to a name, you can’t change
that value. To illustrate this, generate a new project called _variables_ in
your _cairo_projects_ directory by using `scarb new variables`.

Then, in your new _variables_ directory, open _src/lib.cairo_ and replace its
code with the following code, which won’t compile just yet:

<span class="filename">Filename: src/lib.cairo</span>

```cairo,does_not_compile
fn main() {
    let x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);
}

```

Save and run the program using `scarb execute`. You should receive an error message
regarding an immutability error, as shown in this output:

```shell
$ scarb execute
   Compiling no_listing_01_variables_are_immutable v0.1.0 (listings/ch02-common-programming-concepts/no_listing_01_variables_are_immutable/Scarb.toml)
error: Cannot assign to an immutable variable.
 --> listings/ch02-common-programming-concepts/no_listing_01_variables_are_immutable/src/lib.cairo:6:5
    x = 6;
    ^***^

error: could not compile `no_listing_01_variables_are_immutable` due to previous error
error: `scarb metadata` exited with error

```

This example shows how the compiler helps you find errors in your programs.
Compiler errors can be frustrating, but they only mean your program
isn’t safely doing what you want it to do yet; they do _not_ mean that you’re
not a good programmer! Experienced Caironautes still get compiler errors.

You received the error message `Cannot assign to an immutable variable.`
because you tried to assign a second value to the immutable `x` variable.

It’s important that we get compile-time errors when we attempt to change a
value that’s designated as immutable because this specific situation can lead to
bugs. If one part of our code operates on the assumption that a value will
never change and another part of our code changes that value, it’s possible
that the first part of the code won’t do what it was designed to do. The cause
of this kind of bug can be difficult to track down after the fact, especially
when the second piece of code changes the value only _sometimes_.

Cairo, unlike most other languages, has immutable memory. This makes a
whole class of bugs impossible, because values will never change unexpectedly.
This makes code easier to reason about.

But mutability can be very useful, and can make code more convenient to write.
Although variables are immutable by default, you can make them mutable by
adding `mut` in front of the variable name. Adding `mut` also conveys
intent to future readers of the code by indicating that other parts of the code
will be changing the value associated to this variable.

<!-- TODO: add an illustration of this -->

However, you might be wondering at this point what exactly happens when a variable
is declared as `mut`, as we previously mentioned that Cairo's memory is immutable.
The answer is that the _value_ is immutable, but the _variable_ isn't. The value
associated to the variable can be changed. Assigning to a mutable variable in Cairo
is essentially equivalent to redeclaring it to refer to another value in another memory cell,
but the compiler handles that for you, and the keyword `mut` makes it explicit.
Upon examining the low-level Cairo Assembly code, it becomes clear that
variable mutation is implemented as syntactic sugar, which translates mutation operations
into a series of steps equivalent to variable shadowing. The only difference is that at the Cairo
level, the variable is not redeclared so its type cannot change.

For example, let’s change _src/lib.cairo_ to the following:

```cairo
fn main() {
    let mut x = 5;
    println!("The value of x is: {}", x);
    x = 6;
    println!("The value of x is: {}", x);
}
```

When we run the program now, we get this:

```shell
$ scarb execute
   Compiling no_listing_02_adding_mut v0.1.0 (listings/ch02-common-programming-concepts/no_listing_02_adding_mut/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_02_adding_mut
The value of x is: 5
The value of x is: 6
Run completed successfully, returning []

```

We’re allowed to change the value bound to `x` from `5` to `6` when `mut` is
used. Ultimately, deciding whether to use mutability or not is up to you and
depends on what you think is clearest in that particular situation.

## Constants

Like immutable variables, _constants_ are values that are bound to a name and
are not allowed to change, but there are a few differences between constants
and variables.

First, you aren’t allowed to use `mut` with constants. Constants aren’t just
immutable by default—they’re always immutable. You declare constants using the
`const` keyword instead of the `let` keyword, and the type of the value _must_
be annotated. We’ll cover types and type annotations in the next section,
[“Data Types”][data-types], so don’t worry about the details
right now. Just know that you must always annotate the type.

Constant variables can be declared with any usual data type, including structs, enums and fixed-size arrays.

Constants can only be declared in the global scope, which makes
them useful for values that many parts of code need to know about.

The last difference is that constants may natively be set only to a constant expression,
not the result of a value that could only be computed at runtime.

Here’s an example of constants declaration:

```cairo,noplayground
struct AnyStruct {
    a: u256,
    b: u32,
}

enum AnyEnum {
    A: felt252,
    B: (usize, u256),
}

const ONE_HOUR_IN_SECONDS: u32 = 3600;
const STRUCT_INSTANCE: AnyStruct = AnyStruct { a: 0, b: 1 };
const ENUM_INSTANCE: AnyEnum = AnyEnum::A('any enum');
const BOOL_FIXED_SIZE_ARRAY: [bool; 2] = [true, false];
```

Nonetheless, it is possible to use the `consteval_int!` macro to create a `const` variable that is the result of some computation:

```cairo, noplayground
    const ONE_HOUR_IN_SECONDS: u32 = consteval_int!(60 * 60);
```

We will dive into more detail about macros in the [dedicated section](./ch12-05-macros.md).

Cairo's naming convention for constants is to use all uppercase with underscores between words.

Constants are valid for the entire time a program runs, within the scope in
which they were declared. This property makes constants useful for values in
your application domain that multiple parts of the program might need to know
about, such as the maximum number of points any player of a game is allowed to
earn, or the speed of light.

Naming hardcoded values used throughout your program as constants is useful in
conveying the meaning of that value to future maintainers of the code. It also
helps to have only one place in your code you would need to change if the
hardcoded value needed to be updated in the future.

[data-types]: ./ch02-02-data-types.md

## Shadowing

Variable shadowing refers to the declaration of a
new variable with the same name as a previous variable. Caironautes say that the
first variable is _shadowed_ by the second, which means that the second
variable is what the compiler will see when you use the name of the variable.
In effect, the second variable overshadows the first, taking any uses of the
variable name to itself until either it itself is shadowed or the scope ends.
We can shadow a variable by using the same variable’s name and repeating the
use of the `let` keyword as follows:

```cairo
fn main() {
    let x = 5;
    let x = x + 1;
    {
        let x = x * 2;
        println!("Inner scope x value is: {}", x);
    }
    println!("Outer scope x value is: {}", x);
}
```

This program first binds `x` to a value of `5`. Then it creates a new variable
`x` by repeating `let x =`, taking the original value and adding `1` so the
value of `x` is then `6`. Then, within an inner scope created with the curly
brackets, the third `let` statement also shadows `x` and creates a new
variable, multiplying the previous value by `2` to give `x` a value of `12`.
When that scope is over, the inner shadowing ends and `x` returns to being `6`.
When we run this program, it will output the following:

```shell
$ scarb execute
   Compiling no_listing_03_shadowing v0.1.0 (listings/ch02-common-programming-concepts/no_listing_03_shadowing/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_03_shadowing
Inner scope x value is: 12
Outer scope x value is: 6
Run completed successfully, returning []

```

Shadowing is different from marking a variable as `mut` because we’ll get a
compile-time error if we accidentally try to reassign to this variable without
using the `let` keyword. By using `let`, we can perform a few transformations
on a value but have the variable be immutable after those transformations have
been completed.

Another distinction between `mut` and shadowing is that when we use the `let` keyword again,
we are effectively creating a new variable, which allows us to change the type of the
value while reusing the same name. As mentioned before, variable shadowing and mutable variables
are equivalent at the lower level.
The only difference is that by shadowing a variable, the compiler will not complain
if you change its type. For example, say our program performs a type conversion between the
`u64` and `felt252` types.

```cairo
fn main() {
    let x: u64 = 2;
    println!("The value of x is {} of type u64", x);
    let x: felt252 = x.into(); // converts x to a felt, type annotation is required.
    println!("The value of x is {} of type felt252", x);
}
```

The first `x` variable has a `u64` type while the second `x` variable has a `felt252` type.
Shadowing thus spares us from having to come up with different names, such as `x_u64`
and `x_felt252`; instead, we can reuse the simpler `x` name. However, if we try to use
`mut` for this, as shown here, we’ll get a compile-time error:

```cairo,does_not_compile
fn main() {
    let mut x: u64 = 2;
    println!("The value of x is: {}", x);
    x = 5_u8;
    println!("The value of x is: {}", x);
}
```

The error says we were expecting a `u64` (the original type) but we got a different type:

```shell
$ scarb execute
   Compiling no_listing_05_mut_cant_change_type v0.1.0 (listings/ch02-common-programming-concepts/no_listing_05_mut_cant_change_type/Scarb.toml)
error: Unexpected argument type. Expected: "core::integer::u64", found: "core::integer::u8".
 --> listings/ch02-common-programming-concepts/no_listing_05_mut_cant_change_type/src/lib.cairo:6:9
    x = 5_u8;
        ^**^

error: could not compile `no_listing_05_mut_cant_change_type` due to previous error
error: `scarb metadata` exited with error

```

<div class="quiz-placeholder" data-quiz-name="&quot;ch02-01-variables-and-mutability&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;id&quot;:&quot;17e3db31-79aa-44b6-9dc2-be8b37b83ada&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;```rust\nlet mut x = 99;\n```\n&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;```rust\nconst MINUTES_PER_HOUR = 60;\n```\n&quot;,&quot;```rust\nlet y = 10;\n```\n&quot;],&quot;prompt&quot;:&quot;Which syntax creates a variable that can be reassigned?&quot;}},{&quot;id&quot;:&quot;0a902a6d-3fca-4d72-b455-5e9ab12441d9&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;`Final balance is: 6`&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;`Final balance is: 12`&quot;,&quot;The program won't compile.&quot;],&quot;prompt&quot;:&quot;What will be the output of the following program?\n```rust\nfn main() {\n    let initial_balance = 9;\n    let initial_balance = initial_balance - 3;\n    {\n        let initial_balance = initial_balance * 2;\n    }\n    println!(\&quot;Final balance is: {}\&quot;, initial_balance);\n}\n```\n&quot;}}]}"></div>

Now that we’ve explored how variables work, let’s look at more data types they can have.


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Data Types

Every value in Cairo is of a certain _data type_, which tells Cairo what kind of
data is being specified so it knows how to work with that data. This section covers two subsets of data types: scalars and compounds.

Keep in mind that Cairo is a _statically typed_ language, which means that it
must know the types of all variables at compile time. The compiler can usually infer the desired type based on the value and its usage. In cases when many types are possible, we can use a conversion method where we specify the desired output type.

```cairo
fn main() {
    let x: felt252 = 3;
    let y: u32 = x.try_into().unwrap();
}
```

You’ll see different type annotations for other data types.

## Scalar Types

A _scalar_ type represents a single value. Cairo has three primary scalar types:
felts, integers, and booleans. You may recognize
these from other programming languages. Let’s jump into how they work in Cairo.

### Felt Type

In Cairo, if you don't specify the type of a variable or argument, its type defaults to a field element, represented by the keyword `felt252`. In the context of Cairo, when we say “a field element” we mean an integer in the range \\( 0 \leq x < P \\),
where \\( P \\) is a very large prime number currently equal to \\( {2^{251}} + 17 \cdot {2^{192}} + 1 \\). When adding, subtracting, or multiplying, if the result falls outside the specified range of the prime number, an overflow (or underflow) occurs, and an appropriate multiple of \\( P \\) is added or subtracted to bring the result back within the range (i.e., the result is computed \\( \mod P \\) ).

The most important difference between integers and field elements is division: Division of field elements (and therefore division in Cairo) is unlike regular CPUs division, where
integer division \\( \frac{x}{y} \\) is defined as \\( \left\lfloor \frac{x}{y} \right\rfloor \\)
where the integer part of the quotient is returned (so you get \\( \frac{7}{3} = 2 \\)) and it may or may not satisfy the equation \\( \frac{x}{y} \cdot y == x \\),
depending on the divisibility of `x` by `y`.

In Cairo, the result of \\( \frac{x}{y} \\) is defined to always satisfy the equation \\( \frac{x}{y} \cdot y == x \\). If y divides x as integers, you will get the expected result in Cairo (for example \\( \frac{6}{2} \\) will indeed result in `3`).
But when y does not divide x, you may get a surprising result: for example, since \\( 2 \cdot \frac{P + 1}{2} = P + 1 \equiv 1 \mod P \\), the value of \\( \frac{1}{2} \\) in Cairo is \\( \frac{P + 1}{2} \\) (and not 0 or 0.5), as it satisfies the above equation.

### Integer Types

The felt252 type is a fundamental type that serves as the basis for creating all types in the core library.
However, it is highly recommended for programmers to use the integer types instead of the `felt252` type whenever possible, as the `integer` types come with added security features that provide extra protection against potential vulnerabilities in the code, such as overflow and underflow checks. By using these integer types, programmers can ensure that their programs are more secure and less susceptible to attacks or other security threats.
An `integer` is a number without a fractional component. This type declaration indicates the number of bits the programmer can use to store the integer.
Table 3-1 shows the built-in integer types in Cairo. We can use any of these variants to declare the type of an integer value.

| Length  | Unsigned |
| ------- | -------- |
| 8-bit   | `u8`     |
| 16-bit  | `u16`    |
| 32-bit  | `u32`    |
| 64-bit  | `u64`    |
| 128-bit | `u128`   |
| 256-bit | `u256`   |
| 32-bit  | `usize`  |

<br>
<div align="center"><span class="caption">Table 3-1: Integer Types in Cairo.</span></div>

Each variant has an explicit size. Note that for now, the `usize` type is just an alias for `u32`; however, it might be useful when in the future Cairo can be compiled to MLIR.
As variables are unsigned, they can't contain a negative number. This code will cause the program to panic:

```cairo
fn sub_u8s(x: u8, y: u8) -> u8 {
    x - y
}

fn main() {
    sub_u8s(1, 3);
}
```

All integer types previously mentioned fit into a `felt252`, except for `u256` which needs 4 more bits to be stored. Under the hood, `u256` is basically a struct with 2 fields: `u256 {low: u128, high: u128}`.

Cairo also provides support for signed integers, starting with the prefix `i`. These integers can represent both positive and negative values, with sizes ranging from `i8` to `i128`.
Each signed variant can store numbers from \\( -({2^{n - 1}}) \\) to \\( {2^{n - 1}} - 1 \\) inclusive, where `n` is the number of bits that variant uses. So an i8 can store numbers from \\( -({2^7}) \\) to \\( {2^7} - 1 \\), which equals `-128` to `127`.

You can write integer literals in any of the forms shown in Table 3-2. Note
that number literals that can be multiple numeric types allow a type suffix,
such as `57_u8`, to designate the type.
It is also possible to use a visual separator `_` for number literals, in order to improve code readability.

| Numeric literals | Example   |
| ---------------- | --------- |
| Decimal          | `98222`   |
| Hex              | `0xff`    |
| Octal            | `0o04321` |
| Binary           | `0b01`    |

<br>
<div align="center"><span class="caption">Table 3-2: Integer Literals in Cairo.</span></div>

So how do you know which type of integer to use? Try to estimate the max value your int can have and choose the good size.
The primary situation in which you’d use `usize` is when indexing some sort of collection.

### Numeric Operations

Cairo supports the basic mathematical operations you’d expect for all the integer
types: addition, subtraction, multiplication, division, and remainder. Integer
division truncates toward zero to the nearest integer. The following code shows
how you’d use each numeric operation in a `let` statement:

```cairo
fn main() {
    // addition
    let sum = 5_u128 + 10_u128;

    // subtraction
    let difference = 95_u128 - 4_u128;

    // multiplication
    let product = 4_u128 * 30_u128;

    // division
    let quotient = 56_u128 / 32_u128; //result is 1
    let quotient = 64_u128 / 32_u128; //result is 2

    // remainder
    let remainder = 43_u128 % 5_u128; // result is 3
}
```

Each expression in these statements uses a mathematical operator and evaluates
to a single value, which is then bound to a variable.

[Appendix B][operators] contains a list of all operators that Cairo provides.

[operators]: ./appendix-02-operators-and-symbols.md#operators

### The Boolean Type

As in most other programming languages, a Boolean type in Cairo has two possible
values: `true` and `false`. Booleans are one `felt252` in size. The Boolean type in
Cairo is specified using `bool`. For example:

```cairo
fn main() {
    let t = true;

    let f: bool = false; // with explicit type annotation
}
```

When declaring a `bool` variable, it is mandatory to use either `true` or `false` literals as value. Hence, it is not allowed to use integer literals (i.e. `0` instead of false) for `bool` declarations.

The main way to use Boolean values is through conditionals, such as an `if`
expression. We’ll cover how `if` expressions work in Cairo in the ["Control Flow"][control-flow] section.

[control-flow]: ./ch02-05-control-flow.md

### String Types

Cairo doesn't have a native type for strings but provides two ways to handle them: short strings using simple quotes and ByteArray using double quotes.

#### Short strings

A short string is an ASCII string where each character is encoded on one byte (see the [ASCII table][ascii]). For example:

- `'a'` is equivalent to `0x61`
- `'b'` is equivalent to `0x62`
- `'c'` is equivalent to `0x63`
- `0x616263` is equivalent to `'abc'`.

Cairo uses the `felt252` for short strings. As the `felt252` is on 251 bits, a short string is limited to 31 characters (31 \* 8 = 248 bits, which is the maximum multiple of 8 that fits in 251 bits).

You can choose to represent your short string with an hexadecimal value like `0x616263` or by directly writing the string using simple quotes like `'abc'`, which is more convenient.

Here are some examples of declaring short strings in Cairo:

```cairo
# fn main() {
    let my_first_char = 'C';
    let my_first_char_in_hex = 0x43;

    let my_first_string = 'Hello world';
    let my_first_string_in_hex = 0x48656C6C6F20776F726C64;
#
#     let long_string: ByteArray = "this is a string which has more than 31 characters";
# }
```

[ascii]: https://www.asciitable.com/

#### Byte Array Strings

Cairo's Core Library provides a `ByteArray` type for handling strings and byte sequences longer than short strings. This type is particularly useful for longer strings or when you need to perform operations on the string data.

The `ByteArray` in Cairo is implemented as a combination of two parts:

1. An array of `bytes31` words, where each word contains 31 bytes of data.
2. A pending `felt252` word that acts as a buffer for bytes that haven't yet filled a complete `bytes31` word.

This design enables efficient handling of byte sequences while aligning with Cairo's memory model and basic types. Developers interact with `ByteArray` through its provided methods and operators, abstracting away the internal implementation details.

Unlike short strings, `ByteArray` strings can contain more than 31 characters and are written using double quotes:

```cairo
# fn main() {
#     let my_first_char = 'C';
#     let my_first_char_in_hex = 0x43;
#
#     let my_first_string = 'Hello world';
#     let my_first_string_in_hex = 0x48656C6C6F20776F726C64;
#
    let long_string: ByteArray = "this is a string which has more than 31 characters";
# }
```

## Compound Types

### The Tuple Type

A _tuple_ is a general way of grouping together a number of values with a
variety of types into one compound type. Tuples have a fixed length: once
declared, they cannot grow or shrink in size.

We create a tuple by writing a comma-separated list of values inside
parentheses. Each position in the tuple has a type, and the types of the
different values in the tuple don’t have to be the same. We’ve added optional
type annotations in this example:

```cairo
fn main() {
    let tup: (u32, u64, bool) = (10, 20, true);
}
```

The variable `tup` binds to the entire tuple because a tuple is considered a
single compound element. To get the individual values out of a tuple, we can
use pattern matching to destructure a tuple value, like this:

```cairo
fn main() {
    let tup = (500, 6, true);

    let (x, y, z) = tup;

    if y == 6 {
        println!("y is 6!");
    }
}
```

This program first creates a tuple and binds it to the variable `tup`. It then
uses a pattern with `let` to take `tup` and turn it into three separate
variables, `x`, `y`, and `z`. This is called _destructuring_ because it breaks
the single tuple into three parts. Finally, the program prints `y is 6!` as the value of
`y` is `6`.

We can also declare the tuple with value and types, and destructure it at the same time.
For example:

```cairo
fn main() {
    let (x, y): (felt252, felt252) = (2, 3);
}
```

#### The Unit Type ()

A _unit type_ is a type which has only one value `()`.
It is represented by a tuple with no elements.
Its size is always zero, and it is guaranteed to not exist in the compiled code.

You might be wondering why you would even need a unit type? In Cairo, everything is an expression, and an expression that returns nothing actually returns `()` implicitly.

### The Fixed Size Array Type

Another way to have a collection of multiple values is with a _fixed size array_. Unlike a tuple, every element of a fixed size array must have the same type.

We write the values in a fixed-size array as a comma-separated list inside square brackets. The array’s type is written using square brackets with the type of each element, a semicolon, and then the number of elements in the array, like so:

```cairo
fn main() {
    let arr1: [u64; 5] = [1, 2, 3, 4, 5];
}
```

In the type annotation `[u64; 5]`, `u64` specifies the type of each element, while `5` after the semicolon defines the array's length. This syntax ensures that the array always contains exactly 5 elements of type `u64`.

Fixed size arrays are useful when you want to hardcode a potentially long sequence of data directly in your program. This type of array must not be confused with the [`Array<T>` type][arrays], which is a similar collection type provided by the core library that _is_ allowed to grow in size. If you're unsure whether to use a fixed size array or the `Array<T>` type, chances are that you are looking for the `Array<T>` type.

Because their size is known at compile-time, fixed-size arrays don't require runtime memory management, which makes them more efficient than dynamically-sized arrays. Overall, they're more useful when you know the number of elements will not need to change. For example, they can be used to efficiently store lookup tables that won't change during runtime. If you were using the names of the month in a program, you would probably use a fixed size array rather than an `Array<T>` because you know it will always contain 12 elements:

```cairo
    let months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
        'October', 'November', 'December',
    ];

```

You can also initialize an array to contain the same value for each element by specifying the initial value, followed by a semicolon, and then the length of the array in square brackets, as shown here:

```cairo
    let a = [3; 5];
```

The array named `a` will contain `5` elements that will all be set to the value `3` initially. This is the same as writing `let a = [3, 3, 3, 3, 3];` but in a more concise way.

#### Accessing Fixed Size Arrays Elements

As a fixed-size array is a data structure known at compile time, it's content is represented as a sequence of values in the program bytecode. Accessing an element of that array will simply read that value from the program bytecode efficiently.

We have two different ways of accessing fixed size array elements:

- Deconstructing the array into multiple variables, as we did with tuples.

```cairo
fn main() {
    let my_arr = [1, 2, 3, 4, 5];

    // Accessing elements of a fixed-size array by deconstruction
    let [a, b, c, _, _] = my_arr;
    println!("c: {}", c); // c: 3
}
```

- Converting the array to a [Span][span], that supports indexing. This operation is _free_ and doesn't incur any runtime cost.

```cairo
fn main() {
    let my_arr = [1, 2, 3, 4, 5];

    // Accessing elements of a fixed-size array by index
    let my_span = my_arr.span();
    println!("my_span[2]: {}", my_span[2]); // my_span[2]: 3
}
```

Note that if we plan to repeatedly access the array, then it makes sense to call `.span()` only once and keep it available throughout the accesses.

## Type Conversion

Cairo addresses conversion between types by using the `try_into` and `into` methods provided by the `TryInto` and `Into` traits from the core library. There are numerous implementations of these traits within the standard library for conversion between types, and they can be implemented for [custom types as well][custom-type-conversion].

### Into

The `Into` trait allows for a type to define how to convert itself into another type. It can be used for type conversion when success is guaranteed, such as when the source type is smaller than the destination type.

To perform the conversion, call `var.into()` on the source value to convert it to another type. The new variable's type must be explicitly defined, as demonstrated in the example below.

```cairo
fn main() {
    let my_u8: u8 = 10;
    let my_u16: u16 = my_u8.into();
    let my_u32: u32 = my_u16.into();
    let my_u64: u64 = my_u32.into();
    let my_u128: u128 = my_u64.into();

    let my_felt252 = 10;
    // As a felt252 is smaller than a u256, we can use the into() method
    let my_u256: u256 = my_felt252.into();
    let my_other_felt252: felt252 = my_u8.into();
    let my_third_felt252: felt252 = my_u16.into();
}
```

### TryInto

Similar to `Into`, `TryInto` is a generic trait for converting between types. Unlike `Into`, the `TryInto` trait is used for fallible conversions, and as such, returns [Option\<T\>][option]. An example of a fallible conversion is when the target type might not fit the source value.

Also similar to `Into` is the process to perform the conversion; just call `var.try_into()` on the source value to convert it to another type. The new variable's type also must be explicitly defined, as demonstrated in the example below.

```cairo
fn main() {
    let my_u256: u256 = 10;

    // Since a u256 might not fit in a felt252, we need to unwrap the Option<T> type
    let my_felt252: felt252 = my_u256.try_into().unwrap();
    let my_u128: u128 = my_felt252.try_into().unwrap();
    let my_u64: u64 = my_u128.try_into().unwrap();
    let my_u32: u32 = my_u64.try_into().unwrap();
    let my_u16: u16 = my_u32.try_into().unwrap();
    let my_u8: u8 = my_u16.try_into().unwrap();

    let my_large_u16: u16 = 2048;
    let my_large_u8: u8 = my_large_u16.try_into().unwrap(); // panics with 'Option::unwrap failed.'
}
```

<div class="quiz-placeholder" data-quiz-name="&quot;ch02-02-data-types&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;In general, a **signed** number with *n* bits can represent numbers between -(2&lt;sup&gt;n - 1&lt;/sup&gt;) and 2&lt;sup&gt;n - 1&lt;/sup&gt; - 1. For **unsigned** numbers the range is from 0 to 2&lt;sup&gt;n&lt;/sup&gt; - 1.\n&quot;,&quot;id&quot;:&quot;4fd0bdba-6ef4-44ad-b552-953b09b814d7&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;2&lt;sup&gt;127&lt;/sup&gt; - 1&quot;},&quot;prompt&quot;:{&quot;answerIndex&quot;:3,&quot;distractors&quot;:[&quot;2&lt;sup&gt;127&lt;/sup&gt;&quot;,&quot;2&lt;sup&gt;128&lt;/sup&gt;&quot;,&quot;This type can hold any number.&quot;],&quot;prompt&quot;:&quot;The largest number representable by the type `i128` is:&quot;}},{&quot;context&quot;:&quot;`u8` is an unsigned integer type which cannot contain negative numbers.\n&quot;,&quot;id&quot;:&quot;4d5cab51-6eca-4aa0-8666-993acdd85c8d&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;It will always panic.&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;It will return `-1`.&quot;,&quot;Compiler will issue a warning about underflow.&quot;],&quot;prompt&quot;:&quot;If `x : u8 = 0`, what will happen when computing `x - 1`?&quot;}},{&quot;context&quot;:&quot;The type `felt32` does not exist. Proper field type is `felt252`.\n&quot;,&quot;id&quot;:&quot;dc1e6fa1-0d7b-479e-98ac-6a514d60eb1b&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false,&quot;lineNumber&quot;:2},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n  let x: felt32 = 2;\n  println!(\&quot;{x}\&quot;);\n}\n&quot;}}]}"></div>

[arrays]: ./ch03-01-arrays.md
[option]: ./ch06-01-enums.md#the-option-enum-and-its-advantages
[custom-type-conversion]: ./ch05-02-an-example-program-using-structs.md#conversions-of-custom-types
[span]: ./ch03-01-arrays.md#Span


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Functions

Functions are prevalent in Cairo code. You’ve already seen one of the most
important functions in the language: the `main` function, which is the entry
point of many programs. You’ve also seen the `fn` keyword, which allows you to
declare new functions.

Cairo code uses _snake case_ as the conventional style for function and variable
names, in which all letters are lowercase and underscores separate words.
Here’s a program that contains an example function definition:

```cairo
fn another_function() {
    println!("Another function.");
}

fn main() {
    println!("Hello, world!");
    another_function();
}
```

We define a function in Cairo by entering `fn` followed by a function name and a
set of parentheses. The curly brackets tell the compiler where the function
body begins and ends.

We can call any function we’ve defined by entering its name followed by a set
of parentheses. Because `another_function` is defined in the program, it can be
called from inside the `main` function. Note that we defined `another_function`
_before_ the `main` function in the source code; we could have defined it after
as well. Cairo doesn’t care where you define your functions, only that they’re
defined somewhere in a scope that can be seen by the caller.

Let’s start a new project with Scarb named _functions_ to explore functions
further. Place the `another_function` example in _src/lib.cairo_ and run it. You
should see the following output:

```shell
$ scarb execute
   Compiling no_listing_15_functions v0.1.0 (listings/ch02-common-programming-concepts/no_listing_15_functions/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_15_functions
Hello, world!
Another function.
Run completed successfully, returning []

```

The lines execute in the order in which they appear in the `main` function.
First the `Hello, world!` message prints, and then `another_function` is called
and its message is printed.

## Parameters

We can define functions to have _parameters_, which are special variables that
are part of a function’s signature. When a function has parameters, you can
provide it with concrete values for those parameters. Technically, the concrete
values are called _arguments_, but in casual conversation, people tend to use
the words _parameter_ and _argument_ interchangeably for either the variables
in a function’s definition or the concrete values passed in when you call a
function.

In this version of `another_function` we add a parameter:

```cairo
fn main() {
    another_function(5);
}

fn another_function(x: felt252) {
    println!("The value of x is: {}", x);
}
```

Try running this program; you should get the following output:

```shell
$ scarb execute
   Compiling no_listing_16_single_param v0.1.0 (listings/ch02-common-programming-concepts/no_listing_16_single_param/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_16_single_param
The value of x is: 5
Run completed successfully, returning []

```

The declaration of `another_function` has one parameter named `x`. The type of
`x` is specified as `felt252`. When we pass `5` in to `another_function`, the
`println!` macro puts `5` where the pair of curly brackets containing `x` was in the format string.

In function signatures, you _must_ declare the type of each parameter. This is
a deliberate decision in Cairo’s design: requiring type annotations in function
definitions means the compiler almost never needs you to use them elsewhere in
the code to figure out what type you mean. The compiler is also able to give
more helpful error messages if it knows what types the function expects.

When defining multiple parameters, separate the parameter declarations with
commas, like this:

```cairo
fn main() {
    print_labeled_measurement(5, "h");
}

fn print_labeled_measurement(value: u128, unit_label: ByteArray) {
    println!("The measurement is: {value}{unit_label}");
}
```

This example creates a function named `print_labeled_measurement` with two
parameters. The first parameter is named `value` and is a `u128`. The second is
named `unit_label` and is of type `ByteArray` - Cairo's internal type to represent string literals. The function then prints text containing both the `value` and the `unit_label`.

Let’s try running this code. Replace the program currently in your _functions_
project’s _src/lib.cairo_ file with the preceding example and run it using `scarb execute`:

```shell
$ scarb execute
   Compiling no_listing_17_multiple_params v0.1.0 (listings/ch02-common-programming-concepts/no_listing_17_multiple_params/Scarb.toml)
    Finished `dev` profile target(s) in 5 seconds
     Running no_listing_17_multiple_params
The measurement is: 5h
Run completed successfully, returning []

```

Because we called the function with `5` as the value for value and `"h"` as the value for `unit_label`, the program output contains those values.

### Named Parameters

In Cairo, named parameters allow you to specify the names of arguments when you call a function. This makes the function calls more readable and self-descriptive.
If you want to use named parameters, you need to specify the name of the parameter and the value you want to pass to it. The syntax is `parameter_name: value`. If you pass a variable that has the same name as the parameter, you can simply write `:parameter_name` instead of `parameter_name: variable_name`.

Here is an example:

```cairo
fn foo(x: u8, y: u8) {}

fn main() {
    let first_arg = 3;
    let second_arg = 4;
    foo(x: first_arg, y: second_arg);
    let x = 1;
    let y = 2;
    foo(:x, :y)
}
```

## Statements and Expressions

Function bodies are made up of a series of statements optionally ending in an
expression. So far, the functions we’ve covered haven’t included an ending
expression, but you have seen an expression as part of a statement. Because
Cairo is an expression-based language, this is an important distinction to
understand. Other languages don’t have the same distinctions, so let’s look at
what statements and expressions are and how their differences affect the bodies
of functions.

- **Statements** are instructions that perform some action and do not return
  a value.
- **Expressions** evaluate to a resultant value. Let’s look at some examples.

We’ve actually already used statements and expressions. Creating a variable and
assigning a value to it with the `let` keyword is a statement. In Listing 2-1,
`let y = 6;` is a statement.

```cairo
fn main() {
    let y = 6;
}
```

<span class="caption">Listing 2-1: A `main` function declaration containing one statement</span>

Function definitions are also statements; the entire preceding example is a statement in itself.

Statements do not return values. Therefore, you can’t assign a `let` statement
to another variable, as the following code tries to do; you’ll get an error:

```cairo, noplayground
fn main() {
    let x = (let y = 6);
}
```

When you run this program, the error you’ll get looks like this:

```shell
$ scarb execute
   Compiling no_listing_18_statements_dont_return_values v0.1.0 (listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/Scarb.toml)
error: Missing token TerminalRParen.
 --> listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/src/lib.cairo:3:14
    let x = (let y = 6);
             ^

error: Missing token TerminalSemicolon.
 --> listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/src/lib.cairo:3:14
    let x = (let y = 6);
             ^

error: Missing token TerminalSemicolon.
 --> listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/src/lib.cairo:3:23
    let x = (let y = 6);
                      ^

error: Skipped tokens. Expected: statement.
 --> listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/src/lib.cairo:3:23
    let x = (let y = 6);
                      ^^

warn[E0001]: Unused variable. Consider ignoring by prefixing with `_`.
 --> listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/src/lib.cairo:3:9
    let x = (let y = 6);
        ^

warn[E0001]: Unused variable. Consider ignoring by prefixing with `_`.
 --> listings/ch02-common-programming-concepts/no_listing_20_statements_dont_return_values/src/lib.cairo:3:18
    let x = (let y = 6);
                 ^

error: could not compile `no_listing_18_statements_dont_return_values` due to previous error
error: `scarb metadata` exited with error

```

The `let y = 6` statement does not return a value, so there isn’t anything for
`x` to bind to. This is different from what happens in other languages, such as
C and Ruby, where the assignment returns the value of the assignment. In those
languages, you can write `x = y = 6` and have both `x` and `y` have the value
`6`; that is not the case in Cairo.

Expressions evaluate to a value and make up most of the rest of the code that
you’ll write in Cairo. Consider a math operation, such as `5 + 6`, which is an
expression that evaluates to the value `11`. Expressions can be part of
statements: in Listing 2-1, the `6` in the statement `let y = 6;` is an
expression that evaluates to the value `6`.

Calling a function is an expression since it always evaluates to a value: the function's explicit return value, if specified, or the 'unit' type `()` otherwise.

A new scope block created with curly brackets is an expression, for example:

```cairo
fn main() {
    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {}", y);
}
```

This expression:

```cairo, noplayground
    let y = {
        let x = 3;
        x + 1
    };
```

is a block that, in this case, evaluates to `4`. That value gets bound to `y`
as part of the `let` statement. Note that the `x + 1` line doesn’t have a
semicolon at the end, which is unlike most of the lines you’ve seen so far.
Expressions do not include ending semicolons. If you add a semicolon to the end
of an expression, you turn it into a statement, and it will then not return a
value. Keep this in mind as you explore function return values and expressions
next.

## Functions with Return Values

Functions can return values to the code that calls them. We don’t name return
values, but we must declare their type after an arrow (`->`). In Cairo, the
return value of the function is synonymous with the value of the final
expression in the block of the body of a function. You can return early from a
function by using the `return` keyword and specifying a value, but most
functions return the last expression implicitly. Here’s an example of a
function that returns a value:

```cairo
fn five() -> u32 {
    5
}

fn main() {
    let x = five();
    println!("The value of x is: {}", x);
}
```

There are no function calls, or even `let` statements in the `five`
function—just the number `5` by itself. That’s a perfectly valid function in
Cairo. Note that the function’s return type is specified too, as `-> u32`. Try
running this code; the output should look like this:

```shell
$ scarb execute
   Compiling no_listing_20_function_return_values v0.1.0 (listings/ch02-common-programming-concepts/no_listing_22_function_return_values/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_20_function_return_values
The value of x is: 5
Run completed successfully, returning []

```

The `5` in `five` is the function’s return value, which is why the return type
is `u32`. Let’s examine this in more detail. There are two important bits:
first, the line `let x = five();` shows that we’re using the return value of a
function to initialize a variable. Because the function `five` returns a `5`,
that line is the same as the following:

```cairo, noplayground
let x = 5;
```

Second, the `five` function has no parameters and defines the type of the
return value, but the body of the function is a lonely `5` with no semicolon
because it’s an expression whose value we want to return.
Let’s look at another example:

```cairo
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {}", x);
}

fn plus_one(x: u32) -> u32 {
    x + 1
}
```

Running this code will print `x = 6`. But if we place a
semicolon at the end of the line containing `x + 1`, changing it from an
expression to a statement, we’ll get an error:

```cairo,does_not_compile
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {}", x);
}

fn plus_one(x: u32) -> u32 {
    x + 1;
}
```

```shell
$ scarb execute
   Compiling no_listing_22_function_return_invalid v0.1.0 (listings/ch02-common-programming-concepts/no_listing_24_function_return_invalid/Scarb.toml)
error: Unexpected return type. Expected: "core::integer::u32", found: "()".
 --> listings/ch02-common-programming-concepts/no_listing_24_function_return_invalid/src/lib.cairo:9:28
fn plus_one(x: u32) -> u32 {
                           ^

error: could not compile `no_listing_22_function_return_invalid` due to previous error
error: `scarb metadata` exited with error

```

The main error message, `Unexpected return type`, reveals the core issue with this
code. The definition of the function `plus_one` says that it will return an
`u32`, but statements don’t evaluate to a value, which is expressed by `()`,
the unit type. Therefore, nothing is returned, which contradicts the function
definition and results in an error.

### Const Functions

Functions that can be evaluated at compile time can be marked as `const` using the `const fn` syntax. This allows the function to be called from a constant context and interpreted by the compiler at compile time.

Declaring a function as `const` restricts the types that arguments and the return type may use, and limits the function body to constant expressions.

Several functions in the core library are marked as `const`. Here's an example from the core library showing the `pow` function implemented as a `const fn`:

```cairo
use core::num::traits::Pow;

const BYTE_MASK: u16 = 2_u16.pow(8) - 1;

fn main() {
    let my_value = 12345;
    let first_byte = my_value & BYTE_MASK;
    println!("first_byte: {}", first_byte);
}
```

In this example, `pow` is a `const` function, allowing it to be used in a constant expression to define `mask` at compile time. Here's a snippet of how `pow` is defined in the core library using `const fn`:

Note that declaring a function as `const` has no effect on existing uses; it only imposes restrictions for constant contexts.

<div class="quiz-placeholder" data-quiz-name="&quot;ch02-03-functions&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;id&quot;:&quot;fa63d18f-fee3-4923-962b-bdeabbf61fbd&quot;,&quot;type&quot;:&quot;ShortAnswer&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;fn&quot;},&quot;prompt&quot;:{&quot;prompt&quot;:&quot;The keyword for declaring a new function in Cairo is:&quot;}},{&quot;context&quot;:&quot;A function must declare the types of its parameters. In this case, function `f` could be corrected by adding `u8` type to the `x` parameter like this: `fn f(x:u8)`.\n&quot;,&quot;id&quot;:&quot;6343598f-380f-4a59-b6fb-7dfadc397f74&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false,&quot;lineNumber&quot;:1},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn f(x) { \n  println!(\&quot;{x}\&quot;);\n}\n\nfn main() {\n  f(0);\n}\n&quot;}},{&quot;context&quot;:&quot;A block is an expression (#1) that is allowed to contain statements. It also defines a syntactic scope for let-bindings inside it (#3).\n&quot;,&quot;id&quot;:&quot;695f318f-539b-4ce8-9c00-92e29f7f1bb3&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;1 and 3&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;1 only&quot;,&quot;2 only&quot;,&quot;2 and 3&quot;],&quot;prompt&quot;:&quot;In Cairo, a curly-brace block like `{ /* ... */ }` is:\n1. An expression\n2. A statement\n3. A syntactic scope\n&quot;}},{&quot;id&quot;:&quot;7bbc0afb-2ad7-4d8d-97fd-610a65a85e38&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;3&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn f(x: usize) -&gt; usize { x + 1 }\nfn main() {\n  println!(\&quot;{}\&quot;, f({\n    let y = 1;\n    y + 1\n  }));\n}\n&quot;}}]}"></div>


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Comments

All programmers strive to make their code easy to understand, but sometimes extra explanation is warranted. In these cases, programmers leave comments in their source code that the compiler will ignore but people reading the source code may find useful.

Here’s a simple comment:

```cairo,noplayground
// hello, world
```

In Cairo, the idiomatic comment style starts a comment with two slashes, and the comment continues until the end of the line. For comments that extend beyond a single line, you’ll need to include `//` on each line, like this:

```cairo,noplayground
// So we’re doing something complicated here, long enough that we need
// multiple lines of comments to do it! Whew! Hopefully, this comment will
// explain what’s going on.
```

Comments can also be placed at the end of lines containing code:

```cairo
fn main() -> felt252 {
    1 + 4 // return the sum of 1 and 4
}
```

But you’ll more often see them used in this format, with the comment on a separate line above the code it’s annotating:

```cairo
fn main() -> felt252 {
    // this function performs a simple addition
    1 + 4
}
```

## Item-level Documentation

Item-level documentation comments refer to specific items such as functions, implementations, traits, etc. They are prefixed with three slashes (`///`). These comments provide a detailed description of the item, examples of usage, and any conditions that might cause a panic. In case of functions, the comments may also include separate sections for parameter and return value descriptions.

```cairo,noplayground
/// Returns the sum of `arg1` and `arg2`.
/// `arg1` cannot be zero.
///
/// # Panics
///
/// This function will panic if `arg1` is `0`.
///
/// # Examples
///
/// ```
/// let a: felt252 = 2;
/// let b: felt252 = 3;
/// let c: felt252 = add(a, b);
/// assert(c == a + b, "Should equal a + b");
/// ```
fn add(arg1: felt252, arg2: felt252) -> felt252 {
    assert(arg1 != 0, 'Cannot be zero');
    arg1 + arg2
}
```

## Module Documentation

Module documentation comments provide an overview of the entire module, including its purpose and examples of use. These comments are meant to be placed above the module they're describing and are prefixed with `//!`. This type of documentation gives a broad understanding of what the module does and how it can be used.

```cairo,noplayground
//! # my_module and implementation
//!
//! This is an example description of my_module and some of its features.
//!
//! # Examples
//!
//! ```
//! mod my_other_module {
//!   use path::to::my_module;
//!
//!   fn foo() {
//!     my_module.bar();
//!   }
//! }
//! ```
mod my_module { // rest of implementation...
}
```

<div class="quiz-placeholder" data-quiz-name="&quot;ch02-04-comments&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;id&quot;:&quot;ed752dc7-dffd-4ccb-9571-fd442aafe998&quot;,&quot;type&quot;:&quot;ShortAnswer&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;//&quot;},&quot;prompt&quot;:{&quot;prompt&quot;:&quot;What is the syntax introducing a comment?&quot;}}]}"></div>


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Control Flow

The ability to run some code depending on whether a condition is true and to run some code repeatedly while a condition is true are basic building blocks in most programming languages. The most common constructs that let you control the flow of execution of Cairo code are if expressions and loops.

## `if` Expressions

An if expression allows you to branch your code depending on conditions. You provide a condition and then state, “If this condition is met, run this block of code. If the condition is not met, do not run this block of code.”

Create a new project called _branches_ in your _cairo_projects_ directory to explore the `if` expression. In the _src/lib.cairo_ file, input the following:

```cairo
fn main() {
    let number = 3;

    if number == 5 {
        println!("condition was true and number = {}", number);
    } else {
        println!("condition was false and number = {}", number);
    }
}
```

All `if` expressions start with the keyword `if`, followed by a condition. In this case, the condition checks whether or not the variable `number` has a value equal to 5. We place the block of code to execute if the condition is `true` immediately after the condition inside curly brackets.

Optionally, we can also include an `else` expression, which we chose to do here, to give the program an alternative block of code to execute should the condition evaluate to `false`. If you don’t provide an `else` expression and the condition is `false`, the program will just skip the `if` block and move on to the next bit of code.

Try running this code; you should see the following output:

```shell
$ scarb execute
   Compiling no_listing_24_if v0.1.0 (listings/ch02-common-programming-concepts/no_listing_27_if/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_24_if
condition was false and number = 3
Run completed successfully, returning []

```

Let’s try changing the value of `number` to a value that makes the condition `true` to see what happens:

```cairo, noplayground
    let number = 5;
```

```shell
$ scarb execute
condition was true and number = 5
Run completed successfully, returning []
```

It’s also worth noting that the condition in this code must be a `bool`. If the condition isn’t a `bool`, we’ll get an error. For example, try running the following code:

```cairo
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

The `if` condition evaluates to a value of 3 this time, and Cairo throws an error:

```shell
$ scarb build
   Compiling no_listing_28_bis_if_not_bool v0.1.0 (listings/ch02-common-programming-concepts/no_listing_28_bis_if_not_bool/Scarb.toml)
error: Mismatched types. The type `core::bool` cannot be created from a numeric literal.
 --> listings/ch02-common-programming-concepts/no_listing_28_bis_if_not_bool/src/lib.cairo:4:18
    let number = 3;
                 ^

error: could not compile `no_listing_28_bis_if_not_bool` due to previous error

```

The error indicates that Cairo inferred the type of `number` to be a `bool`
based on its later use as a condition of the `if` statement. It tries to create
a `bool` from the value `3`, but Cairo doesn't support instantiating a `bool`
from a numeric literal anyway - you can only use `true` or `false` to create a
`bool`. Unlike languages such as Ruby and JavaScript, Cairo will not
automatically try to convert non-Boolean types to a Boolean. If we want the `if`
code block to run only when a number is not equal to 0, for example, we can
change the if expression to the following:

```cairo
fn main() {
    let number = 3;

    if number != 0 {
        println!("number was something other than zero");
    }
}

```

Running this code will print `number was something other than zero`.

## Handling Multiple Conditions with `else if`

You can use multiple conditions by combining `if` and `else` in an `else if` expression. For example:

```cairo
fn main() {
    let number = 3;

    if number == 12 {
        println!("number is 12");
    } else if number == 3 {
        println!("number is 3");
    } else if number - 2 == 1 {
        println!("number minus 2 is 1");
    } else {
        println!("number not found");
    }
}
```

This program has four possible paths it can take. After running it, you should see the following output:

```shell
$ scarb execute
   Compiling no_listing_25_else_if v0.1.0 (listings/ch02-common-programming-concepts/no_listing_30_else_if/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_25_else_if
number is 3
Run completed successfully, returning []

```

When this program executes, it checks each `if` expression in turn and executes the first body for which the condition evaluates to `true`. Note that even though `number - 2 == 1` is `true`, we don’t see the output `number minus 2 is 1` nor do we see the `number not found` text from the `else` block. That’s because Cairo only executes the block for the first true condition, and once it finds one, it doesn’t even check the rest. Using too many `else if` expressions can clutter your code, so if you have more than one, you might want to refactor your code. [Chapter 6][match] describes a powerful Cairo branching construct called `match` for these cases.

[match]: ./ch06-02-the-match-control-flow-construct.md

## Using `if` in a `let` Statement

Because `if` is an expression, we can use it on the right side of a `let` statement to assign the outcome to a variable.

```cairo
fn main() {
    let condition = true;
    let number = if condition {
        5
    } else {
        6
    };

    if number == 5 {
        println!("condition was true and number is {}", number);
    }
}
```

```shell
$ scarb execute
   Compiling no_listing_26_if_let v0.1.0 (listings/ch02-common-programming-concepts/no_listing_31_if_let/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_26_if_let
condition was true and number is 5
Run completed successfully, returning []

```

The `number` variable will be bound to a value based on the outcome of the `if` expression, which will be 5 here.

## Repetition with Loops

It’s often useful to execute a block of code more than once. For this task, Cairo provides a simple loop syntax, which will run through the code inside the loop body to the end and then start immediately back at the beginning. To experiment with loops, let’s create a new project called _loops_.

Cairo has three kinds of loops: `loop`, `while`, and `for`. Let’s try each one.

### Repeating Code with `loop`

The `loop` keyword tells Cairo to execute a block of code over and over again forever or until you explicitly tell it to stop.

As an example, change the _src/lib.cairo_ file in your _loops_ directory to look like this:

```cairo
fn main() {
    loop {
        println!("again!");
    }
}
```

When we run this program, we’ll see `again!` printed over and over continuously until either the program runs out of gas or we stop the program manually. Most terminals support the keyboard shortcut ctrl-c to interrupt a program that is stuck in a continual loop. Give it a try:

```shell
$ scarb execute --available-gas=20000000
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished release target(s) in 0 seconds
     Running loops
again!
again!
again!
^Cagain!
```

The symbol `^C` represents where you pressed ctrl-c. You may or may not see the word `again!` printed after the ^C, depending on where the code was in the loop when it received the interrupt signal.

> Note: Cairo prevents us from running program with infinite loops by including a gas meter. The gas meter is a mechanism that limits the amount of computation that can be done in a program. By setting a value to the `--available-gas` flag, we can set the maximum amount of gas available to the program. Gas is a unit of measurement that expresses the computation cost of an instruction. When the gas meter runs out, the program will stop. In the previous case, we set the gas limit high enough for the program to run for quite some time.

> It is particularly important in the context of smart contracts deployed on Starknet, as it prevents from running infinite loops on the network.
> If you're writing a program that needs to run a loop, you will need to execute it with the `--available-gas` flag set to a value that is large enough to run the program.

Now, try running the same program again, but this time with the `--available-gas` flag set to `200000` instead of `2000000000000`. You will see the program only prints `again!` 3 times before it stops, as it ran out of gas to keep executing the loop.

Fortunately, Cairo also provides a way to break out of a loop using code. You can place the `break` keyword within the loop to tell the program when to stop executing the loop.

```cairo
fn main() {
    let mut i: usize = 0;
    loop {
        if i > 10 {
            break;
        }
        println!("i = {}", i);
        i += 1;
    }
}
```

The `continue` keyword tells the program to go to the next iteration of the loop and to skip the rest of the code in this iteration.
Let's add a `continue` statement to our loop to skip the `println!` statement when `i` is equal to `5`.

```cairo
fn main() {
    let mut i: usize = 0;
    loop {
        if i > 10 {
            break;
        }
        if i == 5 {
            i += 1;
            continue;
        }
        println!("i = {}", i);
        i += 1;
    }
}
```

Executing this program will not print the value of `i` when it is equal to `5`.

### Returning Values from Loops

One of the uses of a `loop` is to retry an operation you know might fail, such
as checking whether an operation has succeeded. You might also need to pass
the result of that operation out of the loop to the rest of your code. To do
this, you can add the value you want returned after the `break` expression you
use to stop the loop; that value will be returned out of the loop so you can
use it, as shown here:

```cairo
fn main() {
    let mut counter = 0;

    let result = loop {
        if counter == 10 {
            break counter * 2;
        }
        counter += 1;
    };

    println!("The result is {}", result);
}
```

Before the loop, we declare a variable named `counter` and initialize it to
`0`. Then we declare a variable named `result` to hold the value returned from
the loop. On every iteration of the loop, we check whether the `counter` is equal to `10`, and then add `1` to the `counter` variable.
When the condition is met, we use the `break` keyword with the value `counter * 2`. After the loop, we use a
semicolon to end the statement that assigns the value to `result`. Finally, we
print the value in `result`, which in this case is `20`.

### Conditional Loops with `while`

A program will often need to evaluate a condition within a loop.
While the condition is `true`, the loop runs.
When the condition ceases to be `true`, the program calls `break`, stopping the loop.
It’s possible to implement behavior like this using a combination of `loop`, `if`, `else`, and `break`; you could try that now in a program, if you’d like.
However, this pattern is so common that Cairo has a built-in language construct for it, called a `while` loop.

In Listing 2-2, we use `while` to loop the program three times, counting down each time after printing the value of `number`, and then, after the loop, print a message and exit.

```cairo
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{number}!");
        number -= 1;
    }

    println!("LIFTOFF!!!");
}
```

<span class="caption">Listing 2-2: Using a `while` loop to run code while a condition holds `true`.</span>

This construct eliminates a lot of nesting that would be necessary if you used `loop`, `if`, `else`, and `break`, and it’s clearer.
While a condition evaluates to `true`, the code runs; otherwise, it exits the loop.

### Looping Through a Collection with `for`

You can also use the while construct to loop over the elements of a collection, such as an array. For example, the loop in Listing 2-3 prints each element in the array `a`.

```cairo
fn main() {
    let a = [10, 20, 30, 40, 50].span();
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);
        index += 1;
    }
}
```

<span class="caption">Listing 2-3: Looping through each element of a collection using a `while` loop</span>

Here, the code counts up through the elements in the array. It starts at index `0`, and then loops until it reaches the final index in the array (that is, when `index < 5` is no longer `true`). Running this code will print every element in the array:

```shell
$ scarb execute
   Compiling no_listing_45_iter_loop_while v0.1.0 (listings/ch02-common-programming-concepts/no_listing_45_iter_loop_while/Scarb.toml)
    Finished `dev` profile target(s) in 4 seconds
     Running no_listing_45_iter_loop_while
the value is: 10
the value is: 20
the value is: 30
the value is: 40
the value is: 50
Run completed successfully, returning []

```

All five array values appear in the terminal, as expected. Even though `index` will reach a value of `5` at some point, the loop stops executing before trying to fetch a sixth value from the array.

However, this approach is error prone; we could cause the program to panic if the index value or test condition is incorrect. For example, if you changed the definition of the `a` array to have four elements but forgot to update the condition to `while index < 4`, the code would panic. It’s also slow, because the compiler adds runtime code to perform the conditional check of whether the index is within the bounds of the array on every iteration through the loop.

As a more concise alternative, you can use a `for` loop and execute some code for each item in a collection. A `for` loop looks like the code in Listing 2-4.

```cairo
fn main() {
    let a = [10, 20, 30, 40, 50].span();

    for element in a {
        println!("the value is: {element}");
    }
}
```

<span class="caption">Listing 2-4: Looping through each element of a collection using a `for` loop</span>

When we run this code, we’ll see the same output as in Listing 2-3. More importantly, we’ve now increased the safety of the code and eliminated the chance of bugs that might result from going beyond the end of the array or not going far enough and missing some items.

Using the `for` loop, you wouldn’t need to remember to change any other code if you changed the number of values in the array, as you would with the method used in Listing 2-3.

The safety and conciseness of `for` loops make them the most commonly used loop construct in Cairo. Even in situations in which you want to run some code a certain number of times, as in the countdown example that used a while loop in Listing 2-2. Another way to run code a certain number of times would be to use a `Range`, provided by the core library, which generates all numbers in sequence starting from one number and ending before another number.

Here’s how you can use a `Range` to count from 1 to 3:

```cairo
fn main() {
    for number in 1..4_u8 {
        println!("{number}!");
    }
    println!("Go!!!");
}
```

This code is a bit nicer, isn’t it?

## Equivalence Between Loops and Recursive Functions

Loops and recursive functions are two common ways to repeat a block of code multiple times. The `loop` keyword is used to create an infinite loop that can be broken by using the `break` keyword.

```cairo
fn main() -> felt252 {
    let mut x: felt252 = 0;
    loop {
        if x == 2 {
            break;
        } else {
            x += 1;
        }
    }
    x
}
```

Loops can be transformed into recursive functions by calling the function within itself. Here is an example of a recursive function that mimics the behavior of the `loop` example above.

```cairo
fn main() -> felt252 {
    recursive_function(0)
}

fn recursive_function(mut x: felt252) -> felt252 {
    if x == 2 {
        x
    } else {
        recursive_function(x + 1)
    }
}
```

In both cases, the code block will run indefinitely until the condition `x == 2` is met, at which point the value of x will be displayed.

In Cairo, loops and recursions are not only conceptually equivalent: they are also compiled down to similar low-level representations. To understand this, we can compile both examples to Sierra, and analyze the Sierra Code generated by the Cairo compiler for both examples. Add the following in your `Scarb.toml` file:

```toml
[lib]
sierra-text = true
```

Then, run `scarb build` to compile both examples. You will find that the Sierra code generated for both examples is extremely similar, as the loop is compiled to a recursive function in the Sierra statements.

> Note: For our example, our findings came from understanding the **statements** section in Sierra that shows the execution traces of the two programs. If you are curious to learn more about Sierra, check out [Exploring Sierra](https://medium.com/nethermind-eth/under-the-hood-of-cairo-1-0-exploring-sierra-7f32808421f5).

<div class="quiz-placeholder" data-quiz-name="&quot;ch02-05-control-flow&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;The condition to an if-expression must be a boolean. Cairo does not have a concept of \&quot;truthy\&quot; or \&quot;falsy\&quot; values.\n&quot;,&quot;id&quot;:&quot;17a48401-18af-42d3-bc5a-c9fe9d87815e&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false,&quot;lineNumber&quot;:3},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n  let x = 1;\n  let y = if x { 0 } else { 1 }; \n  println!(\&quot;{y}\&quot;);\n}\n&quot;}},{&quot;context&quot;:&quot;When an if condition in Cairo evaluates to true, the program executes the block of code associated with that if condition.\n&quot;,&quot;id&quot;:&quot;2b4f0ad1-ccb2-4854-a8de-9b5067b8a3f1&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;2&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;1&quot;,&quot;3&quot;,&quot;1 and 3&quot;],&quot;prompt&quot;:&quot;What happens in Cairo if an if condition evaluates to true?\n\n1. The program skips the if block and executes the next block of code.\n2. The program executes the block of code associated with the if condition.\n3. The program terminates immediately.\n&quot;}},{&quot;id&quot;:&quot;1abbb637-f4cc-42d2-8a02-c85c1002096a&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;The program skips the if block and moves on to the next bit of code.&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;The program panics.&quot;,&quot;The program executes an implicit else block.&quot;,&quot;The program stops execution.&quot;],&quot;prompt&quot;:&quot;What is the result of running a Cairo program with an if statement where the condition evaluates to false and no else block is provided?\n&quot;}},{&quot;context&quot;:&quot;Cairo supports `loop` and `while` loops that continue execution indefinitely until a break condition is explicitly met or the program runs out of gas.\nThe safety and conciseness of `for` loops make them the most commonly used loop construct in Cairo.\n&quot;,&quot;id&quot;:&quot;5b0baa2b-f5b3-4718-a4d7-9f28c0540e79&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;`loop`, `while` or `for` with a break condition.&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;Automated mechanisms that handle execution retries for you.&quot;,&quot;`while`, `for` or `repeat` until a certain number of iterations is reached.&quot;,&quot;An `if` statement that checks for a condition and repeats execution until the condition is met.&quot;],&quot;prompt&quot;:&quot;What feature does Cairo provide for repeating code execution until a specified condition is met or gas runs out?\n&quot;}},{&quot;context&quot;:&quot;The 'continue' keyword in Cairo skips the remaining code in the current iteration of the loop. In this case, it skips the sum += 10 when 'i = 2'.\n&quot;,&quot;id&quot;:&quot;d2bcb7e6-f234-47b8-9498-4c2332acbd0e&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;40&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n    let mut sum: usize = 0;\n\n    for i in 0..5_usize {\n        if i == 2 {\n            continue;\n        }\n        sum += 10;\n    };\n\n    println!(\&quot;{}\&quot;, sum);\n}\n&quot;}},{&quot;context&quot;:&quot;Can only break with a value inside a `loop`\n&quot;,&quot;id&quot;:&quot;5e2ff5a8-ad4a-47bd-805b-ca58f7821122&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n    let mut i = 0;\n\n     let result = while(i &lt; 10) {\n        if i == 5 {\n            break i * 2;\n        }\n        i += 1;\n    };\n    \n    println!(\&quot;The result is {}\&quot;, result);\n}\n&quot;}}]}"></div>

## Summary

You made it! This was a sizable chapter: you learned about variables, data types, functions, comments,
`if` expressions and loops! To practice with the concepts discussed in this chapter,
try building programs to do the following:

- Generate the _n_-th Fibonacci number.
- Compute the factorial of a number _n_.

Now, we’ll review the common collection types in Cairo in the next chapter.


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Common Collections

Cairo provides a set of common collection types that can be used to store and manipulate data. These collections are designed to be efficient, flexible, and easy to use. This section introduces the primary collection types available in Cairo: Arrays and Dictionaries.
# Arrays

An array is a collection of elements of the same type. You can create and use array methods by using the `ArrayTrait` trait from the core library.

An important thing to note is that arrays have limited modification options. Arrays are, in fact, queues whose values can't be modified.
This has to do with the fact that once a memory slot is written to, it cannot be overwritten, but only read from it. You can only append items to the end of an array and remove items from the front.

## Creating an Array

Creating an array is done with the `ArrayTrait::new()` call. Here's an example of creating an array and appending 3 elements to it:

```cairo
fn main() {
    let mut a = ArrayTrait::new();
    a.append(0);
    a.append(1);
    a.append(2);
}
```

When required, you can pass the expected type of items inside the array when instantiating the array like this, or explicitly define the type of the variable.

```cairo, noplayground
let mut arr = ArrayTrait::<u128>::new();
```

```cairo, noplayground
let mut arr:Array<u128> = ArrayTrait::new();
```

## Updating an Array

### Adding Elements

To add an element to the end of an array, you can use the `append()` method:

```cairo
# fn main() {
#     let mut a = ArrayTrait::new();
#     a.append(0);
#     a.append(1);
    a.append(2);
# }
```

### Removing Elements

You can only remove elements from the front of an array by using the `pop_front()` method.
This method returns an `Option` that can be unwrapped, containing the removed element, or `None` if the array is empty.

```cairo
fn main() {
    let mut a = ArrayTrait::new();
    a.append(10);
    a.append(1);
    a.append(2);

    let first_value = a.pop_front().unwrap();
    println!("The first value is {}", first_value);
}
```

The above code will print `The first value is 10` as we remove the first element that was added.

In Cairo, memory is immutable, which means that it is not possible to modify the elements of an array once they've been added. You can only add elements to the end of an array and remove elements from the front of an array. These operations do not require memory mutation, as they involve updating pointers rather than directly modifying the memory cells.

## Reading Elements from an Array

To access array elements, you can use `get()` or `at()` array methods that return different types. Using `arr.at(index)` is equivalent to using the subscripting operator `arr[index]`.

### `get()` Method

The `get` function returns an `Option<Box<@T>>`, which means it returns an option to a Box type (Cairo's smart-pointer type) containing a snapshot to the element at the specified index if that element exists in the array. If the element doesn't exist, `get` returns `None`. This method is useful when you expect to access indices that may not be within the array's bounds and want to handle such cases gracefully without panics. Snapshots will be explained in more detail in the ["References and Snapshots"][snapshots] chapter.

Here is an example with the `get()` method:

```cairo
fn main() -> u128 {
    let mut arr = ArrayTrait::<u128>::new();
    arr.append(100);
    let index_to_access =
        1; // Change this value to see different results, what would happen if the index doesn't exist?
    match arr.get(index_to_access) {
        Some(x) => {
            *x
                .unbox() // Don't worry about * for now, if you are curious see Chapter 4.2 #desnap operator
            // It basically means "transform what get(idx) returned into a real value"
        },
        None => { panic!("out of bounds") },
    }
}
```

[snapshots]: ./ch04-02-references-and-snapshots.md#snapshots

### `at()` Method

The `at` function, and its equivalent the subscripting operator, on the other hand, directly return a snapshot to the element at the specified index using the `unbox()` operator to extract the value stored in a box. If the index is out of bounds, a panic error occurs. You should only use `at` when you want the program to panic if the provided index is out of the array's bounds, which can prevent unexpected behavior.

```cairo
fn main() {
    let mut a = ArrayTrait::new();
    a.append(0);
    a.append(1);

    // using the `at()` method
    let first = *a.at(0);
    assert!(first == 0);
    // using the subscripting operator
    let second = *a[1];
    assert!(second == 1);
}
```

In this example, the variable named `first` will get the value `0` because that
is the value at index `0` in the array. The variable named `second` will get
the value `1` from index `1` in the array.

In summary, use `at` when you want to panic on out-of-bounds access attempts, and use `get` when you prefer to handle such cases gracefully without panicking.

## Size-related Methods

To determine the number of elements in an array, use the `len()` method. The return value is of type `usize`.

If you want to check if an array is empty or not, you can use the `is_empty()` method, which returns `true` if the array is empty and `false` otherwise.

## `array!` Macro

Sometimes, we need to create arrays with values that are already known at compile time. The basic way of doing that is redundant. You would first declare the array and then append each value one by one. `array!` is a simpler way of doing this task by combining the two steps.
At compile-time, the compiler will expand the macro to generate the code that appends the items sequentially.

Without `array!`:

```cairo
    let mut arr = ArrayTrait::new();
    arr.append(1);
    arr.append(2);
    arr.append(3);
    arr.append(4);
    arr.append(5);
```

With `array!`:

```cairo
    let arr = array![1, 2, 3, 4, 5];
```

## Storing Multiple Types with Enums

If you want to store elements of different types in an array, you can use an `Enum` to define a custom data type that can hold multiple types. Enums will be explained in more detail in the ["Enums and Pattern Matching"][enums] chapter.

```cairo
#[derive(Copy, Drop)]
enum Data {
    Integer: u128,
    Felt: felt252,
    Tuple: (u32, u32),
}

fn main() {
    let mut messages: Array<Data> = array![];
    messages.append(Data::Integer(100));
    messages.append(Data::Felt('hello world'));
    messages.append(Data::Tuple((10, 30)));
}
```

[enums]: ./ch06-00-enums-and-pattern-matching.md

## Span

`Span` is a struct that represents a snapshot of an `Array`. It is designed to provide safe and controlled access to the elements of an array without modifying the original array. Span is particularly useful for ensuring data integrity and avoiding borrowing issues when passing arrays between functions or when performing read-only operations, as introduced in ["References and Snapshots"][references].

All methods provided by `Array` can also be used with `Span`, except for the `append()` method.

[references]: ./ch04-02-references-and-snapshots.md

### Turning an Array into Span

To create a `Span` of an `Array`, call the `span()` method:

```cairo
# fn main() {
#     let mut array: Array<u8> = ArrayTrait::new();
    array.span();
# }
```

<div class="quiz-placeholder" data-quiz-name="&quot;ch03-01-arrays&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;If `til = 4`, then for an array of length 3, the loop will attempt to index the array with `i = 3`,\nwhich is out of bounds.  This function does not panic if `n = 1` because it returns before reaching\nthe out-of-bounds index.\n&quot;,&quot;id&quot;:&quot;dd16401e-9f74-4c86-a6ec-da2937cb26e5&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;`find_until(array![1, 2, 3].span(), 4, 4);`&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;`find_until(array![1, 2, 3].span(), 0, 0);`&quot;,&quot;`find_until(array![1, 2, 3].span(), 3, 3);`&quot;,&quot;`find_until(array![1, 2, 3].span(), 1, 4);`&quot;],&quot;prompt&quot;:&quot;Which call to this `find_until` function will cause a runtime panic?\n\n```\nfn find_until(mut v: Span&lt;u64&gt;, n: u64, til: usize) -&gt; Option&lt;usize&gt; {\n    let mut i = 0;\n    loop {\n        if i == til {\n            break None;\n        }\n        if *v[i] == n {\n            break Some(i);\n        }\n        i += 1;\n    }\n}\n```\n&quot;}},{&quot;context&quot;:&quot;As Cairo's memory layout is immutable, types cannot be moved out of an array by indexing. The only\npossibility is to copy the value to a new variable using the `*` (desnap) operator.  Therefore, as\nByteArray is not copyable, the line `let mut s = *v[0];` does not compile.\n&quot;,&quot;id&quot;:&quot;2e6570eb-8bf4-48b7-9032-5815475bc412&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false,&quot;lineNumber&quot;:3},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n    let mut v: Array&lt;ByteArray&gt; = array![\&quot;Hello \&quot;];\n    let mut s = *v[0];\n    s.append(@\&quot;world\&quot;);\n    println!(\&quot;{s}\&quot;);\n}\n&quot;}},{&quot;context&quot;:&quot;`*v[0]` copies the value of the first element of the array to `i`. Therefore, `i` is a copy of the\nvalue of `v[0]`, and incrementing `i` does not affect `v[0]`.\n&quot;,&quot;id&quot;:&quot;95d528ee-ae78-4892-a438-a5d97f07f52a&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;2, 1&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n    let mut v: Array&lt;usize&gt; = array![1, 2, 3];\n    let mut i = *v[0];\n    i += 1;\n    println!(\&quot;{}, {}\&quot;, i, v[0]);\n}\n&quot;}}]}"></div>


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Dictionaries

Cairo provides in its core library a dictionary-like type. The `Felt252Dict<T>` data type represents a collection of key-value pairs where each key is unique and associated with a corresponding value. This type of data structure is known differently across different programming languages such as maps, hash tables, associative arrays and many others.

The `Felt252Dict<T>` type is useful when you want to organize your data in a certain way for which using an `Array<T>` and indexing doesn't suffice. Cairo dictionaries also allow the programmer to easily simulate the existence of mutable memory when there is none.

## Basic Use of Dictionaries

It is normal in other languages when creating a new dictionary to define the data types of both key and value. In Cairo, the key type is restricted to `felt252`, leaving only the possibility to specify the value data type, represented by `T` in `Felt252Dict<T>`.

The core functionality of a `Felt252Dict<T>` is implemented in the trait `Felt252DictTrait` which includes all basic operations. Among them we can find:

1. `insert(felt252, T) -> ()` to write values to a dictionary instance and
2. `get(felt252) -> T` to read values from it.

These functions allow us to manipulate dictionaries like in any other language. In the following example, we create a dictionary to represent a mapping between individuals and their balance:

```cairo
use core::dict::Felt252Dict;

fn main() {
    let mut balances: Felt252Dict<u64> = Default::default();

    balances.insert('Alex', 100);
    balances.insert('Maria', 200);

    let alex_balance = balances.get('Alex');
    assert!(alex_balance == 100, "Balance is not 100");

    let maria_balance = balances.get('Maria');
    assert!(maria_balance == 200, "Balance is not 200");
}
```

We can create a new instance of `Felt252Dict<u64>` by using the `default` method of the `Default` trait and add two individuals, each one with their own balance, using the `insert` method. Finally, we check the balance of our users with the `get` method. These methods are defined in the `Felt252DictTrait` trait in the core library.

Throughout the book we have talked about how Cairo's memory is immutable, meaning you can only write to a memory cell once but the `Felt252Dict<T>` type represents a way to overcome this obstacle. We will explain how this is implemented later on in ["Dictionaries Underneath"][dict underneath].

Building upon our previous example, let us show a code example where the balance of the same user changes:

```cairo
use core::dict::Felt252Dict;

fn main() {
    let mut balances: Felt252Dict<u64> = Default::default();

    // Insert Alex with 100 balance
    balances.insert('Alex', 100);
    // Check that Alex has indeed 100 associated with him
    let alex_balance = balances.get('Alex');
    assert!(alex_balance == 100, "Alex balance is not 100");

    // Insert Alex again, this time with 200 balance
    balances.insert('Alex', 200);
    // Check the new balance is correct
    let alex_balance_2 = balances.get('Alex');
    assert!(alex_balance_2 == 200, "Alex balance is not 200");
}
```

Notice how in this example we added the 'Alex' individual twice, each time using a different balance and each time that we checked for its balance it had the last value inserted! `Felt252Dict<T>` effectively allows us to "rewrite" the stored value for any given key.

Before heading on and explaining how dictionaries are implemented it is worth mentioning that once you instantiate a `Felt252Dict<T>`, behind the scenes all keys have their associated values initialized as zero. This means that if for example, you tried to get the balance of an inexistent user you will get 0 instead of an error or an undefined value. This also means there is no way to delete data from a dictionary. Something to take into account when incorporating this structure into your code.

Until this point, we have seen all the basic features of `Felt252Dict<T>` and how it mimics the same behavior as the corresponding data structures in any other language, that is, externally of course. Cairo is at its core a non-deterministic Turing-complete programming language, very different from any other popular language in existence, which as a consequence means that dictionaries are implemented very differently as well!

In the following sections, we are going to give some insights about `Felt252Dict<T>` inner mechanisms and the compromises that were taken to make them work. After that, we are going to take a look at how to use dictionaries with other data structures as well as use the `entry` method as another way to interact with them.

[dict underneath]: ./ch03-02-dictionaries.md#dictionaries-underneath

## Dictionaries Underneath

One of the constraints of Cairo's non-deterministic design is that its memory system is immutable, so in order to simulate mutability, the language implements `Felt252Dict<T>` as a list of entries. Each of the entries represents a time when a dictionary was accessed for reading/updating/writing purposes. An entry has three fields:

1. A `key` field that identifies the key for this key-value pair of the dictionary.
2. A `previous_value` field that indicates which previous value was held at `key`.
3. A `new_value` field that indicates the new value that is held at `key`.

If we try implementing `Felt252Dict<T>` using high-level structures we would internally define it as `Array<Entry<T>>` where each `Entry<T>` has information about what key-value pair it represents and the previous and new values it holds. The definition of `Entry<T>` would be:

```cairo,noplayground
struct Entry<T> {
    key: felt252,
    previous_value: T,
    new_value: T,
}
```

For each time we interact with a `Felt252Dict<T>`, a new `Entry<T>` will be registered:

- A `get` would register an entry where there is no change in state, and previous and new values are stored with the same value.
- An `insert` would register a new `Entry<T>` where the `new_value` would be the element being inserted, and the `previous_value` the last element inserted before this. In case it is the first entry for a certain key, then the previous value will be zero.

The use of this entry list shows how there isn't any rewriting, just the creation of new memory cells per `Felt252Dict<T>` interaction. Let's show an example of this using the `balances` dictionary from the previous section and inserting the users 'Alex' and 'Maria':

```cairo
# use core::dict::Felt252Dict;
#
# struct Entry<T> {
#     key: felt252,
#     previous_value: T,
#     new_value: T,
# }
#
# fn main() {
#     let mut balances: Felt252Dict<u64> = Default::default();
    balances.insert('Alex', 100_u64);
    balances.insert('Maria', 50_u64);
    balances.insert('Alex', 200_u64);
    balances.get('Maria');
# }
```

These instructions would then produce the following list of entries:

|  key  | previous | new |
| :---: | -------- | --- |
| Alex  | 0        | 100 |
| Maria | 0        | 50  |
| Alex  | 100      | 200 |
| Maria | 50       | 50  |

Notice that since 'Alex' was inserted twice, it appears twice and the `previous` and `current` values are set properly. Also reading from 'Maria' registered an entry with no change from previous to current values.

This approach to implementing `Felt252Dict<T>` means that for each read/write operation, there is a scan for the whole entry list in search of the last entry with the same `key`. Once the entry has been found, its `new_value` is extracted and used on the new entry to be added as the `previous_value`. This means that interacting with `Felt252Dict<T>` has a worst-case time complexity of `O(n)` where `n` is the number of entries in the list.

If you pour some thought into alternate ways of implementing `Felt252Dict<T>` you'd surely find them, probably even ditching completely the need for a `previous_value` field, nonetheless, since Cairo is not your normal language this won't work.
One of the purposes of Cairo is, with the STARK proof system, to generate proofs of computational integrity. This means that you need to verify that program execution is correct and inside the boundaries of Cairo restrictions. One of those boundary checks consists of "dictionary squashing" and that requires information on both previous and new values for every entry.

## Squashing Dictionaries

To verify that the proof generated by a Cairo program execution that used a `Felt252Dict<T>` is correct, we need to check that there wasn't any illegal tampering with the dictionary. This is done through a method called `squash_dict` that reviews each entry of the entry list and checks that access to the dictionary remains coherent throughout the execution.

The process of squashing is as follows: given all entries with certain key `k`, taken in the same order as they were inserted, verify that the ith entry `new_value` is equal to the ith + 1 entry `previous_value`.

For example, given the following entry list:

|   key   | previous | new |
| :-----: | -------- | --- |
|  Alex   | 0        | 150 |
|  Maria  | 0        | 100 |
| Charles | 0        | 70  |
|  Maria  | 100      | 250 |
|  Alex   | 150      | 40  |
|  Alex   | 40       | 300 |
|  Maria  | 250      | 190 |
|  Alex   | 300      | 90  |

After squashing, the entry list would be reduced to:

|   key   | previous | new |
| :-----: | -------- | --- |
|  Alex   | 0        | 90  |
|  Maria  | 0        | 190 |
| Charles | 0        | 70  |

In case of a change on any of the values of the first table, squashing would have failed during runtime.

## Dictionary Destruction

If you run the examples from ["Basic Use of Dictionaries"][basic dictionaries] section, you'd notice that there was never a call to squash dictionary, but the program compiled successfully nonetheless. What happened behind the scene was that squash was called automatically via the `Felt252Dict<T>` implementation of the `Destruct<T>` trait. This call occurred just before the `balance` dictionary went out of scope.

The `Destruct<T>` trait represents another way of removing instances out of scope apart from `Drop<T>`. The main difference between these two is that `Drop<T>` is treated as a no-op operation, meaning it does not generate new CASM while `Destruct<T>` does not have this restriction. The only type which actively uses the `Destruct<T>` trait is `Felt252Dict<T>`, for every other type `Destruct<T>` and `Drop<T>` are synonyms. You can read more about these traits in [Drop and Destruct][drop destruct] section of Appendix C.

Later in ["Dictionaries as Struct Members"][dictionaries in structs] section, we will have a hands-on example where we implement the `Destruct<T>` trait for a custom type.

[basic dictionaries]: ./ch03-02-dictionaries.md#basic-use-of-dictionaries
[drop destruct]: ./appendix-03-derivable-traits.md#drop-and-destruct
[dictionaries in structs]: ./ch12-01-custom-data-structures.md#dictionaries-as-struct-members

## More Dictionaries

Up to this point, we have given a comprehensive overview of the functionality of `Felt252Dict<T>` as well as how and why it is implemented in a certain way. If you haven't understood all of it, don't worry because in this section we will have some more examples using dictionaries.

We will start by explaining the `entry` method which is part of a dictionary basic functionality included in `Felt252DictTrait<T>` which we didn't mention at the beginning. Soon after, we will see examples of how to use `Felt252Dict<T>` with other [complex types][nullable dictionaries values] such as `Array<T>`.

[nullable dictionaries values]: ./ch03-02-dictionaries.md#dictionaries-of-types-not-supported-natively

## Entry and Finalize

In the ["Dictionaries Underneath"][dict underneath] section, we explained how `Felt252Dict<T>` internally worked. It was a list of entries for each time the dictionary was accessed in any manner. It would first find the last entry given a certain `key` and then update it accordingly to whatever operation it was executing. The Cairo language gives us the tools to replicate this ourselves through the `entry` and `finalize` methods.

The `entry` method comes as part of `Felt252DictTrait<T>` with the purpose of creating a new entry given a certain key. Once called, this method takes ownership of the dictionary and returns the entry to update. The method signature is as follows:

```cairo,noplayground
fn entry(self: Felt252Dict<T>, key: felt252) -> (Felt252DictEntry<T>, T) nopanic
```

The first input parameter takes ownership of the dictionary while the second one is used to create the appropriate entry. It returns a tuple containing a `Felt252DictEntry<T>`, which is the type used by Cairo to represent dictionary entries, and a `T` representing the value held previously.
The `nopanic` notation simply indicates that the function is guaranteed to never panic.

The next thing to do is to update the entry with the new value. For this, we use the `finalize` method which inserts the entry and returns ownership of the dictionary:

```cairo,noplayground
fn finalize(self: Felt252DictEntry<T>, new_value: T) -> Felt252Dict<T>
```

This method receives the entry and the new value as parameters, and returns the updated dictionary.

Let us see an example using `entry` and `finalize`. Imagine we would like to implement our own version of the `get` method from a dictionary. We should then do the following:

1. Create the new entry to add using the `entry` method.
2. Insert back the entry where the `new_value` equals the `previous_value`.
3. Return the value.

Implementing our custom get would look like this:

```cairo,noplayground
use core::dict::{Felt252Dict, Felt252DictEntryTrait};

fn custom_get<T, +Felt252DictValue<T>, +Drop<T>, +Copy<T>>(
    ref dict: Felt252Dict<T>, key: felt252,
) -> T {
    // Get the new entry and the previous value held at `key`
    let (entry, prev_value) = dict.entry(key);

    // Store the value to return
    let return_value = prev_value;

    // Update the entry with `prev_value` and get back ownership of the dictionary
    dict = entry.finalize(prev_value);

    // Return the read value
    return_value
}
```

The `ref` keyword means that the ownership of the variable will be given back at the end of
the function. This concept will be explained in more detail in the ["References and Snapshots"][references] section.

Implementing the `insert` method would follow a similar workflow, except for inserting a new value when finalizing. If we were to implement it, it would look like the following:

```cairo,noplayground
use core::dict::{Felt252Dict, Felt252DictEntryTrait};

fn custom_insert<T, +Felt252DictValue<T>, +Destruct<T>, +Drop<T>>(
    ref dict: Felt252Dict<T>, key: felt252, value: T,
) {
    // Get the last entry associated with `key`
    // Notice that if `key` does not exist, `_prev_value` will
    // be the default value of T.
    let (entry, _prev_value) = dict.entry(key);

    // Insert `entry` back in the dictionary with the updated value,
    // and receive ownership of the dictionary
    dict = entry.finalize(value);
}
```

As a finalizing note, these two methods are implemented in a similar way to how `insert` and `get` are implemented for `Felt252Dict<T>`. This code shows some example usage:

```cairo
# use core::dict::{Felt252Dict, Felt252DictEntryTrait};
#
# fn custom_get<T, +Felt252DictValue<T>, +Drop<T>, +Copy<T>>(
#     ref dict: Felt252Dict<T>, key: felt252,
# ) -> T {
#     // Get the new entry and the previous value held at `key`
#     let (entry, prev_value) = dict.entry(key);
#
#     // Store the value to return
#     let return_value = prev_value;
#
#     // Update the entry with `prev_value` and get back ownership of the dictionary
#     dict = entry.finalize(prev_value);
#
#     // Return the read value
#     return_value
# }
#
# fn custom_insert<T, +Felt252DictValue<T>, +Destruct<T>, +Drop<T>>(
#     ref dict: Felt252Dict<T>, key: felt252, value: T,
# ) {
#     // Get the last entry associated with `key`
#     // Notice that if `key` does not exist, `_prev_value` will
#     // be the default value of T.
#     let (entry, _prev_value) = dict.entry(key);
#
#     // Insert `entry` back in the dictionary with the updated value,
#     // and receive ownership of the dictionary
#     dict = entry.finalize(value);
# }
#
fn main() {
    let mut dict: Felt252Dict<u64> = Default::default();

    custom_insert(ref dict, '0', 100);

    let val = custom_get(ref dict, '0');

    assert!(val == 100, "Expecting 100");
}
#
#
```

[dict underneath]: ./ch03-02-dictionaries.md#dictionaries-underneath
[references]: ./ch04-02-references-and-snapshots.md

## Dictionaries of Types not Supported Natively

One restriction of `Felt252Dict<T>` that we haven't talked about is the trait `Felt252DictValue<T>`.
This trait defines the `zero_default` method which is the one that gets called when a value does not exist in the dictionary.
This is implemented by some common data types, such as most unsigned integers, `bool` and `felt252` - but it is not implemented for more complex types such as arrays, structs (including `u256`), and other types from the core library.
This means that making a dictionary of types not natively supported is not a straightforward task, because you would need to write a couple of trait implementations in order to make the data type a valid dictionary value type.
To compensate this, you can wrap your type inside a `Nullable<T>`.

`Nullable<T>` is a smart pointer type that can either point to a value or be `null` in the absence of value. It is usually used in Object Oriented Programming Languages when a reference doesn't point anywhere. The difference with `Option` is that the wrapped value is stored inside a `Box<T>` data type. The `Box<T>` type is a smart pointer that allows us to use a dedicated `boxed_segment` memory segment for our data, and access this segment using a pointer that can only be manipulated in one place at a time. See [Smart Pointers Chapter](./ch12-02-smart-pointers.md) for more information.

Let's show using an example. We will try to store a `Span<felt252>` inside a dictionary. For that, we will use `Nullable<T>` and `Box<T>`. Also, we are storing a `Span<T>` and not an `Array<T>` because the latter does not implement the `Copy<T>` trait which is required for reading from a dictionary.

```cairo,noplayground
use core::dict::Felt252Dict;
use core::nullable::{NullableTrait, match_nullable, FromNullableResult};

fn main() {
    // Create the dictionary
    let mut d: Felt252Dict<Nullable<Span<felt252>>> = Default::default();

    // Create the array to insert
    let a = array![8, 9, 10];

    // Insert it as a `Span`
    d.insert(0, NullableTrait::new(a.span()));

//...
```

In this code snippet, the first thing we did was to create a new dictionary `d`. We want it to hold a `Nullable<Span>`. After that, we created an array and filled it with values.

The last step is inserting the array as a span inside the dictionary. Notice that we do this using the `new` function of the `NullableTrait`.

Once the element is inside the dictionary, and we want to get it, we follow the same steps but in reverse order. The following code shows how to achieve that:

```cairo,noplayground
//...

    // Get value back
    let val = d.get(0);

    // Search the value and assert it is not null
    let span = match match_nullable(val) {
        FromNullableResult::Null => panic!("No value found"),
        FromNullableResult::NotNull(val) => val.unbox(),
    };

    // Verify we are having the right values
    assert!(*span.at(0) == 8, "Expecting 8");
    assert!(*span.at(1) == 9, "Expecting 9");
    assert!(*span.at(2) == 10, "Expecting 10");
}
```

Here we:

1. Read the value using `get`.
2. Verified it is non-null using the `match_nullable` function.
3. Unwrapped the value inside the box and asserted it was correct.

The complete script would look like this:

```cairo
use core::dict::Felt252Dict;
use core::nullable::{NullableTrait, match_nullable, FromNullableResult};

fn main() {
    // Create the dictionary
    let mut d: Felt252Dict<Nullable<Span<felt252>>> = Default::default();

    // Create the array to insert
    let a = array![8, 9, 10];

    // Insert it as a `Span`
    d.insert(0, NullableTrait::new(a.span()));

    // Get value back
    let val = d.get(0);

    // Search the value and assert it is not null
    let span = match match_nullable(val) {
        FromNullableResult::Null => panic!("No value found"),
        FromNullableResult::NotNull(val) => val.unbox(),
    };

    // Verify we are having the right values
    assert!(*span.at(0) == 8, "Expecting 8");
    assert!(*span.at(1) == 9, "Expecting 9");
    assert!(*span.at(2) == 10, "Expecting 10");
}

```

## Using Arrays inside Dictionaries

In the previous section, we explored how to store and retrieve complex types inside a dictionary using `Nullable<T>` and `Box<T>`. Now, let's take a look at how to store an array inside a dictionary and dynamically modify its contents.

Storing arrays in dictionaries in Cairo is slightly different from storing other types. This is because arrays are more complex data structures that require special handling to avoid issues with memory copying and references.

First, let's look at how to create a dictionary and insert an array into it. This process is pretty straightforward and follows a similar pattern to inserting other types of data:

```cairo
use core::dict::Felt252Dict;

fn main() {
    let arr = array![20, 19, 26];
    let mut dict: Felt252Dict<Nullable<Array<u8>>> = Default::default();
    dict.insert(0, NullableTrait::new(arr));
    println!("Array inserted successfully.");
}
```

However, attempting to read an array from the dictionary using the `get` method will result in a compiler error. This is because `get` tries to copy the array in memory, which is not possible for arrays (as we've already mentioned in the [previous section][nullable dictionaries values], `Array<T>` does not implement the `Copy<T>` trait):

```cairo
use core::nullable::{match_nullable, FromNullableResult};
use core::dict::Felt252Dict;

fn main() {
    let arr = array![20, 19, 26];
    let mut dict: Felt252Dict<Nullable<Array<u8>>> = Default::default();
    dict.insert(0, NullableTrait::new(arr));
    println!("Array: {:?}", get_array_entry(ref dict, 0));
}

fn get_array_entry(ref dict: Felt252Dict<Nullable<Array<u8>>>, index: felt252) -> Span<u8> {
    let val = dict.get(0); // This will cause a compiler error
    let arr = match match_nullable(val) {
        FromNullableResult::Null => panic!("No value!"),
        FromNullableResult::NotNull(val) => val.unbox(),
    };
    arr.span()
}
```

```shell
$ scarb execute
   Compiling no_listing_15_dict_of_array_attempt_get v0.1.0 (listings/ch03-common-collections/no_listing_15_dict_of_array_attempt_get/Scarb.toml)
error: Trait has no implementation in context: core::traits::Copy::<core::nullable::Nullable::<core::array::Array::<core::integer::u8>>>.
 --> listings/ch03-common-collections/no_listing_15_dict_of_array_attempt_get/src/lib.cairo:13:20
    let val = dict.get(0); // This will cause a compiler error
                   ^*^

error: could not compile `no_listing_15_dict_of_array_attempt_get` due to previous error
error: `scarb metadata` exited with error

```

To correctly read an array from the dictionary, we need to use dictionary entries. This allows us to get a reference to the array value without copying it:

```cairo,noplayground
fn get_array_entry(ref dict: Felt252Dict<Nullable<Array<u8>>>, index: felt252) -> Span<u8> {
    let (entry, _arr) = dict.entry(index);
    let mut arr = _arr.deref_or(array![]);
    let span = arr.span();
    dict = entry.finalize(NullableTrait::new(arr));
    span
}
```

> Note: We must convert the array to a `Span` before finalizing the entry, because calling `NullableTrait::new(arr)` moves the array, thus making it impossible to return it from the function.

To modify the stored array, such as appending a new value, we can use a similar approach. The following `append_value` function demonstrates this:

```cairo,noplayground
fn append_value(ref dict: Felt252Dict<Nullable<Array<u8>>>, index: felt252, value: u8) {
    let (entry, arr) = dict.entry(index);
    let mut unboxed_val = arr.deref_or(array![]);
    unboxed_val.append(value);
    dict = entry.finalize(NullableTrait::new(unboxed_val));
}
```

In the `append_value` function, we access the dictionary entry, dereference the array, append the new value, and finalize the entry with the updated array.

> Note: Removing an item from a stored array can be implemented in a similar manner.

Below is the complete example demonstrating the creation, insertion, reading, and modification of an array in a dictionary:

```cairo
use core::nullable::NullableTrait;
use core::dict::{Felt252Dict, Felt252DictEntryTrait};

fn append_value(ref dict: Felt252Dict<Nullable<Array<u8>>>, index: felt252, value: u8) {
    let (entry, arr) = dict.entry(index);
    let mut unboxed_val = arr.deref_or(array![]);
    unboxed_val.append(value);
    dict = entry.finalize(NullableTrait::new(unboxed_val));
}

fn get_array_entry(ref dict: Felt252Dict<Nullable<Array<u8>>>, index: felt252) -> Span<u8> {
    let (entry, _arr) = dict.entry(index);
    let mut arr = _arr.deref_or(array![]);
    let span = arr.span();
    dict = entry.finalize(NullableTrait::new(arr));
    span
}

fn main() {
    let arr = array![20, 19, 26];
    let mut dict: Felt252Dict<Nullable<Array<u8>>> = Default::default();
    dict.insert(0, NullableTrait::new(arr));
    println!("Before insertion: {:?}", get_array_entry(ref dict, 0));

    append_value(ref dict, 0, 30);

    println!("After insertion: {:?}", get_array_entry(ref dict, 0));
}
```

<div class="quiz-placeholder" data-quiz-name="&quot;ch03-02-dictionaries&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;The code compiles and runs without panicking because `get` returns the default value for `u64` when the key is not found.\nThe value of `john_balance` is `0 + 100 = 100`.\n&quot;,&quot;id&quot;:&quot;8b538a1f-0cf9-4c57-8304-c4b07e0134dd&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;100&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;use core::dict::Felt252Dict;\n\nfn main() {\n    let mut balances: Felt252Dict&lt;u64&gt; = Default::default();\n    balances.insert('Alex', 100);\n    balances.insert('Maria', 200);\n    let john_balance = balances.get('John') + 100;\n    println!(\&quot;{}\&quot;, john_balance);\n}\n&quot;}},{&quot;context&quot;:&quot;We could store a Span&lt;T&gt; in the dictionary because it implements the Copy&lt;T&gt; trait.\nHowever, the `zero_default` method is not implemented for Span&lt;T&gt; which thus must be wrapped inside a Nullable&lt;T&gt; type.\nFor this reason the code will not compile.\n&quot;,&quot;id&quot;:&quot;af5bc548-fb84-487f-958e-0622d242dc6f&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;use core::dict::Felt252Dict;\n\nfn main() {\n    let mut dict: Felt252Dict&lt;Span&lt;felt252&gt;&gt; = Default::default();\n    let a = array![8, 9, 10];\n    dict.insert('my_span', a.span());\n    let my_span = d.get('my_span');\n    println!(\&quot;{:?}\&quot;, *my_span.at(0));\n}\n&quot;}},{&quot;context&quot;:&quot;The value type of this dictionary is `u64`, which is an unsigned integer. So the variable `alex_balance` is an unsigned integer that can't be negative.\nThe subtraction operation will cause a runtime panic.\n&quot;,&quot;id&quot;:&quot;8fe876cf-4373-42ca-ae2c-4d13ae23dbed&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;There will be a runtime panic.&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;Alex : -50&quot;,&quot;Alex : 0&quot;,&quot;Alex : 100&quot;],&quot;prompt&quot;:&quot;What will be the output of this code snippet?\n```\nuse core::dict::Felt252Dict;\n\nfn main() {\n    let mut balances: Felt252Dict&lt;u64&gt; = Default::default();\n    balances.insert('Alex', 200);\n    balances.insert('Maria', 200);\n    balances.insert('Alex', 100);\n    let alex_balance = balances.get('Alex') - 150;\n    balances.insert('Alex', alex_balance);\n    println!(\&quot;Alex : {}\&quot;, alex_balance);\n}\n```\n&quot;}},{&quot;context&quot;:&quot;The `entry` method returns a tuple with the entry and the value.  We can mutate this value, and then\nfinalize the entry with this new value, which restores ownership of the dictionary in the calling\ncontext.\n&quot;,&quot;id&quot;:&quot;f78d9b38-1d3a-4b00-a014-9c618070738c&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;`let (entry, my_array) = dict.entry(key);`&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;`let my_array = dict.entry(key);`&quot;,&quot;`let mut my_array = dict.entry(key);`&quot;,&quot;None of these options are correct: Arrays can't be mutated inside Dicts.&quot;],&quot;prompt&quot;:&quot;We want to write a function to append a value to an array stored in a dictionary.\nChoose the right line of code to make the function below work as expected.\n\n```\nfn append_value(ref dict: Felt252Dict&lt;Nullable&lt;Array&lt;u8&gt;&gt;&gt;, key: felt252, value_to_append: u8) {\n    // insert the right line here\n    let mut my_array_unboxed = my_array.deref_or(array![]);\n    my_array_unboxed.append(value_to_append);\n    dict = entry.finalize(NullableTrait::new(my_array_unboxed));\n}\n```\n&quot;}},{&quot;context&quot;:&quot;Squashing only keeps the last entry for each key. In this case, the table will only contain the entries for 'John', 'Alex', 'Maria', and 'Alicia'.\n&quot;,&quot;id&quot;:&quot;d643e8df-2b76-4d2a-bb1f-1a00e53ec8df&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;4&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;6&quot;,&quot;3&quot;,&quot;0&quot;],&quot;prompt&quot;:&quot;Let's consider the following instructions and the associated entry table:\n```\nbalances.insert('Alex', 100);\nbalances.insert('Maria', 200);\nbalances.insert('John', 300);\nbalances.insert('Alex', 50);\nbalances.insert('Maria', 150);\nbalances.insert('Alicia', 250);\n```\nAfter squashing, how many entries will the table contain?\n&quot;}}]}"></div>


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Understanding Cairo's Ownership system

Cairo is a language built around a linear type system that allows us to
statically ensure that in every Cairo program, a value is used exactly once.
This linear type system helps prevent runtime errors by ensuring that operations that could cause such errors, such as writing twice to a memory cell, are detected at compile time.
This is achieved by implementing an ownership system
and forbidding copying and dropping values by default. In this chapter, we’ll
talk about Cairo's ownership system as well as references and snapshots.
# Ownership Using a Linear Type System

Cairo uses a linear type system. In such a type system, any value (a basic type, a struct, an enum) must be used and must only be used once. 'Used' here means that the value is either _destroyed_ or _moved_.

_Destruction_ can happen in several ways:

- a variable goes out of scope.
- a struct is destructured.
- explicit destruction using `destruct()`.

_Moving_ a value simply means passing that value to another function.

This results in somewhat similar constraints to the Rust ownership model, but there are some differences.
In particular, the Rust ownership model exists (in part) to avoid data races and concurrent mutable access to a memory value. This is obviously impossible in Cairo since the memory is immutable.
Instead, Cairo leverages its linear type system for two main purposes:

- Ensuring that all code is provable and thus verifiable.
- Abstracting away the immutable memory of the Cairo VM.

### Ownership

In Cairo, ownership applies to _variables_ and not to _values_. A value can safely be referred to by many different variables (even if they are mutable variables), as the value itself is always immutable.
Variables however can be mutable, so the compiler must ensure that constant variables aren't accidentally modified by the programmer.
This makes it possible to talk about ownership of a variable: the owner is the code that can read (and write if mutable) the variable.

This means that variables (not values) follow similar rules to Rust values:

- Each variable in Cairo has an owner.
- There can only be one owner at a time.
- When the owner goes out of scope, the variable is destroyed.

Now that we’re past basic Cairo syntax, we won’t include all the `fn main() {` code in examples, so if you’re following along, make sure to put the following examples inside a main function manually. As a result, our examples will be a bit more concise, letting us focus on the actual details rather than boilerplate code.

## Variable Scope

As a first example of the linear type system, we’ll look at the _scope_ of some variables. A
scope is the range within a program for which an item is valid. Take the
following variable:

```cairo,noplayground
let s = 'hello';
```

The variable `s` refers to a short string. The variable is valid from the point at
which it’s declared until the end of the current _scope_. Listing 4-1 shows a
program with comments annotating where the variable `s` would be valid.

```cairo
# //TAG: ignore_fmt
# fn main() {
    { // s is not valid here, it’s not yet declared
        let s = 'hello'; // s is valid from this point forward
        // do stuff with s
    } // this scope is now over, and s is no longer valid
# }
```

<span class="caption">Listing 4-1: A variable and the scope in which it is valid</span>

In other words, there are two important points in time here:

- When `s` comes _into_ scope, it is valid.
- It remains valid until it goes _out of_ scope.

At this point, the relationship between scopes and when variables are valid is similar to that in other programming languages. Now we’ll build on top of this understanding by using the `Array` type we introduced in the previous ["Arrays"][array] section.

[array]: ./ch03-01-arrays.md

### Moving values

As said earlier, _moving_ a value simply means passing that value to another function. When that happens, the variable referring to that value in the original scope is destroyed and can no longer be used, and a new variable is created to hold the same value.

Arrays are an example of a complex type that is moved when passing it to another function.
Here is a short reminder of what an array looks like:

```cairo
# fn main() {
    let mut arr: Array<u128> = array![];
    arr.append(1);
    arr.append(2);
# }
```

How does the type system ensure that the Cairo program never tries to write to the same memory cell twice?
Consider the following code, where we try to remove the front of the array twice:

```cairo,does_not_compile
fn foo(mut arr: Array<u128>) {
    arr.pop_front();
}

fn main() {
    let arr: Array<u128> = array![];
    foo(arr);
    foo(arr);
}
```

In this case, we try to pass the same value (the array in the `arr` variable) to both function calls. This means our code tries to remove the first element twice, which would try to write to the same memory cell twice - which is forbidden by the Cairo VM, leading to a runtime error.
Thankfully, this code does not actually compile. Once we have passed the array to the `foo` function, the variable `arr` is no longer usable. We get this compile-time error, telling us that we would need Array to implement the Copy Trait:

```shell
$ scarb execute
   Compiling no_listing_02_pass_array_by_value v0.1.0 (listings/ch04-understanding-ownership/no_listing_02_pass_array_by_value/Scarb.toml)
warn: Unhandled `#[must_use]` type `core::option::Option::<core::integer::u128>`
 --> listings/ch04-understanding-ownership/no_listing_02_pass_array_by_value/src/lib.cairo:3:5
    arr.pop_front();
    ^*************^

error: Variable was previously moved.
 --> listings/ch04-understanding-ownership/no_listing_02_pass_array_by_value/src/lib.cairo:9:9
    foo(arr);
        ^*^
note: variable was previously used here:
  --> listings/ch04-understanding-ownership/no_listing_02_pass_array_by_value/src/lib.cairo:8:9
    foo(arr);
        ^*^
note: Trait has no implementation in context: core::traits::Copy::<core::array::Array::<core::integer::u128>>.

error: could not compile `no_listing_02_pass_array_by_value` due to previous error
error: `scarb metadata` exited with error

```

## The `Copy` Trait

The `Copy` trait allows simple types to be duplicated by copying felts, without allocating new memory segments. This contrasts with Cairo's default "move" semantics, which transfer ownership of values to ensure memory safety and prevent issues like multiple writes to the same memory cell. `Copy` is implemented for types where duplication is safe and efficient, bypassing the need for move semantics. Types like `Array` and `Felt252Dict` cannot implement `Copy`, as manipulating them in different scopes is forbidden by the type system.

All basic types previously described in ["Data Types"][data types] implement by default the `Copy` trait.

While Arrays and Dictionaries can't be copied, custom types that don't contain either of them can be.
You can implement the `Copy` trait on your type by adding the `#[derive(Copy)]` annotation to your type definition. However, Cairo won't allow a type to be annotated with Copy if the type itself or any of its components doesn't implement the Copy trait.

```cairo,ignore_format
#[derive(Copy, Drop)]
struct Point {
    x: u128,
    y: u128,
}

fn main() {
    let p1 = Point { x: 5, y: 10 };
    foo(p1);
    foo(p1);
}

fn foo(p: Point) { // do something with p
}
```

In this example, we can pass `p1` twice to the foo function because the `Point` type implements the `Copy` trait. This means that when we pass `p1` to `foo`, we are actually passing a copy of `p1`, so `p1` remains valid. In ownership terms, this means that the ownership of `p1` remains with the `main` function.
If you remove the `Copy` trait derivation from the `Point` type, you will get a compile-time error when trying to compile the code.

_Don't worry about the `Struct` keyword. We will introduce this in [Chapter 5][structs]._

[data types]: ./ch02-02-data-types.md
[structs]: ./ch05-00-using-structs-to-structure-related-data.md

## Destroying Values - Example with FeltDict

The other way linear types can be _used_ is by being destroyed. Destruction must ensure that the 'resource' is now correctly released. In Rust, for example, this could be closing the access to a file, or locking a mutex.
In Cairo, one type that has such behaviour is `Felt252Dict`. For provability, dicts must be 'squashed' when they are destructed.
This would be very easy to forget, so it is enforced by the type system and the compiler.

### No-op Destruction: the `Drop` Trait

You may have noticed that the `Point` type in the previous example also implements the `Drop` trait.
For example, the following code will not compile, because the struct `A` is not moved or destroyed before it goes out of scope:

```cairo,does_not_compile
struct A {}

fn main() {
    A {}; // error: Variable not dropped.
}
```

However, types that implement the `Drop` trait are automatically destroyed when going out of scope. This destruction does nothing, it is a no-op - simply a hint to the compiler that this type can safely be destroyed once it's no longer useful. We call this "dropping" a value.

At the moment, the `Drop` implementation can be derived for all types, allowing them to be dropped when going out of scope, except for dictionaries (`Felt252Dict`) and types containing dictionaries.
For example, the following code compiles:

```cairo
#[derive(Drop)]
struct A {}

fn main() {
    A {}; // Now there is no error.
}
```

### Destruction with a Side-effect: the `Destruct` Trait

When a value is destroyed, the compiler first tries to call the `drop` method on that type. If it doesn't exist, then the compiler tries to call `destruct` instead. This method is provided by the `Destruct` trait.

As said earlier, dictionaries in Cairo are types that must be "squashed" when destructed, so that the sequence of access can be proven. This is easy for developers to forget, so instead dictionaries implement the `Destruct` trait to ensure that all dictionaries are _squashed_ when going out of scope.
As such, the following example will not compile:

```cairo,does_not_compile
use core::dict::Felt252Dict;

struct A {
    dict: Felt252Dict<u128>,
}

fn main() {
    A { dict: Default::default() };
}
```

If you try to run this code, you will get a compile-time error:

```shell
$ scarb execute
   Compiling no_listing_06_no_destruct_compile_fails v0.1.0 (listings/ch04-understanding-ownership/no_listing_06_no_destruct_compile_fails/Scarb.toml)
error: Variable not dropped.
 --> listings/ch04-understanding-ownership/no_listing_06_no_destruct_compile_fails/src/lib.cairo:9:5
    A { dict: Default::default() };
    ^****************************^
note: Trait has no implementation in context: core::traits::Drop::<no_listing_06_no_destruct_compile_fails::A>.
note: Trait has no implementation in context: core::traits::Destruct::<no_listing_06_no_destruct_compile_fails::A>.

error: could not compile `no_listing_06_no_destruct_compile_fails` due to previous error
error: `scarb metadata` exited with error

```

When `A` goes out of scope, it can't be dropped as it implements neither the `Drop` (as it contains a dictionary and can't `derive(Drop)`) nor the `Destruct` trait. To fix this, we can derive the `Destruct` trait implementation for the `A` type:

```cairo
use core::dict::Felt252Dict;

#[derive(Destruct)]
struct A {
    dict: Felt252Dict<u128>,
}

fn main() {
    A { dict: Default::default() }; // No error here
}
```

Now, when `A` goes out of scope, its dictionary will be automatically `squashed`, and the program will compile.

## Copy Array Data with `clone`

If we _do_ want to deeply copy the data of an `Array`, we can use a common method called `clone`. We’ll discuss method syntax in a dedicated section in [Chapter 5][method syntax], but because methods are a common feature in many programming languages, you’ve probably seen them before.

Here’s an example of the `clone` method in action.

```cairo
fn main() {
    let arr1: Array<u128> = array![];
    let arr2 = arr1.clone();
}
```

When you see a call to `clone`, you know that some arbitrary code is being executed and that code may be expensive. It’s a visual indicator that something different is going on.
In this case, the _value_ `arr1` refers to is being copied, resulting in new memory cells being used, and a new _variable_ `arr2` is created, referring to the new copied value.

[method syntax]: ./ch05-03-method-syntax.md

## Return Values and Scope

Returning values is equivalent to _moving_ them. Listing 4-2 shows an example of a
function that returns some value, with similar annotations as those in Listing 4-1.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
#[derive(Drop)]
struct A {}

fn main() {
    let a1 = gives_ownership();           // gives_ownership moves its return
                                          // value into a1

    let a2 = A {};                        // a2 comes into scope

    let a3 = takes_and_gives_back(a2);    // a2 is moved into
                                          // takes_and_gives_back, which also
                                          // moves its return value into a3

} // Here, a3 goes out of scope and is dropped. a2 was moved, so nothing
  // happens. a1 goes out of scope and is dropped.

fn gives_ownership() -> A {               // gives_ownership will move its
                                          // return value into the function
                                          // that calls it

    let some_a = A {};                    // some_a comes into scope

    some_a                                // some_a is returned and
                                          // moves ownership to the calling
                                          // function
}

// This function takes an instance some_a of A and returns it
fn takes_and_gives_back(some_a: A) -> A { // some_a comes into scope

    some_a                                // some_a is returned and
                                          // moves ownership to the calling
                                          // function
}
```

<span class="caption">Listing 4-2: Moving return values</span>

While this works, moving into and out of every function is a bit tedious. What if we want to let a function use a value but not move the value? It’s quite annoying that anything we pass in also needs to be passed back if we want to use it again, in addition to any data resulting from the body of the function that we might want to return as well.

Cairo does let us return multiple values using a tuple, as shown in Listing 4-3.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
fn main() {
    let arr1: Array<u128> = array![];

    let (arr2, len) = calculate_length(arr1);
}

fn calculate_length(arr: Array<u128>) -> (Array<u128>, usize) {
    let length = arr.len(); // len() returns the length of an array

    (arr, length)
}
```

<span class="caption">Listing 4-3: Returning many values</span>

But this is too much ceremony and a lot of work for a concept that should be common. Luckily for us, Cairo has two features for passing a value without destroying or moving it, called _references_ and _snapshots_.
# References and Snapshots

The issue with the tuple code in previous Listing 4-3 is that we have to return the
`Array` to the calling function so we can still use the `Array` after the
call to `calculate_length`, because the `Array` was moved into
`calculate_length`.

## Snapshots

In the previous chapter, we talked about how Cairo's ownership system prevents us from using a variable after we've moved it, protecting us from potentially writing twice to the same memory cell. However, it's not very convenient. Let's see how we can retain ownership of the variable in the calling function using snapshots.

In Cairo, a snapshot is an immutable view of a value at a certain point in the execution of the program. Recall that memory is immutable, so modifying a variable actually fills a new memory cell. The old memory cell still exists, and snapshots are variables that refer to that "old" value. In this sense, snapshots are a view "into the past".

Here is how you would define and use a `calculate_area` function that takes a snapshot of a `Rectangle` struct as a parameter instead of taking ownership of the underlying value. In this example, the `calculate_area` function returns the area of the `Rectangle` passed as a snapshot. Since we’re passing it as an immutable view, we can be sure that `calculate_area` will not mutate the `Rectangle`, and ownership remains in the `main` function.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
#[derive(Drop)]
struct Rectangle {
    height: u64,
    width: u64,
}

fn main() {
    let mut rec = Rectangle { height: 3, width: 10 };
    let first_snapshot = @rec; // Take a snapshot of `rec` at this point in time
    rec.height = 5; // Mutate `rec` by changing its height
    let first_area = calculate_area(first_snapshot); // Calculate the area of the snapshot
    let second_area = calculate_area(@rec); // Calculate the current area
    println!("The area of the rectangle when the snapshot was taken is {}", first_area);
    println!("The current area of the rectangle is {}", second_area);
}

fn calculate_area(rec: @Rectangle) -> u64 {
    *rec.height * *rec.width
}
```

> Note: Accessing fields of a snapshot (e.g., `rec.height`) yields snapshots of those fields, which we desnap with `*` to get the values. This works here because `u64` implements `Copy`. You’ll learn more about desnapping in the next section.

The output of this program is:

```shell
$ scarb execute
warn: `scarb execute` will be deprecated soon
help: use `scarb execute` instead
   Compiling no_listing_09_snapshots v0.1.0 (listings/ch04-understanding-ownership/no_listing_09_snapshots/Scarb.toml)
    Finished `dev` profile target(s) in 2 seconds
     Running no_listing_09_snapshots
The area of the rectangle when the snapshot was taken is 30
The current area of the rectangle is 50
Run completed successfully, returning []

```

First, notice that all the tuple code in the variable declaration and the function return value is gone. Second, note that we pass `@rec` into `calculate_area` and, in its definition, we take `@Rectangle` rather than `Rectangle`.

Let’s take a closer look at the function call here:

```cairo
let second_length = calculate_length(@arr1); // Calculate the current length of the array
```

The `@rec` syntax lets us create a snapshot of the value in `rec`. Because a snapshot is an immutable view of a value at a specific point in execution, the usual rules of the linear type system are not enforced. In particular, snapshot variables always implement the `Drop` trait, never the `Destruct` trait, even dictionary snapshots.

It’s worth noting that `@T` is not a pointer—snapshots are passed by value to functions, just like regular variables. This means that the size of `@T` is the same as the size of `T`, and when you pass `@rec` to `calculate_area`, the entire struct (in this case, a `Rectangle` with two `u64` fields) is copied to the function’s stack. For large data structures, this copying can be avoided by using `Box<T>`—provided that there's no need to mutate the value, which we’ll explore in [Chapter 12][chap-smart-pointers], but for now, understand that snapshots rely on this by-value mechanism.

Similarly, the signature of the function uses `@` to indicate that the type of the parameter `arr` is a snapshot. Let’s add some explanatory annotations:

```cairo, noplayground
fn calculate_area(
    rec_snapshot: @Rectangle // rec_snapshot is a snapshot of a Rectangle
) -> u64 {
    *rec_snapshot.height * *rec_snapshot.width
} // Here, rec_snapshot goes out of scope and is dropped.
// However, because it is only a view of what the original `rec` contains, the original `rec` can still be used.
```

The scope in which the variable `rec_snapshot` is valid is the same as any function parameter’s scope, but the underlying value of the snapshot is not dropped when `rec_snapshot` stops being used. When functions have snapshots as parameters instead of the actual values, we won’t need to return the values in order to give back ownership of the original value, because we never had it.

### Desnap Operator

To convert a snapshot back into a regular variable, you can use the `desnap` operator `*`, which serves as the opposite of the `@` operator.

Only `Copy` types can be desnapped. However, in the general case, because the value is not modified, the new variable created by the `desnap` operator reuses the old value, and so desnapping is a completely free operation, just like `Copy`.

In the following example, we want to calculate the area of a rectangle, but we don't want to take ownership of the rectangle in the `calculate_area` function, because we might want to use the rectangle again after the function call. Since our function doesn't mutate the rectangle instance, we can pass the snapshot of the rectangle to the function, and then transform the snapshots back into values using the `desnap` operator `*`.

```cairo
#[derive(Drop)]
struct Rectangle {
    height: u64,
    width: u64,
}

fn main() {
    let rec = Rectangle { height: 3, width: 10 };
    let area = calculate_area(@rec);
    println!("Area: {}", area);
}

fn calculate_area(rec: @Rectangle) -> u64 {
    // As rec is a snapshot to a Rectangle, its fields are also snapshots of the fields types.
    // We need to transform the snapshots back into values using the desnap operator `*`.
    // This is only possible if the type is copyable, which is the case for u64.
    // Here, `*` is used for both multiplying the height and width and for desnapping the snapshots.
    *rec.height * *rec.width
}
```

But, what happens if we try to modify something we’re passing as a snapshot? Try the code in
Listing 4-4. Spoiler alert: it doesn’t work!

<span class="filename">Filename: src/lib.cairo</span>

```cairo,does_not_compile
#[derive(Copy, Drop)]
struct Rectangle {
    height: u64,
    width: u64,
}

fn main() {
    let rec = Rectangle { height: 3, width: 10 };
    flip(@rec);
}

fn flip(rec: @Rectangle) {
    let temp = rec.height;
    rec.height = rec.width;
    rec.width = temp;
}
```


<span class="caption">Listing 4-4: Attempting to modify a snapshot value</span>

Here’s the error:

```shell
$ scarb execute
   Compiling listing_04_04 v0.1.0 (listings/ch04-understanding-ownership/listing_04_attempt_modifying_snapshot/Scarb.toml)
error: Invalid left-hand side of assignment.
 --> listings/ch04-understanding-ownership/listing_04_attempt_modifying_snapshot/src/lib.cairo:15:5
    rec.height = rec.width;
    ^********^

error: Invalid left-hand side of assignment.
 --> listings/ch04-understanding-ownership/listing_04_attempt_modifying_snapshot/src/lib.cairo:16:5
    rec.width = temp;
    ^*******^

error: could not compile `listing_04_04` due to previous error
error: `scarb metadata` exited with error

```

The compiler prevents us from modifying values associated to snapshots.

## Mutable References

We can achieve the behavior we want in Listing 4-4 by using a _mutable reference_ instead of a snapshot. Mutable references are actually mutable values passed to a function that are implicitly returned at the end of the function, returning ownership to the calling context. By doing so, they allow you to mutate the value passed while keeping ownership of it by returning it automatically at the end of the execution.
In Cairo, a parameter can be passed as _mutable reference_ using the `ref` modifier.

> **Note**: In Cairo, a parameter can only be passed as _mutable reference_ using the `ref` modifier if the variable is declared as mutable with `mut`.

In Listing 4-5, we use a mutable reference to modify the value of the `height` and `width` fields of the `Rectangle` instance in the `flip` function.

```cairo
#[derive(Drop)]
struct Rectangle {
    height: u64,
    width: u64,
}

fn main() {
    let mut rec = Rectangle { height: 3, width: 10 };
    flip(ref rec);
    println!("height: {}, width: {}", rec.height, rec.width);
}

fn flip(ref rec: Rectangle) {
    let temp = rec.height;
    rec.height = rec.width;
    rec.width = temp;
}
```

<span class="caption">Listing 4-5: Use of a mutable reference to modify a value</span>

First, we change `rec` to be `mut`. Then we pass a mutable reference of `rec` into `flip` with `ref rec`, and update the function signature to accept a mutable reference with `ref rec: Rectangle`. This makes it very clear that the `flip` function will mutate the value of the `Rectangle` instance passed as parameter.

Unlike snapshots, mutable references allow mutation, but like snapshots, `ref` arguments are not pointers—they are also passed by value. When you pass `ref rec`, the entire `Rectangle` type is copied to the function’s stack, regardless of whether it implements `Copy`. This ensures the function operates on its own local version of the data, which is then implicitly returned to the caller. To avoid this copying for large types, Cairo provides the `Box<T>` type introduced in [Chapter 12][chap-smart-pointers] as an alternative, but for this example, the `ref` modifier suits our needs perfectly.

The output of the program is:

```shell
$ scarb execute
   Compiling listing_04_05 v0.1.0 (listings/ch04-understanding-ownership/listing_05_mutable_reference/Scarb.toml)
    Finished `dev` profile target(s) in 3 seconds
     Running listing_04_05
height: 10, width: 3
Run completed successfully, returning []

```

As expected, the `height` and `width` fields of the `rec` variable have been swapped.

<div class="quiz-placeholder" data-quiz-name="&quot;ch04-02-references-and-snapshots&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;The code does not compile because the *desnap* operator has to be used on snapshots, not references.\nInside the `incr` function, the `n` parameter is a reference to a `u32` value, so the `*n` operation is not allowed. The code should be changed to `n += 1;`.\n&quot;,&quot;id&quot;:&quot;6555e9b4-5989-40ee-a8e8-e1fd70d7aa1f&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn incr(ref n: u32) {\n    *n += 1;\n}\n\nfn main() {\n    let mut n : u32 = 1;\n    incr(ref n);\n    println!(\&quot;{}\&quot;, n);\n}\n&quot;}},{&quot;context&quot;:&quot;The code does not compile because a `ref` can only be used on mutable variables.\nYou should write `let mut rect = Rectangle { height: 10, width: 20 };` instead.\n&quot;,&quot;id&quot;:&quot;7237725b-b4d8-4c05-81be-8d8dd4056cc6&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Drop)]\nstruct Rectangle {\n    height: u64,\n    width: u64,\n}\n\nfn double_rect(ref rect: Rectangle) {\n    rect.height *= 2;\n    rect.width *= 2;\n}\n\nfn main() {\n    let rect = Rectangle { height: 10, width: 20 };\n    double_rect(ref rect);\n    println!(\&quot;{}\&quot;, rect.height);\n}\n&quot;}},{&quot;context&quot;:&quot;First `snap` and `snap2` are snapshots of a memory location that contains the array `arr1`.\nThen, `arr1` is mutated by appending a new element.\nFinally, `snap2` is updated to be a snapshot of the new array while `snap` remains a snapshot of the old array.\nThe function `sum` receives the latter and returns its sum before the mutation.\n&quot;,&quot;id&quot;:&quot;4512ce8b-c183-4ad1-96e9-bb808456c321&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;6&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn sum(arr: @Array&lt;u128&gt;) -&gt; u128 {\n    let mut span = arr.span();\n    let mut sum = 0;\n    while let Some(x) = span.pop_front() {\n        sum += *x;\n    };\n    sum\n}\n\nfn main() {\n    let mut arr1: Array&lt;u128&gt; = array![1, 2, 3];\n    let snap = @arr1;\n    let mut snap2 = snap;\n    arr1.append(4);\n    snap2 = @arr1;\n    println!(\&quot;{}\&quot;, sum(snap));\n}\n&quot;}},{&quot;context&quot;:&quot;We want to modify the array and return the ownership to the main function so we must use a mutable reference to the array.\nThe snapshot can't be used because it is immutable and operating on it does not alter the value of the underlying array.\nA mutable reference must be used on mutable variables.\nTo pass a mutable reference as an argument, we must use the `ref` keyword in the definition of the function parameter **and** during the call of the function.\n&quot;,&quot;id&quot;:&quot;b691d9bd-4047-4eb3-bbc8-096f889bb5ac&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;```\nfn give_and_take(ref arr: Array&lt;u128&gt;, n: u128) -&gt; u128 {\n    arr.append(n);\n    arr.pop_front().unwrap_or(0)\n}\nfn main() {\n    let mut arr1: Array&lt;u128&gt; = array![1,2,3];\n    let elem = give_and_take(ref arr1, 4);\n    println!(\&quot;{}\&quot;, elem);\n}\n```\n&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;```\nfn give_and_take(arr: @Array&lt;u128&gt;, n: u128) -&gt; u128 {\n    arr.append(n);\n    arr.pop_front().unwrap_or(0)\n}\nfn main() {\n    let mut arr1: Array&lt;u128&gt; = array![1,2,3];\n    let elem = give_and_take(@arr1, 4);\n    println!(\&quot;{}\&quot;, elem);\n}\n```\n&quot;,&quot;```\nfn give_and_take(arr: @Array&lt;u128&gt;, n: u128) -&gt; u128 {\n    *arr.append(n);\n    *arr.pop_front().unwrap_or(0)\n}\nfn main() {\n    let mut arr1: Array&lt;u128&gt; = array![1,2,3];\n    let elem = give_and_take(@arr1, 4);\n    println!(\&quot;{}\&quot;, elem);\n}\n```\n&quot;,&quot;```\nfn give_and_take(ref arr: Array&lt;u128&gt;, n: u128) -&gt; u128 {\n    arr.append(n);\n    arr.pop_front().unwrap_or(0)\n}\nfn main() {\n    let mut arr1: Array&lt;u128&gt; = array![1,2,3];\n    let elem = give_and_take(arr1, 4);\n    println!(\&quot;{}\&quot;, elem);\n}\n```\n&quot;,&quot;```\nfn give_and_take(ref arr: Array&lt;u128&gt;, n: u128) -&gt; u128 {\n    arr.append(n);\n    arr.pop_front().unwrap_or(0)\n}\nfn main() {\n    let arr1: Array&lt;u128&gt; = array![1,2,3];\n    let elem = give_and_take(ref arr1, 4);\n    println!(\&quot;{}\&quot;, elem);\n}\n```\n&quot;],&quot;prompt&quot;:&quot;Choose the working code snippet that properly defines and uses the function to insert a value at the end of an array while removing the first element and returning it.\nThe array has to be modified by the function and should be usable after the function call.\n&quot;}}]}"></div>

## Small Recap

Let’s recap what we’ve discussed about the linear type system, ownership, snapshots, and references:

- At any given time, a variable can only have one owner.
- You can pass a variable by-value, by-snapshot, or by-reference to a function.
- If you pass-by-value, ownership of the variable is transferred to the function.
- If you want to keep ownership of the variable and know that your function won’t mutate it, you can pass it as a snapshot with `@`.
- If you want to keep ownership of the variable and know that your function will mutate it, you can pass it as a mutable reference with `ref`.

[chap-smart-pointers]: ./ch12-02-smart-pointers.md


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Using Structs to Structure Related Data

A struct, or structure, is a custom data type that lets you package together and name multiple related values that make up a meaningful group. If you’re familiar with an object-oriented language, a struct is like an object’s data attributes. In this chapter, we’ll compare and contrast tuples with structs to build on what you already know and demonstrate when structs are a better way to group data.

We’ll demonstrate how to define and instantiate structs. We’ll discuss how to define associated functions, especially the kind of associated functions called methods, to specify behavior associated with a struct type. Structs and enums (discussed in the [next chapter](ch06-01-enums.md)) are the building blocks for creating new types in your program’s domain to take full advantage of Cairo's compile-time type checking.
# Defining and Instantiating Structs

Structs are similar to tuples, discussed in the [Data Types](ch02-02-data-types.md) section, in that both hold multiple related values. Like tuples, the pieces of a struct can be different types. Unlike with tuples, in a struct you’ll name each piece of data so it’s clear what the values mean. Adding these names means that structs are more flexible than tuples: you don’t have to rely on the order of the data to specify or access the values of an instance.

To define a struct, we enter the keyword `struct` and name the entire struct. A struct’s name should describe the significance of the pieces of data being grouped together. Then, inside curly brackets, we define the names and types of the pieces of data, which we call fields. For example, Listing 5-1 shows a struct that stores information about a user account.

<span class="filename">Filename: src/lib.cairo</span>

```cairo, noplayground
#[derive(Drop)]
struct User {
    active: bool,
    username: ByteArray,
    email: ByteArray,
    sign_in_count: u64,
}
```


<span class="caption">Listing 5-1: A `User` struct definition</span>

To use a struct after we’ve defined it, we create an _instance_ of that struct by specifying concrete values for each of the fields.
We create an instance by stating the name of the struct and then add curly brackets containing _key: value_ pairs, where the keys are the names of the fields and the values are the data we want to store in those fields. We don’t have to specify the fields in the same order in which we declared them in the struct. In other words, the struct definition is like a general template for the type, and instances fill in that template with particular data to create values of the type.

For example, we can declare two particular users as shown in Listing 5-2.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
#[derive(Drop)]
struct User {
    active: bool,
    username: ByteArray,
    email: ByteArray,
    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        active: true, username: "someusername123", email: "someone@example.com", sign_in_count: 1,
    };
    let user2 = User {
        sign_in_count: 1, username: "someusername123", active: true, email: "someone@example.com",
    };
}

```

<span class="caption">Listing 5-2: Creating two instances of the `User` struct</span>

To get a specific value from a struct, we use dot notation. For example, to access `user1`'s email address, we use `user1.email`. If the instance is mutable, we can change a value by using the dot notation and assigning into a particular field. Listing 5-3 shows how to change the value in the `email` field of a mutable `User` instance.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
# #[derive(Drop)]
# struct User {
#     active: bool,
#     username: ByteArray,
#     email: ByteArray,
#     sign_in_count: u64,
# }
fn main() {
    let mut user1 = User {
        active: true, username: "someusername123", email: "someone@example.com", sign_in_count: 1,
    };
    user1.email = "anotheremail@example.com";
}
#
# fn build_user(email: ByteArray, username: ByteArray) -> User {
#     User { active: true, username: username, email: email, sign_in_count: 1 }
# }
#
# fn build_user_short(email: ByteArray, username: ByteArray) -> User {
#     User { active: true, username, email, sign_in_count: 1 }
# }
#
#
```

<span class="caption">Listing 5-3: Changing the value in the email field of a `User` instance</span>

Note that the entire instance must be mutable; Cairo doesn’t allow us to mark only certain fields as mutable.

As with any expression, we can construct a new instance of the struct as the last expression in the function body to implicitly return that new instance.

Listing 5-4 shows a `build_user` function that returns a `User` instance with the given email and username. The `active` field gets the value of `true`, and the `sign_in_count` gets a value of `1`.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
# #[derive(Drop)]
# struct User {
#     active: bool,
#     username: ByteArray,
#     email: ByteArray,
#     sign_in_count: u64,
# }
# fn main() {
#     let mut user1 = User {
#         active: true, username: "someusername123", email: "someone@example.com", sign_in_count: 1,
#     };
#     user1.email = "anotheremail@example.com";
# }
#
fn build_user(email: ByteArray, username: ByteArray) -> User {
    User { active: true, username: username, email: email, sign_in_count: 1 }
}
#
# fn build_user_short(email: ByteArray, username: ByteArray) -> User {
#     User { active: true, username, email, sign_in_count: 1 }
# }
#
#
```

<span class="caption">Listing 5-4: A `build_user` function that takes an email and username and returns a `User` instance.</span>

It makes sense to name the function parameters with the same name as the struct fields, but having to repeat the `email` and `username` field names and variables is a bit tedious. If the struct had more fields, repeating each name would get even more annoying. Luckily, there’s a convenient shorthand!

## Using the Field Init Shorthand

Because the parameter names and the struct field names are exactly the same in Listing 5-4, we can use the field init shorthand syntax to rewrite `build_user` so it behaves exactly the same but doesn’t have the repetition of `username` and `email`, as shown in Listing 5-5.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
# #[derive(Drop)]
# struct User {
#     active: bool,
#     username: ByteArray,
#     email: ByteArray,
#     sign_in_count: u64,
# }
# fn main() {
#     let mut user1 = User {
#         active: true, username: "someusername123", email: "someone@example.com", sign_in_count: 1,
#     };
#     user1.email = "anotheremail@example.com";
# }
#
# fn build_user(email: ByteArray, username: ByteArray) -> User {
#     User { active: true, username: username, email: email, sign_in_count: 1 }
# }
#
fn build_user_short(email: ByteArray, username: ByteArray) -> User {
    User { active: true, username, email, sign_in_count: 1 }
}
#
#
```

<span class="caption">Listing 5-5: A `build_user` function that uses field init shorthand because the `username` and `email` parameters have the same name as struct fields.</span>

Here, we’re creating a new instance of the `User` struct, which has a field named `email`. We want to set the `email` field’s value to the value in the `email` parameter of the `build_user` function. Because the `email` field and the `email` parameter have the same name, we only need to write `email` rather than `email: email`.

## Creating Instances from Other Instances with Struct Update Syntax

It’s often useful to create a new instance of a struct that includes most of
the values from another instance, but changes some. You can do this using
_struct update syntax_.

First, in Listing 5-6 we show how to create a new `User` instance in `user2`
regularly, without the update syntax. We set a new value for `email` but
otherwise use the same values from `user1` that we created in Listing 5-2.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
# #[derive(Drop)]
# struct User {
#     active: bool,
#     username: ByteArray,
#     email: ByteArray,
#     sign_in_count: u64,
# }
#
fn main() {
    // --snip--
#
#     let user1 = User {
#         email: "someone@example.com", username: "someusername123", active: true, sign_in_count: 1,
#     };

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: "another@example.com",
        sign_in_count: user1.sign_in_count,
    };
}
#
#
```


<span class="caption">Listing 5-6: Creating a new `User` instance using all but one of the values from `user1`</span>

Using struct update syntax, we can achieve the same effect with less code, as
shown in Listing 5-7. The syntax `..` specifies that the remaining fields not
explicitly set should have the same value as the fields in the given instance.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
# use core::byte_array;
# #[derive(Drop)]
# struct User {
#     active: bool,
#     username: ByteArray,
#     email: ByteArray,
#     sign_in_count: u64,
# }
#
fn main() {
    // --snip--
#
#     let user1 = User {
#         email: "someone@example.com", username: "someusername123", active: true, sign_in_count: 1,
#     };

    let user2 = User { email: "another@example.com", ..user1 };
}
#
#
```


<span class="caption">Listing 5-7: Using struct update syntax to set a new
`email` value for a `User` instance but to use the rest of the values from `user1`</span>

The code in Listing 5-7 also creates an instance of `user2` that has a
different value for `email` but has the same values for the `username`,
`active`, and `sign_in_count` fields as `user1`. The `..user1` part must come last
to specify that any remaining fields should get their values from the
corresponding fields in `user1`, but we can choose to specify values for as
many fields as we want in any order, regardless of the order of the fields in
the struct’s definition.

Note that the struct update syntax uses `=` like an assignment; this is because it moves the data,
just as we saw in the ["Moving Values"][move]<!-- ignore --> section. In this example, we can no
longer use `user1` as a whole after creating `user2` because the `ByteArray` in the
`username` field of `user1` was moved into `user2`. If we had given `user2` new
`ByteArray` values for both `email` and `username`, and thus only used the
`active` and `sign_in_count` values from `user1`, then `user1` would still be
valid after creating `user2`. Both `active` and `sign_in_count` are types that
implement the `Copy` trait, so the behavior we discussed in the ["`Copy` Trait"][copy]<!-- ignore --> section would apply.

<div class="quiz-placeholder" data-quiz-name="&quot;ch05-01-defining-and-instantiating-structs&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;The `..a` syntax copies each field of `a` into `b` (except `y`), so the second `a.x += 1` has no effect on `b`.\n&quot;,&quot;id&quot;:&quot;bba8893d-f59f-492a-b639-ea04a5c8093b&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;2&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Copy, Drop)]\nstruct Point {\n  x: u32,\n  y: u32,\n}\n\nfn main() {\n  let mut a = Point { x: 1, y: 2 };\n  a.x += 1;\n  let b = Point { y: 1, ..a };\n  a.x += 1;\n  println!(\&quot;{}\&quot;, b.x);\n}\n&quot;}},{&quot;context&quot;:&quot;`p.x` and `p.y` are __copied__ into new `x` and `y` variables, so the `x += 1` and `y += 1` lines have no effect on `p`.\n&quot;,&quot;id&quot;:&quot;77ef68d6-ee7f-4642-8817-73b846c46b2b&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;1 2&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Copy, Drop)]\nstruct Point {\n    x: u32,\n    y: u32,\n}\n\nfn main() {\n    let mut p = Point { x: 1, y: 2 };\n    let mut x = p.x;\n    let mut y = p.y;\n    x += 1;\n    y += 1;\n    println!(\&quot;{} {}\&quot;, p.x, p.y);\n}\n&quot;}}]}"></div>

[move]: ch04-01-what-is-ownership.md#moving-values
[copy]: ch04-01-what-is-ownership.md#the-copy-trait


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># An Example Program Using Structs

To understand when we might want to use structs, let’s write a program that calculates the area of a rectangle. We’ll start by using single variables, and then refactor the program until we’re using structs instead.

Let’s make a new project with Scarb called _rectangles_ that will take the width and height of a rectangle specified in pixels and calculate the area of the rectangle. Listing 5-8 shows a short program with one way of doing exactly that in our project’s _src/lib.cairo_.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
fn main() {
    let width = 30;
    let height = 10;
    let area = area(width, height);
    println!("Area is {}", area);
}

fn area(width: u64, height: u64) -> u64 {
    width * height
}
```

<span class="caption">Listing 5-8: Calculating the area of a rectangle specified by separate width and height variables.</span>

Now run the program with `scarb execute`:

```shell
$ scarb execute
   Compiling listing_04_06_no_struct v0.1.0 (listings/ch05-using-structs-to-structure-related-data/listing_03_no_struct/Scarb.toml)
    Finished `dev` profile target(s) in 3 seconds
     Running listing_04_06_no_struct
Area is 300
Run completed successfully, returning []

```

This code succeeds in figuring out the area of the rectangle by calling the `area` function with each dimension, but we can do more to make this code clear and readable.

The issue with this code is evident in the signature of `area`:

```cairo,noplayground
fn area(width: u64, height: u64) -> u64 {
```

The `area` function is supposed to calculate the area of one rectangle, but the function we wrote has two parameters, and it’s not clear anywhere in our program that the parameters are related. It would be more readable and more manageable to group width and height together. We’ve already discussed one way we might do that in the [Tuple Section of Chapter 2](./ch02-02-data-types.md#the-tuple-type).

## Refactoring with Tuples

Listing 5-9 shows another version of our program that uses tuples.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
fn main() {
    let rectangle = (30, 10);
    let area = area(rectangle);
    println!("Area is {}", area);
}

fn area(dimension: (u64, u64)) -> u64 {
    let (x, y) = dimension;
    x * y
}
```

<span class="caption">Listing 5-9: Specifying the width and height of the rectangle with a tuple.</span>

In one way, this program is better. Tuples let us add a bit of structure, and we’re now passing just one argument. But in another way, this version is less clear: tuples don’t name their elements, so we have to index into the parts of the tuple, making our calculation less obvious.

Mixing up the width and height wouldn’t matter for the area calculation, but if we want to calculate the difference, it would matter! We would have to keep in mind that `width` is the tuple index `0` and `height` is the tuple index `1`. This would be even harder for someone else to figure out and keep in mind if they were to use our code. Because we haven’t conveyed the meaning of our data in our code, it’s now easier to introduce errors.

## Refactoring with Structs: Adding More Meaning

We use structs to add meaning by labeling the data. We can transform the tuple we’re using into a struct with a name for the whole as well as names for the parts.

<span class="filename">Filename: src/lib.cairo</span>

```cairo
struct Rectangle {
    width: u64,
    height: u64,
}

fn main() {
    let rectangle = Rectangle { width: 30, height: 10 };
    let area = area(rectangle);
    println!("Area is {}", area);
}

fn area(rectangle: Rectangle) -> u64 {
    rectangle.width * rectangle.height
}
```

<span class="caption">Listing 5-10: Defining a `Rectangle` struct.</span>

Here we’ve defined a struct and named it `Rectangle`. Inside the curly brackets, we defined the fields as `width` and `height`, both of which have type `u64`. Then, in `main`, we created a particular instance of `Rectangle` that has a width of `30` and a height of `10`. Our `area` function is now defined with one parameter, which we’ve named `rectangle` which is of type `Rectangle` struct. We can then access the fields of the instance with dot notation, and it gives descriptive names to the values rather than using the tuple index values of `0` and `1`.

## Conversions of Custom Types

We've already described how to perform type conversion on in-built types, see [Data Types > Type Conversion][type-conversion]. In this section, we will see how to define conversions for custom types.

> Note: conversion can be defined for compound types, e.g. tuples, too.

[type-conversion]: ./ch02-02-data-types.md#type-conversion

### Into

Defining a conversion for a custom type using the `Into` trait will typically require specification of the type to convert into, as the compiler is unable to determine this most of the time. However this is a small trade-off considering we get the functionality for free.

```cairo
// Compiler automatically imports the core library, so you can omit this import
use core::traits::Into;

#[derive(Drop, PartialEq)]
struct Rectangle {
    width: u64,
    height: u64,
}

#[derive(Drop)]
struct Square {
    side_length: u64,
}

impl SquareIntoRectangle of Into<Square, Rectangle> {
    fn into(self: Square) -> Rectangle {
        Rectangle { width: self.side_length, height: self.side_length }
    }
}

fn main() {
    let square = Square { side_length: 5 };
    // Compiler will complain if you remove the type annotation
    let result: Rectangle = square.into();
    let expected = Rectangle { width: 5, height: 5 };
    assert!(
        result == expected,
        "A square is always convertible to a rectangle with the same width and height!",
    );
}
```

### TryInto

Defining a conversion for `TryInto` is similar to defining it for `Into`.

```cairo
// Compiler automatically imports the core library, so you can omit this import
use core::traits::TryInto;

#[derive(Drop)]
struct Rectangle {
    width: u64,
    height: u64,
}

#[derive(Drop, PartialEq)]
struct Square {
    side_length: u64,
}

impl RectangleIntoSquare of TryInto<Rectangle, Square> {
    fn try_into(self: Rectangle) -> Option<Square> {
        if self.height == self.width {
            Some(Square { side_length: self.height })
        } else {
            None
        }
    }
}

fn main() {
    let rectangle = Rectangle { width: 8, height: 8 };
    let result: Square = rectangle.try_into().unwrap();
    let expected = Square { side_length: 8 };
    assert!(
        result == expected,
        "Rectangle with equal width and height should be convertible to a square.",
    );

    let rectangle = Rectangle { width: 5, height: 8 };
    let result: Option<Square> = rectangle.try_into();
    assert!(
        result.is_none(),
        "Rectangle with different width and height should not be convertible to a square.",
    );
}
```

<div class="quiz-placeholder" data-quiz-name="&quot;ch05-02-an-example-program-using-structs&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;The area function takes ownership of its argument `rectangle`, which doesn't implement `Copy`. Calling `perimeter(rectangle)` therefore moves `rectangle`, meaning it cannot be used on the next line.&quot;,&quot;id&quot;:&quot;3d5a7161-f117-46c6-a293-ccbabe4b4a9d&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Drop)]\nstruct Rectangle {\n    width: u64,\n    height: u64,\n}\n\nfn perimeter(r: Rectangle) -&gt; u64 {\n    2 * (r.width + r.height)\n}\n\nfn main() {\n    let rectangle = Rectangle { width: 20, height: 10, };\n    let p = perimeter(rectangle);\n    println!(\&quot;2 * ({} + {}) = {}\&quot;, rectangle.width, rectangle.height, p);\n}\n&quot;}},{&quot;context&quot;:&quot;Destructuring refers to the process of extracting individual fields from a struct and binding them to separate variables. When destructuring a struct, you can either use variables with the same names as the struct fields or explicitly bind the fields to variables with different names using the syntax `field_name: variable_name`.&quot;,&quot;id&quot;:&quot;da04e96e-b05c-489d-819a-07e53cc4fee4&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;struct Point { x: u128, y: u128, }\n\nfn main() {\n    let p = Point { x: 5, y: 10 };\n    let Point { z, w } = p;\n    println!(\&quot;The values of z and w are: ({}, {})\&quot;, z, w);\n}\n&quot;}}]}"></div>


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Method Syntax

_Methods_ are similar to functions: we declare them with the `fn` keyword and a name, they can have parameters and a return value, and they contain some code that’s run when the method is called from somewhere else. Unlike functions, methods are defined within the context of a struct (or an enum which we cover in [Chapter 6][enums]), and their first parameter is always `self`, which represents the instance of the type the method is being called on.

## Defining Methods

Let’s change the `area` function that has a `Rectangle` instance as a parameter and instead make an `area` method defined on the `Rectangle` struct, as shown in Listing 5-11

```cairo, noplayground
#[derive(Copy, Drop)]
struct Rectangle {
    width: u64,
    height: u64,
}

trait RectangleTrait {
    fn area(self: @Rectangle) -> u64;
}

impl RectangleImpl of RectangleTrait {
    fn area(self: @Rectangle) -> u64 {
        (*self.width) * (*self.height)
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    println!("Area is {}", rect1.area());
}
```

Listing 5-11: Defining an `area` method on the `Rectangle` struct.

To define the function within the context of `Rectangle`, we start an `impl` (implementation) block for a trait `RectangleTrait` that defines the methods that can be called on a `Rectangle` instance. As impl blocks can only be defined for traits and not types, we need to define this trait first - but it's not meant to be used for anything else.

Everything within this `impl` block will be associated with the `Rectangle` type. Then we move the `area` function within the `impl` curly brackets and change the first (and in this case, only) parameter to be `self` in the signature and everywhere within the body. In `main`, where we called the `area` function and passed `rect1` as an argument, we can instead use _method syntax_ to call the `area` method on our `Rectangle` instance. The method syntax goes after an instance: we add a dot followed by the method name, parentheses, and any arguments.

In the signature for `area`, we use `self: @Rectangle` instead of `rectangle: @Rectangle`.
Methods must have a parameter named `self`, for their first parameter, and the type of `self` indicates the type that method can be called on. Methods can take ownership of `self`, but `self` can also be passed by snapshot or by reference, just like any other parameter.

> There is no direct link between a type and a trait. Only the type of the `self` parameter of a method defines the type from which this method can be called. That means, it is technically possible to define methods on multiple types in a same trait (mixing `Rectangle` and `Circle` methods, for example). But **this is not a recommended practice** as it can lead to confusion.

The main reason for using methods instead of functions, in addition to providing method syntax, is for organization. We’ve put all the things we can do with an instance of a type in one `impl` block rather than making future users of our code search for capabilities of `Rectangle` in various places in the library we provide.

## The `generate_trait` Attribute

If you are familiar with Rust, you may find Cairo's approach confusing because methods cannot be defined directly on types. Instead, you must define a [trait](./ch08-02-traits-in-cairo.md) and an implementation of this trait associated with the type for which the method is intended.
However, defining a trait and then implementing it to define methods on a specific type is verbose, and unnecessary: the trait itself will not be reused.

So, to avoid defining useless traits, Cairo provides the `#[generate_trait]` attribute to add above a trait implementation, which tells the compiler to generate the corresponding trait definition for you, and lets you focus on the implementation only. Both approaches are equivalent, but it's considered a best practice to not explicitly define traits in this case.

The previous example can also be written as follows:

```cairo
#[derive(Copy, Drop)]
struct Rectangle {
    width: u64,
    height: u64,
}

#[generate_trait]
impl RectangleImpl of RectangleTrait {
    fn area(self: @Rectangle) -> u64 {
        (*self.width) * (*self.height)
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    println!("Area is {}", rect1.area());
}

```

Let's use this `#[generate_trait]` in the following chapters to make our code cleaner.

## Snapshots and References

As the `area` method does not modify the calling instance, `self` is declared as a snapshot of a `Rectangle` instance with the `@` snapshot operator. But, of course, we can also define some methods receiving a mutable reference of this instance, to be able to modify it.

Let's write a new method `scale` which resizes a rectangle of a `factor` given as parameter:

```cairo
#[generate_trait]
impl RectangleImpl of RectangleTrait {
    fn area(self: @Rectangle) -> u64 {
        (*self.width) * (*self.height)
    }
    fn scale(ref self: Rectangle, factor: u64) {
        self.width *= factor;
        self.height *= factor;
    }
}

fn main() {
    let mut rect2 = Rectangle { width: 10, height: 20 };
    rect2.scale(2);
    println!("The new size is (width: {}, height: {})", rect2.width, rect2.height);
}
```

It is also possible to define a method which takes ownership of the instance by using just `self` as the first parameter but it is rare. This technique is usually used when the method transforms `self` into something else and you want to prevent the caller from using the original instance after the transformation.

Look at the [Understanding Ownership](ch04-00-understanding-ownership.md) chapter for more details about these important notions.

## Methods with Several Parameters

Let’s practice using methods by implementing another method on the `Rectangle` struct. This time we want to write the method `can_hold` which accepts another instance of `Rectangle` and returns `true` if this rectangle can fit completely within self; otherwise, it should return false.

```cairo
#[generate_trait]
impl RectangleImpl of RectangleTrait {
    fn area(self: @Rectangle) -> u64 {
        *self.width * *self.height
    }

    fn scale(ref self: Rectangle, factor: u64) {
        self.width *= factor;
        self.height *= factor;
    }

    fn can_hold(self: @Rectangle, other: @Rectangle) -> bool {
        *self.width > *other.width && *self.height > *other.height
    }
}

fn main() {
    let rect1 = Rectangle { width: 30, height: 50 };
    let rect2 = Rectangle { width: 10, height: 40 };
    let rect3 = Rectangle { width: 60, height: 45 };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(@rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(@rect3));
}
```

Here, we expect that `rect1` can hold `rect2` but not `rect3`.

## Associated functions

We call _associated functions_ all functions that are defined inside an `impl` block that are associated to a specific type. While this is not enforced by the compiler, it is a good practice to keep associated functions related to the same type in the same `impl` block - for example, all functions related to `Rectangle` will be grouped in the same `impl` block for `RectangleTrait`.

Methods are a special kind of associated function, but we can also define associated functions that don’t have `self` as their first parameter (and thus are not methods) because they don’t need an instance of the type to work with, but are still associated with that type.

Associated functions that aren’t methods are often used for constructors that
will return a new instance of the type. These are often called `new`, but
`new` isn’t a special name and isn’t built into the language. For example, we
could choose to provide an associated function named `square` that would have
one dimension parameter and use that as both width and height, thus making it
easier to create a square `Rectangle` rather than having to specify the same
value twice:

Let's create the function `new` which creates a `Rectangle` from a `width` and a `height`, `square` which creates a square `Rectangle` from a `size` and `avg` which computes the average of two `Rectangle` instances:

```cairo
#[generate_trait]
impl RectangleImpl of RectangleTrait {
    fn area(self: @Rectangle) -> u64 {
        (*self.width) * (*self.height)
    }

    fn new(width: u64, height: u64) -> Rectangle {
        Rectangle { width, height }
    }

    fn square(size: u64) -> Rectangle {
        Rectangle { width: size, height: size }
    }

    fn avg(lhs: @Rectangle, rhs: @Rectangle) -> Rectangle {
        Rectangle {
            width: ((*lhs.width) + (*rhs.width)) / 2, height: ((*lhs.height) + (*rhs.height)) / 2,
        }
    }
}

fn main() {
    let rect1 = RectangleTrait::new(30, 50);
    let rect2 = RectangleTrait::square(10);

    println!(
        "The average Rectangle of {:?} and {:?} is {:?}",
        @rect1,
        @rect2,
        RectangleTrait::avg(@rect1, @rect2),
    );
}
```

To call the `square` associated function, we use the `::` syntax with the struct name;
`let sq = RectangleTrait::square(3);` is an example. This function is namespaced by
the trait: the `::` syntax is used for both associated functions and
namespaces created by modules. We’ll discuss modules in [Chapter
7][modules].

Note that the `avg` function could also be written as a method with `self` as the first rectangle. In this case, instead of using the method with `RectangleTrait::avg(@rect1, @rect2)`, it would be called with `rect1.avg(rect2)`.

## Multiple Traits and `impl` Blocks

Each struct is allowed to have multiple `trait` and `impl` blocks. For example,
the following code is equivalent to the code shown in the _Methods with several parameters_ section, which has each method in its own `trait` and `impl` blocks.

```cairo
#[generate_trait]
impl RectangleCalcImpl of RectangleCalc {
    fn area(self: @Rectangle) -> u64 {
        (*self.width) * (*self.height)
    }
}

#[generate_trait]
impl RectangleCmpImpl of RectangleCmp {
    fn can_hold(self: @Rectangle, other: @Rectangle) -> bool {
        *self.width > *other.width && *self.height > *other.height
    }
}
```

There’s no strong reason to separate these methods into multiple `trait` and `impl`
blocks here, but this is valid syntax.

<div class="quiz-placeholder" data-quiz-name="&quot;ch05-03-method-syntax&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;It compiles, because the type `Rectangle` on which we call the method on reference is implicitly passed as a `@Rectangle`\n&quot;,&quot;id&quot;:&quot;98bbc25c-80b2-4226-9219-a8d7b20fb991&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:true,&quot;stdout&quot;:&quot;false&quot;},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Copy, Drop)]\nstruct Rectangle {\n    width: u64,\n    height: u64,\n}\n\n#[generate_trait]\nimpl RectangleImpl of RectangleTrait {\n    fn area(self: @Rectangle) -&gt; u64 {\n        (*self.width) * (*self.height)\n    }\n    fn new(width: u64, height: u64) -&gt; Rectangle {\n        Rectangle { width, height }\n    }\n    fn compare_areas(self: @Rectangle, r2: @Rectangle) -&gt; bool {\n        self.area() == r2.area()\n    }\n}\n\nfn main() {\n    let rect1 = Rectangle {width: 40, height: 50};\n    let rect2 = RectangleTrait::new(10, 40);\n    println!(\&quot;{}\&quot;, rect1.compare_areas(@rect2));\n}\n&quot;}},{&quot;context&quot;:&quot;Methods can only be called on the types they're defined for; here, we try to call `area()` on `Circle`, when it's defined for `Rectangle`.\n&quot;,&quot;id&quot;:&quot;1e4a5bff-dc92-4c09-9f04-1d95fcf039bb&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false,&quot;lineNumber&quot;:25},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Drop)]\nstruct Rectangle {\n    width: u64,\n    height: u64,\n}\n\n#[derive(Drop)]\nstruct Circle {\n    radius: u64,\n}\n\ntrait RectangleTrait {\n    fn area(self: @Rectangle) -&gt; u64;\n}\n\nimpl RectangleImpl of RectangleTrait {\n    fn area(self: @Rectangle) -&gt; u64 {\n        return (*self.width) * (*self.height);\n    }\n}\n\nfn main() {\n    let my_square = Rectangle { width: 30, height: 50 };\n    let my_circle = Circle { radius: 10 };\n    let area = my_circle.area();\n    println!(\&quot;{}\&quot;, area)\n}\n\n&quot;}}]}"></div>

[enums]: ./ch06-01-enums.md
[modules]: ./ch07-02-defining-modules-to-control-scope.md


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Enums and Pattern Matching

In this chapter, we’ll look at _enumerations_, also referred to as _enums_.
Enums allow you to define a type by enumerating its possible _variants_. First,
we’ll define and use an enum to show how an enum can encode meaning along with
data. Next, we’ll explore a particularly useful enum, called `Option`, which
expresses that a value can be either something or nothing. Finally, we’ll look at
how pattern matching in the `match` expression makes it easy to run different
code for different values of an enum.
# Enums

Enums, short for "enumerations," are a way to define a custom data type that consists of a fixed set of named values, called _variants_. Enums are useful for representing a collection of related values where each value is distinct and has a specific meaning.

## Enum Variants and Values

Here's a simple example of an enum:

```cairo, noplayground
#[derive(Drop)]
enum Direction {
    North,
    East,
    South,
    West,
}
```

In this example, we've defined an enum called `Direction` with four variants: `North`, `East`, `South`, and `West`. The naming convention is to use PascalCase for enum variants. Each variant represents a distinct value of the `Direction` type. In this particular example, variants don't have any associated value. One variant can be instantiated using this syntax:

```cairo, noplayground
# #[derive(Drop)]
# enum Direction {
#     North,
#     East,
#     South,
#     West,
# }
#
# fn main() {
    let direction = Direction::North;
# }
#
```

Now let's imagine that our variants have associated values, that store the exact degree of the direction. We can define a new `Direction` enum:

```cairo, noplayground
#[derive(Drop)]
enum Direction {
    North: u128,
    East: u128,
    South: u128,
    West: u128,
}
#
# fn main() {
#     let direction = Direction::North(10);
# }
```

and instantiate it as follows:

```cairo, noplayground
# #[derive(Drop)]
# enum Direction {
#     North: u128,
#     East: u128,
#     South: u128,
#     West: u128,
# }
#
# fn main() {
    let direction = Direction::North(10);
# }
```

In this code, each variant is associated with a `u128` value, representing the direction in degrees. In the next example, we will see that it is also possible to associate different data types with each variant.

It's easy to write code that acts differently depending on the variant of an enum instance, in this example to run specific code according to a direction. You can learn more about it in the [Match Control Flow Construct][match] section.

[match]: ./ch06-02-the-match-control-flow-construct.md

## Enums Combined with Custom Types

Enums can also be used to store more interesting custom data associated with each variant. For example:

```cairo, noplayground
#[derive(Drop)]
enum Message {
    Quit,
    Echo: felt252,
    Move: (u128, u128),
}
```

In this example, the `Message` enum has three variants: `Quit`, `Echo`, and `Move`, all with different types:

- `Quit` doesn't have any associated value.
- `Echo` is a single `felt252`.
- `Move` is a tuple of two `u128` values.

You could even use a Struct or another enum you defined inside one of your enum variants.

## Trait Implementations for Enums

In Cairo, you can define traits and implement them for your custom enums. This allows you to define methods and behaviors associated with the enum. Here's an example of defining a trait and implementing it for the previous `Message` enum:

```cairo, noplayground
trait Processing {
    fn process(self: Message);
}

impl ProcessingImpl of Processing {
    fn process(self: Message) {
        match self {
            Message::Quit => { println!("quitting") },
            Message::Echo(value) => { println!("echoing {}", value) },
            Message::Move((x, y)) => { println!("moving from {} to {}", x, y) },
        }
    }
}
```

In this example, we implemented the `Processing` trait for `Message`. Here is how it could be used to process a `Quit` message:

```cairo
#
# #[derive(Drop)]
# enum Message {
#     Quit,
#     Echo: felt252,
#     Move: (u128, u128),
# }
#
# trait Processing {
#     fn process(self: Message);
# }
#
# impl ProcessingImpl of Processing {
#     fn process(self: Message) {
#         match self {
#             Message::Quit => { println!("quitting") },
#             Message::Echo(value) => { println!("echoing {}", value) },
#             Message::Move((x, y)) => { println!("moving from {} to {}", x, y) },
#         }
#     }
# }
# fn main() {
    let msg: Message = Message::Quit;
    msg.process(); // prints "quitting"
# }
#
#
```

## The `Option` Enum and Its Advantages

The `Option` enum is a standard Cairo enum that represents the concept of an optional value. It has two variants: `Some: T` and `None`. `Some: T` indicates that there's a value of type `T`, while `None` represents the absence of a value.

```cairo,noplayground
enum Option<T> {
    Some: T,
    None,
}
```

The `Option` enum is helpful because it allows you to explicitly represent the possibility of a value being absent, making your code more expressive and easier to reason about. Using `Option` can also help prevent bugs caused by using uninitialized or unexpected `null` values.

To give you an example, here is a function which returns the index of the first element of an array with a given value, or `None` if the element is not present.

We are demonstrating two approaches for the above function:

- Recursive approach with `find_value_recursive`.
- Iterative approach with `find_value_iterative`.

```cairo,noplayground
fn find_value_recursive(mut arr: Span<felt252>, value: felt252, index: usize) -> Option<usize> {
    match arr.pop_front() {
        Some(index_value) => { if (*index_value == value) {
            return Some(index);
        } },
        None => { return None; },
    };

    find_value_recursive(arr, value, index + 1)
}

fn find_value_iterative(mut arr: Span<felt252>, value: felt252) -> Option<usize> {
    let mut result = None;
    let mut index = 0;

    while let Some(array_value) = arr.pop_front() {
        if (*array_value == value) {
            result = Some(index);
            break;
        };

        index += 1;
    };

    result
}
```

Enums can be useful in many situations, especially when using the `match` flow construct that we just used. We will describe it in the next section.

Other enums are used very often, such as the `Result` enum, allowing to handle errors gracefully. We will explain the `Result` enum in detail in the ["Error Handling"][result enum] chapter.

<div class="quiz-placeholder" data-quiz-name="&quot;ch06-01-enums&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;Cairo does not have null pointers, so the `null` keyword does not exist. \nAn `Option` type should be used to represent the possibility of an object being null.\n&quot;,&quot;id&quot;:&quot;8b786183-ef9f-43f8-89a6-0e9c0e87c576&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn main() {\n    let x = null;\n    foo(x);\n}\n\nfn foo(x:u8) {\n    println!(\&quot;{}\&quot;, x);\n}\n&quot;}},{&quot;context&quot;:&quot;It's perfectly fine to have structs contain `Option` types as fields (the question asked for a statement which does **NOT** describe a valid reason). But if your data structure has invariants like \&quot;exactly one of two optional fields should be `Some`\&quot;, then that invariant is better ensured by the use of an enum.\n&quot;,&quot;id&quot;:&quot;0d9b6f65-bfac-447f-a2d4-a650abc8bc01&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;The struct contains `Option` types, which are only intended to wrap structs&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;The struct is more syntactically verbose to construct than the enum&quot;,&quot;The struct uses more space in memory at runtime than the enum&quot;,&quot;The struct could have `ok` and `err` both be `None`, while the enum must have at least one of them&quot;],&quot;prompt&quot;:&quot;Consider these two representations of a `Result` type that contains a value `T` if a computation succeeds, or an error `E` if it fails.\n```\nstruct Result1&lt;T, E&gt; {\n    ok: Option&lt;T&gt;,\n    err: Option&lt;E&gt;,\n}\n  \nenum Result2&lt;T, E&gt; {\n    Ok : T,\n    Err : E,\n}\n```\nThe enum `Result2` is considered more idiomatic than the struct `Result1` in Cairo. Which statement below is **NOT** a valid reason why?\n&quot;}}]}"></div>

[result enum]: ./ch09-02-recoverable-errors.md#the-result-enum


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># The Match Control Flow Construct

Cairo has an extremely powerful control flow construct called `match` that allows you to compare a value against a series of patterns and then execute code based on which pattern matches. Patterns can be made up of literal values, variable names, wildcards, and many other things. The power of `match` comes from the expressiveness of the patterns and the fact that the compiler confirms that all possible cases are handled.

Think of a `match` expression as being like a coin-sorting machine: coins slide down a track with variously sized holes along it, and each coin falls through the first hole it encounters that it fits into. In the same way, values go through each pattern in a match, and at the first pattern the value “fits”, the value falls into the associated code block to be used during execution.

Speaking of coins, let’s use them as an example using `match`! We can write a function that takes an unknown US coin and, in a similar way as the counting machine, determines which coin it is and returns its value in cents, as shown in Listing 6-1.

```cairo,noplayground
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> felt252 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

<span class="caption">Listing 6-1: An enum and a `match` expression that has the variants of the enum as its patterns</span>

Let’s break down the `match` expression in the `value_in_cents` function. First, we list the `match` keyword followed by an expression, which in this case is the value `coin`. This seems very similar to a conditional expression used with the `if` statement, but there’s a big difference: with `if`, the condition needs to evaluate to a boolean value, but here it can be any type. The type of `coin` in this example is the `Coin` enum that we defined on the first line.

Next are the `match` arms. An arm has two parts: a pattern and some code. The first arm here has a pattern that is the value `Coin::Penny` and then the `=>` operator that separates the pattern and the code to run. The code in this case is just the value `1`. Each arm is separated from the next with a comma.

When the `match` expression executes, it compares the resultant value against the pattern of each arm, in the order they are given. If a pattern matches the value, the code associated with that pattern is executed. If that pattern doesn’t match the value, execution continues to the next arm, much as in a coin-sorting machine. We can have as many arms as we need: in the above example, our `match` has four arms.

The code associated with each arm is an expression, and the resultant value of the expression in the matching arm is the value that gets returned for the entire match expression.

We don’t typically use curly brackets if the `match` arm code is short, as it is in our example where each arm just returns a value. If you want to run multiple lines of code in a `match` arm, you must use curly brackets, with a comma following the arm. For example, the following code prints “Lucky penny!” every time the method is called with a `Coin::Penny`, but still returns the last value of the block, `1`:

```cairo,noplayground
fn value_in_cents(coin: Coin) -> felt252 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        },
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

## Patterns That Bind to Values

Another useful feature of `match` arms is that they can bind to the parts of the values that match the pattern. This is how we can extract values out of enum variants.

As an example, let’s change one of our enum variants to hold data inside it. From 1999 through 2008, the United States minted quarters with different designs for each of the 50 states on one side. No other coins got state designs, so only quarters have this extra value. We can add this information to our `enum` by changing the `Quarter` variant to include a `UsState` value stored inside it, which we’ve done in Listing 6-2.

```cairo,noplayground

#[derive(Drop, Debug)] // Debug so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
}

#[derive(Drop)]
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter: UsState,
}
```

<span class="caption">Listing 6-2: A `Coin` enum in which the `Quarter` variant also holds a `UsState` value</span>

Let’s imagine that a friend is trying to collect all 50 state quarters. While we sort our loose change by coin type, we’ll also call out the name of the state associated with each quarter so that if it’s one our friend doesn’t have, they can add it to their collection.

In the `match` expression for this code, we add a variable called `state` to the pattern that matches values of the variant `Coin::Quarter`. When a `Coin::Quarter` matches, the `state` variable will bind to the value of that quarter’s state. Then we can use `state` in the code for that arm, like so:

```cairo,noplayground
fn value_in_cents(coin: Coin) -> felt252 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        },
    }
}
```

Because `state` is an `UsState` enum which implements the `Debug` trait, we can print `state` value with `println!` macro.

> Note: `{:?}` is a special formatting syntax that allows to print a debug form of the parameter passed to the `println!` macro. You can find more information about it in [Appendix C][debug trait].

If we were to call `value_in_cents(Coin::Quarter(UsState::Alaska))`, `coin` would be `Coin::Quarter(UsState::Alaska)`. When we compare that value with each of the match arms, none of them match until we reach `Coin::Quarter(state)`. At that point, the binding for `state` will be the value `UsState::Alaska`. We can then use that binding in `println!` macro, thus getting the inner state value out of the `Coin` enum variant for `Quarter`.

[debug trait]: ./appendix-03-derivable-traits.md#debug-for-printing-and-debugging

## Matching with `Option<T>`

In the previous section, we wanted to get the inner `T` value out of the `Some` case when using `Option<T>`; we can also handle `Option<T>` using `match`, as we did with the `Coin` enum! Instead of comparing coins, we’ll compare the variants of `Option<T>`, but the way the `match` expression works remains the same.

Let’s say we want to write a function that takes an `Option<u8>` and, if there’s a value inside, adds `1` to that value. If there is no value inside, the function should return the `None` value and not attempt to perform any operations.

This function is very easy to write, thanks to `match`, and will look like Listing 6-3.

```cairo
fn plus_one(x: Option<u8>) -> Option<u8> {
    match x {
        Some(val) => Some(val + 1),
        None => None,
    }
}

fn main() {
    let five: Option<u8> = Some(5);
    let six: Option<u8> = plus_one(five);
    let none = plus_one(None);
}
```

<span class="caption">Listing 6-3: A function that uses a `match` expression on an `Option<u8>`</span>

Let’s examine the first execution of `plus_one` in more detail. When we call `plus_one(five)`, the variable `x` in the body of `plus_one` will have the value `Some(5)`. We then compare that against each `match` arm:

```cairo,noplayground
        Some(val) => Some(val + 1),
```

Does `Some(5)` value match the pattern `Some(val)`? It does! We have the same variant. The `val` binds to the value contained in `Some`, so `val` takes the value `5`. The code in the `match` arm is then executed, so we add `1` to the value of `val` and create a new `Some` value with our total `6` inside. Because the first arm matched, no other arms are compared.

Now let’s consider the second call of `plus_one` in our main function, where `x` is `None`. We enter the `match` and compare to the first arm:

```cairo,noplayground
        Some(val) => Some(val + 1),
```

The `Some(val)` value doesn’t match the pattern `None`, so we continue to the next arm:

```cairo
        None => None,
```

It matches! There’s no value to add to, so the matching construct ends and returns the `None` value on the right side of `=>`.

Combining `match` and enums is useful in many situations. You’ll see this pattern a lot in Cairo code: `match` against an enum, bind a variable to the data inside, and then execute code based on it. It’s a bit tricky at first, but once you get used to it, you’ll wish you had it in all languages. It’s consistently a user favorite.

## Matches Are Exhaustive

There’s one other aspect of `match` we need to discuss: the arms’ patterns must cover all possibilities. Consider this version of our `plus_one` function, which has a bug and won’t compile:

```cairo,noplayground
fn plus_one(x: Option<u8>) -> Option<u8> {
    match x {
        Some(val) => Some(val + 1),
    }
}
```

We didn’t handle the `None` case, so this code will cause a bug.
Luckily, it’s a bug Cairo knows how to catch. If we try to compile this code, we’ll get this error:

```shell
$ scarb execute
   Compiling no_listing_08_missing_match_arm v0.1.0 (listings/ch06-enums-and-pattern-matching/no_listing_09_missing_match_arm/Scarb.toml)
error: Missing match arm: `None` not covered.
 --> listings/ch06-enums-and-pattern-matching/no_listing_09_missing_match_arm/src/lib.cairo:5:5
    match x {
    ^*******^

error: could not compile `no_listing_08_missing_match_arm` due to previous error
error: `scarb metadata` exited with error

```

Cairo knows that we didn’t cover every possible case, and even knows which pattern we forgot! Matches in Cairo are exhaustive: we must exhaust every last possibility in order for the code to be valid. Especially in the case of `Option<T>`, when Cairo prevents us from forgetting to explicitly handle the `None` case, it protects us from assuming that we have a value when we might have null, thus making the [billion-dollar mistake][null pointer] discussed earlier impossible.

[null pointer]: https://en.wikipedia.org/wiki/Null_pointer#History

## Catch-all with the `_` Placeholder

Using enums, we can also take special actions for a few particular values, but for all other values take one default action.
`_` is a special pattern that matches any value and does not bind to that value.
You can use it by simply adding a new arm with `_` as the pattern for the last arm of the `match` expression.

Imagine we have a vending machine that only accepts Dime coins.
We want to have a function that processes inserted coins and returns `true` only if the coin is accepted.

Here's a `vending_machine_accept` function that implements this logic:

```cairo,noplayground
fn vending_machine_accept(coin: Coin) -> bool {
    match coin {
        Coin::Dime => true,
        _ => false,
    }
}
```

This example also meets the exhaustiveness requirement because we’re explicitly ignoring all other values in the last arm; we haven’t forgotten anything.

> There's no catch-all pattern in Cairo that allows you to use the value of the pattern.

<!--
  TODO move the following in a separate chapter when there's more pattern matching features in upcoming Cairo versions. cf rust book chapter 18
-->

## Multiple Patterns with the `|` Operator

In `match` expressions, you can match multiple patterns using the `|` syntax, which is the pattern _or_ operator.

For example, in the following code we modified the `vending_machine_accept` function to accept both `Dime` and `Quarter` coins in a single arm:

```cairo,noplayground
fn vending_machine_accept(coin: Coin) -> bool {
    match coin {
        Coin::Dime | Coin::Quarter => true,
        _ => false,
    }
}
```

## Matching Tuples

It is possible to match tuples.
Let's introduce a new `DayType` enum:

```cairo,noplayground
#[derive(Drop)]
enum DayType {
    Week,
    Weekend,
    Holiday,
}
```

Now, let's suppose that our vending machine accepts any coin on weekdays, but only accepts quarters and dimes on weekends and holidays.
We can modify the `vending_machine_accept` function to accept a tuple of a `Coin` and a `Weekday` and return `true` only if the given coin is accepted on the specified day:

```cairo,noplayground
fn vending_machine_accept(c: (DayType, Coin)) -> bool {
    match c {
        (DayType::Week, _) => true,
        (_, Coin::Dime) | (_, Coin::Quarter) => true,
        (_, _) => false,
    }
}
```

Writing `(_, _)` for the last arm of a tuple matching pattern might feel superfluous. Hence, we can use the `_ =>` syntax if we want, for example, that our vending machine only accepts quarters on weekdays:

```cairo,noplayground
fn vending_week_machine(c: (DayType, Coin)) -> bool {
    match c {
        (DayType::Week, Coin::Quarter) => true,
        _ => false,
    }
}
```

## Matching `felt252` and Integer Variables

You can also match `felt252` and integer variables. This is useful when you want to match against a range of values.
However, there are some restrictions:

- Only integers that fit into a single `felt252` are supported (i.e. `u256` is not supported).
- The first arm must be 0.
- Each arm must cover a sequential segment, contiguously with other arms.

Imagine we’re implementing a game where you roll a six-sided die to get a number between 0 and 5.
If you have 0, 1 or 2 you win. If you have 3, you can roll again. For all other values you lose.

Here's a match that implements that logic:

```cairo,noplayground
fn roll(value: u8) {
    match value {
        0 | 1 | 2 => println!("you won!"),
        3 => println!("you can roll again!"),
        _ => println!("you lost..."),
    }
}
```

<div class="quiz-placeholder" data-quiz-name="&quot;ch06-02-match&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;Cairo does not support matching for tuples whose members are not enums yet.\nAs `u32` is not an enum, the matching of `r` can't be done.\n&quot;,&quot;id&quot;:&quot;b0621230-c040-4f30-b658-14d31f4fab82&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Copy, Drop)]\nenum Location {\n    Point : u32,\n    Range : (u32, u32)\n}\n\nfn main() {\n    let loc: Location = Location::Range((2, 5));\n    let n: u32 = match loc {\n        Location::Point(p) =&gt; p,\n        Location::Range(r) =&gt; match r {\n            (0, _) =&gt; 0,\n            (_, n) =&gt; n,\n            _ =&gt; 404\n        },\n        _ =&gt; 403\n    };\n    println!(\&quot;{}\&quot;, n);\n}\n&quot;}},{&quot;context&quot;:&quot;The first match arm `Either::Right(s)` moves the field `s`, so `x` cannot be used in the second match.\n&quot;,&quot;id&quot;:&quot;b0147849-6c36-46a5-b933-51289913a621&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;#[derive(Drop)]\nenum Either {\n    Left: u32,\n    Right: ByteArray\n}\n\nfn main() {\n    let x = Either::Right(\&quot;Hello World\&quot;);\n    let simple = match x {\n      Either::Left(n) =&gt; n,\n      Either::Right(s) =&gt; s.len()\n    };\n    let doubled = match x {\n      Either::Left(n) =&gt; n * 2,\n      Either::Right(s) =&gt; s.len() * 2\n    };\n    println!(\&quot;doubled: {}\&quot;, doubled);\n}\n&quot;}},{&quot;context&quot;:&quot;There's no catch-all pattern in Cairo that allows you to use the value of the pattern.\nYou have to use the placeholder `_` instead.\n&quot;,&quot;id&quot;:&quot;bb07c951-7f3d-4225-ae54-adff59774b76&quot;,&quot;type&quot;:&quot;Tracing&quot;,&quot;answer&quot;:{&quot;doesCompile&quot;:false},&quot;prompt&quot;:{&quot;program&quot;:&quot;fn decr_twice(n: u32) -&gt; Option&lt;u32&gt; {\n    match n {\n        0 | 1 =&gt; None,\n        val =&gt; Some(val - 2)\n    }\n}\n&quot;}},{&quot;context&quot;:&quot;This function \&quot;unwraps\&quot; the option by consuming ownership of it and retrieving the value inside, but if no value exists then it falls back by returning `default`. This is a real function in the core library!\n&quot;,&quot;id&quot;:&quot;72e6696d-379e-4440-af15-803b7255bc80&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;Returns the object inside `self` if it exists, and `default` otherwise&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;Returns a reference to the object inside `self` if it exists, and `default` otherwise&quot;,&quot;Returns a new option containing the object inside `self` if it exists, and `default` otherwise&quot;,&quot;Inserts `default` into `self` if `self` does not already contain a value&quot;],&quot;prompt&quot;:&quot;Consider this method implemented for the `Option` type:\n```\nfn unwrap_or&lt;+Drop&lt;T&gt;&gt;(self: Option&lt;T&gt;, default: T) -&gt; T {\n    match self {\n        Some(x) =&gt; x,\n        None =&gt; default,\n    }\n}\n```\nWhich sentence best describes the behavior of this function?\n&quot;}},{&quot;context&quot;:&quot;The `match` and `if` perform the same operation here. A `match` is like a specialized `if` that checks for equality of the matched object.\n&quot;,&quot;id&quot;:&quot;e07e8e36-2c53-4b30-8040-091c3d4f2fd1&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;All inputs&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;Some, but not all inputs&quot;,&quot;No inputs&quot;],&quot;prompt&quot;:&quot;Consider these two implementations of a function to decrement an unsigned number twice.\n```\nfn decr_twice_v1(n: u32) -&gt; Option&lt;u32&gt; {\n    match n {\n        0 | 1 =&gt; None,\n        _ =&gt; Some(n - 2)\n    }\n}\n\nfn decr_twice_v2(n: u32) -&gt; Option&lt;u32&gt; {\n    if n == 0 {\n        None\n    } else if n == 1 {\n        None\n    } else {\n        Some(n - 2)\n    }\n}\n```\nThe functions have the same behavior for:\n&quot;}}]}"></div>

> These restrictions are planned to be relaxed in future versions of Cairo.


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Concise Control Flow with `if let` and `while let`

## `if let`

The `if let` syntax lets you combine `if` and `let` into a less verbose way to handle values that match one pattern while ignoring the rest. Consider the program in Listing 6-4 that matches on an `Some<u8>` value in the `config_max` variable but only wants to execute code if the value is `Some` variant.

```cairo
# fn main() {
    let config_max = Some(5);
    match config_max {
        Some(max) => println!("The maximum is configured to be {}", max),
        _ => (),
    }
# }
```

<span class="caption">Listing 6-4: A `match` that only cares about executing
code when the value is `Some`</span>

If the value is `Some`, we print out the value in the `Some` variant by binding
the value to the variable `max` in the pattern. We don’t want to do anything
with the `None` value. To satisfy the `match` expression, we have to add `_ =>
()` after processing just one variant, which is annoying boilerplate code to
add.

Instead, we could write this in a shorter way using `if let`. The following
code behaves the same as the `match` in Listing 6-4:

```cairo
# fn main() {
    let number = Some(5);
    if let Some(max) = number {
        println!("The maximum is configured to be {}", max);
    }
# }
```

The syntax `if let` takes a pattern and an expression separated by an equal
sign. It works the same way as a `match`, where the expression is given to the
`match` and the pattern is its first arm. In this case, the pattern is
`Some(max)`, and `max` binds to the value inside `Some`. We can then
use `max` in the body of the `if let` block in the same way we used `max` in
the corresponding `match` arm. The code in the `if let` block isn’t run if the
value doesn’t match the pattern.

Using `if let` means less typing, less indentation, and less boilerplate code.
However, you lose the exhaustive checking that `match` enforces. Choosing
between `match` and `if let` depends on what you’re doing in your particular
situation and whether gaining conciseness is an appropriate trade-off for
losing exhaustive checking.

In other words, you can think of `if let` as syntactic sugar for a `match` that
runs code when the value matches one pattern and then ignores all other values.

We can include an `else` with an `if let`. The block of code that goes with `else`
is the same as the block of code that would go with the `_` case in the `match`
expression. Recall the `Coin` enum definition in Listing 6-2,
where the `Quarter` variant also held a `UsState` value. If we wanted to count
all non-quarter coins we see while also announcing the state of the quarters,
we could do that with a `match` expression, like this:

```cairo
# #[derive(Drop)]
# enum Coin {
#     Penny,
#     Nickel,
#     Dime,
#     Quarter,
# }
#
# fn main() {
    let coin = Coin::Quarter;
    let mut count = 0;
    match coin {
        Coin::Quarter => println!("You got a quarter!"),
        _ => count += 1,
    }
# }
```

Or we could use an `if let` and `else` expression, like this:

```cairo
# #[derive(Drop)]
# enum Coin {
#     Penny,
#     Nickel,
#     Dime,
#     Quarter,
# }
#
# fn main() {
    let coin = Coin::Quarter;
    let mut count = 0;
    if let Coin::Quarter = coin {
        println!("You got a quarter!");
    } else {
        count += 1;
    }
#     println!("{}", count);
# }
#
```

If you have a situation in which your program has logic that is too verbose to
express using `match`, remember that `if let` is in your Cairo toolbox as well.

## `while let`

The `while let` syntax is similar to the `if let` syntax, but it allows you to loop over a collection of values and execute a block of code for each value that matches a specified pattern. In the case below, the pattern is `Some(x)`, which matches any `Some` variant of the `Option` enum.

```cairo
fn main() {
    let mut arr = array![1, 2, 3, 4, 5, 6, 7, 8, 9];
    let mut sum = 0;
    while let Some(value) = arr.pop_front() {
        sum += value;
    }
    println!("{}", sum);
}
```

Using `while let` provides a more concise and idiomatic way of writing this loop compared to a traditional `while` loop with explicit pattern matching or handling of the `Option` type. However, as with `if let`, you lose the exhaustive checking that a `match` expression provides, so you need to be careful to handle any remaining cases outside the `while let` loop if necessary.
# Managing Cairo Projects with Packages, Crates and Modules

As you write large programs, organizing your code will become increasingly
important. By grouping related functionality and separating code with distinct
features, you’ll clarify where to find code that implements a particular
feature and where to go to change how a feature works.

The programs we’ve written so far have been in one module in one file. As a
project grows, you should organize code by splitting it into multiple modules
and then multiple files. As a package grows, you can extract parts into
separate crates that become external dependencies. This chapter covers all
these techniques.

We’ll also discuss encapsulating implementation details, which lets you reuse
code at a higher level: once you’ve implemented an operation, other code can
call your code without having to know how the
implementation works.

A related concept is scope: the nested context in which code is written has a
set of names that are defined as “in scope”. When reading, writing, and
compiling code, programmers and compilers need to know whether a particular
name at a particular spot refers to a variable, function, struct, enum, module,
constant, or other item and what that item means. You can create scopes and
change which names are in or out of scope. You can’t have two items with the
same name in the same scope.

Cairo has a number of features that allow you to manage your code’s
organization. These features, sometimes
collectively referred to as the _module system_, include:

- **Packages:** A Scarb feature that lets you build, test, and share crates.
- **Crates:** A tree of modules that corresponds to a single compilation unit.
  It has a root directory, and a root module defined at the _lib.cairo_ file under this directory.
- **Modules** and **use:** Let you control the organization and scope of items.
- **Paths:** A way of naming an item, such as a struct, function, or module.

In this chapter, we’ll cover all these features, discuss how they interact, and
explain how to use them to manage scope. By the end, you should have a solid
understanding of the module system and be able to work with scopes like a pro!
# Packages and Crates

## What is a Crate?

A crate is a subset of a package that is used in the actual Cairo compilation. This includes:

- The package source code, identified by the package name and the crate root, which is the main entry point of the package.
- A subset of the package metadata that identifies crate-level settings of the Cairo compiler, for example, the `edition` field in the _Scarb.toml_ file.

Crates can contain modules, and the modules may be defined in other files that get compiled with the crate, as will be discussed in the subsequent sections.

## What is the Crate Root?

The crate root is the _lib.cairo_ source file that the Cairo compiler starts from and makes up the root module of your crate. We’ll explain modules in depth in the ["Defining Modules to Control Scope"][modules] chapter.

[modules]: ./ch07-02-defining-modules-to-control-scope.md

## What is a Package?

A Cairo package is a directory (or equivalent) containing:

- A _Scarb.toml_ manifest file with a `[package]` section.
- Associated source code.

This definition implies that a package might contain other packages, with a corresponding _Scarb.toml_ file for each package.

## Creating a Package with Scarb

You can create a new Cairo package using the Scarb command-line tool. To create a new package, run the following command:

```bash
scarb new my_package
```

This command will generate a new package directory named _my_package_ with the following structure:

```
my_package/
├── Scarb.toml
└── src
    └── lib.cairo
```

- _src/_ is the main directory where all the Cairo source files for the package will be stored.
- _lib.cairo_ is the default root module of the crate, which is also the main entry point of the package.
- _Scarb.toml_ is the package manifest file, which contains metadata and configuration options for the package, such as dependencies, package name, version, and authors. You can find documentation about it on the [Scarb reference][manifest].

```toml
[package]
name = "my_package"
version = "0.1.0"
edition = "2024_07"

[executable]

[cairo]
enable-gas = false

[dependencies]
cairo_execute = "2.11.4"
```

As you develop your package, you may want to organize your code into multiple Cairo source files. You can do this by creating additional _.cairo_ files within the _src_ directory or its subdirectories.

<div class="quiz-placeholder" data-quiz-name="&quot;ch07-01-packages-crates&quot;" data-quiz-questions="{&quot;questions&quot;:[{&quot;context&quot;:&quot;A package is the top-level organizational unit, containing crates. A crate contains modules.\n&quot;,&quot;id&quot;:&quot;340f3191-f990-4a3d-89ab-7c98ac6ae0e3&quot;,&quot;type&quot;:&quot;MultipleChoice&quot;,&quot;answer&quot;:{&quot;answer&quot;:&quot;package &gt; crate &gt; module&quot;},&quot;prompt&quot;:{&quot;distractors&quot;:[&quot;crate &gt; package &gt; module&quot;,&quot;crate &gt; module &gt; package&quot;,&quot;package &gt; module &gt; crate&quot;],&quot;prompt&quot;:&quot;Which is the correct order, where \&quot;A &gt; B\&quot; means \&quot;A contains B\&quot;?\n&quot;}}]}"></div>

[manifest]: https://docs.swmansion.com/scarb/docs/reference/manifest.html


<script type="text/javascript" src="quiz-cairo/quiz-embed.iife.js"></script><link rel="stylesheet" type="text/css" href="quiz-cairo/style.css"># Defining Modules to Control Scope

In this section, we’ll talk about modules and other parts of the module system,
namely _paths_ that allow you to name items and the `use` keyword that brings a
path into scope.

First, we’re going to start with a list of rules for easy reference when you’re
organizing your code in the future. Then we’ll explain each of the rules in
detail.

## Modules Cheat Sheet

Here we provide a quick reference on how modules, paths and the `use` keyword
work in the compiler, and how most developers organize their
code. We’ll be going through examples of each of these rules throughout this
chapter, but this is a great place to refer to as a reminder of how modules
work. You can create a new Scarb project with `scarb new backyard` to follow along.

- **Start from the crate root**: When compiling a crate, the compiler first
  looks in the crate root file (_src/lib.cairo_) for code to compile.
- **Declaring modules**: In the crate root file, you can declare new modules;
  say, you declare a “garden” module with `mod garden;`. The compiler will look
  for the module’s code in these places:

  - Inline, within curly brackets that replace the semicolon following `mod garden`.

    ```cairo,noplayground
      // crate root file (src/lib.cairo)
      mod garden {
          // code defining the garden module goes here
      }
    ```

  - In the file _src/garden.cairo_.

- **Declaring submodules**: In any file other than the crate root, you can
  declare submodules. For example, you might declare `mod vegetables;` in
  _src/garden.cairo_. The compiler will look for the submodule’s code within the
  directory named for the parent module in these places:

  - Inline, directly following `mod vegetables`, within curly brackets instead
    of the semicolon.

    ```cairo,noplayground
    // src/garden.cairo file
    mod vegetables {
        // code defining the vegetables submodule goes here
    }
    ```

  - In the file _src/garden/vegetables.cairo_.

- **Paths to code in modules**: Once a module is part of your crate, you can
  refer to code in that module from anywhere else in that same crate, using the path
  to the code. For example, an `Asparagus` type in the `vegetables` submodule would be found at
  `crate::garden::vegetables::Asparagus`.
- **Private vs public**: Code within a module is private from its parent modules by default. This means that it may only be
  accessed by the current module and its descendants. To make a module public, declare it with `pub mod` instead of `mod`. To make items within a public module public as well, use `pub` before their declarations. Cairo also provides the `pub(crate)` keyword, allowing an item or module to be only visible within the crate in which the definition is included.
- **The `use` keyword**: Within a scope, the `use` keyword creates shortcuts to
  items to reduce repetition of long paths. In any scope that can refer to
  `crate::garden::vegetables::Asparagus`, you can create a shortcut with
  `use crate::garden::vegetables::Asparagus;` and from then on you only need to
  write `Asparagus` to make use of that type in the scope.

Here we create a crate named `backyard` that illustrates these rules. The
crate’s directory, also named `backyard`, contains these files and directories:

```text
backyard/
├── Scarb.toml
└── src
    ├── garden
    │   └── vegetables.cairo
    ├── garden.cairo
    └── lib.cairo
```

The crate root file in this case is _src/lib.cairo_, and it contains:

<span class="filename">Filename: src/lib.cairo</span>

```cairo
pub mod garden;
use crate::garden::vegetables::Asparagus;

fn main() {
    let plant = Asparagus {};
    println!("I'm growing {:?}!", plant);
}
```

The `pub mod garden;` line imports the `garden` module. Using `pub` to make `garden` publicly accessible, or `pub(crate)` if you really want to make `garden` only available for your crate, is optional to run our program here, as the `main` function resides in the same module as `pub mod garden;` declaration. Nevertheless, not declaring `garden` as `pub` will make it not accessible from any other package.
This line tells the compiler to include the code it finds in _src/garden.cairo_, which is:

<span class="filename">Filename: src/garden.cairo</span>

```cairo,noplayground
pub mod vegetables;
```

Here, `pub mod vegetables;` means the code in *src/garden/vegetables.cairo* is included too. That code is:

```cairo,noplayground
#[derive(Drop, Debug)]
pub struct Asparagus {}
```

The line `use crate::garden::vegetables::Asparagus;` lets us bring the `Asparagus` type into scope,
so we can use it in the `main` function.

Now let’s get into the details of these rules and demonstrate them in action!

## Grouping Related Code in Modules

_Modules_ let us organize code within a crate for readability and easy reuse.
Modules also allow us to control the privacy of items, because code within a module
is private by default. Private items are internal implementation details not
available for outside use. We can choose to make modules and the items within
them public, which exposes them to allow external code to use and depend on them.

As an example, let’s write a library crate that provides the functionality of a
restaurant. We’ll define the signatures of functions but leave their bodies
empty to concentrate on the organization of the code, rather than the
implementation of a restaurant.

In the restaurant industry, some parts of a restaurant are referred to as
_front of house_ and others as _back of house_. Front of house is where
customers are; this encompasses where the hosts seat customers, servers take
orders and payment, and bartenders make drinks. Back of house is where the
chefs and cooks work in the kitchen, dishwashers clean up, and managers do
administrative work.

To structure our crate in this way, we can organize its functions into nested
modules. Create a new package named _restaurant_ by running `scarb new