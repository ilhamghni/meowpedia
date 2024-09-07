
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

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). 
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

#### 2️⃣ Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![](img/PBBdrawio.png)

 + User akan menuliskan suatu permintaan ke browser yang kemudian akan diteruskan oleh internet.
 + Klien (browser) mengirim permintaan HTTP ke alamat project kita.
 + Project menerima permintaan melalui `url.py` dimana akan diperiksa apakaah yang meminta adalah user yang valid
 + Kemudian URLS akan melanjutkan pengguna ke `views.py` dimana ia akan membangun aplikasi yang akan ditampilkan
 + `views.py` akan meminta ke models untuk mendapatkan data dan informasi dari database. user juga bisa menambahkan sesuatu ke database jika diizinka
 + `views.py` juga akan meminta ke template untuk tampilan utama yang akan dilihat pengguna
 + terakhir, `views.py` membangun bentuk akhir aplikasi untuk dikembalikan ke pengguna

#### 3️⃣ Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment memungkinkan kita sebagai pengguna untuk mengisolasi dependensi setiap proyek Python di sistem kita. Dalam pengembangan aplikasi berbasis Django, proyek yang berbeda mungkin memerlukan versi paket yang berbeda, seperti Django atau library lainnya. Dengan virtual environment, setiap proyek memiliki lingkungan independen sehingga perubahan pada satu proyek tidak akan memengaruhi proyek lain. Hal ini juga memudahkan pengelolaan dependensi dan menjaga konsistensi antar proyek, baik saat mengerjakan sendiri atau bersama dengan rekan tim.

Meskipun aplikasi Django dapat dibuat tanpa menggunakan virtual environment, hal ini cukup tidak disarankan. Menginstal paket secara global di sistem dapat menyebabkan konflik versi dan kesulitan dalam manajemen proyek, terutama jika kita bekerja pada beberapa proyek dengan dependensi yang berbeda. Dependensi itu bisa saja sudah tidak didukung di versi python tertentu, atau diperbarui sehingga tidak dapat digunakan lagi. Tanpa virtual environment, ada risiko salahnya versi dependensi yang bisa menyebabkan aplikasi tidak berfungsi dengan benar. Jadi, meskipun bisa dilakukan tanpa virtual environment, penggunaan virtual environment sangat disarankan dan sudah menjadi standar dimana-mana.

#### 4️⃣ Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya!
Jawab:  
Ketiga istilah adalah sebuah bentuk pattern arsitektur yang biasa digunakan dalam membangun perangkat lunak. Penggunaan pattern arsitektur yang baik akan menciptakan modularitas yang baik dalam menyatukan kerangka perangkat lunak.
- MVC(Model-View-Controller)
- MVT(Model-View-Template)
- MVVM(Model-View-ViewModel)


### 1. **MVC (Model-View-Controller)**:
   - **Model**: Berisi data dan logika bisnis, seperti database dan struktur data.
   - **View**: Mengontrol tampilan antarmuka pengguna, menampilkan data dari model.
   - **Controller**: Mengatur interaksi antara Model dan View, menangani input pengguna dan mengirim data ke Model atau View.
   - **Contoh**: Umum dalam banyak framework seperti Ruby on Rails dan Laravel.

### 2. **MVT (Model-View-Template)**:
   - **Model**: Sama seperti di MVC, berfungsi untuk menangani data dan logika bisnis.
   - **View**: Mengambil data dari Model dan menentukan respons yang akan dikirim ke pengguna.
   - **Template**: Berfungsi sebagai lapisan presentasi, seperti HTML, CSS, untuk menampilkan data ke pengguna.
   - **Contoh**: Digunakan oleh **Django**, dengan `View` yang lebih fokus pada logika, dan `Template` yang menangani tampilan.

### 3. **MVVM (Model-View-ViewModel)**:
   - **Model**: Sama seperti di MVC, mengelola data dan logika bisnis.
   - **View**: Berfungsi untuk menampilkan antarmuka pengguna.
   - **ViewModel**: Mengikat `Model` dan `View`, berisi logika presentasi dan memformat data sebelum ditampilkan pada View.
   - **Contoh**: Banyak digunakan dalam framework frontend seperti **Angular** dan **WPF** di .NET.

### **Perbedaan Utama**:
- **MVC**: Menggunakan `Controller` untuk mengatur logika antar `Model` dan `View`.
- **MVT**: Mengganti `Controller` dengan `View` yang menangani respons, dan menggunakan `Template` untuk presentasi.
- **MVVM**: Menggunakan `ViewModel` untuk memisahkan logika presentasi dari `View`, memungkinkan binding data yang lebih reaktif antara `Model` dan `View`.

</details>
