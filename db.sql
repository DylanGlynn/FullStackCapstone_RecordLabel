INSERT INTO tzadik_api_modifieduser (is_artist, is_vendor, address_street, address_city, address_state, address_zipcode, payment_type, user_id)
VALUES (False, False, "123 Fake St.", "Hell", "TX", 00001, "Street Cred", 1);

UPDATE tzadik_api_modifieduser
SET address_zipcode = 64901
WHERE id = 2;

DELETE FROM tzadik_api_order
WHERE id > 1;