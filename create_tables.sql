-- カテゴリテーブル
CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  category VARCHAR(255) NOT NULL
);

-- 飲食店テーブル
CREATE TABLE eshops (
  id INT AUTO_INCREMENT PRIMARY KEY,
  location VARCHAR(255),
  shop VARCHAR(255) NOT NULL,
  detail TEXT,
  category_id INT,
);
