from database.init_db import db
from database.db_configs import user_db_table_name
import datetime


def create_user_table():
    execute = f"""create table {user_db_table_name}(
          id serial primary key,
          telegram_id bigint UNIQUE not null,
          phone_number varchar UNIQUE,
          order_count varchar,
          gift_type varchar,
          last_command varchar,
          last_sms timestamp,
          current_menu varchar,
          lang varchar,
          hive_id varchar,
          stable_id varchar,
          stable_key varchar,
          create_at varchar);"""
    db.execute_update(execute)


def create_user(telegram_id):
    execute = f"INSERT INTO {user_db_table_name} " \
                      "(telegram_id, lang, create_at) " \
                      "VALUES " \
                      "(%s, %s, %s);"

    db.execute_update(execute, (telegram_id, "uz", datetime.datetime.now()))


def update_phone_number(telegram_id, phone_number):
    execute = f"UPDATE {user_db_table_name} " \
                              "SET phone_number=%s " \
                              "WHERE telegram_id=%s;"

    db.execute_update(execute, (phone_number, telegram_id))


def update_stable_id(telegram_id, stable_id):
    execute = f"UPDATE {user_db_table_name} " \
                           "SET stable_id=%s " \
                           "WHERE telegram_id=%s;"

    db.execute_update(execute, (stable_id, telegram_id))


def update_stable_key(telegram_id, stable_key):
    execute = f"UPDATE {user_db_table_name} " \
                            "SET stable_key=%s " \
                            "WHERE telegram_id=%s;"

    db.execute_update(execute, (stable_key, telegram_id))


def update_user_contact(telegram_id, phone_number, hive_id):
    execute = f"UPDATE {user_db_table_name} " \
                            "SET phone_number=%s, hive_id=%s " \
                            "WHERE telegram_id=%s;"

    db.execute_update(execute, (phone_number, hive_id, telegram_id))


def update_stable_id_and_key(telegram_id, stable_id, stable_key):
    execute = f"UPDATE {user_db_table_name} " \
                                   "SET stable_id=%s, stable_key=%s " \
                                   "WHERE telegram_id=%s;"
    db.execute_update(execute, (stable_id, stable_key, telegram_id))


def update_last_command(telegram_id, last_command):
    execute = f"UPDATE {user_db_table_name} " \
                              "SET last_command=%s " \
                              "WHERE telegram_id=%s;"
    db.execute_update(execute, (last_command, telegram_id))


def update_last_sms(telegram_id, last_sms_date_time):
    execute = f"UPDATE {user_db_table_name} " \
                          "SET last_sms=%s " \
                          "WHERE telegram_id=%s;"

    db.execute_update(execute, (last_sms_date_time, telegram_id))


def update_current_menu(telegram_id, current_menu):
    execute = f"UPDATE {user_db_table_name} " \
                              "SET current_menu=%s " \
                              "WHERE telegram_id=%s;"
    db.execute_update(execute, (current_menu, telegram_id))


def update_order_count(telegram_id, order_count):
    execute = f"UPDATE {user_db_table_name} " \
                             "SET order_count=%s " \
                             "WHERE telegram_id=%s;"

    db.execute_update(execute, (order_count, telegram_id))


def update_config_lang(telegram_id, config_lang):
    execute = f"UPDATE {user_db_table_name} " \
                      "SET lang=%s" \
                      "WHERE telegram_id=%s;"

    db.execute_update(execute, (config_lang, telegram_id))


def get_user(telegram_id):
    execute = f"SElECT * FROM {user_db_table_name} " \
                 "WHERE telegram_id=%s AND telegram_id=%s;"

    return db.execute_get_one(execute, (telegram_id, telegram_id))


def get_all_users():
    execute = f"SElECT id, telegram_id, phone_number, order_count, gift_type FROM {user_db_table_name};"
    return db.execute_get_all(execute)


def get_all_users_id():
    execute = f"SElECT telegram_id FROM {user_db_table_name};"
    return db.execute_get_all(execute)