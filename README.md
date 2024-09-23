
# Pemrograman Berbasis Platform E 
## MeowPedia  😽😽
### Nama : Ilham Ghani Adrin Sapta
### NPM  : 2306201792
### Link : http://ilham-ghani-meowpedia.pbp.cs.ui.ac.id/ (Status: Online)
---



# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django


<details>
<summary>Click for more detail</summary>
<br>

## Deskripsi Tugas
Pada tugas ini, Saya akan mengimplementasikan konsep authentication, session, cookies, serta menerapkan beberapa konsep yang telah dipelajari selama sesi tutorial.

## Checklist Tugas
#### ✅ Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- langkah 1: import formulir dan fungsi bawaan yang disediakan oleh django untuk register, login, dan logout sebagai berikut:
  ```python
  from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
  from django.contrib import messages
  from django.contrib.auth import authenticate, login, logout
  ```
- langkah 2: menambahkan fungsi Login, Register, dan Logout di `views.py` yang diisi dengan form dan fungsi pada library yang sudah di import sebelumnya di langkah 1 seperti berikut:
  ```python
  def register(request):
      form = UserCreationForm()

      if request.method == "POST":
          form = UserCreationForm(request.POST)
          if form.is_valid():
              form.save()
              messages.success(request, 'Your account has been successfully created!')
              return redirect('main:login')
      context = {'form':form}
      return render(request, 'register.html', context)

  def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
              user = form.get_user()
              login(request, user)
              response = HttpResponseRedirect(reverse("main:show_home"))
              response.set_cookie('last_login', str(datetime.datetime.now()))
              return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

  def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
  ```
  fungsi tersebut akan memastikan registrasi dan login di handle dengan baik dan menyimpan sesi sehingga user dapat mengakses aplikasi sebelumnya dengan lancar
- langkah 3: menambahkan template html baru yaitu `login.html` dan `register.html` yang akan menjadi form login dan register aplikasi file. html ini akan terhubung dengan fungsi login dan register di `views.py` dan menggunakan forms bawaan django sehingga tidak perlu lagi membuat form dari awal.

- langkah 4: menambahkan url baru di `urls.py` yang telah dibuat agar redirect url antara home, login, dan register bekerja dengan benar, bentuk `urls.py` akan terlihat sebagai berikut
  ```python
  from django.urls import path
  from main.views import show_home, create_cat_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user

  app_name = 'main'
  urlpatterns = [
      path('', show_home, name='show_home'),
      path('create-cat-entry', create_cat_entry, name='create_cat_entry'),
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
      path('register/', register, name='register'),
      path('login/', login_user, name='login'),
      path('logout/', logout_user, name='logout'),
    ]
  ```
- langkah 5: menambah tombol log out agar pengguna bisa logout dari aplikasi di `home.html`

#### ✅ Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
![](/img/bob.png)
![](/img/dora.png)


#### ✅ Menghubungkan model Product dengan User.
- langkah pertama: menambah import baru di models yaitu User dan menambahkan User tersebut ke CatEntry, User ini akan berperan sebagai Foreign key sehingga setiap User akan memiliki CatEntry khusus. berikut implementasinya 
```python
import uuid
from django.db import models
from django.contrib.auth.models import User

class CatEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    age = models.IntegerField()
    description = models.TextField()
    species = models.CharField(max_length=255)
    colour = models.CharField(max_length=255)

```
- langkah kedua: mengubah fungsi `create_cat_entry` agar dapat menyimpan form bersama dengan user dengan `request.user`.

```python
def create_cat_entry(request):
    form = CatEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        cat_entry = form.save(commit=False)
        cat_entry.user = request.user
        cat_entry.save()
        return redirect('main:show_home')

    context = {'form': form}
    return render(request, "create_cat_entry.html", context)
```

- langkah terakhir: lakukan makemigrations dan migrate menggunakan `python manage.py makemigrations` & `python manage.py migrate` agar perubahan skema database diterapkan.

#### ✅ Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi..
- pertama ubah value context pada fungsi `show_home` di `views.py` yang sebelumnya menampikan nama secara static menjadi menampikan nama tergantung user yang login. disini juga tambahkan entry baru yaitu last-login yang akan mengambil cookies dari penyimpanan user untuk ditampikan, cookies inni dibuat saat user memanggil fungsi login pada `views.py` dan menggunakan datetime library. berikut kodenya:
```python
def show_home(request):
    cat_entries = CatEntry.objects.filter(user=request.user)
    
    context = {
        'npm' : '2306201792',
        'name': request.user.username,
        'class': 'PBP E',
        'cat_entries': cat_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "home.html", context)
```
- lalu tambahkan informasi last login ke `home.html` sehingga kode terlihat sebagai berikut
```html
...
    <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    <h5>Sesi terakhir login: {{ last_login }}</h5>
  </a>
...
```

#### ✅ Menjawab beberapa pertanyaan berikut pada README.md pada root folder.

  - #### 1️⃣ Apa perbedaan antara HttpResponseRedirect() dan redirect()
  `HttpResponseRedirect()` adalah kelas Django yang secara eksplisit membuat respons HTTP dengan kode status 302 (redirect) dan URL tujuan. Sementara itu, `redirect()` adalah fungsi bawaan Django yang mempermudah proses pengalihan (redirect) dengan menerima argumen seperti URL, view name, atau objek model dan secara otomatis menghasilkan `HttpResponseRedirect()` di balik layar.

  Jadi, perbedan utama terletak dimana `HttpResponseRedirect()` mengharuskan URL penuh sebagai argumen, sedangkan `redirect()` lebih fleksibel dan menangani detail pembuatan respons redirect.

  - #### 2️⃣ Jelaskan cara kerja penghubungan model Product dengan User!
  Untuk menghubungkan model **Product** dengan model **User** dalam Django, kita bisa menggunakan **ForeignKey** atau **ManyToManyField**, tergantung pada jenis relasi yang diinginkan. **ForeignKey** digunakan jika setiap produk dimiliki oleh satu pengguna, sementara **ManyToManyField** digunakan jika sebuah produk bisa dimiliki oleh banyak pengguna, dan setiap pengguna bisa memiliki banyak produk. Dengan **ForeignKey**, setiap objek di model **Product** akan memiliki referensi atau istilahnya "terhubung" ke satu pengguna.

  Sebagai contoh, dalam model **CatEntry** yang saya buat, setiap entry kucing dihubungkan dengan pengguna melalui **ForeignKey** pada field **user**. Field **id** menggunakan **UUIDField** sebagai primary key yang dihasilkan secara otomatis menggunakan library bawaan `uuid.uuid4`. Ini memberikan identifikasi unik dan membuat aplikasi menjadi lebih aman untuk setiap catatan. 
  
  - #### 3️⃣ Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
    Dalam django, autentikasi dan otorisasi memiliki beberapa perbedaan mulai dari fungsionalitas dan tujuannya, dimulai dari Authentikasi. Autentikasi adalah proses untuk memverifikasi identitas pengguna. proses ini memastikan bahwa  pengguna yang mencoba mengakses aplikasi adalah pengguna yang terdaftar dan dapat dipercaya. Di Django, autentikasi biasanya melibatkan pengecekan kredensial seperti nama pengguna dan password melalui sistem autentikasi bawaan Django. Contoh umum adalah proses login, dimana pengguna harus memasukkan username dan password yang valid.

    Otorisasi adalah proses untuk menentukan apa yang diizinkan dilakukan oleh pengguna yang sudah terautentikasi. Setelah pengguna berhasil terautentikasi, Django akan menentukan akses atau hak apa yang dimiliki oleh pengguna tersebut, misalnya pengguna boleh melihat halaman admin atau tidak, mengedit data, atau mengakses fitur tertentu.

    Contoh tambahan, Disuatu Perusahaan, kita memiliki user **superuser** yang memiliki akses authorization penuh, ia bisa menetapkan apakah user dari departemen tertentu bisa mengakses laman tertentu seperti admin panel, atau fitur-fitur khusus misalnya sistem informasi departemen lain dalam perusahaan. tentu dengan fitur authorization dan authentication, ini bisa dilakukan dengan mudah.
  
  - #### 4️⃣ Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

    Dalam website berbasis django, Django mengingat pengguna yang telah login menggunakan **session**. Saat pengguna login, Django membuat entri di database yang menyimpan data sesi pengguna, seperti ID pengguna atau status login. Sebuah cookie berisi ID sesi dikirim ke browser pengguna, yang kemudian digunakan oleh server untuk mengidentifikasi sesi saat permintaan berikutnya diterima. Dengan cara ini, Django dapat "mengingat" pengguna antara permintaan, meskipun HTTP adalah protokol tanpa status (stateless).
    
    Selain mengelola sesi, di django juga terdapat **cookies** yang juga digunakan untuk berbagai kegunaan seperti menyimpan preferensi pengguna, melacak aktivitas, atau hal sederhana seperti mengingat item di keranjang belanja. Namun, tidak semua cookies aman secara default. Ada risiko seperti serangan XSS (Cross-Site Scripting) yang dapat mencuri cookies, dan CSRF (Cross-Site Request Forgery) yang dapat memanfaatkan cookies untuk melakukan tindakan tidak diizinkan. Oleh karena itu, cookies perlu diamankan lebih lanjut dengan menerapkan beberapa langkah seperti menggunakan flag HttpOnly, Secure, dan SameSite.
    
  #### ✅ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### ✅  Melakukan add-commit-push ke GitHub.

</details>




---




# Tugas 3: Implementasi Form dan Data Delivery pada Django


<details>
<summary>Click for more detail</summary>
<br>

## Deskripsi Tugas
Pada tugas ini, Saya akan menjalankan implementasi konsep data delivery serta menerapkan beberapa konsep yang telah dipelajari selama sesi tutorial.

## Checklist Tugas
#### ✅ Membuat input form untuk menambahkan objek model pada app sebelumnya.
- Membuat folder templates yang berisi base.html pada root folder dan menambahkannya pada `settings.py`.
  `base.html` ini akan menjadi template html project ini untuk kedepannya
- Melengkapi kerangka yang terdapat pada `base.html` untuk kebutuhan aplikasi main berupa atribut form untuk menerima input user dan mendisplay hasil dari input tersebut.
- Membuat file baru bernama `forms.py`. File ini akan berperan sebagai struktur form yang dapat menerima input data oleh user, berikut adalah isi dai `forms.py`.
```python
from django.forms import ModelForm
from main.models import CatEntry

class CatEntryForm(ModelForm):
    class Meta:
        model = CatEntry
        fields = ["name", "price", "age", "description", "species", "colour"]
```

#### ✅  Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
- Fungsi dalam format XML dan JSON menambahkan variable yang menyimpan objects pada item dan mereturn HttpResponse  yang isi parameternya adalah objects yang diserialisasi.
- Fungsi XML by ID dan JSON by ID sama implementasinya dengan XML dan JSON biasa namun untuk variable yang menyimpan objects menggunakan filter `(pk=id)` sehingga dapat diurutkan berdasarkan input. Berikut adalah kodenya
``` python
def show_xml(request):
    data = CatEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = CatEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = CatEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### ✅ Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
- Pada urls.py, tambahkan beberapa import terhadap setiap fungsi yang terdapat pada views.
  ``` python
  from main.views import show_home, create_cat_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
  ```
- Untuk fungsi create_cat_entry, XML, dan JSON tambahkan path yang sesuai.
```python
  path('create-cat-entry', create_cat_entry, name='create_cat_entry'),
  path('xml/', show_xml, name='show_xml'),
  path('json/', show_json, name='show_json'),
```
- Untuk fungsi XML by ID dan JSON by ID path ditambahkan `<str:id>` untuk mendapatkan data sesuai dengan id
```python
  path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
  path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

#### ✅ Menjawab beberapa pertanyaan berikut pada README.md pada root folder.

  - #### 1️⃣ Jelaskan mengapa kita memerlukan data delivery dalam - pengimplementasian sebuah platform?.
    Secara umum, dalam pengembangan platform di Django atau bahasa lainnya, data delivery adalah proses pengiriman data antara server (backend) dan client (frontend) atau bahkan antar server. Django sendiri memerlukan mekanisme ini karena beberapa hal seperti:

    - Komunikasi Client-Server: Pengguna berinteraksi melalui frontend, yang kemudian membutuhkan data dari backend untuk menampilkan informasi atau melakukan pemrosesan lebih lanjut.
    - Integrasi API: Jika platform membutuhkan integrasi API, misalnya REST API atau GraphQL, data delivery memungkinkan pengiriman dan penerimaan data dengan cara yang terstruktur.
    - Dynamic Web Pages: Untuk halaman-halaman dinamis yang sering berubah atau membutuhkan pemuatan data secara real-time, seperti dashboard atau feed, data delivery dibutuhkan untuk menjaga sinkronisasi antara frontend dan backend.
    - Keamanan: Data delivery juga memungkinkan penyaringan dan pengelolaan data yang masuk dari client, misalnya melalui form submission, agar sesuai dengan aturan keamanan platform.
  -  #### 2️⃣ Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?.
      Jika dilihat dari penggunaannya, `JSON` lebih banyak digunakan dan populer dibandingkan `XML` dalam pengiriman data, terutama dalam aplikasi web. Tetapi JSON tidak serta merta mengantikan XML sebagai format pengiriman data melainkan memberi alternatif yang lebih baik walaupun XML masih memiliki kegunaannya. Oleh karena itu, JSON mungkin lebih baik untuk kebanyakan penggunaan, tetapi tidak semua. Beberapa alasan mengapa JSON lebih populer dibanding XML ada beberapa alasan yaitu:

      - Lebih Ringan: JSON memiliki sintaks yang lebih sederhana dan pendek dibanding XML yang banyak di isi oleh Tag, sehingga ukuran data lebih kecil dibandingkan XML yang menggunakan banyak tag.
      - Human Readable: Sintaks JSON lebih mirip dengan objek JavaScript, membuatnya lebih mudah dibaca dan dipahami oleh manusia serta developer. selain itu JSON juga dirancang untuk bekerja dengan baik dalam JavaScript, sehingga ideal untuk aplikasi web modern yang umumnya menggunakan JavaScript di frontend.
      - Parsing Lebih Cepat: Parsing JSON cenderung lebih cepat dibandingkan XML karena JSON langsung mendukung format yang dipakai oleh kebanyakan bahasa pemrograman tanpa perlu tambahan konversi.
  
      Namun, XML tetap memiliki tempat dalam aplikasi tertentu, terutama yang membutuhkan struktur dokumen kompleks atau data dengan skema yang ketat.


  - #### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Dalam Django, method `is_valid()` digunakan untuk memvalidasi data yang dikirim melalui form dengan memeriksa apakah data memenuhi kriteria seperti tipe data, panjang teks, atau aturan khusus lainnya yang kita berikan. Jika data tidak valid, Django secara otomatis mengisi atribut `errors` pada form sehingga pengembang dapat memberikan feedback kepada pengguna mengenai kesalahan input. Selain itu, `is_valid()`juga memastikan bahwa hanya data yang aman dan valid yang diproses atau disimpan ke dalam database, menjaga  keamanan aplikasi.

  - #### 3️⃣ Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token (Cross-Site Request Forgery token) adalah token keamanan yang digunakan dalam Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang memanfaatkan sesi pengguna yang sudah diautentikasi untuk melakukan tindakan berbahaya di situs tanpa sepengetahuan mereka.

    Jika kita tidak menambahkan csrf_token pada form Django, situs kita rentan terhadap serangan CSRF, di mana penyerang bisa memanipulasi pengguna untuk mengirimkan permintaan yang tidak sah ke server, seperti mengubah data pengguna tanpa izin, melakukan transaksi atau aksi yang berbahaya atas nama pengguna, dan masih banyak lagi.

    #### Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    Penyerang bisa membuat sebuah situs palsu atau mengirimkan email yang mengandung form tersembunyi yang melakukan aksi ke server kita. Jika pengguna mengklik tautan atau membuka halaman tersebut dan mereka sudah login ke situs kita, browser mereka akan mengirimkan request tanpa disadari pengguna, membuat serangan itu berhasil.

    Menggunakan csrf_token memastikan bahwa request hanya valid jika berasal dari form yang dibuat oleh server, karena token tersebut unik untuk setiap sesi dan request, sehingga serangan ini dapat dicegah.


  - #### 4️⃣ Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### ✅ Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
### Mengakses XML
![](/img/XML.png)
### Mengakses JSON
![](/img/JSON.png)
### Mengakses XML dengan ID tertentu
![](/img/XML_by_ID.png)
### Mengakses JSON dengan ID tertentu
![](/img/JSON_by_ID.png)

#### ✅  Melakukan add-commit-push ke GitHub.

</details>




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
