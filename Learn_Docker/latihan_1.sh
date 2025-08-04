#!/bin/bash

# Cara menggunakan?

# Berikan Izin Eksekusi
# "chmod +x <nama_file>.sh"

# Jalankan Script:
# "./<nama_file>.sh"

#!/bin/bash

echo "--- Memulai Sesi Latihan Docker ---"
echo "Pastikan Docker Desktop/Daemon kamu berjalan."
echo "Beberapa perintah memerlukan interaksi atau penggantian ID secara manual."
echo "Tekan Enter untuk melanjutkan ke bagian berikutnya..."
read -r

# --- Bagian 1 ---
echo -e "\n--- Bagian 1: Perintah dasar menjalankan kontainer ---"
# Latihan: Jalankan image alpine dan cetak teks “Halo Farhan”
docker run alpine echo "Halo Parhan"
# Latihan: Jalankan image ubuntu dan jalankan perintah ls
docker run ubuntu ls
# Latihan: Jalankan image busybox dan jalankan date
docker run busybox date
read -r -p "Bagian 1 Selesai. Tekan Enter untuk lanjut ke Bagian 2..."

# --- Bagian 2 ---
echo -e "\n--- Bagian 2: Kontainer di latar belakang dan pemeriksaan status ---"
# Latihan: Jalankan container ubuntu dalam mode sleep selama 60 detik
docker run -d ubuntu sleep 60
# Latihan: Jalankan docker ps dan pastikan container terlihat
docker ps
# Latihan: Tambahan: Lihat semua container (termasuk yang sudah stop)
docker ps -a
read -r -p "Bagian 2 Selesai. Tekan Enter untuk lanjut ke Bagian 3..."

# --- Bagian 3 ---
echo -e "\n--- Bagian 3: Menghentikan kontainer ---"
# Latihan: Jalankan container ubuntu dan biarkan sleep 300 detik
docker run -d ubuntu sleep 300
# Latihan: Stop container itu setelah 10 detik
docker stop <container_id>
# Latihan: Coba stop 2 container sekaligus (pakai dua ID)
docker stop <container_id> <container_id>
read -r -p "Bagian 3 Selesai. Tekan Enter untuk lanjut ke Bagian 4..."

# --- Bagian 4 ---
echo -e "\n--- Bagian 4: Menghapus kontainer ---"
# Latihan: Jalankan dan stop container alpine
docker run alpine 
docker stop <container_id>
docker run <container_id>
# (ku skip, aku menggunakan rm, karena ada beberapa container penting)
read -r -p "Bagian 4 Selesai. Tekan Enter untuk lanjut ke Bagian 5..."

# --- Bagian 5 ---
echo -e "\n--- Bagian 5: Mengelola image dan kontainer HTTPD ---"
# Latihan: Jalankan docker images
docker images
# Latihan: Jalankan image baru (misal: httpd) lalu cek apakah muncul di daftar image
docker run -d --name my-httpd-server httpd
# Latihan: Coba download image baru, lalu lihat kembali
docker ps
read -r -p "Bagian 5 Selesai. Tekan Enter untuk lanjut ke Bagian 6..."

# --- Bagian 6 ---
echo -e "\n--- Bagian 6: Menghapus image ---"
# Latihan: Hapus image hello-world dari sistemmu
docker rmi <images_id>
# Latihan: Coba hapus image yang sedang dipakai oleh container (lihat errornya!)
docker rmi <images_id> (mengeluarkan output error, karena sedang ada container yang menggunakan images tsb)
# (ku skip, aku menggunakan rm, karena ada beberapa container penting)
read -r -p "Bagian 6 Selesai. Tekan Enter untuk lanjut ke Bagian 7..."

# --- Bagian 7 ---
echo -e "\n--- Bagian 7: Mengunduh image dari Docker Hub ---"
# Latihan: Download image python:3.10
docker pull python:3.10
# Latihan: Download node:18-alpine
docker pull node:18-alpine
# Latihan: Download image mysql, cek ukurannya
docker pull mysql
docker images | grep mysql
read -r -p "Bagian 7 Selesai. Tekan Enter untuk menyelesaikan script..."

# --- Bagian 8 ---
# Latihan: Jalankan container Ubuntu dengan sleep 300 agar tetap hidup:
docker run -d --name latihan-exec ubuntu sleep 300
# Latihan: masuk ke dalam container yang sedang berjalan
docker exec -it <container_id> bash

# --- Bagian 9 ---
# Format
# docker run -d -p <host_port>:<container_port> <image>

# Latihan: Jalankan Web Server Nginx
docker run -d --name web-nginx -p 8080:80 nginx
# Latihan: Jalankan Server Python HTTP (Port 8000)
docker run -d -p 8000:8000 python:3-slim python -m http.server 8000

# --- Bagian 10 ---
# Format
# docker run -v /path/di/host:/path/di/container image

# Latihan: Jalankan Python Script dari Folder Host
print("Hai dari volume!") # anggap aja file ini berada di direktori "docker_test/test.py"
docker run --rm -v $(cd)/docker_test:/app python:3 python /app/test.py  # Jika linux
docker run --rm -v %cd%:/app python:3 python /app/test.py  # Jika windows

# --- Bagian 11 ---
# Format
# docker build -t nama-image:tag .

# Latihan: Buat Dockerfile sederhana
docker build -t farhan/halo:v1 .
