-- init_db.sql
CREATE TABLE IF NOT EXISTS stamps (
    id INT AUTO_INCREMENT PRIMARY KEY,
    route_name VARCHAR(255) NOT NULL,
    qr_code VARCHAR(255) NOT NULL
);

INSERT INTO stamps (route_name, qr_code) VALUES ('ルートA', 'QR_CODE_A');
INSERT INTO stamps (route_name, qr_code) VALUES ('ルートB', 'QR_CODE_B');