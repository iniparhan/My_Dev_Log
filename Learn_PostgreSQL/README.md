# Learn PostgreSQL

Repository ini berisi langkah-langkah dasar untuk menjalankan PostgreSQL menggunakan Docker.

## Langkah-langkah

### 1. Membuat Container
Jalankan perintah berikut untuk membuat container PostgreSQL:

`docker run --name learn-databases -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres`

### 2. Menjalankan Container
Untuk menjalankan container yang sudah dibuat:

`docker start [Container_ID]`

### 3. Mengakses PostgreSQL
Untuk masuk ke PostgreSQL di dalam container:

`docker exec -it learn-databases psql -U postgres`
