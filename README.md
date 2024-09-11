
# Pemrograman Berbasis Platform E 
## MeowPedia  😽😽
### Nama : Ilham Ghani Adrin Sapta
### NPM  : 2306201792
### Link : http://ilham-ghani-meowpedia.pbp.cs.ui.ac.id/ (Status: Offline)


---

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

<details>
<summary>Click for more detail</summary>
<br>

### 1️⃣ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
Tema Project ini adalah toko adopsi kucing menggunakan Django Framework

#### ✅ Membuat sebuah proyek Django baru:
- Membuat direktori baru bernama meowpedia yang akan menjadi root dari project ini.
- Masuk ke dalam direktori dan membuat virtual environment python pada directory tersebut dengan kode berikut.
  
  ```
  python -m venv env
  ```

- Mengaktifkan virtual Enviroment agar bisa menginstall dependencies pada virtual environment dengan kode berikut.

  ```
  \env\scripts\activate
  ```


- Selanjutnya membuat file `requirement.txt` yang akan menampung semua dependencies yang digunakan oleh proyek ini, saat ini dependenciesnya adalah sebagai berikut.

  ```
  django
  gunicorn 
  whitenoise
  psycopg2-binary
  requests
  urllib3
  ```
- Terakhir yaitu menginstall seluruh dependencies pada requirements.txt dengan menjalankan perintah berikut.
  ```
  pip install -r requirements.txt
  ```

#### ✅ Membuat aplikasi dengan nama main pada proyek tersebut:
- Menjalankan command `python manage.py startapp main` pada root direktori untuk membuat kerangka aplikasi kita.
- Direktori aplikasi bernama main akan menjadi struktur aplikasi kita kedepannya.

#### ✅ Melakukan routing pada proyek agar dapat menjalankan aplikasi main:
- menambah aplikasi `'main'` pada variabel `INSTALLED_APPS` di direktori `meowpedia\settings.py` a agar aplikasi dapat ditampilkan.

#### ✅ Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut:
Selanjutnya memodifikasi models.py di folder main sebagai struktur database kita sebagai berikut:
```python
class MeowEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField
    description = models.TextField
    species = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)
    age = models.IntegerField
```
 name akan menerima tipe char dengaan panjang maximum 255.
 price akan menerima harga.
 description akan menerima Text.
 species akan menerima char.
 colour akan menerima char.
 age akan menerima integer.

#### ✅ Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu:
- Membuat direktori baru bernama `templates` pada direktor main.
- Membuat file bernama home.html pada direktori templates yang berisi kode HTML yang akan menampilkan nama aplikasi, nama, dan kelas:
- 
  ```markdown
  <h1>Meowpedia</h1>

  <h4>NPM: {{ npm }}</h5>
  <h4>Nama: {{ name }}</h5>
  <h4>Kelas: {{ class }}</h5>

  ```
  
- Menambah fungsi show_home pada views.py di direktori aplikasi main untuk mengembalikan nilai nama aplikasi, nama, dan kelas:
  ```python
  def show_home(request):
    context = {
        'npm' : '2306201792',
        'name': 'Ilham Ghani Adrin Sapta',
        'class': 'PBP E'
    }

    return render(request, "home.html", context)
  ```
- Menjalankan command `python manage.py makemigrations` dan `python manage.py migrate` untuk melakukan membuat berkas migrasi dan mengaplikasikan perubahan model ke basis data.

#### ✅ Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
- Masuk ke file urls.py pada direktori aplikasi main untuk menulis rute url aplikasi main dan menggunakan fungsi yang telah dibuat:
  ```python
  from django.urls import path
  from main.views import show_home

  app_name = 'home'
  urlpatterns = [
      path('', show_home, name='show_home')
  ]

  ```
- Masuk ke dalam file `urls.py` pada direktori meowpedia dan import fungsi `include` dari `django.urls`.
- Menambah pattern url untuk aplikasi main yang menunjuk pada direktori `main.urls`:

  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('main.urls'))
  ]

  ```

#### ✅ Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
- Melakukan inisiasi git pada direktori utama dengan`git init`.
- Menambah konfigurasi user pada git.
- Menambah file .gitignore untuk file yang diabaikan.
- Membuat repositori baru pada github bernama `meowpedia`.
- Membuat branch baru bernama `main` pada git dan menghubungkan repositori lokal dengan repositori yang telah dibuat pada github dengan perintah. `git remote add origin <link repository>`
- Melakukan add, commit, dan push pada repositori github.
- menginisialisasi project baru pada PWS dengan nama project `meowpedia` dan menyimpan kredensial untuk kedepannya.
- menghubungkan repository saat ini dengan PWS melalui perintah `git remote add pws <pws repository>`.
- Menjalankan `python manage.py makemigrations` dan `python manage.py migrate` untuk memperbarui bentuk database
- lihat project di PWS dan tunggu hingga build selesai.
- Jika build selesai, lihat dan bagikan project ke teman-teman untuk dilihat 😺 

### 2️⃣ Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](/img/PBPdrawio.png)

 + User akan menuliskan suatu permintaan ke browser yang kemudian akan diteruskan oleh internet.
 + Klien (browser) mengirim permintaan HTTP ke alamat project kita.
 + Project menerima permintaan melalui `url.py` dimana akan diperiksa apakaah yang meminta adalah user yang valid
 + Kemudian URLS akan melanjutkan pengguna ke `views.py` dimana ia akan membangun aplikasi yang akan ditampilkan
 + `views.py` akan meminta ke models untuk mendapatkan data dan informasi dari database. user juga bisa menambahkan sesuatu ke database jika diizinka
 + `views.py` juga akan meminta ke template untuk tampilan utama yang akan dilihat pengguna
 + terakhir, `views.py` membangun bentuk akhir aplikasi untuk dikembalikan ke pengguna

### 3️⃣ Jelaskan fungsi git dalam pengembangan perangkat lunak!
  git berperan penting sebagai version control dan collaborative tool yang memungkinkan pengembangan perangkat lunak besar yang terstruktur. Sebelum adanya git, setiap pengembang harus memberi source code program ke pengembang yang lain yang ingin ikut mengembangkan perangkat lunak yang sama. pada saat yang sama, pengembang yang lain tidak bisa mengubah source code itu sesukanya tanpa kemungkinan terjadinya konflik dengan pengembang yang lain sehingga pengembangan menjadi lambat dan error-prone.
  
  Dengan git, pengembangan menjadi jauh lebih terstruktur dengan fitur fitur utama yang ditawari git yaitu:

  + Track History: pengembang dapat melihat sejarah pengembangannya
  + Backup: pengembang dapat kembali ke versi kode yang sudah di simpan di git jika terjadi masalah dengan kode saat ini
  + Collaborative Development: beberapa pengembang dapat bekerja pada satu proyek yang sama di waktu yang sama dengan tools tambahan seperti github yang memungkinkan git untuk terhubung ke internet.
  + Branching: saat pengembangan suatu fitur selesai, fitur tersebut dapat di-integrasikan dengan kode utama dengan fitur branch merge. fitur ini juga membuat kode utama tidak berubah saat pengembangan fitur lainnya.

  Masih banyak fitur yang git tawarkan untuk memudahkan proses pengembangan perangkat lunak. Oleh karena beberapa alasan tersebut, git menjadi standar industri dalam pengembangan perangkat lunak.


### 4️⃣ Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  Menurut saya, alasan utama kenapa Django dijadikan pembelajaran utama dibanding framework lain adalah karena prinsip yang ada di Django itu sendiri yaitu RAPID DEVELOPMENT.

  Di Django sendiri, prinsip rapid development ini ada dalam bentuk fitur dan kemampuan yang diberikan django ke para  yang sangat lengkap. misalnya, Django hadir dengan banyak fitur web development utama yang sering digunakan pengembang sehingga kita tidak perlu membuat kode-kode sederhana sehingga membuat proses pengembangan lebih berfokus kepada hasil akhir.

  Beberapa fitur utama lainnya yang menjadikan Django sebagai permulaan pembelajaran adalah:

  + ORM, atau object relational model yang memberikan pengembang cara mudah untuk melaksanakan CRUD(Create, Retrive, Update, Delete) pada database setelah model dibuat.
  + Database Migration, saat struktur database perlu diubah, django membuatnya sangat mudah bagi pengembang
  + MVT, dengan MVT, django menggunakan sistem antarmuka yang intuitif dan mengedepankan pengembangan terstruktur.
  + Powerfull Routing, Django menyediakan alat routing yang mudah, dengan dynamic URLS. 
  + Essentials built-in, fitur seperti admin, autentikasi, users sudah ada di Django sehingga pengembang dapat fokus ke logic utama aplikasinya

Dari beberapa alasan tersebut, dapat disimpulkan bahwa Django adalah framework yang tepat sebagai alat pembelajaran pertama.

### 5️⃣ Mengapa model pada Django disebut sebagai ORM?
Di Django, kita dapat berinteraksi dengan database melalui objek objek yang kita buat dibanding menulis query SQL khusus untuk setiap perintah ke database.

Dalam Django, model adalah representasi dari tabel dalam database, dan setiap field dalam model merepresentasikan kolom dalam tabel. ORM ini membantu mengelola dan memanipulasi data dalam database dengan menggunakan method di Python tanpa perlu menulis SQL secara manual.
fitur yang ada pada ORM meliputi

+ Mapping antara Objek dan Database, Kelas model Django dihubungkan ke tabel database, di mana setiap instance dari model merepresentasikan satu baris data di database.

+ CRUD Operations, Django ORM menyediakan cara mudah untuk melakukan operasi CRUD (Create, Read, Update, Delete) dengan cara Pythonik seperti Model.objects.create(), Model.objects.filter(), dan Model.objects.delete().

+ Abstraksi Database, ORM memungkinkan untuk menggunakan berbagai database (MySQL, PostgreSQL, SQLite, dll.) tanpa perlu mengubah kode Python, cukup mengubah konfigurasi database.

karena interaksi antara database dan model object inilah django disebut sebagai ORM.

</details>
