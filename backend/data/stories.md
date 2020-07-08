## table booking story
* booking_enquiry
  - utter_askname
* name{"PERSON":"Habib"}
  - slot{"PERSON":"Habib"}
  - action_save_name
  - utter_askemail
* email_id{"email":"javed@yahoomail.com"}
  - slot{"email":"javed@yahoomail.com"}
  - action_save_email
  - utter_asktable_no
  - action_availabe_table
* table{"table":"10"}
  - slot{"PERSON":"Habib"}
  - slot{"email":"javed@yahoomail.com"}
  - slot{"table":"10"}
  - action_save_table

## table booking story 2
* greet
  - utter_greet_user
* booking_enquiry
  - utter_askname
* name{"PERSON":"Habib"}
  - slot{"PERSON":"Habib"}
  - action_save_name
  - utter_askemail
* email_id{"email":"javed@yahoomail.com"}
  - slot{"email":"javed@yahoomail.com"}
  - action_save_email
  - utter_asktable_no
  - action_availabe_table
* table{"table":"10"}
  - slot{"PERSON":"Habib"}
  - slot{"email":"javed@yahoomail.com"}
  - slot{"table":"10"}
  - action_save_table

## booking cancel path
* cancel_booking
  - utter_tellstatusnumber
* ref_no{"refno":"2e2a74"}
  - slot{"refno":"2e2a74"}
  - action_check_booking
* confirm_cancel{"cancl":"positive"}
  - slot{"cancl":"positive"}
  - action_cancel_booking

## booking cancel path 2
* greet
  - utter_greet_user
* cancel_booking
  - utter_tellstatusnumber
* ref_no{"refno":"2e2a74"}
  - slot{"refno":"2e2a74"}
  - action_check_booking
* confirm_cancel{"cancl":"positive"}
  - slot{"cancl":"positive"}
  - action_cancel_booking

## story path starter veg
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_veg{"veg": "veg"}
  - slot{"veg": "veg"}
  - action_save_veg
  - utter_food_veg
* vegitem{"cuisine": "Paneer"}
  - slot{"cuisine": "Paneer"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter veg 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_veg{"veg": "veg"}
  - slot{"veg": "veg"}
  - action_save_veg
  - utter_food_veg
* vegitem{"cuisine": "Paneer"}
  - slot{"cuisine": "Paneer"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order


## story path main veg
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_veg{"veg": "veg"}
  - slot{"veg": "veg"}
  - action_save_veg
  - utter_food_veg
* vegitem{"cuisine": "Paneer"}
  - slot{"cuisine": "Paneer"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main veg 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_veg{"veg": "veg"}
  - slot{"veg": "veg"}
  - action_save_veg
  - utter_food_veg
* vegitem{"cuisine": "Paneer"}
  - slot{"cuisine": "Paneer"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter nonveg
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_nonveg{"non_veg": "non_veg"}
  - slot{"non_veg": "non_veg"}
  - action_save_nonveg
  - utter_food_nonveg
* nonvegitem{"cuisine": "Butter Chicken"}
  - slot{"cuisine": "Butter Chicken"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter nonveg 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_nonveg{"non_veg": "non_veg"}
  - slot{"non_veg": "non_veg"}
  - action_save_nonveg
  - utter_food_nonveg
* nonvegitem{"cuisine": "Butter Chicken"}
  - slot{"cuisine": "Butter Chicken"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main nonveg
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_nonveg{"non_veg": "non_veg"}
  - slot{"non_veg": "non_veg"}
  - action_save_nonveg
  - utter_food_nonveg
* nonvegitem{"cuisine": "Butter Chicken"}
  - slot{"cuisine": "Butter Chicken"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main nonveg 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_nonveg{"non_veg": "non_veg"}
  - slot{"non_veg": "non_veg"}
  - action_save_nonveg
  - utter_food_nonveg
* nonvegitem{"cuisine": "Butter Chicken"}
  - slot{"cuisine": "Butter Chicken"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter bread
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_bread{"bread": "bread"}
  - slot{"bread": "bread"}
  - action_save_bread
  - utter_food_bread
* rooti{"cuisine": "Naan"}
  - slot{"cuisine": "Naan"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter bread 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_bread{"bread": "bread"}
  - slot{"bread": "bread"}
  - action_save_bread
  - utter_food_bread
* rooti{"cuisine": "Naan"}
  - slot{"cuisine": "Naan"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main bread
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_bread{"bread": "bread"}
  - slot{"bread": "bread"}
  - action_save_bread
  - utter_food_bread
* rooti{"cuisine": "Naan"}
  - slot{"cuisine": "Naan"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main bread 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_bread{"bread": "bread"}
  - slot{"bread": "bread"}
  - action_save_bread
  - utter_food_bread
* rooti{"cuisine": "Naan"}
  - slot{"cuisine": "Naan"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter desert
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_desert{"desserts": "desserts"}
  - slot{"desserts": "desserts"}
  - action_save_desserts
  - utter_food_desert
* sweet{"cuisine": "Kulfi"}
  - slot{"cuisine": "Kulfi"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path starter desert 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* starter
  - utter_starter_item
* starter_item{"starters": "Soup"}
  - slot{"starters": "Soup"}
  - action_starter_entry
  - utter_food_type
* food_desert{"desserts": "desserts"}
  - slot{"desserts": "desserts"}
  - action_save_desserts
  - utter_food_desert
* sweet{"cuisine": "Kulfi"}
  - slot{"cuisine": "Kulfi"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main desert
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_desert{"desserts": "desserts"}
  - slot{"desserts": "desserts"}
  - action_save_desserts
  - utter_food_desert
* sweet{"cuisine": "Kulfi"}
  - slot{"cuisine": "Kulfi"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order

## story path main desert 2
* greet
  - utter_greet_user
* hunger
  - utter_food_question
  - action_start_entry
* main_course
  - utter_food_type
* food_desert{"desserts": "desserts"}
  - slot{"desserts": "desserts"}
  - action_save_desserts
  - utter_food_desert
* sweet{"cuisine": "Kulfi"}
  - slot{"cuisine": "Kulfi"}
  - action_save_cuisine
  - utter_anythingelse
* order_continue{"contorder": "more order"}
  - slot{"contorder": "more order"}
  - action_check_more_order
