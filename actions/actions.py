# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import datetime
from rasa_sdk.events import UserUtteranceReverted
import secrets
import json
# class ActionGreetUser(Action):

#     def name(self) -> Text:
#         return "action_greet_user"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message("Hello Foodie! How may I  help you today? 😃")

#         return [UserUtteranceReverted()]



class ActionSaveNme(Action):
    #
    def name(self) -> Text:
        return "action_save_name"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        import datetime
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("testrasa").sheet1  # Open the spreadhseet
        # data = sheet.get_all_records()  # Get a list of all records
        date = str(datetime.date.today())
        time = datetime.datetime.now()
        hour = str(time.hour)
        minu = str(time.minute)
        to_save = [date, hour, minu]
        sheet.insert_row(to_save, 3)
        name = tracker.get_slot("PERSON")
        sheet.update_cell(3, 4, name)
        dispatcher.utter_message("Okay")

        return []


class ActionSaveEmail(Action):
    #
    def name(self) -> Text:
        return "action_save_email"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("testrasa").sheet1  # Open the spreadhseet
        # data = sheet.get_all_records()  # Get a list of all records

        email = tracker.get_slot("email")

        sheet.update_cell(3, 5, email)
        dispatcher.utter_message("Okay.")

        return []


class ActionAvailableTable(Action):
    #
    def name(self) -> Text:
        return "action_availabe_table"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        import datetime

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet = sheets.worksheet("Sheet2")
        date = str(datetime.date.today())
        cell = sheet.find(date)
        Row = cell.row
        Tables = sheet.row_values(Row)
        # val = sheet.cell(Row, Col).value
        # print(val)
        # print(sheet.row_values(Row))
        available_table = []
        for idx, table in enumerate(Tables):
            if table == 'Available':
                x = "Table" + str(idx)
                available_table.append(x)
        if available_table != []:

            # for idx, table in enumerate(available_table):
            #     print(idx)
            #     print(table)

            dispatcher.utter_message(', '.join(map(str, available_table)))
        else:
            dispatcher.utter_message("All table booked today")

        return []


class ActionSaveTable(Action):
    #
    def name(self) -> Text:
        return "action_save_table"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return["table"]

    @staticmethod
    def table_db() -> List[Text]:
        """Database of supported passanger"""

        return [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",

        ]

    def validate_table(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if value in self.table_db():

            return {"table": value}
        else:
            dispatcher.utter_message("Table Not in our list. kindly table 1-9 in availabe table. like 2")

            return {"table": None}

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("testrasa").sheet1  # Open the spreadhseet
        sheets = client.open("testrasa")
        sheet2 = sheets.worksheet("Sheet2")
        # data = sheet.get_all_records()  # Get a list of all records

        date = str(datetime.date.today())
        cell = sheet2.find(date)
        Row = cell.row
        Tables = sheet2.row_values(Row)
        # val = sheet.cell(Row, Col).value
        # print(val)
        # print(sheet.row_values(Row))


        z = int(tracker.get_slot("table"))
        Col=z+1
        # print(z)
        # print(type(z))
        available_table = []
        for idx, table in enumerate(Tables):
            if table == 'Available':
                x = idx
                available_table.append(x)

        if z in available_table:

            table = tracker.get_slot("table")
            x = "Table" + str(table)
            sheet.update_cell(3, 8, x)
            sheet2.update_cell(Row, Col, "Booked")
            refNo = secrets.token_hex(3)
            sheet.update_cell(3, 7, refNo)
            sheet.update_cell(3, 6, "Confirmed")
            message = f"Okay.your booking Reference no is {refNo}"
            dispatcher.utter_message(message)
        else:
            dispatcher.utter_message("Kindly provide correct table Number")

        return []


class ActionCancelBooking(Action):
    #
    def name(self) -> Text:
        return "action_cancel_booking"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        import datetime

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("testrasa").sheet1  # Open the spreadhseet
        # data = sheet.get_all_records()  # Get a list of all records
        sheets = client.open("testrasa")
        sheet2 = sheets.worksheet("Sheet2")

        cancel = tracker.get_slot("cancl")
        if cancel == "positive":
            refNo = tracker.get_slot("refno")
            # print()
            # print(refno)
            cell = sheet.find(refNo)
            Col = cell.col
            Row = cell.row
            Table = sheet.cell(Row, Col + 1).value
            sheet.update_cell(Row, Col - 1, "Cancel")

            tabelcell = sheet2.find(Table)
            tabelcol = tabelcell.col

            date = str(datetime.date.today())
            tabelcell2 = sheet2.find(date)
            tabelrow = tabelcell2.row

            sheet2.update_cell(tabelrow, tabelcol, "Available")
            dispatcher.utter_message("Your booking has been cancel")
            # sheet.update_cell(Row, Col+1, "")
        elif cancel == "negative":

            dispatcher.utter_message("See you on tabel")

        return []


class ActionCheckBookingStatus(Action):
    #
    def name(self) -> Text:
        return "action_check_booking"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheet = client.open("testrasa").sheet1  # Open the spreadhseet
        # data = sheet.get_all_records()  # Get a list of all records
        refNo = tracker.latest_message['text']
        try:

            cell = sheet.find(refNo)
            # print(refno)

            dispatcher.utter_message(template="utter_confirmcancel")

        except Exception as e:
            print(e)
            dispatcher.utter_message("Record Not Found")

        return [SlotSet('refno', tracker.latest_message['text'])]
# ###############################################


class ActionSaveLocation(Action):
    #
    def name(self) -> Text:
        return "action_save_location"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        import datetime
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("testrasa").sheet1  # Open the spreadhseet
        # data = sheet.get_all_records()  # Get a list of all records
        date = str(datetime.date.today())
        time = datetime.datetime.now()
        hour = str(time.hour)
        minu = str(time.minute)
        to_save = [date, hour, minu]
        sheet.insert_row(to_save, 3)
        location = tracker.get_slot("location")
        sheet.update_cell(3, 4, location)
        dispatcher.utter_message("Okay")

        return []


class ActionSaveVeg(Action):
    #
    def name(self) -> Text:
        return "action_save_veg"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials


        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        veg = tracker.get_slot("veg")

        sheet3.update_cell(3, 5, veg)
        # sheet4.insert_row([veg], 3)
        dispatcher.utter_message("Okay.")

        return []


class ActionSaveNonVeg(Action):
    #
    def name(self) -> Text:
        return "action_save_nonveg"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials


        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        non_veg = tracker.get_slot("non_veg")

        sheet3.update_cell(3, 5, non_veg)
        # sheet4.insert_row([non_veg], 3)
        dispatcher.utter_message("Okay.")

        return []


class ActionSaveBread(Action):
    #
    def name(self) -> Text:
        return "action_save_bread"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials


        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        bread = tracker.get_slot("bread")

        sheet3.update_cell(3, 5, bread)
        # sheet4.insert_row([bread], 3)
        dispatcher.utter_message("Okay.")

        return []


class ActionSaveDesserts(Action):
    #
    def name(self) -> Text:
        return "action_save_desserts"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials


        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        desserts = tracker.get_slot("desserts")

        sheet3.update_cell(3, 5, desserts)
        # sheet4.insert_row([desserts], 3)
        dispatcher.utter_message("Okay.")

        return []


class ActionStartEntry(Action):
    #
    def name(self) -> Text:
        return "action_start_entry"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        import datetime
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        date = str(datetime.date.today())
        time = datetime.datetime.now()
        hour = str(time.hour)
        minu = str(time.minute)
        to_save = [date, hour, minu]
        sheet3.insert_row(to_save, 3)
        refNo = secrets.token_hex(3)

        sheet3.update_cell(3, 7, refNo)
        sheet4.insert_row([], 3)
        sheet4.update_cell(3, 3, refNo)
        sheet4.insert_row([], 3)
        sheet4.update_cell(4, 2, "=sum(B1:B3)")

        dispatcher.utter_message("Okay.")


        return []


class ActionStarterEntry(Action):
    #
    def name(self) -> Text:
        return "action_starter_entry"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        import datetime
        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        starter = tracker.get_slot("starters")

        sheet3.update_cell(3, 4, starter[0])
        sheet4.insert_row(starter, 3)
        dispatcher.utter_message("Okay.")

        return []


class ActionSaveCuisine(Action):
    #
    def name(self) -> Text:
        return "action_save_cuisine"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        cuisines = tracker.get_slot("cuisine")
        sheet4.insert_row(cuisines, 3)


        dispatcher.utter_message("Okey")

        return []


class ActionMoreOrder(Action):
    #
    def name(self) -> Text:
        return "action_check_more_order"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

        creds = ServiceAccountCredentials.from_json_keyfile_name("/app/actions/creds.json", scope)
        client = gspread.authorize(creds)
        sheets = client.open("testrasa")
        sheet3 = sheets.worksheet("Sheet3")  # Open the spreadhseet
        sheet4 = sheets.worksheet("Sheet4")
        # data = sheet.get_all_records()  # Get a list of all records

        more_or_not = tracker.get_slot("contorder")
        if more_or_not == "no more":
            x = list(sheet4.col_values(1))
            order_is = ', '.join(map(str, x))
            Bill = sheet4.cell(len(x) + 2, 2).value
            Bill_message = f'your bill amount is Rs. {Bill} plus tax'
            for idx, value in enumerate(x):
                if (idx + 1) <= 2:
                    continue
                sheet4.update_acell("C{}".format(idx + 1), value)
                sheet4.update_acell("A{}".format(idx + 1), '')

            dispatcher.utter_message(order_is)
            dispatcher.utter_message(Bill_message)
        elif more_or_not == "more order":
            dispatcher.utter_message(template="utter_food_type")



        return []
