# Dokumentasi API EcoRealm
- Method                    : Get
- Url                       : https://ecorealm-api.vercel.app/
- Deskripsi                 : Mengecek Status Aktif API
- Headers                   : Content-Type: application/json  
- Request Body              : None
- Response Sukses (201)     : 
{
  "message": "API EcoRealm aktif!",
  "status": "sukses"
}
- Response Error  (400)     : 
Status: 404 Not Found

- Method                    : Get
- Url                       : https://ecorealm-api.vercel.app/pemain
- Deskripsi                 : Mengambil Seluruh Daftar Pemain di Database
- Headers                   : Content-Type: application/json  
- Request Body              : None
- Response Sukses (201)     : 
{
  "data": [
    {
      "id_pemain": 1,
      "kata_sandi": "123",
      "tanggal_bergabung": "Sat, 24 Oct 2026 06:15:46 GMT",
      "total_jam_bermain": 0,
      "username": "diandratama"
    },
    {
      "id_pemain": 6,
      "kata_sandi": "Betatester",
      "tanggal_bergabung": "Sat, 24 Oct 2026 11:48:22 GMT",
      "total_jam_bermain": 0,
      "username": "Kirito"
    }
  ],
  "status": "sukses"
}
- Response Error  (400)     : 
Status: 404 Not Found


- Method                    : Post
- Url                       : https://ecorealm-api.vercel.app/pemain
- Deskripsi                 : Menambah pemain ke database
- Headers                   : Content-Type: application/json  
- Request Body              : 
{
  "username": "AkselJoss",
  "kata_sandi": "Polines"
}
- Response Sukses (201)     : 
{
  "data": {
    "id_pemain": 7,
    "username": "AkselJoss"
  },
  "message": "Pemain berhasil ditambahkan",
  "status": "sukses"
}
- Response Error  (400)     :
{
  "error": "Data tidak lengkap"
}

- Method                    : Put
- Url                       : https://ecorealm-api.vercel.app/pemain/7
- Deskripsi                 : Mengubah Password dari pemain 7
- Headers                   : Content-Type: application/json  
- Request Body              : 
{
  "kata_sandi": "Polinasssss"
}
- Response Sukses (201)     : 
{
  "message": "Kata sandi pemain ID 7 berhasil diubah",
  "status": "sukses"
}
- Response Error  (400)     :
{
  "message": "Pemain tidak ditemukan",
  "status": "error"
}

- Method                    : Delete
- Url                       : https://ecorealm-api.vercel.app/pemain/8
- Deskripsi                 : Mengahapus data pemain 8 dari database (sebelumnya saya sudah Post data pemain 8)
- Headers                   : Content-Type: application/json  
- Request Body              : None
- Response Sukses (201)     : 
{
  "message": "Pemain ID 8 berhasil dihapus",
  "status": "sukses"
}
- Response Error  (400)     : 
{
  "message": "Pemain tidak ditemukan",
  "status": "error"
}