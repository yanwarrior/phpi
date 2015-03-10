# phpi
PHP Interactive Shell, dengan PHP interactive shell kita bisa 'mencoba' memasukkan kode apa saja mengenai PHP dan hasilnya langsung keluar ketika di ketik perintah `phpi:run`. PHP Interactive shell ini juga berfungsi untuk menampilkan keluaran dari kode PHP yang kita buat. Selain itu, PHP Interactive Shell ini juga bisa dipakai untuk mencari kesalahan kode kita, mencoba apakah satu baris kode/perintah yang kita buat akan berjalan semestinya atau tidak tanpa perlu mencobanya dengan membuat file dan menjalankannya di browser.

# required
* Python 2.7
* Py2exe for windows
* PHP 5

# Package Optional
jika ingin di jadikan exe, maka perlu package python `py2exe`. sudah di sediakan `setup.py` nya. tinggal mengetik perintah :
```shell
python setup.py py2exe
```

# Cara Pakai Langsung
## For Windows
cara menggunakan PHPI langsung (dengan asumsi `require` terpenuhi) adalah dengan mengeset `System Environment Variable` ke direktori PHPI yang sudah di unduh.
## For Linux
dengan membuat `symbolic link`.

# Setting Path PHP
```batch
PHP Interactive Shell Version 1.0.0 (Yanwar Solahudin)
please typing 'phpi:help' for help.

phpi-> phpi:path <enter>
set php path: C:\xampp\php\php.exe
```

#Example phpi:run
###Hello PHPI
```php
phpi-> echo "hello PHPI";
phpi-> phpi:run
hello PHPI
phpi->
```

###Longer code examples
```php
phpi-> class Person {
phpi->
phpi->  private $name;
phpi->  private $age;
phpi->  private $friends;
phpi->
phpi->  public function __construct($name, $age)
phpi->  {
phpi->      $this->name = $name;
phpi->      $this->age = $age;
phpi->  }
phpi->
phpi->  public function set_friend()
phpi->  {
phpi->      $this->friends = array(
phpi->          "junox", "felin", "rio", "irwan"
phpi->      );
phpi->  }
phpi->
phpi->  public function get_data_person()
phpi->  {
phpi->      return array($this->name, $this->age, $this->friends);
phpi->  }
phpi->
phpi-> }
phpi->
phpi-> $person = new Person("yanwar", 22);
phpi-> $person->set_friend();
phpi-> print_r($person->get_data_person());
```
running code :
```php
phpi-> phpi:run 
```
result :
```php
Array
(
    [0] => yanwar
    [1] => 22
    [2] => Array
        (
            [0] => junox
            [1] => felin
            [2] => rio
            [3] => irwan
        )

)

phpi->
```

#Example phpi:line
menampilkan semua code yang sudah Anda tulis.
```php
phpi-> $data = array(
phpi->  "name" => array("yanwar", "junox", "faris"),
phpi->  "age" => array(22, 19, 26),
phpi-> );
phpi->
phpi-> $data_json = json_encode($data);
phpi->
phpi-> echo $data_json;
phpi->
phpi-> phpi:line
```
result :
```
<?php
[0]     $data = array(
[1]             "name" => array("yanwar", "junox", "faris"),
[2]             "age" => array(22, 19, 26),
[3]     );
[4]
[5]     $data_json = json_encode($data);
[6]
[7]     echo $data_json;
[8]
?>

phpi->
```
#Example phpi:save
menyimpan script yang sudah Anda tulis menjadi file.
```php
phpi-> phpi:save
Directory: D:
Filename: save_example.php
check file in : D:/save_example.php
phpi->
```

#Example phpi:out
mengeluarkan atau menghapus baris kode dengan posisi line nya.
```php
phpi-> echo "phpi is a php interactive shell";
phpi-> echo "<br>";
phpi-> echo "\n";
phpi->
phpi-> phpi:line

<?php
[0]     echo "phpi is a php interactive shell";
[1]     echo "<br>";
[2]     echo "\n";
[3]
?>
```
kita akan menghapus posisi line `1`
```php
phpi-> phpi:out
out code in line > 1
phpi->
```
result :
```php
phpi-> phpi:line
<?php
[0]     echo "phpi is a php interactive shell";
[1]     echo "\n";
[2]
?>

phpi->
```
#Example phpi:clear
Mereset semua code menjadi kosong, kembali seperti sedia kala.
```php
phpi-> phpi:clear
phpi-> phpi:line

<?php
?>

phpi->
```

#Example phpi:repair
memperbaiki code pada line tertentu.
```php

phpi-> $name = "yanwar";
phpi-> $age = 22;
phpi-> $is_awesome = true;
phpi->
phpi-> echo $is_awesomseeeee;
phpi->
phpi-> phpi:line

<?php
[0]     $name = "yanwar";
[1]     $age = 22;
[2]     $is_awesome = true;
[3]
[4]     echo $is_awesomseeeee;
[5]
?>

phpi-> phpi:repair
repair number > 4
insert code > echo "yes " . $name . " is a " . $is_awesome . " awesome";
phpi-> phpi:line

<?php
[0]     $name = "yanwar";
[1]     $age = 22;
[2]     $is_awesome = true;
[3]
[4]     echo "yes " . $name . " is a " . $is_awesome . " awesome";
[5]
?>
```

#Example phpi:toclear
menghapus code dari baris `n` sampai ke `n`..
```php
phpi-> echo "yes i am yanwar";
phpi-> echo "i'm programmer, i have no live";
phpi-> echo "i love mamah";
phpi-> echo "and i love papah";
phpi-> echo "yes, i love my parents";
phpi->
phpi-> phpi:line

<?php
[0]     echo "yes i am yanwar";
[1]     echo "i'm programmer, i have no live";
[2]     echo "i love mamah";
[3]     echo "and i love papah";
[4]     echo "yes, i love my parents";
[5]
?>

phpi-> phpi:toclear
from: 1
to: 3
phpi-> phpi:line

<?php
[0]     echo "yes i am yanwar";
[1]     echo "yes, i love my parents";
[2]
?>

phpi->
```

#Example phpi:server
menjalankan script yang Anda tulis untuk ditampilkan di browser.
```php

phpi-> echo "<h1>Hello PHPI</h1>";
phpi-> echo "<p>this is my blog PHPI</p>";
phpi->
phpi-> phpi:server
PHP 5.6.3 Development Server started at Wed Mar 11 02:24:07 2015
Listening on http://localhost:8000
Document root is C:\Users\yanwar
Press Ctrl-C to quit.
```
buka URL : `http://localhost:8000` lihat hasilnya.

#Example help
```php

phpi-> phpi:help



        * phpi:run     > running script in interactive shell
        * phpi:exit    > stop interactive shell
        * phpi:line    > show all your code in interactive shell
        * phpi:clear   > reset interactive
        * phpi:out     > remove code based index in interactive shell
        * phpi:repair  > repair line code in interactive shell
        * phpi:path    > setting path php
        * phpi:info    > About PHPI
        * phpi:save    > Save Script in your directory
        * phpi:toclear > Clear code from ... to ...
        * phpi:server  > Running Script to server
        
```
#Example info
```php
phpi-> phpi:info

<?phpi
     PHPI - PHP Intrecative
     By Yanwar Solahudin
     Version 1.0.0
     Backend in Python Console
?>

phpi->
```
