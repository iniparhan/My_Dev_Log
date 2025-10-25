# Learn PostgreSQL

Repository ini berisi langkah-langkah dasar untuk menjalankan PostgreSQL menggunakan Docker, serta contoh perintah SQL dan konsep database penting.

## Langkah-langkah Setup PostgreSQL dengan Docker

### 1. Membuat Container
Jalankan perintah berikut untuk membuat container PostgreSQL:

`docker run --name learn-databases -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres`

### 2. Menjalankan Container
Untuk menjalankan container yang sudah dibuat:

`docker start learn-databases`

### 3. Mengakses PostgreSQL
Masuk ke PostgreSQL di dalam container:

`docker exec -it learn-databases psql -U postgres`

## Dasar-dasar SQL di PostgreSQL

### Database

```sql
-- Buat database baru
CREATE DATABASE nama_database;

-- Hapus database
DROP DATABASE nama_database;

-- Pindah ke database lain
\c nama_database

-- Lihat daftar database
\l
```

### Table (Tabel)

```sql
-- Buat tabel
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Hapus tabel
DROP TABLE users;

-- Lihat struktur tabel
\d users
```

### Insert Data (Masukkan Data)

```sql
-- Masukkan satu baris
INSERT INTO users (name, email) VALUES ('Ahmad', 'ahmad@mail.com');

-- Masukkan beberapa baris
INSERT INTO users (name, email) VALUES 
('Budi', 'budi@mail.com'),
('Citra', 'citra@mail.com');
```

### Select (Ambil Data)

```sql
-- Ambil semua kolom
SELECT * FROM users;

-- Ambil kolom tertentu
SELECT name, email FROM users;

-- Ambil data dengan kondisi
SELECT * FROM users WHERE name='Ahmad';

-- Ambil data dengan urutan
SELECT * FROM users ORDER BY created_at DESC;

-- Limit jumlah data
SELECT * FROM users LIMIT 5;
```

### Update (Ubah Data)

```sql
-- Ubah email user tertentu
UPDATE users
SET email='ahmadbaru@mail.com'
WHERE name='Ahmad';

-- Ubah semua baris (contoh: tambahkan domain email)
UPDATE users
SET email = name || '@example.com';
```

### Delete (Hapus Data)

```sql
-- Hapus baris tertentu
DELETE FROM users WHERE name='Citra';

-- Hapus semua data
DELETE FROM users;
```

### Alter (Ubah Struktur Tabel)

```sql
-- Tambah kolom baru
ALTER TABLE users ADD COLUMN age INT;

-- Ubah tipe data kolom
ALTER TABLE users ALTER COLUMN age TYPE SMALLINT;

-- Hapus kolom
ALTER TABLE users DROP COLUMN age;
```

### Index (Optimasi Pencarian)

```sql
-- Buat index
CREATE INDEX idx_users_name ON users(name);

-- Hapus index
DROP INDEX idx_users_name;
```

### Query Lanjutan & Aggregate Functions

```sql
-- Hitung jumlah baris
SELECT COUNT(*) FROM users;

-- Hitung jumlah per kategori
SELECT age, COUNT(*) FROM users GROUP BY age;

-- Ambil data dengan kondisi logika
SELECT * FROM users WHERE age > 20 AND name LIKE 'A%';

-- Contoh fungsi agregat lain
SELECT AVG(age) AS rata_rata_umur FROM users;
SELECT SUM(age) AS total_umur FROM users;
```

### Transaction (Transaksi)

```sql
-- Mulai transaksi
BEGIN;

-- Jalankan query yang ingin dijalankan dalam transaksi
UPDATE users SET email='test@mail.com' WHERE name='Budi';

-- Commit untuk menyimpan perubahan
COMMIT;

-- Rollback untuk membatalkan perubahan
ROLLBACK;
```

### Shortcut dan perintah psql

```sql
-- Lihat semua tabel
\dt

-- Lihat struktur tabel
\d users

-- Keluar psql
\q
```

## Konsep Database Lanjutan dengan Contoh Syntax

### JOIN (Menggabungkan Data dari Beberapa Tabel)

```sql
-- Contoh tabel orders dan users
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product_name VARCHAR(50),
    amount INT
);

-- Inner Join: ambil data user beserta order-nya
SELECT u.name, o.product_name, o.amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- Left Join: ambil semua user walaupun tidak punya order
SELECT u.name, o.product_name, o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;
```

### WHERE, ORDER BY, LIMIT (Filter, Urutkan, Batasi Hasil Query)

```sql
-- Ambil user dengan umur > 20
SELECT * FROM users
WHERE age > 20;

-- Urutkan user berdasarkan umur menurun
SELECT * FROM users
ORDER BY age DESC;

-- Ambil 5 data pertama
SELECT * FROM users
LIMIT 5;

-- Kombinasi WHERE, ORDER BY, LIMIT
SELECT * FROM users
WHERE age > 20
ORDER BY created_at DESC
LIMIT 3;
```

### Database Design & Normalisasi

* **1NF (First Normal Form)** → Hilangkan kolom yang mengandung banyak nilai, tiap kolom satu nilai.
* **2NF (Second Normal Form)** → Hilangkan ketergantungan parsial pada primary key.
* **3NF (Third Normal Form)** → Hilangkan ketergantungan transitif antar kolom non-key.

```sql
-- Contoh 1NF → pisahkan alamat menjadi kolom sendiri
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    street VARCHAR(100),
    city VARCHAR(50),
    postal_code VARCHAR(10)
);

-- Contoh 2NF → tabel orders sudah memiliki user_id, tidak ada info user ganda
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product_name VARCHAR(50),
    amount INT
);

-- Contoh 3NF → tabel products pisahkan kategori supaya tidak duplikat
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    category_id INT REFERENCES categories(id)
);
```

### Indexes (Optimasi Pencarian Data)

```sql
-- Buat index untuk mempercepat pencarian user berdasarkan nama
CREATE INDEX idx_users_name ON users(name);

-- Hapus index
DROP INDEX idx_users_name;

-- Contoh penggunaan index dengan query cepat
SELECT * FROM users WHERE name='Ahmad';
```
