-- Write your migrate up statements here
create table users(
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
  create_at varchar
);

---- create above / drop below ----

drop table users;
-- Write your migrate down statements here. If this migration is irreversible
-- Then delete the separator line above.
