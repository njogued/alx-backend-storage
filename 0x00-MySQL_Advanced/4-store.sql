-- CREATE TRIGGER to update items when new order is created

CREATE TRIGGER update_items_qty
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name